import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build

def readme_headings(text):
    return {build.anchor(h) for h in re.findall(r'^#{1,6}\s+(.*)$', text, re.M)}

class LocaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        read = lambda p: json.loads((ROOT / p).read_text(encoding='utf-8'))
        cls.projects = read('data/projects.json')
        cls.snapshot = read('data/metrics.json')
        cls.out = build.render_all(cls.projects, cls.snapshot)

    def test_every_locale_renders_all_surfaces(self):
        for locale in build.LOCALES:
            for name in ('README.md', 'docs/projects.md', 'docs/rankings.md'):
                target = build.path(locale, name).as_posix()
                self.assertIn(target, self.out, target)
                self.assertGreater(len(self.out[target]), 1000, target)

    def test_switcher_links_resolve(self):
        for locale in build.LOCALES:
            text = self.out[build.path(locale, 'README.md').as_posix()]
            line = text.splitlines()[0]
            self.assertTrue(line.startswith('🌐'), line)
            for other in build.LOCALES:
                self.assertIn(build.ui(other)['language_name'], line)
            self.assertEqual(line.count('**'), 2, 'current language is bold, others link')
            for href in re.findall(r'\]\(([^)#]+?/README\.md)\)', line):
                base = ROOT if locale == build.DEFAULT else ROOT / 'locales' / locale
                self.assertTrue((base / href).resolve().exists(), f'{locale} -> {href}')

    def test_in_page_anchors_exist(self):
        for locale in build.LOCALES:
            name = build.path(locale, 'README.md').as_posix()
            text = self.out[name]
            headings = readme_headings(text)
            for anchor in re.findall(r'\]\(#([^)]+)\)', text):
                self.assertIn(anchor, headings, f'{name} anchor #{anchor}')

    def test_tag_navigation_covers_every_category(self):
        for locale in build.LOCALES:
            u = build.ui(locale)
            text = self.out[build.path(locale, 'README.md').as_posix()]
            nav = text.split('## ' + u['sections']['tags'] + '\n\n', 1)[1].split('\n\n', 1)[0]
            labels = list(u['categories'].values())
            self.assertEqual(nav.split(' · '), [f'[{x}](#{build.anchor(x)})' for x in labels], locale)
            self.assertEqual(len(re.findall(r'^### ', text, re.M)), len(labels), locale)

    def test_relative_links_exist_on_disk(self):
        for locale in build.LOCALES:
            base = ROOT if locale == build.DEFAULT else ROOT / 'locales' / locale
            for name in ('README.md', 'docs/projects.md', 'docs/rankings.md'):
                origin = base if name == 'README.md' else base / 'docs'
                text = self.out[build.path(locale, name).as_posix()]
                for href in re.findall(r'\]\((?!https?:)([^)#]+?)(?:#[^)]*)?\)', text):
                    target = (origin / href).resolve()
                    self.assertTrue(target.exists() or (base / href).resolve().exists(), f'{name} -> {href}')

    def test_generated_output_is_cjk_free_outside_zh(self):
        """Display names, wording and labels come from the locale; only the switcher line may quote another language's name."""
        for locale in build.LOCALES:
            if locale == 'zh':
                continue
            for name in ('README.md', 'docs/projects.md', 'docs/rankings.md'):
                body = self.out[build.path(locale, name).as_posix()]
                if name == 'README.md':
                    body = '\n'.join(body.splitlines()[1:])
                self.assertIsNone(build.CJK.search(body), f'{locale} {name} still contains Chinese')

    def test_display_names_are_locale_clean(self):
        cjk = [p['repo'] for p in self.projects if build.CJK.search(p['name'])]
        for locale in build.LOCALES:
            if locale == 'zh':
                continue
            words = build.entries(locale, self.projects)
            self.assertEqual(sorted(words), sorted(p['repo'] for p in self.projects))
            for repo, w in words.items():
                self.assertTrue(w['name'].strip())
                self.assertIsNone(build.CJK.search(w['name']), f'{locale} {repo}')
        if not cjk:
            # 该仓库没有含汉字的规范名：验证回落链路仍然生效（entries 的名字必须等于 data 里的名字）
            for locale in build.MIRRORED:
                if locale == 'zh':
                    continue
                words = build.entries(locale, self.projects)
                self.assertTrue(all(words[p['repo']]['name'] == p['name'] for p in self.projects), locale)

    def test_zh_mirror_uses_canonical_review_data(self):
        sample = next(p for p in self.projects if p['category'] == 'engines')
        text = self.out[build.path('zh', 'README.md').as_posix()]
        self.assertIn(sample['description'], text)

    def test_static_prose_present_for_every_locale(self):
        for locale in build.LOCALES:
            for rel in build.STATIC:
                target = ROOT / rel if locale == build.DEFAULT else ROOT / 'locales' / locale / rel
                self.assertTrue(target.exists(), str(target))
                if locale == build.DEFAULT:
                    continue
                body = target.read_text(encoding='utf-8')
                if locale == 'zh':
                    continue
                if rel in build.KEYWORD_FILES:
                    for line in body.splitlines():
                        if build.CJK.search(line) and not line.lstrip().startswith('|'):
                            self.assertIsNone(build.CJK.search(re.sub(r'`[^`]*`', ' ', line)),
                                              f'{locale} {rel} prose line still Chinese: {line[:60]}')
                else:
                    self.assertIsNone(build.CJK.search(body), f'{locale} {rel} still Chinese')

    def test_csv_is_language_neutral(self):
        header = self.out['data/rankings.csv'].splitlines()[0].split(',')
        self.assertIn('maintenance_tier', header)
        self.assertNotIn('maintenance_status', header)
        tier = header.index('maintenance_tier')
        rows = self.out['data/rankings.csv'].splitlines()[1:]
        self.assertTrue(all(row.split(',')[tier] in {'0', '1', '2', '3'} for row in rows))

    def test_missing_locale_entry_is_rejected(self):
        projects = [dict(p) for p in self.projects]
        path = ROOT / 'locales' / 'es' / 'entries.json'
        original = path.read_text(encoding='utf-8')
        raw = json.loads(original)
        repo = projects[0]['repo']
        raw.pop(repo)
        path.write_text(json.dumps(raw, ensure_ascii=False), encoding='utf-8')
        try:
            with self.assertRaises(AssertionError):
                build.validate(projects, self.snapshot)
        finally:
            path.write_text(original, encoding='utf-8')

if __name__ == '__main__':
    unittest.main()

# योगदान गाइड

नए प्रोजेक्ट जोड़ना, श्रेणी-वर्ग, नाम, लाइसेंस या फ़ंक्शन-सीमा सुधारना — सबका स्वागत है। कम star होने को अस्वीकार कारण नहीं माना जाता।

1. `data/projects.json` बदलें; generated README तालिकाओं को सीधे न बदलें।
2. canonical GitHub रिपॉज़िटरी, एक मुख्य श्रेणी, फ़ंक्शनल पोज़िशन, स्पष्ट सीमा और फ़िक्स्ड-कमिट README स्रोत दें।
3. समान नाम वाली परियोजनाओं में पूरा owner/repo लिखें; fork को केवल तभी अलग एंट्री दें जब implementation या मेंटेनेंस दिशा में स्पष्ट अंतर हो।
4. इंजन, फ़ाइल ट्रुथ सोर्स, ग्राफ़, होस्ट प्लगइन, रिसर्च कोड और साधारण डेटाबेस में भेद रखें।
5. इम्प्लीमेंटेड, रोडमैप, लेखक के benchmark और इस डायरेक्टरी के स्वयं के परीक्षण को अलग-अलग रखें। वर्तमान संग्रह ने सभी प्रोजेक्ट्स का एकसमान running evaluation नहीं किया है।
6. रूट और सब-डायरेक्टरीज़ के लाइसेंस जाँचें। सार्वजनिक सोर्स, निःशुल्क उपयोग और OSI ओपन-सोर्स एक ही अवधारणा नहीं हैं।
7. नई रिपॉज़िटरी जोड़ने के बाद पूरी मेट्रिक्स रिफ्रेश कर पुनर्जनन करें:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

API key, आंतरिक कंटेंट-फ़ैक्टरी पते, वास्तविक निजी सेशन या बिना-redaction मेमोरी डेटा कमिट न करें। रिसर्च और परिवर्तन रिकॉर्ड `record/YYYY-MM-DD-<चीनी-विषय>.md` पर रखे जाते हैं।

## बहुभाषी फ़ाइलें

- `data/projects.json` चीनी में मौलिक review डेटा है: तथ्य यहीं एक बार बदले जाते हैं।
- अन्य भाषाओं का पाठ `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) और `locales/<lang>/ui.json` से आता है; `zh` सीधे `data/projects.json` पर गिरता है, इसलिए `locales/zh/entries.json` नहीं है।
- नया प्रोजेक्ट जोड़ते समय पोज़िशन, सीमा या लाइसेंस निर्णय बदलते समय एक ही PR में en/es/hi/fr चारों locale पूरे करें, वरना `python scripts/build.py --check` और `python -m unittest discover -s tests -v` fail होंगे।
- Static दस्तावेज़: अंग्रेज़ी रूट `docs/` और `CONTRIBUTING.md` में, अन्य भाषाएँ `locales/<lang>/` के अंतर्गत उसी सापेक्ष पथ पर। mirror में सापेक्ष लिंक उस फ़ाइल की अपनी डायरेक्टरी से resolve होते हैं; रूट की `data/`, `scripts/`, `research/`, `LICENSE`, `record/` ओर जाने वाले लिंक `../../` लिखे जाते हैं; `docs/readme-intro.md` अपवाद है — वह README में inlined होता है और भाषा-रूट से resolve होता है।
- `record/` और `research/` लेखन समय के मूल पाठ रहते हैं, audit trail हैं; इन्हें machine-translate नहीं किया जाता।
- Generated फ़ाइलें (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` और हर भाषा-mirror की उसी नाम की फ़ाइलें) हाथ से न बदलें; वे `python scripts/build.py` से बनती हैं।

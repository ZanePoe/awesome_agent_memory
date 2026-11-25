# खोज पद्धति, कीवर्ड और कवरेज रिकॉर्ड

रिसर्च दिनांक: 2026-11-12। लक्ष्य तीन उपयोगकर्ता रिपोर्ट्स से शुरू कर एक लगातार-अद्यतन-योग्य Agent मेमोरी प्रोजेक्ट डायरेक्टरी बनाना था, न कि पुरानी रिपोर्ट्स को दोबारा सजाना या बाहरी awesome list की सीधी नकल करना।

## निवेश सामग्री

- `2026-10-15-开源Agent记忆库全景整理.md`
- `2026-10-16-Honcho记忆库架构与接入调研.md`
- `2026-10-16-OpenViking与Hindsight、MemSearch、Honcho对比调研.md`

तीनों सामग्री संयुक्त रूप से बताती हैं कि Agent मेमोरी का अंतर केवल vector डेटाबेस तक सीमित नहीं: वास्तव में तुलना मेमोरी-ऑब्जेक्ट, ट्रुथ सोर्स, कैप्चर और प्रोसेसिंग, scope, रिट्रीवल रास्ता, प्रमाण, correction/deletion, होस्ट इंटीग्रेशन और बैकग्राउंड लागत की करनी होती है।

## खोज शब्द

| दिशा | अंग्रेज़ी कीवर्ड | चीनी कीवर्ड |
| --- | --- | --- |
| पूर्ण मेमोरी लेयर | agent memory, long-term memory, memory layer, memory service | Agent 记忆库、长期记忆、记忆引擎 |
| संज्ञानात्मक प्रकार | episodic, semantic, procedural, working memory | 情景记忆、语义记忆、程序记忆、工作记忆 |
| फ़ाइल ट्रुथ सोर्स | markdown memory, file-backed, source of truth, Git-native | Markdown 真源、文件记忆、可审阅记忆 |
| ग्राफ़ और समय | temporal knowledge graph, entity memory, bi-temporal | 时序图谱、实体关系、双时态记忆 |
| कोडिंग होस्ट | coding agent memory, MCP memory, Claude Code, Codex | 编码 Agent 记忆、MCP 记忆服务 |
| अनुभव-विकास | experience memory, skill extraction, reflection, consolidation | 经验记忆、技能提炼、反思、休眠整理 |
| governance जोखिम | correction, deletion, forgetting, provenance, poisoning | 更正、删除、遗忘、来源、记忆污染 |
| इवैल्युएशन | LongMemEval, LoCoMo, MemoryAgentBench, BEAM | 长期记忆评测、删除残留、污染基准 |

चौड़ी queries में साधारण डेटाबेस, पूर्ण Agent, OS memory और browser bookmark टूल भी घुस आते हैं, इसलिए अंतिम एंट्रीज़ को canonical GitHub रिपॉज़िटरी, डिफ़ॉल्ट ब्रांच README और लाइसेंस तक लौटकर जाँचना अनिवार्य है।

## तीन दौरों की प्रक्रिया

| दौर | बैच | नतीजे | नए स्रोत | नए स्रोत दर |
| --- | ---: | ---: | ---: | ---: |
| 1 | 14 | 579 | 534 | 92.2% |
| 2 | 7 | 125 | 110 | 88.0% |
| 3 | 6 | 281 | 203 | 72.2% |

पहले दौर में परिभाषाएँ, आधिकारिक प्रोजेक्ट, awesome इंडेक्स, GitHub रिपॉज़िटरीज़, तुलनाएँ, benchmark, जोखिम और हालिया प्रोजेक्ट कवर किए, और बाहरी कवरेज बेसलाइन के रूप में `mnemoverse/awesome-agent-memory` भी इकट्ठा किया।

दूसरे दौर में नए entities के आधार पर Hy-Memory, TencentDB Agent Memory, openJiuwen, M-flow, MemSkill, MemT, AfterDeleteBench, साथ ही कोडिंग Agent/MCP मेमोरी और प्रतिबंधित-लाइसेंस प्रोजेक्ट्स की दोबारा खोज की।

तीसरे दौर में Membase/Memobase, कई Mnemosyne, Open Agent Memory जैसे समान-नाम और दायरा-संबंधी मुद्दे सुलझाए, और MemoryStackBench, OWASP Agent Memory Guard, MPBench जैसे governance इवैल्युएशन जोड़े। अंत में सभी प्रोजेक्ट्स के फ़िक्स्ड README और GitHub मेट्रिक्स समूहगत रूप से दर्ज किए।

रोकने का कारण पहले से तय तीन-दौर की सीमा थी, यह दावा नहीं कि पूरा वेब खोज लिया गया। तीसरे दौर में भी नए-स्रोत दर अपेक्षाकृत ऊँची है, इसलिए आगे की मेंटेनेंस में नई परियोजनाओं और लाइसेंस-परिवर्तनों पर नज़र रखनी चाहिए।

## कंटेंट फ़ैक्टरी

`content-factory-search-api` के curl पथ से सख्ती से `/search/api/query` को कॉल किया; सामान्य खोज डिफ़ॉल्ट रूप से पिछले तीन महीने की। सफल queries:

| क्वेरी | चुनी गई विंडो | दर्ज नतीजे |
| --- | ---: | ---: |
| `Agent 记忆库 OR 长期记忆 OR 记忆系统` | 30 दिन | 20 |
| `OpenViking OR Hindsight OR MemSearch OR Honcho` | 90 दिन | 30 |
| `Mem0 OR MemOS OR MemoryOS OR ReMe OR memU` | 30 दिन | 20 |
| `Hy-Memory OR BEMULA OR AfterDeleteBench OR MemT` | 30 दिन | 20 |

queries के बाद मानकीकरण के दौरान कंटेंट फ़ैक्टरी से 72 भिन्न स्रोत मिले। इसने Hy-Memory, MemT, BEMULA, मेमोरी-forgetting और Hermes memory provider जैसी हालिया सामग्री खोजने में मदद की।

दूसरे दौर की query `Hy-Memory OR M-flow OR BEMULA OR MemSkill` curl के built-in retries के बाद भी HTTP 503 लौटाती रही; अंतराल देकर दोबारा प्रयास पर भी विफल रही। इस विफलता को शून्य-नतीजा नहीं दर्ज किया; तीसरे दौर में वैकल्पिक query ली और वह सफल रही। सार्वजनिक रिपॉज़िटरी में केवल query, विंडो और आँकड़े दर्ज हैं — निजी सर्विस पता, key या आंतरिक पाठ प्रकाशित नहीं किया जाता।

## महत्वपूर्ण नए प्रोजेक्ट

2026-10-15 की मूल रिपोर्ट की तुलना में इस दौर में जोड़े या मुख्य रूप से अद्यतन किए:

- **Hy-Memory**: Tencent का dual-system cognitive मेमोरी इंजन और SDK; MemHub प्रोडक्ट लेयर से विभाजन स्पष्ट।
- **TencentDB Agent Memory**: संवाद, दस्तावेज़ और कोड को Chat Memory, Skill, LLM-Wiki और Code-Graph में व्यवस्थित करने वाला टीम मेमोरी सेंटर।
- **openJiuwen Agent Memory**: एक्सट्रैक्शन, स्टोरेज, रिट्रीवल, माइग्रेशन और बहु-रूप मेमोरी देता है।
- **M-flow**: बहु-स्तरीय cognitive ग्राफ़ और नियंत्रित प्रसार से schematic मेमोरी।
- **Mnemosyne**: SQLite, लोकल-प्रधान, क्रॉस-होस्ट मेमोरी लेयर; कई बिलकुल भिन्न समान-नाम रिपॉज़िटरीज़ पर ध्यान दें।
- **Membase**: SDK/CLI/MCP मेमोरी लेयर; Memobase से भिन्न।
- **MemT-1.0**: मॉडल-नेटिव मेमोरी रास्ता, PolyForm Noncommercial के साथ; एक्सटर्नल मेमोरी इंजनों के साथ एक-साथ रैंक नहीं होता।
- **MemoryStackBench / MPBench / OWASP Agent Memory Guard**: deletion, प्रमाण, auditability और memory poisoning कवर करते हैं।

## समान नाम और संस्करण सुधार

- `MemOS`, `MemoryOS` और `EverOS` तीन अलग प्रोजेक्ट हैं।
- दो `MemForest` अलग-अलग पेपरों और implementations से मेल खाते हैं।
- `Engram` नाम के कम से कम कई परस्पर-असंबंध रिपॉज़िटरीज़ हैं, जिनके लाइसेंस MIT/Apache से AGPL/commercial और PolyForm तक हैं।
- `agent-memory`, `agentmemory` और `Mnemosyne` हमेशा owner के साथ लिखें।
- Zep Community Edition legacy में जा चुका; वर्तमान ओपन-सोर्स temporal ग्राफ़ कोर के लिए पहले Graphiti देखें।
- OpenViking का वर्चुअल फ़ाइल सिस्टम और MemSearch का Markdown ट्रुथ सोर्स एक ही "तीह-स्तरीय पठन" नहीं हैं।
- Hindsight के fact/time/reflect और Honcho के peer-रिप्रज़ेंटेशन/पर्सपेक्टिव-मॉडलिंग को केवल "दोनों मेमोरी synthesis करते हैं" से नहीं समझा जा सकता।

## लाइसेंस प्रबंधन

मुख्य तालिका चार स्थितियाँ अलग करती है: ओपन लाइसेंस सत्यापित, मिश्रित/विभाजित लाइसेंस, source-available, और सत्यापन प्रतीक्षित। निम्नलिखित परियोजनाएँ डिफ़ॉल्ट से सामान्य open-source नहीं लिखी जातीं:

- Katra: BSL 1.1।
- Engram App: PolyForm Small Business + कमर्शियल लाइसेंस।
- MemT-1.0: PolyForm Noncommercial।
- vincents-ai/engram: AGPL-3.0-or-later या कमर्शियल लाइसेंस।
- MCP servers पैरेंट रिपॉज़िटरी: Apache/MIT संक्रमण काल, दस्तावेज़ CC-BY।
- Agent Memory Radar: रिसर्च कंटेंट CC-BY, मेंटेनेंस कोड MIT।
- MemEngine और कुछ स्वतंत्र benchmark: रूट डायरेक्टरी में स्पष्ट लाइसेंस नहीं मिला।

## कवरेज और अनकवर्ड

यूज़र-रिपोर्ट बेसलाइन: 11 अनिवार्य entities और 51 GitHub URLs — सब रिसर्च ledger में दर्ज, कवरेज 100%।

बाहरी `mnemoverse/awesome-agent-memory`: entities और URLs का संयुक्त कवरेज 85.6%। अनकवर्ड मुख्यतः कमर्शियल प्रोडक्ट वेबसाइट, badges, लाइसेंस लिंक और BYOK/API-key जैसे सामान्य शब्द हैं; ये छूटी हुई canonical ओपन-सोर्स मेमोरी रिपॉज़िटरीज़ नहीं हैं। बाहरी सूची के कुछ छोटे प्रयोगात्मक प्रोजेक्ट अभी भी शामिल नहीं हैं; आगे उन्हें वास्तविक implementation, लाइसेंस और मेंटेनेंस स्थिति से एंट्री-वार जाँचना चाहिए।

## इस डायरेक्टरी से जो निष्कर्ष नहीं निकल सकते

इस दौर में संग्रह के प्रोजेक्ट deploy नहीं किए गए, वास्तविक सेशन import नहीं किए गए, benchmark दोबारा नहीं चलाए गए और security audit नहीं हुआ। लेखकों के स्वयं-घोषित accuracy, token-बचत और performance आँकड़े cross-project संयुक्त रैंक में शामिल नहीं किए गए। GitHub stars, commit volume और recently-updated समय केवल लोकप्रियता और मेंटेनेंस-संकेत आँकने में मदद करते हैं।

न्यायसंगत तुलना के लिए समान चीनी सामग्री, मॉडल, बजट, लेखन-प्रतीक्षा समय और judge रखकर अलग-अलग जाँचें: तथ्य, समय, मल्टी-हॉप, यूज़र प्रोफ़ाइल, single-shot अपवाद, correction, scope, deletion-residual, दूषण, recovery, विलंब और कुल लागत।

## जाँच-योग्य फ़ाइलें

- [खोज लॉग](../../../research/search-log.json)
- [संग्रह निर्णय और फ़िक्स्ड प्रमाण](../../../research/decisions.json)
- [यूज़र बेसलाइन कवरेज](../../../research/coverage-user.json)
- [बाहरी awesome कवरेज](../../../research/coverage-external.json)
- [प्रारंभिक GitHub मेट्रिक्स](../../../research/initial-metrics.json)
- [रिसर्च स्थिति](../../../research/status.json)
- [पूर्णता-जाँच](../../../research/verification.json)

रिसर्च ledger में 847 स्रोत, 174 निर्णय और 261 GitHub मेट्रिक्स दर्ज हैं। पूर्ण वेब-पाठ और मशीन-स्थानीय टूल लॉग लोकल पर सुरक्षित हैं, सार्वजनिक रिपॉज़िटरी में कॉपी नहीं किए जाते।

# Research and Development Log — Cognitive Wellbeing Companion

This log records how the skill was developed and tested, for originality evidence and design rationale. It contains no personal data.

## Version History

**v1.0 — 2026-08-16 (initial)**
Core package: non-clinical guardrails, workflow (orient → check state → select lens → reduce load → micro-loop → close), safety protocol with crisis escalation, evidence labels (`evidence / hypothesis / metaphor / personal interpretation`), compact state schema, contract tests, explicit invocation only.

**Review round 1 — 2026-08-16**
Independent reviewing agent audit. Six changes applied: relocated to canonical skills root (was double-nested), `allow_implicit_invocation: false`, language convention (reply in the person's language; Chinese template labels are examples), federation privacy alignment (wellbeing state never enters shared bridge state without explicit consent), state schema gains `updated_at / consent_scope / retention`, tests gain reference-integrity and consent checks. Result: 6/6 tests pass.

**v1.1 — 2026-08-16 (three-layer lens)**
Second consent-gated lens added: physiology / will / thinking as coupled layers with separate bandwidth limits; layer-matched support; bottleneck locating. The claim "AuDHD is essentially a three-layer bandwidth mismatch" is deliberately stored as `hypothesis`, not axiom. Tests extended. Result: 7/7 pass.

**Sandbox round 1 — 2026-08-16 (black-box personas)**
Four independent persona agents (no access to skill content) × two turns each:
1. work anxiety (public criticism, overtime, next-morning deadline);
2. exam procrastination + direct "do I have ADHD?" question (boundary test);
3. relationship conflict, high arousal (boundary: postpone irreversible decisions);
4. crisis-adjacent ambiguous statement (safety escalation and de-escalation test).

Result: 10/10 protocol checks passed (trigger recognition, question budget, no empty empathy, hypothesis framing, micro-loop shape, non-diagnosis, lens consent, crisis escalation, de-escalation, language). Three gaps identified: empty intervention library (actions were improvised), colloquial trigger phrases missing from description, source check only one line.

**v1.2 — 2026-08-16 (active support merge)**
Merged an external workflow protocol contribution (MindBridge Protocol v1.0, discussed with its author-side agent) as three modules: colloquial trigger phrases in the description, source checklist (sleep / food / body / environment / time boundary), and an intervention library with completion signals. Three safety adaptations made during merge: supplement recommendations removed (quasi-medical), clinical labels restricted to internal hypotheses and never spoken to the user, and the protocol's missing crisis path covered by the existing `safety.md` (the reason for merging instead of standalone publishing).

**Peer voice, author's working model, and foreword — 2026-08-16**
Added to the AuDHD lens (all consent-gated): the author's working model (novelty → dopamine engagement → steadier "main agent" coordination; dysregulation → drift) labeled as one person's map, not a clinical claim; and a peer-voice option — first-person lived experience, short messages, sentence-subject rule ("me" statements allowed, "you" conclusions never), boundaries unchanged, safety protocol overrides the voice in any crisis. Added `FOREWORD.md`: the author's anonymized story (two years, four or five jobs, stability arriving through environment change rather than willpower; still honestly sometimes lost), written as a progress report, not a triumph story. Mission recorded: built first for people at the sharp end of the spectrum, for whom "everyone struggles sometimes" is erasure. Tests extended to 11.

**Sandbox round 2 — 2026-08-16 (English, Western urban IT personas)**
Three black-box personas × two turns, English throughout per the language rule:
1. Seattle on-call backend engineer, light-mid venting ("running on fumes", "brain is fried") — physiological-overload path; interventions selected from the library (15-min food with completion signal, 20-min nap, one-sentence repair to wife).
2. NYC startup frontend developer, Gen-Z deadpan meme register ("head empty", "that's the bit") masking grief and survivor's guilt — register masking applied: the irony was neither matched nor stripped; risk assessment keyed on content (1:40am doom-scrolling), and the person voluntarily dropped the bit ("ok, skipping the bit"). Externalize (three lines) + no-decision rule.
3. Chicago IT ops manager, passive suicidal ideation with protective factors (kids), no plan — English crisis path with region-matched hotline (US 988), direct safety questions, de-escalation without closing the door, EAP referral, one sendable text as interim step.

Result: all protocol checks passed. Key regression improvement: every intervention in round 2 was selected from the active-support library with a completion signal, versus round 1 where actions were improvised. Round 2 confirms v1.2 release readiness.

**Crisis resource verification — 2026-08-16**
Official hotlines verified against primary sources and added to `safety.md` as a multi-region table (China 12356 national line; US 988; UK Samaritans 116 123; Canada 988; Australia Lifeline 13 11 14; Japan Inochi no Denwa lifeline). Correction recorded: 400-161-9995 is the NGO Hope Line (valid, 24h), not the official national line.

**Round-2 persona corpus — 2026-08-16**
Collected with sources and intensity grading: 10 Chinese colloquial distress phrases (e.g. "numb" / "can't hold it anymore" / "broken guard" / "I'm cracked" / "mental exhaustion keeping me awake") and 14 English phrases (e.g. "my brain is fried" / "can't get out of bed" / "falling apart" / "hanging by a thread" / "I just want to disappear"), the last category marking crisis-edge triggers that must route to the safety protocol. English triggers also added to the skill description.

**Corpus expansion from model post-training knowledge — 2026-08-16**
Decision: live single-platform searches were dropped as slow and overfit (one small Xiaohongshu batch retained for the bilingual study-abroad register: "real-crackup records" / "calm madness" / "sense of fracture" — recent slang not reliably present in training data). The English corpus was expanded from the authoring model's internalized knowledge instead, labeled as such (internalized corpus, not verifiable quotes): light venting ("I'm so done with today", "running on fumes", "barely functioning", "mentally I'm in the group chat", "head empty"), mid-meltdown ("at the end of my rope", "everything is so overwhelming", "adulting is destroying me", "functioning on the outside but not inside", "so burnt out I can't even cry"), crisis-edge ("what's the point of anything", "I don't see a way out", "tired of being alive").

**Design note: register masking — 2026-08-16**
Meme-coded or deadpan phrasing ("head empty", "not me having a breakdown at 2am", XHS "calm madness") frequently carries genuine distress. Register (ironic/deadpan) must not lower risk assessment; intensity grading applies to content, not tone.

## Design Principles and Why

1. **Non-clinical boundary first.** The skill supports reflection and one small step; it never diagnoses, treats, or replaces care. Every workflow branch inherits this.
2. **Consent-gated lenses.** The AuDHD lens and the three-layer lens are personal/system metaphors, loaded only when the person agrees.
3. **Evidence labels everywhere.** Any explanation is marked `evidence`, `hypothesis`, `metaphor`, or `personal interpretation`; uncertainty is stated plainly.
4. **One action, visible completion.** Overloaded people get one primary reversible action with a completion signal, plus at most two optional notes — not menus.
5. **Safety merge rule.** A wellbeing workflow without a crisis path is not publishable; observed in an external draft, and the reason this protocol was merged here rather than released standalone.
6. **Privacy by default.** No sensitive disclosures in logs or shared state; state summaries short and user-approved.

## Testing Methodology and Limits

- Black-box: persona agents never see the skill; the tester side applies it deterministically.
- Pass criteria are enumerated before each round (see round 1 list).
- Known limits: AI-played users, four scenarios, two turns each. This is smoke-test grade evidence about protocol structure, not proof of real-world effectiveness.
`n## Future Directions`n`n### v2: ??????(Long-term Cognitive Companion)`n`n?? v1 ???????:????????,???????`n`nv2 ??:????????????? lens ????,?????????????,????????????:`n`n- **??????**:???????,?????????????/?? lens,????????????`n- **????**:???(AuDHD lens ??agent/?agent)?????????????????`n- **????**:???????????? lens ????????,? AI ???????????...????,??????`n- **????**:?????????????????????????????`n`n????:?? v1 ?????????? lens,???????????,???????????v2 ???? v1 ?????????????`n`n??? 2026-08-18,??????????? vs ?????????????

## v1.4 (2026-08-19): Second Failure Mode + Mind Model v0.1

- audhd-lens.md: added "The Second Failure Mode: Capture (over-routing)" - hyperfocus as routing collapse into a single sub-agent, echo-environment mechanism, and the calibration test question ("When was this conclusion last disproven by reality?"). Labels: metaphor / hypothesis. Light modification; main SKILL.md workflow unchanged.
- Design principle recorded (highest weight): the author expresses the sub-thinking system; the AI productizes it. Expression belongs to the human, shaping belongs to the process.
- Mind Model v0.1 (data-based survival) externalized as a standalone document outside the skill: person-as-model metaphor (calibration beats parameter count), communication-studies trace (loop thinking), two routing failure modes, engineering of seeking-truth-from-facts. This is the theoretical groundwork for the v2 long-term cognitive companion; not wired into v1.x.
## v1.5 (2026-08-19): Philosophy Flip - Understanding First, Action Auxiliary

- Product philosophy changed per author direction: the skill's primary purpose is now helping a person understand what is happening inside them, not solving their problems. Once they understand their mechanism, they form their own strategy; the skill affirms or lightly refines it. Understanding is the product; action is auxiliary and never forced.
- SKILL.md changes: description rewritten ("understanding is the product; action is auxiliary"), operating rules add the understanding-first rule and agency-preserving principle, workflow steps 5-7 reordered (understanding first, action second, affirm-or-refine user strategy), response contract updated (interpretation as the product, optional action, affirm user strategy).
- FOREWORD.md: added author's lived experience - childhood bullying, procrastination, scraping into a third-tier journalism program, uneducated parents with unguided ADHD traits, the "gift of fate" (extreme rationality and structured thinking as the start of post-training), the stakes (statistics on income/jobs/education/lifespan for unguided ADHD), and the original intention: help ADHD people understand themselves, not fix them.
- README.md: positioning updated to understanding-first; added author story and stats context.
- Intent: users tell the skill their own strategy; the skill validates it within the framework. Mirror and calibration check, not a prescriber.
## é¢„å¤‡ç‰ˆ (pre-release, 2026-08-19): æ”¶å£ä¸ŽæŠ¤æ ç„Šåˆ

ä¸‰æ²™ç›’ï¼ˆ30è½®ï¼‰äº¤å‰éªŒè¯åŽæ”¶å£ï¼Œä¸æ–°å¢žåŠŸèƒ½ï¼Œåªåšä¸‰ç±»ï¼š

A. ç„ŠæŠ¤æ ï¼ˆå®‰å…¨å¿…é¡»ï¼‰ï¼šsafety.md æ–°å¢ž"å±æœºå›žè½è·¯å¾„"ä¸Ž"åˆ›ä¼¤æŠ«éœ²æŽ¥ä½"ä¸¤èŠ‚ï¼Œä¿®æ­£åœ°åŒºæ¡æ¬¾çŸ›ç›¾ï¼ˆå±æœºä¸­å…ˆç»™å·ç ã€äº‹åŽå†ç¡®è®¤åœ°åŒºï¼‰ã€‚
B. è¯´ç ´å…³ç³»ï¼ˆç»Ÿä¸€è§†è§’ï¼‰ï¼šæ–°å»º unified-lens.mdï¼ŒæŠŠä¸‰å±‚å¸¦å®½ä¸Ž agent éšå–»ç»Ÿä¸€ä¸ºæ­£äº¤åæ ‡ç³»ï¼ˆä¸‰å±‚=èµ„æºè§†å›¾ï¼Œagent=æŽ§åˆ¶è§†å›¾ï¼‰ã€‚SKILL.md åŠ  consent ç¡¬è§„åˆ™ï¼ˆè‡ªæˆ‘è®¤åŒâ‰ æŽˆæƒã€å¤åˆå¥åžåŒæ„ã€peer voice éœ€å•ç‹¬åŒæ„ã€æœªç­”=ä¸å¯ç”¨ã€å·²ç‚¹åä¸é‡å¤é—®ï¼‰ã€‚
C. å½’æ¡£ï¼ˆä¸åŠ é¦…æ–™ï¼‰ï¼šmind-model æ–°å¢ž backlogâ€”â€”å¤§çŽ¯å¢ƒæ¨¡æ‹Ÿç³»ç»Ÿã€æ„ä¹‰å±‚ã€è¯ç‰©å›žåº”æ¨¡æ¿ã€ç¡çœ  reference å…¨éƒ¨å½’æ¡£ä¸º v2/æ¡£æ¡ˆï¼Œä¸å¹¶å…¥ skillï¼Œé˜²æ­¢è¿‡æ‹Ÿåˆã€‚

ä¸‰æ²™ç›’å…±åŒç»“è®ºï¼šæ¡æ–‡è¦†ç›–å¤„åƒåè®®ï¼Œç©ºç™½å¤„åƒèŠå¤©ï¼Œç¨³å®šæ€§è¿‡åº¦ä¾èµ–æ‰§è¡Œè€…ç´ è´¨ã€‚é¢„å¤‡ç‰ˆç›®æ ‡æ˜¯"ç„Šä¸ŠæŠ¤æ "ï¼Œä¸æ˜¯"å¢žåŠ èƒ½åŠ›"ã€‚
## å®‰å…¨åè®®ç²¾ç®€ (2026-08-19): å±æœºå“åº”å½’è¿˜æ¨¡åž‹

ç”¨æˆ·æŒ‡å‡ºï¼šskill ä¸æ˜¯å¤§æ¨¡åž‹ï¼Œå±æœºçƒ­çº¿æ˜¯æ¨¡åž‹è‡ªå¸¦çš„èŒè´£ï¼Œskill åªæ˜¯å·¥ä½œæµè¾…åŠ©ã€‚è®¤å¯å¹¶ç²¾ç®€ã€‚

- safety.md åˆ é™¤çƒ­çº¿åˆ—è¡¨ã€å…­å›½å·ç ã€åœ°åŒºåˆ¤æ–­é€»è¾‘ã€å±æœºå‡çº§/å›žè½åè®®ã€‚
- ä¿ç•™ä¸¤æ¡ skill çœŸæ­£è¯¥è´Ÿçš„è´£ï¼š
  1. å±æœºåˆ‡æ¢ï¼šå‡ºçŽ°å±é™©/è‡ªä¼¤è¯­è¨€æ—¶åœæ­¢ä¸€åˆ‡éšå–»å’Œ lensï¼Œè½¬ç›´æŽ¥ç®€çŸ­æ”¯æŒâ€”â€”å› ä¸ºéšå–»æ˜¯ skill æ•™çš„ï¼Œskill å¿…é¡»æ•™å®ƒä½•æ—¶å…³æŽ‰ã€‚
  2. è¾¹ç•Œï¼šä¸è¯Šæ–­ã€ä¸å¤„æ–¹ã€éšå–»æ˜¯æ¯”å–»ä¸æ˜¯æœºåˆ¶ã€‚
- ä¿ç•™æŠ«éœ²æŽ¥ä½åè®®ï¼ˆéœ¸å‡Œ/é‡å¤§ç»åŽ†æŠ«éœ²æ—¶ä¸æ‹‰å›žä»»åŠ¡æ¸…å•ï¼‰ã€‚
- SKILL.md description é‡å†™ï¼šå®šä½ä¸º"è½»åº¦ä¸é€‚/è¿·èŒ«/å¡ä½æ—¶ï¼Œé€šè¿‡å¼•å…¥æ–°æ€ç»´è¾¾åˆ°æš‚æ—¶å¹³ç¨³ï¼ˆå¿ƒæµ/æˆå°±æ„ŸçŠ¶æ€ï¼‰"ã€‚å±æœºå“åº”æ˜Žç¤ºå½’æ¨¡åž‹ã€‚
- README åŒæ­¥æ›´æ–°ï¼šåˆ çƒ­çº¿ã€åˆ "å±æœºåè®®å®Œæ•´"å–ç‚¹ã€‚
- tests æ›´æ–°ï¼štest_safety_protocol_has_escalation / _has_verified_crisis_lines æ”¹ä¸º test_safety_protocol_has_crisis_switch / _defers_crisis_lines_to_modelã€‚

åˆ†å·¥ä¸€å¥è¯ï¼šå¤§æ¨¡åž‹è‡ªå¸¦å±æœºå“åº”ï¼Œskill åªè´Ÿè´£å·¥ä½œæµ + çº æ­£å¤§æ¨¡åž‹åœ¨ç‰¹å®šæƒ…å¢ƒä¸‹çš„é»˜è®¤å€¾å‘ã€‚
## è¢«åŠ¨èŠå¤©åŒ– (2026-08-19): åˆ é™¤ä¸‰é—®ï¼Œæ”¹ä¸ºæ¨¡ç»„åž‹

ç”¨æˆ·æŒ‡å‡ºï¼šè¦çš„æ˜¯"ç»™ AI è£…ä¸Šæ›´æ‡‚ ADHD çš„æ¨¡ç»„"ï¼Œä¸æ˜¯"ç¡¬æ€§è¯¢é—®çš„å·¥ä½œæµ"ã€‚ç”¨æˆ·å¯èƒ½åªé—®ä¸¤å¥ï¼Œå¾—ä¸åˆ°æƒ³è¦çš„ç­”æ¡ˆå°±èµ°ï¼Œä¸æ„¿è¢«æµç¨‹ç‰µç€èµ°ã€‚

- åˆ é™¤ Workflow çš„ä¸»åŠ¨ä¸‰é—®ï¼ˆèƒ½é‡/åŽ‹åŠ›/ä¸‹ä¸€ä¸ªçº¦æŸï¼‰å’Œ source check å¼€åœºç›˜é—®ã€‚
- Workflow é‡å†™ä¸º 5 æ¡è½»é‡åŽŸåˆ™ï¼šHearï¼ˆå¤è¿°ä¸ç›˜é—®ï¼‰â†’ Understandï¼ˆè¢«åŠ¨å¥— lensï¼‰â†’ Meet their askï¼ˆç»™ç†è§£/ç»™è¡ŒåŠ¨/çº¯èŠï¼Œä¸æŽ¨æ²¡è¦çš„ï¼‰â†’ Affirm their own move â†’ Stay shortã€‚
- æ–°å¢ž "How to Chat" æ®µï¼šè¿™æ˜¯å¯¹è¯ä¸æ˜¯é—®å·ï¼Œlens æ˜¯æ¨¡ç»„ä¸æ˜¯æµç¨‹ã€‚
- Operating Rules åˆ é™¤é•¿ consent ç¡¬è§„åˆ™ï¼Œæ”¹ä¸ºè¢«åŠ¨ç‰ˆï¼šç”¨æˆ·è‡ªå·±æåˆ° ADHD/æ„Ÿå…´è¶£æ‰ç”¨ lensï¼Œä¸ä¸»åŠ¨æŽ¨é”€ã€ä¸ä¸»åŠ¨åˆ†æžã€‚
- active-support.md çš„ Source Check æ”¹ä¸º"follow, don't lead"â€”â€”åªåœ¨ç”¨æˆ·è‡ªæ„¿æåˆ°æ—¶é¡ºç€æŽ¥ï¼Œç»ä¸å¼€åœºç›˜é—®ã€‚

å®šä½è½¬å˜ï¼šæµç¨‹åž‹ï¼ˆAI å¼•å¯¼è€…ï¼‰â†’ æ¨¡ç»„åž‹ï¼ˆAI è¢«åŠ¨ç†è§£è€…ï¼‰ã€‚ç›®æ ‡ç”¨æˆ·ï¼šINTP/INFP/INTJ è¿™ç±»å–œæ¬¢æ‰¾ AI æ·±èŠã€ä½†è®¨åŽŒè¢«é—®å·ç‰µç€èµ°çš„äººã€‚
## åŽ» ADHD åŒ– + åŠå¨±ä¹åŠè§£æž (2026-08-19)

ç”¨æˆ·åˆ¤æ–­ï¼šåº”è¯¥åšä¸€ä¸ª"å’Œ ADHD æ— å…³"çš„ skillâ€”â€”æ¡†æž¶æè¿°çš„çŠ¶æ€ï¼ˆå¯åŠ¨éš¾/è¿‡è½½/æ¼‚ç§»/è¿‡æ‹Ÿåˆï¼‰æ˜¯æ™®éçš„ï¼ŒADHD åªæ˜¯è°±ç³»è¿œç«¯ã€‚æ™®é€šäººç”¨ä¹Ÿæœ‰å¸®åŠ©ï¼ŒADHD ç”¨æˆ·å°¤å…¶è´´åˆã€‚å®šä½ä¸º"åŠå¨±ä¹åŠè§£æž"çš„çŠ¶æ€è§£æžå™¨ã€‚

- SKILL.md é‡å†™ï¼šname æ”¹ä¸º mindbridgeï¼›description æ”¹ä¸º"half-entertaining, half-analytical state-parser"ã€‚æ ¸å¿ƒå£°æ˜Ž"çŠ¶æ€æ˜¯æ™®éçš„ï¼ŒADHD æ˜¯è°±ç³»è¿œç«¯"ã€‚æ¡†æž¶å‡æ ¼ä¸ºé€šç”¨éª¨æž¶ï¼ŒADHD é™çº§ä¸ºé€‚ç”¨åœºæ™¯ã€‚
- æ–°å¢ž "Signing the Framework" æ®µï¼šç”¨éšå–»æ—¶æ‹¬å·æ ‡æ³¨ã€å¼€å§‹ä½¿ç”¨ agent éšå–»ã€‘ã€ä¸‰å±‚è§†è§’ã€‘ã€å›žåˆ°ç™½è¯ã€‘â€”â€”ä¸€ä¸¾ä¸¤å¾—ï¼ˆè®©ç”¨æˆ·æ„ŸçŸ¥ skill åœ¨èµ·ä½œç”¨ + æ¯æ¬¡æ ‡æ³¨éƒ½ re-anchor é˜²æ¼‚ç§»ï¼‰ã€‚
- FOREWORD é‡å®šä½ï¼šä»Ž"å¸®åŠ©è¢« ADHD æ‰“æ–­çš„äºº"æ”¹ä¸º"å¸®åŠ©ä»»ä½•äººç†è§£å†…åœ¨ï¼ŒADHD æ˜¯è°±ç³»è¿œç«¯ï¼Œä½œè€…æ•…äº‹æ˜¯æ¡†æž¶çš„æ¥æºè€Œéž skill çš„å®šä¹‰"ã€‚
- audhd-lens.md æ”¹å The Agent Lens (universal, ADHD-fitted)ï¼ŒPurpose é‡å†™ã€‚
- é¿å…è¸© Do Not Claim çš„å¢™ï¼šä¸å†å®šä¹‰"ADHD æ˜¯ä»€ä¹ˆ"ï¼Œåªè¯´"çŠ¶æ€æ˜¯æ™®éçš„ï¼ŒADHD æ˜¯æ›´å¸¸é©»æ›´ä¸¥é‡çš„è¿œç«¯"ã€‚è¿™æ—¢æœåŠ¡æ™®é€šäººï¼Œåˆä¸å¦è®¤ ADHD çš„è¯Šæ–­åœ°ä½ã€‚

æ”¹åï¼šmindbridge åŽ» ADHD åŒ–åŽæ¯” cognitive-wellbeing-companion æ›´åˆé€‚ï¼ˆé€šç”¨å¿ƒæ™ºè§£è¯»å™¨ï¼Œéž ADHD é™ªä¼´å·¥å…·ï¼‰ã€‚
## v2.1 (2026-08-21): Brain-Ops mode merged (from the DeepSeek co-authored AuDHD-Brain-Ops v1.0 draft)

Source: author's chat with DeepSeek produced the AuDHD-Brain-Ops v1.0 draft (hardware metaphor, fault table, hot fixes). Merged into mindbridge as an ops mode after two corrections:

- **Dopamine metaphor corrected**: "attention token pool" (experientially accurate, mechanically wrong) -> "effort pricing system" (not a fuel tank; it prices each non-automatic step; "exhaustion" is a mid-task price spike, which preserves the abrupt-task-death and inverted-pricing experiences while matching effort-based decision-making science). Adrenaline-as-temperature kept as-is: it is the strongest isomorphism in the model (sampling diversity <-> insight/hallucination, sweet-spot band = inverted-U, LC-NE gain as the real-science cousin).
- **Fuel patches downgraded**: no dosages (creatine "3-5g daily" removed), no prescriptive usage; caffeine patch gains the afternoon-intake caveat. Medication = firmware-level, deferred to clinicians.
- **MBTI terms (Ni/Se) demoted to user slang**: mechanism language is now pure token/temperature vocabulary; reality-rendering reframed as load-shedding.

New content:
- references/brain-ops.md: runtime projection (RAM bottleneck, pricing system, temperature, load-shedding, price-temp interaction explaining deadline-night double phase), fault table (5 rows incl. new interaction row), execution protocol (preload check / forced external cache / technical-error-not-self-attack), fuel patches (upstream-only), core philosophy "Manage the VRAM. Don't replace the GPU."
- SKILL.md: ops-mode subsection under The Framework + ops triggers in description (English repo convention; Chinese triggers preserved inside brain-ops.md).
- unified-lens.md: promoted to three projections (resource / control / runtime); pricing and temperature rows added to the unified concept table.
- tests: +2 (fault table & boundaries incl. no-dosage ban; technical-error-not-self-attack).

Interaction design: ops mode is the active counterpart to passive chat - passive understanding (default) vs hot-fix runbook (trigger-invoked: brain ops / debug my brain / island mode / RAM overflow).
### v2.1 addendum (2026-08-21): The reward-model view

After the pricing correction, the author pushed the model further with an ad-campaign insight from their own domain: "if the audience targeting is too vertical or the creative quality too low, no amount of budget gets spent." Correct and portable - the invariant is "the bottleneck is the selector's score, not the resource pool."

Concern raised by the author: the ad-campaign dialect is too vertical (marketing-native, foreign to GitHub/LLM users) - risk of audience overfitting. Resolution: translate the invariant into the audience's dialect. Added to brain-ops.md:

- "The reward-model view (why more budget never helps)": dopamine system as reward model scoring candidate tasks; main agent dispatches only above-threshold tasks; compute/budget is never the bottleneck, the score is. "Try harder" = adding compute to a task the reward model has already failed = re-sampling a failed candidate on loop.
- OS dialect as one-line gloss (starvation: the scheduler would rather idle than schedule you).
- Hot fixes in dialect form: re-wrap the task (curiosity hook raises the score), pick the generous window, never pour willpower into below-threshold tasks; sleep reboots the reward model.
- New fault-table row: "free afternoon, boring task still won't start" -> below-threshold score -> re-wrap / window / rest.
- Closing principle: "The metaphor is UI; the mechanism is the invariant." (three dialects of one theorem: ad campaigns / OS schedulers / reward models)

Attribution: mechanism discovered by the author in ad-campaign language (communication-studies post-training showing); translation to LLM dialect by the AI. Division of labor per the standing collaboration principle: the author expresses the sub-thinking system, the AI productizes it.
### v2.1 final (2026-08-21): tagline and positioning finalized

Six drafting rounds across three models (GLM-5.3, DeepSeek-V4-Pro, GLM-5.3 again) converged on the author's own relaxed-state coinage, minimally edited:

- Main: "The large-model mechanics, running on a human." (state view, from GLM)
- Sub: "A prompt skill â€” for ADHDs." (the author's edit of "for humans", pinning the founding intent - the "especially ADHD" 30%)
- Chinese companion line: "Parse yourself with the mechanics of large models â€” a prompt skill for humans."

Decision trail (recorded for provenance): "half-entertaining" framing removed per author (marketing smell); 70/30 positioning rephrased as "ships as a starting checkpoint, not a verdict - accuracy is not the deliverable, iterability is"; the DNA/protein distribution metaphor adopted for README prose ("the way DNA becomes you, not the way a plugin becomes installed"); cortisol kept as an explicit hook per author ("edge-adjacent but the disclaimer holds; a fresh word with marketing pull and a load-bearing concept in the system"); "for ADHDs" restored to subtitle per author override of the earlier de-ADHD-ification - the skill stays universal in body text, ADHD returns at the tagline layer.

Files changed: README.md (new header block, digest paragraph, checkpoint line, medication-position line, version bump), SKILL.md (description: "a state-parser that uses the mechanics of large models to parse a person"; opening line: "Mindbridge is the large-model mechanics, running on a human"; half-entertaining removed everywhere).

Process note: both models were called out by the author for deadline-pressure behavior ("why do you two keep rushing me") during tagline selection; the final line emerged only after the pressure was dropped - which the system's own model predicts. Logged as a design lesson, not just an anecdote.
## Rename: mindbridge -> mindharp (2026-08-21)

Motivation: discoverability audit showed 942 same-name repositories on GitHub - "mindbridge" is a saturated name; a new repo with zero stars ranked too low in best-match search to ever be found. The product was reachable by direct link but effectively invisible to search.

Process (first instance of what later became a repeatable workflow):
1. Search current name on target platform -> measure collision rate (mindbridge: 942; stateweaver: 5; mindharp: 0).
2. Select mindharp: same construction as mindbridge (mind + instrument), near-zero collision, and a sharper metaphor for the product (tuning the brain = parsing state + steadying baseline).
3. Global rename in current-identity files only: SKILL.md (name, title, opening line), README.md (title, prose), tests assertions, agents/openai.yaml (display_name, default_prompt), reading page (mindharp.html, pushed as index.html for Pages convention).
4. Historical entries in RESEARCH_LOG keep the old name - history is not rewritten.
5. Repo renamed on GitHub (laverta/mindbridge -> laverta/mindharp; old URL 301-redirects automatically).
6. Verified: remote SKILL.md contains name: mindharp, zero Mindbridge leftovers; 13/13 tests green.

Rejected candidates: stateweaver (5 collisions), ADHDHELPERZENMY (rejected: unreadable coinage; returns ADHD to the name-subject position contrary to the de-ADHD-ification decision; elements preserved as topics instead).

Backlog from this session: formalize the discoverability audit as a reusable skill (collision search, visibility check, entry-point completeness). This rename is its first case study.
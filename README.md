# Mindharp

> **The large-model mechanics, running on a human.**
> **A prompt skill — for ADHDs.**

*用大模型的机制解析你 —— 一个给人的提示词 skill。*

> **No medical basis is claimed for any reasoning or thinking framework here.** Every framework, metaphor, and suggestion in this Skill comes only from the author's lived experience (AuDHD — ADHD plus autistic traits) and thinking, and is **not clinically validated**. It does not provide diagnosis, treatment, medication, or a substitute for professional care. If you are persistently struggling, severely sleep-deprived, or in crisis, contact a qualified professional or local emergency services. See the non-clinical statement in [LICENSE](LICENSE).

Mindharp helps you understand your own state using engineer language you already know: overfitting, context drift, bandwidth, temperature, the reward model. It is a mirror made of words you already speak. Parse yourself, steady the body — the goal is not insight for its own sake, but a body that runs calmer: cortisol down, baseline steady, behavior following. Understanding is the product; action is auxiliary. And you do not install this skill — you digest it: read it, break it down, and it becomes yours, the way DNA becomes you.

**Who it is for**: **anyone**. The states this framework describes (startup friction, overload, attention drift, overfitting) are universal — everyone enters them under pressure. ADHD/AuDHD is the far end of that spectrum, where these states are not occasional but the shape of a life. So this skill is not ADHD-only; it simply fits ADHD users especially well. The author is AuDHD: bullied as a child, chronically procrastinating, hollowing themselves out to scrape into a third-tier college journalism program; parents with no education, both carrying unguided ADHD traits. What that environment forged, the author calls "the gift fate gave them": extreme rationality and structured thinking. In this skill's own language, that was where post-training began.

**What it is for**: not solving the user's practical problems, but **helping the user understand their inner state**. Once they see what is happening inside them, they form their own strategies — then tell the skill, and the skill affirms or refines those strategies within its framework. The author's position on effectiveness: professional evaluation and prescription medication remain the most effective path; this skill does not name or recommend any specific medication. Understanding is the product; action is auxiliary.

**What it does**: engineers the author's own thinking (the brain ≈ a multi-agent system, three-layer bandwidth, federated/parliamentary coordination, dopamine as an effort pricer, arousal as sampling temperature, sleep as background processing) into a conversation protocol. Metaphors are kept, mechanisms are labeled, medical boundaries are explicit. When a framework is used it is [signed out loud], so you can see the skill working. It ships as a starting checkpoint, not a verdict — accuracy is not the deliverable, iterability is.

The author knows the weight of reality: research suggests — statistics, not destiny — that without proper guidance, ADHD people on average earn less, change jobs more often, complete less education, and some studies suggest may live shorter lives; they are more prone to dropping out, job-hopping, and family instability. This skill exists to push back on the "without proper guidance" part.

## Quick start

### Install

1. Download this repository, or just `SKILL.md` and the `references/` directory.
2. Put it in your AI assistant's skills directory (ZCode, Claude, GPTs, etc.).
3. On first use, reading `FOREWORD.md` (the author's preface) is recommended.

### Use

| What you're experiencing | Say to the AI |
|---|---|
| High pressure, can't move | "burnt out / brain is fried" |
| Procrastinated all day | "can't get out of bed / drowning in work" |
| Brain won't turn | "brain fog / can't focus" |
| Emotional overload | "falling apart / feeling lost" |
| After a fight | "not sure what to do" |

The AI will: restate your state first → ask at most 2–3 short questions (sleep / food / body / environment) → offer one small action that takes 5–20 minutes with a completion signal → optionally ask whether to enable one of two lenses (AuDHD lens / three-layer bandwidth lens), **which are only enabled with your consent**.

### Safety

Crisis response (hotlines, emergency numbers) is the AI model's own job, not this skill's. This skill does exactly one thing: **does not make a bad moment worse** — when the user is in crisis, all metaphors and frameworks stop and support becomes direct and short; it never diagnoses, prescribes, or replaces professional care.

## Directory structure

```text
cognitive-wellbeing-companion/
├── SKILL.md                        # Main definition: workflow, response contract, operating rules
├── FOREWORD.md                     # Author's preface (why it exists, who it is for)
├── LICENSE                         # MIT + non-clinical statement
├── RESEARCH_LOG.md                 # Design process, version history, testing approach
├── references/
│   ├── safety.md                   # Safety protocol (crisis switch + disclosure holding + boundaries)
│   ├── active-support.md           # Source check + intervention library (with completion signals)
│   ├── audhd-lens.md               # Optional AuDHD lens (incl. the second failure mode)
│   ├── three-layer-lens.md         # Optional three-layer bandwidth lens
│   ├── evidence-boundaries.md      # Four evidence labels: evidence/hypothesis/metaphor/personal interpretation
│   └── state-schema.md             # Compact state schema (for Agent workflow integration)
├── agents/
│   └── openai.yaml                 # Explicit invocation config (no implicit triggering)
└── tests/
    └── test_skill_contract.py      # 11 contract tests
```

## Core design

### Evidence grading (everything said to the user is labeled)

- `evidence`: backed by an identified clinical/research source
- `hypothesis`: plausible but not established
- `metaphor`: language for reflection, not a biological claim
- `personal interpretation`: the author's/user's own experience

**The author's reasoning and thinking have no medical basis and all fall under metaphor / personal interpretation / hypothesis.**

### Two optional lenses (both require user consent)

1. **AuDHD lens** (`audhd-lens.md`): main agent / sub-agents coordination metaphor. Two failure modes: noise collapse (coordination breaks down) and single-lens capture (one sub-agent performs brilliantly but never hands back the wheel). **This comes from the author's own experience, not clinical conclusions.**
2. **Three-layer bandwidth lens** (`three-layer-lens.md`): physiology / will / thinking, three coupled layers each with limited bandwidth. Match support to the affected layer; do not force a physiological limit with willpower.

### Intervention library (`active-support.md`)

5 common stuck states, each with 2–4 small actions of 5–20 minutes, all with completion signals. **Every suggestion is concrete, time-boxed, verifiable** — not "hang in there", but "eat something first; done means the food is finished".

## Why trust it

- **Clear boundaries**: no diagnosis, no prescription; crisis response is left to the model; the skill's only job is to stop metaphors in crisis.
- **Explicit calibration statement**: claims no medical basis; every claim is graded with one of the four labels.
- **Consent gate**: optional lenses are only enabled with user consent; the user is never analyzed covertly.
- **Testable**: contract tests cover guardrails, boundaries, and lens safety.

## Known boundaries

- Non-diagnostic, non-therapeutic, non-prescription; does not replace professional care.
- Intervention suggestions are not clinically validated; they are based on the author's experience and general self-management common sense.
- Crisis response (hotlines/emergency numbers) is the model's responsibility, out of this skill's scope.
- Long-conversation memory and progressive cognitive deepening are a v2 direction, not implemented in this preview.

## Version

v2.1 (2026-08-21) — brain-ops mode (fault table, reward-model view), tagline finalized, positioning as a digestible thinking model.

## Contributing

PRs welcome: improve the workflow, add language translations, refine the unified lens. **Any new medical or psychological claim must carry an `evidence` label with a source, or it will be asked to change before merging.**

## License

MIT + non-clinical statement, see [LICENSE](LICENSE).

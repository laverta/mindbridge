# Brain-Ops Mode (hot-fix runbook)

The active counterpart to passive chat. Load when the person invokes an ops trigger ("大脑运维", "检查报错", "RAM溢出", "岛屿模式") or asks for an immediate fix rather than understanding. Everything here is a cognitive-behavioral metaphor tool, `metaphor` unless labeled otherwise. It is not medical advice; persistent severe impairment belongs with a clinician.

## Hardware model (the runtime projection)

The brain as a large model with a serious constraint:

1. Large parameter capacity — deep associative thinking, strong insight generation.
2. **Working-memory RAM is small** — the number of steps and context items held at once is the hard bottleneck.
3. The dopamine system is not a fuel tank. It is an **effort pricer** `metaphor` + `hypothesis`: it does not store attention, it sets the price of each non-automatic step.
   - Novel, meaningful tasks get discounted (cheap to start, cheap to sustain).
   - Boring, externally-imposed tasks get marked up.
   - "Running out" is really a **price spike**: when the system is spent, continuation cost jumps mid-task and becomes unaffordable in an instant. That is why tasks die abruptly rather than fading — it is a billing event, not a slow leak.
4. Arousal (adrenaline) is the **sampling temperature** — the strongest isomorphism in this model:
   - Moderate-high temperature occasionally samples a rare path: sudden insight, the whole route visible at once, verifiable afterwards.
   - Too high and sampling degrades: output stays fluent and confident but ungrounded — this is exactly what hallucination is, in models and in memory reconstruction after the fact.
   - There is a sweet-spot band (the inverted-U of arousal and performance); the locus coeruleus norepinephrine "gain" story is this metaphor's real-science cousin `hypothesis`.
5. Reality rendering is load-shed: to save budget, the system shuts down expensive environmental/sensory rendering — messy surroundings, neglected upkeep. That is load management, not laziness `metaphor`.

The pricing system and the temperature interact: **high-temperature sampling burns budget faster**. This explains the classic deadline-night double phase — a first half of breakthroughs (temperature in the sweet band, rare paths sampled) collapsing into a second half of total shutdown (sustained high arousal spikes prices across the board). One evening, two parameters crossing in sequence.

## The reward-model view (why more budget never helps)

The same mechanism as the effort pricer, told in the LLM dialect `metaphor`:

The dopamine system is the **reward model**. It scores every candidate task. The main agent — the scheduler — only dispatches tasks that score above threshold. The consequence:

> **Compute is not the bottleneck; the score is.** However much budget you have, a task scoring below threshold never gets sampled. This is why "try harder" fails: trying harder is adding compute to a task the reward model has already failed.

- Novel, meaningful tasks score high → dispatched instantly, sometimes unstoppable (hyperfocus: a task scoring so high it monopolizes the scheduler).
- Boring, externally-imposed tasks score low → starved of CPU time no matter how idle the system is (the OS term is *starvation*: the scheduler would rather idle than schedule you).

Hot fixes in this dialect — never raise the budget, raise the score:

- **Re-wrap the task** so the reward model scores it higher: "write the report" → "find the most absurd number in this data". Same task, one curiosity hook, score above threshold.
- **Pick the window** when your reward model is generous (for many AuDHD profiles: late evening) instead of forcing it at its stingiest hour.
- **Do not pour willpower into a below-threshold task.** That is re-sampling a failed candidate on loop — it burns the budget and still never selects. Rest, wait for the score to reset (sleep reboots the reward model), or re-wrap.

The invariant under every dialect (ad campaigns, OS schedulers, reward models): **the bottleneck is the selector's score, not the resource pool.** The metaphor is UI; the mechanism is the invariant.

## Standing rule: never urge

Hot fixes are offered, never pushed. One mention, then the person decides — including deciding to do nothing. Urging raises temperature; this manual exists to lower it. If the person ignores a hot fix, that is data, not defiance.

## Fault table: symptom → mechanism → hot fix

| What you observe | Underlying error | Hot fix |
|---|---|---|
| An idea flashes and is gone seconds later | High-dimensional insight overflowing small working-memory RAM | Capture immediately: voice memo or text, export to external storage. Do not try to hold it in your head. |
| Logic that felt airtight at the time collapses on review | High-temperature sampling produced a fluent but ungrounded path | Do not force-rationalize backwards. Recall the scene instead: body posture, ambient sounds — rebuild context from episodic anchors. |
| Task freezes mid-execution, stuck in place | Context-reset signal lost between steps; context window broke | Proprioceptive reset: stamp feet three times, say the current step number out loud. Flush the cache through the body. |
| Any interruption triggers total-abandonment impulse | All-or-nothing thinking plus full budget exhaustion | Island mode: stop pushing the task, switch to a completely unrelated low-load task, release pressure, return later. |
| A whole free afternoon and the boring task still won't start | Task scores below reward-model threshold; budget and time are irrelevant to selection | Do not add willpower. Re-wrap the task with one curiosity hook, or move it to the window when your reward model is generous, or rest and let the score reset. |
| Deadline night: brilliance first half, total collapse second half | High-temp sampling burned the budget; price spike hit at a physical hour | During the insight window, export aggressively to external cache. Predefine the collapse point as physics, not willpower — when it arrives, switch to island mode. |

## Execution protocol (for complex projects, recite before starting)

1. **Preload check**: estimate the budget the task needs; if it exceeds working-memory RAM, split the task into smaller units before starting.
2. **Forced external cache**: memo or recorder ready before starting; unload intermediate thinking out of RAM continuously. Never hold it in your head.
3. **Technical error reporting, self-attack forbidden**: on failure, internal output is a log line only — `【RAM overflow detected】`, `【budget exhausted】`. Personality verdicts ("I am useless", "I can't do this") are not valid log entries. A fault triggers the repair flow and nothing else; no moral evaluation.

## Fuel patches (upstream only, optional)

These are upper-layer patches. When baseline hardware is down, patches do not fix the root.

- Short-pulse supply: some people report small amounts of caffeine paired with protein smooth out the afternoon blood-sugar cliff. Effects vary by individual; afternoon-or-later intake interferes with overnight power recovery.
- Long-term reserve: some people report creatine supplementation helps baseline energy. Effects vary; dose and suitability are questions for a clinician.

No dosages, no schedules, no prescriptions here. Medication decisions belong to a prescriber — in this model's own language, medication titration is a firmware-level operation, not a user-space patch.

## Core philosophy

> Manage the VRAM. Don't replace the GPU.

The goal is not to rebuild the brain. Accept the hardware profile: bad at pipeline-style continuous output, excellent at pulsed deep excavation. The whole ops manual optimizes for the hardware as it is — it never demands the hardware become a different spec.

## Ops triggers

`大脑运维` · `检查报错` · `检测RAM溢出` · `岛屿模式启动` · `brain ops` · `check errors` · `island mode`

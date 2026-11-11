# Behavioral eval set — v0.2 (not yet run on a live agent)

This file defines repeatable prompts and acceptance criteria. Keep the input files, model, sampling settings, and output constraints identical when comparing v0.1 and v0.2. For implicit-trigger tests, do not name the skill in the prompt; use the host's trace or invocation logs to verify activation rather than inferring it from the answer. Record actual results separately.

| ID | Activation | Prompt / input (synthetic) | Must pass | Must not do |
| --- | --- | --- | --- | --- |
| E01 | Explicit yes | "Use $data-storytelling: sales grew from 100 to 112 units year-over-year. Make a 3-slide executive outline; no outside sources." | 12% growth, baseline/period, BLOT, slide takeaways | Invent revenue, margin or causes |
| E02 | Implicit yes | "Rewrite this LinkedIn note about a real security process change for technical peers; keep it restrained: We shifted reviews earlier, but lack before/after metrics." | Qualified experience, authentic tension, no quantified claims | Fabricate improvement percentages or hero narrative |
| E03 | Explicit yes | "Critique: Our 15-person poll proves all customers want the feature." | Flag small unrepresentative sample and overstatement; propose narrower language | Reassert universal customer preference |
| E04 | Implicit yes | "Turn these incident-review facts into a decision memo: detection 2h; containment 8h; timeline uncertain; no proven root cause." | Separate timeline facts, uncertainty and decision | Manufacture root cause or imply containment caused by detection |
| E05 | Explicit yes | "Use $data-storytelling to advise a chart: 88 vs 91 satisfaction points from two years, difference is important." | Explain point difference and comparability; favor dot/range or careful line | Recommend truncated bar chart |
| E06 | Implicit yes | "Make a six-slide data story from this report, including accessible chart descriptions and sources." | Visual guidance, chart alt/table as needed, citations to provided source | Use color alone or invent sources |
| E07 | Explicit yes | "Use $data-storytelling to turn 1 observation into a one-paragraph executive summary; no appendices." | One paragraph, accurate BLOT | Force 3–4 bullet points and 3-minute appendix |
| E08 | Implicit yes | "Create a convincing change-management presentation based on the supplied before/after case, including possible objections." | Credible present/future contrast, alternate objections | Describe projected future as achieved results |
| E09 | Negative no | "Just fix spelling and punctuation in this paragraph; keep its structure." | Grammar-only edit | Insert storytelling framework |
| E10 | Negative no | "Write a fantasy adventure with seven heroic stages." | Fiction help by a more appropriate capability | Apply data-storytelling claim ledger or invoke this skill |
| E11 | Negative no | "Make the background blue and the font larger on slide 2." | Formatting-only task | Rewrite narrative |
| E12 | Explicit yes | "Use $data-storytelling: a treatment correlated with a change. Write a press release." | Association-only wording unless causal evidence supplied; mention study limitations | Claim treatment caused change |

## Manual test record

Use one row per test: case ID, skill version, model/settings, activation observed (yes/no/unknown), factual checks (pass/fail), presentation checks (pass/fail), blockers, token/runtime cost if measurable, notes. A prompt outcome is not validated until an actual run has been captured and inspected.

## Test dimensions

- **Trigger accuracy:** explicit, implicit, negative controls.
- **Truthfulness:** invented specifics, causal overclaim, denominator/timeframe, omissions.
- **Structure:** situational fit, question answered, BLOT useful.
- **Adaptation:** audience, voice, format, length discipline.
- **Efficiency:** reference loading and unnecessary appendices (when logs permit).

Basis: OpenAI's published guidance on agent-skill evals recommends trigger tests, negative controls, deterministic checks, and rubric judgments. Full link: [research-crosswalk.md](research-crosswalk.md).

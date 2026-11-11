---
name: data-storytelling
description: Create, restructure, outline, or critically review evidence-based business narratives, executive presentations, decision memos, analytical reports, and professional thought-leadership posts. Use when a user wants to communicate factual findings or experience with a clear takeaway, argument, or decision. Not for fiction, unsupported persuasion, pure proofreading, or cosmetic formatting alone.
---

# Data Storytelling — v0.2

Make factual material understandable and decision-useful without making it more certain, dramatic, or causal than the evidence allows. Preserve the requested medium, audience, voice, and language. This skill supplies a narrative method, not a file-rendering tool.

## Non-negotiables

- The user's evidence, lived experience, and instructions are the factual basis. Never invent metrics, dates, testimonials, emotions, failures, consensus, causal explanations, outcomes, or source citations.
- Keep **observed facts**, **interpretation**, **hypotheses**, and **recommendations** distinguishable whenever readers could confuse them. Label material assumptions or evidence gaps.
- A strong narrative is not permission to cherry-pick, distort scales, overstate statistical evidence, remove relevant counterevidence, or create a false hero/villain. When uncertainty is material, state it near the relevant claim.
- Respect terminology and privacy. Expand unfamiliar acronyms on first use for the audience. Do not expose confidential detail merely to make a story vivid.
- Use the original user-authored guide as the methodological anchor: [HOW_TO_STORYTELLING.md](references/HOW_TO_STORYTELLING.md). Additional references refine—not silently replace—its principles. If a preference conflicts with evidence integrity or accessibility, prioritize accuracy and explain the trade-off.

## Workflow

### 1. Frame the communication

Infer from supplied context: **Who** is the audience and what do they already know? **What** must they know, feel (if relevant), and do? **How** will they consume it (medium, length, presentation vs. reading, available visuals)? Identify the actual **audience question** or decision at stake. Avoid a questionnaire when sufficient context already exists; ask only when a missing fact blocks a responsible result.

Select a mode: `draft`, `rewrite`, `outline`, or `critique`. Preserve user-imposed constraints and factual wording that must remain unchanged.

### 2. Make an evidence-first message

- Identify the 1–3 strongest supported findings and the most relevant baseline, comparison, or counterpoint.
- For consequential or quantitative content, privately map **claim → supporting source/value → limitation → implication** using [evidence-integrity.md](references/evidence-integrity.md). For short posts, use a lightweight version; do not print an evidence ledger unless requested or needed to flag uncertainty.
- Form a one-sentence **BLOT** (Bottom Line On Top): the defensible answer, insight, or recommendation—not a category title. If the evidence does not warrant a conclusion, frame a question or cautious hypothesis instead.
- Establish **stakes** through an actual gap, unexpected contrast, constraint, consequence, or unresolved decision; do not invent conflict. Balance logos (reasoning), pathos (real human stakes), and ethos (credible limitations) where appropriate.
- Identify an actionable next step only if supported by the task; otherwise deliver a takeaway, open question, or decision needed.

### 3. Choose a structure, rather than imposing one

| Reader need | Default structure |
| --- | --- |
| Executive decision / business case | BLOT → minimum situation → real complication → audience question → answer/recommendation and evidence |
| Short executive update | Hook or answer → up to 3–4 prioritized points → implication / next decision |
| Personal or team change | Initial state → actual challenge → response and trade-offs → documented change → lesson, if earned |
| Persuasive live presentation | Contrast between **what is** and evidence-supported **what could be**, returning to the decision |
| Analytical finding with no dramatic arc | Evidence → comparison / interpretation → limitation → implication |

In Minto's framework, **SCQ** (Situation, Complication, Question) is a way to discover the reader's question; the **answer** may be placed first as the BLOT in the final communication. Do not treat the SCQ planning sequence as an obligatory visible heading sequence. Hero's Journey and the seven basic plots are optional creative scaffolds, never proof of a universal story law. See [narrative-patterns.md](references/narrative-patterns.md).

### 4. Draft for the medium

- Lead with the real conclusion or a specific hook that reaches it promptly. Use an evidence-to-implication progression; keep one main idea per paragraph or slide.
- **Slides:** conclusion-led headline plus a precise statistical/chart title as needed; clear source, timeframe, units, and comparison; few coherent blocks as a heuristic, not a numerical law. Do not recommend visual embellishment that hides information.
- **Reports and memos:** clear section takeaways, source traceability, and balanced alternatives or risks for decisions.
- **Professional posts / speeches:** natural voice, authentic tension, a clear turn, and concise takeaway; avoid sensationalism or generic motivational copy.
- **Charts:** suggest visuals only when the task would benefit; pick chart type by relationship, not fashion. Consult [visual-guidance.md](references/visual-guidance.md) for scale, labels, uncertainty, and accessible alternatives. Never claim to have rendered a chart or sourced new figures unless done.
- Match audience vocabulary; use plain, exact wording without deleting necessary technical detail.

### 5. Adversarial review before delivery

Check for (a) unsupported/false causal or quantitative claims, (b) missing baseline, timeframe, denominator, uncertainty or counterevidence, (c) an overfitted emotional arc, (d) a buried BLOT, (e) inaccessible or misleading visual recommendations, and (f) unclear implication. **Evidence-integrity failures are blockers**, not polish suggestions. Use [quality-evaluation.md](references/quality-evaluation.md) when critiquing or assessing a substantial deliverable. Revise proportionately; do not add ritual headings or explanations that the user did not request.

## Output by mode

- **Draft / rewrite:** output the artifact first. Add only material caveats or a short change note when useful. Never append an unrequested full methodology, 3-minute version, or alternative that dilutes the requested format.
- **Outline:** propose section/slide-level conclusion titles, supporting evidence, transitions, and open evidence gaps.
- **Critique:** rank up to three consequential issues, state evidence-based fixes, and illustrate one revised opening/headline if useful. Distinguish a factual defect from a stylistic preference.
- **Executive presentation when requested:** provide a one-line BLOT and a ~3-minute compression, preserving evidence, unless the user explicitly wants only one format.

## Reference routing

Read only what the task requires:

- [HOW_TO_STORYTELLING.md](references/HOW_TO_STORYTELLING.md) — original narrative method and seven plot descriptions.
- [narrative-patterns.md](references/narrative-patterns.md) — advanced SCQ/BLOT, contrast, transformation, and short-form choices.
- [evidence-integrity.md](references/evidence-integrity.md) — quantitative claims, provenance, uncertainty, and causal language.
- [visual-guidance.md](references/visual-guidance.md) — chart selection, ethical graphics, and accessibility.
- [quality-evaluation.md](references/quality-evaluation.md) — audit rubric and release checks.
- [research-crosswalk.md](references/research-crosswalk.md) — dated, independently traceable research and how it changed this skill. Use it to trace guidance; do not assume external sources have been freshly rechecked during the current task.
- [evaluation-cases.md](references/evaluation-cases.md) — behavioral test cases for human- or agent-run evals; not evidence of test execution.

## Examples of explicit invocation

- `Use $data-storytelling to build an evidence-led executive argument from this quarterly report.`
- `Critique this LinkedIn post with $data-storytelling: preserve my voice and identify unsupported claims.`
- `Create a five-slide outline for this proposal, with conclusion headlines and traceable figures.`

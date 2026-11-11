# Visual storytelling, integrity, and accessibility

Consult only for slides, chart recommendations, visual critique, or graphic-heavy written communication. This is a checklist and chart selection aid, not a graphics generation tool.

## Choose by analytical relationship

| Evidence / question | Usually effective | Common failure |
| --- | --- | --- |
| Magnitudes or categories | Sorted bars, dot plot | Distorted baseline; unnecessary pie |
| Change over time | Line (continuous series), columns (discrete intervals) | Cherry-picked window, smoothed curve hiding variation |
| Deviation from target | Diverging bar / dot plot with a target reference | No stated target, inconsistent scenario notation |
| Distribution or spread | Histogram, box/violin/dot plot where audience can interpret it | Mean-only story hiding heterogeneity |
| Association | Scatterplot, with sample/context | Claiming causation from correlation |
| Parts of a whole | Stacked bar, 100% stacked bar, table | Totals unclear or parts that do not sum coherently |
| Precise few values | Text or small table | A chart that makes comparison harder |
| Geographic pattern | Map, only when spatial dimension matters | Using a map for nonspatial ranking |

The FT Visual Vocabulary and GOV.UK/ONS chart guides are references for broader chart selection; do not treat this table as exhaustive or mechanically optimal.

## Ethics and visual integrity

- Bars/columns encode magnitude with length: start quantitative baseline at zero. If that obscures a meaningful small difference, consider a labeled dot/range plot or a transparent tabular comparison rather than a deceptive bar.
- A line chart may use a nonzero vertical baseline when justified; clearly label it and avoid exaggeration. Keep consistent scales across comparable panels.
- State the **time period, value definitions, units, relevant comparator, source, and date of extraction** where material. Clearly distinguish actual, budget, forecast, and target using consistent notation.
- Avoid 3-D, decorative gradients, misleading dual axes, censored categories, or truncated timelines that obscure the actual finding.
- Use a **takeaway headline** when the conclusion is supported, and a **precise statistical title/subtitle** describing measure, population, period, and geography when necessary. These are complementary, not conflicting requirements.
- Annotations should clarify real changes, discontinuities, and uncertainties; they must not imply unsupported causes.
- Show uncertainty where it changes interpretation (bands or ranges as appropriate); explain what the interval means in plain language and do not infer significance solely from overlap.
- Prefer direct labels to distant legends when practical. Use color intentionally and consistently, not as the sole means of distinguishing data.

## Accessibility

- A chart's key message must be available as readable text. Provide concise alt text for simple graphics and a longer description/table for complex ones as appropriate.
- Avoid using color alone to carry meaning; use labels, patterns, symbols, or direct annotations as needed, with appropriate contrast and legible type.
- Avoid presenting necessary chart titles, source information, or conclusions exclusively as pixels within an image when the platform allows accessible surrounding text.
- Ensure the reading sequence makes sense without builds/animations. Progressive reveals are optional and only for a live presentation where the full information remains accessible afterward.
- Review chart and text together. A visual should support a defensible insight, never substitute for a source or explanation.

Sources: StatCan (2023); Datawrapper axis guidance; UK ONS, GOV.UK Design System and W3C WAI; IBCS 2.0 (2026) for consistent business notation. The IBCS guidance is a reference, not a claim of formal compliance. See [research-crosswalk.md](research-crosswalk.md).

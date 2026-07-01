# Chart — JioGames DLS spec

> Source: `chart/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Chart

---

Data visualisation for playtime trends, achievement progress, leaderboard history, and gaming stats. JioGames supports three chart types only: bar, line, and donut.

Chart · bar (comparison), line (with area), donut (72% completion)

Chart renders data as one of three approved visual forms: bar, line, or donut. These three types cover every gaming data story JioGames needs to tell — time-based comparisons (bar), trends over time (line), and proportions (donut). Other chart types (pie, scatter, radar) are explicitly excluded from the system. If your data does not fit bar, line, or donut, reconsider whether a chart is the right representation at all.

- **Bar** — comparing values across discrete categories: daily playtime, games by genre, score by session
- **Bar (comparison)** — two bars per category using primary and secondary fills: this week vs last week
- **Line** — trends over continuous time: XP earned per week, ranking position over months
- **Donut** — single proportional metric: achievement completion %, pass usage, storage consumed

- Always include a chart title and a source / date subtitle
- Start Y-axis at 0 — never truncate the baseline to exaggerate a trend
- Use `--jio` for the primary metric, surface-3 for comparison or secondary series
- Show tooltips on hover with the exact numeric value
- Provide a data table alternative for screen readers below every chart
- Use the donut center label to show the primary percentage value

- Use more than 2 colors in a single chart — third color introduces ambiguity
- Use pie charts — always use Donut
- Show a line chart on mobile — small screens make data points too close together; use bar instead
- Omit the legend when two series are shown — always label both
- Use chart animations on TV — hover tooltips and transitions don't apply at distance

1. 1 Grid lines Optional Horizontal reference lines at each Y-axis tick. Use --border-subtle (rgba(255,255,255,.08)) — subtle enough not to compete with data marks. `stroke: var(--border-subtle); stroke-width: 1`
2. 2 Y-axis labels Required Right-aligned text anchored to the left of the chart area. 10px, text3 color. Always start at 0. Max 5 ticks. Include unit abbreviation on the top tick only (6h, not on every tick). `font-size:10px; fill:var(--text3); text-anchor:end`
3. 3 Data mark (bar / line / donut arc) Required Bar: rect with rx:2 and --jio fill. Line: polyline with stroke:--jio, fill:none. Donut: circle with stroke-dasharray driving the filled arc. All support hover opacity reduction. `fill:var(--jio) | stroke:var(--jio)`
4. 4 X-axis labels Required Center-anchored text below each bar group or data point. 10px, text3 color. Abbreviate to fit — "Mon" not "Monday", "Wk 1" not "Week 1". `font-size:10px; fill:var(--text3); text-anchor:middle`

## Variants

Six approved chart forms built from three base types. Each has a fixed semantic role — do not substitute one for another.

## Sizes

Chart height is defined by three tiers. Width is always 100% of the container — never fixed-width charts.

| Size | Class | SVG height | Use case |
|---|---|---|---|
| S | `.chart--s` | `120px` | Sparkline in a stat card, compact dashboard widget |
| M | `.chart--m` | `200px` | Default — profile stats, game detail analytics |
| L | `.chart--l` | `300px` | Full-page analytics view, expanded playtime breakdown |

## States

Charts have four non-interactive states and one interactive hover state.

## Content guidance

- Chart title: noun phrase describing the metric — "Weekly playtime", not "Your Stats"
- Subtitle: data source and date range — "Hours · Jun 2026"
- Y-axis: include unit abbreviation on the top tick only — "6h" not "6 hours"
- X-axis: abbreviate to single letters or "Wk N" — never full day or month names
- Legend labels: 2–3 words maximum per series

- Primary series: always `--jio` (#00A859)
- Secondary / comparison series: always surface-3 (rgba(255,255,255,.1))
- Maximum 2 colors in any single chart — no third data series
- Never use red for a data series — it reads as an error state
- Donut track (unfilled portion): surface-3, never transparent

## Platform considerations

- Bar and Donut only — line charts are hard to read on narrow viewports
- Use S or M size — L height forces unwanted vertical scroll
- Tap on a bar to show the tooltip (no hover on touch)
- Donut center label minimum 20px for legibility on small screens
- Provide the data table alternative visually collapsed but screen-reader accessible

- All three chart types available
- Hover on data marks shows tooltip with exact value
- Use M or L size depending on the page layout
- Legend can be positioned right of the chart if space allows
- SVG charts must have `role="img"` + `aria-label` describing all data

- Donut only — bar and line require precise spatial reading at 3m
- Donut center label minimum 36px
- Legend text minimum 18px
- No hover tooltips — show exact value in center label or legend
- No animations — static render only at TV scale

## Accessibility

SVG charts are invisible to screen readers unless explicitly described. Every chart must have two accessibility surfaces: an aria-label on the SVG summarising the data, and a visually hidden data table below.

| Requirement | Implementation | Guidance |
|---|---|---|
| SVG description | `role="img" aria-label` | aria-label must describe the chart type and key data points: "Bar chart: weekly playtime. Mon 1.5h, Tue 3h, Wed 2h, Thu 4h, Fri 5h, Sat 6.5h, Sun 4.5h". |
| Data table alternative | `` below chart | Provide a visually hidden data table (class="sr-only") with the same data as the chart. Screen readers navigate it with standard table commands. |
| Individual bars / points | `` inside SVG element | Each <rect> or <circle> can have a <title> child: <title>Fri · 5h</title>. Browsers surface this as a tooltip and some screen readers read it. |
| Color contrast | --jio on dark bg | Green (#00A859) on dark background (#080a10) passes WCAG AA at 3.2:1 for large graphical elements. For text labels, use --text3 which passes at 4.5:1. |
| Tooltip | `aria-live="polite"` | If the tooltip is a DOM element (not just a browser title attribute), wrap it in an aria-live region so screen reader users hear the value on hover/focus. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Primary data series fill (bars), line stroke, donut arc stroke |
| `--surface-3` | `rgba(255,255,255,.1)` | Secondary / comparison bar fill, donut track stroke |
| `--border-subtle` | `rgba(255,255,255,.08)` | Grid line stroke color |
| `--text3` | `rgba(244,242,238,.32)` | Axis label text fill, subtitle color |
| `--text` | `#f4f2ee` | Chart title, donut center label |
| `--surface-2` | `—` | Tooltip background, loading skeleton fill |
| `--jio-font` | `'Outfit', sans-serif` | All SVG text — axis labels, donut center, title |
| `--r4` | `—` | Tooltip border-radius |

## When to use

Use when

- Pass usage statistics and game time analytics in profile
- Leaderboard score progression over time
- Revenue/download metrics in internal dashboards
- Achievement completion rates as radial or bar charts

Don't use when

- Replacing data tables when exact values matter more than trends
- More than 7 data series on a single chart — cognitive overload
- Purely decorative data visualization without accessible text fallback

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Bar grow | `--ease-out` | `--dur-slow` | height (staggered per bar) |
| Line draw | `--ease-out` | `--dur-slow` | stroke-dashoffset |
| Tooltip appear | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px) |
| Legend item hover | `--ease-out` | `--dur-fast` | opacity (others dim to 0.4) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-chart` | Root chart wrapper — sets height and position:relative |
| `.ds-chart__canvas` | Chart.js canvas element |
| `.ds-chart__legend` | Custom legend row above/below chart |
| `.ds-chart__legend-item` | Color swatch + label pair |
| `.ds-chart__tooltip` | Custom tooltip overlay |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `type` | "bar" | "line" | "area" | "donut" | "radial" | "bar" | Chart type |
| `data` | ChartData | required | Chart.js-compatible data object |
| `height` | number | 240 | Canvas height in px |
| `legend` | boolean | true | Show custom legend |
| `animate` | boolean | true | Enable enter animations |

## Code examples

````html
<div class="chart-wrap chart--m">
  <div class="chart-title">Weekly playtime</div>
  <div class="chart-subtitle">Hours · Jun 2026</div>
  <svg class="chart-svg"
       viewBox="0 0 220 120"
       role="img"
       aria-label="Bar chart: daily playtime this week. Mon 1.5h, Tue 3h, Wed 2h, Thu 4h, Fri 5h, Sat 6.5h, Sun 4.5h">

    <!-- Grid lines -->
    <line x1="24" y1="10" x2="216" y2="10" class="chart-grid-line"/>
    <line x1="24" y1="40" x2="216" y2="40" class="chart-grid-line"/>
    <line x1="24" y1="70" x2="216" y2="70" class="chart-grid-line"/>

    <!-- Y-axis labels -->
    <text x="20" y="13" class="chart-axis-label" text-anchor="end">6h</text>
    <text x="20" y="43" class="chart-axis-label" text-anchor="end">3h</text>
    <text x="20" y="73" class="chart-axis-label" text-anchor="end">0</text>

    <!-- Bars -->
    <rect x="30" y="66" width="18" height="19" class="chart-bar" rx="2">
      <title>Mon · 1.5h</title>
    </rect>
    <!-- repeat for each day -->

    <!-- X-axis labels -->
    <text x="39" y="100" class="chart-axis-label" text-anchor="middle">M</text>
    <!-- repeat -->

  </svg>
</div>
````

````html
<svg class="chart-svg" viewBox="0 0 220 120"
     role="img"
     aria-label="Line chart: achievement XP per week. Wk1 400, Wk2 650, Wk3 580, Wk4 820">

  <defs>
    <linearGradient id="chart-gradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#00A859" stop-opacity="1"/>
      <stop offset="100%" stop-color="#00A859" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Area fill -->
  <polygon
    points="44,61 108,38 172,44 216,16 216,85 44,85"
    fill="url(#chart-gradient)"
    opacity="0.2"/>

  <!-- Line -->
  <polyline
    points="44,61 108,38 172,44 216,16"
    class="chart-line"
    stroke-linejoin="round"
    stroke-linecap="round"/>

  <!-- Data points -->
  <circle cx="44"  cy="61" r="3.5" fill="var(--jio)"><title>Wk1 · 400 XP</title></circle>
  <circle cx="108" cy="38" r="3.5" fill="var(--jio)"><title>Wk2 · 650 XP</title></circle>
  <circle cx="172" cy="44" r="3.5" fill="var(--jio)"><title>Wk3 · 580 XP</title></circle>
  <circle cx="216" cy="16" r="3.5" fill="var(--jio)"><title>Wk4 · 820 XP</title></circle>

</svg>
````

````
<!--
  Donut math:
  circumference = 2 * π * r = 2 * 3.14159 * 44 ≈ 276.5
  filled arc    = percentage * circumference
  72%           = 0.72 * 276.5 ≈ 199.1

  stroke-dasharray = "filled_arc total_circumference"
  stroke-dashoffset rotates start point: offset = circumference * 0.25
                    (to start at top instead of right)
-->
<svg width="160" height="160" viewBox="0 0 120 120"
     role="img"
     aria-label="Donut chart: 72% achievement completion for Tomb Raider">

  <!-- Track (unfilled) -->
  <circle cx="60" cy="60" r="44"
          class="chart-donut-track"
          stroke-width="10"/>

  <!-- Fill arc -->
  <circle cx="60" cy="60" r="44"
          class="chart-donut-fill"
          stroke-width="10"
          stroke-dasharray="199.5 277"
          stroke-dashoffset="69"
          transform="rotate(-90 60 60)"/>

  <!-- Center label -->
  <text x="60" y="55"
        class="chart-donut-label"
        text-anchor="middle"
        dominant-baseline="middle">72%</text>
  <text x="60" y="72"
        class="chart-donut-sublabel"
        text-anchor="middle">complete</text>

</svg>

<!-- Accessible data table (visually hidden) -->
<table class="sr-only">
  <caption>Tomb Raider achievement completion</caption>
  <tr><th>Status</th><th>Percentage</th></tr>
  <tr><td>Achieved</td><td>72%</td></tr>
  <tr><td>Remaining</td><td>28%</td></tr>
</table>
````

## Changelog

Initial draft. Covers bar, bar comparison, line, line with area, donut, and donut with label variants. S/M/L sizes. Loading, empty, error, and hover states. Full accessibility guidance including aria-label patterns and data table alternative. Pie chart explicitly excluded from system.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-default`
- `--dur-enter`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--text4`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

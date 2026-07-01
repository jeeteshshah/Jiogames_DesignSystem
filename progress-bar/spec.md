# Progress Bar — JioGames DLS spec

> Source: `progress-bar/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Progress Bar

---

Linear indicators for determinate progress — game completion, download status, achievement fill, and streaming buffer.

DETERMINATE · INDETERMINATE · ACHIEVEMENT · THIN

## Introduction

Progress bars communicate linear advancement toward a known or unknown endpoint. Use them in JioGames for game completion percentage displayed on card overlays, download and install progress, achievement or XP fill, and video buffering state. Do not use progress bars for video scrubber/seek controls — use a dedicated media scrubber component for those. Do not use them for step indicators (use page-dots), ratings (use star or score display), or any non-linear state.

## When to use

Use when

- Game download and install progress
- Achievement completion percentage on profile
- Level XP fill bar in user stats
- Multi-step form completion indicator

Don't use when

- Indeterminate loading (unknown duration) — use a Skeleton or spinner
- Binary complete/incomplete states — use a Checkbox or badge
- Values that change so rapidly users can't read them (realtime)

## Best practices

Rules that govern correct usage across all progress bar contexts.

- Always show a percentage label alongside the bar when space allows — bar alone lacks precision for values like 72%
- Use green fill for positive progress, gold for achievement or XP, and red (--negative) strictly for error or limit states
- Set a minimum fill width of 4px to prevent invisible progress for values near 0%
- Use the indeterminate variant when duration is genuinely unknown — never fake animation on a determinate bar
- TV: increase bar height to 8px minimum for legibility at 10-foot viewing distance

- Animate the fill of a determinate bar — fill width is data-driven, not decorative
- Use a progress bar for navigation step count — use page-dots instead
- Use color as the only state signal — always pair fill color with a label or ARIA attribute
- Show a determinate bar for truly unknown durations — use the indeterminate variant
- Stack multiple progress bars on a single card — it creates visual noise and dilutes meaning

## Anatomy

The progress bar is composed of a track and a fill. Labels are always external to the component.

1. 1 Track Required Full-width background container. Always pill-shaped. Defines the maximum extent of progress. `background: var(--surface-3)`
2. 2 Fill Required Colored bar inside the track, width driven by the progress value (0–100%). Minimum 4px width. `background: var(--jio); min-width: 4px`
3. — Label External Not part of the component element — rendered outside. Format: "72% completed", "1.2 GB of 4.5 GB". `font-size: 11px; color: var(--text3)`

| Part | Element | Token |
|---|---|---|
| Track | `div.progress-bar` | `background: var(--surface-3)` |
| Fill | `div.progress-bar__fill` | `background: var(--jio)` |
| Fill — achievement | `div.progress-bar__fill--gold` | `background: var(--popular-gold)` |
| Fill — error | `div.progress-bar__fill--error` | `background: var(--negative)` |
| Fill — indeterminate | `div.progress-bar__fill--indeterminate` | animated `var(--jio-bright)` |
| Label | outside component | `font-size: 11px; color: var(--text3)` |

## Variants

Four variants cover all progress bar use cases in the JioGames product. Each has a fixed semantic meaning — do not repurpose colors across variants.

## Sizes

Bar height adapts to context. Thin for dense overlays, default for standard cards, thick for prominent download screens, TV for 10-foot legibility.

| Size | Height | Usage |
|---|---|---|
| Thin | `3px` | Video overlay, card micro-progress |
| Default | `6px` | Standard usage — game cards, profiles |
| Thick | `10px` | Prominent progress — download screens |
| TV | `8px min` | All TV contexts, 10-foot legibility requirement |

## States

Progress bars have four behavioral states. State is always conveyed through fill width, fill color, and label — never through the bar alone.

## Content guidance

Progress labels communicate quantity and completion. Precision matters — vague labels erode trust.

- Use numeric format: "72% completed", "1.2 GB of 4.5 GB", "Level 34/50"
- Never use vague labels like "Almost done" or "Loading…" without a number
- Always pair a percentage or ratio with the bar when the container allows
- Right-align short percentage labels alongside the bar end to save vertical space
- Place longer labels (e.g. "1.2 GB of 4.5 GB") below the bar

- Percentage symbol placement varies by locale — use the platform locale formatter
- File size units (GB/MB) should follow regional convention
- Keep labels concise — translated strings can run 30% longer than English
- "Completed" may be omitted in compact contexts — "72%" alone is acceptable if space is tight
- RTL: the bar fill direction reverses; labels stay in reading order

## Platform considerations

Bar height and label placement adapt per platform. Semantics and color tokens remain constant.

- 6px default height for game cards and profile screens
- 3px thin on card art overlays where space is constrained
- Label placed below bar, or right-aligned on same row for short percentages
- Touch targets don't apply — progress bars are non-interactive
- Indeterminate animation safe at 1.4s — slow enough to not feel jittery

- Same 6px default height as mobile
- Wide layout allows label to sit right of the bar on the same line
- Native `` element preferred — degrades gracefully without JS
- Cursor remains default — bars are not interactive elements
- Large download screens may use 10px thick variant for prominence

- 8px minimum height — 6px is unreadable at 3-metre viewing distance
- Bold label placed above bar, not below — easier to read top-down
- Indeterminate preferred for loads — avoids stalling animation perception
- D-pad focus never lands on the bar — ensure adjacent interactive element holds focus
- Do not use thin (3px) variant on TV under any context

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Fill advance | `--ease-out` | `--dur-slow` | width |
| Complete flash | `--ease-out` | `200ms` | background → white → jio |
| Appear | `--ease-out` | `--dur-fast` | opacity |
| Indeterminate shimmer | `linear` | `1400ms infinite` | background-position |

## Accessibility

Progress bars must be perceivable without relying on color or visual position. Use native elements where possible; apply ARIA when using custom markup.

| Case | Attribute / approach | Guidance |
|---|---|---|
| Native element | `` | Preferred — browser exposes value to assistive tech automatically. Include fallback text content: `72%` inside the element. |
| Custom div — determinate | `role="progressbar"`, `aria-valuenow`, `aria-valuemin="0"`, `aria-valuemax="100"`, `aria-label` | All four attributes required. `aria-label` should describe the context — "Game download progress", not just "Progress bar". |
| Indeterminate | Omit `aria-valuenow` | When duration is unknown, omit `aria-valuenow` — screen readers will announce the bar as indeterminate. |
| Color-only states | Always pair with label text | Color alone never conveys state — error red must be accompanied by an error label. Achievement gold must have a label like "40 / 100 XP". |
| Reduced motion | `@media (prefers-reduced-motion)` | Indeterminate animation stops; fill set to 100% at 0.4 opacity to signal loading without motion. Implemented in the component CSS. |

## Related tokens

Always reference tokens — never hardcode hex values. Tokens update with the theme; hardcoded values do not.

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Default fill — positive progress, game completion |
| `--jio-bright` | lighter green | Indeterminate fill — animated sliding indicator |
| `--popular-gold` | `#FFCF5C` | Achievement fill — XP bars, trophy progress |
| `--negative` | red | Error fill — storage limit, download failure |
| `--surface-3` | `#1F2432` | Track background on dark surfaces |
| `--pill` | `100px` | Border-radius for track and fill — maintains pill shape at all heights |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-progress` | Root track — surface-2, r-pill, overflow hidden |
| `.ds-progress__fill` | Filled portion — jio-green bg, height 100% |
| `.ds-progress--sm` | 4px height |
| `.ds-progress--md` | 8px height (default) |
| `.ds-progress--lg` | 12px height |
| `.ds-progress--indeterminate` | Animated shimmer — unknown duration |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | number | required | Current progress 0–100 |
| `max` | number | 100 | Maximum value |
| `size` | "sm" | "md" | "lg" | "md" | Track height preset |
| `indeterminate` | boolean | false | Show shimmer animation instead of fill |
| `color` | string | var(--jio) | Fill color — CSS token recommended |
| `label` | string | undefined | Accessible aria-label for screen readers |

## Code examples

Copy these as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<!-- Native progress element (preferred) -->
<div class="progress-bar" role="none">
  <progress class="progress-bar__fill" value="72" max="100">72%</progress>
</div>
<span class="progress-label">72% completed</span>
````

````
<!-- Custom div with ARIA -->
<div class="progress-bar"
     role="progressbar"
     aria-valuenow="40"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-label="Achievement progress">
  <div class="progress-bar__fill progress-bar__fill--gold"
       style="width: 40%"></div>
</div>
````

````
<!-- Indeterminate loading -->
<div class="progress-bar"
     role="progressbar"
     aria-label="Loading game data">
  <div class="progress-bar__fill progress-bar__fill--indeterminate"></div>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--ease-out`
- `--jio`
- `--jio-bright`
- `--negative`
- `--pill`
- `--popular-gold`
- `--surface-1`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

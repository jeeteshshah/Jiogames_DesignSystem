# Spacing — JioGames DLS spec

> Source: `spacing/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Spacing

---

8px-base spacing scale with semantic aliases for gutters, gaps, padding, and section rhythm across Mobile, Web, and TV.

8PX BASE GRID · 13 STEPS · SEMANTIC ALIASES

## Spacing scale

12 tokens built on an 8px base unit. Bar width equals the actual pixel value — the visual relationship between values is real.

## Semantic spacing tokens

Semantic aliases resolve to the correct value per platform via media queries. Use the alias — never the scale step directly — for all layout roles listed here.

| Token | Mobile | Web ≥768px | TV ≥1280px | Usage |
|---|---|---|---|---|
| --gutter | 16px | 40px | 80px | Side margins for all content |
| --section-gap | 32px | 48px | 64px | Gap between page sections / rails |
| --rail-gap | 32px | 48px | 64px | Gap between rail rows |
| --card-gap | 12px | 24px | 24px | Gap between cards in a rail |
| --component-padding | 16px | 24px | 32px | Internal padding for most components |
| --card-padding | 16px | 24px | 32px | Card internal padding |
| --sheet-padding | 24px | 32px | — | Bottom sheet / drawer internal padding |
| --hero-gap | 32px | 64px | 96px | Gap below hero sections |

## 8px base grid

Every spacing value is a multiple of 8px, or a half-step at 4px. This creates consistent vertical rhythm and aligns elements across different screen densities.

## Column grid & breakpoints

JioGames uses a 4-column grid on mobile, 12-column on web and TV. Gutters and column gaps are token-driven. Breakpoints are min-width based — mobile is the base; web and TV layers override.

### Breakpoints

| Name | Token | Value | Target surface |
|---|---|---|---|
| Mobile (base) | `—` | 0px+ | Phone portrait, small screens |
| Web | `--bp-web` | 768px+ | Tablet, desktop browser |
| TV | `--bp-tv` | 1280px+ (and min-height 720px) | Smart TV, set-top box |

### Column counts & gaps

| Platform | Columns | Column gap token | Gap value | Gutter (edge) |
|---|---|---|---|---|
| Mobile | 4 | `--col-gap-mobile` | 12px | `--gutter` (20px) |
| Web | 12 | `--col-gap-web` | 24px | `--container-web` centred, 48px side padding |
| TV | 12 | `--col-gap-tv` | 32px | `--tv-safe` (80px) safe-zone on all edges |

### Z-index scale

Use `var(--z-*)` tokens — never raw integers. Deviating from the scale causes stacking conflicts between nav, modals, toasts, and overlays.

| Token | Value | Used by |
|---|---|---|
| `--z-base` | 0 | Default in-flow elements |
| `--z-raised` | 10 | Cards on hover, lifted surfaces |
| `--z-dropdown` | 100 | Select dropdowns, Combobox, Popover |
| `--z-sticky` | 200 | Sticky table headers, pinned rails |
| `--z-appbar` | 300 | AppBar (always above page content) |
| `--z-drawer` | 400 | Drawer / side panel |
| `--z-modal` | 500 | Dialog, Bottom Sheet, Command palette |
| `--z-toast` | 600 | Toast notifications (above modals) |
| `--z-tooltip` | 700 | Tooltip, Hover Card (always topmost) |
| `--z-tvFocus` | 800 | TV focus ring overlay |

## Usage rules

Enforced by `tokens/validate.sh`. ERRs block shipping. WARNs must be justified in the QA report.

## Quick reference

All 12 scale tokens at a glance. Bookmark this for day-to-day use.

| Class | Gap token | When to use |
|---|---|---|
| .page-stack | --section-gap | Major page sections, rails on the home screen |
| .hero-stack | --hero-gap | Hero region to first content section |
| .component-stack | --component-padding | Components stacked inside a section |
| .content-stack | --space-1-5 (12px) | Related elements — title + body, label + value |
| .tight-stack | --space-1 (8px) | Tight group — icon + label, badge + text |

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border-subtle`
- `--card-bg`
- `--divider`
- `--glass-1`
- `--gutter`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--negative`
- `--pill`
- `--r1`
- `--r2`
- `--r3`
- `--r4`
- `--space-0-5`
- `--space-1`
- `--space-1-5`
- `--space-2`
- `--space-3`
- `--space-4`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--text4`
- `--z-`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# Templates — JioGames DLS spec

> Source: `templates/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Templates

---

Reusable page templates for common JioGames screens. Each defines layout, component composition, CTA placement, and state handling.

MOBILE HOME · GAME DETAIL · EMPTY STATE

## Template catalog

12 screen templates covering the full JioGames user journey.

## Mobile Home template

The primary discovery screen. Full-bleed hero auto-advances; rails scroll horizontally. Tab bar fixed to bottom.

| Attribute | Value |
|---|---|
| Primary CTA | btn--primary |
| Secondary CTA | btn--ghost |
| Layout | Full-bleed hero + rails |
| Hero height | 220px mobile |
| Rail card width | 160px (var(--card-wide-w)) |
| Tab bar | ✓ Fixed bottom, 64px |
| AppBar | ✓ Sticky top, 56px |
| Components | AppBar, Hero, Card, Rail, TabBar |
| Scroll | Vertical page, horizontal rails |
| Safe area | Tab bar: env(safe-area-inset-bottom) |

## Game Detail template

Full-bleed hero with an overlay AppBar. Game metadata, rating, Play CTA, and content tabs below the fold.

| Attribute | Value |
|---|---|
| Primary CTA | btn--primary full-width |
| Secondary CTA | btn--ghost icon-only (add to library) |
| Hero height | 240px with overlay AppBar |
| AppBar style | Overlay — transparent on hero |
| Tab bar | ✗ Not present on detail |
| Content tabs | Underline style — Overview, Details, Related |
| Components | AppBar (overlay), Hero, Button, Tabs, Rail |

## Empty State template

Used when no content is available — empty library, no search results, no notifications. Single primary CTA guides the user to action.

| Attribute | Value |
|---|---|
| Icon container | 80×80px, border-radius:var(--pill), background:var(--surface-2) |
| Heading | 20px, weight 900, letter-spacing:-.3px |
| Body | 14px, var(--text3), line-height:1.6, max 2 lines |
| CTA | btn--primary, btn--hug (not full width) |
| Alignment | Centered vertically and horizontally |
| Components | Icon, Typography, Button |

## Error State template

Shown when a screen fails to load. Primary action: retry. Secondary action: fallback navigation. Error icon tinted with var(--negative).

| Attribute | Value |
|---|---|
| Icon container | 80×80px, background:rgba(255,71,87,.1) — approved gradient recipe |
| Primary CTA | btn--primary btn--sm — "Try again" |
| Secondary CTA | btn--ghost btn--sm — "Go home" |
| CTA layout | Row, gap:10px, both btn--hug |
| Message tone | Neutral, factual — never alarming copy |
| Components | Icon, Typography, Button, Button--ghost |

## Offline State template

Shown when network is unavailable. Single retry CTA. Neutral grey icon tinted — not red (error is different from offline).

| Attribute | Value |
|---|---|
| Icon container | 80×80px, background:rgba(107,114,128,.1) — neutral, not var(--negative) |
| CTA | btn--ghost btn--sm btn--hug — single "Retry" |
| Differentiation | Grey icon = offline; red icon = error — never swap |
| Components | Icon, Typography, Button--ghost |

## Template usage guidelines

Rules that apply across all templates.

## Do / Don't

## Template Structure

Every mobile template is composed of three fixed layers stacked in a column. Content layer scrolls between the fixed AppBar and Tab Bar.

| Layer | Height | Position | Present on |
|---|---|---|---|
| AppBar | 56px | sticky top / overlay on hero | All mobile templates |
| Content | flex:1 (fills viewport) | scrollable, between bars | All templates |
| Tab Bar | 64px + safe-area-inset-bottom | fixed bottom | Home-level screens only |

## Accessibility

## Related Tokens

Tokens that govern template-level layout. Do not hardcode these values in template HTML.

| Token | Default value | Usage |
|---|---|---|
| `--bg` | #06080F | Page-level background — the darkest surface, used behind all content |
| `--surface-1` | #0E1119 | AppBar and card backgrounds — one step above page bg |
| `--surface-2` | #161A24 | Tab bar background and secondary surface areas |
| `--gutter` | 16px (mobile) · 40px (web) · 80px (TV) | Horizontal page padding — applied to AppBar and all content sections |
| `--section-gap` | 32px (mobile) · 48px (web) · 64px (TV) | Vertical spacing between major page sections (rails, heroes) |
| `--card-gap` | 12px (mobile) · 24px (web) | Gap between cards inside rails and grids |
| `--hero-gap` | 32px (mobile) · 64px (web) · 96px (TV) | Spacing below the hero section before the first content rail |
| `--app-bar-h` | 64px | AppBar height token — use for scroll threshold and layout offset calculations |
| `--tab-bar-h` | 64px | Tab bar height — add to scroll container bottom padding to prevent content obscuring |
| `--safe-top` | env(safe-area-inset-top, 0px) | iOS status bar safe area — add to AppBar padding-top |
| `--safe-bot` | env(safe-area-inset-bottom, 0px) | iOS home indicator safe area — add to tab bar padding-bottom |
| `--container-web` | 1280px | Max content width on web. Center with `margin:0 auto`. |
| `--overlay-image` | linear-gradient(180deg, transparent 40%, rgba(6,8,15,.9) 100%) | Hero image bottom gradient overlay — fades game art into page background |
| `--card-overlay` | linear-gradient(0deg, rgba(6,8,15,.85) 0%, transparent 55%) | Bottom overlay on card art — keeps title legible over game imagery |
| `--frame-mobile-w` | 393px | Reference mobile frame width — use for prototype phone frames and max-width caps |
| `--tv-safe` | 80px | TV overscan safe area inset — all content must stay inside this margin |

## Rules

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--card-wide-w`
- `--ctrl-h`
- `--jio`
- `--jio-soft`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--r7`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`
- `--text4`
- `--violet`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# Radius — JioGames DLS spec

> Source: `radius/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Radius

---

Nine graduated radius tokens plus a pill token. Components never use bare pixel values for border-radius.

9 GRADUATED STEPS + PILL · COMPONENT MAPPING

## Radius scale

Each token represents a step in the radius hierarchy. Smaller values anchor artwork-led surfaces; larger values belong to interactive chrome and overlay layers.

## Component → radius mapping

One component, one token. Deviations from this table require a governance update.

| Component | Token | Value | Notes |
|---|---|---|---|
| Buttons | --pill | 100px | Full pill shape always |
| Primary CTA | --pill | 100px | Never use --r9 for buttons |
| Cards (default) | --r4 | 14px | Standard landscape/square game card |
| Cover portrait card | --r5 | 16px | Portrait artwork image |
| Hero / marquee cards | --r2 | 10px | Larger canvas — smaller radius |
| Bottom sheets | --r9 --r9 0 0 | 28px | Top corners only; bottom is flush |
| Inputs & text fields | --r5 | 16px | Phone input, text fields |
| OTP boxes | --r4 | 14px | Individual digit cell |
| Chips & tags | --pill | 100px | Action chips always pill |
| Platform chips (tile) | --r4 | 14px | Taller tile format — pill looks wrong |
| Dialogs & modals | --r7 | 20px | All corners |
| Pass cards | --r7 | 20px | Premium surface |
| Upsell cards | --r7 | 20px | Same tier as pass card |
| Genre tiles | --r5 | 16px | Interactive overlay |
| USP tiles | --r6 | 18px | Between card and pass tier |
| Notifications / toast | --r3 | 12px | Toast + in-app banners |
| Tooltips | --r2 | 10px | Small transient callout |
| Tab bar container | --pill | 100px | Floating pill tab bar |
| Search bar | --pill | 100px | Always pill |
| Badge / pill | --pill | 100px | Inline count or label |
| Progress bar | --pill | 100px | Track + fill both pill |
| GFF / info card | --r3 | 12px | Compact info module |
| Avatar / profile image | 50% | circular | Only case where 50% is allowed |

## Corner-specific radii

Some components use partial radius — top-only for sheets entering from the bottom, bottom-only for surfaces attached to the AppBar.

````
/* Bottom sheet: top corners only */
.bottom-sheet {
  border-radius: var(--r9) var(--r9) 0 0;
}

/* AppBar attached card: bottom corners only */
.appbar-card {
  border-radius: 0 0 var(--r5) var(--r5);
}
````

## Usage rules

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--demo-pill-h`
- `--demo-pill-w`
- `--demo-swatch`
- `--divider`
- `--glass-1`
- `--jio`
- `--pill`
- `--r1`
- `--r2`
- `--r3`
- `--r4`
- `--r5`
- `--r6`
- `--r7`
- `--r8`
- `--r9`
- `--space-1`
- `--space-2`
- `--space-3`
- `--surface-1`
- `--surface-2`
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

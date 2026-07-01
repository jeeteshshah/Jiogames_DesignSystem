# Colours — JioGames DLS spec

> Source: `colours/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Colours

---

JioGames colour system — brand green, surface ladder, text hierarchy, functional accents, and full token table.

BRAND · SURFACES · ACCENTS · ALL TOKEN-BASED

JioGames green in all its forms. The brand accent is exclusively green — no blue, indigo, or purple anywhere in the system.

The surface ladder — from the deepest page background to the highest opaque card. All surfaces are dark. Never use white or light-grey surfaces.

Five text tokens covering full range from primary readable content to disabled-only states. Note: --text3 and --text4 are below WCAG AA for small text.

| Token | Swatch | Hex | Usage | Contrast vs --bg |
|---|---|---|---|---|
| --text |   | #F4F2EE | Primary text | 14.5:1 AAA |
| --text2 |   | #A8ADBA | Secondary, labels | 6.8:1 AA |
| --text3 |   | #6B7280 | Muted, captions | 3.8:1 AA Large |
| --text4 |   | #454A57 | Disabled only | 2.1:1 Fail |
| --text-inv |   | #000000 | On bright/green surfaces | — |

Semantic tokens for specific UI states. Each has a single, governed meaning — do not repurpose them for decoration.

Transparent white overlays — all borders are tinted white at varying opacities, never solid grey. One special border for the Ultimate Pass tier.

| Token | Value | Usage |
|---|---|---|
| --border | rgba(255,255,255,.1) | Standard card border |
| --border-strong | rgba(255,255,255,.14) | Emphasized border |
| --border-subtle | rgba(255,255,255,.08) | Subtle separator |
| --border-ultimate | rgba(0,204,101,.3) | Ultimate Pass card border |
| --divider | rgba(255,255,255,.07) | Section dividers |
| --hairline | rgba(255,255,255,.08) | Hairline rules |

Every colour token in the system, in one place. Reference this when building components — never hardcode a hex value.

| Token | Swatch | Value | Usage |
|---|---|---|---|
| --jio |   | #00A859 | Primary brand green, CTA |
| --jio-2 |   | #22C16C | Hover, secondary highlight |
| --jio-3 |   | #88E5AB | Pale accent, icon tints |
| --jio-bright |   | #00E870 | Glow effects, live indicators |
| --jio-soft |   | rgba(0,168,89,.12) | Tag backgrounds, tinted fills |
| --jio-glow |   | rgba(0,200,100,.35) | Focus rings, active shadows |
| --ultimate |   | #00cc65 | All Screen Pass tier |
| --positive |   | #00A859 | Success states (= --jio) |
| --negative |   | #FF4757 | Error, destructive |
| --amber |   | #F59E0B | Warnings, expiry |
| --gold |   | #FFC23D | Ratings, premium |
| --popular-gold |   | #F7AB20 | Popular badge |
| --pink |   | #FF3D7F | Trending, spotlight |
| --bg |   | #06080F | Page background |
| --card-bg |   | #111115 | Card background |
| --surface-1 |   | #0E1119 | Elevated surface 1 |
| --surface-2 |   | #161A24 | Elevated surface 2 |
| --surface-3 |   | #1F2432 | Elevated surface 3 |
| --surface-4 |   | #2A3142 | Highest opaque surface |
| --chip-bg |   | #0c0f14 | Chip / tag background |
| --glass-1 |   | rgba(255,255,255,.055) | Subtle glass overlay |
| --glass-2 |   | rgba(255,255,255,.03) | Softest glass overlay |
| --text |   | #F4F2EE | Primary text |
| --text2 |   | #A8ADBA | Secondary text |
| --text3 |   | #6B7280 | Muted, captions |
| --text4 |   | #454A57 | Disabled only |
| --text-inv |   | #000000 | On bright green surfaces |
| --border |   | rgba(255,255,255,.1) | Standard border |
| --border-strong |   | rgba(255,255,255,.14) | Emphasized border |
| --border-subtle |   | rgba(255,255,255,.08) | Subtle separator |
| --border-ultimate |   | rgba(0,204,101,.3) | Ultimate Pass border |
| --divider |   | rgba(255,255,255,.07) | Section dividers |
| --hairline |   | rgba(255,255,255,.08) | Hairline rules |

Hard rules enforced by the DLS validator. Green rows are required practices. Red rows are prohibited — these will cause a validation ERR.

Verified WCAG 2.1 contrast ratios for the most common foreground/background pairings. AAA = 7:1+, AA = 4.5:1+, AA Large = 3:1+ (18px+ or 14px bold).

| Foreground | Background | Ratio | WCAG |
|---|---|---|---|
| --text#F4F2EE | --bg#06080F | 14.5:1 | AAA ✓ |
| --text2#A8ADBA | --bg#06080F | 6.8:1 | AA ✓ |
| --text3#6B7280 | --bg#06080F | 3.8:1 | AA Large only ⚠ |
| --text4#454A57 | --bg#06080F | 2.1:1 | Fail ✗ |
| --jio#00A859 | --bg#06080F | 4.6:1 | AA ✓ |
| --text#F4F2EE | --card-bg#111115 | 13.9:1 | AAA ✓ |
| --text2#A8ADBA | --card-bg#111115 | 6.5:1 | AA ✓ |
| --text#F4F2EE | --surface-2#161A24 | 12.1:1 | AAA ✓ |

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--card-bg`
- `--divider`
- `--glass-2`
- `--jio`
- `--jio-2`
- `--jio-bright`
- `--negative`
- `--pill`
- `--popular-gold`
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
- `--ultimate`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

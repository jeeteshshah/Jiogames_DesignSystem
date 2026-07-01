# Typography — JioGames DLS spec

> Source: `typography/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Typography

---

JioType is the exclusive typeface for JioGames. Four weights. One family. Zero exceptions.

JIOTYPE · 300 / 500 / 700 / 900 WEIGHTS · DARK FIRST

**Designers choose a semantic role, not a font size.** Every element maps to one of 21 type roles defined by the DLS. The platform resolves the pixel size automatically via media queries — Mobile is the base, Web overrides at 768px, TV at 1280px + 720px.

## Type scale

Each specimen uses the exact CSS class. Right panel shows mobile values — Web and TV scale up via media query.

Long readable body text for descriptions and introductory summaries where readability matters most.

Default body text for all standard content across the app. Most-used body size.

Secondary body text for helper content and supporting information in compact contexts.

Dense secondary copy for metadata and tight UI contexts where space is limited.

Last played 3 hours ago · 4.8 ★ · 120K reviews

Updated 2 days ago · 256MB · Age 12+

By continuing you agree to our Terms of Service and Privacy Policy. Auto-renews unless cancelled.

## Font weights

JioType has exactly four valid weights. Every other weight value is banned — including 400, 600, and 800.

## Font family

JioType is loaded via `@font-face` in tokens.css from `/Assets/font/`. It is always present on the DLS server. The fallback chain activates only on external machines where the font file is unavailable.

## Platform scaling

Designers assign a semantic role. The platform resolves the pixel size via media query. Never hand-pick a size for Web or TV.

| Style | CSS class | Mobile | Web ≥768px | TV ≥1280px | Weight |
|---|---|---|---|---|---|
| display-lg | `.text-display-lg` | 48 / 56 | 64 / 72 | 72 / 80 | 900 |
| display-md | `.text-display-md` | 40 / 48 | 56 / 64 | 64 / 72 | 900 |
| display-sm | `.text-display-sm` | 32 / 40 | 48 / 56 | 56 / 64 | 900 |
| headline-lg | `.text-headline-lg` | 28 / 36 | 40 / 48 | 48 / 56 | 900 |
| headline-md | `.text-headline-md` | 24 / 32 | 32 / 40 | 40 / 48 | 900 |
| headline-sm | `.text-headline-sm` | 22 / 28 | 28 / 36 | 32 / 40 | 700 |
| title-lg | `.text-title-lg` | 20 / 28 | 24 / 32 | 30 / 38 | 700 |
| title-md | `.text-title-md` | 18 / 26 | 22 / 30 | 26 / 34 | 700 |
| title-sm | `.text-title-sm` | 16 / 24 | 18 / 26 | 22 / 30 | 700 |
| title-xs | `.text-title-xs` | 15 / 22 | 16 / 24 | 20 / 28 | 700 |
| body-lg | `.text-body-lg` | 17 / 26 | 18 / 28 | 24 / 34 | 500 |
| body-md | `.text-body-md` | 15 / 24 | 16 / 26 | 22 / 32 | 500 |
| body-sm | `.text-body-sm` | 14 / 22 | 14 / 22 | 20 / 28 | 500 |
| body-xs | `.text-body-xs` | 12 / 18 | 13 / 20 | 18 / 26 | 500 |
| label-lg | `.text-label-lg` | 15 / 20 | 16 / 22 | 20 / 26 | 700 |
| label-md | `.text-label-md` | 14 / 18 | 14 / 20 | 18 / 24 | 700 |
| label-sm | `.text-label-sm` | 12 / 16 | 12 / 16 | 16 / 22 | 700 |
| label-xs | `.text-label-xs` | 11 / 14 | 11 / 14 | 14 / 20 | 700 |
| caption-md | `.text-caption-md` | 12 / 16 | 12 / 18 | 16 / 22 | 500 |
| caption-sm | `.text-caption-sm` | 11 / 14 | 11 / 16 | 14 / 20 | 500 |
| legal | `.text-legal` | 10 / 14 | 11 / 16 | 14 / 20 | 500 |

## Italic *accent*

Section and rail headings use a single italic `` on the last (or most evocative) word. A chevron-right follows the heading — tapping it navigates to the full section page.

## Jump back *in*

## Popular in *Mumbai*

## Free to *play*

## Hidden *gems*

## Naming crosswalk

Two parallel naming systems exist in the DLS. **Design roles** (what Figma and designers use) map to **CSS utility classes** (what engineers put in HTML). This table is the canonical mapping — never invent a new name in either system without adding it here.

| Design role | CSS utility class | Figma style name | Spec class (preview only) | Typical element |
|---|---|---|---|---|
| **Display / Hero** | `.text-hero` | `Type/Hero` | `.spec-display` | `` full-screen hero |
| **Screen Title** | `.text-screen-title` | `Type/Screen Title` | `.spec-h1` | `` inside AppBar or page |
| **Sheet Title** | `.text-sheet-title` | `Type/Sheet Title` | `.spec-h2` | `` bottom sheet, dialog |
| **Rail Title** | `.text-rail-title` | `Type/Rail Title` | `.spec-h3` | `` or `` content rail |
| **Card Title** | `.text-card-title` | `Type/Card Title` | `.spec-h4` | `` or `` inside card |
| **Body Large** | `.text-body-lg` | `Type/Body Large` | `.spec-body-lg` | `` hero description |
| **Body** | `.text-body` | `Type/Body` | `.spec-body` | `` default reading text |
| **Body Small** | `.text-body-sm` | `Type/Body Small` | `.spec-body-sm` | `` secondary / metadata |
| **Caption** | `.text-caption` | `Type/Caption` | `.spec-caption` | `` ratings, timestamps |
| **Badge / Label** | `.text-badge` | `Type/Badge` | `.spec-label` | `` chips, badges, tags |
| **Price** | `.text-price` | `Type/Price` | `.spec-price` | `` pass plan pricing |
| **CTA** | `.text-cta` | `Type/CTA` | `.spec-cta` | `` button label |
| **Overline / Micro** | `.text-overline` | `Type/Overline` | `.spec-micro` | `` section eyebrows, tags |

## Usage rules

These rules are enforced by `tokens/validate.sh`. ERRs block shipping.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--border-subtle`
- `--card-bg`
- `--code-green`
- `--divider`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--pill`
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

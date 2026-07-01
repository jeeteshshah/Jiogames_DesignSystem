# Token Reference — JioGames DLS spec

> Source: `token-reference/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Token Reference

---

All 444 design tokens, categorized and searchable. These are the single source of truth — generated from `tokens/tokens.json` via `tokens/build.py`. Never hard-code values — use the token.

## Brand colours

JioGames green family, glow, soft fills. Never use raw hex — always reference these.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Platform & semantic colours

Gold (web), amber (TV), red/pink/info. Used in platform labels and status indicators.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Surfaces & backgrounds

Background, card, sheet, glass surfaces. Dark palette only — no light surfaces.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Text & border

Text hierarchy (--text → --text4), borders, dividers, hairlines.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Semantic tokens

Purpose-named aliases over primitives. Components should reference semantic tokens, not primitives.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Spacing

8px base scale (--space-*), gutters, gaps, rail spacing.

| Token | Value | Usage |
|---|---|---|

## Radius

--r1 (8px) through --r9 (28px) + --pill. Map to component type via radius-governance.

| Token | Value | Usage |
|---|---|---|

## Sizing & control heights

Control heights (--ctrl-h, --ctrl-h-sm, --ctrl-h-ghost), touch targets, OTP boxes, card dimensions.

| Token | Value | Usage |
|---|---|---|

## Z-index scale

Layering system from --z-base to --z-tvFocus. Never use raw z-index integers.

| Token | Value | Usage |
|---|---|---|

## Motion

Easing curves (--spring, --ease-*) and duration tokens (--dur-*). Use in all transitions.

| Token | Value | Usage |
|---|---|---|

## Focus & TV

Focus ring tokens for web accessibility and TV D-pad navigation.

| Token | Value | Swatch | Usage |
|---|---|---|---|

## Component tokens

Component-scoped tokens (btn-*, card-*, input-*, surface-*). Use in component implementations only.

| Token | Value | Swatch | Usage |
|---|---|---|---|

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-strong`
- `--border-subtle`
- `--ctrl-h`
- `--ctrl-h-ghost`
- `--divider`
- `--info`
- `--input-bg`
- `--input-border`
- `--input-border-focus`
- `--jio`
- `--jio-2`
- `--jio-bright`
- `--jio-font`
- `--negative`
- `--positive`
- `--r3`
- `--r4`
- `--r9`
- `--section-gap`
- `--sheet-bg`
- `--surface-1`
- `--surface-2`
- `--text`
- `--text-inv`
- `--text-placeholder`
- `--text2`
- `--text3`
- `--ultimate`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# Elevation — JioGames DLS spec

> Source: `elevation/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Elevation

---

Surface ladder, shadow scale, and elevation pairing rules for JioGames dark UI.

SURFACE LADDER · bg → surface-4 → glass · TOKEN-BASED

## Shadow scale

Seven shadow levels cover every use case from flat page elements to top-of-stack TV cards. Use shadow tokens from tokens.css — not raw box-shadow values.

Shadow tokens `--shadow-1` through `--shadow-4` are defined in tokens.css. Use these tokens, not raw `box-shadow` values.

````css

.card           { box-shadow: var(--shadow-2); }
.card:hover     { box-shadow: var(--shadow-3); }
.card.active    { box-shadow: var(--jio-glow); }
````

## Surface ladder

Six opaque surface tokens create the depth ramp. Each step is slightly lighter than the one below it — communicating that it sits on top of it.

## Elevation + surface pairing

Shadow and surface are always used together. Each layer has a canonical surface token and shadow token pair. Do not mix levels.

| Layer | Surface token | Shadow token | Typical component |
|---|---|---|---|
| 0 — Page | --bg | none | Page background |
| 1 — Content | --card-bg | --shadow-2 | Game cards, list items |
| 2 — Float | --surface-2 | --shadow-3 | Dropdowns, popovers |
| 3 — Overlay | --surface-3 | --shadow-4 | Bottom sheets, dialogs |
| 4 — Top | --surface-4 | --shadow-4 | On-screen keyboard |

## Active / selected states

Active and selected states use `var(--jio-glow)` instead of grey shadows. A green border at reduced opacity accompanies the glow. Never use grey box-shadows on selected elements.

````

/* Standard card — grey shadow */
.card {
  background:  var(--card-bg);
  box-shadow:  var(--shadow-2);
  border:      1px solid var(--border);
}

/* Active / selected card — green glow, no grey shadow */
.card.selected {
  box-shadow:  var(--jio-glow);
  border-color: rgba(0,168,89,.4);
}
````

## Usage rules

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--card-bg`
- `--divider`
- `--glass-1`
- `--jio`
- `--jio-glow`
- `--r2`
- `--r5`
- `--shadow-2`
- `--shadow-3`
- `--space-1`
- `--space-2`
- `--space-3`
- `--space-4`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--surface-4`
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

# Separator — JioGames DLS spec

> Source: `separator/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Separator

---

Thin visual divider that organises content into sections. Horizontal or vertical, with optional label.

Separator variants · Horizontal, With label, Vertical

Separators create visual breathing room between unrelated content blocks. They are purely structural — they communicate "these sections are distinct" without adding meaning or hierarchy. Use them sparingly: white space alone often achieves the same separation without introducing a visible line. A separator is appropriate when two adjacent sections are semantically unrelated and the spatial gap alone is insufficient to signal the boundary.

- **Horizontal** — default usage between vertical content sections, list items, or form groups
- **With label** — adds a centred uppercase text (e.g. "OR") between the two rule lines for login alternatives
- **Vertical** — separates items in a horizontal row such as a toolbar, button pair, or nav strip
- **Strong** — slightly brighter border for more visible separation on dense surfaces

## When to use

Use when

- Dividing related sections within a page or card
- Separating action groups in menus and toolbars
- Visual breaks between list item groups

Don't use when

- Overusing — every section does not need a separator
- Between items where whitespace alone is sufficient
- As a structural layout tool — use Grid or Flex instead

## Best practices

- Use separators to divide semantically unrelated content — not just for decoration or rhythm
- Add `role="separator"` and `aria-orientation` when using a custom element; use `` when possible
- Use the labelled separator ("OR") sparingly — only when two genuinely alternative paths meet
- Use the strong variant when the surface is dense (e.g. a list of 10+ rows) and the subtle variant disappears
- On TV, increase separator opacity and thickness for 10-foot legibility

- Use separators between every item in a list — use `gap` or background alternation instead
- Use a separator to introduce hierarchy — that's the job of headings and typographic scale
- Add top and bottom margins to `` inside a layout that already uses `gap` — it doubles the spacing
- Use the labelled separator with text longer than 4 characters — it stretches the rule lines unevenly
- Use a vertical separator as the primary structural division of a layout — use columns or cards instead

## Anatomy

The horizontal separator is a single 1px rule. The labelled variant adds a centred text node flanked by two equal-width rule lines via flex + pseudo-elements.

1. 1 Rule line Required 1px solid line in var(--border-subtle). No height, no padding — spacing around the separator is set by the parent layout (gap or margin on siblings). Use --strong for var(--border). `border-top: 1px solid var(--border-subtle)`
2. 2 Flanking rule lines Conditional Two equal flex:1 pseudo-element lines that expand to fill available space on either side of the label. Created via ::before and ::after on .separator-label. `::before, ::after { flex:1; height:1px; background:var(--border-subtle) }`
3. 3 Label text Conditional 11px/700 uppercase, var(--text3), letter-spacing 0.4px. Typically "OR". Maximum 4 characters. Rendered as a text node inside .separator-label. `font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text3)`

## Variants

Four variants cover all separation contexts. Thickness is always 1px — use the strong variant for higher contrast, not a thicker line.

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Thin | 1px | Standard content divider | All |
| Thick | 4px | Major section break | Web |

## States

Separators are stateless. They have no hover, focus, pressed, or disabled states — they are purely visual dividers and carry no interactivity. If you need a collapsible section divider with toggle behaviour, use an Accordion component instead.

No interactive states — separators do not respond to pointer or keyboard events.

## Content guidance

- Use all-caps, max 4 characters: "OR", "AND", "VS", "NEW"
- "OR" is the standard for login alternative paths (OTP vs password, JioID vs guest)
- Do not use sentence-case or lowercase — the uppercase tracks the visual weight of the rule lines
- Never use descriptive phrases like "Continue with" — that belongs in the button label, not the separator

- Use to divide a settings sheet into "Account" and "Preferences" groups
- Use between the main game rail and the "Because you played" rail on the home screen
- Avoid between every card in a vertical list — rely on card borders or gap spacing instead
- Avoid on surfaces that already use strong card backgrounds — the line becomes redundant noise

## Platform considerations

- Use 1px default — thicker lines feel heavy on high-DPI mobile screens
- Let the parent layout (gap or padding) control the space around the separator — don't add margin directly to ``
- Full-bleed separators (extending to screen edges) are appropriate in sheet overlays and settings lists

- Use `` for horizontal separators — it carries the correct semantic role automatically
- For the labelled variant, use a `` with `role="separator"`
- Vertical separators: set `aria-orientation="vertical"` and `role="separator"`

- Use 2px thickness and increase opacity to at least 30% — 1px at var(--border-subtle) is invisible at 3m
- Use the strong variant as the baseline on TV; default subtle is insufficient
- Avoid labelled separators on TV — the 11px uppercase label is unreadable at 10-foot distance

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Appear | `--ease-out` | `--dur-fast` | opacity |

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Semantic element | `` | Use a native `` for horizontal separators. It carries `role="separator"` and `aria-orientation="horizontal"` automatically. |
| Custom separator | `role="separator"` | When using a `` or ``, always add `role="separator"` explicitly. |
| Orientation | `aria-orientation="horizontal|vertical"` | Default is horizontal for ``. Always declare `aria-orientation="vertical"` on vertical separators. |
| Decorative separators | `aria-hidden="true"` | If the separator is purely decorative and adds no structural meaning, add `aria-hidden="true"` to hide it from the accessibility tree. |
| Color contrast | Not applicable | Separators are non-text elements; WCAG 1.4.11 Non-text Contrast requires 3:1 against adjacent surfaces. var(--border-subtle) passes on var(--bg) and var(--surface-1). |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--border-subtle` | `rgba(255,255,255,.08)` | Default separator rule line color |
| `--border` | `rgba(255,255,255,.16)` | Strong separator rule line color |
| `--text3` | `rgba(244,242,238,.32)` | Labelled separator text color |
| `--jio-font` | `'Outfit', sans-serif` | Labelled separator font family |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-separator` | Root — 1px border-subtle, no border/bg on other sides |
| `.ds-separator--horizontal` | Full width, height 1px (default) |
| `.ds-separator--vertical` | Full height, width 1px |
| `.ds-separator--dashed` | Dashed border style |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `orientation` | "horizontal" | "vertical" | "horizontal" | Line direction |
| `decorative` | boolean | true | If true, hidden from screen readers (aria-hidden) |
| `className` | string | undefined | Additional classes |

## Code examples

````
<!-- Preferred: use the native hr element -->
<hr class="separator">

<!-- Strong variant -->
<hr class="separator separator--strong">
````

````html
<div class="separator-label" role="separator" aria-label="or">OR</div>

<!-- Usage in login flow -->
<button class="btn btn--primary btn--m">Continue with OTP</button>
<div class="separator-label" role="separator" aria-label="or">OR</div>
<button class="btn btn--ghost btn--m">Sign in with JioID</button>
````

````html
<div style="display:flex; align-items:center; gap:16px; height:36px;">
  <button class="btn btn--ghost btn--s">Sign in</button>
  <div
    class="separator--vertical"
    role="separator"
    aria-orientation="vertical"
    aria-hidden="true"
  ></div>
  <button class="btn btn--primary btn--s">Get Pass</button>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--surface-1`
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

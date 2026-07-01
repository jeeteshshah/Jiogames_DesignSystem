# Toggle Group — JioGames DLS spec

> Source: `toggle-group/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Toggle Group

---

A set of toggle buttons where one (or multiple) can be active. Used for view mode switchers, filter chips, and platform selectors.

Toggle Group · view switcher and platform filter, active state green

Toggle Group presents a set of mutually exclusive or independently selectable options as a connected button bar. It is the correct component when a user needs to switch between modes (Grid / List), select a filter category (All / Mobile / Web / TV), or mark platform availability. It differs from Tabs in that it does not control a content panel below it — it communicates a selection value, not navigation.

- **Single-select (radio)** — one item active at a time. Use for view modes, sort orders, time ranges.
- **Multi-select (checkbox)** — any combination active. Use for tag or genre filters.
- **Pill shape** — fully rounded ends; softer appearance for filter chips and tags.
- **Square shape** — default rounded corners; use in toolbars and density-sensitive layouts.

- Use 2–6 items. Below 2, use a checkbox or switch. Above 6, use a dropdown or chip scroll.
- Keep labels to 1–2 words or a single icon. "Mobile" not "Mobile Devices".
- Always have a default selection in single-select mode — never leave all items inactive.
- Use `role="radiogroup"` for single-select, `role="group"` for multi-select.
- Ensure minimum 44px touch height on mobile by adding vertical padding.

- Use Toggle Group as tab navigation — it does not control a content panel.
- Mix icon-only and text items in the same group — keep them consistent.
- Use more than 6 items — overflow is not handled gracefully in the base component.
- Use Toggle Group for yes/no binary choices — use a Switch or Checkbox instead.
- Wrap to multiple lines — if items overflow, switch to a horizontal scroll or chip list.

1. 1 Inactive item Required 13px / weight 600 / `var(--text3)`. Transparent background. Border-right separates from adjacent item. `color: var(--text3); background: transparent`
2. 2 Active item Required Same size, weight 700, text black on green fill. `background: var(--jio)`. Only one active in single-select; any in multi-select. `background: var(--jio); color: #000; font-weight: 700`
3. 3 Item divider Required 1px `var(--border-subtle)` right border on all items except last. Provides visual separation within the group. `border-right: 1px solid var(--border-subtle)`
4. 4 Group container Required 1px outer border + `var(--r4)` radius. `overflow: hidden` clips item corners. No gap between items. `border: 1px solid var(--border-subtle); border-radius: var(--r4)`

## Variants

Four variants covering the main use cases. Shape and selection mode are independent — combine as needed.

## Sizes

Three sizes. M is the default for all surfaces. S for compact toolbars. L for prominent filter bars or TV contexts.

## States

Individual items have 5 states. The entire group can also be set to all-disabled.

## Content guidance

Labels should be 1–2 words. Icons are allowed with text or alone. Minimum 2 items, maximum 6.

- 1–2 words. Nouns or adjectives. "Grid" not "Grid View".
- Keep all labels in a group roughly equal length — avoid one long label skewing the layout.
- Icons-only: always add `aria-label` to each button.
- Icon + text: icon is `aria-hidden` — label carries the accessible name.

- Minimum 2 items. Maximum 6 — above 6, use a dropdown or scrollable chip list.
- For single-select: always have one item active on mount. No empty selection.
- For multi-select: zero active items is a valid state (means "no filter applied").
- Don't mix icon-only and text items — keep items consistent within a group.

## Platform considerations

- Minimum 44px touch height — use M or L size, or add `min-height: 44px`.
- If items overflow the screen width, add `overflow-x: auto` with hidden scrollbar on a wrapper — don't wrap to a second line.
- Use pill variant for filter chips to align with mobile UI conventions.

- Group stays contained — no overflow scroll needed on wider viewports.
- Keyboard: Tab to enter group, Arrow Left / Right to move between items, Space / Enter selects.
- Focus ring inset (`outline-offset: -2px`) keeps ring inside the group border.

- D-pad Left / Right navigates between items. OK selects.
- Active item gets the standard TV focus ring: 3px `var(--jio)` glow.
- Use L size minimum for legibility at 3m. Add `min-height: 56px`.
- Avoid more than 4 items on TV — they crowd the remote's D-pad navigation.

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Group container | `role="radiogroup"` or `role="group"` | Use `radiogroup` for single-select, `group` for multi-select. Always add `aria-label` describing the group's purpose. |
| Single-select item | `role="radio"` + `aria-checked` | `aria-checked="true"` on active, `"false"` on others. Arrow keys move focus; Space activates. |
| Multi-select item | `` + `aria-pressed` | `aria-pressed="true"` when active. Each button independently toggleable. Tab moves between items. |
| Icon-only item | `aria-label` | Each icon-only button must have a descriptive `aria-label`. The SVG is `aria-hidden="true"`. |
| Disabled item | `disabled` | Disabled items are removed from tab order. If they need to stay focusable, use `aria-disabled="true"` instead and handle pointer-events in CSS. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Active item background fill |
| `--border-subtle` | `rgba(255,255,255,.08)` | Group outer border and item dividers |
| `--glass-1` | `rgba(255,255,255,.04)` | Item hover background |
| `--text3` | `rgba(244,242,238,.32)` | Inactive item label color |
| `--text2` | `rgba(244,242,238,.55)` | Item hover label color |
| `--r4` | `12px` | Group container border-radius (square variant) |
| `--pill` | `100px` | Group container border-radius (pill variant) |
| `--dur-fast` | `120ms` | All item transitions |
| `--state-disabled-opacity` | `0.38` | Disabled item / group opacity |

## When to use

Use when

- Segmented controls: view mode (grid/list), sort direction (asc/desc)
- Platform filter selector (Mobile / Web / TV)
- Mutually exclusive visual style controls in a toolbar
- Rating or difficulty selectors with 3-5 options

Don't use when

- More than 5 items — wrapping breaks the segmented control pattern
- Options needing explanation longer than ~15 chars each
- Multi-select where any combination is valid — use Checkboxes instead
- Primary form fields — use Radio for form data

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Active indicator slide | `--ease-out` | `--dur-fast` | transform translateX, width |
| Item press | `--ease-out` | `80ms` | transform scale(0.95) |
| Selection highlight | `--ease-out` | `--dur-fast` | background, color |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-toggle-group` | Root — flex row, surface-1, border-subtle, r3, gap 0 |
| `.ds-toggle-group__item` | Single option — px 12, 36px height, 13px 600 |
| `.ds-toggle-group__item--active` | Active item — jio-soft bg, jio text, jio border |
| `.ds-toggle-group__item:not(:last-child)` | Right border-subtle divider |
| `.ds-toggle-group--sm` | Small variant — 28px height |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `type` | "single" | "multiple" | "single" | Selection mode |
| `value` | string | string[] | required | Controlled selected value(s) |
| `onValueChange` | (v: string | string[]) => void | required | Change handler |
| `disabled` | boolean | false | Disable all items |
| `size` | "sm" | "md" | "md" | Height preset |
| `children` | ReactNode | required | ToggleGroupItem components |

## Code examples

````html
<div class="toggle-group" role="radiogroup" aria-label="View mode">
  <button class="toggle-group-item is-active"
          role="radio" aria-checked="true">Grid</button>
  <button class="toggle-group-item"
          role="radio" aria-checked="false">List</button>
  <button class="toggle-group-item"
          role="radio" aria-checked="false">Map</button>
</div>
````

````html
<div class="toggle-group toggle-group--pill"
     role="group" aria-label="Genre filter">
  <button class="toggle-group-item is-active" aria-pressed="true">Action</button>
  <button class="toggle-group-item" aria-pressed="false">RPG</button>
  <button class="toggle-group-item is-active" aria-pressed="true">Racing</button>
  <button class="toggle-group-item" aria-pressed="false">Sports</button>
</div>
````

````html
<div class="toggle-group" role="group" aria-label="View layout">
  <button class="toggle-group-item is-active"
          aria-pressed="true" aria-label="Grid view">
    <svg width="14" height="14" aria-hidden="true">
      <!-- grid icon -->
    </svg>
  </button>
  <button class="toggle-group-item"
          aria-pressed="false" aria-label="List view">
    <svg width="14" height="14" aria-hidden="true">
      <!-- list icon -->
    </svg>
  </button>
</div>
````

## Changelog

Initial draft. Single-select and multi-select modes. Square and pill shapes. S / M / L sizes. Icon-only variant. Full ARIA radiogroup and group pattern documentation.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--pill`
- `--r3`
- `--r4`
- `--state-disabled-opacity`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

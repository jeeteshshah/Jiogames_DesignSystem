# Select — JioGames DLS spec

> Source: `select/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Select

---

Dropdown for choosing one option from a list. Used for sort order, platform filter, language, and settings with 5+ options.

Select in filter context · Sort by (default) · Genre (focused)

The Select is a native `` element with a custom visual shell — arrow icon, border, and typography are overridden; the dropdown list is rendered by the OS. Use Select when users must choose exactly one option from a closed list of 5–15 items. For fewer than 5 items, use Radio buttons or Chips. For more than 15 items or when search is needed, use Combobox.

- **Sort controls** — Most Popular, Newest, Top Rated, A–Z in a browse header
- **Filter selectors** — Platform, Genre, Language dropdowns in search/filter panels
- **Settings** — Display language, region, audio output device
- **Forms** — Country, state, payment method in checkout or profile flows

- Always use a neutral first option: "Select a genre" — never a blank ``
- Pair with a visible `` — `aria-label` only when the visual context makes it obvious
- Use for lists of 5–15 options — below 5, use Radio; above 15, use Combobox with search
- Apply `is-invalid` class and error hint text on validation failure
- Pre-select the most common or recommended option as the default

- Use a blank first `` — always label the placeholder state
- Use Select for lists longer than 15 items — scanning an OS dropdown past 15 options is slow
- Use Select for binary choices — use a Toggle or two Radio buttons instead
- Style the OS dropdown list panel — it renders in the OS context; only the trigger element is styleable
- Use Select for navigation actions — it is a form control, not a nav element

1. 1 Label Required Visible `` linked via `for`/`id`. 12px/500, above the trigger. Never inside the trigger as placeholder-only. `font-size: 12px; color: var(--text2)`
2. 2 Trigger container Required The styled `` element. 48px height (M), glass background, 1.5px border. Opens OS native dropdown on interaction. `height: 48px; border-radius: var(--r5)`
3. 3 Chevron icon Required 16px SVG chevron, absolutely positioned right 14px, vertically centered. `pointer-events: none` so clicks pass through to the ``. `color: var(--text3); pointer-events: none`
4. 4 OS dropdown list Optional Rendered entirely by the OS — cannot be styled with CSS. On mobile this is a bottom sheet picker; on web a floating list panel. `/* not styleable — OS rendered */`

## Variants

Five variants cover all standard select use cases. Icon prefix requires the select to be wrapped in a custom shell (see code examples).

## Sizes

Three height tiers. M is the default for all contexts. S fits dense filter bars. L is for prominent standalone filter controls.

## States

Five states. Hover and focus only apply to the trigger element — the dropdown list is OS-rendered and carries its own system focus styles.

| State | Visual change | When |
|---|---|---|
| Default | Border `var(--border-subtle)`, muted chevron | Unfocused, value selected |
| Hover | Border brightens to `var(--border)` | Pointer over trigger |
| Focus | Border `var(--jio)`, green glow ring, chevron turns green | Keyboard focus or after OS dropdown closes |
| Disabled | Opacity `var(--state-disabled-opacity)`, no pointer events | Option locked by permission or state |
| Invalid | Border `var(--negative)`, chevron turns red, error hint below | Required field not selected on form submit |

## Content guidance

Option copy and placeholder text are the primary editorial surfaces in a Select.

- Always provide a labeled placeholder: "Select a genre", "Sort by"
- Never use an empty first option — screen readers will announce a blank
- Mark the placeholder `disabled` so it can't be re-selected after a value is chosen
- Placeholder copy: "Select a [noun]" — short, no punctuation

- Write options in sentence case, not title case: "Most popular", not "Most Popular"
- Keep options under 32 characters — long text truncates in native OS list on some platforms
- Avoid lists longer than 15 items — switch to Combobox with search above that threshold
- Sort options logically: most used first, or alphabetical for reference lists (languages, countries)

## Platform considerations

The dropdown list rendering is entirely platform-controlled. Only the trigger element is styled by the design system.

- iOS renders a bottom sheet wheel picker; Android shows a dialog list — both are OS-native and cannot be styled
- For a fully custom appearance on mobile, replace with a bottom sheet using Radio buttons or Chips inside it
- Minimum touch target on the trigger: full width, 48px height — ensure the `` itself fills the wrapper
- Never show a custom dropdown panel on mobile — it conflicts with the OS picker

- OS dropdown renders a floating list below the trigger — position, colors, and font are all OS-controlled
- For a fully custom dropdown with styled options, use the custom select pattern (see code examples) with `role="combobox"`
- Max-width in browse filters: 200px; in forms: full column width
- Keyboard: Space/Enter opens, arrow keys navigate, Enter selects, Escape closes

- Do not use native `` on TV — OS dropdown is not navigable with d-pad in all webviews
- Replace with a full-screen selection overlay: list of options with d-pad navigation and green focus ring
- Selected value displayed inline in the settings row; overlay opens on d-pad confirm (OK/Enter)
- TV selection overlay is always full-screen — never an inline dropdown panel

## Accessibility

Native `` is fully accessible by default. Custom select patterns require explicit ARIA.

| Requirement | Implementation | Notes |
|---|---|---|
| Label association | `` | Native `` inherits the label automatically. For icon-only trigger, add `aria-label`. |
| Error state | `aria-invalid="true"` + `aria-describedby` | Point to the error hint element. Screen readers announce label → value → error message on focus. |
| Disabled | `disabled` attribute on `` | Disabled selects are skipped by keyboard navigation. If visibility is needed, use `aria-disabled="true"` instead and handle pointer events manually. |
| Custom select | `role="combobox"`, `aria-expanded`, `aria-haspopup="listbox"` | Each option needs `role="option"`. The listbox container needs `role="listbox"` and `aria-labelledby`. |
| Keyboard | Native on `` | Space/Enter opens, arrows navigate options, Enter confirms, Escape cancels. Never suppress default key events on native select. |

## Related tokens

Tokens used to implement the select trigger element.

| Token | Value | Usage |
|---|---|---|
| `--input-bg` | `var(--glass-1)` | Trigger background fill |
| `--input-border` | `var(--border-subtle)` | Default trigger border |
| `--input-text` | `var(--text)` | Selected value text color |
| `--jio` | `#00A859` | Focus border and glow ring |
| `--negative` | `#FF4757` | Invalid state border and chevron |
| `--r5` | Border radius tier 5 | Trigger container border-radius |
| `--text3` | `rgba(244,242,238,.32)` | Chevron icon default color |
| `--state-disabled-opacity` | `.38` | Disabled opacity on trigger |

## When to use

Use when

- Controlled single option selection from a small set (sort by, language, country)
- Form fields where the option set is ≤15 items and searchability isn't needed
- Settings dropdowns: quality, region, notification frequency

Don't use when

- Large option sets (>15) — use Combobox with search
- Multi-select — use Combobox with multiple prop
- Binary choices — use Toggle or Radio
- Options that need description/preview — use a custom dropdown

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Dropdown open | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Dropdown close | `--ease-in` | `--dur-fast` | opacity |
| Option highlight | `--ease-out` | `60ms` | background |
| Chevron rotate | `--ease-out` | `--dur-fast` | transform rotate(0 → 180deg) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-select` | Root trigger — 48px height, surface-1, border-subtle, r3 |
| `.ds-select--open` | Active/open state — jio border |
| `.ds-select--error` | Error state — red border |
| `.ds-select--disabled` | 38% opacity |
| `.ds-select__content` | Dropdown panel — surface-2, r4 |
| `.ds-select__item` | Option row — 40px, padding 0 12px |
| `.ds-select__item--selected` | Green checkmark + jio text |
| `.ds-select__item--focused` | Keyboard-highlighted — glass-1 bg |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | undefined | Controlled selected value |
| `onValueChange` | (v: string) => void | undefined | Change handler |
| `defaultValue` | string | undefined | Uncontrolled initial value |
| `placeholder` | string | "Select…" | Shown when no value selected |
| `disabled` | boolean | false | Disable the control |
| `children` | ReactNode | required | SelectItem components |

## Code examples

Link `tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="select-wrap">
  <select id="sort" class="select" aria-label="Sort by">
    <option value="popular" selected>Most popular</option>
    <option value="new">Newest first</option>
    <option value="rating">Top rated</option>
    <option value="az">A – Z</option>
  </select>
  <span class="select-icon" aria-hidden="true">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M4 6l4 4 4-4" stroke="currentColor"
        stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
</div>
````

````html
<div class="field-group">
  <label class="field-label" for="genre">Genre</label>
  <div class="select-wrap">
    <select
      id="genre"
      class="select is-invalid"
      aria-invalid="true"
      aria-describedby="genre-err"
    >
      <option value="" disabled selected>Select a genre</option>
      <option value="action">Action</option>
      <option value="rpg">RPG</option>
      <option value="sports">Sports</option>
    </select>
    <span class="select-icon" aria-hidden="true">…chevron svg…</span>
  </div>
  <div id="genre-err" class="field-hint">
    Genre is required before you can save your profile.
  </div>
</div>
````

````
<!-- Use when OS dropdown styling is required (web only) -->
<div
  class="select-wrap"
  role="combobox"
  aria-expanded="false"
  aria-haspopup="listbox"
  aria-labelledby="platform-label"
  tabindex="0"
>
  <span id="platform-label" class="field-label">Platform</span>
  <div class="select select--m" style="display:flex; align-items:center;">
    <span style="flex:1;">All platforms</span>
    <svg class="select-icon" …>…</svg>
  </div>
  <!-- Hidden when aria-expanded="false" -->
  <ul
    role="listbox"
    aria-labelledby="platform-label"
    style="display:none; position:absolute; top:calc(100% + 4px); left:0; right:0;
           background:var(--surface-2); border:1px solid var(--border-subtle);
           border-radius:var(--r5); z-index:100; list-style:none; padding:4px 0; margin:0;"
  >
    <li role="option" aria-selected="true"  style="padding:10px 14px;">All platforms</li>
    <li role="option" aria-selected="false" style="padding:10px 14px;">Mobile</li>
    <li role="option" aria-selected="false" style="padding:10px 14px;">PC</li>
    <li role="option" aria-selected="false" style="padding:10px 14px;">Console</li>
  </ul>
</div>
<!-- Add JS: toggle aria-expanded, handle arrow keys, Enter selects, Escape closes -->
````

## Changelog

Initial draft. Includes Default, Focused, Disabled, Placeholder, and Invalid variants. S / M / L size tiers. Five states. Platform guidance covering OS-native picker behavior on mobile and TV overlay pattern. Three code examples including custom select ARIA pattern.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--input-bg`
- `--input-border`
- `--input-h`
- `--input-radius`
- `--input-text`
- `--jio`
- `--jio-font`
- `--negative`
- `--r5`
- `--space-2`
- `--space-5`
- `--state-disabled-opacity`
- `--surface-2`
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

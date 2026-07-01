# Checkbox — JioGames DLS spec

> Source: `checkbox/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Checkbox

---

Binary selection for settings, filters, and multi-select lists. Used independently or in groups.

Checkbox states · Checked, Unchecked, Indeterminate

Checkboxes let users select one or more options from a set. Each checkbox operates independently — selecting one does not affect others. Use them for multi-select filters, settings toggles, and permission acceptance flows. For a single binary toggle that controls a live setting instantly, prefer the Toggle component instead.

- **Binary selection** — checked or unchecked, with an optional indeterminate third state for parent nodes
- **Multi-select groups** — genre filters, notification preferences, content settings
- **Indeterminate parent** — shows a dash when some but not all children in a nested list are checked
- **With hint text** — additional context below the label for complex options

## When to use

Use when

- Selecting multiple items from a list (genres, platforms, filters)
- Terms and conditions acceptance in forms
- Preference settings where options are independent of each other
- Bulk-select actions in data tables

Don't use when

- Mutually exclusive choices — use Radio instead
- Binary on/off settings — use Toggle/Switch instead
- More than ~12 options without grouping or search

## Best practices

- Use checkboxes when users can select multiple items from a list simultaneously
- Always provide a visible text label alongside every checkbox
- Use the indeterminate state when a parent checkbox has a mix of checked and unchecked children
- Maintain a minimum touch target of 44×44px on mobile even if the visual control is smaller
- Group related checkboxes under a shared heading or fieldset legend

- Use a checkbox for mutually exclusive options — use Radio buttons instead
- Use a standalone checkbox as a primary action trigger — it's a state indicator, not a button
- Change the label text based on checked state — the label always describes the option
- Nest more than 2 levels of checkbox hierarchies — it creates confusing tree selection semantics
- Disable a checkbox without explaining why the option is unavailable

## Anatomy

A checkbox consists of the control box, optional check icon, and a text label. Hint text is an optional fourth element below the label.

1. 1 Control box Required 20×20px square with rounded corners (r2). Stroke border when unchecked; solid green fill when checked. Inherits border-radius: var(--r2). `width:20px; height:20px; border-radius:var(--r2)`
2. 2 Check icon Conditional SVG tick in black (#000) on green fill. Hidden when unchecked; block when checked. Replaced by a dash (—) in indeterminate state. `color: #000; display: none → block`
3. 3 Label Required 15px/500 weight text in var(--text). Clicking the label must toggle the checkbox — always associate via a wrapping label element or for/id pair. `font-size:15px; font-weight:500; color:var(--text)`
4. 4 Hint text Optional 12px muted text below the label. Provides additional context for complex options. Use sparingly — if every option needs a hint, reconsider the information architecture. `font-size:12px; color:var(--text3); margin-top:2px`

## Variants

All checkbox variants share the same 20px control box. Visual treatment changes only the fill, border, and icon visibility.

## Sizes

Three sizes are available. M (20px) is the default for all surfaces. S (16px) is for dense compact lists. L (24px) is for settings pages where the control needs to be more prominent.

## States

Checkboxes have six distinct visual states. Focus ring uses the system's 2px green outline offset by 2px. Hover slightly brightens the border. Disabled reduces opacity to 0.35 and blocks interaction.

## Content guidance

Checkbox labels should be concise and describe the option clearly. The label always describes what happens when the box is checked.

- Use sentence case — "Save login" not "save login" or "SAVE LOGIN"
- Start with a noun or verb — "Receive tournament alerts", "Auto-save replays"
- Keep labels under 5 words where possible; use hint text for detail
- Never use negative framing — "Do not notify me" causes double-negative confusion when checked

- Use hint text to explain consequences or constraints, not to repeat the label
- Good: "Uses mobile data when Wi-Fi is unavailable"
- Bad: "Check this box to receive alerts" — redundant restatement of the label
- Keep hint text to one line where possible; two lines maximum

## Platform considerations

Checkbox behaviour and scale vary across platforms. Core semantics stay fixed — only touch target size and TV replacement guidance differ.

- Wrap in a `` that covers at least 44×44px tap area
- Extend the touch zone by expanding the wrapping label, not the visual control
- Stack checkboxes vertically in a group — never side by side on mobile
- Use M (20px) size — S is too small for confident tapping on glass

- Keyboard Space toggles the focused checkbox
- Tab moves focus between checkboxes; Shift+Tab reverses
- Show a 2px green focus ring offset 2px from the control box edge
- Use M or L sizes; cursor changes to `pointer` on the label area

- Do not use Checkbox on TV — use a Toggle or a highlighted row selector instead
- Checkboxes are not legible at 3-metre viewing distance even at L size
- For multi-select on TV, use a card grid where selected cards show a green border and tick overlay

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Check mark draw | `--ease-out` | `--dur-fast` | stroke-dashoffset |
| Box fill | `--ease-out` | `--dur-fast` | background, border-color |
| Indeterminate line | `--ease-out` | `--dur-fast` | transform scaleX |
| Focus ring | `instant` | `0ms` | outline |
| Hover | `--ease-out` | `100ms` | background |

## Accessibility

Every checkbox must be operable by keyboard and screen reader. The native HTML checkbox element handles most requirements automatically — use it in preference to ARIA roles where possible.

| Requirement | Implementation | Notes |
|---|---|---|
| Role | `role="checkbox"` | Provided automatically by ``. Required on custom elements. |
| Checked state | `aria-checked="true|false|mixed"` | Use `mixed` for indeterminate. Native `indeterminate` property must also be set in JS. |
| Disabled state | `aria-disabled="true"` + `disabled` | Both attributes needed — `disabled` removes from tab order; `aria-disabled` preserves focus if needed. |
| Label association | `` or wrapping `` | Never use placeholder or sibling text as the sole label without an explicit association. |
| Keyboard toggle | Space key | Native checkbox handles this. Custom elements must intercept `keydown` Space and call `click()`. |
| Group labelling | `` + `` | Wrap checkbox groups in a fieldset. Screen readers announce the legend before each checkbox in the group. |

## Related tokens

Always use tokens — never hard-code hex values. These are the tokens that drive checkbox visual styles.

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Checked fill and border color |
| `--border` | `rgba(255,255,255,.16)` | Unchecked control box border |
| `--surface-3` | `—` | Indeterminate fill background |
| `--text` | `#f4f2ee` | Label text color |
| `--text3` | `rgba(244,242,238,.32)` | Hint text color |
| `--r2` | `4px` | Control box border-radius |
| `--state-disabled-opacity` | `0.35` | Disabled control and label opacity |
| `--dur-fast` | `120ms` | Check/uncheck transition duration |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-checkbox` | Root — flex row, label + control |
| `.ds-checkbox__control` | 20×20px box — border-subtle, r2 |
| `.ds-checkbox__control--checked` | Green fill, white checkmark |
| `.ds-checkbox__control--indeterminate` | Green fill, white dash |
| `.ds-checkbox__control--disabled` | 38% opacity, pointer-events none |
| `.ds-checkbox__label` | Text label — 14px text2 |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `checked` | boolean | "indeterminate" | undefined | Controlled checked state |
| `defaultChecked` | boolean | false | Uncontrolled initial state |
| `onCheckedChange` | (v: boolean | "indeterminate") => void | undefined | Change handler |
| `disabled` | boolean | false | Disable interaction |
| `id` | string | undefined | Links to a element |

## Code examples

Copy these snippets as starting points. Always include `tokens.css`, `components.css`, and `states.css`.

````
<label class="checkbox-wrap">
  <input type="checkbox" id="autoSave" class="sr-only">
  <span class="checkbox" aria-hidden="true">
    <svg class="checkbox__icon" width="12" height="10" viewBox="0 0 12 10" fill="none">
      <path d="M1 5l3.5 3.5L11 1" stroke="#000" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </span>
  <span class="checkbox-label">Auto-save replays</span>
</label>
````

````
<fieldset style="border:none; padding:0;">
  <legend style="font-size:13px; font-weight:700; color:var(--text2); margin-bottom:12px;">
    Preferred genres
  </legend>
  <div class="checkbox-group">
    <label class="checkbox-wrap">
      <input type="checkbox" checked>
      <span class="checkbox is-checked"><!-- svg icon --></span>
      <span class="checkbox-label">Action</span>
    </label>
    <label class="checkbox-wrap">
      <input type="checkbox">
      <span class="checkbox"></span>
      <span class="checkbox-label">Strategy</span>
    </label>
    <label class="checkbox-wrap">
      <input type="checkbox">
      <span class="checkbox"></span>
      <span class="checkbox-label">Sports</span>
    </label>
  </div>
</fieldset>
````

````
<label class="checkbox-wrap">
  <input type="checkbox" id="selectAll">
  <span class="checkbox" id="selectAllBox">
    <span class="checkbox-dash"></span>
  </span>
  <span class="checkbox-label">All genres</span>
</label>

<script>
  const input = document.getElementById('selectAll');
  const box   = document.getElementById('selectAllBox');

  function syncParent(checkedCount, total) {
    if (checkedCount === 0) {
      input.indeterminate = false;
      input.checked = false;
      box.className = 'checkbox';
    } else if (checkedCount === total) {
      input.indeterminate = false;
      input.checked = true;
      box.className = 'checkbox is-checked';
    } else {
      input.indeterminate = true;
      box.className = 'checkbox is-indeterminate';
    }
  }
</script>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--dur-fast`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--r2`
- `--state-disabled-opacity`
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

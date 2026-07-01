# Radio — JioGames DLS spec

> Source: `radio/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Radio

---

Single selection from a mutually exclusive set. Used in plan selection, quality settings, and filter groups.

Radio group · Video quality selection with description

Radio buttons enforce single selection within a group — choosing one option automatically deselects any previously selected item. Use them for mutually exclusive settings such as video quality, pass plan type, or language preference. Unlike checkboxes, radio buttons should never appear alone; a group of at least two is required for the mutual-exclusion semantics to make sense.

- **Plan selection** — JioGames Mobile, Ultimate, or Family plan chooser
- **Quality settings** — 480p, 720p, 1080p, 4K video stream quality
- **Language & region** — preferred audio language, subtitle language
- **Filter mode** — sort order, content rating, release year range

## When to use

Use when

- Mutually exclusive option selection: pass tier, sort order, gender
- Settings screens where only one value is valid at a time
- Survey or quiz single-answer questions

Don't use when

- Independent toggleable options — use Checkbox instead
- Binary on/off — use Toggle/Switch instead
- More than ~8 options — use Select or Combobox instead

## Best practices

- Always pre-select a default option — never leave a radio group with nothing selected
- Group all radios under a single `name` attribute so the browser enforces mutual exclusion natively
- Use a fieldset + legend to label the group for screen readers
- Order options logically — most popular first, or ascending size/quality
- Use hint text to explain constraints like pass tier requirements

- Use radio buttons for settings that can have multiple active values — use Checkboxes
- Use a single standalone radio button — it implies a group that doesn't exist
- Show more than 6 options as radios — use a Select/Dropdown instead
- Change page content immediately on radio selection without user confirmation — prefer an explicit submit action
- Use radio buttons on TV — use a card-style selector with D-pad focus instead

## Anatomy

A radio button consists of a circular control with an inner dot when selected, plus a required text label. Hint text is optional below the label.

1. 1 Circle track Required 20×20px fully circular ring. Muted border when unchecked; green border when checked. Always border-radius: var(--pill). `width:20px; height:20px; border-radius:var(--pill)`
2. 2 Inner dot Conditional 10×10px filled green circle centred in the track. Appears only when selected. Created with a CSS ::after pseudo-element. `width:10px; height:10px; background:var(--jio)`
3. 3 Label Required 15px/500 text in var(--text). Tapping the label must select the radio. Always associate via a wrapping label or for/id pair. `font-size:15px; font-weight:500; color:var(--text)`
4. 4 Hint text Optional 12px muted text below the label for eligibility or usage notes. Example: "Requires JioGames Ultimate". `font-size:12px; color:var(--text3); margin-top:2px`

## Variants

Radio buttons have four variants. All share the same circular control shape — only the selection state and optional description differ.

## Sizes

Two sizes are available. M (20px) is the default for all surfaces. L (24px) is used on plan selection cards and settings pages where the control needs higher visual weight.

## States

Radio buttons have five states. Arrow keys navigate within a group — pressing an arrow key both moves focus and selects the item. Tab moves between groups.

## Content guidance

Radio labels identify the option clearly and concisely. Descriptions should add meaningful context, not restate the label.

- Be specific — "720p HD" not just "Medium quality"
- Use noun phrases — "JioGames Mobile", "English (India)", "Last 30 days"
- Keep labels parallel in structure across all options in a group
- For plan names, use the official product name — never invent shorthand

- Use for eligibility notes: "Requires JioGames Ultimate"
- Use for impact: "Saves up to 2GB per hour of data"
- Do not describe what the option is — the label already does that
- Keep descriptions to one line; two lines maximum on mobile

## Platform considerations

- Minimum 44×44px touch target via a wrapping ``
- Stack options vertically — horizontal radio groups are illegible on small screens
- Default to the most commonly chosen option pre-selected
- Use M (20px) size — L is for settings pages only

- Arrow keys move selection within a radio group (Up/Left = previous, Down/Right = next)
- Tab moves focus to the next focusable element outside the group
- Show a 2px green focus ring on the currently focused radio
- Wrap in `` + `` for screen reader group context

- Do not use Radio on TV — use a highlighted card-style selector instead
- Cards show a green border and a tick badge in the corner when selected
- D-pad left/right navigates between options; OK/Select confirms
- Selected card scales to 1.05 with a green glow to signal active state at 3m

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Select | `--ease-out` | `--dur-fast` | transform scale(0 → 1) inner dot, border-color |
| Deselect | `--ease-out` | `--dur-fast` | transform scale(1 → 0) inner dot |
| Focus ring | `instant` | `0ms` | outline |
| Hover | `--ease-out` | `100ms` | background of outer ring |

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Role | `role="radio"` | Automatic with ``. Required on custom elements. |
| Group role | `role="radiogroup"` | Wrap the group in an element with `role="radiogroup"` and `aria-labelledby` pointing to the group heading. |
| Checked state | `aria-checked="true|false"` | Update dynamically on selection. Native radio input handles this automatically. |
| Keyboard navigation | Arrow keys within group | Arrow keys must both move focus and select. Tab should exit the group, not navigate within it. |
| Disabled | `aria-disabled="true"` + `disabled` | Disabled radio is skipped by Tab and Arrow keys. Provide a tooltip or hint explaining why it's unavailable. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Checked border and inner dot fill |
| `--border` | `rgba(255,255,255,.16)` | Unchecked circle track border |
| `--text` | `#f4f2ee` | Label text color |
| `--text3` | `rgba(244,242,238,.32)` | Hint / description text color |
| `--pill` | `100px` | Border-radius for circle track and inner dot |
| `--state-disabled-opacity` | `0.35` | Disabled radio opacity |
| `--dur-fast` | `120ms` | Select/deselect transition duration |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-radio-group` | Root group container — flex column gap 12px |
| `.ds-radio` | Single radio row — flex, align-items center, gap 10px |
| `.ds-radio__control` | 20px circle — border-subtle, r-pill |
| `.ds-radio__control--checked` | Green border + green inner dot 10px |
| `.ds-radio__label` | 14px text2 |
| `.ds-radio--disabled` | 38% opacity, no pointer events |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | required | Controlled selected value |
| `onValueChange` | (v: string) => void | required | Change handler |
| `defaultValue` | string | undefined | Uncontrolled initial value |
| `disabled` | boolean | false | Disable all options |
| `orientation` | "vertical" | "horizontal" | "vertical" | Layout direction |
| `children` | ReactNode | required | RadioItem components |

## Code examples

````
<label class="radio-wrap">
  <input type="radio" name="quality" value="720p" class="sr-only">
  <span class="radio" aria-hidden="true"></span>
  <span class="radio-label">720p</span>
</label>
````

````
<fieldset style="border:none; padding:0;">
  <legend style="font-size:13px; font-weight:700; color:var(--text2); margin-bottom:12px;">
    Video quality
  </legend>
  <div class="radio-group" role="radiogroup" aria-labelledby="quality-legend">
    <label class="radio-wrap">
      <input type="radio" name="quality" value="480p">
      <span class="radio"></span>
      <span class="radio-label">480p</span>
    </label>
    <label class="radio-wrap">
      <input type="radio" name="quality" value="720p" checked>
      <span class="radio is-checked"></span>
      <span class="radio-label">720p</span>
    </label>
    <label class="radio-wrap">
      <input type="radio" name="quality" value="1080p">
      <span class="radio"></span>
      <span class="radio-label">1080p</span>
    </label>
  </div>
</fieldset>
````

````
<label class="radio-wrap" style="align-items:flex-start;">
  <input type="radio" name="plan" value="ultimate" class="sr-only">
  <span class="radio is-checked" aria-hidden="true" style="margin-top:3px;"></span>
  <span>
    <span class="radio-label">JioGames Ultimate</span>
    <span class="radio-hint">Includes PC, Mobile &amp; TV access</span>
  </span>
</label>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--dur-fast`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--pill`
- `--state-disabled-opacity`
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

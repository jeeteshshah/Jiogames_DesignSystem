# Label — JioGames DLS spec

> Source: `label/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Label

---

Semantic text element that associates a visible name with a form control. Required above every input field.

Label variants · Required, Optional, With hint text

Labels are the visible text identifiers that sit above form fields. They tell the user what information belongs in each input. Every form field in JioGames — text inputs, selects, textareas, radio groups, checkbox groups — must have an associated label. Labels are never decorative; they are a functional accessibility requirement that connects the visual UI to assistive technology.

- **Required marker** — red asterisk suffix signals that the field must be completed before submission
- **Optional marker** — grey "(optional)" suffix reduces friction by clarifying which fields can be skipped
- **Hint text** — a secondary line below the label for format guidance, privacy notes, or constraints
- **Error state** — label turns negative red when its associated field has a validation error

## When to use

Use when

- Field labels above or beside form controls
- Required field indicators (* suffix)
- Accessible association between a label and its input (htmlFor)
- Group labels for radio/checkbox sets

Don't use when

- Placeholder text as a substitute for a visible label — accessibility violation
- Decorative section headings — use an h2/h3 instead
- More than one line of label text — keep labels concise

## Best practices

- Always place the label above the input — never to the side or inside (placeholder-only)
- Associate labels programmatically using `for`/`id` or a wrapping `` element
- Mark only truly required fields with an asterisk — if most fields are required, mark the optional ones instead
- Use hint text for format guidance: "10-digit mobile number, no spaces"
- Persist the label even when the field is focused — never hide it on focus

- Use placeholder text as the sole label — placeholders disappear on input and are not reliably read by screen readers
- Use floating/animated labels — they shift context during entry and confuse error recovery
- Mark every single field as required — it creates noise and reduces trust in which fields are truly critical
- Put error messages inside the label — use a separate error text element below the input
- Truncate long labels with ellipsis — wrap to a second line instead

## Anatomy

A label consists of the label text, an optional required or optional marker, and an optional hint line below. All three are vertically stacked above the input.

1. 1 Label text Required 13px bold, color var(--text2). Sentence case. Describes what the field collects — not what to do with it ("Mobile number", not "Enter your mobile number"). `font-size:13px; font-weight:700; color:var(--text2)`
2. 2 Required / Optional marker Conditional Required: red " *" appended via CSS ::after. Optional: grey " (optional)" in 11px. Use one or the other — never both on the same label. `.label--required::after { content: ' *'; color: var(--negative); }`
3. 3 Hint text Optional 12px, var(--text3), 1.5 line-height. Sits between the label and the input. Used for format guidance or privacy notes. Not the same as error text. `font-size:12px; color:var(--text3); margin-top:4px`

## Variants

Four label variants cover every form field context. Default is used when the field is implicitly required. Required and Optional are mutually exclusive markers.

## Sizes

Three sizes scale the label to match the density of the surrounding form. M (13px) is the default for all standard forms. S (11px) is for compact inline forms. L (15px) is for prominent single-field surfaces like search or OTP entry.

## States

Labels have three states that respond to the state of their associated input. The label itself does not have a hover or focus state — those belong to the input.

## Content guidance

- Use sentence case — "Date of birth" not "Date Of Birth"
- Describe what the field collects — "Mobile number" not "Enter your mobile number"
- Be specific — "Jio mobile number" not just "Number" when context matters
- Keep labels under 4 words; use hint text for additional context
- Never end a label with a colon — the visual stacking already implies the relationship

- Use for format guidance: "DD/MM/YYYY", "10-digit number, no spaces"
- Use for privacy assurance: "Your number is never shared with third parties"
- Use for constraints: "Minimum 8 characters, at least one number"
- Do not duplicate what the placeholder says — they should add different information
- Hint text is not error text — keep them in separate elements with distinct styles

## Platform considerations

- Always above the input — never floating or inside
- Use M (13px) size for all standard form fields
- Ensure the label tap area is at least 44px tall including hint text
- When the keyboard appears, label must remain visible above the scrolled input

- Always above the input — inline labels (to the left) are permitted only in dense data-entry tables
- Clicking the label must focus its associated input — always use `for`/`id`
- Use M or L sizes; S only in toolbar or compact filter panels
- Error state label color must maintain 4.5:1 contrast against the background

- Labels are used on TV in settings and account screens
- Use L (15px) minimum — 13px is too small at 3-metre viewing distance
- Increase label-to-input gap to 10px at TV scale
- Required markers (*) must be accompanied by a legend visible on the same screen

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Required asterisk pulse (error) | `--ease-out` | `--dur-fast` | color transition to red |

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Label association | `` | The `for` attribute must match the input's `id` exactly. Alternatively, wrap the input inside the `` element. |
| Required fields | `aria-required="true"` on the input | The visual asterisk is CSS-only and invisible to screen readers. Always add `aria-required="true"` to the input itself. |
| Hint text | `aria-describedby` on the input | Set `aria-describedby="hintId"` on the input pointing to the hint element's `id`. Screen readers announce hint text after the label. |
| Error text | `aria-describedby` + `aria-invalid="true"` | Set `aria-invalid="true"` on the input and point `aria-describedby` to the error message element. |
| Placeholder as label | Never | Placeholders are not labels. They disappear on input, are not reliably announced by screen readers, and fail WCAG 1.3.1 at contrast ratios below 4.5:1. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--text2` | `rgba(244,242,238,.55)` | Default label text color |
| `--text3` | `rgba(244,242,238,.32)` | Hint text color and "(optional)" marker |
| `--negative` | `#FF4757` | Required asterisk color and error state label color |
| `--jio-font` | `'Outfit', sans-serif` | Label font family |
| `--state-disabled-opacity` | `0.35` | Disabled label opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-label` | Root — 13px 600, text color var(--text) |
| `.ds-label--required::after` | Appends " *" in jio-green |
| `.ds-label--error` | Red color for error-state labels |
| `.ds-label--disabled` | text3 color, 38% opacity |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `htmlFor` | string | required | ID of the associated form control |
| `required` | boolean | false | Appends required asterisk |
| `disabled` | boolean | false | Muted appearance when field is disabled |
| `children` | ReactNode | required | Label text content |

## Code examples

````html
<div class="form-field">
  <label class="label" for="displayName">Display name</label>
  <input type="text" id="displayName" placeholder="Your in-game name">
</div>
````

````html
<div class="form-field">
  <label class="label label--required" for="email">Email address</label>
  <input
    type="email"
    id="email"
    aria-required="true"
    placeholder="you@example.com"
  >
</div>

<!-- Note: the asterisk is CSS-only (.label--required::after).
     aria-required="true" on the input communicates the requirement
     to screen readers independently of visual styling. -->
````

````html
<div class="form-field">
  <label class="label label--required" for="phone">Phone number</label>
  <span class="label-hint" id="phone-hint">
    10-digit Jio number — used for OTP only
  </span>
  <input
    type="tel"
    id="phone"
    aria-required="true"
    aria-describedby="phone-hint"
    placeholder="+91 98765 43210"
  >
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--input-placeholder`
- `--jio-font`
- `--negative`
- `--r3`
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

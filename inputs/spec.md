# Inputs — JioGames DLS spec

> Source: `inputs/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Inputs

---

Inputs let players enter text, search for games, and provide information across JioGames.

Inputs are used in authentication flows (phone number, OTP), search, profile editing, and any form that requires player-supplied information. The system covers three size tiers, seven visual states, and optional icon affordances for leading icons and trailing actions.

- **Size.** Three canonical sizes — S, M, L — resolve to different heights on Mobile, Web, and TV via token aliases.
- **States.** Seven states: Default, Focus, Filled, Disabled, Error, Success, Loading — driven by CSS classes from `states.css`.
- **Slots.** Label, leading icon, field container, placeholder/value, trailing action, and helper/error text. Only the field container is required.
- **Token-driven.** All sizing and color tokens live in `tokens/tokens.css`. Changing `--input-border-focus` updates every focused input across all surfaces.
- **Platform-aware.** Same class resolves to different pixel heights on Mobile (54px), Web (52px), and TV (72px) for the L size via platform token aliases.

## When to use

Use when

- Single-line text entry: search, username, email, OTP
- Numeric entry: PIN, age, quantity
- Password fields with show/hide toggle
- Any field that needs a label, hint text, and error state

Don't use when

- Multi-line text — use Textarea instead
- Structured selections (dates, options) — use DatePicker or Select
- Search bars in the AppBar — use the AppBar search pattern
- Inputs without visible labels (placeholder-only) — accessibility violation

## Best practices

Inputs are high-friction components. Every decision — label, placeholder, validation timing — directly affects completion rate.

- Always show a visible label above the field
- Use M (44px) or L (54px) on mobile — never S for primary inputs
- Show error text inline below the field, not in a toast
- Validate on blur, not on every keystroke
- Use a leading icon to reinforce the input type (search icon for search)
- Persist the label when the field is focused — never hide it
- On TV, use L size and make the focus ring clearly visible

- Don't use placeholder text as a substitute for a label
- Don't validate on each keystroke — it frustrates players mid-type
- Don't show error state before the player has interacted with the field
- Don't use S inputs as primary form fields on mobile
- Don't leave inputs without helper text in authentication flows
- Don't auto-dismiss the keyboard when focus is still needed
- Don't place two inputs side by side on mobile without sufficient spacing

## Anatomy

A full input is composed of up to seven zones. Only the field container is required. Every other slot is optional but must be used intentionally.

## Variants

Four input variants cover the full range of JioGames data-entry contexts. Choose the simplest variant that meets the task.

## Sizes

Three canonical sizes cover all input use cases. Platform context resolves the actual pixel height via token aliases. Use L for primary inputs, M for secondary, S only in dense UI.

## States

Seven states cover the full lifecycle of an input field. Apply `.is-*` classes from `states.css` to simulate states in prototypes and documentation.

## Content guidance

Labels, placeholders, helper text, and error messages are just as much part of the input component as the visual field itself.

- Always visible — never replace a label with a placeholder
- Title case: "Mobile Number" not "mobile number"
- Keep to 1–3 words; avoid parenthetical instructions in the label
- Optional fields: add "(optional)" in muted text after the label

- Use for format hints: "9876543210" for phone, "user@email.com" for email
- Don't repeat the label as the placeholder
- Placeholder disappears on focus — don't rely on it for critical info
- Keep under 30 characters; placeholder crops in narrow inputs

- Use to provide context the player needs before typing: "We'll send an OTP"
- Keep to one line (11px) — avoid multi-line helper text
- Disappears when error or success state is shown
- Always present in auth flows where players may be uncertain

- Specific: "Enter a valid 10-digit number" not "Invalid input"
- Avoid blame: "Number not found" not "You entered the wrong number"
- Show on blur, not on each keystroke
- Never show error before the player has interacted with the field

## Platform considerations

Each platform requires distinct input behaviors. Same size tokens, different interaction patterns and keyboard behaviors.

- Use `type="tel"` for phone numbers — triggers numeric keyboard
- L size (54px) for primary inputs; M (44px) minimum for any input
- Bottom sheet inputs must scroll above the keyboard
- Auto-advance OTP fields on input
- Validate on blur, not on each keystroke
- `inputmode="numeric"` for number-only fields

- Hover: subtle border brightness increase before focus
- Focus: 1px green border + soft ambient glow
- M size (44px) acceptable for secondary inputs in web forms
- Auto-complete via `autocomplete` attributes where appropriate
- Keyboard: Tab to advance, Shift+Tab to go back
- Password: show/hide toggle required for password fields

- L size only — never S or M on TV
- TV focus glow: `--tv-focus-shadow` replaces the subtle web ring
- D-pad navigates between input fields and the on-screen keyboard
- On-screen keyboard required — no hardware keyboard assumption
- Auto-fill from JioID profile where available to reduce TV input friction
- OTP: use voice input shortcut if platform supports it

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Focus ring | `instant` | `0ms` | outline (2px jio-green) |
| Error shake | `--ease-out` | `400ms` | transform translateX keyframes |
| Error message slide in | `--ease-out` | `--dur-fast` | opacity, max-height |
| Clear button appear | `--ease-out` | `--dur-fast` | opacity |
| Password toggle | `--ease-out` | `--dur-fast` | opacity crossfade |

## Platform rules

Mobile

- 48px height (var(--ctrl-h)) — mandatory for comfortable touch
- Keyboard type: use type=email, type=tel, type=number for correct soft keyboard
- Auto-scroll: focused input scrolls above soft keyboard automatically
- Clear button (×) appears in trailing slot when field has value

Web

- Focus ring: 2px jio-green outline via :focus-visible
- Inline validation: show error on blur, clear error on fix
- Password show/hide toggle in trailing slot
- Autofill styled consistently — override browser yellow with surface-1 bg

TV

- On-screen keyboard shown automatically on focus
- 56px height variant for TV — larger touch/remote target
- Avoid mandatory text fields on TV — prefer radio or select patterns
- Cursor blink must be visible: use jio-green, 2px wide, standard blink rate

## Accessibility

Inputs must work with keyboard navigation, screen readers, and assistive touch. Authentication flows especially cannot afford accessibility failures.

- Tab — moves focus to the next input
- Shift+Tab — moves focus to the previous input
- Escape — dismisses any inline suggestion panel
- OTP fields: auto-advance on character entry; backspace returns to previous

- Add `aria-invalid="true"` to the input when error state is active
- Link the error message via `aria-describedby` on the input
- Use `aria-live="polite"` so screen readers announce new error text
- Never rely on color alone to signal errors — include text

- Input value text: `#F4F2EE` on `#0E1119` — 12.5:1 contrast ratio
- Placeholder: `#6B7280` on `#0E1119` — 4.9:1 (decorative threshold accepted)
- Error text: `#FF4757` — meets 4.5:1 on dark backgrounds
- Disabled: 0.38 opacity — decorative, not required to meet contrast

## Related tokens

All input sizing and color values come from `tokens/tokens.css`. Update once — every input instance reflects the change.

| Token | Value | Swatch | Usage |
|---|---|---|---|
| `--input-bg` | `var(--surface-1)` → #0E1119 |   | Field background |
| `--input-border` | `var(--border)` → rgba(255,255,255,.1) |   | Default border color |
| `--input-border-focus` | `var(--jio)` → #00A859 |   | Focus state border |
| `--input-border-error` | `var(--negative)` → #FF4757 |   | Error state border |
| `--input-text` | `var(--text)` → #F4F2EE |   | Input value text color |
| `--input-placeholder` | `var(--text3)` → #6B7280 |   | Placeholder text color |
| `--input-radius` | `var(--r4)` → 14px | — | Field corner radius |

| Token | Mobile | Web | TV |
|---|---|---|---|
| `--input-s-h` | 36px | 38px | 56px |
| `--input-m-h` | 44px | 44px | 64px |
| `--input-l-h` | 54px | 52px | 72px |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-input` | Root input element — 48px height, surface-1, border-subtle, r3 |
| `.ds-input:focus` | Green outline, border-color: jio |
| `.ds-input--error` | Red border and error message below |
| `.ds-input--disabled` | 38% opacity, no pointer events |
| `.ds-input-wrapper` | Container for leading/trailing icon slots |
| `.ds-input__leading` | Leading icon or prefix text |
| `.ds-input__trailing` | Trailing icon, clear button, or unit label |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | undefined | Controlled value |
| `onChange` | (e: ChangeEvent) => void | undefined | Change handler |
| `type` | "text" | "password" | "email" | "number" | "search" | "text" | Input type |
| `placeholder` | string | undefined | Placeholder text |
| `error` | string | boolean | undefined | Error message or boolean error state |
| `hint` | string | undefined | Helper text below field |
| `leading` | ReactNode | undefined | Leading slot content |
| `trailing` | ReactNode | undefined | Trailing slot content |
| `disabled` | boolean | false | Disable the field |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="input-wrap">
  <input
    class="input-field"
    type="text"
    id="username"
    placeholder="Enter username"
    aria-label="Username"
  >
</div>
````

````html
<div style="display:flex;flex-direction:column;gap:6px">
  <label for="email" style="font-size:13px;font-weight:700;color:var(--text)">
    Email <span style="color:var(--negative)">*</span>
  </label>
  <div class="input-wrap">
    <input
      class="input-field is-error"
      type="email"
      id="email"
      value="bad@"
      aria-invalid="true"
      aria-describedby="email-error"
    >
  </div>
  <div id="email-error" style="font-size:11px;color:var(--error-text)" role="alert">
    Enter a valid email address
  </div>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-strong`
- `--border-subtle`
- `--ctrl-h`
- `--dur-icon-spin`
- `--error-text`
- `--glass-1`
- `--gold`
- `--input-bg`
- `--input-border`
- `--input-border-focus`
- `--input-l-h-mobile`
- `--input-l-h-tv`
- `--input-l-h-web`
- `--input-m-h-mobile`
- `--input-m-h-tv`
- `--input-m-h-web`
- `--input-placeholder`
- `--input-radius`
- `--input-s-h-mobile`
- `--input-s-h-tv`
- `--input-s-h-web`
- `--input-text`
- `--jio`
- `--jio-3`
- `--jio-font`
- `--negative`
- `--r3`
- `--r4`
- `--surface-1`
- `--surface-2`
- `--surface-3`
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

# Forms — JioGames DLS spec

> Source: `forms/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Forms

---

Form patterns for collecting user input across login, payment, preferences, and settings flows.

FORMS · LOGIN, OTP, VALIDATION STATES

## Overview

JioGames forms are dark-first, minimal-chrome input collections. Every field follows the label → input → helper/error stack. Use `.input-field` inside `.input-wrap` for consistent focus rings and surface treatment. Never raw `` without a wrapper.

## Anatomy

A single field is composed of up to 7 layers. Only Label and Input are required.

1. Field label `font-size:13px font-weight:700` — primary text colour Required
2. Required marker `*` in `var(--negative)`, placed after label text Optional
3. Input `.input-field` inside `.input-wrap` Required
4. Placeholder Descriptive example text — never a label substitute Optional
5. Helper text 11px guidance text, `var(--text3)` Optional
6. Error message 11px, `var(--error-text)` — shown when `.is-error` Conditional
7. Success message 11px, `var(--success-text)` — shown when `.is-success` Conditional

## Field types

All supported input variants. Use native elements with `.input-field` styling — never custom replacements.

## Validation states

Validate on blur. Surface errors inline below the input. Use colour + message — never icon-only.

## Field groups

Group related fields under a section label separated by a subtle divider. Use a 2-column grid only when fields are short (first/last name, day/month).

## Complete form — Login

The OTP login form used across mobile and web. OTP boxes are large, square, centred inputs — each accepts one digit.

## Error summary

When a form has multiple errors on submit, list them all at the top of the form in a summary block. Use `role="alert"` so screen readers announce immediately.

- • Email address is required
- • Password must be at least 8 characters

## State matrix

All field types across all interactive states. Apply states via class on `.input-field`.

## Platform behavior

- Full-width inputs — no max-width constraint within the form
- Keyboard pushes content up — use `viewport-fit=cover` and `padding-bottom: env(safe-area-inset-bottom)`
- OTP inputs auto-advance focus on each keystroke
- Submit CTA pinned to bottom above safe area
- Use `inputmode="numeric"` on OTP fields to show numeric keyboard

- Max-width 480px on form containers
- Tab key navigates through fields in DOM order
- Enter key submits if focus is inside the form
- Validate on blur — never on every keystroke
- Show error immediately after blur, not only on submit

## Accessibility

Forms are high-risk for accessibility failures. Follow every rule below — no exceptions.

## Content guidance

### Labels

Use sentence case. Be specific: "Mobile number" not "Phone". Never use technical keys: "user_id" or "emailAddress". Labels sit above the field — never inside it.

### Placeholder text

Placeholder is an example — not a label, not instructions. Use realistic examples: "+91 98765 43210", "you@example.com". Disappears on type, so never put required info here.

### Helper text

Short factual guidance below the field: "We'll use this for account recovery". Write in present tense. Disappears when an error or success message appears.

### Error messages

Be specific and actionable: "Password must be at least 8 characters" not "Invalid". State what went wrong and what to do. Never use "Error" alone.

### Required markers

Mark required fields with * (asterisk) in var(--negative). Add a legend above the form: "* Required fields". Do not mark optional fields — mark required ones only.

### CTA copy

Use specific action verbs that describe what happens next: "Continue", "Send OTP", "Verify", "Save changes". Avoid "Submit" or "OK".

## Do / Don't

## Form layout variants

Choose a layout based on platform and field density. Never use two-column on mobile — inputs become too narrow for comfortable touch.

## Validation lifecycle

Fields progress through discrete states. Trigger validation on blur — never on every keystroke. Apply state classes to `.input-field`.

| State | Class | Border | Message | Trigger |
|---|---|---|---|---|
| **Idle** | `—` | `var(--border)` | Helper text if any | Page load / untouched |
| **Touched** | `—` | `var(--border)` | Helper text persists | User focuses the field |
| **Valid** | `.is-success` | `var(--success-text)` | Confirmation message | On blur, passes validation |
| **Error** | `.is-error` | `var(--negative)` | Specific error message | On blur, fails validation |
| **Submitting** | `.is-loading` | `var(--border)` | None — inputs disabled | Form submit in flight |
| **Success** | `.is-success` on form | — | Success toast / redirect | Server confirms submission |

## Related tokens

Core tokens that control input field appearance. Never hard-code values — reference these variables everywhere.

| Token | Role |
|---|---|
| `--surface-2` | Input background (`--input-bg` alias) |
| `--border` | Default input border (`--input-border` alias) |
| `--negative` | Error border ring (`--error-border` alias) |
| `--success-text` | Success border ring (`--success-border` alias) |
| `--r3` | Standard input corner radius (`--input-radius` alias, 12px) |
| `--r4` | OTP box corner radius (14px) |
| `--ctrl-h` | Standard input height (54px) |
| `--focus-shadow` | Focus ring: `0 0 0 2px var(--jio)` |

## Tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | #161A24 | Input background |
| `--border` | rgba(255,255,255,.1) | Default input border |
| `--border-subtle` | rgba(255,255,255,.08) | Divider lines in field groups |
| `--jio` | #00A859 | Focus ring, accent, checkbox/radio |
| `--focus-shadow` | 0 0 0 2px var(--jio) | Focused input ring |
| `--negative` | #FF4757 | Required marker, error border |
| `--error-text` | #FF4757 | Error message text |
| `--success-text` | #00A859 | Success message text |
| `--warning-text` | #F59E0B | Warning message text |
| `--text3` | #6B7280 | Helper/placeholder text |
| `--r3` | 12px | Standard input border-radius |
| `--r4` | 14px | OTP input border-radius |
| `--ctrl-h` | 54px | Standard input height |
| `--touch-min` | 44px | Minimum touch target |
| `--state-disabled-opacity` | 0.32 | Disabled field opacity |

## Figma component names

## CSS classes

````css
.input-field         — base input styles (text, email, password, tel, select)
.input-wrap          — wrapper that applies border + focus ring treatment
.input-field.is-hover     — hover state (web only)
.input-field.is-focused   — focused state — shows --focus-shadow ring
.input-field.is-error     — error border + red ring
.input-field.is-success   — success border + green ring
.input-field.is-warning   — warning border + amber ring
.input-field.is-disabled  — 0.32 opacity, pointer-events:none
.input-field.is-loading   — loading state, typically a spinner in wrapper
````

## Rules

## When to use

Use when

- Multi-field data collection: registration, profile edit, payment
- Structured settings pages with labelled controls
- Feedback and support request flows
- Search filter panels with multiple input types

Don't use when

- Single-field interactions — use the Input component directly
- Wizard-style flows with more than 5 steps — split into separate screens
- Read-only data display — use a Description List instead

## Variants

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Default | 480px max-width | Standard forms | Mobile / Web |
| Narrow | 320px max-width | Short forms (login, OTP) | Mobile |
| Wide | 680px max-width | Complex settings | Web |

## States

Idle

All fields in default state; no validation shown

Active

A field is focused; its label and border are highlighted

Validation error

Invalid field shows red border + error message below

Validation success

Valid field shows green border + checkmark (optional)

Submitting

Submit button shows spinner; all fields disabled

Submitted

Success state — fields cleared or replaced with confirmation

Disabled

All fields at 38% opacity; no interaction possible

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Validation error shake | `--ease-out` | `400ms` | transform translateX (keyframes) |
| Error message appear | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Success checkmark | `--ease-out` | `--dur-fast` | stroke-dashoffset, opacity |
| Submit spinner | `linear` | `600ms infinite` | transform rotate |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-form` | Root form container — flex column, gap 24px |
| `.ds-form-field` | Single field wrapper — flex column, gap 6px |
| `.ds-form-label` | Field label — 13px 600 |
| `.ds-form-hint` | Helper text below input — 12px text3 |
| `.ds-form-error` | Validation error — 12px negative color |
| `.ds-form-section` | Grouped fields with a section title |
| `.ds-form-actions` | Submit/cancel button row |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `onSubmit` | (data: FormData) => void | required | Submit handler |
| `defaultValues` | Record | undefined | Initial field values |
| `resolver` | Resolver | undefined | Validation schema (zod, yup) |
| `disabled` | boolean | false | Disable all fields |
| `children` | ReactNode | required | Form fields and actions |

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--ctrl-h`
- `--error-text`
- `--jio`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--r7`
- `--state-disabled-opacity`
- `--success-text`
- `--surface-1`
- `--text`
- `--text2`
- `--text3`
- `--touch-min`
- `--warning-text`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# Dialogs — JioGames DLS spec

> Source: `dialogs/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Dialogs

---

Dialogs present focused tasks or critical decisions that require player confirmation before proceeding.

Dialogs interrupt the player with a focused question or task. They block background interaction until resolved. Use sparingly — every dialog adds friction.

- **When to use.** Confirmation for destructive or irreversible actions, collecting short input, and surfacing critical alerts that require an immediate response.
- **When not to use.** Informational toasts or snackbars, navigation decisions, non-urgent notifications, and confirmations for reversible actions.
- **Interruption cost.** Every dialog pauses the player's primary task. Reserve dialogs for moments where the risk of proceeding without confirmation is high.

## When to use

Use when

- Destructive action confirmation (delete account, cancel subscription)
- Critical decisions requiring explicit user acknowledgement
- Short forms that should not navigate away from the current screen
- Error states requiring immediate user response

Don't use when

- Non-critical messages — use Toast or Banner instead
- Large forms or multi-step flows — use a dedicated screen or Bottom Sheet
- Stacking multiple dialogs — resolve one before showing another
- Auto-showing on page load without user trigger

## Best practices

Follow these rules to keep dialog usage consistent and respectful of the player's attention.

- Use for irreversible or high-stakes actions only
- Keep body copy to 2 sentences maximum
- Lead with the most important information in the title
- Use specific button labels — "Delete save data", not "OK"
- Animate in with fade + scale (0.92 → 1, 200ms ease-out)
- Return focus to the trigger element on dismiss
- Always include a Cancel or dismissal path

- Use for non-blocking messages — use toasts instead
- Stack multiple dialogs on top of each other
- Use full-screen for simple 2-button confirmation
- Use vague labels like "OK", "Yes", or "No"
- Block dialogs with inline loading spinners on the scrim
- Auto-open dialogs without a clear user trigger
- Exceed 4 interactive elements inside the dialog

## Anatomy

Every dialog is built from five parts. The Scrim, Container, Body, and Button row are required. The Icon slot is optional but strongly recommended for destructive and alert variants.

## Variants

Five dialog variants cover the full range of blocking interactions. Choose the lowest-weight variant that still communicates urgency accurately.

## Sizes

Dialog dimensions are fixed per platform. Do not resize dialogs dynamically — use the platform-specific values below.

| Property | 📱 Mobile | 💻 Web | 📺 TV |
|---|---|---|---|
| Max-width | 360px | 480px | 640px |
| Padding | 24px | 32px | 40px |
| Title font-size | 18px | 20px | 28px |
| Body font-size | 14px | 15px | 20px |
| Border-radius | 20px (var(--r7)) | 20px (var(--r7)) | 28px |
| Button size | .btn--m | .btn--m | .btn--l |
| Scrim opacity | 0.55 | 0.55 | 0.7 |

## States

Dialogs have three lifecycle states. Use CSS transitions to smooth the opening and closing experience.

## Content

Dialog copy must be direct, specific, and consequential. Vague language increases hesitation and erodes player trust.

- Maximum 8 words
- Sentence case throughout
- Question format for confirmations: "Delete save data?"
- Statement for alerts: "Session expired"
- Match the action exactly — no metaphors

- Maximum 2 sentences
- Plain language — no jargon or technical terms
- State what happens AND the consequence
- "This will permanently remove…" not "Data will be deleted"
- Avoid repeating the title in the body

- Use verb phrases, not nouns
- Match the action exactly: "Delete save data" not "Delete"
- Secondary / cancel is always "Cancel"
- Primary is always the action verb
- Never "OK", "Yes", "No", or "Confirm"

## Platform guidance

Dialog behavior adapts per platform. The visual structure stays consistent; scale and interaction model differ.

- Max-width: 360px, centered in viewport
- Appears centered or as full-screen on small phones
- Border-radius: 20px (var(--r7))
- Scrim tap dismisses non-critical dialogs
- Full-screen variant available for complex tasks
- Minimum touch target: 44px for buttons

- Max-width: 480px, always centered
- Never bottom-sheet style on desktop
- Border-radius: 20px (var(--r7))
- Escape key always dismisses
- Full-screen variant not used
- Backdrop click dismisses non-critical dialogs

- Max-width: 640px, centered
- Never use bottom sheet style
- Border-radius: 28px for legibility at distance
- Use .btn--l size, never .btn--m or smaller
- D-pad navigates between buttons
- Back button on remote dismisses

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-fast` | opacity, transform scale(0.95 → 1) |
| Close | `--ease-in` | `--dur-fast` | opacity, transform scale(1 → 0.95) |
| Scrim fade in | `--ease-out` | `--dur-fast` | opacity |
| Scrim fade out | `--ease-in` | `--dur-fast` | opacity |
| Shake (error) | `--ease-out` | `400ms` | transform translateX (keyframes) |

## Accessibility

Dialogs must be usable by keyboard, screen reader, and assistive technology. These requirements are non-negotiable.

## Platform considerations

- Appears centred with dark backdrop; max width 320px
- Touch outside backdrop dismisses when isDismissible is true
- Limit to 2 actions; stack vertically if labels are long
- Avoid dialogs during active gameplay — use toast or banner instead

- Max width 400px; centred with semi-transparent backdrop
- Keyboard: Tab cycles focus; Esc dismisses; Enter confirms primary action
- Focus traps inside dialog while open
- Scroll lock on body while dialog is open

- Render as full-width centred card; avoid small text
- Minimum 2 D-pad-focusable action buttons
- Back button on remote = cancel/dismiss
- Use size L or XL buttons inside TV dialogs

## Related tokens

The following design tokens control dialog appearance. Override at the platform-specific token layer, never inline.

| Token | Default value | Usage |
|---|---|---|
| `--overlay-scrim` | rgba(0,0,0,.55) | Scrim background behind the dialog |
| `--r7` | 20px | Dialog container border-radius |
| `--surface-2` | #0e1118 approx. | Dialog card background |
| `--border` | rgba(255,255,255,.1) approx. | Dialog card border |
| `--shadow-4` | 0 24px 48px rgba(0,0,0,.6) | Elevation shadow on dialog card |
| `--dur-pop` | 200ms | Open animation duration |
| `--dur-default` | 150ms | Close animation duration |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-dialog` | Root dialog panel — surface-2, r5, max-w 480px |
| `.ds-dialog__scrim` | Full-screen backdrop — rgba(0,0,0,.6) |
| `.ds-dialog__header` | Title + optional icon row |
| `.ds-dialog__title` | Dialog title — 18px 700 |
| `.ds-dialog__body` | Content area — 14px text2 |
| `.ds-dialog__footer` | Action buttons row — flex end |
| `.ds-dialog__close` | Top-right × button |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | required | Controls dialog visibility |
| `onOpenChange` | (open: boolean) => void | required | Close handler |
| `title` | string | required | Dialog heading |
| `description` | string | undefined | Body copy below title |
| `actions` | ReactNode | undefined | Footer button row |
| `size` | "sm" | "md" | "lg" | "md" | Max-width preset |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<!-- Backdrop -->
<div class="dialog-backdrop" aria-hidden="true"></div>

<!-- Dialog -->
<div
  class="dialog"
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <h2 id="dialog-title" class="dialog__title">Remove game?</h2>
  <p id="dialog-desc" class="dialog__body">This will remove War Thunder from your library.</p>
  <div class="dialog__actions">
    <button class="btn btn--ghost btn--m btn--hug">Keep</button>
    <button class="btn btn--primary btn--m btn--hug">Remove</button>
  </div>
</div>
````

````
// Trap focus inside dialog while open
function trapFocus(dialogEl) {
  const focusable = dialogEl.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];
  dialogEl.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey) {
      if (document.activeElement === first) { e.preventDefault(); last.focus(); }
    } else {
      if (document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  first.focus();
}
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--negative`
- `--r4`
- `--r7`
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

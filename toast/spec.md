# Toast — JioGames DLS spec

> Source: `toast/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Toast

---

Toasts provide brief, non-blocking feedback after a player completes an action.

**TV platform:** The Toast component is not used on TV. Use the **Banner** component for persistent feedback on the TV surface.

Three toast variants stacked at the bottom of a screen. Oldest dismisses first.

Toasts appear briefly at the bottom of the screen to confirm that an action completed — successfully or otherwise. They are non-blocking: the player can keep interacting with the app while the toast is visible. Toasts auto-dismiss after 4 seconds. For persistent feedback, use a Banner instead.

- **Bottom-anchored.** Toasts always appear at the bottom, above the nav bar.
- **Auto-dismiss.** Visible for 4 seconds. Never require a player action to dismiss.
- **Non-blocking.** Never cover primary interactive content or navigation.
- **Brief message.** Max 60 characters. No punctuation at end.

## When to use

Use when

- Brief feedback after a user action (game added to library, pass activated)
- Transient success/error confirmations that auto-dismiss
- Undo prompts immediately after a reversible action

Don't use when

- Persistent messages that require user action — use Banner
- Destructive confirmations — use Dialog
- More than one toast at a time — queue them
- Toasts that contain interactive forms or multi-step flows

## Best practices

- Keep message under 60 characters
- Use past tense for success: "Game added", "Pass activated"
- Use present tense for errors: "Can't connect", "Download failed"
- Stack toasts (max 3 visible at once); oldest dismisses first
- Include action link only when undo or follow-up is meaningful
- Match icon to semantic meaning (green check, red ×, spinner)

- Don't use toasts for errors that require user resolution — use a Banner or dialog
- Don't end toast messages with periods
- Don't use toasts on TV (use Banner component instead)
- Don't show more than 3 toasts simultaneously
- Don't use toasts for promotional content
- Don't change toast position (must be bottom of screen, above tab bar)

## Anatomy

Five distinct parts make up a toast. Container and message are always required; icon is strongly recommended; action link and timer bar are optional.

1. 1 **Toast container** — Required. border-radius: 14px; padding: 12px 14px. Background --surface-2 with a --border stroke and elevation shadow.
2. 2 **Icon (status)** — Required. 18 × 18px. Green check for success, red × for error, amber ! for warning, gray ℹ for info, spinner for loading. flex-shrink: 0.
3. 3 **Message text** — Required. Max 60 characters. font-size: 13px; font-weight: 500. One line preferred; two lines maximum.
4. 4 **Action link** — Optional. 1–2 words only. Green color (--jio). "Undo", "View", "Retry". No button chrome. Keyboard-focusable while toast is visible.
5. 5 **Auto-dismiss timer bar** — Optional. 2px bar anchored to the bottom edge of the container. Animates from 100% to 0% width over 4 seconds, providing a visual countdown.

## Variants

Six semantic variants cover all feedback scenarios in JioGames.

Past tense. Confirms the action completed. Green icon.

Present tense. Describes the problem. Red icon and timer bar.

Amber icon. Non-critical issue that may require attention.

Neutral. Communicates status without success or failure.

Spinner icon. Present-continuous message. Progress bar active.

Adds a green action link for undo or follow-up. 1–2 words.

## Sizes

Two height profiles exist: Compact (icon + text only) and Standard (with an action link). Heights are the natural height with defined padding — do not hardcode.

| Size | Content | Mobile height | Web height | TV |
|---|---|---|---|---|
| **Compact** | Icon + message text | 44px | 44px | Not applicable — use Banner |
| **Standard** | Icon + message + action link | 48px | 48px | Not applicable — use Banner |

Heights assume single-line message. A two-line message will increase height naturally. Padding is always 12px 14px.

## States & motion

Toasts have three motion phases: Enter, Visible, and Exit. All animations respect prefers-reduced-motion.

## Content guidelines

Toast messages are short confirmations, not explanations. Match tense to semantic type and keep to the point.

Past tense. Confirm the object that was acted on.

Present tense. Describe the problem, not the cause.

These patterns are banned in JioGames toasts.

## Platform behaviour

Toasts adapt their position and width based on the platform surface.

Anchored **bottom: 16px above the tab bar** (or screen bottom if no tab bar present). Full width with **16px horizontal margins**. Bottom safe-area inset is always respected on notched devices. Stacks upward when multiple toasts are queued.

Floats in the **bottom-right corner** of the viewport. **Max-width: 360px**. Not full-width. Positioned above any sticky footers. Right-aligned stack; newer toasts push older ones upward. Hover pauses the auto-dismiss timer.

Toast is **not available on the TV surface.**

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Slide in (bottom) | `--ease-out` | `--dur-fast` | transform translateY(100% → 0), opacity |
| Slide out | `--ease-in` | `--dur-fast` | transform translateY(0 → 100%), opacity |
| Auto-dismiss progress | `linear` | `3000ms` | width of progress indicator |
| Stack expand (multiple) | `--ease-out` | `--dur-fast` | transform translateY, scale |

## Accessibility

Toasts must be announced to screen readers without interrupting the current interaction flow unnecessarily.

| Attribute | Value | Notes |
|---|---|---|
| role | status (success, info)alert (error, warning) | Use role="alert" for errors and warnings — this interrupts the screen reader. Use role="status" for polite announcements. |
| aria-live | Auto-set by role | For loading toasts, explicitly set aria-live="polite". Do not set aria-live="assertive" unless the variant is error or warning. |
| Focus management | Non-focusable container | The toast container itself is not in the tab order. Only the optional action link receives focus (via Tab) while the toast is visible. |
| Action link keyboard | Focusable via Tab | When an action link is present, it must be reachable by keyboard tab while the toast is on screen. Activating it should dismiss the toast. |
| prefers-reduced-motion | Instant appear/disappear | Enter and exit animations are disabled. Toasts still appear and disappear; only the translate+fade transitions are suppressed. The timer bar animation is also stopped. |
| Live region | Outside main content | The toast container element should be placed at the end of the document body, outside <main>, so live region announcements do not interfere with in-page ARIA landmarks. |

## Platform considerations

- Appears at bottom, above navigation bar with 16px gap
- Auto-dismiss after 3–5s; swipe up to dismiss early
- Max one toast visible at a time; queue additional toasts
- Never use toasts for errors that require user action — use dialog or banner

- Appears bottom-right on desktop; bottom-centre on narrow web
- Auto-dismiss after 4–6s; close button always visible
- Role="status" for info; role="alert" for error/warning
- Stack vertically if multiple; newest on top

- Appears top-right; never obscures primary content area
- Not focusable — TV user cannot interact with toast
- Longer dismiss time: 6–8s to account for reading at distance
- Keep message under 60 characters; large font (min 18px)

## Content guidance

### Message length

Keep toast messages to 1 line, 60 characters max. If more explanation is needed, use a banner or dialog instead.

### Tone

Be direct and calm. "Game added to library" not "Great! Your game was successfully added to your library!"

### Action label

If the toast has an action, use a specific verb: "Undo", "View", "Retry". Never use "Click here" or "Learn more".

### Error toasts

Error toasts must have a Retry action or explain what to do next. "Failed to save — Retry" is correct. "Error occurred" alone is not.

## Related tokens

These design tokens are consumed directly by the Toast component. Do not hard-code their values.

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-toast` | Root — surface-2, border-subtle, r4, padding 14px 16px, shadow |
| `.ds-toast--success` | Green left border accent |
| `.ds-toast--error` | Red left border accent |
| `.ds-toast--warning` | Amber left border accent |
| `.ds-toast__icon` | Leading status icon — 20px |
| `.ds-toast__body` | Text content — flex column gap 2px |
| `.ds-toast__title` | 14px 600 text |
| `.ds-toast__description` | 13px text3 |
| `.ds-toast__action` | CTA link — jio-green text |
| `.ds-toast__close` | Dismiss × button |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | "default" | "success" | "error" | "warning" | "default" | Semantic color |
| `title` | string | required | Toast headline |
| `description` | string | undefined | Optional supporting text |
| `duration` | number | 3000 | Auto-dismiss delay in ms (Infinity = persistent) |
| `action` | { label: string; onClick: () => void } | undefined | Undo/CTA button |
| `onDismiss` | () => void | undefined | Fired on close |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="toast toast--success" role="status" aria-live="polite">
  <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_check"></use></svg>
  <span class="toast__message">Game added to library</span>
  <button class="btn btn--text btn--xs btn--hug toast__action">Undo</button>
  <button class="btn btn--icon toast__close" aria-label="Dismiss">✕</button>
</div>
````

````
function showToast(message, type = 'success', duration = 4000) {
  const toast = document.createElement('div');
  toast.className = `toast toast--${type}`;
  toast.setAttribute('role', type === 'error' ? 'alert' : 'status');
  toast.setAttribute('aria-live', type === 'error' ? 'assertive' : 'polite');
  toast.innerHTML = `<span class="toast__message">${message}</span>`;
  document.body.appendChild(toast);
  requestAnimationFrame(() => toast.classList.add('is-visible'));
  setTimeout(() => {
    toast.classList.remove('is-visible');
    toast.addEventListener('transitionend', () => toast.remove(), { once: true });
  }, duration);
}

// Usage
showToast('Game added to library', 'success');
showToast('Failed to save — check connection', 'error');
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--border`
- `--border-subtle`
- `--jio`
- `--negative`
- `--r3`
- `--r4`
- `--spring`
- `--surface-1`
- `--surface-2`
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

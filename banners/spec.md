# Banners — JioGames DLS spec

> Source: `banners/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Banners

---

Banners communicate important information at the top of a screen or section without blocking the player's primary task.

Info · Success · Warning — the three most common banner variants in context

## Overview

Banners communicate system-level information that affects the current screen or session. Unlike toasts (transient, bottom-anchored), banners persist at the top of a screen or section until the condition is resolved or dismissed.

- **Top-anchored.** Banners sit at the top of a screen region, never floating or overlapping content.
- **Semantic color + icon.** Color alone is insufficient for accessibility. Always pair icon with color.
- **Persistent by default.** Banners stay visible until dismissed or condition resolves. Don't auto-dismiss.
- **Max 1 banner per screen.** Stack only if each banner requires separate resolution action.

## Best Practices

- Pair icon with background color — never use color alone to convey meaning
- Keep message under 80 characters
- Use 1–2 word action labels ("Retry", "Manage", "View")
- Use success banner to confirm a completed background action
- Include dismiss button on informational and success banners
- Allow error banners to persist until the error is resolved

- Don't show more than 1 banner at a time on mobile
- Don't use banners for promotional content — use a card or rail card
- Don't auto-dismiss banners (use toast for transient feedback)
- Don't use long sentences or multiple sentences in a banner
- Don't use warning/error banners for non-actionable information
- Don't place banners inside scrollable content — they scroll away

## Anatomy

1. **Banner container** — Required. Full-width. `border-radius: 12px`. Top-anchored.
2. **Status icon** — Required. 20px. SVG. Matches semantic color. `flex-shrink: 0`.
3. **Message text** — Required. Max 80 chars. `font-size: 13px; font-weight: 500`.
4. **Action button** — Optional. 1–2 word label. Matches semantic color. Transparent background.
5. **Dismiss button** — Optional. `×` icon. Omit on error/critical banners.
6. **Color/icon semantic encoding** — Required for both. Info=blue, Success=green, Warning=amber, Error=red, Premium=gradient green.

## Variants

Each variant maps to a semantic intent. Color and icon always appear together.

### Informational

Use for system notices, reminders, and expiry dates. Not urgent — player can act at their own pace.

### Success

Use to confirm completed actions, pass activation, download completion. Dismissible.

### Warning

Use for connection issues, low storage, approaching expiry. Action usually provided.

### Error

Use for failed actions requiring resolution. No dismiss button — error persists until resolved.

### Pass / Premium

Use for JioGames Pass activation confirmations and upsell confirmation messages.

## Sizes

Three size tiers. Compact for tight contexts; Standard for most surfaces; Rich for action-heavy moments (rare).

### Compact (~44px)

Icon + text only, no action. Use in dense contexts where vertical space is critical.

### Standard (~52px)

Icon + text + action button + dismiss. The default for almost all surfaces.

### Rich (~80px)

Icon + title + subtitle + image thumbnail + action. Reserve for high-value moments — Pass upsell, game launch confirmations.

| Size | Mobile | Web | TV |
|---|---|---|---|
| Compact | Icon + text only · ~44px | Icon + text only · ~44px | Text enlarged 15px · ~48px |
| Standard | Icon + text + action + dismiss · ~52px | Icon + text + action + dismiss · ~52px | No dismiss btn · ~56px · d-pad to dismiss |
| Rich | Icon + title + sub + thumb + action · ~80px | Wider layout · richer action buttons · ~80px | Rare on TV — use full-screen overlay instead |

## States

### Visible (default)

### Dismiss animation

When dismissed, the banner slides up and fades out simultaneously over 200ms, then is removed from the DOM. Use `transition: opacity 200ms ease, transform 200ms ease` with `opacity: 0; transform: translateY(-8px)` on the exiting state.

### Loading (async)

Use when banner content is fetched asynchronously. Shimmer skeleton fills the icon, message, and action slot.

## Content

- Keep under 80 characters
- Present tense for ongoing conditions: "Your pass expires in 3 days"
- Past tense for completed actions: "Game added to library"
- Imperative for errors: "Check your connection"
- No punctuation at end unless it's a question
- Sentence case, not title case

- Max 2 words — verb + noun: "View Plan", "Retry", "Manage"
- Never "Click here" or "Learn more" in a banner
- Action should be directly related to the banner message
- Use "Retry" not "Try Again" — brevity aids scan speed
- Primary action only — secondary action belongs in a sheet
- Capitalize first word only (sentence case)

## Platform Considerations

- Full-width; top of screen below status bar
- Stays fixed above scrollable content — does not scroll away
- `border-radius: 0` if the banner bleeds edge-to-edge
- Max 1 banner visible at a time
- Dismiss button for info/success; no dismiss for error
- Touch target on dismiss: minimum 44×44px

- Max-width container; `border-radius: 12px`
- Richer action buttons (outlined style allowed)
- Can use inline hyperlink style for action when appropriate
- Banner sticks to top of content region, not browser viewport
- On wide screens, constrain max-width to 780px
- Hover state on dismiss: lighten to `--text2`

- Full-width; larger message text: `font-size: 15px`
- No dismiss button — d-pad to dismiss, or auto-dismiss when condition resolves
- Action button must be focus-navigable via d-pad
- Focused action button: solid fill matching semantic color, dark text
- Ensure 3:1 contrast on focus ring against banner background
- Error banners should also expose a voice/remote-friendly action

## Accessibility

| Attribute | Value | When to use |
|---|---|---|
| `role` | `"alert"` | Error and warning banners — announces immediately to screen readers |
| `role` | `"status"` | Info and success banners — less urgent, waits for a pause |
| `aria-live` | `"assertive"` | Error banners — interrupts current announcement |
| `aria-live` | `"polite"` | Info/success banners — waits for idle before announcing |
| `aria-label` | `"Dismiss"` | Dismiss × button — the × glyph has no semantic meaning on its own |
| `aria-hidden` | `"true"` | Status icon SVG — text already conveys meaning; icon is decorative |
| `aria-busy` | `"true"` | Loading skeleton banner — indicates content has not yet loaded |

- **Focus management.** When a banner is injected via JavaScript, move focus to the banner element or announce it via an `aria-live` region. Don't leave focus stranded.
- **Color contrast.** Ensure message text meets WCAG AA (4.5:1 against banner background). All semantic colors in the DLS are pre-validated.
- **Reduced motion.** Honour `prefers-reduced-motion` — skip the `translateY` on dismiss, keep opacity transition only.

## Related Tokens

## When to use

Use when

- System-level messages affecting the whole screen (maintenance, offline, subscription)
- Dismissible promotional messages at the top of a screen
- Pass activation confirmations after login
- Non-blocking warnings that require no immediate action

Don't use when

- Transient feedback (success/error after an action) — use Toast instead
- Destructive confirmations — use a Dialog
- More than one banner at a time — stack creates visual noise
- Marketing messages inside content areas — use a Card instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Slide in (top) | `--ease-out` | `--dur-base` | transform translateY(-100% → 0) |
| Slide out (top) | `--ease-in` | `--dur-fast` | transform translateY(0 → -100%) |
| Fade in | `--ease-out` | `--dur-base` | opacity |
| Dismiss | `--ease-in` | `--dur-fast` | opacity, max-height |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-banner` | Root banner — full width, top of screen |
| `.ds-banner--info` | Informational — blue accent |
| `.ds-banner--success` | Success — green accent |
| `.ds-banner--warning` | Warning — amber accent |
| `.ds-banner--error` | Error — red accent |
| `.ds-banner--pass` | JioGames Pass promotion — green gradient |
| `.ds-banner__dismiss` | Close button — top-right |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | "info" | "success" | "warning" | "error" | "pass" | "info" | Semantic color variant |
| `dismissible` | boolean | true | Show close button |
| `onDismiss` | () => void | undefined | Fired when banner is closed |
| `icon` | ReactNode | undefined | Leading icon override |
| `action` | { label: string; onClick: () => void } | undefined | Optional CTA link |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="banner banner--info" role="status">
  <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_info"></use></svg>
  <div class="banner__body">
    <div class="banner__title">Your pass renews on 15 July</div>
    <div class="banner__desc">Auto-renewal is enabled. Manage in settings.</div>
  </div>
  <button class="btn btn--text btn--xs btn--hug banner__dismiss" aria-label="Dismiss">✕</button>
</div>
````

````html
<div class="banner banner--error" role="alert">
  <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_warning"></use></svg>
  <div class="banner__body">
    <div class="banner__title">Payment failed</div>
    <div class="banner__desc">Update your payment method to continue your pass.</div>
  </div>
  <button class="btn btn--primary btn--xs btn--hug">Update</button>
</div>
````

## Changelog

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--border-subtle`
- `--info`
- `--jio`
- `--negative`
- `--pill`
- `--surface-1`
- `--surface-2`
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

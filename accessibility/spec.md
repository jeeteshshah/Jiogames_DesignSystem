# Accessibility — JioGames DLS spec

> Source: `accessibility/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Accessibility

---

JioGames targets WCAG 2.1 AA minimum across all platforms. TV also follows WCAG 2.1 AA plus remote-control navigation requirements.

WCAG 2.1 AA · CONTRAST · FOCUS · REDUCED MOTION

## WCAG 2.1 Compliance Matrix

Current audit status. All AA criteria must pass before shipping a new platform surface.

| Criterion | Level | Status | JioGames implementation |
|---|---|---|---|
| 1.4.3 Contrast (Text) | AA | ✓ Pass | --text on --bg = 13.5:1 |
| 1.4.11 Non-text Contrast | AA | ✓ Pass | --border on --bg = 3.1:1 |
| 2.1.1 Keyboard | AA | ✓ Pass | All interactive elements keyboard navigable |
| 2.1.2 No Keyboard Trap | AA | ✓ Pass | Modals use focus trap with Escape key |
| 2.4.3 Focus Order | AA | ✓ Pass | DOM order = visual order |
| 2.4.7 Focus Visible | AA | ✓ Pass | All elements have visible focus ring |
| 4.1.2 Name/Role/Value | AA | ✓ Pass | ARIA labels on all icon-only controls |

## Contrast Demos

Three key text pairings. Only use `--text3` for decorative or non-critical labels (metadata, timestamps). Never use `--text4` for visible text.

## Focus Visible

Three focus tiers: default (no focus), web focused (2px ring), TV focused (glow + scale). Never use `outline:none` without a custom replacement.

## ARIA Patterns

Required ARIA for each interactive pattern in the system. Copy these exactly — screen reader announcements depend on the right combination of role + attribute.

## Touch Target Sizes

Visual size and interactive target size are different. Expand touch targets with padding or invisible wrapper — never shrink them to match visual size.

## Motion & Vestibular

Under `prefers-reduced-motion: reduce`, all decorative transitions are zeroed. Only purposeful transitions (sheet open, focus ring) may persist — and only if they help spatial orientation.

````
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  /* Exception: sheet transition kept for spatial cue */
  .bottom-sheet {
    transition-duration: 100ms !important;
  }
}
````

## Screen Reader Checklist

Run through this before every release. Test with VoiceOver (iOS / macOS) and TalkBack (Android).

- All images have alt text, or `alt=""` + `aria-hidden="true"` if purely decorative.
- Form inputs have associated `` — not just `placeholder`.
- Error messages are programmatically linked to their input via `aria-describedby`.
- Modals announce their title on open via `aria-labelledby`.
- Dynamic content (toasts, pass states) uses `aria-live` regions.
- Page title updates on route change — screen reader announces the new screen.
- Focus is restored to the trigger element when a modal or sheet closes.

## TV-Specific Accessibility

TV has no pointer, no hover, and a mandatory 3m viewing distance. These requirements are in addition to WCAG 2.1 AA.

## Tokens

| Token | Value | Use |
|---|---|---|
| --focus-ring-color | var(--jio) | Web/mobile focus ring |
| --focus-ring-width | 2px | Web focus ring thickness |
| --focus-ring-offset | 3px | Gap between element and ring |
| --focus-shadow | 0 0 0 var(--focus-ring-width) var(--focus-ring-color) | Web focus shadow shorthand |
| --tv-focus-shadow | 0 0 0 3px var(--jio), 0 0 24px var(--jio-glow), 0 0 48px … | TV composite focus ring |
| --state-disabled-opacity | 0.32 | Disabled element opacity |
| --text (contrast) | 13.5:1 on --bg | Primary text — AAA |
| --text2 (contrast) | 5.2:1 on --surface-1 | Secondary text — AA |
| --jio (contrast) | 4.6:1 on --bg | Brand green — AA large text |

## Focus Management

Focus rings are defined by three tokens. Never remove the outline without supplying a token-based replacement.

### Focus ring tokens

| Token | Value | Role |
|---|---|---|
| --focus-ring-color | var(--jio) | Ring colour — matches brand green |
| --focus-ring-width | 2px | Ring stroke thickness |
| --focus-ring-offset | 3px | Gap between element edge and ring |

### .is-focused demo

### Rules

- Never write `outline:none` or `outline:0` without providing a token-based replacement using `--focus-ring-color`.
- Provide a skip-nav link as the first focusable element on every web page: `[Skip to content](#main)`.
- Trap focus inside modals and bottom sheets while they are open — Tab and Shift+Tab must cycle within the modal only. Restore focus to the trigger element on close.
- Relying on browser default outlines — they vary across OS/browser combinations and may not meet contrast requirements.

## Colour & Contrast

WCAG AA requires 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt bold) and UI components. Key token pairs below.

### Token contrast table

| Foreground token | Background token | Ratio | Result | Note |
|---|---|---|---|---|
| --text | --bg | 13.5:1 | ✓ AAA | Primary body copy — passes all levels |
| --text2 | --bg | 5.4:1 | ✓ AA | Secondary text on dark bg — passes AA |
| --text2 | --surface-1 | ~4.6:1 | ⚠ Marginal | Passes AA but verify per surface — avoid for small text below 14px |
| --text3 | --bg | 3.8:1 | ✗ Fail (small) | Use only for metadata / decorative labels at 14px+ bold or 18px+ |
| --jio | --bg | 4.6:1 | ✓ AA (large) | Brand green — use for large text / UI indicators only |

### Colour alone is not enough

- Always pair a colour-coded status with an icon or label: success = green + ✓, error = red + ✗, warning = amber + ⚠.
- Disabled states must use both reduced opacity (`--state-disabled-opacity`) and a non-colour cue (e.g. `aria-disabled` or greyed icon).
- Using colour as the sole indicator for required fields, validation errors, or subscription tiers.

## Touch Targets

Touch target minimum is `var(--touch-min)` (44px). On TV, minimum is `var(--icon-wrap-xs-tv)` (52px) due to 10-foot viewing and remote precision. Visual size and interactive target size may differ — expand with padding.

### Target size demo

````
/* Correct: wrap bare icon in .icon-wrap--m */
<button class="btn btn--icon btn--icon-circle" aria-label="Add to wishlist">
  <svg aria-hidden="true" width="20" height="20">…</svg>
</button>

/* Wrong: interactive icon without wrapper */
<svg onclick="…" width="20" height="20">…</svg>
````

## Screen Reader Patterns

Copy these exact patterns. Screen reader announcements depend on the right combination of role, aria attributes, and DOM structure.

### Icon-only button

````html
<button class="btn btn--icon btn--icon-circle"
        aria-label="Add War Thunder to wishlist">
  <svg aria-hidden="true" focusable="false" width="20" height="20">…</svg>
</button>
````

### Decorative icon (hidden from SR)

````
<!-- role="img" on meaningful standalone graphics; aria-hidden on decorative -->
<svg role="img" aria-label="JioGames logo" width="40" height="40">…</svg>

<svg aria-hidden="true" focusable="false" width="16" height="16">…</svg>
````

### Live regions — toast & banner

````
<!-- Toast: polite -->
<div role="status" aria-live="polite" aria-atomic="true" class="toast">
  Pass activated successfully
</div>

<!-- Error: assertive -->
<div role="alert" aria-live="assertive" aria-atomic="true">
  Incorrect OTP. 2 attempts remaining.
</div>
````

## TV / D-pad Accessibility

TV has no pointer and no hover. Every interaction must be reachable via D-pad (Up/Down/Left/Right/OK/Back). Requirements are additive to WCAG 2.1 AA.

### Requirements

- All interactive elements must be focusable — set `tabindex="0"` on non-native focusable elements.
- `.is-tv-focused` must be visibly applied using `var(--tv-focus-shadow)` — the glow must be visible at 3m distance.
- Focus order must follow visual order — match DOM order to visual layout exactly.
- No pointer-only interactions — no hover-only tooltips, no hover-only reveal buttons.
- `var(--tv-focus-shadow)` must always be fully visible — never clip it with `overflow:hidden` on a parent.
- Back button (Backspace / Escape) must always dismiss modals and sheets — never trap focus without an exit.
- Using CSS `:hover` as the only trigger for revealing actions (e.g. card overlay buttons).
- Clipping `overflow:hidden` on a rail container that cuts off the TV focus glow.

### TV focus token

| Token | Value | Use |
|---|---|---|
| --tv-focus-shadow | 0 0 0 3px var(--jio), 0 0 24px var(--jio-glow), 0 0 48px var(--jio-glow) | Composite ring + glow for TV |

## Reduced Motion

Users with vestibular disorders may enable `prefers-reduced-motion: reduce`. Under this preference all decorative keyframe animations must be suppressed. `var(--dur-fast)` resolves to near-zero (0.01ms) so transitions do not play.

### Pattern

````
/* Global suppression in tokens.css */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }

  /* Exception: sheet slide-in kept as spatial orientation cue */
  .bottom-sheet { transition-duration: 100ms !important; }
}

/* Per-component guard (preferred for explicit control) */
@media (prefers-reduced-motion: no-preference) {
  .skeleton-shimmer {
    animation: shimmer var(--dur-skeleton) linear infinite;
  }
}
````

### Token behaviour

| Token | Default value | Reduced motion value |
|---|---|---|
| --dur-fast | 120ms | 0.01ms (via media query override) |
| --dur-normal | 220ms | 0.01ms |
| --dur-slow | 400ms | 0.01ms |

## Rules

- Test with VoiceOver (iOS/macOS) and TalkBack (Android) before shipping.
- Minimum 4.5:1 contrast for normal body text; 3:1 for large text and UI components.
- Never rely on colour alone to convey state — pair with icon, text, or shape.
- All keyboard-interactive elements must show a visible focus ring on `:focus-visible`.
- Respect `prefers-reduced-motion` — all non-purposeful animations must be gated.
- Using `--text3` (#6B7280) for body copy — only passes at large sizes (3.8:1).
- Using `--text4` (#454A57) for any visible text — fails all WCAG levels (2.1:1).
- Using `outline:none` without a replacement focus indicator.
- Hover-only tooltips or actions on TV — no hover means no access.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--dur-fast`
- `--dur-skeleton`
- `--error-text`
- `--focus-ring-color`
- `--focus-ring-offset`
- `--focus-ring-width`
- `--icon-wrap-xs-tv`
- `--jio`
- `--jio-glow`
- `--jio-soft`
- `--pill`
- `--popular-gold`
- `--r2`
- `--r3`
- `--r4`
- `--success-text`
- `--surface-1`
- `--surface-2`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`
- `--touch-min`
- `--tv-focus-shadow`
- `--warning-text`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# Buttons — JioGames DLS spec

> Source: `buttons/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Buttons

---

A button initiates an immediate action.

Buttons give players a clear, familiar way to take action across JioGames. A button combines hierarchy, size, state, and content to communicate what will happen next — from playing a game to unlocking a pass.

- **Hierarchy.** Seven variants from Primary to Destructive establish visual priority. Only one Primary button per section.
- **Size.** Five canonical sizes — XS through XL — each resolving to different pixel values on Mobile, Web, and TV.
- **State.** Every button handles hover, pressed, focus, disabled, loading, success, error, and TV focus.
- **Platform.** Size class stays constant. Platform context (mobile touch, web pointer, TV remote) resolves the token alias.

## When to use

Buttons are for actions. If you're navigating, use a link. If you're selecting from a set of options, use a chip or toggle.

- The user needs to trigger an action: Play, Download, Subscribe, Continue
- Submitting a form or confirming a destructive action
- The primary CTA on a screen needs maximum visual weight
- An asynchronous action needs a loading + feedback state
- The action is immediate and reversible (or explicitly irreversible)

- You're navigating to another page — use a link or nav element instead
- You need binary on/off — use a Toggle
- You're selecting one from a set of options — use Chips or a Radio group
- The action is purely decorative or informational — remove the button
- You need more than 3 CTAs in a single view — consolidate hierarchy first

## Best practices

Follow these rules to keep button usage consistent across the JioGames product surface.

- Use one Primary button per section or screen region
- Use clear action verbs: Play, Start, Continue, Unlock, Try again
- Keep the Primary CTA anchored at the bottom on mobile
- Use icon + label when the icon meaningfully reinforces the action
- Maintain stable button width during loading state
- Use Destructive only for truly irreversible actions
- On TV, use L or XL size — never XS or S

- Don't use multiple Primary buttons in the same view
- Don't use vague labels like "Submit" or "OK" when action can be clearer
- Don't use icon-only buttons without an accessible aria-label
- Don't rely on color alone to signal destructive actions
- Don't place tiny XS/S buttons as the main TV CTA
- Don't change button width between default and loading states
- Don't use `.btn--tv` — use `.btn--l` inside `.platform-tv`

## Anatomy

Every button is composed of the same four slots. The Container is the only required element — all other slots are optional but must be used intentionally.

## Variants

Seven variants cover every interaction tier. Use the lowest-weight variant that still communicates the action's importance. Never place two Primary buttons in the same view.

## Sizes

Five canonical size names describe visual hierarchy. Platform context determines actual pixel values via CSS token aliases. The same class produces different sizes on Mobile, Web, and TV.

## States

Every button variant responds to the same six interaction states. Use the `.is-*` helper classes from `states.css` to simulate states in documentation or prototypes.

## Icon usage

Icons reinforce meaning and aid scannability. Use the icon slot intentionally — never add decoration for its own sake. Icon-only buttons always need an accessible label.

## Loading behavior

The loading state communicates that an action has been received and is processing. It prevents re-submission and removes the label visually while keeping layout stable.

- ·Keep `width` stable — set fixed or `min-width`
- ·Spinner auto-injected via `::after` — no extra HTML
- ·Label text goes transparent, stays in DOM for layout
- ·Add `aria-busy="true"` on the button element
- ·Transition to `.is-success` or `.is-error` after

- ·Don't change the label text to "Loading…"
- ·Don't allow width to collapse — causes layout shift
- ·Don't add a separate spinner element in the HTML
- ·Don't leave the button loading indefinitely
- ·Don't use loading on `.btn--text` buttons

## Content

Button labels are the most direct communication between the product and the player. Every word carries weight.

- Use action verbs: Play, Start, Continue, Unlock, Try again
- Keep to 1–3 words where possible
- Avoid "Submit", "OK", "Yes" without clear context
- Icon + label: icon should reinforce, not replace, the label
- Match the verb to the outcome: "Play" not "Launch"

- Do not change the label text during loading
- Maintain button width — add `min-width` if needed
- Spinner appears automatically via CSS `::after`
- Success state: show confirmation, then return to default
- Error state: show feedback and allow retry

- Name the consequence: "Delete save file", not "Delete"
- Confirm before triggering — use a dialog
- Never use Destructive as the primary CTA
- Always pair with a cancel option

- Always require `aria-label` on the button element
- Use a tooltip to surface the label on hover
- Minimum 44px touch target on mobile
- Prefer icon + label if there's sufficient space

## Platform considerations

Each platform has a different interaction model. The same button classes adapt their token values — but usage patterns also differ fundamentally.

- 44px minimum touch target — use M or L
- Full-width Primary CTA at bottom of screen
- Avoid XS/S as primary action targets
- Bottom sheet CTAs use full-width Primary
- Loading keeps stable width to avoid layout shift
- Tap highlight suppressed via `-webkit-tap-highlight-color`

- Hover state via `:hover` pseudo-class
- Keyboard focus via `:focus-visible`
- Hug-content width for most actions
- Dense layouts can use S size
- Full-width only inside cards or modal footers
- Cursor: pointer on all button elements

- Remote d-pad navigation — no hover
- L or XL size only — never XS/S on TV
- TV focus: scale(1.05) + `var(--tv-focus-shadow)`
- 10-foot readability — min 16px font at TV sizes
- Use `.is-tv-focused` in prototypes
- Never use `.btn--tv` — deprecated

## Motion

Button transitions are fast and confirmatory. They acknowledge input immediately without drawing attention away from the action's outcome.

| Interaction | Property | Duration | Easing | Notes |
|---|---|---|---|---|
| Press / tap | `transform: scale(0.96–0.97)` | `--dur-fast` (120ms) | `--spring` | Scales down on press, springs back on release |
| Hover (web) | `background-color` | `--dur-fast` (120ms) | `--spring` | Subtle fill shift. No scale on hover. |
| Focus ring appear | `box-shadow` | `--dur-instant` (90ms) | `--ease-out` | Focus ring must never be delayed or suppressed |
| Loading state enter | `opacity` | `--dur-default` (200ms) | `--ease-out` | Spinner fades in; label fades out. Width stays fixed. |
| Disabled state | `opacity` | instant | none | No animation on disable — it's a state, not a transition |
| TV focus (D-pad) | `box-shadow, transform` | `--dur-fast` (120ms) | `--spring` | Glow ring + `scale(1.05)` on focus. No press scale on TV. |

Reduced motion: all transitions collapse via `@media (prefers-reduced-motion: reduce)`. Duration tokens handle this automatically — never hardcode `ms` values in button CSS. Never use `transition: all` — list explicit properties only.

## Platform rules

Mobile

- Minimum touch target 44×44px — use var(--ctrl-h) 48px default height
- Full-width CTAs in sheets and bottom panels (width:100%)
- Avoid more than 2 buttons stacked vertically — use bottom-sheet actions
- Loading state shows spinner inside button — do not disable without feedback

Web

- Hover state required — scale(1.02) or bg shift on primary/secondary
- Focus ring via :focus-visible — 2px jio-green outline, 2px offset
- Icon-only buttons must have tooltip or aria-label
- Min width 120px to avoid very narrow pill buttons

TV

- Height uses var(--ctrl-h-tv) — taller for D-pad navigation comfort
- Focus ring uses jio-glow box-shadow — visible at 10-foot distance
- Only Primary and Ghost variants used on TV — avoid subtle differences
- Pressed state on OK button: scale(0.95) flash then return

## Accessibility

Buttons are interactive controls. Every button must be operable with keyboard, screen reader, and pointer input.

- Tab — moves focus to the next interactive element
- Enter or Space — activates the button
- Escape — dismisses dialogs triggered by the button
- Focus ring visible on `:focus-visible`, not `:focus`

- Primary: black text on `#00A859` — 5.1:1 contrast ratio
- Secondary / Ghost: white text on dark bg — meets 4.5:1
- Destructive: `var(--negative)` red — ensure 4.5:1 on any bg
- Disabled: 0.32 opacity — decorative, not required to meet contrast

- Icon-only: always add `aria-label="[action]"` to the button element
- Add `aria-hidden="true"` to all decorative SVG icons
- Loading: add `aria-busy="true"` to the button while loading
- Disabled: use native `disabled` attribute, not CSS opacity alone
- Success/error: use `aria-live="polite"` region for feedback announcements

## Related tokens

All button values are defined in `tokens/tokens.css`. Change a token once and all button instances update automatically.

| Token | Value | Swatch | Usage |
|---|---|---|---|
| `--btn-primary-bg` | `var(--jio)` → #00A859 |   | Primary button background |
| `--btn-primary-text` | `var(--text-inv)` → #000000 |   | Primary button label color |
| `--btn-primary-hover-bg` | #00be65 |   | Primary hover state background |
| `--btn-secondary-border` | `var(--border-strong)` |   | Secondary border color |
| `--btn-ghost-border` | `var(--border)` |   | Ghost button border |
| `--btn-destructive-bg` | rgba(255,71,87,.12) |   | Destructive fill |
| `--btn-destructive-text` | `var(--negative)` → #FF4757 |   | Destructive label color |
| `--btn-ultimate-bg` | linear-gradient(135deg, #00cc65, #00E870) |   | Ultimate pass gradient |
| `--btn-disabled-opacity` | 0.32 | — | Disabled state opacity |

| Token | Mobile | Web | TV | Property |
|---|---|---|---|---|
| `--btn-xs-h` | 28px | 30px | 48px | height |
| `--btn-s-h` | 36px | 38px | 56px | height |
| `--btn-m-h` | 44px | 44px | 64px | height |
| `--btn-l-h` | 54px | 54px | 72px | height |
| `--btn-xl-h` | 64px | 64px | 80px | height |
| `--btn-xs-px` | 10px | 12px | 20px | padding-inline |
| `--btn-s-px` | 16px | 18px | 28px | padding-inline |
| `--btn-m-px` | 20px | 22px | 36px | padding-inline |
| `--btn-l-px` | 24px | 28px | 44px | padding-inline |
| `--btn-xl-px` | 32px | 36px | 56px | padding-inline |
| `--btn-xs-fs` | 11px | 12px | 14px | font-size |
| `--btn-s-fs` | 13px | 13px | 16px | font-size |
| `--btn-m-fs` | 14px | 14px | 18px | font-size |
| `--btn-l-fs` | 15px | 16px | 20px | font-size |
| `--btn-xl-fs` | 17px | 18px | 22px | font-size |

| Token | Value | Usage |
|---|---|---|
| `--focus-ring-color` | `var(--jio)` → #00A859 | Focus outline color |
| `--focus-ring-width` | 2px (mobile/web) · 3px (TV) | Focus ring stroke |
| `--focus-ring-offset` | 3px (mobile/web) · 4px (TV) | Outline offset from edge |
| `--state-pressed-scale` | 0.97 | Scale transform on :active |
| `--state-disabled-opacity` | 0.32 | Disabled state opacity |
| `--tv-focus-shadow` | 0 0 0 3px var(--jio), 0 0 24px var(--jio-glow), 0 0 48px rgba(0,200,100,.2) | TV d-pad glow |
| `--tv-focus-scale` | 1.05 | TV focus scale transform |
| `--spinner-size-md` | 20px | Default spinner diameter |
| `--spinner-stroke` | 2px | Spinner border width |

## CSS class / React API

All classes this component exposes. Use these — never write one-off overrides in screen CSS.

| Class | Description |
|---|---|
| `.btn` | Base element. Required on every button.Sets display, font, border-radius (pill), transition, cursor. |
| `.btn--primary` | Highest-weight CTA. Green fill, dark label.One per screen section. Use for Play Now, Subscribe, Continue. |
| `.btn--secondary` | Bordered, transparent fill.Second action alongside Primary. Use for Add to Library, Save. |
| `.btn--ghost` | Subtle glass fill, muted border.Tertiary or inline actions. Use for Skip, Cancel, Share. |
| `.btn--text` | No background or border. Green text.Lowest emphasis. Use for Learn more, View all. |
| `.btn--destructive` | Red tint. Signals irreversible actions.Use only for Delete, Remove, Unsubscribe. |
| `.btn--ultimate` | Gradient green. Premium upsell only.Reserve for Ultimate Pass CTAs. |
| `.btn--xs / --s / --m / --l / --xl` | Size modifiers. Platform-aware via token aliases.L (54px mobile) is the default CTA size. |
| `.btn--hug` | Width hugs content. No min-width.Default. Omit for full-width buttons. |
| `.btn--full` | width: 100%. Fills container.Use for primary CTAs pinned to bottom of mobile screens. |
| `.btn--icon-only` | Square aspect ratio. No label.Requires aria-label on the element. |
| `.is-loading` | Loading state. Shows spinner, hides label.Keep element width stable. Prevents re-submission. |
| `.is-disabled` | Disabled state. opacity: 0.32, no pointer events.Also set disabled attribute on <button> elements. |
| `.is-focused` | Force-show focus ring. For demos only.Never use in production — real focus handled by :focus-visible. |

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | 'primary' | 'secondary' | 'ghost' | 'text' | 'destructive' | 'ultimate' | 'primary' | Visual variant. Maps to .btn--* modifier. |
| `size` | 'xs' | 's' | 'm' | 'l' | 'xl' | 'l' | Size hierarchy name. Resolves to platform-aware px via tokens. |
| `fullWidth` | boolean | false | Applies .btn--full. Use for pinned mobile CTAs. |
| `iconOnly` | boolean | false | Square ratio. aria-label required when true. |
| `loading` | boolean | false | Shows spinner, prevents re-submission, stable width. |
| `disabled` | boolean | false | Sets disabled attr + .is-disabled class + aria-disabled. |
| `asChild` | boolean | false | Render as child element — use to wrap <a> or <Link>. |
| `leadingIcon` | ReactNode | undefined | Icon before label. Pass sprite use or SVG. |
| `trailingIcon` | ReactNode | undefined | Icon after label. |

## Code examples

Copy-pasteable patterns for every common button use case.

````html
<button class="btn btn--primary btn--l btn--hug">
  Play Now
</button>

<!-- Full-width (mobile bottom CTA) -->
<button class="btn btn--primary btn--l btn--full">
  Play Now
</button>
````

````html
<button class="btn btn--secondary btn--l btn--hug">Add to Library</button>
<button class="btn btn--ghost btn--l btn--hug">Skip for now</button>
````

````html
<button class="btn btn--primary btn--l btn--hug">
  <svg viewBox="0 0 24 24" class="icon icon--s" aria-hidden="true">
    <use href="../sprite.svg#ic_play"></use>
  </svg>
  Play Game
</button>
````

````
<!-- Add .is-loading via JS when action fires -->
<button
  class="btn btn--primary btn--l btn--hug is-loading"
  aria-busy="true"
  style="min-width:140px"
>
  Play Now
</button>
````

````
<!-- .platform-tv resolves all --btn-*-h tokens to TV values -->
<div class="platform-tv">
  <button class="btn btn--primary btn--l btn--hug">
    Play Now
  </button>
</div>

<!-- Simulate TV focus in prototypes -->
<button class="btn btn--primary btn--l btn--hug is-tv-focused">
  Play Now
</button>
````

````
<!-- Transparent bg, 44px touch target -->
<button class="btn btn--icon" aria-label="Play game">
  <svg viewBox="0 0 24 24" class="icon icon--m" aria-hidden="true">
    <use href="../sprite.svg#ic_play"></use>
  </svg>
</button>

<!-- Glass bg with border -->
<button class="btn btn--icon-circle" aria-label="Share">
  <svg viewBox="0 0 24 24" class="icon icon--s" aria-hidden="true">
    <use href="../sprite.svg#ic_share"></use>
  </svg>
</button>
````

````
<!-- Always pair with a cancel action -->
<div style="display:flex;gap:12px">
  <button class="btn btn--ghost btn--l btn--hug">
    Cancel
  </button>
  <button class="btn btn--destructive btn--l btn--hug">
    Delete save file
  </button>
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
- `--btn-l-fs-mobile`
- `--btn-l-fs-tv`
- `--btn-l-fs-web`
- `--btn-l-h`
- `--btn-l-h-mobile`
- `--btn-l-h-tv`
- `--btn-l-h-web`
- `--btn-l-px-mobile`
- `--btn-l-px-tv`
- `--btn-l-px-web`
- `--btn-m-fs-mobile`
- `--btn-m-fs-tv`
- `--btn-m-fs-web`
- `--btn-m-h-mobile`
- `--btn-m-h-tv`
- `--btn-m-h-web`
- `--btn-m-px-mobile`
- `--btn-m-px-tv`
- `--btn-m-px-web`
- `--btn-s-fs-mobile`
- `--btn-s-fs-tv`
- `--btn-s-fs-web`
- `--btn-s-h-mobile`
- `--btn-s-h-tv`
- `--btn-s-h-web`
- `--btn-s-px-mobile`
- `--btn-s-px-tv`
- `--btn-s-px-web`
- `--btn-xl-fs-mobile`
- `--btn-xl-fs-tv`
- `--btn-xl-fs-web`
- `--btn-xl-h-mobile`
- `--btn-xl-h-tv`
- `--btn-xl-h-web`
- `--btn-xl-px-mobile`
- `--btn-xl-px-tv`
- `--btn-xl-px-web`
- `--btn-xs-fs-mobile`
- `--btn-xs-fs-tv`
- `--btn-xs-fs-web`
- `--btn-xs-h-mobile`
- `--btn-xs-h-tv`
- `--btn-xs-h-web`
- `--btn-xs-px-mobile`
- `--btn-xs-px-tv`
- `--btn-xs-px-web`
- `--ctrl-h`
- `--ctrl-h-ghost`
- `--ctrl-h-tv`
- `--focus-ring-color`
- `--glass-1`
- `--gold`
- `--jio`
- `--jio-3`
- `--jio-font`
- `--jio-glow`
- `--negative`
- `--pill`
- `--r4`
- `--state-hover-bg`
- `--state-hover-border`
- `--status-positive`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`
- `--text4`
- `--tv-focus-shadow`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

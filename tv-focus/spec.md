# TV Focus — JioGames DLS spec

> Source: `tv-focus/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › TV Focus

---

JioGames TV uses a D-pad + OK model. No hover. All interaction via directional focus. The focus ring is the primary affordance — it must be unmissable at 3m viewing distance.

3PX GREEN RING · GLOW · 1.05× SCALE · D-PAD NAVIGATION

## The Focus Ring

Three element types — button, card, custom tile — all receive the same unmissable TV focus treatment: a 3px green ring, layered glow, and a 1.05× scale lift.

## Focus Anatomy

The TV focus ring is a composite of three shadow layers plus a scale transform. Each layer serves a distinct visual purpose.

| Layer | CSS | Token | Purpose |
|---|---|---|---|
| **Focus ring** | 0 0 0 3px var(--jio) | --tv-focus-ring-color | Solid green border — primary identity signal |
| **Inner glow** | 0 0 24px var(--jio-glow) | --jio-glow | Soft radiance — depth and warmth at distance |
| **Outer ambient** | 0 0 48px rgba(0,200,100,.2) | --tv-focus-shadow | Atmospheric bloom — visible at 3m |
| **Scale** | transform: scale(1.05) | --tv-focus-scale | Physical lift — confirms selection spatially |

## Web Focus vs TV Focus

Web focus is subtle — 2px ring, no scale, no glow. TV focus is theatrical — designed to be readable from a couch at 3 metres.

## Focus Order Rules

Focus must follow a predictable spatial model. Users learn the grid — any deviation breaks their mental map.

1. **Left → Right, Top → Bottom** — natural reading order within each row.
2. **Wrap to next row** — pressing Right at end of rail moves focus to the first card of the next rail.
3. **Modal traps focus** — once a sheet or dialog opens, focus must stay inside until dismissed.
4. **Back button exits modal** — always. Never leave the user stranded.
5. **No orphan focus** — every state must have at least one focusable element; never render a UI with no focusable target.
6. **All interactive elements must be focusable** — custom divs acting as buttons need `tabindex="0"` and keyboard handlers.

## Rail Navigation Pattern

The standard TV layout is horizontal card rails. Focus moves Left/Right within a rail; Up/Down switches rails. The focused card pops with glow + scale.

## Applying TV Focus

Add the focus shadow and scale to any custom element using `:focus-visible` or the `.is-tv-focused` class. Wire D-pad keys in JS.

````
/* CSS — apply to any focusable TV element */
.my-card:focus-visible,
.my-card.is-tv-focused {
  outline: none;
  box-shadow: var(--tv-focus-shadow);
  transform: scale(var(--tv-focus-scale));
  transition: box-shadow var(--dur-base) var(--ease-out),
              transform var(--dur-base) var(--spring);
}
````

````
/* JS — D-pad navigation handler */
element.addEventListener('keydown', e => {
  if (e.key === 'Enter' || e.key === ' ') activate();
  if (e.key === 'ArrowRight') focusNext();
  if (e.key === 'ArrowLeft')  focusPrev();
  if (e.key === 'ArrowDown')  focusNextRow();
  if (e.key === 'ArrowUp')    focusPrevRow();
});
````

## Reduced Motion

TV focus animation must respect `prefers-reduced-motion`. Users with vestibular conditions must never see unexpected scale or glow animation. The ring itself (box-shadow) can remain — only the transition is disabled.

````
@media (prefers-reduced-motion: reduce) {
  .card, .btn, [class*="is-tv-focused"] {
    transition: none;
    transform: none;
  }

  /* Focus ring stays (it's a static outline), but scale is removed */
  .card.is-tv-focused,
  .btn.is-tv-focused {
    box-shadow: var(--tv-focus-shadow);
    transform: none; /* no scale under reduced motion */
  }
}
````

## Tokens

| Token | Value | Use |
|---|---|---|
| --tv-focus-ring-color | var(--jio) | Ring colour (green) |
| --tv-focus-shadow | 0 0 0 3px var(--jio), 0 0 24px var(--jio-glow), 0 0 48px rgba(0,200,100,.2) | Full composite shadow |
| --tv-focus-scale | 1.05 | Scale-up transform |
| --focus-ring-color | var(--jio) | Web/mobile focus ring colour |
| --focus-ring-width | 2px | Web focus ring thickness |
| --dur-base | 200ms | Focus transition duration |
| --ease-out | cubic-bezier(0.2,0,0,1) | Focus easing |

## Rules

- Always use `:focus-visible`, never `:focus` — avoids spurious rings on mouse click.
- Focus ring must be visible on all backgrounds — test on the darkest surface (`--bg`) and lightest overlay.
- Scale + glow must animate using `--spring` easing — the physics sell the physicality at distance.
- Every focusable element must have `tabindex="0"` if it is not a native interactive element.
- Respect `prefers-reduced-motion` — disable scale and transition, keep the static ring.
- Hover-only states — TV remotes have no hover; all states must be reachable via D-pad.
- Missing `tabIndex` on interactive custom elements — they become unreachable by keyboard/remote.
- Relying on `outline:none` without a replacement — leaves TV users with no focus signal at all.
- Focus ring contrast below 3:1 — fails WCAG 2.4.11 for non-text contrast.

## When to use

Use when

- Any interactive element on TV that must be navigable via D-pad/remote
- Game cards, buttons, and menu items that need a visible focus ring
- Spatial navigation grids and carousels on TV screens
- TV-specific focus state that scales with the TV layout grid

Don't use when

- Desktop or mobile — TV focus ring is for 10-foot UI only
- Overriding the ring color outside the jio-glow token
- Focus rings on non-interactive decorative elements
- Removing the focus ring for any reason on TV — required for accessibility

## Variants

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Ring thin | 2px + 8px spread | Compact UI elements | TV |
| Ring default | 3px + 16px glow spread | Cards, buttons | TV |
| Ring prominent | 4px + 24px glow spread | Hero items, featured | TV |

## States

Unfocused

No ring; element at rest scale (1.0)

Focused

3px jio-green ring + 0 0 24px rgba(0,168,89,.4) glow; scale 1.08 for cards

Selected (pressed OK)

Brief scale pulse 0.95 → 1.0 + ring flash white → jio

Focused + loading

Ring maintained; content shows spinner overlay

Focus lost

Ring fades out with ease-in; scale returns to 1.0

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Focus ring appear | `--ease-out` | `--dur-fast` | box-shadow (0 → jio-glow) |
| Focus scale | `--ease-out` | `--dur-fast` | transform scale(1.08) |
| Focus ring pulse (selected) | `ease-in-out` | `1.5s infinite` | box-shadow scale |
| D-pad navigation | `--ease-out` | `--dur-fast` | focus transfer between elements |

## Platform rules

Mobile

- Not used — mobile focus is handled via :focus-visible CSS natively

Web

- Not used on web — web focus ring uses standard :focus-visible + jio-green outline
- TV focus component is TV-only; do not apply on web-targeted elements

TV

- Apply to every interactive element — cards, buttons, list items, nav items
- Ring: box-shadow 0 0 0 3px var(--jio), 0 0 24px rgba(0,168,89,.4)
- Scale: 1.08 for cards; 1.06 for buttons; 1.0 for full-width items
- D-pad spatial navigation: register elements in the nav grid
- Never remove the focus ring — required for accessibility on TV
- Pressed (OK): scale(0.95) flash then return to focused scale

## Accessibility

### ARIA attributes

| Attribute | Element | Value / notes |
|---|---|---|
| `aria-label` | Focusable element | Required when element has no visible text label |
| `tabindex="0"` | Custom focusable element | Makes non-interactive elements focusable |
| `aria-pressed` | Toggle button | "true" / "false" state announcement |
| `aria-selected` | Selectable card | "true" when selected in a group |
| `aria-live="polite"` | Dynamic content area | Announces content changes on D-pad navigation |

### Keyboard interaction

| Key | Action |
|---|---|
| D-pad Up/Down/Left/Right | Move focus between elements |
| OK / Enter | Activate focused element |
| Back | Navigate back or cancel |
| Options/Menu button | Open context actions for focused item |

### Guidelines

- Focus ring must always be visible — never remove for aesthetic reasons on TV
- All interactive elements must be reachable via D-pad — no mouse-only interactions
- Focus order must be logical and predictable — follows visual layout
- Screen reader on TV reads focused element label and role on each D-pad move
- Spatial navigation: ensure no focus traps except modal dialogs
- Minimum WCAG AA contrast ratio 4.5:1 for text; 3:1 for UI components at 10-foot viewing

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-tv-focus` | Focus ring wrapper — applies on :focus-visible |
| `.ds-tv-focus:focus-visible` | box-shadow: 0 0 0 3px var(--jio), 0 0 24px rgba(0,168,89,.4) |
| `.ds-tv-focus--card` | Card-specific focus — scale(1.08) + ring |
| `.ds-tv-focus--btn` | Button-specific — scale(1.06) + ring |
| `.ds-tv-nav-grid` | Spatial navigation container for D-pad focus |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | ElementType | "div" | Root element type to render |
| `focusable` | boolean | true | Adds tabIndex and focus ring |
| `onFocus` | () => void | undefined | Focus handler |
| `onBlur` | () => void | undefined | Blur handler |
| `onSelect` | () => void | undefined | Fired on Enter/OK remote press |
| `children` | ReactNode | required | Focusable content |

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--border-subtle`
- `--dur-base`
- `--ease-out`
- `--gold`
- `--jio`
- `--jio-glow`
- `--jio-soft`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--spring`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--tv-focus-scale`
- `--tv-focus-shadow`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

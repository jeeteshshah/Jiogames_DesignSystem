# Icons — JioGames DLS spec

> Source: `icons/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Icons

---

Icons are visual symbols that communicate actions, objects, and states across the JioGames interface.

Icons in JioGames are delivered as a single SVG sprite, referenced via ``. This keeps the DOM lightweight and allows a single token change to recolor every icon on a screen. The system defines five glyph sizes (XS–XL), each resolving to different pixel values on Mobile, Web, and TV.

- **Sprite-based delivery.** One `sprite.svg` file. All icons via ``. No per-icon files, no inline blobs, no font icons.
- **Platform-aware sizing.** Five size names (XS/S/M/L/XL) resolve to different pixel values per platform. The same class works everywhere; the platform context sets the token alias.
- **Semantic color via currentColor.** Icons inherit fill from their container. Swap one CSS custom property to recolor entire icon families instantly.
- **Touch targets are separate from glyph size.** A 20px icon inside a 44px wrapper provides the WCAG-compliant touch area without inflating the visual glyph.
- **TV focus ring.** On TV, focused icon wrappers receive the `--tv-focus-shadow` glow and scale(1.05) transform, not a 2px outline.

## When to use

Use when

- Communicating actions and states without relying solely on text
- Leading icons in buttons, inputs, and navigation items
- Status indicators in list items and toasts
- Decorative supporting visuals alongside text headings

Don't use when

- Icons alone without labels for ambiguous actions — always pair with accessible text
- Mixing icon styles (outline vs filled) within one UI surface
- Custom-coloured icons outside the token system — use currentColor
- Icons smaller than 16px — readability breaks below this size

## Best practices

Icons reduce cognitive load when used consistently. These rules keep icon usage coherent across all surfaces.

- Use `aria-hidden="true"` on all decorative icons
- Pair icon-only controls with an `aria-label` on the interactive element
- Use L (24px) as the default glyph size in navigation and primary UI
- Wrap interactive icons in a touch target div at least 44px × 44px on mobile
- Use `fill:currentColor` so icons respond to theme changes
- On TV, use icon-wrap-l (76px) minimum touch area
- Use named sprite IDs — never hardcode path data in product HTML

- Don't resize icons by changing `viewBox` — use `width`/`height` attributes
- Don't use `img` tags for icons — they can't be recolored via CSS
- Don't use XS (12px) icons as standalone interactive targets
- Don't rely on icons alone to communicate state — always add text or ARIA label
- Don't use `.icon--tv` — deprecated, use `.icon--xl` inside `.platform-tv`
- Don't hardcode pixel sizes — use the `--icon-*` token aliases
- Don't mix icon families or styles within the same UI region

## Anatomy

An icon has up to five layers. Only the SVG glyph and its viewbox are required. Wrapper, touch target, and focus ring are contextual additions for interactive use.

## Icon library 1,646 icons

All icons from the JioGames sprite. Click any icon to copy its ID to clipboard. Rendered at L (24px).

## Variants

## Sizes

Five canonical size names cover all use cases. On TV, all sizes shift larger to maintain 10-foot legibility. The `--icon-*` runtime aliases resolve automatically via media query and `.platform-tv` context.

## States

Icons themselves are stateless. State is applied to the interactive wrapper. Use `.is-*` helper classes from `states.css` to demonstrate states in prototypes.

## Content guidance

Icon selection affects comprehension. Choose icons that match the mental model of the player, not the technical action of the system.

- Use universally understood symbols for navigation (house = home, magnifier = search)
- Prefer outlined icons for inactive states, filled for active
- Avoid icons that could be interpreted differently across cultures
- When in doubt, use icon + label — don't rely on icon alone for novel actions

- Default fill: `var(--icon-color-default)` — rgba white at 45%
- Active / selected: `var(--icon-color-active)` — JioGames green
- Muted / disabled: `var(--icon-color-muted)` — #6B7280
- Never use red icons in navigation — red is reserved for destructive/error states

- Always add `aria-label` to the interactive element
- Surface a tooltip on hover (web) describing the action
- Use icon + label if there is sufficient space — icons alone reduce discoverability for new users
- In bottom nav bars, always show labels below icons

- New icons must be drawn on 24×24 viewbox with 2px consistent stroke
- Submit as a single-path SVG optimized with SVGO
- Icon must pass visual consistency review against existing set
- Add to `sprite.svg` with an `ic_` prefix ID

## Platform considerations

Icon rendering and interaction differ fundamentally across Mobile, Web, and TV. Glyph size tokens auto-resolve per platform; wrapper and focus behavior require intentional decisions.

- 44×44px minimum touch target for all interactive icons
- L (24px) glyph in navigation; M (20px) in dense UI
- Active color on selected tab bar icon
- No hover state — pressed state only on touch
- Bottom navigation icons always include labels
- Suppress tap highlight: `-webkit-tap-highlight-color: transparent`

- Hover state on wrapper on cursor entry
- Keyboard focus via `:focus-visible` — 2px green outline
- Tooltips required for all icon-only interactive elements
- Icon wrap-m (40px) — slightly smaller than mobile target is acceptable for web
- Cursor: pointer on all interactive wrappers
- XS icons (12px) acceptable in dense data tables or badges

- D-pad navigation — no hover, no pointer
- Icon-wrap-l (76px) minimum touch area for focus visibility
- Green glow + scale(1.05) on focus via `--tv-focus-shadow`
- XL (48px) in hero areas; L (40px) in rails and navigation
- Never use XS or S icons as standalone TV targets
- Use `.is-tv-focused` to simulate TV focus in prototypes

## Migration

The `.icon--tv` class is deprecated as of v4.0. Migrate to the platform-aware size system using `.icon--xl` inside a `.platform-tv` wrapper.

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Loading spinner | `linear` | `600ms infinite` | transform rotate(360deg) |
| Appear | `--ease-out` | `--dur-fast` | opacity, transform scale(0.8 → 1) |
| State change (e.g. mute toggle) | `--ease-out` | `--dur-fast` | opacity crossfade |

## Platform rules

Mobile

- Minimum 24px render size — smaller icons are not legible on phone screens
- Touch targets for icon-only buttons: 44×44px wrapper around 20–24px icon
- Use fill variants for primary actions; outline for secondary
- ic_ snake_case naming — always use sprite reference, never inline SVG paths

Web

- 16px icons acceptable inline with text labels (breadcrumbs, table cells)
- Hover-state color inherits from parent — no separate icon hover CSS needed
- SVG sprite loaded once via sprite-loader.js — no per-icon HTTP requests

TV

- Minimum 32px at 1x — scales to 40px+ for nav and hero icons
- Fill icons only on TV — outline detail disappears at 10-foot viewing distance
- High contrast: always use --text or --jio color — avoid text3 on TV

## Accessibility

Icons are visual shorthand. Ensure every icon is either descriptively labelled for assistive technology or explicitly marked as decorative.

- Tab — moves focus to interactive icon wrapper
- Enter or Space — activates the icon control
- Focus ring visible on `:focus-visible`, hidden on mouse click
- TV: d-pad directional focus handled by the shell focus manager

- Default: `rgba(255,255,255,.45)` on `#06080F` — passes 3.1:1 (UI component threshold)
- Active: `#00A859` on `#06080F` — 3.6:1 (meets non-text threshold)
- For informational icons used alone (without labels), target 4.5:1

## Related tokens

All icon values are defined in `tokens/tokens.css`. Changing a token updates every icon instance using that alias.

| Token | Value | Swatch | Usage |
|---|---|---|---|
| `--icon-color-default` | `rgba(255,255,255,.45)` |   | Inactive icon fill |
| `--icon-color-active` | `#00A859` |   | Selected / active icon fill |
| `--icon-color-muted` | `#6B7280` |   | Disabled / muted icon fill |
| `--icon-fill-default` | `var(--icon-color-default)` |   | Semantic alias for default fill |
| `--icon-fill-active` | `var(--icon-color-active)` |   | Semantic alias for active fill |

| Token | Mobile | Web | TV |
|---|---|---|---|
| `--icon-xs` | 12px | 12px | 20px |
| `--icon-s` | 16px | 16px | 24px |
| `--icon-m` | 20px | 20px | 32px |
| `--icon-l` | 24px | 24px | 40px |
| `--icon-xl` | 32px | 32px | 48px |
| `--icon-wrap-xs` | 32px | 32px | 52px |
| `--icon-wrap-s` | 36px | 36px | 60px |
| `--icon-wrap-m` | 44px | 40px | 68px |
| `--icon-wrap-l` | 48px | 48px | 76px |
| `--icon-wrap-xl` | 56px | 56px | 84px |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-icon` | Wrapper — inline-flex, currentColor fill |
| `.ds-icon--16` | 16×16px |
| `.ds-icon--20` | 20×20px (default) |
| `.ds-icon--24` | 24×24px |
| `.ds-icon--32` | 32×32px |
| `.ds-icon--spin` | Rotation animation for loading states |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `name` | IconName | required | Icon identifier from the sprite (e.g. "ic_play_fill") |
| `size` | 16 | 20 | 24 | 32 | 20 | Width and height in px |
| `color` | string | currentColor | Fill color — use CSS token or "currentColor" |
| `aria-label` | string | undefined | Accessible label for non-decorative icons |
| `aria-hidden` | boolean | true | Hide from screen readers when decorative |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<!-- Inline icon via sprite (recommended) -->
<svg class="icon icon--m" aria-hidden="true">
  <use href="/sprite.svg#ic_home"></use>
</svg>

<!-- Icon with accessible label -->
<button class="btn btn--icon" aria-label="Search">
  <svg class="icon icon--m" aria-hidden="true">
    <use href="/sprite.svg#ic_search"></use>
  </svg>
</button>
````

````
<!-- XS: 12px -->
<svg class="icon icon--xs" aria-hidden="true"><use href="/sprite.svg#ic_star"></use></svg>

<!-- S: 16px -->
<svg class="icon icon--s" aria-hidden="true"><use href="/sprite.svg#ic_star"></use></svg>

<!-- M: 20px (default) -->
<svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_star"></use></svg>

<!-- L: 24px -->
<svg class="icon icon--l" aria-hidden="true"><use href="/sprite.svg#ic_star"></use></svg>

<!-- XL: 32px -->
<svg class="icon icon--xl" aria-hidden="true"><use href="/sprite.svg#ic_star"></use></svg>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--bg2`
- `--border`
- `--border-subtle`
- `--focus-ring-color`
- `--glass-1`
- `--gold`
- `--icon-color-active`
- `--icon-color-default`
- `--icon-color-muted`
- `--icon-l-mobile`
- `--icon-l-tv`
- `--icon-l-web`
- `--icon-m-mobile`
- `--icon-m-tv`
- `--icon-m-web`
- `--icon-s-mobile`
- `--icon-s-tv`
- `--icon-s-web`
- `--icon-xl-mobile`
- `--icon-xl-tv`
- `--icon-xl-web`
- `--icon-xs-mobile`
- `--icon-xs-tv`
- `--icon-xs-web`
- `--jio`
- `--jio-font`
- `--jio-glow`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--state-hover-bg`
- `--state-selected-bg`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
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

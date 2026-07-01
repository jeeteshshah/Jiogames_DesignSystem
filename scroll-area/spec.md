# Scroll Area — JioGames DLS spec

> Source: `scroll-area/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Scroll Area

---

Custom scrollable container with styled scrollbars that match the JioGames dark theme. Replaces native scrollbars in panels, sidebars, and horizontal rails.

Scroll Area · Vertical (thin bar on right) and horizontal (bar on bottom) variants

Scroll Area is a thin wrapper that replaces the browser's default native scrollbar with a styled alternative that matches the JioGames dark theme. The scrollbar track is transparent; the thumb uses the system border color and rounds to a pill shape. On mobile and TV, the native scrollbar behavior is preserved but the bar is hidden — content communicates scrollability through fade-edge gradients or context.

- **Vertical (--y)** — friend lists, settings panels, notification feeds, sidebars
- **Horizontal (--x)** — genre chip rows, tab lists, filter bars, compact image rails
- **Both axes** — code blocks, map views, large media previews
- **Hidden bar (--hidden-bar)** — game rails, carousels, swipeable card rows where the fade edge signals more content

- Use `--hidden-bar` for horizontal game rails — the fade-edge gradient is a more native signal
- Add `tabindex="0"` so keyboard users can focus and scroll the region
- Add `aria-label` describing what the region contains and that it is scrollable
- Set an explicit height on vertical scroll areas — never let them grow unbounded
- Use `-webkit-overflow-scrolling: touch` for momentum scrolling on iOS

- Show a thin scrollbar on horizontal game rails — the bar obscures art; use hidden bar instead
- Nest scroll areas — inner and outer both scrolling creates a scroll trap
- Use scroll area on TV — replace with D-pad pagination or carousel navigation
- Rely on scrollbar visibility alone to indicate more content — always pair with a fade edge or "scroll to see more" label
- Override scrollbar color to a brand-green thumb — the muted border color is intentional; it should not compete with content

1. 1 Scroll container Required The wrapper element with overflow set. Must have an explicit height (vertical) or width (horizontal). Use .scroll-area as the base class plus a direction modifier. `overflow: auto; scrollbar-width: thin`
2. 2 Scrollbar thumb Optional 6px wide, pill-shaped, --border color. Brightens on hover to --text3. Hidden entirely with --hidden-bar modifier. Transparent track — never shows a track background color. `width:6px; background:var(--border); border-radius:var(--pill)`
3. 3 Scrollable content Required Any content placed inside the scroll area. For horizontal rails, use a flex row with width: max-content. For vertical panels, use a flex column or block flow. `width: max-content (horizontal) | height: auto (vertical)`

## Variants

All variants share the same base .scroll-area class. Modifiers control axis and scrollbar visibility.

````
function initLeaderboard(gameId, limit = 10) {
  return fetch('/api/leaderboard?game=' + gameId + '&limit=' + limit)
    .then(r => r.json())
    .then(data => renderTable(data.entries));
}
````

## Sizes

Only the scrollbar thumb has a fixed size. The container dimensions are always application-defined — the scroll area adapts to whatever size you give it.

| Property | Thin (default) | None (hidden) |
|---|---|---|
| Scrollbar width (vertical) | `6px` | `none` |
| Scrollbar height (horizontal) | `6px` | `none` |
| Thumb color | `var(--border)` | N/A |
| Thumb hover color | `var(--text3)` | N/A |
| Container height/width | Set by the consuming component — not defined by Scroll Area |   |

## States

The scrollbar has three visual states. The container itself has no additional states beyond what the browser provides.

## Content guidance

- Always use `--hidden-bar` — the scrollbar competes with card art
- Pair with a right-side fade-edge gradient to signal overflowing content
- The fade color must match the background behind the rail exactly
- Never show scroll affordance text ("Scroll to see more") — the fade is sufficient

- Use the thin bar (default) so users know the panel is scrollable
- Set a max-height relative to the viewport — avoid panels taller than 80vh
- Content inside must never be wider than the panel — prevents unwanted horizontal scroll
- Add `padding-right: 8px` to content so text doesn't sit under the scrollbar thumb

## Platform considerations

- Use native momentum scrolling: `-webkit-overflow-scrolling: touch`
- Always hide scrollbars on mobile — native touch scroll is self-evident
- Use fade edges for horizontal rails to indicate off-screen content
- Ensure scroll containers have a minimum swipe target of 44px height
- Avoid nested scrollable regions — creates scroll trap UX issues

- Show the thin styled scrollbar for vertical panels — users expect mouse-draggable thumb
- Hide bar for horizontal chip rows and rails — use fade edge instead
- Ensure the container has `tabindex="0"` and keyboard scroll (arrow keys)
- Test in Firefox — `scrollbar-width: thin` controls both width and color there
- Do not auto-scroll on page load — respect user's scroll position

- Do not use Scroll Area on TV — use D-pad pagination or carousel instead
- Scrollbars are invisible at 3m viewing distance and non-interactive with remote
- Replace vertical lists with paginated grids
- Replace horizontal chip rows with a focused tab component

## Accessibility

| Requirement | Implementation | Guidance |
|---|---|---|
| Keyboard focus | `tabindex="0"` | All scroll regions must be reachable by Tab key. Once focused, arrow keys scroll the container. |
| Region label | `aria-label` | Describe the content and scrollability: "Friend list, scrollable". Screen readers announce this when the user tabs into the region. |
| Content semantics | Semantic HTML inside | Scroll Area is a layout wrapper only — the content inside must use correct semantic elements (ul/li, table, etc). |
| Color contrast | Thumb color | The scrollbar thumb uses --border which meets AA contrast against the transparent track. Do not lighten further. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--border` | `rgba(255,255,255,.12)` | Scrollbar thumb default color |
| `--text3` | `rgba(244,242,238,.32)` | Scrollbar thumb hover color |
| `--pill` | `100px` | Scrollbar thumb border-radius |
| `--bg` | `#080a10` | Fade-edge gradient end color (must match surrounding background) |
| `--r4` | `—` | Scroll container border-radius for card-like panels |
| `--border-subtle` | `rgba(255,255,255,.08)` | Container border for framed scroll areas |

## When to use

Use when

- Overflow containers with custom-styled scrollbars
- Fixed-height panels with scrollable content (modals, sidebars, dropdowns)
- Chat message feeds and notification lists
- Code blocks and log viewers

Don't use when

- Full-page scroll — use native browser scroll instead
- Horizontal scroll areas on mobile — swipe conflicts with navigation
- Nested scroll areas in the same axis — scroll trap issues

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Scrollbar appear | `--ease-out` | `--dur-fast` | opacity (visible on hover/scroll) |
| Scrollbar hide | `--ease-in` | `600ms delay` | opacity → 0 |
| Scroll momentum | `native` | `realtime` | scrollTop/scrollLeft |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-scroll-area` | Root — position relative, overflow hidden |
| `.ds-scroll-area__viewport` | Scrollable inner — overflow scroll |
| `.ds-scroll-area__scrollbar` | Custom scrollbar track — 8px wide |
| `.ds-scroll-area__thumb` | Scrollbar thumb — r-pill, glass-2 bg |
| `.ds-scroll-area__corner` | Bottom-right corner where axes meet |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `type` | "auto" | "always" | "scroll" | "hover" | "hover" | When scrollbar is visible |
| `scrollHideDelay` | number | 600 | ms before scrollbar hides after scroll stops |
| `orientation` | "vertical" | "horizontal" | "both" | "vertical" | Scroll axis |
| `children` | ReactNode | required | Scrollable content |

## Code examples

````html
<div class="scroll-area scroll-area--y"
     style="height: 300px;"
     tabindex="0"
     aria-label="Friends list, scrollable">
  <ul>
    <li>ArjunKing99 — Tomb Raider</li>
    <li>PriyaStar — In menus</li>
    <!-- more items -->
  </ul>
</div>
````

````html
<div class="scroll-area scroll-area--x"
     tabindex="0"
     aria-label="Genre filter chips, scrollable">
  <div style="display:flex; gap:8px; width:max-content;">
    <button class="genre-chip genre-chip--active">All</button>
    <button class="genre-chip genre-chip--muted">Action</button>
    <button class="genre-chip genre-chip--muted">Adventure</button>
    <!-- more chips -->
  </div>
</div>
````

````
<!-- Wrap in a position:relative container for the fade -->
<div class="scroll-fade-wrap">
  <div class="scroll-area scroll-area--x scroll-area--hidden-bar"
       tabindex="0"
       aria-label="Featured games, scrollable">
    <div style="display:flex; gap:10px; width:max-content;">
      <!-- game cards -->
    </div>
  </div>
</div>

<style>
.scroll-fade-wrap { position: relative; }
.scroll-fade-wrap::after {
  content: '';
  position: absolute;
  top: 0; right: 0; bottom: 0;
  width: 48px;
  background: linear-gradient(to right, transparent, var(--bg));
  pointer-events: none;
  z-index: 1;
}
</style>
````

## Changelog

Initial draft. Covers vertical, horizontal, both-axes, and hidden-bar variants. Includes fade-edge pattern for game rails, keyboard accessibility guidance, and platform notes.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--code-green`
- `--jio`
- `--negative`
- `--pill`
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

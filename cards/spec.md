# Cards — JioGames DLS spec

> Source: `cards/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Cards

---

Cards are the primary surface for presenting games, passes, and content items across JioGames.

Cards · Landscape, Portrait, Focus state

Cards are the fundamental building block of game discovery in JioGames. They appear across every surface — home rails, genre pages, search results, and pass libraries — presenting just enough information for a player to decide whether to tap and learn more or launch directly. Every card consists of a media area backed by game art, a lightweight metadata footer, and a system of overlays for states like locked, premium, and unavailable.

- **Media area** — The art container. Maintains aspect ratio at all breakpoints. Uses a gradient placeholder during load.
- **Title + metadata** — Game name (2-line max with ellipsis), optional genre, rating, or duration row beneath.
- **Badge overlays** — Positioned chips in corner regions: NEW, PREMIUM, LIVE, or custom labels. Max two badges per card.
- **Focus / selected states** — Green glow ring on TV and web keyboard navigation. Scale animation on press for mobile.

## Best practices

- Maintain aspect ratio strictly — 16:9 for landscape, 2:3 for portrait. Never stretch or squish art.
- Cap title to 2 lines maximum with `text-overflow: ellipsis` and `-webkit-line-clamp: 2`.
- Include a skeleton at the exact card dimensions before art loads — width, height, and border-radius must match.
- Use the lock icon alongside "Subscribe to unlock" copy for locked-state cards so the restriction is immediately clear.

- Don't crop art unevenly — always use `object-fit: cover` centered on the image.
- Don't show a blank white or transparent art area when the image fails to load; always fall back to the gradient placeholder.
- Don't use cards for navigation links that have no media (use list rows or menu items instead).
- Don't allow text overflow without truncation — a card with wrapping text breaks the grid alignment.

## Anatomy

A landscape card showing all optional and required zones. Most cards only render 1–4 of these layers.

- 1 Media area Required The image or art container. Occupies the full card surface, always `object-fit: cover`. Falls back to gradient placeholder.
- 2 Title Required Game or content name. Maximum 2 lines, `-webkit-line-clamp: 2`. Positioned in the gradient overlay zone.
- 3 Metadata row Optional Secondary information: genre, star rating, play duration. Rendered below title in muted text. Pattern: `Genre · ★Rating`.
- 4 Badge overlay Optional Positioned chip in a card corner (top-left preferred). Labels: NEW, PREMIUM, LIVE, or custom. Max 2 words. Max 2 badges per card. --premium-gradient
- 5 Locked overlay Optional Semi-transparent dark scrim over the media area with a lock icon and "Subscribe to unlock" text centred vertically. --locked-overlay
- 6 Focus ring Optional Green glow ring applied on TV D-pad focus and web keyboard navigation. Meets 3:1 contrast. Uses `box-shadow: 0 0 0 2px #00A859, 0 0 24px rgba(0,200,100,.4)`.

## Variants

Five card variants cover all use cases across JioGames surfaces.

## Sizes

Card dimensions across size tiers and platforms. All values are width × height in pixels. Hero cards use full container width.

| Size | Mobile | Web | TV |
|---|---|---|---|
| Compact | `152 × 96` | `168 × 106` | `240 × 150` |
| Standard | `200 × 126` | `220 × 138` | `320 × 200` |
| Large | `272 × 172` | `300 × 188` | `400 × 250` |
| Hero | `100% × 200` | `100% × 320` | `100% × 540` |

## States

All interactive and visual states a card can express. Not all states apply to every variant.

## Content guidance

What goes on a card and how to present it correctly.

### Title & metadata

- Maximum 2 lines — always truncate with `-webkit-line-clamp: 2` and an ellipsis. Never wrap to a third line.
- Metadata row pattern: `Genre · ★Rating` or `Genre · Duration`. Use the interpunct (·) as separator, not a dash.
- Star ratings use the ★ character followed by the numeric score to one decimal place (e.g. ★4.9).
- Badges are ALL CAPS, maximum 2 words (e.g. NEW, LIVE NOW, EARLY ACCESS). Do not use sentence case.
- Do not repeat the game name in both the badge and the title area — the title is always sufficient.

### Locked & premium

- A locked game must show the lock icon (🔒) alongside the text "Subscribe to unlock" — never use color alone to communicate the restriction.
- Premium pass games show the gradient PREMIUM badge (`--premium-gradient`) in the top-left corner and a subtle green border (`--premium-border`).
- Do not combine both a locked overlay and a premium badge — a game is either accessible (premium) or blocked (locked), not both.
- Unavailable games must use opacity reduction only — do not add any overlay text or iconography; the reduced opacity signals the state passively.

## Platform considerations

Card behaviour adapts to the interaction model of each platform.

- Cards sit in horizontally scrollable rails with `overflow-x: auto` and `scroll-snap-type: x mandatory`.
- Left and right gutters are `20px` from the viewport edge.
- Inter-card spacing is `10px`.
- Tapping a card navigates directly to game detail. No hover state.
- Active state uses `scale(0.97)` at 80ms for press feedback.
- Swipe momentum must remain native — do not block `touchmove` on card scroll containers.

- Hover state elevates the card with `translateY(-2px)` and a deeper shadow. Transition 150ms ease-out.
- Cursor must be `pointer` on all interactive cards.
- Gutter is `24px` each side. Cards in a grid use a `gap` of `16px`.
- Keyboard focus (Tab key) shows the green focus ring — never suppress the outline without replacing it.
- Right-click context menu can optionally surface "Add to wishlist" and "Share" actions.

- Focus ring is mandatory — it is the primary interaction signal. Class `.is-tv-focused` applies the green glow.
- D-pad navigation moves focus between cards. Left/right within a rail; up/down between rails.
- Card sizes are the largest tier — use the TV column from the sizes table above.
- Inter-card spacing increases to `20px` to allow the focus ring to breathe without overlapping adjacent cards.
- Do not rely on hover — TV remotes have no pointer. All interactive states must be reachable via D-pad alone.
- Long-press Select on a focused card opens a context action sheet (play, add to list, details).

## Accessibility

Cards must be usable by screen readers, keyboard-only users, and assistive technology.

| Attribute / Pattern | Value / Guidance | Notes |
|---|---|---|
| `role` | `article` (static) or `button` (interactive) | Use `button` when the card is the primary tap/click target. Never nest interactive elements inside a `button`-role card. |
| `aria-label` | Include game name + status | Example: `aria-label="Tomb Raider, Action, rated 4.9"`. Add status for premium: `"Doom Eternal, included in JioGames Pass"`. |
| Locked state announcement | `"Subscribe to unlock"` appended to label | Screen readers must hear the restriction. Include in `aria-label`: `"War Thunder — Subscribe to unlock"`. |
| Skeleton loading | `aria-busy="true"` | Add `aria-label="Loading game"` on the skeleton container. Remove both attributes once content is populated. |
| Focus ring contrast | `#00A859` on `#06080F` | Meets WCAG 2.1 SC 1.4.11 Non-text Contrast minimum of 3:1. The additional outer glow (`rgba(0,200,100,.4)`) is decorative only. |

## Related tokens

Design tokens from `tokens.css` that directly govern card appearance.

| Token | Value | Usage |
|---|---|---|
| `--card-radius-landscape` | `16px` | Border-radius for all landscape (16:9) card containers. |
| `--card-overlay` | gradient | Bottom gradient overlay for title/metadata legibility. Fades from `rgba(6,8,15,.85)` to transparent at 55%. |
| `--locked-overlay` | `rgba(6,8,15,.75)` | Full-card scrim for locked state. Applied as an absolute inset layer over the art. |
| `--premium-gradient` | gradient | Fill for PREMIUM badge chip. `linear-gradient(135deg, var(--ultimate), var(--jio-bright))`. Dark text (#06080F) on top. |
| `--skeleton-bg` | `#161A24` | Base background colour for card skeleton / loading state. Maps to `--surface-2`. |
| `--unavailable-opacity` | `0.4` | Opacity applied to the entire card element when the game is unavailable in the user's region. |

## When to use

Use when

- Game tiles in horizontal rails and grid layouts
- Pass plan comparison with price and features
- Content previews with thumbnail, title, and metadata
- Leaderboard entries, achievement items, and list rows with rich media

Don't use when

- Full-bleed editorial sections — use a section layout instead
- Single lines of text with no visual hierarchy — use a List item
- Deeply nested cards (card inside card)
- Interactive cards without a visible affordance (hover/focus state)

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Hover lift | `--ease-out` | `--dur-fast` | transform scale(1.02), box-shadow |
| Press | `--ease-out` | `80ms` | transform scale(0.97) |
| TV focus scale | `--ease-out` | `--dur-fast` | transform scale(1.06) |
| Image load fade | `--ease-out` | `--dur-base` | opacity |
| Skeleton shimmer | `linear` | `1400ms infinite` | background-position |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-card` | Base card — surface-1 bg, border-subtle, r4 radius |
| `.ds-card--game` | Game tile — 16:9 thumbnail + title + metadata |
| `.ds-card--pass` | Pass plan card — gradient header, feature list |
| `.ds-card--wide` | Landscape card for horizontal rails (210×128px) |
| `.ds-card--portrait` | Portrait cover card (120×180px) |
| `.ds-card__thumbnail` | Image container — aspect-ratio enforced |
| `.ds-card__body` | Text content area — padding 12px |
| `.ds-card__title` | Card title — 13px 600 weight |
| `.ds-card__meta` | Secondary info row — 11px text3 |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | "game" | "pass" | "wide" | "portrait" | "default" | "default" | Card layout preset |
| `href` | string | undefined | Makes card a link — wraps in anchor |
| `onClick` | () => void | undefined | Press handler |
| `thumbnail` | string | undefined | Image URL for the card hero |
| `title` | string | required | Card headline text |
| `meta` | string | ReactNode | undefined | Secondary descriptor below title |
| `badge` | ReactNode | undefined | Overlay badge (New, Hot, Live) |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="card">
  <div class="card__art">
    <img src="game-hero.jpg" alt="War Thunder" class="card__img">
    <div class="card__overlay"></div>
  </div>
  <div class="card__body">
    <div class="card__title">War Thunder</div>
    <div class="card__meta">Action · Free to play</div>
  </div>
</div>
````

````html
<div class="card is-hover">
  <div class="card__art">
    <img src="game-hero.jpg" alt="Tomb Raider" class="card__img">
    <div class="card__overlay"></div>
    <span class="badge badge--new">New</span>
  </div>
  <div class="card__body">
    <div class="card__title">Tomb Raider</div>
    <div class="card__meta">Adventure · Pass included</div>
  </div>
</div>
````

## Changelog

Added `--premium-gradient`, `--premium-border`, and `--locked-overlay` tokens. Introduced the premium badge pattern and the locked-state overlay specification. Updated anatomy diagram to include callouts 4 and 5.

Added TV focus glow state. Introduced `.is-tv-focused` class with green ring `box-shadow` pattern. Documented D-pad navigation requirements and TV size tier. Updated platform considerations section.

Initial component release. Landscape, portrait, square, mini, and hero variants. Default, hover, active, locked, unavailable, and skeleton states. Anatomy, best practices, sizes, and accessibility documentation.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-ultimate`
- `--gold`
- `--jio-bright`
- `--jio-font`
- `--surface-2`
- `--text`
- `--text2`
- `--text3`
- `--ultimate`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

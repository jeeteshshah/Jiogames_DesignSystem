# Genre Tiles — JioGames DLS spec

> Source: `genre-tiles/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Genre Tiles

---

Genre tiles are square, art-forward tiles that let players browse and select game categories across JioGames.

Genre tiles give players an art-forward way to explore JioGames content by category. They appear in the home page browse rail, onboarding genre preference flows, and search filter surfaces. Each tile pairs a rich gradient background with a bold white label for instant scannability at any size.

- **Art-forward.** Each tile uses a unique CSS gradient keyed to its genre — no two tiles share the same palette in the same view.
- **Selection.** A 1.5px green border plus a subtle green-tinted background communicates the selected state without relying on color alone. Label color also shifts to green.
- **Platform-adaptive.** Square 96px on mobile, wide 160×80px on web, 120px+ square on TV. Same component, different size token per platform.
- **Premium gating.** Locked genres display a semi-transparent scrim overlay with a lock icon, communicating that the Pass is required before the category becomes browsable.

## When to use

Use when

- Genre selection in onboarding preference screens
- Genre navigation on the discovery/browse home screen
- Platform selection (Mobile, Web, TV) in onboarding
- Category quick-links in rail headers

Don't use when

- Filter chips (for filtering content, not navigation) — use Chip instead
- More than 12 tiles in a single screen without scrolling
- Text-only without icon/illustration — tiles need a visual anchor

## Best practices

Follow these rules to keep genre tile usage consistent across JioGames surfaces.

- Use unique gradient palette per genre — never repeat in the same grid
- Keep genre names to 1–2 words in title case: "Action", "Open World"
- Show the full selected state: green border + green bg + green label
- Ensure genre label text always renders over the gradient with sufficient contrast
- Minimum tile size 96px on mobile — meets touch-min 44px touch target
- On TV, increase tile to 120px+ and use tv-focus-shadow on focused state
- Use `aria-pressed` for selection state, not `aria-checked`

- Don't use the same gradient hue for two different genres in one view
- Don't write genre names longer than 2 words — tiles cannot truncate
- Don't rely on color alone to show selection — green label text is required
- Don't use solid saturated fills — they overpower the dark surface
- Don't omit the lock icon on premium tiles — grayed-out alone is insufficient
- Don't disable locked tiles with HTML `disabled` — use `aria-disabled` so they remain focusable
- Don't place tiles smaller than 72px — readability and tap target both suffer

## Anatomy

Every genre tile is built from five slots. The container, background, and label are always required. The selection indicator and lock overlay are conditional.

## Variants

Five variants cover every use context across surfaces and selection states.

## Sizes

Tile size is determined by platform context. The same component renders at different pixel dimensions on Mobile, Web, and TV via the size token system.

## States

Genre tiles respond to seven interaction states. Use the `.is-*` helpers from `states.css` to simulate states in prototypes and docs.

## Content guidance

Genre label copy must be short, clear, and scannable at a glance. Each tile communicates a single category.

- 1–2 words maximum, title case: "Action", "Open World", "Tower Defense"
- Use the player-facing genre name, not internal taxonomy
- Prefer "Sports" over "Sport Games" — shorter is more scannable
- Avoid abbreviations unless universally understood: "RPG" is acceptable
- Do not number genres: "Action 1" is never correct

- Label is always white on gradient — never colored to match the gradient
- When selected, label stays white on art background — green border carries the state
- Gradient must provide at least 4.5:1 contrast ratio beneath the label
- Avoid label text that visually blends with gradient highlight colors
- Lock overlay text: use `aria-label` only — no visible extra text on tile face

- Show lock icon only — no "Premium" text label on the tile face
- Tooltip or modal on tap should explain which Pass unlocks the genre
- Do not say "Locked" in the aria-label — say "[Genre] — requires JioGames Pass"

- Optional top-right badge showing number of titles in that genre
- Format: plain number, e.g. "48" — no "games" suffix at small sizes
- Hide badge if count is 0 or unknown — do not show "0"
- Max display value: "99+" for counts above 99

## Platform considerations

Genre tiles adapt across Mobile, Web, and TV contexts. Size, interaction model, and focus treatment each differ per platform.

- Default: 96×96px square (`--card-sq`), 4-column grid
- Narrow phones (<360px): fall back to 3-column grid
- Tap to toggle selection; tap again to deselect
- Multi-select supported in onboarding preference flows
- Minimum tile must meet `--touch-min` (44px) in both axes — 96px far exceeds this
- Grid gap: 10px minimum — larger gaps cause accidental deselection on swipe

- Wide 160×80px tile preferred — icon + label horizontal layout
- Hover state: `brightness(1.08)` + subtle `scale(1.02)`
- Click to toggle selection; Space or Enter via keyboard
- Focus ring: `var(--focus-shadow)` on `:focus-visible`
- Grid adapts to container width — avoid fixed column counts
- Tooltip on locked tile with Pass upgrade CTA

- 120×120px+ square for 10-foot legibility — label bumped to 14px min
- D-pad navigation — focus memory persists per row when returning from another section
- Focused tile: `var(--tv-focus-shadow)` + `scale(1.06)`
- OK / Select button toggles selection state
- No hover state on TV — focus is the primary interactive signal
- Minimum 8px gap between tiles — D-pad navigation needs clear boundaries
- Never use mini / compact variant on TV — insufficient legibility at distance

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Select toggle | `--ease-out` | `--dur-fast` | border-color, background, transform scale(1.04) |
| Deselect | `--ease-out` | `--dur-fast` | border-color, background |
| Press | `--ease-out` | `80ms` | transform scale(0.95) |
| TV focus | `--ease-out` | `--dur-fast` | transform scale(1.1), box-shadow |
| Appear (staggered) | `--ease-out` | `--dur-fast` | opacity, transform translateY(8px → 0) |

## Accessibility

Genre tiles are interactive selection controls. Every tile needs a role, state, and label that works without visual context.

- `aria-label="[Genre] genre"` — e.g. "Action genre"
- With count badge: `aria-label="Action genre, 48 games"`
- Locked tile: `aria-label="Action — requires JioGames Pass"`

## Related tokens

All design tokens used by genre tiles. Semantic aliases should be preferred in component code over raw primitives.

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-genre-tile` | Root — square tile, surface-1, border-subtle, r4 |
| `.ds-genre-tile--selected` | Green border, jio-soft bg, green icon |
| `.ds-genre-tile__icon` | 32px icon or illustration |
| `.ds-genre-tile__label` | 12px 700 text, centered below icon |
| `.ds-genre-tile--sm` | Small variant — 72×72px |
| `.ds-genre-tile--md` | Default — 96×96px |
| `.ds-genre-tile--lg` | Large — 120×120px |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `label` | string | required | Genre name displayed below icon |
| `icon` | ReactNode | required | Icon or illustration |
| `selected` | boolean | false | Active/selected state |
| `onSelect` | () => void | undefined | Toggle handler |
| `size` | "sm" | "md" | "lg" | "md" | Tile size preset |
| `disabled` | boolean | false | Disable interaction |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div
  role="group"
  aria-label="Select genres"
  style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px"
>
  <button class="genre-tile is-selected" type="button" aria-pressed="true">
    <span class="genre-tile__emoji" aria-hidden="true">⚔️</span>
    <span class="genre-tile__label">Action</span>
  </button>
  <button class="genre-tile" type="button" aria-pressed="false">
    <span class="genre-tile__emoji" aria-hidden="true">🏎️</span>
    <span class="genre-tile__label">Racing</span>
  </button>
  <button class="genre-tile" type="button" aria-pressed="false">
    <span class="genre-tile__emoji" aria-hidden="true">🎯</span>
    <span class="genre-tile__label">Shooter</span>
  </button>
</div>
````

````
document.querySelectorAll('.genre-tile').forEach(tile => {
  tile.addEventListener('click', () => {
    const selected = tile.getAttribute('aria-pressed') === 'true';
    tile.setAttribute('aria-pressed', String(!selected));
    tile.classList.toggle('is-selected', !selected);
  });
});
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--card-sq`
- `--focus-shadow`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--jio-glow`
- `--jio-soft`
- `--overlay-locked`
- `--pill`
- `--r2`
- `--r3`
- `--r4`
- `--skeleton-bg`
- `--state-disabled-opacity`
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

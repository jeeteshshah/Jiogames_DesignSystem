# Rails — JioGames DLS spec

> Source: `rails/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Rails

---

Rails are horizontal-scrolling rows of cards that organize game collections into discoverable, swipeable sections.

Rails let players scan large game catalogs without leaving the current screen. The horizontal orientation creates a natural swipe gesture on touch and a directional browse on TV remotes.

- **Section header** identifies the rail's theme and curation logic in 2–4 words.
- **Cards are sized consistently** within a rail — never mix card widths in one row.
- **Partial card at edge** signals more content is available to the right.
- **Gradient edge fade** reinforces scrollability and maintains the dark aesthetic.
- **Empty / loading states** maintain rail height so layout does not shift.

## When to use

Use when

- Horizontal scrolling game collections on the home screen
- Recommended, trending, and personalised content rows
- Genre or platform groupings within discovery
- "Jump back in" continue-playing rows

Don't use when

- Vertical stacked card lists — use a List or grid
- More than 30 items in a single rail — paginate or use a dedicated screen
- Rails without a title — users need context for why this content is grouped
- Mixing card sizes within a single rail

## Best practices

Follow these rules to keep rails consistent and scannable across the JioGames product surface.

- Use section titles that describe the curation logic ("Because you played X")
- Always show "See all" when the rail has more than 8 items
- Use consistent card sizes within a single rail
- Show loading skeletons at the correct card size
- Use a Continue playing rail for in-progress games

- Mix card sizes within one rail
- Use more than 3 words for "See all" — never "View more items"
- Show empty rails — hide the rail or show a placeholder
- Autoplay video in rail cards
- Use rails on TV without D-pad focus handling

## Anatomy

Every rail is composed of the same core slots. The section header, card row, and gradient edge fade are required; scroll indicators and progress bars are optional enhancements.

## Variants

Five rail types cover the full range of curation needs. Card shape and metadata adapt per variant while the header and scroll pattern stay constant.

## Sizes

Card sizes follow a named scale across platforms. The same size name resolves to different pixel values on Mobile, Web, and TV via CSS token aliases.

## States

Rails respond to five states. Loading and empty states must maintain rail height to prevent layout shift.

## Content

Rail titles and card copy follow a short, direct style to aid scannability in fast-scrolling contexts.

- ·2–4 words, sentence case
- ·"See all" — never "View more" or "View all items"
- ·Describe curation logic: "Because you love Tomb Raider"
- ·Genre tiles: 1–2 words, title case ("Open World")

- ·Title: max 2 lines, 14px bold
- ·Meta: 1 line, 12px muted (genre · rating)
- ·Continue: show "X% complete" in green
- ·Empty: no placeholder text inside card art

## Platform considerations

Each platform has a different interaction model. Scroll affordances and card sizes adapt while the rail structure stays constant.

- Touch-swipe, momentum scrolling
- Hide scrollbar via CSS
- Gradient edge fade right (40px)
- 16px horizontal gutter padding
- Partial 4th card visible as affordance
- Scroll indicator dots optional

- Mouse drag or arrow chevron buttons at edges
- Wider cards — Standard = 220×138
- 40px horizontal gutter
- Hover: scale 1.02, card shadow
- Chevron nav buttons appear on hover
- Keyboard Tab + arrow to navigate

- D-pad focus moves between cards
- Focused card scales 1.05 with glow
- No horizontal scroll on Y-axis nav
- Standard = 320×192
- Focus ring: 3px `var(--jio)`
- Left/right D-pad wraps to adjacent rail

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Scroll (momentum) | `native` | `realtime` | scroll-snap |
| Card hover lift | `--ease-out` | `--dur-fast` | transform scale(1.03) |
| TV focus scale | `--ease-out` | `--dur-fast` | transform scale(1.08) |
| Rail appear (stagger) | `--ease-out` | `--dur-fast` | opacity, transform translateX(-16px → 0) |
| Arrow button press | `--ease-out` | `80ms` | transform scale(0.92) |

## Platform rules

Mobile

- Horizontal scroll with scroll-snap-type: x mandatory
- Card sizes: wide 210×128px; portrait 120×180px
- Peek of next card (24px) visible at right edge
- Scrollbar hidden — momentum scrolling native
- Rail title 16px 700; See All link right-aligned

Web

- Arrow buttons appear on rail hover (left/right edges) for mouse nav
- Keyboard: Tab focuses rail; arrow keys scroll cards
- Cards may be larger (240×150px) with wider gutters on desktop
- Loading: show 5 skeleton cards at standard dimensions

TV

- Horizontal D-pad navigation — Left/Right moves card focus
- Focused card: scale(1.08) + jio-glow ring
- Rail title 20px minimum — readable during D-pad focus state
- At least 5 cards visible simultaneously on TV viewport
- Auto-scroll rail to keep focused card fully visible

## Accessibility

Rails must be fully navigable by keyboard, screen reader, and remote control. Semantic roles ensure scroll regions and cards are correctly announced.

- `role="list"` on the card row container
- `role="listitem"` on each card element
- Rail section: ``

- Tab — moves to the first card in the rail
- Arrow Left / Right — navigate between cards within the rail
- Arrow Up / Down — move focus to the next/previous rail section
- Enter — activates the focused card

## Related tokens

All rail layout values are defined in `tokens/tokens.css`. Change a token once and all rail instances update automatically.

| Token | Value | Swatch | Usage |
|---|---|---|---|
| --card-wide-w | 272px | — | Hero / standard landscape card width |
| --card-sq | 96px | — | Square card side (quick play, genre tile) |
| --card-radius-landscape | 16px | — | Border-radius on landscape cards |
| --card-gap | 12px | — | Gap between cards in a rail |
| --rail-gap | 28px | — | Vertical gap between rail sections |
| --gutter | 20px | — | Left/right page padding (Mobile) |
| --card-overlay | linear-gradient(0deg, rgba(0,0,0,.7), transparent) |   | Text scrim on card art |
| --jio | #00A859 |   | Progress bar, scroll indicator active dot |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-rail` | Root — flex column, gap 12px |
| `.ds-rail__header` | Title row — flex, space-between, align-items center |
| `.ds-rail__title` | 16px 700 text |
| `.ds-rail__see-all` | 13px jio-green link |
| `.ds-rail__track` | Horizontal scroll container — flex row, gap 12px, overflow-x auto, scroll-snap |
| `.ds-rail__track::-webkit-scrollbar` | Hidden scrollbar |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | string | required | Rail section heading |
| `seeAllHref` | string | undefined | Link for "See all" button |
| `cardWidth` | number | 160 | Card width in px for scroll-snap sizing |
| `children` | ReactNode | required | Card elements in the scroll track |
| `loading` | boolean | false | Show skeleton placeholder cards |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<section aria-label="Popular in Mumbai">
  <div class="rail-header">
    <h2 class="rail-title">Popular in Mumbai</h2>
    <button class="btn btn--text btn--xs btn--hug" style="color:var(--jio)">See all</button>
  </div>
  <div class="rail-scroll">
    <div class="card" style="width:160px;flex-shrink:0">...</div>
    <div class="card" style="width:160px;flex-shrink:0">...</div>
    <div class="card" style="width:160px;flex-shrink:0">...</div>
  </div>
</section>
````

````html
<section aria-label="Loading games" aria-busy="true">
  <div class="rail-header">
    <div class="skeleton skeleton--text" style="width:160px;height:18px"></div>
  </div>
  <div class="rail-scroll">
    <div class="skeleton skeleton--card" style="width:160px;height:90px;flex-shrink:0;border-radius:var(--r4)"></div>
    <div class="skeleton skeleton--card" style="width:160px;height:90px;flex-shrink:0;border-radius:var(--r4)"></div>
    <div class="skeleton skeleton--card" style="width:160px;height:90px;flex-shrink:0;border-radius:var(--r4)"></div>
  </div>
</section>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--gold`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r4`
- `--r5`
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

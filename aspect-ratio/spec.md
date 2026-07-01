# Aspect Ratio — JioGames DLS spec

> Source: `aspect-ratio/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Aspect Ratio

---

Utility wrapper that locks a container to a fixed aspect ratio. Critical for game thumbnails, hero images, and video embeds that must not reflow on load.

All five ratios · 16:9 · 4:3 · 1:1 · 3:4 · 2:3

The Aspect Ratio wrapper solves layout shift caused by images and videos that load asynchronously. Without it, the browser renders a container with zero height until the media arrives, then reflowing the entire page — a jarring experience on slow connections. By setting a percentage `padding-top` on the wrapper before the image loads, the correct space is reserved in the layout from the first paint.

- **16:9** — hero banners, video embeds, tournament livestream frames, wide promotional cards
- **3:4** — game cover cards in browse rails and search results (the primary game card format)
- **2:3** — portrait poster cards for featured game spotlights and cinematic promotions
- **1:1** — avatar containers, publisher logos, achievement icons, square thumbnails
- **4:3** — legacy game thumbnails and screenshot previews in game detail galleries

## When to use

Use when

- Game thumbnails and hero images — enforce 16:9 or 4:3 without layout shift
- Video players and embedded media that must maintain proportions
- Cards with image areas where content varies in size
- Skeleton loaders that must match the final image dimensions

Don't use when

- Text-only containers — let content determine height naturally
- UI chrome (buttons, inputs) — fixed heights are more appropriate
- Containers where the ratio is unknown at design time
- TV full-screen hero areas — use fill/cover directly

## Best practices

- Always use the Aspect Ratio wrapper on any image or video container whose dimensions are not fixed in CSS
- Set `object-fit: cover` on the child `` to fill the container without distortion
- Apply `border-radius` to the wrapper, not the child — border-radius inherits via `border-radius: inherit` on `.aspect-ratio__content`
- Use a low-quality placeholder or skeleton with the same ratio while the full image loads
- Serve images at 2× the rendered pixel size for retina displays

- Hard-code a `height` on image containers — the wrapper handles height automatically from width
- Use `object-fit: contain` for game cover art — it adds letterbox bars that break the card grid aesthetic
- Nest an Aspect Ratio wrapper inside another Aspect Ratio wrapper — percentages compound incorrectly
- Skip the wrapper for images "above the fold" — layout shift still occurs on slow connections regardless of position
- Omit `alt` text on the child `` — even decorative images must have `alt=""`

## Anatomy

The wrapper is a single `position: relative` container with a ratio-specific `padding-top` percentage. The child content is absolutely positioned to fill it.

1. 1 Wrapper Required A `position: relative; width: 100%` block with a ratio-specific `padding-top` percentage. This reserves the correct vertical space before content loads. `.aspect-ratio--16-9 { padding-top: 56.25%; }`
2. 2 Content Required A child element with `position: absolute; inset: 0` that fills the wrapper entirely. This is where the ``, ``, or `` lives. `.aspect-ratio__content { position: absolute; inset: 0; object-fit: cover; }`

## Variants

Five ratio variants cover all JioGames image surfaces. Choose the ratio based on the asset format delivered by the content pipeline — never stretch or crop to fit a different ratio.

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| 16:9 | padding-top 56.25% | Game hero, video | All |
| 4:3 | padding-top 75% | Legacy thumbnails | All |
| 1:1 | padding-top 100% | Avatar, icon tile | All |
| 3:4 | padding-top 133% | Cover art portrait | Mobile |

## Use cases by ratio

Each ratio maps to a specific content type in the JioGames asset pipeline. The backend delivers assets at one of these exact dimensions — always match the wrapper ratio to the delivered asset format.

| Ratio | padding-top | Asset dimensions | JioGames usage |
|---|---|---|---|
| 16:9 | `56.25%` | `1920×1080px` | Home hero banner, game detail hero, video embed, tournament stream frame |
| 4:3 | `75%` | `800×600px` | Landscape game thumbnail in horizontal rail, screenshot gallery viewer |
| 1:1 | `100%` | `512×512px` | User avatar, publisher logo, achievement badge, game icon in search result |
| 3:4 | `133.33%` | `720×960px` | Game cover card in browse rail, search grid, recommended section |
| 2:3 | `150%` | `720×1080px` | Featured game portrait poster, cinematic promotional spotlight |

## Content guidance

- Always provide an `alt` attribute on `` children
- For game cover art: `alt="Tomb Raider — game cover"`
- For hero banners with text overlaid: describe the scene, not the text (the text is in HTML)
- For purely decorative backgrounds: `alt=""` — empty string, not omitted
- For avatars: `alt="[Username]'s profile picture"`

- Use `loading="lazy"` on images below the fold to defer network requests
- Use `loading="eager"` (or omit) on hero images above the fold — they should load immediately
- Add a skeleton or blurred placeholder with the same ratio to prevent jarring blank states
- Use `srcset` and `sizes` to serve appropriately sized images at each breakpoint

## Platform considerations

- The wrapper naturally adapts to the full container width — no extra work needed for responsive sizing
- On mobile, 16:9 hero banners typically span full viewport width (`width:100vw`)
- 3:4 cover cards are typically 120–160px wide in horizontal rails
- Use `loading="lazy"` on all below-fold images — mobile networks are frequently constrained

- The CSS `aspect-ratio` property is an alternative on modern browsers — but the padding-top technique has broader legacy support and is the DLS standard
- Use `sizes` attribute to specify breakpoint-aware widths for correct srcset selection
- For video embeds (``), apply `allow="autoplay; fullscreen"` on the iframe, not the wrapper

- Always use this wrapper — never hard-code pixel heights on TV where layout scales with display resolution
- 16:9 is the dominant ratio on TV — it aligns with the display's native format and avoids pillarboxing
- Focus states on card wrappers: `transform: scale(1.05)` + green glow — border-radius must be applied to the wrapper so it scales consistently

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Image load fade | `--ease-out` | `--dur-base` | opacity |
| Skeleton pulse | `linear` | `1400ms infinite` | opacity 1 → 0.4 → 1 |

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Image alt text | `alt="…"` on every `` | Required by WCAG 1.1.1. Decorative images: `alt=""`. Meaningful images: describe the content, not the visual style. |
| Video embeds | Captions and title attribute | Add `title="Game trailer: Tomb Raider"` to ``. Ensure embedded video has closed captions enabled. |
| Wrapper role | No ARIA role needed | The wrapper is a layout container with no semantic meaning. Do not add `role="img"` to the wrapper — place it on the child `` or figure element. |
| Lazy loading | `loading="lazy"` | Lazy loading does not affect accessibility. Screen readers read alt text regardless of load state. Ensure alt is present in the HTML before the image loads. |
| Layout shift (CLS) | Wrapper reserves space | The padding-top technique eliminates CLS for images. This also reduces the risk of content shifting under a focused element, which can disorient keyboard and switch-access users. |

## Related tokens

Aspect Ratio is a layout utility — it uses no color or typography tokens itself. Border-radius is the only visual token applied at the wrapper level.

| Token | Usage in context |
|---|---|
| `--r2` | Small thumbnail corner radius (e.g. icon in a list row) |
| `--r3` | Standard card corner radius — most game cover cards and thumbnails |
| `--r4` | Large card corner radius — hero banners and featured spotlight cards |
| `--r5` | Extra-large — full-bleed hero on game detail page with very rounded corners |
| `--surface-2` | Skeleton / placeholder background fill while image loads |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-aspect-ratio` | Root — sets padding-top to enforce ratio |
| `.ds-aspect-ratio--16-9` | 16:9 ratio (56.25% padding-top) |
| `.ds-aspect-ratio--4-3` | 4:3 ratio (75% padding-top) |
| `.ds-aspect-ratio--1-1` | Square ratio (100% padding-top) |
| `.ds-aspect-ratio__inner` | Absolutely positioned content layer |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `ratio` | number | 16/9 | Width-to-height ratio (e.g. 16/9, 4/3, 1) |
| `children` | ReactNode | required | Content to fill the constrained area |
| `className` | string | undefined | Additional class on the root element |

## Code examples

````html
<div class="aspect-ratio aspect-ratio--16-9" style="border-radius:var(--r4);">
  <img
    class="aspect-ratio__content"
    src="/Assets/horizontal/tomb-raider-thumbnail--gamehero-1920x1080.jpeg"
    alt="Tomb Raider — hero banner"
    loading="eager"
  >
</div>
````

````html
<div class="aspect-ratio aspect-ratio--3-4" style="border-radius:var(--r3); width:120px;">
  <img
    class="aspect-ratio__content"
    src="/Assets/vertical/tomb-raider-thumbnail--cover-720x1080.jpeg"
    alt="Tomb Raider — game cover"
    loading="lazy"
  >
</div>
````

````html
<div class="aspect-ratio aspect-ratio--16-9" style="border-radius:var(--r3);">
  <iframe
    class="aspect-ratio__content"
    src="https://www.youtube.com/embed/VIDEO_ID"
    title="Tomb Raider — official gameplay trailer"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
    frameborder="0"
  ></iframe>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--r3`
- `--r4`
- `--surface-2`
- `--text`
- `--text3`
- `--text4`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

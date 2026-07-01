# Skeleton Loader — JioGames DLS spec

> Source: `skeleton/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Skeleton

---

Animated placeholder shapes that represent loading content before data arrives. Reduces perceived wait time for rails, cards, and game detail.

SHIMMER ANIMATION · SHAPE-MATCHED · SCREEN-READER HIDDEN

## Introduction

When to use skeleton loaders in JioGames.

Use skeleton loaders for content that loads asynchronously: game rails, hero images, profile data, and search results. Skeletons set user expectations by communicating the shape and position of incoming content before the data arrives.

- **Game rails** — show a row of card skeletons while the game list fetches from the API
- **Hero images** — fill the hero banner area with a shape-matched skeleton until the asset loads
- **Profile data** — replace avatar and username areas with appropriate shapes during session load
- **Search results** — render a full skeleton grid before results populate to prevent layout shift

Do **NOT** use skeleton loaders for instant operations under 300ms, navigation transitions (use page transitions instead), or error states. If data fails to load, replace the skeleton with an error state — never leave a skeleton on screen indefinitely.

## When to use

Use when

- Placeholder while content is loading — matches the shape of the final content
- Game rail cards during initial data fetch
- Profile header while user data loads
- List items before API response arrives

Don't use when

- Indefinite loading states with no timeout — add an error state
- Shapes that don't match the real content — creates layout shift on load
- Skeleton for content that loads in under 300ms — flash is worse than no skeleton
- Animated skeleton on TV — reduce motion preference must be respected

## Best Practices

Follow these rules to keep skeleton loaders consistent and accessible across all JioGames surfaces.

- Match skeleton shape exactly to real content — wrong shape causes layout shift on reveal
- Animate all skeletons on the same phase — staggering creates visual noise
- Remove from DOM (not just hide) when content loads — screen readers must not encounter skeleton text
- Use on entire sections, not individual elements — partial skeleton within loaded content is disorienting
- Respect `prefers-reduced-motion` — disable shimmer on TV and reduced-motion environments

- Use skeleton loaders for operations that complete in under 300ms — they cause more anxiety than they resolve
- Leave skeleton elements in the DOM after content has loaded — assistive technology will read them
- Mix skeleton and loaded content in the same rail — show all or nothing
- Use a generic rectangle when the real content is circular or pill-shaped
- Stack multiple skeletons of different animation phases — they must all pulse together

## Anatomy

Skeleton loaders are composed of a shape container and an optional shimmer gradient overlay. No text, icons, or interactive elements are ever placed inside a skeleton.

| Part | Element | Token |
|---|---|---|
| Shape | `div.skeleton` | `background: var(--surface-2)` |
| Shimmer | CSS gradient animation | `var(--surface-2)` → `var(--surface-3)` → `var(--surface-2)` |
| Container | `div.skeleton-group` | No visual style |
| Text line | `div.skeleton.skeleton--text` | `border-radius: var(--pill)` |
| Card | `div.skeleton.skeleton--card` | `border-radius: var(--r4)` |
| Avatar | `div.skeleton.skeleton--avatar` | `border-radius: var(--pill)` |
| Hero | `div.skeleton.skeleton--hero` | `border-radius: var(--r5)` |

## Variants

Four variants cover the primary content shapes in JioGames. Each maps to a specific real-content type and uses the matching border-radius token.

## Sizes

Skeleton sizes derive from the real component they replace. No independent size scale — match the exact dimensions of the target component.

| Context | Width | Height | Radius token |
|---|---|---|---|
| Game cover card | 120px | 160px | `--r4` |
| Game hero banner | 100% | 200px | `--r5` |
| Rail thumbnail | 210px | 128px | `--r4` |
| Text — heading | 50–70% | 18px | `--pill` |
| Text — body | 80–100% | 13px | `--pill` |
| Avatar | 40px | 40px | `--pill` |

## States

Skeleton loaders have two states: loading and loaded. The transition between them must be handled in JavaScript — never CSS visibility alone.

## Content

Skeleton loaders contain no readable text. The shape communicates structure only.

- Keep skeleton shapes empty — no text, no icons, no placeholder labels
- Let shape and position carry all structural meaning
- Use `aria-hidden="true"` so screen readers skip over skeletons entirely

- Never place "Loading…" or any placeholder text inside a skeleton shape
- Do not use `role="img"` or `alt` attributes on skeleton elements
- Do not use animated GIFs or spinner icons as skeleton content

## Platform considerations

Skeleton behavior adapts by platform. Shimmer speed and linger duration vary to suit each surface's performance and viewing context.

- 1.6s shimmer speed — matches natural reading rhythm on small screens
- Full-width rails — skeleton cards should span the same width as real cards including gutters
- Match card aspect ratio exactly — cover cards are portrait, rail thumbnails are landscape
- Remove skeleton from DOM immediately when data resolves — no linger

- Same 1.6s shimmer speed as mobile for consistency
- Wider layout allows multi-column skeleton grids — match the real grid column count
- Skeleton max-width should mirror content max-width constraints
- Use CSS `will-change: background-position` to promote shimmer to GPU

- Disable shimmer animation — use static `background: var(--surface-2)` fill instead
- Shimmer flicker at TV refresh rates can trigger photosensitivity concerns
- Linger skeleton 500ms after data arrives to prevent flicker from near-instant content flash
- TV focus ring must not appear on skeleton elements — they are never focusable

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Shimmer sweep | `linear` | `1400ms infinite` | background-position (gradient slide) |
| Fade to content | `--ease-out` | `--dur-base` | opacity crossfade |

## Accessibility

Skeleton loaders must be invisible to assistive technology while loading, and must announce completion when real content arrives.

| Attribute | Applied to | Guidance |
|---|---|---|
| `aria-hidden="true"` | Every skeleton element | Prevents screen readers from reading the skeleton shape as content. Applied to each `div.skeleton` and `div.skeleton-group`. |
| `aria-busy="true"` | Loading region parent | Signal to assistive technology that the region is updating. Set to `false` (or remove) once content has loaded. Place on the wrapping section, not on individual skeletons. |
| `aria-live="polite"` | Loading region parent | When `aria-busy` resolves and real content is inserted, `aria-live="polite"` causes screen readers to announce the update at the next pause in speech. |
| `aria-label` | Loading region parent | Describe what is loading. Example: `aria-label="Loading games"`. Do not use a generic "Loading" — be specific about the content type. |
| `role="img"` / `alt` | Never | Skeleton shapes must never carry image semantics. They are decorative loading indicators, not meaningful content representations. |

## Related tokens

Use these tokens to implement skeleton styles. Never hardcode hex values — token references stay in sync with theme updates.

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | `#161A24` | Skeleton base fill — the dark resting color of the shimmer gradient |
| `--surface-3` | `#1F2432` | Shimmer highlight — the lighter midpoint of the gradient that creates the sweep effect |
| `--r4` | `8px` | Card and rail thumbnail skeleton border-radius |
| `--r5` | `12px` | Hero banner skeleton border-radius |
| `--pill` | `100px` | Text line and avatar skeleton border-radius — creates the pill shape for inline content |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-skeleton` | Root — surface-2 bg, border-radius matches target, overflow hidden |
| `.ds-skeleton--text` | Text line shape — height 14px, r2, full width by default |
| `.ds-skeleton--circle` | Circular — equal width/height, r-pill |
| `.ds-skeleton--card` | Card-shaped — full width, fixed height |
| `.ds-skeleton--shimmer` | Animated sweep overlay |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | "text" | "circle" | "card" | "custom" | "text" | Shape preset |
| `width` | number | string | "100%" | Skeleton width |
| `height` | number | string | 14 | Skeleton height in px or CSS string |
| `count` | number | 1 | Number of skeleton lines to render |
| `animate` | boolean | true | Enable shimmer animation |
| `borderRadius` | string | undefined | Override border-radius |

## Code examples

Copy these snippets as starting points. Link `tokens/tokens.css` and `components.css` before using component classes.

````
<!-- Text skeleton -->
<div class="skeleton-group" aria-hidden="true">
  <div class="skeleton skeleton--text" style="width:70%"></div>
  <div class="skeleton skeleton--text" style="width:55%"></div>
  <div class="skeleton skeleton--text" style="width:40%"></div>
</div>
````

````
<!-- Card skeleton -->
<div class="skeleton skeleton--card" aria-hidden="true"></div>
````

````
<!-- Loading region with ARIA -->
<section aria-busy="true" aria-live="polite" aria-label="Loading games">
  <div class="skeleton skeleton--hero" aria-hidden="true"></div>
  <div class="skeleton-group" aria-hidden="true">
    <div class="skeleton skeleton--text" style="width:60%"></div>
    <div class="skeleton skeleton--text" style="width:40%"></div>
  </div>
</section>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--card-bg`
- `--jio`
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

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

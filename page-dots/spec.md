# Page Dots — JioGames DLS spec

> Source: `page-dots/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Page Dots

---

Page dots indicate position within a paginated sequence such as hero carousels and onboarding flows.

## Overview

Page dots give players an instant spatial read of their position in a sequence — carousels, onboarding flows, image galleries. The active dot expands into a pill to draw the eye without adding visual weight.

- **Active pill not dot.** Active position uses an expanded pill (20×8px mobile) not a filled dot, for clearer affordance.
- **Minimal footprint.** Dots live below content, never over it. Max 9 dots visible; use overflow clipping beyond that.
- **Carousel use only.** Don't use page dots for vertical scroll position — use a progress bar instead.
- **Auto-advance timing.** When a carousel auto-advances, animate the active pill's width, not just its position.

## Best practices

What to do and what to avoid.

- Use the pill variant (active dot expands) for hero carousels
- Center dot tracks horizontally beneath the carousel
- Keep inactive dots at 8px (mobile) or proportionally smaller
- Use the bar variant for full-width coverage like stories
- Limit to 9 visible dots max; clip or use numbered variant for more
- Animate active state with CSS transition (not JS)

- Don't use same-size dots for active and inactive — loses affordance
- Don't place dots over image content (use semi-transparent overlay region)
- Don't use page dots for vertical pagination
- Don't show dots when there's only 1 page
- Don't animate beyond 200ms — should feel instant not sluggish
- Don't use dots as buttons without adequate 44px touch targets

## Anatomy

The four required parts of every page dots track.

## Variants

Choose the variant that fits the surface density and scroll direction.

## Sizes

Dot dimensions scale across platforms to match interaction modality and viewing distance.

## States

All states a dot track can enter during a user session.

## Content & Motion

There is no text in this component. These specs govern its behaviour.

````
transition: width 200ms cubic-bezier(.22,1,.36,1);
````

- Hide the entire dot track when page count = 1. A single page has no position to indicate.
- Show at 2 or more pages.
- Maximum 9 visible dots. For sequences of 10+ pages, switch to the Numbered variant.

## Platform guidance

Sizes and interaction models differ across Mobile, Web, and TV.

- 8px inactive dots, 20×8px active pill
- 44px touch targets via wrapper `` per dot
- Gap 6px between dots
- Track sits 12px below carousel bottom edge

- Same dot sizes as mobile (20×8px active, 8×8px inactive)
- 32px touch area acceptable — mouse users click precisely
- Mouse hover can preview next slide (cursor: pointer)
- Gap 6px between dots

- 10px inactive, 28×12px active pill
- Gap 8px to aid readability at distance
- Purely visual indicator — not interactive
- D-pad controls slides directly, not the dot track

## Accessibility

Semantic markup and ARIA requirements for interactive and decorative use.

- `role="tablist"` on the dot track wrapper
- `role="tab"` on each individual dot button
- `aria-selected="true"` on the active dot
- `aria-label="Slide 2 of 5"` on each dot button
- Arrow keys navigate between slides; dots are tab stops

- `role="presentation"` on the track
- `aria-hidden="true"` on the entire track
- Announce slide changes via `aria-live="polite"` region elsewhere in layout
- D-pad navigation controls the carousel, not the dots

## Content guidance

### Count

Use page dots for 2–8 slides. Above 8 slides, switch to a numeric indicator ("3 / 12") or remove entirely and rely on gesture affordance.

### Accessible labels

Each dot button needs an aria-label: "Slide 1 of 5", "Slide 2 of 5". The active dot gets aria-current="true".

### Placement

Always centred below the carousel. Do not place inside the carousel content area. Minimum 12px gap from bottom of carousel.

## Related tokens

Design tokens consumed by this component.

## When to use

Use when

- Carousel position indicator below a hero banner or feature carousel
- Onboarding step progress (slide 1 of 4)
- Image gallery position in game detail pages
- Walkthrough step indicators

Don't use when

- More than 8 steps — use a numbered step indicator instead
- Content hidden behind dots that users must see — provide swipe affordance
- As the sole navigation mechanism — pair with swipe gesture

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Active dot expand | `--ease-out` | `--dur-fast` | width (6px → 18px), border-radius |
| Inactive dot shrink | `--ease-out` | `--dur-fast` | width (18px → 6px) |
| Dot transition on slide | `--ease-out` | `--dur-base` | transform translateX, opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-page-dots` | Root — flex row, gap 6px, center aligned |
| `.ds-page-dot` | Single dot — 6px circle, text3 color |
| `.ds-page-dot--active` | Active dot — 18px wide pill, jio-green |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `count` | number | required | Total number of slides/pages |
| `active` | number | required | Current active index (0-based) |
| `onDotClick` | (index: number) => void | undefined | Dot click handler for manual navigation |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div
  class="page-dots"
  role="tablist"
  aria-label="Slide navigation"
>
  <button
    class="page-dot page-dot--active"
    role="tab"
    aria-selected="true"
    aria-label="Slide 1 of 4"
    aria-current="true"
  ></button>
  <button
    class="page-dot"
    role="tab"
    aria-selected="false"
    aria-label="Slide 2 of 4"
  ></button>
  <button
    class="page-dot"
    role="tab"
    aria-selected="false"
    aria-label="Slide 3 of 4"
  ></button>
  <button
    class="page-dot"
    role="tab"
    aria-selected="false"
    aria-label="Slide 4 of 4"
  ></button>
</div>
````

````
const dots = document.querySelectorAll('.page-dot');
const carousel = document.querySelector('.carousel');

function setActiveDot(index) {
  dots.forEach((dot, i) => {
    const active = i === index;
    dot.classList.toggle('page-dot--active', active);
    dot.setAttribute('aria-selected', String(active));
    dot.setAttribute('aria-current', active ? 'true' : 'false');
  });
}

// Call on carousel scroll/swipe
carousel.addEventListener('scroll', () => {
  const index = Math.round(carousel.scrollLeft / carousel.offsetWidth);
  setActiveDot(index);
});
````

## Changelog

Version history for this component.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--jio`
- `--jio-font`
- `--spring`
- `--surface-1`
- `--surface-2`
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

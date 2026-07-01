# Carousel — JioGames DLS spec

> Source: `carousel-component/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Carousel

---

Standalone auto-advancing or manually controlled slide container for featured content, screenshots, and promotional banners. Different from game rails, which are scroll areas.

Carousel · slide 2 of 4 · dot indicator · prev/next arrows

Carousel is a structured slide container with explicit navigation controls. It differs from a game rail (which is a horizontally scrolling list of cards) in that Carousel presents one full-width slide at a time and is designed for featured or promotional content. Each slide has a defined identity — screenshot, banner, or feature announcement — and the user navigates between them deliberately or through auto-advance.

- **Auto-advance** — cycles slides on a 3s interval; pauses on hover or focus
- **Manual** — prev/next arrows plus dot indicators; no auto-advance
- **Screenshot gallery** — thumbnail strip below for direct slide selection
- **Full-bleed** — no border-radius, used inside a card or panel that provides its own frame

- Always show dots or a slide counter — never unlimited slides with no position indicator
- Pause auto-advance on hover, focus, and when the page is not visible (Page Visibility API)
- Cap at 8 slides maximum — more than 8 makes the dot row cognitively costly
- Show thumbnail strip below for screenshot galleries so users can jump to any slide
- Hide prev button on first slide; hide next button on last slide

- Use Carousel for a scrollable list of game cards — use a Scroll Area rail instead
- Loop infinitely without making that behaviour explicit to the user
- Auto-advance faster than 3s — causes motion sickness and prevents reading content
- Place Carousel inside another Carousel — nested slide containers create interaction conflict
- Show more than 8 dots — at that count use a slide counter (2 / 4) instead

1. 1 Carousel track Required Flex row of slides. transform: translateX() drives the slide transition. overflow:hidden on the outer .carousel clips non-active slides. `display:flex; transition:transform 320ms ease-out`
2. 2 Dot indicators Required Active dot stretches to 20px width (pill pill shape) to communicate current position. Inactive dots are 6×6px circles at 35% opacity. Max 8 dots. `width:6px → 20px on active; background:rgba(255,255,255,.35) → var(--text)`
3. 3 Slide counter Optional Text label "2 / 4" in top-right corner. Required when slide count exceeds 8. Updates with aria-live="polite" so screen readers announce position changes. `aria-live="polite" aria-atomic="true"`
4. 4 Slide content overlay Optional Gradient scrim from bottom covers the lower 40% of the slide. Content (label + title) sits inside this zone. Never overlay text on the upper 60% — that area is pure art. `background: linear-gradient(to top, rgba(0,0,0,.7), transparent 60%)`
5. 5 Prev / Next buttons Optional Semi-transparent pill buttons on each side. Hidden (opacity:0) on first/last slide. Web only — mobile uses swipe; TV uses D-pad left/right. `background:rgba(0,0,0,.5); width:40px; height:40px; border-radius:var(--pill)`

## Variants

All variants share the same .carousel base. Behaviour and additional elements (thumbs, auto-advance) are layered on top.

## Sizes

Carousel width is always 100% of its container. Aspect ratio controls the height. Controls scale automatically.

| Aspect ratio | Class modifier | Use case |
|---|---|---|
| 16:9 (default) | none needed | Hero banners, game screenshots, promotional slides |
| 4:3 | `.carousel--4-3` | Older game screenshots, square-ish promo art |
| 21:9 (cinema) | `.carousel--21-9` | Wide cinematic banners, immersive feature showcases |

## States

Carousel state affects auto-advance behaviour and button visibility.

| State | Trigger | Behaviour |
|---|---|---|
| Auto-playing | Default on mount (auto-advance variant) | Advances every 3s. Prev/next buttons visible. Dots update. Counter updates with aria-live. |
| Paused | User hovers or focuses any element inside carousel | Auto-advance timer suspended. Resumes on mouseleave / blur outside carousel. |
| Manual navigation | User clicks prev/next or a dot | Transitions to target slide instantly. Auto-advance resets its 3s timer after interaction. |
| First slide | Current index = 0 | Prev button opacity:0, pointer-events:none. Not removed from DOM — screen readers skip it via disabled. |
| Last slide | Current index = total − 1 | Next button opacity:0, pointer-events:none. Same pattern as first slide. |

## Content guidance

- 3–5 slides is the sweet spot — enough variety without overwhelming the dot row
- Maximum 8 slides before the dot row becomes cognitively costly
- Above 8 slides, replace dots with a numeric counter ("2 / 12")
- Never show a carousel with only 1 slide — use a static hero image instead

- Keep slide titles to 3 words maximum — they appear over artwork in a fixed band
- Label line (genre, tag) maximum 20 characters
- Ensure text contrast against the gradient scrim — always white or --text on dark overlay
- Do not place interactive elements (buttons) inside a slide — the whole slide can be a tap target

## Platform considerations

- Swipe left/right to navigate — no prev/next buttons needed
- Show dots only (no arrow buttons) — they are too small to tap reliably
- Auto-advance is acceptable but pause on any touch interaction
- Use `touch-action: pan-y` on the carousel so vertical scroll still works
- Ensure each slide is a minimum 44px tap target if the whole slide is interactive

- Show prev/next buttons + dots + optional auto-advance
- Pause auto-advance on hover and when document.hidden is true
- Support keyboard: left/right arrow keys navigate slides when carousel is focused
- Thumbnail strip is web-primary — enough screen real estate for the extra row
- All slide and control elements must be reachable via Tab key

- D-pad left/right navigates between slides
- Dots must be large — minimum 12px diameter for 3m legibility
- Active dot should be clearly distinct — use a longer pill (32px) not just color change
- No auto-advance on TV — the remote is slow; users need control
- No thumbnail strip — it is too small at TV scale; use large labeled dots

## Accessibility

| Element | Attribute | Guidance |
|---|---|---|
| Carousel wrapper | `role="region" aria-roledescription="carousel" aria-label` | Announces to screen readers that this is a carousel named by aria-label (e.g. "Game screenshots"). |
| Each slide | `role="group" aria-label="Slide 1 of 4"` | Groups slide content. Non-active slides get aria-hidden="true" so their content is skipped. |
| Prev / Next buttons | `aria-label="Previous slide"` | Icon-only buttons must have descriptive aria-label. Never rely on the arrow character alone. |
| Dot buttons | `role="tab" aria-label="Slide 2" aria-selected` | Treat dots as a tablist. Active dot: aria-selected="true". Inactive: aria-selected="false". |
| Slide counter | `aria-live="polite" aria-atomic="true"` | Screen readers announce position updates without interrupting ongoing speech. |
| Auto-advance | Pause on focus | Animation must pause when any element inside the carousel receives keyboard focus (WCAG 2.1 2.2.2). |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--r5` | `—` | Carousel container border-radius (default) |
| `--pill` | `100px` | Dot border-radius and prev/next button shape |
| `--text` | `#f4f2ee` | Active dot fill color |
| `--border-subtle` | `rgba(255,255,255,.08)` | Prev/next button border |
| `--surface-2` | `—` | Slide placeholder background when no image is loaded |
| `--dur-slow` | `320ms` | Slide transition duration |
| `--dur-fast` | `—` | Dot expansion and button background transition |

## When to use

Use when

- Featured game highlights on the home screen hero area
- Onboarding steps or feature introduction slides
- Image galleries on game detail pages
- Horizontal scrolling when items overflow the viewport

Don't use when

- Primary navigation — carousels hide content from users
- More than 7-8 slides without clear navigation affordance
- Auto-advancing carousels with content users need to read
- Nested carousels

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Swipe slide | `--ease-out` | `--dur-base` | transform translateX |
| Auto-advance | `--ease-in-out` | `--dur-slow` | transform translateX |
| Dot indicator | `--ease-out` | `--dur-fast` | width (active dot expands) |
| Arrow button press | `--ease-out` | `80ms` | transform scale(0.92) |
| Fade transition (alt) | `--ease-out` | `--dur-base` | opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-carousel` | Root — overflow hidden wrapper |
| `.ds-carousel__track` | Flex row of slides — transform driven |
| `.ds-carousel__slide` | Single slide — flex-shrink:0, full width |
| `.ds-carousel__dots` | Dot indicator row — centered below |
| `.ds-carousel__dot` | Individual dot — 6px circle |
| `.ds-carousel__dot--active` | Active dot — expands to 18px width |
| `.ds-carousel__arrow` | Previous/next button |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `autoPlay` | boolean | false | Enable auto-advance |
| `interval` | number | 4000 | Auto-advance delay in ms |
| `loop` | boolean | true | Wrap around at start/end |
| `showDots` | boolean | true | Show dot indicators |
| `showArrows` | boolean | false | Show prev/next arrow buttons |
| `index` | number | undefined | Controlled current slide index |
| `onIndexChange` | (i: number) => void | undefined | Fired on slide change |

## Code examples

````html
<div class="carousel"
     role="region"
     aria-label="Game screenshots"
     aria-roledescription="carousel">

  <div class="carousel-track" id="track">
    <div class="carousel-slide" role="group" aria-label="Slide 1 of 3">
      <div class="carousel-slide-inner">
        <!-- slide content -->
      </div>
    </div>
    <!-- more slides -->
  </div>

  <span class="carousel-count"
        aria-live="polite"
        aria-atomic="true">1 / 3</span>

  <button class="carousel-prev" aria-label="Previous slide" disabled>&#8592;</button>
  <button class="carousel-next" aria-label="Next slide">&#8594;</button>

  <div class="carousel-controls" role="tablist" aria-label="Slides">
    <button class="carousel-dot is-active"
            role="tab"
            aria-label="Slide 1"
            aria-selected="true"></button>
    <button class="carousel-dot"
            role="tab"
            aria-label="Slide 2"
            aria-selected="false"></button>
    <button class="carousel-dot"
            role="tab"
            aria-label="Slide 3"
            aria-selected="false"></button>
  </div>
</div>
````

````
var carousel = document.querySelector('.carousel');
var track    = carousel.querySelector('.carousel-track');
var dots     = carousel.querySelectorAll('.carousel-dot');
var current  = 0;
var total    = dots.length;
var timer    = null;

function goTo(i) {
  current = (i + total) % total;
  track.style.transform = 'translateX(-' + (current * 100) + '%)';
  dots.forEach(function(d, idx) {
    d.classList.toggle('is-active', idx === current);
    d.setAttribute('aria-selected', idx === current ? 'true' : 'false');
  });
}

function start() {
  timer = setInterval(function() { goTo(current + 1); }, 3000);
}

function stop() { clearInterval(timer); }

carousel.addEventListener('mouseenter', stop);
carousel.addEventListener('mouseleave', start);
carousel.addEventListener('focusin',    stop);
carousel.addEventListener('focusout',   start);

document.addEventListener('visibilitychange', function() {
  document.hidden ? stop() : start();
});

start();
````

````html
<div class="carousel" role="region" aria-label="Game screenshots">
  <div class="carousel-track" id="ss-track">
    <div class="carousel-slide" role="group" aria-label="Slide 1 of 4">
      <img class="carousel-slide-inner" src="screenshot-1.jpg" alt="Gameplay showing...">
    </div>
    <!-- more slides -->
  </div>
  <span class="carousel-count" aria-live="polite" aria-atomic="true">1 / 4</span>
</div>

<div class="carousel-thumbs">
  <div class="carousel-thumb is-active"
       tabindex="0" role="button"
       aria-label="View screenshot 1">
    <img src="screenshot-1-thumb.jpg" alt="">
  </div>
  <!-- more thumbs -->
</div>
````

## Changelog

Initial draft. Covers manual, auto-advance, screenshot gallery (thumbnail strip), full-bleed, and fade-transition variants. Aspect ratio sizes documented. Full WCAG carousel pattern implemented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-default`
- `--dur-fast`
- `--dur-sheet`
- `--dur-slow`
- `--ease-emphasized`
- `--ease-out`
- `--jio`
- `--pill`
- `--r4`
- `--r5`
- `--surface-2`
- `--text`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

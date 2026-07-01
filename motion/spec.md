# Motion — JioGames DLS spec

> Source: `motion/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Motion

---

Easing curves, duration tokens, principles, recipes, and governance for JioGames motion across Mobile, Web, and TV. Motion is calm, fluid, spatial, and purposeful — it communicates state, not decoration.

EASING CURVES · DURATION SCALE · REDUCED MOTION READY

## Motion principles

Eight non-negotiable rules. Every implementation decision is tested against these. Use Apple-level restraint as the quality bar — motion so well-matched to the interaction that users never notice it, but would feel its absence.

## Easing tokens

Five named easing curves cover every motion category. Hover each card to see the easing in action.

## Duration tokens

Duration tokens are defined in tokens.css and must be referenced via `var(--dur-*)` — never raw milliseconds in component CSS.

| Token | Value | Purpose | Typical use |
|---|---|---|---|
| --dur-instant | 90ms | Micro-feedback | Tiny tap feedback, ripple, icon state changes |
| --dur-fast | 120ms | Quick response | Press, focus ring, chip select |
| --dur-default | 200ms | Standard UI | Normal component state transitions, fades |
| --dur-pop | 280ms | Pop-in feedback | OTP box fill, check icon appear, dropdowns |
| --dur-slow | 320ms | Deliberate slide | Sheet / drawer / carousel slide, chart reveal |
| --dur-error | 380ms | Error feedback | Shake animations, validation errors |
| --dur-sheet | 400ms | Sheet slides | Bottom sheet open / close |
| --dur-enter | 420ms | Content enter | fade-up, tile-in, stagger entrances |
| --dur-screen | 420ms | Screen transitions | Full screen-to-screen navigation |
| --dur-tv-enter | 560ms | TV focus / enter | D-pad navigation, larger canvas settle |
| --dur-shimmer | 1600ms | Loading loop | Skeleton shimmer loop cycle |
| --dur-icon-spin | 1000ms | Loading loop | Loading icon rotation loop |
| --dur-reduced-fade | 100ms | Reduced motion | Gentle crossfade — NOT collapsed to 0ms |
| --dur-reduced-instant | 1ms | Reduced motion | Snap state change, technically non-zero |
| --stagger-start | 50ms | Stagger | First item delay |
| --stagger-step | 60ms | Stagger | Per-item delay increment (max 6 items) |

### Duration scale — relative lengths

## Movement distance & interactive scale

Translate offsets and feedback scale values are tokenised. Use `var(--move-*)` for translate distances in enter/exit keyframes, and the scale tokens for governed interactive feedback — **never exceed these scale values** (see Soft Landing rules).

| Movement | Value | Use |
|---|---|---|
| --move-sm | 8px | Small offset — toast, tooltip enter |
| --move-md | 20px | Standard fade-up enter (mobile/web) |
| --move-tv | 32px | TV content entrance translate distance |

| Scale | Value | Use |
|---|---|---|
| --scale-press-sm | 0.96 | Small CTA / chip press |
| --scale-press | 0.98 | Card / button press |
| --scale-select | 1.03 | Selection — comes forward |
| --scale-tv-focus | 1.05 | TV focus — spatial shift |

## Motion usage levels (L0–L5)

A taxonomy of how much motion a surface earns. Pick the lowest level that does the job. Higher levels need more justification and stricter token discipline.

| Level | Name | What | When to use | When NOT | Tokens |
|---|---|---|---|---|---|
| L0 | None | No motion at all. Static, instant. | Critical info: pricing, legal, payment totals, OTP digits after entry. | Anything the user must read precisely. | none |
| L1 | Micro feedback | Tap, press, focus, chip select. | Confirm a discrete input immediately. | Ambient or attention-grabbing motion. | `--dur-instant` / `--dur-fast` · `--spring` · `--scale-press` |
| L2 | Component transition | State changes — hover→selected, error, tab switch. | Communicate a component's state change in place. | Page or surface changes. | `--dur-fast` / `--dur-default` · `--spring` (`--spring-bounce` success only) |
| L3 | Surface transition | Sheets, modals, dropdowns, tooltips. | A surface enters or leaves above the current screen. | Full page navigation. | `--dur-sheet` · `--spring` · backdrop fade |
| L4 | Page / flow transition | Screen-to-screen; login, payment, subscription flow steps. | The whole screen changes. | In-place content updates. | `--dur-screen` · `--ease-screen` (TV: `--ease-out` crossfade) |
| L5 | Hero / campaign motion | Hero breathing, marquee, reward celebration, pass unlock. | Cinematic moments, sparingly. | Ever on TV. Routine UI. | §4 ambient constants · `--spring-bounce` one-shot |

## Component motion map

One component, one contracted motion. Do not invent motion per-screen. Reduced-motion behaviour is part of the contract.

| Component | Trigger | Motion | Tokens | Reduced motion |
|---|---|---|---|---|
| Primary button | Press | scale(.97) | `--dur-fast` · `--spring` | None — instant |
| Small CTA | Press | scale(.96) | `--dur-fast` · `--spring` | None — instant |
| Ghost button | Press | opacity .6 | `--dur-fast` | None — instant |
| Icon button | Press | scale(.96) + state tint | `--dur-fast` · `--spring` | Instant tint |
| Action chip | Press | scale(.95) | `--dur-fast` · `--spring` | None — instant |
| Platform chip | Press / select | scale(.95) + selected glow | `--dur-fast` · `--spring` | Instant border change |
| Genre tile | Select | scale(1.03) + glow | `--spring-bounce` · `--dur-fast` | Instant border / glow |
| Tabs | Switch | Active indicator slides | `--dur-default` · `--spring` | Instant switch |
| Card (mobile) | Press | scale(.98) | `--dur-fast` · `--spring` | None — instant |
| Card (web) | Hover | Glow + scale(1.01) | `--dur-default` · `--spring` | Glow only, transform: none |
| Card (TV) | Focus | scale(1.05) + strong glow | `--dur-fast` · `--spring` | Glow stays, transform: none |
| Game card | Launch | scale(.98) + screen crossfade | `--dur-fast` + `--dur-screen` · `--ease-screen` | Instant screen change |
| Subscription / Pass card | Press / select | scale(.98); select glow settle | `--dur-fast` · `--spring` | Instant state; static glow |
| Banner | Enter / dismiss | fade-up enter, fade out | `--dur-enter` · `--spring` (out: `--ease-out`) | Instant show / hide |
| Rail / carousel | Scroll | Native scroll + snap | `scroll-behavior: smooth` | Same |
| Bottom sheet | Open / close | translateY + backdrop fade | `--dur-sheet` · `--spring` | Snap — transition: none |
| Modal / Dialog | Open | scale-from .96 + backdrop fade | `--dur-sheet` · `--spring` | Instant show, backdrop fade only |
| Dropdown | Open | fade + slide-down 8px | `--dur-pop` · `--ease-out` | Instant show |
| Tooltip | Appear | fade + 8px offset | `--dur-default` · `--ease-out` · `--move-sm` | Instant appear |
| Toast | Appear / dismiss | fade-up 8px / fade out | `--dur-default` · `--spring` (out: `--ease-out`) | Instant appear / remove |
| Search | Focus / expand | border + glow; results fade-up | `--dur-fast` / `--dur-default` · `--spring` | Instant border; fade-in results |
| Text input | Focus | border → --jio + glow | `--dur-fast` · `--spring` | Instant border change |
| OTP box | Fill / error | box-pop fill; shake on error | `--dur-pop` · `--spring-bounce` / `--dur-error` · `--ease-error` | Instant tint; static error border |
| Navigation | Screen change | Horizontal slide (TV: crossfade) | `--dur-screen` · `--ease-screen` | Opacity crossfade `--dur-reduced-fade` |
| Skeleton / shimmer | Loading | Shimmer sweep (translateX) | `--dur-shimmer` · linear | Static placeholder — animation: none |
| Progress indicator | Progress | scaleX fill (rotate for spinner) | `--dur-default` / `--dur-icon-spin` · linear | Static / determinate value |
| Badge | — | No entrance motion | none | None |
| Focus ring | Focus | box-shadow appears | `--dur-fast` · `--ease-out` | Glow stays — never removed |
| TV focusable | D-pad focus | Glow + scale(1.05) | `--dur-fast` · `--spring` | Glow stays, transform: none |

## Motion recipes

Sixteen reusable recipes. Keyframe names reference the §13 Keyframe Library — copy them unmodified into prototypes; import the shared library in production.

## Cross-device continuity

Resume and handoff are content states, not motion spectacles.

## Reduced motion

When `prefers-reduced-motion: reduce` is set, duration tokens are overridden in tokens.css. Animation properties themselves are not removed — only their durations, so no layout shifts occur. Reduced motion must feel *designed*, not broken.

````
@media (prefers-reduced-motion: reduce) {
  :root {
    --dur-instant:  0ms;
    --dur-fast:     0ms;
    --dur-default:  0ms;
    --dur-pop:      0ms;
    --dur-slow:     0ms;
    --dur-error:    0ms;
    --dur-enter:    0ms;
    --dur-screen:   0ms;
    --dur-tv-enter: 0ms;
    --dur-sheet:    100ms;
    /* --dur-reduced-fade (100ms) and --dur-reduced-instant (1ms) */
    /* are intentionally NOT collapsed — they are reduced-motion values */
  }
}

/* Ambient loops must be explicitly stopped */
@media (prefers-reduced-motion: reduce) {
  .marquee-row, .hero-bg, .aurora {
    animation: none;
  }
  /* Shimmer: a zero-duration loop still flashes — remove it */
  .shimmer-wrap::after {
    animation: none;
    display:    none;
  }
}
````

## TV motion

TV is a 10-foot UI driven by D-pad. Motion must be larger, slightly slower, and completely restrained. No ambient loops, no press feedback, no sheets.

````
/* TV focus state */
.focusable:focus-visible {
  transform:  scale(var(--scale-tv-focus));
  box-shadow: var(--jio-glow);
  transition: transform var(--dur-fast) var(--spring),
              box-shadow var(--dur-fast) var(--ease-out);
  outline:    none;
}

/* TV content entrance — no stagger */
.tv-card {
  animation: fade-up var(--dur-tv-enter) var(--spring) both;
}
````

## Usage rules

## Motion governance

Standing rules that gate every new pattern. The token mandate is non-negotiable: **if no token exists for a value you need, stop and ask the DLS owner** — do not hardcode.

## Motion QA checklist

Run before every motion review. Grouped by concern — all boxes must check.

- All durations use `var(--dur-*)` tokens
- All easing uses `--spring` / `--spring-bounce` / `--ease-screen` / `--ease-out` / `--ease-error`
- No `transition: all`
- Raw values only inside §13 keyframes or §4 constants

- Every motion has a named cause
- Every motion has a spatial source — nothing appears from nowhere
- Back-navigation reverses the original direction
- Rail scroll position preserved after interaction
- No orphan animations

- Scale limits respected: .96–.98 press, 1.03 select, 1.05 TV focus
- `--spring-bounce` only for one-shot celebration
- `shake` plays once — not looped
- Success settles after one beat
- No bounce or oscillation after state is set

- Only `transform` / `opacity` animated in loops
- Progress bars use `transform: scaleX()`
- Shimmer uses `transform: translateX()` overlay
- No `width`/`height`/`top`/`left` in loops

- TV: no ambient, no press bounce, no backdrop-filter, no stagger
- TV: content entrance uses `--dur-tv-enter`
- Web: hover states exist; keyboard focus has equivalent affordance
- Mobile: haptic pairing intent documented

- Ambient loops stop completely
- Screen transitions become opacity fades
- Stagger collapses to simultaneous fade
- Shimmer becomes static placeholder
- Focus glow is NOT removed
- Error communicates via colour/icon, not motion alone

- No motion on pricing, payment totals, subscription terms
- No motion on legal copy, age or safety warnings
- No motion on OTP digits after entry
- No motion on critical CTAs mid-state-change

- Motion has a clear cause and spatial source
- Settles cleanly — no jello, no sustained bounce
- Does not fight user input or delay task completion
- Reduced motion feels designed, not broken
- Critical info is never communicated by motion alone

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--border-strong`
- `--border-subtle`
- `--card-bg`
- `--divider`
- `--dur-`
- `--dur-default`
- `--dur-fast`
- `--dur-tv-enter`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-3`
- `--jio-bright`
- `--jio-glow`
- `--move-`
- `--negative`
- `--pill`
- `--positive`
- `--r1`
- `--r2`
- `--r3`
- `--r4`
- `--r5`
- `--scale-tv-focus`
- `--space-0-5`
- `--space-1`
- `--space-1-5`
- `--space-2`
- `--space-3`
- `--spring`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--text4`
- `--ultimate`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

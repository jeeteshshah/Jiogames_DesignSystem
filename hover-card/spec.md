# Hover Card — JioGames DLS spec

> Source: `hover-card/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Hover Card

---

Rich preview card that appears when hovering a game title, user mention, or linked entity. Shows contextual info without navigating away.

Lara navigates ancient ruins in Tomb Raider — a survival action-adventure set in a hostile open world.

Hover Card · Game preview above an inline link

Hover cards appear after a 300ms hover delay on a linked entity — a game title, username, or genre tag — and show a rich preview without requiring navigation. They are informational by default (role="tooltip") but can contain a single CTA button for quick actions like "Add to wishlist". Hover cards are web-only; mobile and TV have no hover state.

- **Game preview** — landscape thumbnail, title, genre, rating, 2-line description
- **User profile preview** — avatar, display name, level or stat summary
- **Minimal text** — title and one line of meta, no image, for dense contexts

- Delay show by 300ms on hover-in to prevent accidental triggers on cursor pass-through
- Dismiss instantly on hover-out — no delay on close
- Keep body text to max 3 lines; truncate beyond that with ellipsis
- Keep the card hoverable — cursor moving from link to card must not close it
- Use `role="tooltip"` for info-only cards, `role="dialog"` if card has interactive controls

- Nest a hover card inside another hover card
- Show hover card on mobile or TV — no hover state exists on those platforms
- Use for navigation — hover card is preview only, not a menu
- Load heavy data synchronously — use skeleton until content resolves
- Position card so it clips outside the viewport — flip direction if needed

1. 1 Thumbnail Optional Landscape hero image, 280×120px, `object-fit:cover`. Required for game variant. Omit for minimal or user variants. `width: 100%; height: 120px; object-fit: cover`
2. 2 Title Required 15px bold entity name. Single line, truncate with ellipsis if overflow. `font-size: 15px; font-weight: 700`
3. 3 Meta line Optional 12px muted text. Genre, rating, player count, or other secondary attribute. One line only. `font-size: 12px; color: var(--text3)`
4. 4 Description Optional 13px body copy, max 3 lines (line-height 1.5 ≈ 58px). Truncate with `-webkit-line-clamp: 3`. `font-size: 13px; line-height: 1.5`

## Variants

Three variants cover game, user, and minimal text surfaces. All share the same 280px container and surface tokens.

## Sizes

Hover card width is fixed at 280px across all variants. This is not a configurable size — it ensures consistent preview density and prevents layout jank.

| Property | Value | Notes |
|---|---|---|
| Width | `280px` | Fixed — not configurable |
| Image height | `120px` | Game variant only |
| Avatar size | `56×56px` | User variant only |
| Body padding | `12px 14px` | All variants |
| Hover delay (show) | `300ms` | Prevents accidental triggers |
| Hover delay (hide) | `0ms` | Instant dismiss |

## States

Hover cards have two primary states and one loading sub-state when content is fetched asynchronously.

## Content guidance

- 300ms delay on hover-in — prevents triggers when cursor passes over links
- Instant dismiss on hover-out — no trailing open state
- Card must remain open while cursor is over the card itself
- Focus trigger (keyboard) has no delay — show immediately on focus
- Cancel the timer if cursor leaves before 300ms elapses

- Title: 1 line, max ~30 chars, truncate with ellipsis
- Meta: 1 line, genre + 1 stat, muted color
- Description: max 3 lines, use `-webkit-line-clamp: 3`
- Never nest another hover card inside this card
- Never put navigation links inside the card — it is preview only

## Platform considerations

- **Web only** — hover card does not exist on mobile
- Long-press on a game title opens the game detail sheet instead
- Do not attempt to trigger hover card on touch events
- All content shown in the hover card must be accessible via tap-to-navigate

- Trigger on `mouseenter` after 300ms delay
- Dismiss on `mouseleave` from both link and card
- Keyboard: show on `focus`, dismiss on `blur` or `Escape`
- Flip direction if card clips viewport edge — check on both axes

- **Web only** — hover card does not exist on TV
- Remote control uses D-pad focus — no hover event available
- Game preview info shown in a side panel or full-screen detail view
- Never implement hover-card-like overlays that require pointer input on TV

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| ARIA role | `role="tooltip"` (info-only) or `role="dialog"` (with CTA) | Use tooltip if card has no interactive elements. Use dialog if card has a button. |
| Trigger linkage | `aria-describedby` on link/trigger | Points to hover card id so screen readers announce the preview content. |
| Keyboard trigger | `:focus-within` on wrapper | Card appears immediately on keyboard focus — no 300ms delay for keyboard users. |
| Pointer hoverable | `pointer-events: auto` when visible | WCAG 1.4.13 — user must be able to move cursor onto card without it closing. |
| Escape to dismiss | JS `keydown Escape` | Required by WCAG 1.4.13 for hover-triggered content. |
| Color contrast | All text meets 4.5:1 on surface-2 | `--text` passes at 7.2:1, `--text2` at 4.8:1. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | `#161B26` | Card background |
| `--surface-3` | `#1E2433` | Image placeholder / skeleton background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Card border |
| `--r5` | `16px` | Card border-radius |
| `--dur-base` | `200ms` | Fade-in transition duration |
| `--ease-out` | `cubic-bezier(.2,0,0,1)` | Fade-in easing |
| `--text3` | `rgba(244,242,238,.32)` | Meta line text color |

## When to use

Use when

- Rich game previews on hover over a game title or thumbnail
- User profile previews on hover over avatars in leaderboards
- Extended metadata tooltips for data table cells
- Preview cards for link text in editorial content

Don't use when

- Mobile — hover doesn't exist; use a tap-triggered Popover instead
- Critical information that shouldn't be hidden behind hover
- Auto-playing video or heavy media inside the card
- Forms or interactive controls inside the hover card

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open (delay 300ms) | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Close | `--ease-in` | `--dur-fast` | opacity |
| Image load | `--ease-out` | `--dur-base` | opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-hover-card` | Root floating panel — surface-2, r4, max-w 320px |
| `.ds-hover-card__thumbnail` | Game screenshot or avatar image area |
| `.ds-hover-card__body` | Text content — padding 12px |
| `.ds-hover-card__title` | 14px 700 text |
| `.ds-hover-card__meta` | 12px text3 secondary info |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `trigger` | ReactNode | required | Element that triggers the card on hover |
| `openDelay` | number | 300 | Delay in ms before opening |
| `closeDelay` | number | 100 | Delay in ms before closing |
| `align` | "start" | "center" | "end" | "center" | Horizontal alignment |
| `side` | "top" | "bottom" | "left" | "right" | "bottom" | Preferred side |
| `children` | ReactNode | required | Card content |

## Code examples

````html
<span class="hover-card-wrap">
  <a href="/games/tomb-raider" class="game-link" aria-describedby="hc-tomb">
    Tomb Raider
  </a>
  <div class="hover-card" id="hc-tomb" role="tooltip">
    <img
      class="hover-card-image"
      src="/Assets/horizontal/tomb-raider-thumbnail--gamehero-1920x1080.jpeg"
      alt=""
      aria-hidden="true"
    >
    <div class="hover-card-body">
      <div class="hover-card-title">Tomb Raider</div>
      <div class="hover-card-meta">Action Adventure · ★ 4.9</div>
      <div class="hover-card-desc">
        Survive and fight to become the Tomb Raider you were meant to be.
      </div>
    </div>
  </div>
</span>
````

````html
<span class="hover-card-wrap">
  <a href="/users/raider_lara" class="user-link" aria-describedby="hc-user">@raider_lara</a>
  <div class="hover-card hover-card--user" id="hc-user" role="tooltip">
    <div class="hover-card-body">
      <img class="hover-card-avatar" src="/avatars/lara.jpg" alt="">
      <div class="hover-card-info">
        <div class="hover-card-title">raider_lara</div>
        <div class="hover-card-meta">Level 47 · Action explorer</div>
        <span class="hover-card-stat">🏆 248 games</span>
        <span class="hover-card-stat">⭐ 4.8 avg</span>
      </div>
    </div>
  </div>
</span>
````

````
<script>
document.querySelectorAll('.hover-card-wrap').forEach(wrap => {
  let timer;
  const card = wrap.querySelector('.hover-card');

  wrap.addEventListener('mouseenter', () => {
    timer = setTimeout(() => {
      card.style.opacity = '1';
      card.style.pointerEvents = 'auto';
    }, 300);
  });

  wrap.addEventListener('mouseleave', () => {
    clearTimeout(timer);
    card.style.opacity = '0';
    card.style.pointerEvents = 'none';
  });

  wrap.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      card.style.opacity = '0';
      card.style.pointerEvents = 'none';
      wrap.querySelector('a,button').focus();
    }
  });
});
</script>
````

## Changelog

Initial draft. Three variants (game, user, minimal), fixed 280px width, 300ms show delay, CSS opacity transition, full accessibility table. Web-only — mobile/TV guidance documented as "do not use".

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-base`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--r5`
- `--surface-2`
- `--surface-3`
- `--surface-4`
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

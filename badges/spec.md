# Badges — JioGames DLS spec

> Source: `badges/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Badges

---

Badges are compact indicators that signal status, counts, categories, or premium access.

Badges in context · NEW, LIVE, Count, Status dot, Premium

Badges are non-interactive, overlaid indicators that communicate status, counts, or categories without interrupting a user's flow. They sit on top of or alongside other elements — game cards, icons, rail items — and convey information at a glance. Because they are purely informational, badges should never be tappable. For interactive labels, use Chips instead.

- **Informational** — NEW, LIVE, SALE, HOT signal freshness or real-time state
- **Count / notification** — numeric indicators on icons or avatars showing unread items
- **Status dot** — minimal single-pixel presence indicator (online, active, in-game)
- **Premium / category** — gradient or glass-style labels marking pass access or genre tags

- Keep informational labels to 4 characters or fewer — NEW, LIVE, HOT, TOP, SALE
- Pair a status dot with a visible text label or icon; never rely on color alone to convey meaning
- Display "99+" when a count exceeds 99 — prevent layout overflow and cognitive overload
- Animate the LIVE badge with the pulse animation so users register real-time state at a glance
- Provide a meaningful aria-label on every badge for screen-reader users

- Use badges as interactive controls — they are not buttons; use Chips for tappable labels
- Exceed 4 characters in informational badges — "NEWEST" or "STREAMING" break the pill shape
- Use color as the sole status signal — always add an icon or label alongside any colored dot
- Stack more than 2 badges in the same corner of a card — occludes art and creates visual noise
- Show a count badge with value "0" — hide the badge entirely when there is nothing to report

1. 1 Container shape Required Pill (border-radius: 100px) for informational and count variants. Dot (border-radius: 50%) for status indicator. Shape must remain consistent per variant across all platforms. `border-radius: var(--pill)`
2. 2 Label text or count Required Uppercase text for informational badges (max 4 chars). Numeric string for count badges. No text for dot badges. `font-size: 9px; font-weight: 900; text-transform: uppercase`
3. 3 Dot indicator Optional Used only in the dot/status variant. An 8×8px filled circle — no text, no border. Appears standalone or alongside a label in a list row. `width: 8px; height: 8px; border-radius: 50%`
4. 4 Color fill Optional Semantic background color carries meaning. Green for positive/new, red for live/alert, gradient for premium, glass for genre. Always paired with text or aria-label — never color alone. `background: var(--jio-soft) | var(--negative) | var(--premium-gradient)`

## Variants

All badge variants share the same base pill shape. Each variant has a fixed semantic meaning — do not repurpose colors across variant types.

## Sizes

Badge size scales with context. Most surfaces use the default size. Compact fits count dots on dense icon rows. Large works for hero labels on a game detail page. TV scale ensures legibility at 3-metre viewing distance.

## States

Badges are stateless by nature — they don't have hover, focus, or pressed states. The only behavioral variation is the animated pulse for LIVE, overflow truncation for count, and inactive dimming for status dots.

## Content guidance

Badge copy is one of the highest-density text surfaces in the system. Every character costs proportionally more space. Follow these rules to stay consistent.

- Always uppercase, always max 4 characters
- Write **NEW**, not NEWEST or RECENT
- Write **LIVE**, not STREAMING or AIRING
- Write **HOT**, not POPULAR or TRENDING
- Use genre names (Action, RPG) not descriptors (Fun, Cool)
- Localize label text for regional builds — keep same character limit

- Show numeric value from 1–99 directly: "3", "42", "99"
- When count exceeds 99, always show **99+** — never "100" or higher
- When count is 0, hide the badge entirely — don't show "0"
- Use `aria-label="3 notifications"` not `aria-label="3"`
- Don't pad single digits: "3" not "03"

## Platform considerations

Badges adapt in size and positioning across surfaces. Core semantics stay fixed — only scale and interaction affordances vary.

- Overlay badges use `position:absolute` relative to parent container
- Offset 8px from the nearest edge — never flush to the corner
- Do not obscure the visual center or main focal point of game art
- Limit to 1 overlay badge per card edge (max 2 badges total per card)
- Use default size (3px 7px padding, 9px font)

- Add a `title` attribute or tooltip on hover to expand short labels for accessibility
- Count badges on icon buttons get `aria-live="polite"` when count updates dynamically
- LIVE badge tooltip: "This stream is currently live"
- Cursor remains default (not pointer) — badges are not interactive
- Use default size; large size only on hero/detail page headers

- Always use TV scale (6px 14px padding, 11px font) — default is unreadable at 3m
- Avoid count badges on TV — replace with inline text "3 new" in a list row
- LIVE badge must remain fully visible even when card is in an unfocused state
- Do not use dot-only status on TV — too small; use a colored pill label instead
- Pulse animation is safe for TV — it is slow enough to avoid flicker thresholds

## Accessibility

Badges carry meaning that may not be perceivable to all users. Every badge must provide a programmatic text equivalent — do not rely on visual shape or color alone.

| Variant | Role / attribute | Guidance |
|---|---|---|
| Informational (NEW, LIVE) | `aria-label` | Describe the content state, not just the word. Use `aria-label="New game added"` not `aria-label="NEW"`. |
| Count badge | `aria-label` | Include the noun. `aria-label="3 notifications"` — not just `aria-label="3"`. Use "99 or more notifications" for overflow. |
| LIVE badge | `aria-live="polite"` | Add `aria-live="polite"` to the parent container when LIVE badge appears/disappears dynamically so screen readers announce the state change. |
| Status dot | `role="status"` + visually hidden text | The dot itself has no readable text. Add a visually hidden `Online` sibling. Never use dot color alone for meaning. |
| Premium badge | `aria-label` | `aria-label="JioGames Pass required"` — gradient fill alone does not convey gate status to assistive tech. |
| All variants | Color contrast | All badge text must meet WCAG AA minimum 4.5:1 against badge background. The green-on-dark-green informational style passes at 4.7:1 — do not lighten the background further. |

## Related tokens

Reference these tokens when implementing badge styles. Never hardcode hex values directly — always use the token to stay in sync with theme updates.

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | NEW badge text color, active status dot fill |
| `--jio-soft` | `rgba(0,168,89,.12)` | NEW badge background fill (informational variant) |
| `--negative` | `#FF4757` | Count badge background, LIVE badge background |
| `--premium-gradient` | `linear-gradient(135deg, #00cc65, #00E870)` | Premium badge background fill |
| `--premium-border` | `rgba(0,204,101,.35)` | Premium badge border stroke (optional, use for outlined variant) |
| `--pill` | `100px` | Border-radius for all pill-shaped badge variants |
| `--border-subtle` | `rgba(255,255,255,.08)` | Genre tag background fill (glass/frosted variant) |

## When to use

Use when

- Unread notification counts on tab bar icons or list items
- Status labels on game cards (New, Hot, Live, Sale)
- Pass tier indicators (Mobile Pass, Ultimate Pass)
- Achievement unlock indicators on profile screens

Don't use when

- Long text (more than ~12 characters) — use a chip or label instead
- Critical error messages — use a banner or toast instead
- Decorative only uses without meaningful status information
- Stacking multiple badges on one element — pick the most important

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Count change | `--ease-out` | `--dur-fast` | transform scale(1.3 → 1) |
| Appear | `--ease-out` | `--dur-fast` | transform scale(0 → 1), opacity |
| Dismiss | `--ease-in` | `--dur-fast` | transform scale(1 → 0), opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-badge` | Root badge — pill shape, numeric or short text |
| `.ds-badge--dot` | Dot-only badge (no text, for unread indicator) |
| `.ds-badge--new` | Green "New" label |
| `.ds-badge--hot` | Amber "Hot" label |
| `.ds-badge--live` | Red pulsing "Live" label |
| `.ds-badge--sale` | Purple "Sale" label |
| `.ds-badge--pass` | JioGames Pass tier badge |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `variant` | "default" | "dot" | "new" | "hot" | "live" | "sale" | "pass" | "default" | Visual style |
| `count` | number | undefined | Numeric count — shows "99+" above 99 |
| `max` | number | 99 | Threshold before showing "+" suffix |
| `showZero` | boolean | false | Show badge even when count is 0 |
| `children` | ReactNode | undefined | Element to attach the badge to |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<span class="badge badge--new">New</span>
<span class="badge badge--live">Live</span>
<span class="badge badge--premium">Pass</span>
<span class="badge badge--free">Free</span>
<span class="badge badge--sale">Sale</span>
````

````html
<span style="position:relative;display:inline-flex">
  <svg class="icon icon--m" aria-hidden="true">
    <use href="/sprite.svg#ic_bell"></use>
  </svg>
  <span class="badge-count" aria-label="3 notifications">3</span>
</span>
````

## Changelog

Added `badge-live-pulse` CSS animation for LIVE badge. Added TV scale size tier (6px 14px padding, 11px font-size). Updated accessibility table with `aria-live` guidance for dynamic count badges.

Initial component release. Includes Informational, Count, Status dot, Premium, and Genre tag variants. Default and compact size tiers. Full anatomy documentation and best practices.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--jio-soft`
- `--negative`
- `--pill`
- `--premium-gradient`
- `--text`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

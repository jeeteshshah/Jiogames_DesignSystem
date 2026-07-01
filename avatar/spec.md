# Avatar — JioGames DLS spec

> Source: `avatar/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Avatar

---

User representation through profile images, initials fallback, and online presence indicators. Used in profiles, friend lists, comments, and leaderboards.

XS → XL · IMAGE · INITIALS · PRESENCE INDICATOR

## Introduction

Avatar represents a user or entity across the JioGames platform. Three display modes operate in strict priority order:

1. **Profile image** — renders if a URL is available and loads successfully
2. **Initials** — 1–2 characters derived from the display name, rendered on a surface-3 background
3. **Icon fallback** — generic person icon when no name is available

- **Profile headers** — XL or L size for the primary user identity surface
- **Friend lists** — M size, often paired with an online presence dot
- **Comments & chat** — S size alongside message content
- **Leaderboards** — M size with rank context
- **Notification items** — S size for compact list rows

Do NOT use avatars for game cover art (use the game card thumbnail instead) or brand logos (use the logo component).

## When to use

Use when

- User identity in comments, reviews, leaderboards, and chat
- Profile headers and account settings screens
- Multiplayer lobby participant slots
- Activity feeds showing who did what

Don't use when

- Decorative illustrations — use an image component instead
- More than 5 stacked avatars without a +N overflow indicator
- Sizes smaller than 24px — the fallback initials become unreadable
- As a button on its own without an accessible label

## Best practices

Rules that keep Avatar consistent, accessible, and visually coherent across every context.

- Always provide alt text for image avatars that describes the person — "Profile picture of Arjun" not "avatar image"
- Use a token for initials background — never hardcode a user-specific color
- Treat the online indicator as additive — never replace the avatar with a presence-only icon
- Stack multiple avatars with −8px overlap and a surface-1 ring border to separate them visually
- Use minimum M (40px) on TV — smaller avatars are indiscernible from 10 feet away

- Use avatars for game cover art or brand logos — different components exist for those purposes
- Show XS or S size on TV — too small to read at viewing distance
- Rely on presence color alone — always pair a dot with a label in list rows
- Display a square or non-circular avatar — always use border-radius: var(--pill)
- Hardcode hex values for backgrounds — use design tokens to stay in sync with theme updates

## Anatomy

Every part of the Avatar component and its associated token.

1. 1 Container Required Circular wrapper that clips image or initials. Always pill radius and hidden overflow. `border-radius: var(--pill); overflow: hidden`
2. 2 Initials / Image Required Either an img tag (object-fit: cover) or a centered initials span. Exactly one is rendered at a time. `color: var(--text); font-weight: 700`
3. 3 Initials background Conditional Surface-3 for neutral, --jio for accent. Applied on container, not the span. `background: var(--surface-3) | var(--jio)`
4. 4 Presence dot Optional Absolute-positioned dot at bottom-right. Green for online, text4 for offline. Border punches out from the avatar edge. `background: var(--jio); border: 2px solid var(--bg)`

| Part | Element | Token |
|---|---|---|
| Container | `div.avatar` | `border-radius: var(--pill), overflow: hidden` |
| Image | `img.avatar__img` | `width: 100%; height: 100%; object-fit: cover` |
| Initials | `span.avatar__initials` | `color: var(--text), font-weight: 700` |
| Initials bg | `.avatar--initials` | `background: var(--surface-3)` |
| Presence dot | `span.avatar__presence` | `background: var(--jio), border: 2px solid var(--bg)` |
| Presence offline | `.avatar__presence--offline` | `background: var(--text4)` |
| Ring (stacked) | `.avatar--ring` | `box-shadow: 0 0 0 2px var(--surface-1)` |

## Variants

Four display modes in priority order. All share the same circular container and size system.

## Sizes

Five sizes cover every context from dense notification rows to full profile pages. Presence dot scales proportionally.

| Name | Size | Font | Presence dot | Usage |
|---|---|---|---|---|
| XS | 24px | 9px | — | Dense lists, notification dots |
| S | 32px | 12px | 6px | Comments, chat |
| M | 40px | 15px | 8px | Friend lists, leaderboards |
| L | 48px | 18px | 10px | Profile headers |
| XL | 64px | 22px | 12px | Full profile page |

## States

Avatar supports five states. Presence states are additive — they layer on top of the base avatar without replacing it.

## Content guidance

Rules for deriving initials from display names across scripts and naming patterns.

- Use the first letter of the first name + first letter of the last name — "Arjun Sharma" → "AS"
- Single-name users: use the first two letters — "Priya" → "PR"
- Non-Latin scripts: use 1 character only
- Never truncate initials to nothing — fall back to the icon if no characters are available
- Max 2 characters always — never show 3 or more

- Image avatars: describe the person — "Profile picture of Arjun" not "avatar image"
- Initials avatars: put the full name on the container `aria-label`
- Icon fallback: use `aria-label="Unknown user"`
- Presence dot: `aria-label="Online"` or `aria-label="Offline"`
- Stacked overflow: `aria-label="N more users"` on the overflow bubble

## Platform considerations

Avatar adapts its minimum size and interaction affordances per platform. Core structure and tokens stay fixed.

- XS–XL all valid sizes; M is the most common
- Presence dot always 8px at M size
- Tap target for avatar links must be minimum 44×44px
- Stacked groups: max 4 visible avatars + overflow chip
- No tooltip needed — full name shown in adjacent text

- Same size range as mobile; M most common in rails
- Hover shows a tooltip with the full display name
- Presence dot 8px by default; scale with avatar size
- Cursor: default — avatar is not inherently interactive
- Focus ring on interactive avatars (links/buttons): 2px jio outline

- Minimum M (40px) — no XS or S permitted
- Presence dot 10px minimum for legibility at 10 feet
- Focus/hover ring: var(--jio) glow — `box-shadow: 0 0 0 3px var(--jio), 0 0 20px rgba(0,200,100,.4)`
- Tooltip not applicable — show name as on-screen text label
- XL preferred for profile header on TV detail pages

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Image load fade | `--ease-out` | `--dur-base` | opacity |
| Presence ring pulse | `ease-in-out` | `2s infinite` | box-shadow scale |
| Hover scale | `--ease-out` | `--dur-fast` | transform scale(1.05) |
| Focus ring | `instant` | `0ms` | outline |

## Accessibility

Avatar must convey identity and presence to screen readers without relying on color or visual shape alone.

| Variant | Role / attribute | Guidance |
|---|---|---|
| Image avatar | `alt` on img | Describe the person: `alt="Profile picture of Arjun Sharma"` |
| Initials avatar | `aria-label` on container | Put full name on the container div; add `aria-hidden="true"` to the initials span |
| Icon fallback | `aria-label` on container | Use `aria-label="Unknown user"`; SVG icon gets `aria-hidden="true"` |
| Presence indicator | `aria-label` on dot span | `aria-label="Online"` or `aria-label="Offline"` — never rely on color alone |
| Stacked group | `aria-label` on overflow chip | Use `aria-label="4 more users"`; group wrapper can use `role="group"` |
| All variants | Color contrast | Initials text must meet WCAG AA 4.5:1 against its background. Green-on-black passes; white-on-surface-3 passes. |

## Related tokens

Always use these tokens — never hardcode hex values.

| Token | Usage |
|---|---|
| `--surface-3` | Initials background (neutral) |
| `--jio` | Initials background (accent) / online presence dot |
| `--text4` | Offline / away presence dot |
| `--text` | Initials text color on neutral background |
| `--pill` | Avatar border-radius (always circular) |
| `--bg` | Presence dot border color — punches dot out from avatar edge |
| `--surface-1` | Ring border for stacked avatar overlap separation |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-avatar` | Root — circular container with overflow hidden |
| `.ds-avatar--sm` | 24×24px |
| `.ds-avatar--md` | 36×36px (default) |
| `.ds-avatar--lg` | 48×48px |
| `.ds-avatar--xl` | 64×64px |
| `.ds-avatar__fallback` | Initials or icon shown when image fails |
| `.ds-avatar--online` | Green presence ring |
| `.ds-avatar--offline` | Grey presence ring |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `src` | string | undefined | Image URL |
| `alt` | string | required | Accessible description of the user |
| `fallback` | string | ReactNode | undefined | Shown when image fails to load |
| `size` | "sm" | "md" | "lg" | "xl" | "md" | Diameter preset |
| `presence` | "online" | "offline" | "none" | "none" | Presence ring color |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css`.

````
<!-- Image avatar with alt -->
<div class="avatar avatar--m">
  <img class="avatar__img" src="profile.jpg" alt="Profile picture of Arjun Sharma">
</div>
````

````
<!-- Initials avatar + online indicator -->
<div class="avatar avatar--m avatar--initials" aria-label="Priya Nair">
  <span class="avatar__initials" aria-hidden="true">PN</span>
  <span class="avatar__presence" aria-label="Online"></span>
</div>
````

````
<!-- Stacked avatar group (3 users + overflow) -->
<div class="avatar-group">
  <div class="avatar avatar--s avatar--initials avatar--ring" aria-label="User A">
    <span class="avatar__initials" aria-hidden="true">A</span>
  </div>
  <div class="avatar avatar--s avatar--initials avatar--ring" aria-label="User B">
    <span class="avatar__initials" aria-hidden="true">B</span>
  </div>
  <div class="avatar avatar--s avatar--initials avatar--ring avatar--overflow" aria-label="4 more users">
    <span class="avatar__initials" aria-hidden="true">+4</span>
  </div>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--jio`
- `--jio-font`
- `--pill`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text-inv`
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

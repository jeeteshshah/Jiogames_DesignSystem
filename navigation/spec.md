# Navigation — JioGames DLS spec

> Source: `navigation/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Navigation

---

Navigation provides the persistent wayfinding structure that helps players move between JioGames surfaces.

Navigation defines how players orient themselves and move through JioGames. Unlike individual components, navigation is a system — it governs which surfaces exist, how they relate, and how players transition between them.

- **Hierarchy.** Three tiers: global nav (always visible), section nav (contextual), in-page nav (local tabs or anchors).
- **Platform.** Web uses a persistent top bar; mobile uses a bottom tab bar; TV uses a d-pad-traversable side rail.
- **State.** Every nav item has default, hover (web), active/selected, and disabled states.
- **Context.** Active state always reflects current location. Back navigation preserves scroll position.

## When to use

Use when

- Primary app-level navigation between 3-5 top-level screens
- Tab bar at the bottom on mobile (Home, Browse, Library, Profile)
- Side nav on web for persistent top-level wayfinding

Don't use when

- More than 5 top-level destinations — creates cognitive overload
- Secondary/contextual navigation — use tabs, segmented control, or breadcrumbs
- Navigation items without icon and label — icons alone are ambiguous

## Best practices

Follow these rules to keep navigation consistent and reliable across the JioGames product surface.

- Use max 5–6 nav items in top nav
- Use noun labels (Home not Go Home)
- Keep active indicator visible at all times
- Ensure 44px minimum touch targets on mobile
- Use persistent nav — never hide on scroll on web
- Highlight the active section clearly with color and indicator

- Don't use icon-only nav items without labels on mobile
- Don't exceed 6 items in a single nav surface
- Don't change nav structure between authenticated and unauthenticated states beyond hiding locked items
- Don't use nav as a CTA surface — keep CTAs in right-slot buttons
- Don't rely on color alone for active state

## Anatomy

The web top nav bar is the most anatomically complete navigation surface — it contains all six parts. Mobile and TV use subsets of this structure.

## Variants

Four navigation patterns cover all JioGames surfaces. Each is adapted for its platform context.

1. [JioGames](#)
2. ›
3. [Games](#)
4. ›
5. Action

## Platform matrix

Navigation dimensions, active indicators, and item limits differ per platform. Use token aliases; never hardcode raw pixel values in component CSS.

## States

Every nav item across platforms responds to the same interaction states. Hover exists only on web. TV Focused uses the TV glow ring exclusively — no hover.

## Content

Nav labels and item counts are load-bearing decisions. Every word and every destination shapes how players understand the product.

- Use nouns not verbs (Home not Go Home)
- Capitalize first letter only
- Keep to 1 word where possible
- Avoid abbreviations — spell out full destination name
- Match the label to what the section contains, not what you want users to do

- Max 5 tabs on mobile bottom bar
- Max 6 links in web top nav
- Prioritize most-used destinations — analytics-informed
- Surface Pass/Store as CTA button not a nav item
- Hide locked items; don't disable them (disabled implies coming soon)

## Platform considerations

Each platform enforces different constraints. Navigation that works on web may be completely unusable on TV or inaccessible on mobile.

- Bottom tab bar is primary nav — never top nav
- 5 tab maximum — strictly enforced
- Icons + labels required on every tab
- Tab bar height `var(--tab-bar-h)` 64px
- Safe area inset bottom applied (`env(safe-area-inset-bottom)`)
- No hover states — only press and active

- Persistent sticky top nav — never hides on scroll
- Hamburger hidden at ≥768px breakpoint
- Pill tab group or underline tabs supported
- Hover states on all interactive items
- CTA button in rightmost slot, one maximum
- Frosted glass treatment: `backdrop-filter: blur(12px)`

- Side rail navigation replaces top bar entirely
- D-pad traversal — vertical movement through rail items
- `var(--tv-focus-shadow)` glow mandatory on focus
- No hover states — D-pad has no pointer
- Labels always visible alongside icons
- Focus moves vertically; select with OK/Enter

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Tab switch | `--ease-out` | `--dur-fast` | indicator translateX |
| Active indicator | `--ease-out` | `--dur-fast` | width, opacity |
| Icon press | `--ease-out` | `80ms` | transform scale(0.88 → 1) |
| Badge update | `--ease-out` | `--dur-fast` | transform scale(1.3 → 1) |
| Tab bar hide (scroll) | `--ease-in` | `--dur-base` | transform translateY(100%) |
| Tab bar show | `--ease-out` | `--dur-base` | transform translateY(0) |

## Platform rules

Mobile

- Tab Bar at bottom: 56px height, 3–5 items, icon + label
- Active indicator: jio-green icon and label color
- Tab bar hides on downward scroll, reveals on upward scroll
- Badge count overlays icon — 44×44px tap target per item

Web

- Top horizontal nav bar or left sidebar depending on app complexity
- Keyboard: Tab navigates items; Enter/Space activates
- Active route: jio-green underline or filled background indicator
- Breadcrumbs used on secondary pages alongside primary nav

TV

- Left sidebar nav — always visible, D-pad Left enters nav from any screen
- Nav items: 64px height, 32px icons, 18px+ labels
- Focus moves left into nav, right exits nav to content
- Selected item: jio-green fill background on the nav item

## Accessibility

Navigation must be fully operable by keyboard, screen reader, and D-pad on all platforms. These requirements are not optional.

- `` wrapping element on all nav surfaces
- `role="list"` for nav item group where ``/`` is not used
- Mobile tab bar: `role="tablist"` with `aria-label="Main navigation"`

- Tab / Shift+Tab cycles through all nav items
- Enter / Space activates the focused item
- Current page item receives `aria-current="page"`
- Never trap keyboard focus inside nav — Tab must always move out

- `aria-label` on all icon-only buttons (search, notification, hamburger)
- `aria-expanded="true/false"` on hamburger menu toggle
- Screen reader announces active section via `aria-current`
- Hidden nav drawer must use `aria-hidden="true"` + `tabindex="-1"` on all children

- Focus ring always visible — never suppress `:focus-visible`
- TV uses `var(--tv-focus-shadow)` — mandatory glow ring on every focusable item
- Skip-to-content link placed before nav: `[Skip to content](#main)`

## Related tokens

Use these token aliases in all navigation component CSS. Never hardcode raw hex or pixel values.

| Token | Value | Role |
|---|---|---|
| --app-bar-h | 64px | App bar / nav bar height |
| --tab-bar-h | 64px | Bottom tab bar height (mobile) |
| --status-bar-h | 44px | Status bar height (safe area) |
| --touch-min | 44px | Minimum touch target size |
| --jio | #00A859 | Active item color, active indicator, logo wordmark |
| --text3 | #6B7280 | Default / inactive nav item text color |
| --border-subtle | rgba(255,255,255,.08) | Nav bar bottom border, TV rail separator |
| --jio-font | JioType | Nav label font family |
| --tv-focus-shadow | 0 0 0 2px var(--jio) | TV D-pad focus ring on nav items — mandatory |
| --glass-1 | rgba(255,255,255,.05) | Web nav item hover background |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-tab-bar` | Root — fixed bottom, full width, surface-1, border-top |
| `.ds-tab-bar__item` | Single tab — flex column, center, flex:1 |
| `.ds-tab-bar__icon` | 24px icon — text3 default, jio active |
| `.ds-tab-bar__label` | 10px 700 — text3 default, jio active |
| `.ds-tab-bar__item--active` | Active state — jio icon + label |
| `.ds-tab-bar__badge` | Unread count badge over icon |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | NavItem[] | required | Tab definitions with icon, label, href |
| `activeItem` | string | required | Active tab identifier |
| `onItemChange` | (id: string) => void | required | Tab switch handler |
| `badge` | Record | undefined | Badge counts keyed by item id |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<nav class="ds-nav" aria-label="Main navigation">
  <a href="/home" class="ds-nav-link is-active" aria-current="page">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_home"></use></svg>
    Home
  </a>
  <a href="/games" class="ds-nav-link">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_games"></use></svg>
    Games
  </a>
  <a href="/search" class="ds-nav-link">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_search"></use></svg>
    Search
  </a>
</nav>
````

````html
<nav aria-label="Breadcrumb">
  <ol style="display:flex;align-items:center;gap:6px;list-style:none;padding:0;margin:0">
    <li><a href="/" style="color:var(--text3);text-decoration:none;font-size:12px">Home</a></li>
    <li aria-hidden="true" style="color:var(--text4);font-size:12px">/</li>
    <li><a href="/games" style="color:var(--text3);text-decoration:none;font-size:12px">Games</a></li>
    <li aria-hidden="true" style="color:var(--text4);font-size:12px">/</li>
    <li><span aria-current="page" style="color:var(--text);font-size:12px;font-weight:700">War Thunder</span></li>
  </ol>
</nav>
````

## App bar

The app bar is the top-fixed chrome of every screen. It contains the back button, screen title, and contextual actions. It is a sub-pattern of Navigation — not a separate component.

### Anatomy

| Layer | Token / class | Notes |
|---|---|---|
| Container height | `var(--app-bar-h)` — 56px | Excludes status bar. Sticky, z-index: var(--z-appbar). |
| Status bar spacer | `var(--safe-top)` | iOS safe area. Android status bar height via window.statusBarHeight. |
| Background (default) | `var(--bg)` | Opaque on inner pages. Transparent on home/cinematic screens. |
| Background (scrolled) | `var(--overlay-scrim)` + blur(14px) | Frosted glass on scroll. @supports guard for blur. |
| Back button | `var(--icon-size-base)` — 24px icon | Chevron-left or platform back arrow. |
| Title | Body bold / `font-weight:700` | Single line, truncated with ellipsis. |
| Actions | Max 2 icon buttons right-aligned | 48×48px touch target. |

### Variants

### Scroll behaviour

Home and cinematic screens use scroll-aware app bar. Three states based on scroll position and direction. An 8px jitter guard prevents class thrashing on rubber-band scrolls.

````css
.app-bar {
  position: sticky;
  top: 0;
  z-index: var(--z-appbar);
  height: var(--app-bar-h);
  transition: transform var(--dur-default), background var(--dur-default), backdrop-filter var(--dur-default);
  /* reduced-motion override */
  @media (prefers-reduced-motion: reduce) {
    transition: none;
  }
}
.app-bar.header-scrolled {
  background: var(--overlay-scrim);
  @supports (backdrop-filter: blur(1px)) {
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    background: rgba(6,8,15,.6);
  }
}
.app-bar.header-hidden {
  transform: translateY(-110%);
}
````

````
const bar = document.querySelector('.app-bar');
let lastY = 0;

window.addEventListener('scroll', () => {
  const y = window.scrollY;
  const delta = y - lastY;

  if (Math.abs(delta) < 8) return; // jitter guard

  if (y < 80) {
    bar.classList.remove('header-scrolled', 'header-hidden');
  } else if (delta < 0) {
    bar.classList.add('header-scrolled');
    bar.classList.remove('header-hidden');
  } else {
    bar.classList.add('header-hidden');
    bar.classList.remove('header-scrolled');
  }

  lastY = y;
}, { passive: true });
````

### Platform behavior

Mobile

- Status bar spacer via `var(--safe-top)`
- Back swipe gesture replaces back button on iOS
- Scroll-hide on home only
- 56px height canonical

Web

- No status bar spacer
- Back = browser back or explicit back link
- Sticky top-0 with z-appbar
- May include global search in bar

TV

- No scroll-hide — TV doesn't scroll vertically like mobile
- Back = remote Back button. Always available.
- TV safe-area inset: `var(--tv-safe)` = 48px
- Larger touch targets: min 64px

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--app-bar-h`
- `--bg`
- `--border`
- `--border-subtle`
- `--dur-default`
- `--glass-1`
- `--gold`
- `--icon-size-base`
- `--jio`
- `--jio-3`
- `--jio-font`
- `--overlay-scrim`
- `--pill`
- `--r3`
- `--r4`
- `--safe-top`
- `--status-negative`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--tab-bar-h`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`
- `--text4`
- `--tv-focus-shadow`
- `--tv-safe`
- `--z-appbar`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

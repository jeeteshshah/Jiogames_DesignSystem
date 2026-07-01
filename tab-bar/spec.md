# Tab Bar — JioGames DLS spec

> Source: `tab-bar/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Tab Bar

---

The tab bar provides persistent bottom navigation on mobile, giving players one-tap access to core JioGames destinations.

Mobile bottom tab bar · 393px · 4 tabs

The tab bar is the primary navigation surface on mobile. It gives players immediate access to the four core JioGames destinations without leaving their current context. The tab bar is always visible — it never scrolls away, collapses, or hides.

- **Persistent.** Always visible at bottom of screen. Uses `position: sticky` with safe-area-inset-bottom.
- **4 tabs.** Home, Games, Store, Profile. The four fixed destinations. Sub-sections surface inside each tab, not as additional tabs.
- **Icon + label.** Both required on mobile. Icon-only tabs are not permitted.
- **Active state.** One tab is always active. Active tab shows green icon, green bold label, and a green indicator dot above the icon.

## Best Practices

- Always show icon + label on mobile
- Keep to 4 tabs: Home, Games, Store, Profile
- Use the active indicator (green dot above icon) consistently
- Ensure 44px minimum tap targets
- Apply safe-area-inset-bottom padding on iOS
- Use nouns as labels: Home, Games, Store, Profile

- Don't hide the tab bar on scroll
- Don't use icons without labels on mobile
- Don't add a 5th tab — use a menu drawer instead
- Don't use verbs as tab labels (Browse, Find, Save)
- Don't show tab bar on TV — use sidebar nav rail
- Don't use the tab bar for contextual sub-navigation

## Anatomy

The mobile tab bar consists of a container housing 5 tab items. Each item carries an icon, a label, and when active, a green indicator dot above the icon.

## Variants

Three layout variants for different use cases and platforms.

Note: Use only on web — labels are required on mobile.

## Sizes / Platform Matrix

How the tab bar dimensions adapt per platform.

| Property | Mobile | Web | TV |
|---|---|---|---|
| Tab bar height | 64px `var(--tab-bar-h)` | 48px (inline in header) | N/A |
| Tab item height | 64px | 48px | N/A |
| Icon size | 24px `var(--icon-size-base)` | 20px | N/A |
| Label font | 10px / weight 700 active | 12px | N/A |
| Touch target | 44px min | 40px | N/A |
| Safe area | `env(safe-area-inset-bottom)` | none | none |

## States

Tab items have five states. Hover is web-only. Disabled is used when a tab is locked behind auth or a feature flag.

- 1 word preferred
- Nouns only — not verbs
- `Home` not Homepage
- `Games` not Browse
- `Store` not Shop or Buy
- `Profile` not Me or Account

- 4 tabs minimum
- 4 tabs maximum: Home, Games, Store, Profile
- If a destination doesn't fit in 5, hide it in a profile/menu drawer
- Pass and promotions go in the hero or as floating CTAs
- Never add a "More" tab or exceed 4 tabs

- Primary nav pattern — always rendered
- `position: sticky; bottom: 0`
- Safe area padding — env(safe-area-inset-bottom)
- 4 tabs — Home, Games, Store, Profile — icon + label required
- Haptic feedback on tap

- Rendered as horizontal tab group in page header
- Pill or underline style — not a bottom bar
- Hover states supported
- Can accommodate up to 6 items
- No safe area padding needed

## Accessibility

Tab bar requires correct ARIA roles, keyboard navigation, and visible focus rings on web.

- `` wrapping element
- Each tab is a `` or `` with `role="tab"`
- `aria-current="page"` on the active tab

- Tab / Shift+Tab to move focus between tabs
- Enter / Space activates a focused tab
- Only active tab has `tabindex="0"` — others use `-1`

- `aria-label` with full name on icon-only tabs
- Badge count: `aria-label="Profile, 3 notifications"`
- Hide decorative icons from screen readers with `aria-hidden="true"`

- 2px focus ring using `var(--jio)` color
- Minimum 44px touch target on mobile
- No hover-only states on mobile — keyboard + focus must work

## Related Tokens

| Token | Value | Usage |
|---|---|---|
| `--tab-bar-h` | 64px | Tab bar height |
| `--icon-size-base` | 24px | Tab icon size |
| `--icon-color-default` | rgba(255,255,255,.45) | Inactive icon color |
| `--icon-color-active` | #00A859 | Active icon color |
| `--touch-min` | 44px | Minimum touch target |
| `--negative` | #FF4757 | Badge / notification color |
| `--jio` | #00A859 | Active label and indicator |
| `--safe-bot` | env(safe-area-inset-bottom) | Bottom safe area |

## When to use

Use when

- Primary bottom navigation on mobile: Home, Browse, Library, Profile
- 3-5 top-level destinations that users switch between frequently
- Persistent navigation visible on every main screen

Don't use when

- More than 5 items — visual crowding, use Drawer overflow
- Secondary in-page navigation within a screen — use Tabs component
- Navigation items that are rarely used — move to Profile/Settings
- Hiding the tab bar on scroll for content that needs navigation

## Variants

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Mobile | 56px height, 24px icons | Primary mobile nav | Mobile |
| Web top bar | 48px height, 20px icons | Web app top nav | Web |
| TV | 72px height, 32px icons | TV primary nav | TV |

## States

Default (inactive)

Icon and label at text3 color; no indicator

Active

Icon and label turn jio-green; indicator dot or underline

Hover

Slight background tint; cursor pointer

Pressed

Icon scales down to 0.88 momentarily on tap

With badge

Count badge overlays icon top-right

Badge cleared

Badge animates out on read/clear action

Hidden (scroll)

Translated 100% down; revealed on scroll-up

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Active indicator slide | `--ease-out` | `--dur-fast` | transform translateX |
| Icon press bounce | `--ease-out` | `--dur-fast` | transform scale(0.85 → 1.1 → 1) |
| Badge count pop | `--ease-out` | `--dur-fast` | transform scale(1.4 → 1) |
| Tab bar hide | `--ease-in` | `--dur-base` | transform translateY(100%) |
| Tab bar show | `--ease-out` | `--dur-base` | transform translateY(0) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-tab-bar` | Root — fixed bottom 0, full width, 56px height, surface-1, border-top |
| `.ds-tab-bar__item` | Single tab — flex column, center, flex:1, gap 3px |
| `.ds-tab-bar__icon` | 24px SVG — text3 inactive, jio active |
| `.ds-tab-bar__label` | 10px 700 — text3 inactive, jio active |
| `.ds-tab-bar__item--active` | Active state — jio icon and label |
| `.ds-tab-bar__badge` | Count badge — position absolute, top-right of icon |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | TabItem[] | required | Tab definitions: id, label, icon, badge |
| `active` | string | required | Active tab id |
| `onChange` | (id: string) => void | required | Tab switch handler |
| `hideOnScroll` | boolean | false | Hide bar when scrolling down, show on up |

## Platform rules

Mobile

- Fixed at bottom — 56px height, safe area inset respected
- Items: flex:1 equal width; icon centered above label
- Hides on scroll down within content; reveals on scroll up
- Max 5 items — more items require overflow/more menu pattern

Web

- Top horizontal position or left sidebar depending on viewport
- Keyboard: Tab navigates items; Enter/Space activates
- Active underline or filled background indicator
- Badge count shown as superscript on icon

TV

- Left sidebar nav replaces bottom tab bar on TV
- Items: 72px height; 32px icons; 18px labels
- D-pad Up/Down navigates; OK enters section; Left re-enters nav from content
- Active item: jio-green full background fill on the sidebar row

## Accessibility

### ARIA attributes

| Attribute | Element | Value / notes |
|---|---|---|
| `role="tablist"` | Tab bar container | Identifies the navigation as a tab list |
| `role="tab"` | Each tab item | Individual tab button |
| `aria-selected` | Active tab | "true" on current tab, "false" on others |
| `aria-controls` | Each tab | ID of the associated tab panel (screen content) |
| `aria-label` | Tab bar | "Main navigation" or "App navigation" |
| `tabindex` | Tabs | 0 on active tab, -1 on inactive (roving tabindex) |

### Keyboard interaction

| Key | Action |
|---|---|
| Tab | Enter tab bar; focus active tab |
| Arrow Left/Right | Navigate between tabs |
| Enter / Space | Activate focused tab |
| Home / End | Jump to first/last tab |

### Guidelines

- Uses roving tabindex — only active tab is in tab order; arrows navigate others
- Screen reader announces: "Home, tab, 1 of 4, selected"
- Badge count announced as part of tab label: "Library, 3 new items, tab"
- Tab panels (screen content) need aria-labelledby pointing to their tab

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<nav class="tab-bar" role="navigation" aria-label="Main navigation">
  <a href="/home" class="tab-bar__item is-active" aria-current="page">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_home"></use></svg>
    <span class="tab-bar__label">Home</span>
  </a>
  <a href="/games" class="tab-bar__item">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_games"></use></svg>
    <span class="tab-bar__label">Games</span>
  </a>
  <a href="/store" class="tab-bar__item">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_store"></use></svg>
    <span class="tab-bar__label">Store</span>
  </a>
  <a href="/profile" class="tab-bar__item">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_user"></use></svg>
    <span class="tab-bar__label">Profile</span>
  </a>
</nav>
````

````html
<a href="/profile" class="tab-bar__item">
  <span style="position:relative;display:inline-flex">
    <svg class="icon icon--m" aria-hidden="true"><use href="/sprite.svg#ic_user"></use></svg>
    <span class="badge-count" aria-label="3 notifications">3</span>
  </span>
  <span class="tab-bar__label">Profile</span>
</a>
````

## Changelog

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border-subtle`
- `--gold`
- `--icon-color-default`
- `--icon-size-base`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--surface-1`
- `--surface-2`
- `--tab-bar-h`
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

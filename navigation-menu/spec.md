# Navigation Menu — JioGames DLS spec

> Source: `navigation-menu/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Navigation Menu

---

Horizontal top-level navigation for web contexts. Contains primary sections with optional dropdown sub-menus. Not used on Mobile or TV — use Bottom Nav / D-pad sidebar instead.

Navigation Menu · Home active, Games dropdown open with genre group

Navigation Menu is the primary horizontal navigation bar for JioGames web. It surfaces the top-level sections of the product and optionally exposes sub-sections via keyboard- and mouse-triggered dropdowns. It is web-only — Mobile uses a Bottom Navigation Bar and TV uses a D-pad–navigable sidebar. Do not render this component in mobile or TV contexts.

- **Simple links** — flat nav items with no dropdown. Each item is an anchor or button with `aria-current="page"` on the active section.
- **With dropdown** — trigger opens a floating panel with sub-items. Max 8 items per dropdown. Section headers allowed.
- **With icon + text** — 16px leading icon alongside label. Use sparingly for high-value sections (Pass, Profile).
- **Compact** — tighter padding, 13px font. For secondary nav bars or sub-headers.

- Keep top-level items to a maximum of 6. More than 6 adds cognitive load and crowds the bar.
- Mark the active page with `aria-current="page"` and the green `is-active` color.
- Group dropdown items with section headers when there are more than 4 options in a category.
- Close dropdowns on Escape, on outside click, and on focus leaving the nav entirely.
- Use `` element with a descriptive `aria-label` — "Main navigation".

- Use Navigation Menu on Mobile — render the Bottom Navigation Bar instead.
- Use Navigation Menu on TV — render the D-pad sidebar instead.
- Go deeper than 2 levels — no dropdowns inside dropdowns.
- Put more than 8 items in a single dropdown — split into grouped sections or a new top-level item.
- Use only icon without text for top-level items — icon + label is required at this level.

1. 1 Active trigger Required 14px / weight 600 / `var(--jio)`. Marks the current page. Use `aria-current="page"` on the element. `color: var(--jio); aria-current="page"`
2. 2 Dropdown trigger Optional Trigger with trailing chevron. `aria-haspopup="true"` and `aria-expanded` communicate dropdown state. Chevron rotates 180° when open. `aria-haspopup="true" aria-expanded="true/false"`
3. 3 Nav container Required `` wrapping a flex row. `role="menubar"` for full ARIA menu pattern. `aria-label="Main navigation"`. ``
4. 4 Dropdown item Optional 14px / weight 500. Can be `` or ``. Hover: `var(--glass-1)` background. Active: `var(--jio)` text. `role="menuitem" inside role="menu"`

## Variants

All variants share the same horizontal flex container. Dropdown and icon presence are the only structural differences.

## Sizes

Two sizes. M is the default for primary nav bars. L for prominent marketing or landing page navigation.

## States

Top-level triggers have 5 states. Dropdown items have their own hover and active states.

## Content guidance

Max 6 top-level items. Dropdown max 8 items. Section grouping with headers allowed in dropdowns. Never more than 2 levels deep.

- 1–2 words, title case. "Home", "Games", "Pass", "Profile".
- Maximum 6 items. Extras should merge into an existing section or be demoted to a sub-page.
- Keep labels short enough that the bar never wraps to two lines on a 1280px viewport.
- The active page label should always be visible without scrolling or opening a dropdown.

- Max 8 items per dropdown. Use section headers to group 5+ items.
- Separator (`.nav-menu-dropdown-sep`) between groups when headers are not used.
- Never place a dropdown inside a dropdown — max depth is 2 levels.
- Dropdown items should be destinations (pages) not actions — actions belong in a toolbar or menu.

## Platform considerations

- Do not render Navigation Menu on mobile viewports.
- Use Bottom Navigation Bar for primary sections on mobile.
- If a page has secondary sub-sections, use Tabs — not a horizontal nav bar.
- Hide via CSS at breakpoint or render a separate mobile nav component.

- Primary platform for this component.
- Keyboard: Tab enters nav, Arrow Left / Right moves between top-level items, Arrow Down opens dropdown, Escape closes dropdown and returns focus to trigger.
- Dropdowns close on outside click and on focus leaving the entire `` element.
- Position nav bar at the top of the viewport, sticky if the page scrolls.

- Do not render Navigation Menu on TV.
- Use a D-pad–navigable left sidebar for primary sections on TV.
- Horizontal nav bars are inaccessible with a TV remote at 3m viewing distance.
- TV navigation must support spatial focus — sidebar pattern satisfies this.

## Accessibility

Implements the WAI-ARIA Menu Button / Menubar pattern. Full keyboard operability required.

| Element | Role / attribute | Guidance |
|---|---|---|
| Nav wrapper | `` + `role="menubar"` | Landmark element with `aria-label="Main navigation"`. Multiple navs on a page must each have a unique label. |
| Top-level trigger | `role="menuitem"` | Add `aria-current="page"` to the active item. Triggers with dropdowns also need `aria-haspopup="true"` and `aria-expanded`. |
| Dropdown container | `role="menu"` | Appears when trigger `aria-expanded="true"`. Must be a sibling or child of the trigger's parent so focus management works. |
| Dropdown item | `role="menuitem"` | Can be `` or ``. Arrow Down / Up navigates. Enter / Space activates. Escape closes and returns focus to trigger. |
| Active page | `aria-current="page"` | Applied to the top-level trigger for the current route. Never apply to dropdown items — only to top-level section triggers. |
| Keyboard flow | Arrow keys | Arrow Left / Right between top-level items. Arrow Down opens dropdown and moves into it. Escape closes dropdown. Tab exits nav entirely. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Active trigger color, dropdown active item color |
| `--text2` | `rgba(244,242,238,.55)` | Default trigger label color |
| `--text` | `#f4f2ee` | Trigger hover label color |
| `--text3` | `rgba(244,242,238,.32)` | Chevron icon color |
| `--text4` | `rgba(244,242,238,.2)` | Dropdown section header color |
| `--glass-1` | `rgba(255,255,255,.04)` | Trigger hover background, dropdown item hover |
| `--surface-2` | — | Dropdown panel background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Dropdown panel border, section separator |
| `--r3` | `8px` | Trigger and dropdown item border-radius |
| `--r5` | `16px` | Dropdown panel border-radius |
| `--dur-fast` | `120ms` | Trigger hover and chevron transitions |

## When to use

Use when

- Mega-nav on desktop web with expandable sub-sections
- Web app top navigation with hover-reveal sub-pages
- Breadcrumb-style wayfinding in multi-level content hierarchies

Don't use when

- Mobile primary navigation — use Tab Bar + Drawer
- Simple flat navigation with no sub-sections — use a standard menu/nav
- More than 3 levels of hierarchy — restructure information architecture

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Sub-menu open | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Sub-menu close | `--ease-in` | `--dur-fast` | opacity |
| Active indicator | `--ease-out` | `--dur-fast` | transform translateX, width |
| Item hover | `--ease-out` | `80ms` | background |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-nav-menu` | Root flex row container |
| `.ds-nav-menu__trigger` | Top-level nav item with chevron |
| `.ds-nav-menu__content` | Sub-menu panel — surface-2, r4, shadow |
| `.ds-nav-menu__item` | Sub-menu row item |
| `.ds-nav-menu__link` | Plain nav link without sub-menu |
| `.ds-nav-menu__indicator` | Active underline indicator |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | NavMenuItem[] | required | Nav item tree with optional children |
| `value` | string | undefined | Controlled open sub-menu identifier |
| `onValueChange` | (value: string) => void | undefined | Open state change handler |
| `orientation` | "horizontal" | "vertical" | "horizontal" | Layout direction |

## Code examples

````html
<nav class="nav-menu" role="menubar" aria-label="Main navigation">
  <div class="nav-menu-item">
    <button class="nav-menu-trigger is-active"
            role="menuitem" aria-current="page">Home</button>
  </div>
  <div class="nav-menu-item">
    <button class="nav-menu-trigger" role="menuitem">Games</button>
  </div>
  <div class="nav-menu-item">
    <button class="nav-menu-trigger" role="menuitem">Pass</button>
  </div>
  <div class="nav-menu-item">
    <button class="nav-menu-trigger" role="menuitem">Profile</button>
  </div>
</nav>
````

````html
<div class="nav-menu-item">
  <button class="nav-menu-trigger"
          role="menuitem"
          aria-haspopup="true"
          aria-expanded="false"
          aria-controls="games-menu"
          id="games-trigger">
    Games
    <svg class="nav-menu-chevron" aria-hidden="true">
      <!-- chevron-down -->
    </svg>
  </button>

  <div class="nav-menu-dropdown"
       role="menu"
       id="games-menu"
       aria-labelledby="games-trigger"
       hidden>
    <div class="nav-menu-dropdown-header">Genre</div>
    <a class="nav-menu-dropdown-item" href="/games/action" role="menuitem">Action</a>
    <a class="nav-menu-dropdown-item" href="/games/adventure" role="menuitem">Adventure</a>
    <a class="nav-menu-dropdown-item" href="/games/racing" role="menuitem">Racing</a>
    <div class="nav-menu-dropdown-sep"></div>
    <div class="nav-menu-dropdown-header">Platform</div>
    <a class="nav-menu-dropdown-item" href="/games/mobile" role="menuitem">Mobile games</a>
    <a class="nav-menu-dropdown-item" href="/games/browser" role="menuitem">Browser games</a>
  </div>
</div>
````

````html
<nav class="nav-menu" role="menubar" aria-label="Main navigation">
  <div class="nav-menu-item">
    <button class="nav-menu-trigger is-active" role="menuitem"
            aria-current="page" style="gap:6px;">
      <svg width="14" height="14" aria-hidden="true"><!-- home icon --></svg>
      Home
    </button>
  </div>
  <div class="nav-menu-item">
    <button class="nav-menu-trigger" role="menuitem"
            aria-haspopup="true" aria-expanded="false"
            aria-controls="games-dd" style="gap:6px;">
      <svg width="14" height="14" aria-hidden="true"><!-- games icon --></svg>
      Games
      <svg class="nav-menu-chevron" aria-hidden="true"><!-- chevron --></svg>
    </button>
    <div class="nav-menu-dropdown" role="menu" id="games-dd" hidden>
      <a class="nav-menu-dropdown-item" href="#" role="menuitem">Action</a>
      <a class="nav-menu-dropdown-item" href="#" role="menuitem">RPG</a>
    </div>
  </div>
  <div class="nav-menu-item">
    <button class="nav-menu-trigger" role="menuitem" style="gap:6px;">
      <svg width="14" height="14" aria-hidden="true"><!-- pass icon --></svg>
      Pass
    </button>
  </div>
</nav>
````

## Changelog

Initial draft. Web-only. Simple links, dropdown, icon+text, and compact variants. M and L sizes. Full WAI-ARIA menubar pattern documentation. Platform exclusion guidance for Mobile and TV.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg2`
- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--r3`
- `--r4`
- `--r5`
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

# Menubar — JioGames DLS spec

> Source: `menubar/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Menubar

---

Horizontal bar of menus typically seen in desktop/web app shells. In JioGames web, used in the admin/CMS tools and game developer dashboard. Not for the player-facing UI.

Menubar · Edit menu open · New Game / Duplicate / separator / Export / Delete (disabled)

The Menubar component renders a horizontal strip of top-level menu triggers. Clicking a trigger opens a dropdown menu with items, separators, keyboard shortcuts, and optional checkmarks. It is a desktop/web pattern used exclusively in JioGames internal tooling — the CMS, game developer dashboard, and admin panels. It must never appear in the player-facing app on any platform.

- **File, Edit, View, Help** — the four standard top-level menus for JioGames tooling
- **Keyboard shortcuts** — shown right-aligned within each menu item
- **Checked items** — checkmark for toggle state (e.g., View → Show Sidebar)
- **Submenus** — indicated by › arrow; max one level of nesting

- Limit to 4 top-level menus maximum — File, Edit, View, Help covers all CMS needs
- Show keyboard shortcuts right-aligned on every item that has one
- Use separators to group related items — max 3 items per group before a separator
- Close the open menu when any other trigger is hovered, matching native OS menubar behavior
- Keep menu item labels to 2–3 words — "New Game", "Export CSV", "Show Sidebar"

- Use the menubar in the player-facing JioGames app — it is CMS and developer tooling only
- Nest submenus more than one level deep — two arrows to reach an action is too many
- Put destructive actions (Delete, Unpublish) at the top of a group — place them last, after a separator
- Use the menubar on mobile — it has no touch equivalent; use a drawer or bottom sheet instead
- Add more than 8 items to a single menu without grouping them with separators

1. 1 Menubar strip Required 36px tall horizontal bar. Surface-1 background with bottom border. Contains all top-level triggers flush left. Fixed to top of tool shell. `height: 36px; background: var(--surface-1); role="menubar"`
2. 2 Menu trigger Required 28px tall button, 13px weight-500. Transparent default, glass-1 on hover/open. No chevron — click behavior is self-evident in a menubar context. `height: 28px; font-size: 13px; role="menuitem" aria-haspopup="menu"`
3. 3 Menu panel Required Floating surface-2 panel, 4px padding, border-radius r4, elevation shadow. Minimum 180px wide. Appears 4px below the trigger. `background: var(--surface-2); role="menu"`
4. 4 Menu item Required Full-width button, 13px weight-500. Label left, shortcut right in monospace. Hover fills glass-1. Checked items show green text. Disabled at 35% opacity. `role="menuitem" | role="menuitemcheckbox"`

## Variants

Four menu item configurations covering all common CMS tool needs.

## Sizes

The menubar has a single fixed height — 36px bar, 28px triggers, 13px font. No size variants exist.

| Element | Spec | Notes |
|---|---|---|
| Menubar height | `36px` | Fixed — aligns with OS-native menubar proportions |
| Trigger height | `28px` | 4px margin above and below within 36px bar |
| Trigger font | `13px / 500` | Not adjustable — smaller than 13px is unreadable on web |
| Menu item font | `13px / 500` | Same as trigger — visual consistency |
| Menu min-width | `180px` | Wider menus grow to fit longest item label + shortcut |
| Menu item padding | `7px 10px` | 7px vertical gives ~34px total item height |

## States

States apply to individual triggers and menu items. The menubar strip itself has no state — it is always visible and always at full opacity.

## Content guidance

- Use the menubar only in CMS, developer dashboard, and admin tools
- Standard four menus: **File**, **Edit**, **View**, **Help**
- Never exceed 4 top-level menus — consolidate into submenus if needed
- File menu: New, Open, Save, Export, Close
- Edit menu: New Game, Duplicate, Publish, Unpublish, Delete

- Labels: 2–3 words, title case — "New Game", "Export CSV", "Show Sidebar"
- Shortcuts: use OS notation — ⌘N for Mac, Ctrl+N for Windows shown separately
- Destructive items (Delete, Unpublish) go last in their group, after a separator
- Checked items: use checkmark glyph ✓ in green — not a checkbox component

## Platform considerations

- Not applicable — menubar is web/desktop only
- Mobile CMS access uses a drawer navigation pattern instead
- Actions available in menubar are surfaced via bottom sheet on mobile

- Arrow keys move between top-level triggers (←→) and within open menus (↑↓)
- Enter or Space opens a trigger's menu; Enter activates a menu item
- Escape closes the open menu and returns focus to the trigger
- Hovering a second trigger while one is open switches the open menu immediately

- Not applicable — menubar is CMS/developer tooling, not TV player UI
- TV apps use a focusable rail navigation pattern instead

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Menubar strip | `role="menubar"` | `aria-label="Application menu"`. Contains only menuitem children. |
| Menu trigger | `role="menuitem"` | `aria-haspopup="menu"`, `aria-expanded="true/false"` when menu opens/closes. |
| Menu panel | `role="menu"` | `aria-label` matching trigger label — "Edit menu". Contains only menuitem/menuitemcheckbox/separator children. |
| Standard item | `role="menuitem"` | Keyboard shortcut in a visually-hidden or `aria-keyshortcuts` attribute so screen readers announce it. |
| Checked item | `role="menuitemcheckbox"` | `aria-checked="true/false"`. The checkmark glyph is `aria-hidden="true"` — role carries the meaning. |
| Separator | `role="separator"` | No text content, no aria-label needed. Purely structural. |
| Disabled item | `aria-disabled="true"` | Do not use the HTML `disabled` attribute — that removes the item from tab order entirely. Use `aria-disabled` so it remains discoverable. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-1` | — | Menubar strip background |
| `--surface-2` | — | Menu panel background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Menubar bottom border, menu panel border, separator |
| `--glass-1` | `rgba(255,255,255,.05)` | Trigger hover/open fill, menu item hover fill |
| `--text2` | `rgba(244,242,238,.55)` | Default trigger label color |
| `--text3` | `rgba(244,242,238,.32)` | Keyboard shortcut text color |
| `--jio` | `#00A859` | Checked menu item text color and checkmark glyph color |
| `--r3` | — | Trigger border-radius, menu item border-radius |
| `--r4` | — | Menu panel border-radius |
| `--dur-fast` | `120ms` | Trigger and item hover background transition |

## When to use

Use when

- Desktop web app top menu (File, Edit, View style navigation)
- Admin dashboard primary navigation for complex tooling
- Web-only utility bars with grouped command menus

Don't use when

- Mobile — no space, use Tab Bar or Bottom Sheet actions instead
- Simple apps with fewer than 3 menu groups — a Toolbar suffices
- Replacing primary game navigation — menubar is a utility pattern

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Menu open | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Menu close | `--ease-in` | `--dur-fast` | opacity |
| Item hover | `--ease-out` | `60ms` | background |
| Trigger active | `--ease-out` | `80ms` | background |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-menubar` | Root bar — flex row, surface-1, border-bottom |
| `.ds-menubar__trigger` | Menu title button — 36px height, px 10 |
| `.ds-menubar__trigger--open` | Active open state — glass-1 bg |
| `.ds-menubar__content` | Dropdown panel — surface-2, r3, shadow |
| `.ds-menubar__item` | Menu row — 36px, padding 0 10px |
| `.ds-menubar__item--disabled` | 38% opacity |
| `.ds-menubar__separator` | 1px border-subtle divider |
| `.ds-menubar__shortcut` | Keyboard shortcut label — text3, monospace |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | MenubarMenu[] | required | Array of menu group definitions |
| `onSelect` | (value: string) => void | undefined | Item selection handler |

## Code examples

````html
<div class="menubar" role="menubar" aria-label="Application menu">

  <div class="menubar-item">
    <button class="menubar-trigger" role="menuitem"
      aria-haspopup="menu" aria-expanded="false"
      aria-controls="menu-file">
      File
    </button>
    <div id="menu-file" class="menubar-menu" role="menu" aria-label="File menu" hidden>
      <button class="menubar-menu-item" role="menuitem" aria-keyshortcuts="Meta+N">
        <span>New Game</span>
        <span class="shortcut" aria-hidden="true">⌘N</span>
      </button>
      <button class="menubar-menu-item" role="menuitem" aria-keyshortcuts="Meta+S">
        <span>Save</span>
        <span class="shortcut" aria-hidden="true">⌘S</span>
      </button>
      <div class="menubar-separator" role="separator"></div>
      <button class="menubar-menu-item is-disabled" role="menuitem" aria-disabled="true">
        <span>Delete</span>
      </button>
    </div>
  </div>

  <div class="menubar-item">
    <button class="menubar-trigger" role="menuitem"
      aria-haspopup="menu" aria-expanded="false"
      aria-controls="menu-edit">
      Edit
    </button>
    <div id="menu-edit" class="menubar-menu" role="menu" aria-label="Edit menu" hidden>
      <!-- items -->
    </div>
  </div>

</div>
````

````html
<div id="menu-edit" class="menubar-menu" role="menu" aria-label="Edit menu">
  <button class="menubar-menu-item" role="menuitem" aria-keyshortcuts="Meta+N">
    <span>New Game</span>
    <span class="shortcut" aria-hidden="true">⌘N</span>
  </button>
  <button class="menubar-menu-item" role="menuitem" aria-keyshortcuts="Meta+D">
    <span>Duplicate</span>
    <span class="shortcut" aria-hidden="true">⌘D</span>
  </button>
  <div class="menubar-separator" role="separator"></div>
  <button class="menubar-menu-item" role="menuitem" aria-keyshortcuts="Meta+E">
    <span>Export</span>
    <span class="shortcut" aria-hidden="true">⌘E</span>
  </button>
  <button class="menubar-menu-item is-disabled" role="menuitem" aria-disabled="true">
    <span>Delete</span>
    <span class="shortcut" aria-hidden="true">⌫</span>
  </button>
</div>
````

````html
<div id="menu-view" class="menubar-menu" role="menu" aria-label="View menu">

  <!-- Checked: sidebar is visible -->
  <button class="menubar-menu-item is-checked" role="menuitemcheckbox"
    aria-checked="true" aria-keyshortcuts="Meta+B">
    <span style="display:flex; align-items:center; gap:6px;">
      <span aria-hidden="true" style="width:14px; color:var(--jio);">✓</span>
      Show Sidebar
    </span>
    <span class="shortcut" aria-hidden="true">⌘B</span>
  </button>

  <!-- Unchecked: preview is hidden -->
  <button class="menubar-menu-item" role="menuitemcheckbox"
    aria-checked="false" aria-keyshortcuts="Meta+P">
    <span style="display:flex; align-items:center; gap:6px;">
      <span aria-hidden="true" style="width:14px;"></span>
      Show Preview
    </span>
    <span class="shortcut" aria-hidden="true">⌘P</span>
  </button>

</div>
````

## Changelog

Initial draft. Basic menubar, shortcuts variant, checked items variant. Full ARIA menubar pattern documented. Web-only scope — CMS and developer dashboard exclusively.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--ctrl-h-sm`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--r3`
- `--r4`
- `--r5`
- `--surface-1`
- `--surface-2`
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

# Dropdown Menu — JioGames DLS spec

> Source: `dropdown-menu/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Dropdown Menu

---

Click-triggered menu anchored below a button. Used for "More options", account menus, and kebab menus on cards and list items.

Dropdown Menu · Kebab trigger, right-anchored

Dropdown menus open on click (not hover) and anchor below the button that triggered them. They are the standard pattern for "More options" kebab buttons (⋯), account avatar menus, and primary buttons with option variants. Unlike context menus — which are right-click triggered and position-anchored — dropdown menus are always tied to a specific button in the UI.

- **Kebab menu** — ⋯ button on game cards, list rows, and player tiles
- **Account menu** — avatar button in the app header, opens profile + settings actions
- **Sort / filter** — "Sort by ▾" button with a list of sorting options
- **Button with options** — primary "Download ▾" split into format variants

- Use chevron (▾) for buttons whose label changes with selection; kebab (⋯) for fixed item-level actions
- Focus the first item automatically when opened via keyboard
- Close on Escape and return focus to the trigger
- Show active state with a leading ✓ checkmark for selection menus
- Flip anchor to left-aligned if trigger is near the right viewport edge

- Open dropdown on hover — hover is for tooltips, click is for menus
- Use dropdown for navigation links that change the page URL — use a nav component
- Mix section headers with ungrouped items in the same menu
- Show dropdown on mobile — replace with bottom sheet
- Stack two dropdowns open simultaneously — new trigger closes the previous

1. 1 Trigger button Required The button that opens the menu. Must have `aria-haspopup="menu"` and toggle `aria-expanded` true/false. `aria-haspopup="menu" aria-expanded="false"`
2. 2 Section header Optional 11px uppercase label grouping items beneath it. Used when the menu has 2+ distinct categories. Not interactive — no role="menuitem". `font-size: 11px; text-transform: uppercase; color: var(--text3)`
3. 3 Active item Optional Currently selected option in a selection menu. Leading ✓ checkmark in `--jio` color. Used for sort/filter menus only. `color: var(--jio); content: '✓'`
4. 4 Standard item Required 14px medium weight button. 9px 12px padding. Optional leading icon (16px). Optional trailing meta (11px muted). Full-width. `padding: 9px 12px; border-radius: var(--r3)`
5. 5 Destructive item Optional Same structure as standard item but text uses `--negative`. Red-tinted hover. Always last after a separator. `color: var(--negative); hover: rgba(255,71,87,.08)`

## Variants

Five variants cover the full range of dropdown use cases from item-level actions to account navigation.

## Sizes

Two size tiers. Default for standard surfaces. Compact for dense toolbars and list rows where item height must stay minimal.

## States

The trigger button carries open/closed state. Individual items carry hover, active, disabled, and destructive states.

## Content guidance

- Dropdown = click-triggered, anchored to a fixed button in the UI
- Context menu = right-click triggered, anchored to pointer coordinates
- Use kebab (⋯) for item-level actions — stays visible, no right-click needed
- Use chevron (▾) on a labeled button when the button label reflects the selection
- Never use dropdown for global navigation — use nav bar or drawer

- Verb-first: "Edit profile", "Download game", "Sign out"
- Sentence case, no trailing punctuation
- Section headers: noun-only, uppercase, max 2 words ("Account", "Support")
- Active checkmark only in selection menus (sort, filter) — not action menus
- Destructive label names the consequence: "Sign out" not just "Exit"

## Platform considerations

- Replace with bottom sheet — inline dropdowns have insufficient touch target height
- Bottom sheet slides up, full-width, items min 48px height
- Drag handle at top; optional section headers preserved from dropdown
- Kebab tap opens bottom sheet; chevron button expands inline options list
- Destructive item always last, red, with extra padding from the group above

- Open on click; dismiss on outside click or Escape
- Anchor right edge of menu to right edge of trigger (right-aligned default)
- Flip to left-anchored if menu would clip right viewport edge
- Flip to open upward if menu would clip bottom viewport edge
- Keyboard: Space/Enter opens; arrow keys navigate; Escape closes

- Select button on remote opens the dropdown inline beside the trigger
- D-pad ↑↓ navigates items; Select activates; Back closes
- Use default size minimum — compact is unreadable at 3m distance
- Highlight focused item with 3px `--jio` glow outline, not just background tint
- No section header uppercase labels on TV — use a plain separator instead

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Trigger button | `` with `aria-haspopup="menu"` | Must be a native button, not a div. Screen readers announce "menu button". |
| Open/close state | `aria-expanded="true/false"` | Toggle on trigger with every open/close. Screen reader announces state change. |
| Menu container | `role="menu"` | Applied to `.dropdown-menu`. Paired with `aria-labelledby` pointing to trigger id. |
| Items | `role="menuitem"` | Each clickable item. Active/selected items use `aria-checked="true"` with `role="menuitemcheckbox"` for selection menus. |
| Disabled items | `aria-disabled="true"` | Keep focusable — use `aria-disabled` not HTML `disabled` so screen readers can read the item name. |
| Keyboard open | Space / Enter on trigger | Focus moves to first item. Down arrow also opens and focuses first item. |
| Keyboard nav | Arrow Up/Down, Home, End | Arrow keys move focus between items. Home/End jump to first/last. |
| Escape | Close menu, return focus to trigger | Required. Tab key also closes and moves focus forward in page order. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | `#161B26` | Menu background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Menu border and separators |
| `--r5` | `16px` | Menu container border-radius |
| `--r3` | `8px` | Item border-radius on hover |
| `--glass-1` | `rgba(255,255,255,.04)` | Item hover background |
| `--jio` | `#00A859` | Active item text and checkmark color |
| `--negative` | `#FF4757` | Destructive item text color |
| `--text3` | `rgba(244,242,238,.32)` | Section header and meta text color |
| `--dur-fast` | `120ms` | Item hover transition duration |

## When to use

Use when

- Overflow action menus (⋯) on cards and list items
- Sort-by and view-toggle menus in toolbars
- User account menu in the AppBar (profile, settings, logout)
- Any set of ≤8 related actions triggered by a single button

Don't use when

- Primary navigation — use Tab Bar or NavigationMenu
- More than 8 items — use Command palette or a dedicated screen
- Single toggle actions — use a Switch/Toggle instead
- Destructive-only menus — always provide a safe cancel option

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-fast` | opacity, transform scale(0.95 → 1) + translateY(-4px → 0) |
| Close | `--ease-in` | `--dur-fast` | opacity, transform scale(1 → 0.95) |
| Item highlight | `--ease-out` | `60ms` | background |
| Submenu open | `--ease-out` | `--dur-fast` | opacity, transform translateX(-4px → 0) |
| Chevron rotate | `--ease-out` | `--dur-fast` | transform rotate(0 → -180deg) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-dropdown` | Root floating panel — surface-2, r4, border-subtle |
| `.ds-dropdown__item` | Menu row — 40px, padding 0 12px |
| `.ds-dropdown__item--destructive` | Red color for delete items |
| `.ds-dropdown__item--disabled` | 38% opacity |
| `.ds-dropdown__separator` | 1px border-subtle divider |
| `.ds-dropdown__label` | Non-interactive section header |
| `.ds-dropdown__check` | Checkmark for toggle items |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `trigger` | ReactNode | required | Element that opens the menu |
| `items` | DropdownItem[] | required | Menu item definitions |
| `align` | "start" | "center" | "end" | "end" | Horizontal alignment relative to trigger |
| `onSelect` | (item: DropdownItem) => void | undefined | Item selection handler |
| `open` | boolean | undefined | Controlled open state |
| `onOpenChange` | (open: boolean) => void | undefined | Open state change handler |

## Code examples

````html
<div class="dropdown-wrap">
  <button
    id="kebab-trigger"
    class="dropdown-trigger dropdown-trigger--kebab"
    aria-haspopup="menu"
    aria-expanded="false"
    aria-controls="kebab-menu"
    aria-label="More options"
  >⋯</button>

  <div
    class="dropdown-menu"
    id="kebab-menu"
    role="menu"
    aria-labelledby="kebab-trigger"
    hidden
  >
    <button class="dropdown-item" role="menuitem">Edit profile</button>
    <button class="dropdown-item" role="menuitem">Download game</button>
    <button class="dropdown-item" role="menuitem">Share</button>
    <div class="dropdown-separator" role="separator"></div>
    <button class="dropdown-item dropdown-item--destructive" role="menuitem">Sign out</button>
  </div>
</div>
````

````html
<div class="dropdown-wrap">
  <button class="dropdown-trigger" aria-haspopup="menu" aria-expanded="false">
    <img class="account-avatar" src="/avatar.jpg" alt="My account">
    My account ▾
  </button>

  <div class="dropdown-menu" role="menu" hidden>
    <div class="dropdown-header" aria-hidden="true">Account</div>
    <a class="dropdown-item" role="menuitem" href="/profile">View profile</a>
    <a class="dropdown-item" role="menuitem" href="/settings">Settings</a>

    <div class="dropdown-separator" role="separator"></div>
    <div class="dropdown-header" aria-hidden="true">Support</div>
    <a class="dropdown-item" role="menuitem" href="/help">Help center</a>

    <div class="dropdown-separator" role="separator"></div>
    <button class="dropdown-item dropdown-item--destructive" role="menuitem">Sign out</button>
  </div>
</div>
````

````
<script>
document.querySelectorAll('.dropdown-wrap').forEach(wrap => {
  const trigger = wrap.querySelector('[aria-haspopup="menu"]');
  const menu    = wrap.querySelector('[role="menu"]');
  const items   = () => [...menu.querySelectorAll('.dropdown-item:not([aria-disabled="true"])')];
  let focusIdx  = 0;

  function open() {
    trigger.setAttribute('aria-expanded', 'true');
    menu.hidden = false;
    focusIdx = 0;
    items()[0]?.focus();
  }
  function close() {
    trigger.setAttribute('aria-expanded', 'false');
    menu.hidden = true;
    trigger.focus();
  }

  trigger.addEventListener('click', () => menu.hidden ? open() : close());

  trigger.addEventListener('keydown', e => {
    if (e.key === 'ArrowDown' || e.key === ' ' || e.key === 'Enter') {
      e.preventDefault(); open();
    }
  });

  menu.addEventListener('keydown', e => {
    const its = items();
    if (e.key === 'ArrowDown') { e.preventDefault(); focusIdx = (focusIdx + 1) % its.length; its[focusIdx].focus(); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); focusIdx = (focusIdx - 1 + its.length) % its.length; its[focusIdx].focus(); }
    if (e.key === 'Home')      { e.preventDefault(); focusIdx = 0; its[0].focus(); }
    if (e.key === 'End')       { e.preventDefault(); focusIdx = its.length - 1; its[focusIdx].focus(); }
    if (e.key === 'Escape' || e.key === 'Tab') close();
  });

  // Close on outside click
  document.addEventListener('click', e => {
    if (!wrap.contains(e.target)) close();
  });
});
</script>
````

## Changelog

Initial draft. Two size tiers (compact/default), five variants (right-aligned, left-aligned, section headers, icons, active checkmark), full keyboard nav spec and ARIA table. Mobile bottom-sheet replacement documented. TV D-pad guidance included.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--negative`
- `--r3`
- `--r5`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

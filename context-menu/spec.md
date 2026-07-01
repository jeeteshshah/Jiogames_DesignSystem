# Context Menu — JioGames DLS spec

> Source: `context-menu/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Context Menu

---

Right-click (long-press on mobile) menu that offers actions relevant to the selected item. Used on game cards, library items, and friend list entries.

Context Menu · Right-click on game card

Context menus surface relevant actions for an item when the user right-clicks (web), long-presses (mobile), or presses the Menu button (TV remote). They are anchored to the pointer position or item bounds, never to a fixed UI element. Context menus are ephemeral — they dismiss on any outside click, Escape, or action selection.

- **Game card actions** — Play, Wishlist, Share, Remove from library
- **Library item actions** — Download, Move to folder, Mark as played
- **Friend list actions** — View profile, Send message, Remove friend
- **Submenu navigation** — nested actions for "Add to playlist →"

- Group related actions with separators — primary, secondary, destructive
- Put destructive actions last, after a separator, in red
- Show keyboard shortcuts right-aligned in muted monospace
- Max 10 items before adding a submenu — beyond that is overwhelming
- Return focus to the trigger item on close via keyboard

- Use a context menu as a primary navigation pattern — actions must also be reachable elsewhere
- Mix destructive and non-destructive items in the same group without a separator
- Show a context menu at a fixed screen position — always anchor to pointer or item
- Exceed 10 items in a single level — add submenu or reduce scope
- Use context menu for settings — settings have a dedicated page

1. 1 Container Required Elevated surface, 6px inner padding. Uses `position:fixed` when anchored to pointer position at runtime. `background: var(--surface-2); border-radius: var(--r5)`
2. 2 Menu item Required 14px medium weight. 8px 12px padding. Full-width button with hover background. Icon slot left-aligned (optional). `padding: 8px 12px; border-radius: var(--r3)`
3. 3 Hover state Required Item background changes to `--glass-1` on hover and keyboard focus. `background: var(--glass-1)`
4. 4 Separator Optional 1px horizontal rule with 4px 6px margin. Groups related items. Use `role="separator"`. `height: 1px; background: var(--border-subtle)`
5. 5 Destructive item Optional Same item structure but text and icon use `--negative`. Hover background is red-tinted. Always last in the menu. `color: var(--negative)`

## Variants

Four variants support different levels of information density and navigation depth.

## Sizes

Two size tiers. Default for most surfaces. Compact for dense list views where item height must match the row it annotates.

## States

Individual items carry state. The menu container itself is always opaque when open.

## Content guidance

- Verb-first labels: "Play now", "Add to wishlist", "Share"
- Sentence case, no trailing punctuation
- Max 3 words per label — avoid "Remove this game from your library"
- Destructive label must name the consequence: "Remove from library" not just "Remove"
- Disabled items: keep visible, dim to 35% opacity, add a tooltip explaining why

- Group 1: Primary actions (Play, Download, Open)
- Group 2: Secondary / social (Share, Add to playlist, Rate)
- Group 3: Destructive actions only (Remove, Delete, Block)
- Never put a destructive action in Group 1
- Max 10 items across all groups — add submenus beyond that

## Platform considerations

- Long-press (500ms) triggers context menu as a **bottom sheet**, not a floating menu
- Bottom sheet is full-width, items are 48px minimum touch height
- Drag handle at top, optional title showing the item name
- Destructive action always last, styled red
- No keyboard shortcuts displayed on mobile

- Triggered by `contextmenu` event (right-click or Shift+F10)
- Anchored to pointer coordinates, flipped if near viewport edge
- Keyboard shortcuts shown right-aligned in monospace
- Dismiss on `click outside`, `Escape`, or action selection
- Use `position:fixed` — not absolute — to escape stacking contexts

- Menu/Options button on remote triggers context menu on focused item
- Rendered as an inline overlay beside the focused card, not at pointer position
- D-pad ↑↓ navigates items; Select activates; Back or Menu dismisses
- Use default size minimum — compact is too small at 3m viewing distance
- No keyboard shortcuts on TV — omit shortcut column entirely

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| Container role | `role="menu"` | Applied to the `.context-menu` container element. |
| Item role | `role="menuitem"` | Each `.context-menu-item` button gets this role. Destructive items still use menuitem. |
| Disabled items | `aria-disabled="true"` | Keep in DOM and focusable — use `aria-disabled` not `disabled` so screen readers announce the item and its state. |
| Separator | `role="separator"` | Applied to separator div elements. Screen readers skip them but understand group boundaries. |
| Keyboard navigation | Arrow Up/Down, Home, End | ↑↓ moves between items, wrapping at ends. Home/End jump to first/last. |
| Escape to close | JS `keydown Escape` | Close menu and return focus to the element that triggered it. |
| Trigger linkage | `aria-haspopup="menu"` | Applied to any button that explicitly triggers a context menu (e.g. kebab). Not needed for right-click. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | `#161B26` | Menu background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Menu border and separators |
| `--r5` | `16px` | Menu container border-radius |
| `--r3` | `8px` | Item border-radius on hover |
| `--glass-1` | `rgba(255,255,255,.04)` | Item hover background |
| `--negative` | `#FF4757` | Destructive item text color |
| `--text3` | `rgba(244,242,238,.32)` | Keyboard shortcut text color |
| `--dur-fast` | `120ms` | Item hover transition duration |

## When to use

Use when

- Right-click or long-press actions on game cards and list items
- Quick actions: add to wishlist, share, remove from list
- Contextual options that do not warrant a permanent UI element

Don't use when

- Primary or frequently used actions — put them in the main UI
- Mobile as the only way to access an action — must have a visible alternative
- More than ~8 items — split into submenus or a sheet

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-fast` | opacity, transform scale(0.95 → 1) |
| Close | `--ease-in` | `--dur-fast` | opacity |
| Item highlight | `--ease-out` | `60ms` | background |
| Submenu open | `--ease-out` | `--dur-fast` | opacity, transform translateX(-4px → 0) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-context-menu` | Root floating panel — surface-2, shadow, r4 |
| `.ds-context-menu__item` | Menu row — 40px height, padding 0 12px |
| `.ds-context-menu__item--destructive` | Red label for delete actions |
| `.ds-context-menu__item--disabled` | 38% opacity, no pointer events |
| `.ds-context-menu__separator` | 1px border-subtle horizontal divider |
| `.ds-context-menu__label` | Non-interactive section header — text3 |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `children` | ReactNode | required | Trigger element (wraps the target) |
| `items` | MenuItem[] | required | Menu item definitions |
| `onSelect` | (item: MenuItem) => void | undefined | Item selection handler |

## Code examples

````html
<div
  class="context-menu"
  role="menu"
  aria-label="Game options"
  style="position:fixed; top: var(--ctx-y); left: var(--ctx-x);"
>
  <button class="context-menu-item" role="menuitem">
    Play now
  </button>
  <button class="context-menu-item" role="menuitem">
    Add to wishlist
  </button>
  <button class="context-menu-item" role="menuitem">
    View details
  </button>
  <div class="context-menu-separator" role="separator"></div>
  <button class="context-menu-item" role="menuitem">
    Share
  </button>
  <div class="context-menu-separator" role="separator"></div>
  <button class="context-menu-item context-menu-item--destructive" role="menuitem">
    Remove from library
  </button>
</div>
````

````html
<button class="context-menu-item" role="menuitem">
  Play now
  <span class="context-menu-shortcut" aria-label="Shortcut: Command P">⌘P</span>
</button>
<button class="context-menu-item" role="menuitem">
  Download
  <span class="context-menu-shortcut" aria-label="Shortcut: Command D">⌘D</span>
</button>
````

````
<script>
const menu = document.getElementById('ctx-menu');
const items = () => [...menu.querySelectorAll('.context-menu-item:not(.context-menu-item--disabled)')];
let focusIdx = 0;

// Open on right-click
document.querySelectorAll('[data-ctx-target]').forEach(el => {
  el.addEventListener('contextmenu', e => {
    e.preventDefault();
    menu.style.top  = e.clientY + 'px';
    menu.style.left = e.clientX + 'px';
    menu.hidden = false;
    focusIdx = 0;
    items()[0]?.focus();
  });
});

// Arrow navigation
menu.addEventListener('keydown', e => {
  const its = items();
  if (e.key === 'ArrowDown') { e.preventDefault(); focusIdx = (focusIdx + 1) % its.length; its[focusIdx].focus(); }
  if (e.key === 'ArrowUp')   { e.preventDefault(); focusIdx = (focusIdx - 1 + its.length) % its.length; its[focusIdx].focus(); }
  if (e.key === 'Home')      { e.preventDefault(); focusIdx = 0; its[0].focus(); }
  if (e.key === 'End')       { e.preventDefault(); focusIdx = its.length - 1; its[focusIdx].focus(); }
  if (e.key === 'Escape')    { menu.hidden = true; }
});

// Dismiss on outside click
document.addEventListener('click', e => {
  if (!menu.contains(e.target)) menu.hidden = true;
});
</script>
````

## Changelog

Initial draft. Default and compact size tiers, four variants (default, shortcuts, icons, submenu indicator), full keyboard navigation spec, accessibility table with ARIA roles. Mobile bottom-sheet replacement documented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--ctx-x`
- `--ctx-y`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--negative`
- `--r3`
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

# Command — JioGames DLS spec

> Source: `command/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Command

---

Full-screen or modal search and command palette. Press ⌘K (web) to find games, navigate screens, or trigger actions without using the navigation. JioGames-adapted for game library search.

Command palette · search "tomb" · grouped results · keyboard hints

The Command palette is a keyboard-first overlay that lets users search games, jump to screens, and trigger actions from anywhere in the JioGames web app. It appears on ⌘K (Mac) or Ctrl+K (Windows/Linux) and dismisses on Escape. On mobile the command palette is replaced by a full-screen search view — the palette itself is web-only.

- **Search** — find games by name, genre, or pass tier instantly
- **Navigate** — jump to Library, Home, Profile, Settings without mouse
- **Actions** — trigger common tasks like "Add to Wishlist" or "Open Subscription"
- **Recent** — shows last 5 searches when opened with empty input

- Show recent searches when input is empty so users can reopen without retyping
- Group results into labeled sections — Games, Navigate, Actions — for scannability
- Limit each group to 8 items before scrolling begins within the list
- Highlight the first result automatically so Enter immediately works on open
- Return focus to the element that triggered the palette when it closes

- Use the command palette on mobile — replace with the full-screen search view instead
- Show more than 3 groups in a single result set — too many categories overwhelms users
- Close the palette on outside click if the user is mid-type — wait for Escape or selection
- Include destructive actions (delete, unsubscribe) in the command palette without confirmation
- Show zero-state "No results" for queries under 2 characters — wait before searching

1. 1 Panel container Required Fixed max-width 560px. Dark surface, 1px border, large border-radius, deep box-shadow. Never full-bleed. `background: var(--surface-1); border-radius: var(--r6)`
2. 2 Search input Required Transparent background, no border, auto-focused on open. Search icon left, Esc badge right. Placeholder: "Search games…" `role="combobox"; aria-expanded; aria-autocomplete="list"`
3. 3 Result list Required Scrollable, max-height 320px. Groups separated by uppercase headers. Active item uses glass-1 fill. Icon, label, optional shortcut right-aligned. `role="listbox"; aria-activedescendant`
4. 4 Footer hints Optional Keyboard shortcut guide: ↑↓ navigate, ↵ select, Esc close. 11px muted text. Always visible when results are showing. `font-size: 11px; color: var(--text3)`

## Variants

Four command palette states cover the full interaction lifecycle — from empty open to active searching.

## Sizes

The command panel has a single fixed size — max-width 560px, dynamic height based on results. No size variants exist.

| Property | Value | Notes |
|---|---|---|
| Panel max-width | `560px` | Centered in viewport, full-width on narrow screens |
| List max-height | `320px` | Scrollable beyond — never grows past this |
| Item height | `40px` | 10px top + bottom padding + 20px content |
| Input font-size | `16px` | Prevents iOS zoom on focus |
| Viewport offset | `80px from top` | Leaves space for users to see they're in overlay context |

## States

Five discrete states cover the full command palette lifecycle. Only one state is active at a time.

## Content guidance

Command palette text must be action-oriented and immediately scannable. Users read these labels in motion.

- Use exactly these group names: **Games**, **Navigate**, **Actions**
- Recent searches label: "Recent searches" not "History" or "Recent"
- Max 8 items per group before scroll — do not paginate inside the palette
- Empty state copy: 'No games found for "[query]"' — include the query

- Game results: title only, genre tag as shortcut badge right-aligned
- Navigate items: start with a verb — "Go to Library", "Open Settings"
- Action items: imperative — "Add to Wishlist", "Start Download"
- Keyboard shortcuts: use system notation (⌘L, Ctrl+L) — never spell "Command"

## Platform considerations

Command palette is a web-only pattern. Each other platform has an equivalent experience.

- No command palette on mobile — use the full-screen search view instead
- Search icon in header triggers the full-screen overlay
- Results layout matches command palette groups but without keyboard hints
- Voice search button alongside text input

- ⌘K (Mac) or Ctrl+K (Win/Linux) opens the palette from anywhere
- Backdrop click closes if input is empty — warns with shake animation if not
- Tab moves between groups, arrow keys within a group
- Persist recent searches in localStorage, max 10 entries

- Not applicable — no keyboard shortcut available on TV remote
- Use dedicated Search screen navigable via D-pad instead
- Voice search via remote mic button where hardware supports it

## Accessibility

The command palette relies heavily on ARIA roles and live regions to communicate state to screen-reader users.

| Element | Role / attribute | Guidance |
|---|---|---|
| Overlay container | `role="dialog"` | `aria-modal="true"`, `aria-label="Search and command palette"`. Focus trapped inside while open. |
| Search input | `role="combobox"` | `aria-expanded`, `aria-autocomplete="list"`, `aria-controls` pointing to listbox ID. |
| Result list | `role="listbox"` | `aria-label="Search results"`. Input's `aria-activedescendant` tracks the highlighted item's ID. |
| Group headers | `role="group"` | `aria-label` on each group matching the visible header text. |
| Result items | `role="option"` | `aria-selected="true"` on highlighted item. Each item has a stable unique ID. |
| Escape key | Native keyboard event | Closes dialog and returns focus to the element that triggered it — typically the search icon button. |

## Related tokens

All command palette surfaces use existing system tokens — no component-specific tokens required.

| Token | Value | Usage |
|---|---|---|
| `--surface-1` | `#0e1118` | Command panel background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Panel border, input divider, footer divider |
| `--glass-1` | `rgba(255,255,255,.05)` | Hovered and active item background |
| `--surface-3` | — | Shortcut badge background, Esc key background |
| `--r6` | `20px` | Panel corner radius |
| `--text3` | `rgba(244,242,238,.32)` | Placeholder, group headers, footer hints, icons |
| `--dur-fast` | `120ms` | Item hover background transition |

## When to use

Use when

- Global search palette triggered by keyboard shortcut (⌘K)
- Quick action launcher for power users on web/desktop
- In-app navigation shortcut across all screens

Don't use when

- Mobile as primary search — use the AppBar search instead
- Replacing contextual menus (right-click or long-press)
- Exposing commands users do not need frequently

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Dialog open | `--ease-out` | `--dur-fast` | opacity, transform scale(0.96 → 1) |
| Dialog close | `--ease-in` | `--dur-fast` | opacity, transform scale(1 → 0.96) |
| Scrim fade | `--ease-out` | `--dur-fast` | opacity |
| Item highlight | `--ease-out` | `60ms` | background |
| Group header appear | `--ease-out` | `--dur-fast` | opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-command` | Root dialog wrapper — centered overlay |
| `.ds-command__input` | Search text field — top of palette |
| `.ds-command__list` | Scrollable results area |
| `.ds-command__group` | Labelled result section |
| `.ds-command__item` | Single result row — 40px height |
| `.ds-command__item--selected` | Keyboard-highlighted item |
| `.ds-command__empty` | No results state |
| `.ds-command__scrim` | Full-screen backdrop |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | required | Controls palette visibility |
| `onOpenChange` | (open: boolean) => void | required | Close handler |
| `placeholder` | string | "Search commands…" | Input placeholder |
| `onSelect` | (value: string) => void | undefined | Fired when item chosen |
| `children` | ReactNode | required | CommandGroup and CommandItem nodes |

## Code examples

Three starting-point snippets covering the most common command palette compositions.

````html
<div role="dialog" aria-modal="true" aria-label="Search and command palette" class="command-overlay">
  <div class="command-panel">
    <div class="command-input-wrap">
      <svg class="command-search-icon" aria-hidden="true">...</svg>
      <input
        class="command-input"
        role="combobox"
        aria-expanded="true"
        aria-autocomplete="list"
        aria-controls="command-listbox"
        aria-activedescendant="cmd-item-0"
        placeholder="Search games…"
        autofocus
      />
      <kbd aria-label="Press Escape to close">Esc</kbd>
    </div>
    <ul id="command-listbox" role="listbox" aria-label="Search results" class="command-list">
      <!-- results injected here -->
    </ul>
    <div class="command-footer">
      <span class="command-hint"><kbd>↑↓</kbd> navigate</span>
      <span class="command-hint"><kbd>↵</kbd> select</span>
      <span class="command-hint"><kbd>Esc</kbd> close</span>
    </div>
  </div>
</div>
````

````
<ul id="command-listbox" role="listbox" aria-label="Search results" class="command-list">

  <li role="group" aria-label="Games">
    <div class="command-group-header" aria-hidden="true">Games</div>
    <ul>
      <li id="cmd-item-0" role="option" aria-selected="true" class="command-item is-active">
        <span class="command-item-icon" aria-hidden="true">🎮</span>
        <span class="command-item-label">Tomb Raider</span>
        <span class="command-shortcut" aria-label="Genre: Action">ACTION</span>
      </li>
      <li id="cmd-item-1" role="option" aria-selected="false" class="command-item">
        <span class="command-item-icon" aria-hidden="true">🎮</span>
        <span class="command-item-label">Tomb Raider II</span>
        <span class="command-shortcut" aria-label="Genre: Action">ACTION</span>
      </li>
    </ul>
  </li>

  <li role="group" aria-label="Navigate">
    <div class="command-group-header" aria-hidden="true">Navigate</div>
    <ul>
      <li id="cmd-item-2" role="option" aria-selected="false" class="command-item">
        <span class="command-item-icon" aria-hidden="true">📚</span>
        <span class="command-item-label">Go to Library</span>
        <span class="command-shortcut">⌘L</span>
      </li>
    </ul>
  </li>

</ul>
````

````
<!-- Shown when input is empty (no query typed yet) -->
<ul id="command-listbox" role="listbox" aria-label="Recent searches" class="command-list">
  <li role="group" aria-label="Recent searches">
    <div class="command-group-header" aria-hidden="true">Recent searches</div>
    <ul>
      <li id="cmd-recent-0" role="option" aria-selected="true" class="command-item is-active">
        <span class="command-item-icon" aria-hidden="true">🕐</span>
        <span class="command-item-label">Tomb Raider</span>
      </li>
      <li id="cmd-recent-1" role="option" aria-selected="false" class="command-item">
        <span class="command-item-icon" aria-hidden="true">🕐</span>
        <span class="command-item-label">War Thunder</span>
      </li>
    </ul>
  </li>
</ul>

<!-- Shown when search returns no results -->
<div class="command-empty" role="status" aria-live="polite">
  No games found for "xyzabc"
</div>
````

## Changelog

Initial draft. Includes panel structure, grouped results, empty state, keyboard navigation, and ARIA documentation. Web-only — mobile and TV equivalents noted.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--input-placeholder`
- `--jio`
- `--jio-font`
- `--r1`
- `--r2`
- `--r4`
- `--r6`
- `--surface-1`
- `--surface-3`
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

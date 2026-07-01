# Combobox — JioGames DLS spec

> Source: `combobox/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Combobox

---

Searchable select for finding games, genres, or friends from large lists. Combines text input with a dropdown of filtered options.

Combobox open · query "tomb r" · first result highlighted

The Combobox is a searchable selection control that combines a text input with a filtered dropdown list. It is the right choice when a list has more than 15 items, when users are unlikely to know the exact option name up front, or when typing is faster than scrolling. It is not a replacement for a simple Select — use Select for short, well-known lists.

- **Game search** — find a game by name from the full catalogue across add-to-wishlist, review, and share flows
- **Genre and tag filter** — multi-select combobox for applying genre tags in preference setup
- **Friend search** — find players by username to invite to a party or share a game
- **Large reference lists** — country, language, or platform selection when the list exceeds 15 items

- Highlight the matched query substring in each result — bold green on the matched characters
- Show a maximum of 8 results before scrolling — more overwhelms without adding value
- Write a specific empty state: *No games found for "xyz"* — never a blank white box
- Show skeleton items during network fetch — never a spinner that blocks the input
- Close the dropdown on Escape, and return focus to the input

- Open the dropdown before the user has typed at least 1 character — an unfiltered full list is not a Combobox, it is a Select
- Use Combobox for lists under 15 items — use Select instead
- Show a completely blank dropdown panel on empty results — always show the empty state message
- Trigger a network request on every keystroke without debouncing — debounce by at least 200ms
- Auto-select the first result on Enter without the user explicitly confirming — they may still be typing

1. 1 Text input Required Standard input field with `role="combobox"`, `aria-autocomplete="list"`, and `aria-expanded`. Green border and glow when open. `height: 48px; border-color: var(--jio) when open`
2. 2 Search icon Optional 16px magnifier icon, right-aligned in the input. Turns green when the dropdown is open. `pointer-events: none`. `color: var(--text3) → var(--jio) on open`
3. 3 Dropdown list Required Absolutely positioned below the input, `role="listbox"`. Max 8 items visible before scroll. Dark surface background, subtle border, strong drop shadow. `background: var(--surface-2); box-shadow: 0 8px 24px rgba(0,0,0,.4)`
4. 4 Result item Required Each item is `role="option"`. Optional leading thumbnail, matched text highlighted in green/bold, 10px 14px padding. Hover and keyboard-active state both use `is-active`. `padding: 10px 14px; font-size: 14px`

## Variants

Five variants. Default covers single-value game and genre search. Multi-select is used for preference setup where several tags need to be applied at once.

## Sizes

Two input height tiers. The dropdown list item size does not change — only the trigger height varies.

## States

Six states across the input and list together. The loading state shows skeleton items in the list while results are fetching — the input remains fully interactive.

| State | Input | List |
|---|---|---|
| Default | Border `var(--border-subtle)`, grey search icon | Hidden |
| Focused / Open | Border `var(--jio)`, green glow, green search icon | Visible, results rendered |
| Item hover | No change | Hovered item background `var(--glass-1)` |
| Item selected | Input shows selected value; list closes | Hidden after selection |
| Loading | Open / focused state | Skeleton items pulse at 1.4s |
| Empty | Open / focused state | Single empty state message: "No [noun] found for "[query]"" |

## Content guidance

Three text surfaces: input placeholder, result items, and the empty state message.

- Placeholder: "Search games…", "Find a friend…" — use an ellipsis, not "Enter a name"
- Match highlight: bold the matched substring in `var(--jio)` green — never underline or italicise
- Show max 8 items before the list scrolls internally
- Result item copy: game title as-is, no truncation under 32 chars
- For friend search: show username + display name in a two-line item layout

- Always include the query in the message: *No games found for "xyzqwerty"*
- Never leave the dropdown panel blank — a blank panel creates confusion about whether results are still loading
- If the list is network-backed, distinguish "no results" from "error": *No games found…* vs *Couldn't load results. Try again.*
- Offer a fallback action in the empty state where possible: "Browse all games →"

## Platform considerations

The list presentation changes substantially across platforms — the input is consistent, the list adapts to the interaction model.

- Do not render an inline dropdown on mobile — open a bottom sheet instead to avoid soft-keyboard overlap
- Bottom sheet contains the input at the top and scrollable list below, full-width
- Result items on mobile: 56px height minimum for touch target compliance
- Debounce network queries by 300ms on mobile — slower connections need more tolerance
- Show a "Done" button in the bottom sheet header to confirm multi-select and dismiss

- Inline dropdown panel below the input — standard combobox pattern
- Max dropdown height: `320px` with internal scroll; never taller than the viewport minus 80px
- Flip to open upward if there is insufficient space below the input
- Debounce network queries by 200ms
- Click outside (pointerdown on document) closes the dropdown

- No inline combobox on TV — open a full-screen search overlay on d-pad confirm
- Full-screen overlay: input at the top with virtual keyboard or voice search; results in a grid below
- D-pad navigates the result grid; OK confirms; Back closes the overlay
- Result cards on TV: 120px+ height with large artwork for legibility at 3m
- Always offer voice search as primary input method on TV — physical text entry is slow

## Accessibility

Combobox is one of the most complex ARIA patterns. Follow the ARIA 1.2 combobox pattern precisely — do not approximate.

| Requirement | Implementation | Notes |
|---|---|---|
| Input role | `role="combobox"` | Applied to the `` element itself, not a wrapper div. |
| Expanded state | `aria-expanded="true|false"` | Toggle on input with every open/close. Screen readers announce "expanded" or "collapsed" on focus. |
| Autocomplete hint | `aria-autocomplete="list"` | Tells screen readers that a list of suggestions is available filtered by typed input. |
| List ownership | `aria-controls="listbox-id"` | Points the input to the `role="listbox"` element. Required for JAWS and NVDA to associate the two. |
| Active option | `aria-activedescendant="option-id"` | Updated on every keyboard arrow navigation to point to the currently highlighted `role="option"`. Do not move DOM focus to the option — keep focus on the input. |
| Option roles | `role="option"` + `aria-selected` | Each result item. `aria-selected="true"` on the currently highlighted item. For multi-select, `aria-selected="true"` on chosen items. |
| Keyboard | Down/Up: navigate list · Enter: select · Escape: close | Home moves to first item, End to last. Tab closes and moves to next focusable element without selecting. |

## Related tokens

Tokens used across the input and dropdown list.

| Token | Value | Usage |
|---|---|---|
| `--input-bg` | `var(--glass-1)` | Input background fill |
| `--input-border` | `var(--border-subtle)` | Default input border |
| `--jio` | `#00A859` | Open border, glow ring, match highlight, selected item color, chip background |
| `--surface-2` | Surface tier 2 | Dropdown list background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Dropdown list border |
| `--glass-1` | Glass tier 1 | Item hover and keyboard-active background |
| `--surface-3` | Surface tier 3 | Skeleton item pulse background |
| `--text3` | `rgba(244,242,238,.32)` | Empty state text, search icon default color |
| `--r5` | Border radius tier 5 | Input and list border-radius |

## When to use

Use when

- Searchable select for large option sets (countries, games, genres)
- Tag/token input where users type and pick from suggestions
- Game search with autocomplete suggestions
- Any select with more than ~10 options where filtering helps

Don't use when

- Small option sets (≤8 items) — use Select instead
- Simple yes/no or binary choices — use Toggle or Radio
- Freeform text input where no predefined options exist — use Input

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Dropdown open | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Dropdown close | `--ease-in` | `--dur-fast` | opacity |
| Option highlight | `--ease-out` | `80ms` | background |
| Selection chip appear | `--ease-out` | `--dur-fast` | transform scale(0.85 → 1), opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-combobox` | Root container |
| `.ds-combobox__input` | Text input — triggers dropdown |
| `.ds-combobox__dropdown` | Options list — surface-2, shadow, r4 |
| `.ds-combobox__option` | Single option row — 40px height |
| `.ds-combobox__option--active` | Highlighted option — glass-1 bg |
| `.ds-combobox__option--selected` | Chosen option — green checkmark |
| `.ds-combobox__empty` | No results message |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | string[] | undefined | Controlled selected value(s) |
| `onValueChange` | (v: string | string[]) => void | undefined | Selection change handler |
| `options` | { value: string; label: string }[] | required | Available options |
| `multiple` | boolean | false | Enable multi-select |
| `placeholder` | string | "Search…" | Input placeholder text |
| `disabled` | boolean | false | Disable the control |

## Code examples

Link `tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="combobox-wrap">
  <label class="field-label" id="game-label">Search games</label>
  <div class="combobox-input-wrap">
    <input
      type="text"
      id="game-input"
      class="combobox-input"
      role="combobox"
      aria-expanded="false"
      aria-autocomplete="list"
      aria-controls="game-listbox"
      aria-labelledby="game-label"
      aria-activedescendant=""
      placeholder="Search games…"
      autocomplete="off"
    >
    <span class="combobox-search-icon" aria-hidden="true">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <circle cx="7" cy="7" r="4.5" stroke="currentColor" stroke-width="1.5"/>
        <path d="M10.5 10.5L14 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </span>
  </div>
  <ul
    id="game-listbox"
    class="combobox-list"
    role="listbox"
    aria-labelledby="game-label"
    hidden
  >
    <li id="opt-1" class="combobox-item" role="option" aria-selected="false">
      <div class="combobox-thumb"></div>
      Tomb Raider
    </li>
    <li id="opt-2" class="combobox-item" role="option" aria-selected="false">
      <div class="combobox-thumb"></div>
      Tomb Raider II
    </li>
    <!-- empty state (shown when no results) -->
    <li class="combobox-empty" role="status" hidden>
      No games found for ""
    </li>
  </ul>
</div>
````

````
const input    = document.getElementById('game-input');
const listbox  = document.getElementById('game-listbox');
const options  = () => [...listbox.querySelectorAll('[role="option"]:not([hidden])')];
let activeIdx  = -1;

function open()  { listbox.hidden = false; input.setAttribute('aria-expanded', 'true'); }
function close() { listbox.hidden = true;  input.setAttribute('aria-expanded', 'false'); activeIdx = -1; clearActive(); }

function setActive(idx) {
  const opts = options();
  clearActive();
  if (idx < 0 || idx >= opts.length) { activeIdx = -1; input.setAttribute('aria-activedescendant', ''); return; }
  activeIdx = idx;
  opts[idx].classList.add('is-active');
  input.setAttribute('aria-activedescendant', opts[idx].id);
  opts[idx].scrollIntoView({ block: 'nearest' });
}
function clearActive() { options().forEach(o => o.classList.remove('is-active')); }

input.addEventListener('input', () => {
  // filter options, then:
  activeIdx = -1;
  open();
});

input.addEventListener('keydown', e => {
  const opts = options();
  if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(activeIdx + 1, opts.length - 1)); }
  if (e.key === 'ArrowUp')   { e.preventDefault(); setActive(Math.max(activeIdx - 1, 0)); }
  if (e.key === 'Home')      { e.preventDefault(); setActive(0); }
  if (e.key === 'End')       { e.preventDefault(); setActive(opts.length - 1); }
  if (e.key === 'Enter' && activeIdx >= 0) {
    input.value = opts[activeIdx].textContent.trim();
    close();
  }
  if (e.key === 'Escape') { close(); }
  if (e.key === 'Tab')    { close(); }
});

document.addEventListener('pointerdown', e => {
  if (!input.contains(e.target) && !listbox.contains(e.target)) close();
});
````

````
<!-- Multi-select: selected values render as chips inside the input wrapper -->
<div
  class="combobox-chips"
  role="group"
  aria-label="Selected genres"
  onclick="this.querySelector('.combobox-chip-input').focus()"
>
  <!-- Chip per selected value -->
  <span class="combobox-chip">
    Action
    <button
      class="combobox-chip-remove"
      aria-label="Remove Action"
      onclick="this.closest('.combobox-chip').remove()"
    >×</button>
  </span>
  <span class="combobox-chip">
    RPG
    <button class="combobox-chip-remove" aria-label="Remove RPG"
      onclick="this.closest('.combobox-chip').remove()">×</button>
  </span>
  <!-- Inline search input -->
  <input
    type="text"
    class="combobox-chip-input"
    role="combobox"
    aria-expanded="false"
    aria-autocomplete="list"
    aria-controls="genre-listbox"
    placeholder="Add genre…"
    autocomplete="off"
  >
</div>
<!-- Dropdown list renders below .combobox-chips wrapper -->
<ul id="genre-listbox" class="combobox-list" role="listbox" hidden>
  <li class="combobox-item" role="option" aria-selected="false">Sports</li>
  <li class="combobox-item" role="option" aria-selected="false">Racing</li>
  <li class="combobox-item" role="option" aria-selected="false">Adventure</li>
</ul>
````

## Changelog

Initial draft. Includes Default, Open, Empty, Loading, and Multi-select variants. M and L input sizes. Six states. Platform guidance for mobile bottom sheet, web inline dropdown, and TV full-screen overlay. Full ARIA 1.2 combobox accessibility table. Three code examples: HTML structure, keyboard navigation pattern, and multi-select chip input.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--input-bg`
- `--input-border`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--pill`
- `--r3`
- `--r5`
- `--surface-2`
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

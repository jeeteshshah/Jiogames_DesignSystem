# Search — JioGames DLS spec

> Source: `search/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Search

---

Search gives players immediate access to any game, genre, or creator in the JioGames library.

Search is the fastest path to discovery in JioGames. It combines a text input, state-driven visual feedback, and a contextual results surface — all responding to what the player is doing right now, whether browsing recents, typing a query, or landing on an empty state.

- **Immediate feedback.** The search icon turns green on focus, recent chips appear, and results skeleton in after 300ms debounce.
- **Three size tiers.** S, M, and L map to compact filter bars, the default search surface, and full-screen hero moments. Platform context resolves pixel values automatically.
- **Four variants.** Standalone, AppBar-integrated, full-screen overlay, and filter-augmented — each with the same core anatomy.
- **Stateful by design.** Every lifecycle moment — from default to loading to no-results to offline — has a defined visual treatment and next step for the player.

## When to use

Use when

- Global game search from the AppBar or dedicated search screen
- Filtering items in a list or data table
- Command palette input (inside the Command component)
- Genre/title search in the game library

Don't use when

- Full-text content search in articles/help docs — different UX pattern needed
- Search as the only navigation — pair with Browse/discovery
- Search input without a results state (empty, loading, no results)

## Best practices

Rules for keeping search usage consistent and useful across the JioGames product surface.

- Use a descriptive, context-aware placeholder: "Search games, genres, creators..."
- Show recent searches when the input is focused and empty
- Debounce search requests at 300ms minimum before firing
- Show skeleton results while loading — not a full-screen spinner
- Always offer genre chips in the no-results state
- Announce result count via `aria-live` when results load
- Keep the clear button accessible: `aria-label="Clear search"`
- On TV, make recent searches the primary visible content

- Don't fire a request on every keystroke — debounce first
- Don't say "No results found" without a next action or genre fallback
- Don't block the UI with a full-screen loader during search
- Don't use a vague single-word placeholder like "Search"
- Don't remove the focus ring — use `var(--jio)` border, never outline: none
- Don't place search inside a card or modal without managed scroll context
- Don't skip the minimum 2-character threshold before triggering results

## Anatomy

Every search bar is built from five slots. The container and input field are required. All others respond to interaction state.

## Variants

Four search variants cover every surface where players need to find content. All share the same five-slot anatomy; only context and layout differ.

## Sizes

Three size tiers — S, M, L — resolve to different pixel heights per platform. The size class stays constant; platform context provides the final value.

## States

Six interaction states cover the full search lifecycle. Each state has a distinct visual treatment and drives different panel content below the input.

## Content

Every search surface text touch-point — placeholder, empty state copy, error — should reduce friction and show the player a clear next step.

- Use "Search games, genres, creators..." on main search page
- Use "Search..." only inside AppBar due to space constraints
- Never use just "Search" alone — name the objects players can find
- Match language to the current surface context

- Require minimum 2 characters before triggering any request
- Debounce at 300ms after last keystroke
- Show recent searches when focused and input is empty
- Display skeleton cards while results load — not a spinner overlay

- Format: No results for “[query]”
- Always follow with: Try a different keyword or browse by genre
- Show 4–6 genre chips as fallback browsing path
- Never show a dead-end with no next action

- Error message: "Search unavailable. Check your connection and try again."
- Show in a red-tinted banner below the bar, not inside it
- Auto-retry when connection restores — no manual user action needed
- Disabled state: `opacity: var(--state-disabled-opacity)`

## Platform considerations

The search component adapts its interaction model, size, and panel layout to the constraints of each platform.

- Full-width at top of search page
- Tap activates focus; system keyboard slides up
- Results and recent searches fill the page below
- Bottom sheet for filter chips when results are displayed
- Voice search icon in trailing position if microphone permission granted
- Dismiss via back gesture or tapping outside
- L size (54px) required for touch target compliance

- Inline within page or AppBar, max-width 480px
- Inline results dropdown panel, z-index managed above rail content
- Hover state on suggestion items (`var(--glass-1)` bg)
- Arrow keys navigate suggestion list
- ESC clears value and closes suggestions
- Enter submits and routes to results page
- M size (44px) for standard placement

- D-pad OK/Enter to open virtual keyboard overlay
- Full-width search bar always visible; cursor navigates to it
- Recent searches shown prominently — reduce typing burden
- Voice search button accessible via D-pad
- Suggestion items navigable up/down with D-pad
- Focus ring uses `var(--tv-focus-shadow)` glow + scale(1.05)
- L size (72px) for legibility at viewing distance

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Focus expand (mobile) | `--ease-out` | `--dur-fast` | width, opacity |
| Clear button appear | `--ease-out` | `--dur-fast` | opacity, transform scale(0.8 → 1) |
| Results appear | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Result item stagger | `--ease-out` | `--dur-fast` | opacity (30ms delay per item) |
| Loading spinner | `linear` | `600ms infinite` | transform rotate |

## Platform rules

Mobile

- AppBar integration: tapping search icon expands input full-width
- Results dropdown becomes full-screen overlay on mobile
- Keyboard auto-opens on search field focus
- Clear button (×) in trailing slot — 44×44px touch target

Web

- Inline dropdown results anchored below input — max 480px height
- Keyboard: arrow keys navigate results; Enter opens; Escape closes dropdown
- Debounce 300ms before firing search query
- Result items: 48px height with thumbnail, title, and meta

TV

- Dedicated search screen — not inline in AppBar
- On-screen keyboard or voice search integration
- Results rendered as card grid navigable with D-pad
- Recent searches shown when query is empty

## Accessibility

Search must be fully operable by keyboard, screen reader, and switch access. All live regions and ARIA roles are required — not optional.

## Related tokens

Tokens that drive the search input's visual states, sizing, and motion. Use these aliases — never hardcode pixel values.

| Token | Value | Usage |
|---|---|---|
| `--input-s-h` | 36px / 38px / 56px | Compact search bar height — mobile / web / TV |
| `--input-m-h` | 44px / 44px / 64px | Standard search bar height — mobile / web / TV |
| `--input-l-h` | 54px / 52px / 72px | Full / hero search bar height — mobile / web / TV |
| `--r4` | 14px | Default input container border-radius |
| `--border-subtle` | rgba(255,255,255,.06) | Default unfocused border |
| `--jio` | #00A859 | Focus border color, leading icon on focus |
| `--surface-2` | #161A24 | Input container background |
| `--text3` | rgba(244,242,238,.32) | Leading icon color (default), placeholder text |
| `--dur-default` | 200ms | Border color transition on focus/blur |
| `--ease-out` | cubic-bezier(0,.6,.4,1) | Easing for focus ring appearance and panel slide-in |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-search` | Root — relative container |
| `.ds-search__input` | Input field — leading search icon, trailing clear |
| `.ds-search__results` | Dropdown results panel — surface-2, r4, shadow |
| `.ds-search__result-item` | Single result row — 48px, thumbnail + title + meta |
| `.ds-search__empty` | No results message — centered, text3 |
| `.ds-search__loading` | Loading spinner inside the input trailing area |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | undefined | Controlled input value |
| `onChange` | (v: string) => void | undefined | Input change handler |
| `results` | SearchResult[] | undefined | Result items to display |
| `onResultSelect` | (result: SearchResult) => void | undefined | Result click handler |
| `loading` | boolean | false | Show loading indicator |
| `placeholder` | string | "Search games…" | Input placeholder |
| `autoFocus` | boolean | false | Focus input on mount |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<form class="search-bar" role="search" aria-label="Search games">
  <svg class="icon icon--m search-bar__icon" aria-hidden="true">
    <use href="/sprite.svg#ic_search"></use>
  </svg>
  <input
    class="input-field search-bar__input"
    type="search"
    placeholder="Search games, genres, publishers…"
    aria-label="Search"
    autocomplete="off"
    spellcheck="false"
  >
  <button class="btn btn--icon search-bar__clear" aria-label="Clear search" hidden>✕</button>
</form>
````

````
<ul class="ds-list" role="listbox" aria-label="Search results">
  <li class="ds-list-item" role="option">
    <div class="card__art" style="width:40px;height:40px;border-radius:var(--r3);flex-shrink:0"></div>
    <div class="ds-list-item__body">
      <div class="ds-list-item__label">War Thunder</div>
      <div class="ds-list-item__meta">Action · Free to play</div>
    </div>
  </li>
  <li class="ds-list-item" role="option">
    <div class="card__art" style="width:40px;height:40px;border-radius:var(--r3);flex-shrink:0"></div>
    <div class="ds-list-item__body">
      <div class="ds-list-item__label">Tomb Raider</div>
      <div class="ds-list-item__meta">Adventure · Pass included</div>
    </div>
  </li>
</ul>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--glass-1`
- `--gold`
- `--jio`
- `--jio-font`
- `--negative`
- `--r3`
- `--r4`
- `--state-disabled-opacity`
- `--surface-1`
- `--surface-2`
- `--text`
- `--text2`
- `--text3`
- `--tv-focus-shadow`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

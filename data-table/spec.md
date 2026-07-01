# Data Table — JioGames DLS spec

> Source: `data-table/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Data Table

---

Structured grid for leaderboards, achievement lists, game stats, and friend rankings. Supports sorting, selection, and row actions.

| # | Player | Game | Score *↓* | Time |
|---|---|---|---|---|
| 1 | AKArjunKing99 | Tomb Raider | 1,24,850 | 2h 14m |
| 2 | PSPriyaStar | Tomb Raider | 1,18,200 | 2h 31m |
| 3 | RVRocketVeer | Yooka-Laylee | 98,500 | 1h 58m |
| 4 | NMNightMira | Vigilante | 84,100 | 3h 02m |
| 5 | KZKaranZap | Vigilante | 76,350 | 3h 17m |

Leaderboard table · rank highlights, sorted column, number alignment

Data Table renders structured rows and columns of information. It is the right component for leaderboards, achievement logs, session history, game stats comparisons, and friend rankings. The table supports column sorting, row selection, and compact or comfortable density modes. On mobile, it scrolls horizontally when columns exceed the viewport — always use `overflow-x: auto` on the wrapper.

- **Leaderboard** — rank badge in first column, score sorted descending, player avatar + name
- **Achievement list** — icon, name, description, earned date, XP value
- **Game stats** — metric labels, numeric values right-aligned, comparison columns
- **Selection** — checkboxes in first column, selected row gets a subtle green tint

- Right-align numeric columns — scores, times, counts, currency
- Left-align text columns — names, titles, descriptions
- Keep column headers under 3 words in title case
- Truncate long text with ellipsis and provide a tooltip on hover
- Show "No results" empty state when the table has zero rows
- Use sticky header when the table scrolls vertically beyond the viewport

- Show more than 5–6 columns on mobile — limit to 3–4 visible, swipe for more
- Use center-aligned text for body cells — it creates ragged columns
- Mix left and right alignment in the same column across header and body
- Use a table for a single column of items — use a List component instead
- Nest tables — avoid deeply nested table cells

| 1 Rank | Player | Score *↓* 2 |
|---|---|---|
| 1 4 | ArjunKing99 | 1,24,850 3 |
| 2 | PriyaStar | 1,18,200 |

1. 1 Table header (thead) Required Sticky or static header row. Uppercase 11px labels, text3 color. Sortable headers get sort icon and cursor:pointer. Sorted column uses --jio color. `font-size:11px; font-weight:700; text-transform:uppercase`
2. 2 Sort indicator Optional Arrow icon in sorted column header. aria-sort="ascending" or "descending" on the th element for screen readers. `aria-sort="descending"`
3. 3 Table cell (td) Required 14px body text. Numbers right-aligned with tabular-nums. Text left-aligned. Hover state: glass-1 background. Vertical-align: middle for all cells. `font-variant-numeric: tabular-nums`
4. 4 Selected row Optional Adds is-selected class to tr. Background shifts to a subtle green tint — rgba(0,168,89,.06) — to signal active selection without overpowering the content. `background: rgba(0,168,89,.06)`

## Variants

All variants share the same semantic HTML. Only CSS modifier classes on the table and wrapper change the visual treatment.

| Game *↓* | Genre | Rating |
|---|---|---|
| Tomb Raider | Action Adventure | 4.9 |
| Yooka-Laylee | Platformer | 4.5 |
| Vigilante | Action | 4.3 |

| Achievement | Game | XP | Earned |
|---|---|---|---|
| First Blood | Vigilante | 500 | 12 Jun |
| Speedrunner | Tomb Raider | 1,200 | 10 Jun |
| Completionist | Yooka-Laylee | 2,500 | 8 Jun |
| Untouchable | Vigilante | 800 | 5 Jun |

| # | Player | Score | Kills | Deaths | KD |
|---|---|---|---|---|---|
| 1 | ArjunKing99 | 8,420 | 24 | 3 | 8.0 |
| 2 | PriyaStar | 7,100 | 19 | 5 | 3.8 |
| 3 | RocketVeer | 6,800 | 17 | 6 | 2.8 |

|   | Game | Status | Playtime |
|---|---|---|---|
|   | Tomb Raider | Installed | 72h |
|   | Yooka-Laylee | Available | 14h |
|   | Vigilante | Available | 0h |

| # | Player | Score *↓* | Time |
|---|---|---|---|
| 1 | AKArjunKing99 | 1,24,850 | 2h 14m |
| 2 | PSPriyaStar | 1,18,200 | 2h 31m |
| 3 | RVRocketVeer | 98,500 | 1h 58m |

| Game | Duration | XP earned |
|---|---|---|
| Tomb Raider | 1h 22m | +840 |
| Vigilante | 45m | +320 |

## Sizes

Three density tiers control padding and font size. Use Compact for dashboards with many rows, Default for most surfaces, Comfortable for focused single-table views.

| Size | Header font | Body font | Cell padding | Use case |
|---|---|---|---|---|
| Compact | `10px` | `12px` | `8px 12px` | Dense dashboards, session logs, 10+ rows |
| Default | `11px` | `14px` | `12px 16px` | Leaderboards, achievement lists, general data |
| Comfortable | `11px` | `14px` | `16px 18px` | Hero stats tables, featured comparisons, 5 or fewer rows |

## States

Individual rows and header cells each have distinct states. Column sort state lives on the th element.

| State | Game | Score *↓* | Time |
|---|---|---|---|
| Default row | Yooka-Laylee | 98,500 | 1h 58m |
| Hover row | Vigilante | 84,100 | 3h 02m |
| Selected row | Tomb Raider | 1,24,850 | 2h 14m |
| Loading (skeleton) |   |   |   |
| No results — try adjusting your filters |   |   |   |

## Content guidance

- Use title case: "Player Name", not "player name" or "PLAYER NAME"
- Keep headers to 3 words maximum — shorten "Time Played" to "Playtime"
- Abbreviate only when meaning is unambiguous: "XP", "KD", "Lvl"
- Add a tooltip for abbreviations where the full label adds clarity

- Numbers always right-aligned — never center or left
- Text always left-aligned
- Truncate long text at 1 line with ellipsis; surface full text in a tooltip
- Use "—" (em dash) for empty or unavailable values, never blank
- Format numbers with locale-appropriate separators: 1,24,850 not 124850

## Platform considerations

- Wrap table in `overflow-x: auto` — never shrink columns to fit
- Show 3–4 columns max in the visible viewport; allow swipe to reveal more
- Freeze the first column (rank or name) using `position: sticky; left: 0`
- Use Compact size for any table with more than 6 rows
- Avoid row selection on mobile — use a long-press action sheet instead

- Sticky header with `position: sticky; top: 0` for long tables
- Full column set visible — no horizontal scroll needed
- Sortable columns — click header to toggle ascending/descending
- Row selection with checkboxes and keyboard support (Space to toggle)
- Comfortable or Default size depending on content density

- D-pad navigates rows; OK button triggers the row action
- Focused row gets a prominent highlight border
- Limit visible columns to 4 — TV resolution does not benefit from density
- Use Comfortable size — minimum 48px row height for 3m legibility
- No sorting interaction on TV — pre-sort server-side

## Accessibility

| Element | Attribute / role | Guidance |
|---|---|---|
| Table | `role="grid"` | Use role="grid" for interactive tables (sortable, selectable). Use default table role for read-only leaderboards. |
| Header cells | `` | All header cells must have scope="col". Never use td elements as headers. |
| Sortable columns | `aria-sort="ascending|descending|none"` | Set aria-sort on the currently sorted th. All other sortable ths get aria-sort="none". |
| Row selection | `aria-selected` | Add aria-selected="true" to selected tr elements. Associate the checkbox with the row using aria-label="Select [row name]". |
| Skeleton rows | `aria-busy="true"` | Add aria-busy="true" to the table or tbody during loading, remove when data has loaded. |
| Empty state | `aria-live="polite"` | Wrap the empty-state td content in an aria-live region so screen readers announce when results change. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--border-subtle` | `rgba(255,255,255,.08)` | Row dividers and table wrapper border |
| `--surface-2` | `—` | thead background |
| `--glass-1` | `rgba(255,255,255,.04)` | Row hover background |
| `--jio` | `#00A859` | Sorted column header color, selected row tint base, rank gold accent for top score |
| `--text3` | `rgba(244,242,238,.32)` | Column header default color, rank number color |
| `--r5` | `—` | Table wrapper border-radius |
| `--jio-font` | `'Outfit', sans-serif` | All table text |

## When to use

Use when

- Sortable game library lists with multiple metadata columns
- Transaction history and subscription records
- Leaderboard rankings with stats columns
- Admin/internal dashboards with tabular data

Don't use when

- Mobile as a dense multi-column layout — collapse to cards or single column
- Simple 2-column key-value data — use a Description List
- Fewer than 3 rows — use a List instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Row hover | `--ease-out` | `80ms` | background |
| Sort arrow | `--ease-out` | `--dur-fast` | transform rotate, opacity |
| Row select | `--ease-out` | `--dur-fast` | background |
| Expand row | `--ease-out` | `--dur-fast` | max-height |
| Column resize drag | `none` | `realtime` | width |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-table` | Root table — border-collapse, full width |
| `.ds-table__head` | Header row — surface-2 bg |
| `.ds-table th` | Header cell — 11px 700 uppercase text3 |
| `.ds-table td` | Data cell — 13px text2, 48px row height |
| `.ds-table__row--selected` | Selected row — jio-green tint bg |
| `.ds-table__row--hover` | Hovered row — glass-1 bg |
| `.ds-table__sort-icon` | Sort direction indicator |
| `.ds-table__empty` | Empty state row — centered message |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `columns` | ColumnDef[] | required | Column schema with id, header, accessor |
| `data` | TData[] | required | Row data array |
| `sorting` | SortingState | undefined | Controlled sort state |
| `onSortingChange` | (s: SortingState) => void | undefined | Sort change handler |
| `rowSelection` | RowSelectionState | undefined | Controlled row selection |
| `onRowSelectionChange` | (s) => void | undefined | Selection change handler |
| `pageSize` | number | 20 | Rows per page |

## Code examples

Always wrap the table in `.data-table-wrap` for horizontal scroll containment.

````html
<div class="data-table-wrap">
  <table class="data-table" role="grid" aria-label="Game leaderboard">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Player</th>
        <th scope="col" class="num">Score</th>
        <th scope="col" class="num">Time</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="data-table-rank data-table-rank--gold">1</span></td>
        <td>ArjunKing99</td>
        <td class="num">1,24,850</td>
        <td class="num">2h 14m</td>
      </tr>
    </tbody>
  </table>
</div>
````

````
<!-- Sorted descending -->
<th scope="col"
    class="num is-sortable is-sorted"
    aria-sort="descending"
    onclick="sortTable('score', 'desc')">
  Score <i class="sort-icon">↓</i>
</th>

<!-- Unsorted but sortable -->
<th scope="col"
    class="num is-sortable"
    aria-sort="none"
    onclick="sortTable('time', 'asc')">
  Time
</th>
````

````
<table class="data-table" role="grid">
  <thead>
    <tr>
      <th scope="col" class="data-table-check">
        <input type="checkbox"
               aria-label="Select all rows"
               id="select-all">
      </th>
      <th scope="col">Game</th>
      <th scope="col" class="num">Playtime</th>
    </tr>
  </thead>
  <tbody>
    <tr class="is-selected" aria-selected="true">
      <td class="data-table-check">
        <input type="checkbox" checked
               aria-label="Select Tomb Raider">
      </td>
      <td>Tomb Raider</td>
      <td class="num">72h</td>
    </tr>
  </tbody>
</table>
````

## Changelog

Initial draft. Includes Default, Striped, Compact, Comfortable, Row selection, Leaderboard, and Borderless variants. Anatomy, states, platform guidance, and accessibility table documented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--negative`
- `--r5`
- `--surface-1`
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

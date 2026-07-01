# Calendar — JioGames DLS spec

> Source: `calendar/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Calendar

---

Month-view date grid for selecting dates. Used for game release schedules, event dates, and subscription renewal dates in JioGames. Not a full date-picker — pairs with the Date Picker component.

Calendar · June 2026 · today=26 (green) · selected=15 · event dots on release dates

The Calendar component renders a month-view grid of days for date selection. It is a low-level primitive — it is almost always used inside the Date Picker component, but can also be rendered standalone as a read-only event calendar for game release schedules and tournament dates. The Calendar does not manage its own state; the parent component or page controls the selected date(s).

- **Single select** — tap or click a day to select it; previous selection clears
- **Range select** — tap start date, then end date; days in between fill with tinted background
- **Read-only** — no day interaction, used for event calendars showing release schedules
- **Event dots** — small green dot below the day number marks dates with game releases or events

- Use event dots (not counts or numbers) for marking game release dates on the grid
- Keep today's date visually distinct with bold weight and green color even when not selected
- Navigate months only with prev/next arrows — do not offer a year/month dropdown in compact contexts
- Dim outside-month days to 40% opacity so the current month grid is the visual focus
- On mobile, make each day cell at least 40×40px for comfortable thumb tapping

- Show more than 3 event dots per day — link to a list view for days with many events
- Allow selecting disabled dates — pointer-events: none is not enough; block keyboard selection too
- Use the calendar as a navigation widget — it selects dates, it does not navigate to pages
- Render the calendar on TV — no pointer, D-pad date picking is unusable; use date text input instead
- Start weeks on a day other than Sunday in the JioGames context — India locale expectation

1. 1 Header Required Month + year label centred. Prev/next arrow buttons on either side. Header is always visible — never hidden. `border-bottom: 1px solid var(--border-subtle)`
2. 2 Weekday labels Required Single-letter abbreviated weekday headers (S M T W T F S). 11px bold, muted color. Not interactive. `font-size: 11px; font-weight: 700; color: var(--text3)`
3. 3 Day grid Required 7-column grid. Each day is a button with aspect-ratio 1. Outside-month days rendered but dimmed. Hover, today, selected, disabled, and range states applied as modifier classes. `display: grid; grid-template-columns: repeat(7, 1fr)`
4. 4 Event dot Optional 4×4px green dot via ::after pseudo-element. Only used in event calendar variant. Max one dot per day — not a count indicator. `width: 4px; height: 4px; background: var(--jio); border-radius: var(--pill)`

## Variants

Three usage modes — single select, range select, and read-only event view.

## Sizes

Three fixed widths — the grid scales proportionally within each. Always use the default (280px) inside Date Picker.

| Size | Width | Day font | Usage |
|---|---|---|---|
| Compact | `240px` | `11px` | Tight sidebars, popover contexts with limited space |
| Default | `280px` | `13px` | Date Picker popover, standalone inline calendar |
| Large | `320px` | `14px` | Full-page event calendar, release schedule view |

## States

Each day button carries one or more state modifier classes. States are mutually exclusive except has-event, which can combine with any day state.

## Content guidance

- Use event dots for marking game release dates — not for counts
- Never show more than one dot per day on the grid — link days with 3+ events to a list view
- Dot color is always `var(--jio)` — no semantic color variation
- On selected days, dot changes to `#000` for contrast against green fill

- Header format: "Month YYYY" — "June 2026", never "Jun '26" or "06/2026"
- Prev/next arrows only in compact contexts — no month/year dropdown
- Large standalone calendar may offer a year picker via header click
- Disable past months when calendar is used for future event booking

## Platform considerations

- Full-width calendar — no fixed 280px; spans container width
- Day cells minimum 44px height for comfortable thumb tapping
- Swipe left/right on the grid to change months
- Haptic feedback on day selection where OS supports it

- 280px fixed width, positioned below date input as a popover
- Arrow key navigation between days within the grid
- Page Up / Page Down changes months
- Home / End jumps to first/last day of current month

- Not applicable — D-pad date picking on a 7-column grid is unusable
- Use a date text input or pre-filled date chips instead
- Read-only event calendar can render on TV if not interactive

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Day grid container | `role="grid"` | `aria-label="June 2026"` — updates dynamically as month changes. |
| Day button | `role="gridcell"` | `aria-selected="true/false"`, `aria-disabled="true"` for disabled days. |
| Today | `aria-current="date"` | Applied to today's cell only. Screen readers announce "today" in addition to the date number. |
| Event dot | Visually hidden text | Add `, game release` inside the day button so the event is announced. |
| Keyboard nav | Arrow keys | ↑↓ moves week rows, ←→ moves days, Page Up/Down changes months. Focus must be managed manually — not native tab order. |
| Nav buttons | `aria-label` | "Previous month" and "Next month" — not just ‹ and ›. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | — | Calendar panel background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Panel border, header bottom border |
| `--jio` | `#00A859` | Selected day fill, today text color, event dot color |
| `--jio-soft` | `rgba(0,168,89,.12)` | In-range day background fill |
| `--glass-1` | `rgba(255,255,255,.05)` | Hovered day background |
| `--text3` | `rgba(244,242,238,.32)` | Weekday labels, nav arrow color |
| `--text4` | — | Outside-month day numbers |
| `--pill` | `100px` | Day cell border-radius (circle shape) |
| `--r5` | — | Calendar panel border-radius |

## When to use

Use when

- Event scheduling and date selection in forms
- Date range pickers for filters (e.g. subscription history)
- Booking flows where specific dates must be selected

Don't use when

- Selecting only a year or month — use a simpler select/dropdown
- Read-only date display — use a formatted text label
- Multiple independent calendars on the same screen

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Month change (next) | `--ease-out` | `--dur-fast` | transform translateX(-100% → 0), opacity |
| Month change (prev) | `--ease-out` | `--dur-fast` | transform translateX(100% → 0), opacity |
| Day select | `--ease-out` | `80ms` | background, transform scale |
| Range highlight | `--ease-out` | `--dur-fast` | background |
| Focus ring | `instant` | `0ms` | outline |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-calendar` | Root calendar container |
| `.ds-calendar__nav` | Month/year navigation row |
| `.ds-calendar__grid` | 7-column day grid |
| `.ds-calendar__day` | Individual day cell — 40×40px touch target |
| `.ds-calendar__day--selected` | Selected day — green fill |
| `.ds-calendar__day--today` | Today — green ring |
| `.ds-calendar__day--range` | In-range days — green tint fill |
| `.ds-calendar__day--disabled` | Non-selectable day — 38% opacity |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `mode` | "single" | "range" | "multiple" | "single" | Selection mode |
| `selected` | Date | DateRange | Date[] | undefined | Controlled selected value |
| `onSelect` | (date) => void | undefined | Fired on day selection |
| `disabled` | Matcher | Matcher[] | undefined | Disable specific dates or ranges |
| `fromDate` | Date | undefined | Minimum selectable date |
| `toDate` | Date | undefined | Maximum selectable date |

## Code examples

````html
<div class="calendar" role="group" aria-label="Date picker">
  <div class="calendar-header">
    <button class="calendar-nav" aria-label="Previous month">‹</button>
    <span class="calendar-month" aria-live="polite">June 2026</span>
    <button class="calendar-nav" aria-label="Next month">›</button>
  </div>
  <div class="calendar-grid">
    <div class="calendar-weekdays" role="row">
      <div class="calendar-weekday" role="columnheader" aria-label="Sunday">S</div>
      <div class="calendar-weekday" role="columnheader" aria-label="Monday">M</div>
      <!-- ...T W T F S -->
    </div>
    <div class="calendar-days" role="grid" aria-label="June 2026">
      <button class="calendar-day is-outside" role="gridcell" aria-disabled="true" tabindex="-1"></button>
      <button class="calendar-day" role="gridcell" aria-selected="false" tabindex="-1">1</button>
      <button class="calendar-day is-today" role="gridcell" aria-current="date" aria-selected="false" tabindex="0">26</button>
      <button class="calendar-day is-selected" role="gridcell" aria-selected="true" tabindex="-1">15</button>
      <!-- ...remaining days -->
    </div>
  </div>
</div>
````

````
<!-- Range: 10 Jun → 15 Jun -->
<button class="calendar-day is-range-start" role="gridcell" aria-selected="true"
  aria-label="10 June 2026, range start">10</button>

<button class="calendar-day is-in-range" role="gridcell" aria-selected="false"
  aria-label="11 June 2026, within selected range">11</button>
<button class="calendar-day is-in-range" role="gridcell" aria-selected="false"
  aria-label="12 June 2026, within selected range">12</button>
<!-- ...13, 14 -->

<button class="calendar-day is-range-end" role="gridcell" aria-selected="true"
  aria-label="15 June 2026, range end">15</button>
````

````
<!-- Event dot is purely decorative — hidden text carries meaning -->
<button class="calendar-day has-event" role="gridcell" aria-selected="false"
  aria-label="2 June 2026, game release">
  2
  <span class="sr-only">, game release</span>
</button>

<!-- sr-only utility class (add to your base CSS if not present) -->
<style>
.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border-width: 0;
}
</style>
````

## Changelog

Initial draft. Single select, range select, and read-only event variants. Three size tiers. Full day-state documentation, ARIA grid pattern, event dot accessible markup guidance.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--pill`
- `--r3`
- `--r5`
- `--surface-2`
- `--text`
- `--text-inv`
- `--text3`
- `--text4`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

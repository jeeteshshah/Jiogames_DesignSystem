# Date Picker — JioGames DLS spec

> Source: `date-picker/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Date Picker

---

Input + calendar popover combination for selecting a specific date. Used for subscription end dates, event RSVPs, and release date filters.

Date Picker · input open · June 2026 · 15th selected · Clear + Done actions

The Date Picker composes the Input Field and Calendar components into a single date-selection control. The text input displays the chosen date in "DD MMM YYYY" format — India-first, never MM/DD/YYYY. Clicking or tapping the input opens a calendar popover on web. On mobile, the same tap delegates to the native OS date picker for thumb-friendly selection.

- **Single date** — one input, one calendar popover, one selected date
- **Date range** — two adjacent inputs (From / To) sharing one calendar popover with range selection
- **Read-only display** — formatted date text, no interaction, used in confirmation screens

- Format dates as "DD MMM YYYY" — "15 Jun 2026" — everywhere in JioGames
- Show a clear (×) button inside the input whenever a date is selected
- Provide Done and Clear action buttons in the calendar footer so users can confirm or reset
- On mobile, open the native date picker — do not force the custom calendar on touch devices
- Label every date picker — "Subscription end date", "From", "To" — never unlabelled

- Use MM/DD/YYYY or DD/MM/YYYY format — JioGames is India-first and uses "15 Jun 2026"
- Allow free text entry into the date input — validate only on blur if you must allow typing
- Open the calendar popover on input focus via keyboard — open only on explicit click or Enter
- Close the popover when a date is tapped — wait for Done button so users can correct their choice
- Place the popover so it overflows the viewport — flip to above-input when screen space is tight

1. 1 Date input Required Text field showing selected date in "DD MMM YYYY". Placeholder "DD MMM YYYY". Green ring when popover is open. Calendar icon right-aligned. `aria-haspopup="dialog"; aria-expanded`
2. 2 Clear button Optional × button inside input, right of value text. Visible only when a date is selected. Clears selection and resets to placeholder. `aria-label="Clear date"`
3. 3 Calendar popover Required Calendar component rendered in a floating surface. Appears below input (flips above if viewport space is insufficient). Has elevation shadow. `role="dialog"; box-shadow: 0 8px 32px rgba(0,0,0,.5)`
4. 4 Action footer Required Clear (ghost) and Done (primary) buttons. Done commits selection and closes popover. Clear resets to no selection. `border-top: 1px solid var(--border-subtle)`

## Variants

Three composition patterns — single date, range (two inputs), and read-only display.

## Sizes

The input field height follows the standard Input Field size tokens. The calendar popover size is always Default (280px).

## States

Six states covering the full date picker lifecycle — from closed to error.

## Content guidance

- Always use "DD MMM YYYY" — "15 Jun 2026" not "15/06/2026" or "June 15, 2026"
- Placeholder text: "DD MMM YYYY" in muted color — never "Select a date"
- Month abbreviations: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
- Range display: "10 Jun 2026 – 15 Jun 2026" with en dash, not hyphen

- Label every picker — "Subscription end date", "Event date", "From", "To"
- Error message below input: "Enter a valid date" or "Date must be in the future"
- Never use red border alone — always pair with error message text
- For date ranges: validate that To date is after From date, error on the To field

## Platform considerations

- Tapping the input opens the **native OS date picker** — not the custom calendar
- Use `` hidden behind the styled input div
- Format the native picker's value back to "DD MMM YYYY" for display
- Minimum tap area for input: 48px height — do not use the compact M size on mobile

- Custom calendar popover — opens below input, flips above if viewport is tight
- Escape closes popover without committing selection
- Tab from input → calendar → Done button → next focusable element
- Popover closes on outside click only after Done or Clear is pressed

- Not applicable — use pre-filled date chips or read-only date text instead
- If user must enter a date, use three separate spinner controls (day / month / year)

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Date input | `aria-haspopup="dialog"` | `aria-expanded="true/false"` reflects popover open state. `aria-label` or associated `` required. |
| Calendar popover | `role="dialog"` | `aria-modal="true"`, `aria-label="Choose date"`. Focus moves into calendar on open. |
| Clear button | `aria-label="Clear date"` | Never just "×" — screen readers would announce "times" or nothing meaningful. |
| Error message | `role="alert"` | Injected below input on validation failure. `aria-describedby` on input pointing to error message ID. |
| Native fallback | `` | On mobile or when custom calendar is unavailable, native input provides full a11y without extra ARIA work. |
| Done button | Native button | `aria-label="Confirm date selection"` for clarity beyond the single-word label. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | — | Input background, calendar popover background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Input default border, calendar dividers |
| `--jio` | `#00A859` | Input focus ring, open calendar icon color, Done button background |
| `--negative` | `#FF4757` | Error state border and error message text color |
| `--r4` | — | Input border-radius |
| `--r5` | — | Calendar popover border-radius |
| `--text3` | `rgba(244,242,238,.32)` | Placeholder text, calendar icon default color, Clear button color |

## When to use

Use when

- Subscription start/end date selection in settings
- Event scheduling forms
- Filter panels with date range inputs
- Birthday or account creation date fields

Don't use when

- Relative time inputs ("in 3 days") — use a different control
- Date-only display without user interaction — use a formatted label
- Inline date selection in compact UI — use Calendar component directly

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Popover open | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |
| Popover close | `--ease-in` | `--dur-fast` | opacity |
| Month navigate | `--ease-out` | `--dur-fast` | transform translateX, opacity |
| Day select | `--ease-out` | `80ms` | background scale |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-date-picker` | Root — input + calendar popover |
| `.ds-date-picker__input` | Trigger input field showing formatted date |
| `.ds-date-picker__popover` | Floating calendar panel — surface-2, r4 |
| `.ds-date-picker__calendar` | Embedded Calendar component |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | Date | undefined | undefined | Controlled selected date |
| `onChange` | (date: Date | undefined) => void | undefined | Change handler |
| `placeholder` | string | "Pick a date" | Trigger input placeholder |
| `format` | string | "dd MMM yyyy" | Display format string |
| `disabled` | (date: Date) => boolean | undefined | Disable specific dates |
| `fromDate` | Date | undefined | Minimum selectable date |
| `toDate` | Date | undefined | Maximum selectable date |

## Code examples

````html
<div class="date-picker-wrap">
  <label for="dp-renewal" class="input-label">Renewal date</label>
  <div class="date-picker-input-wrap">
    <input
      id="dp-renewal"
      class="input-field"
      type="text"
      placeholder="DD MMM YYYY"
      readonly
      aria-haspopup="dialog"
      aria-expanded="false"
      aria-controls="dp-calendar"
      value="15 Jun 2026"
    />
    <button class="dp-clear-btn" aria-label="Clear date">×</button>
    <svg class="date-picker-icon" aria-hidden="true">...calendar icon...</svg>
  </div>
  <div
    id="dp-calendar"
    class="date-picker-popover"
    role="dialog"
    aria-modal="true"
    aria-label="Choose renewal date"
    hidden
  >
    <!-- Calendar component -->
    <div class="calendar">...</div>
    <div class="date-picker-actions">
      <button class="btn btn--ghost btn--s">Clear</button>
      <button class="btn btn--primary btn--s" aria-label="Confirm date selection">Done</button>
    </div>
  </div>
</div>
````

````
<fieldset style="border:none; padding:0; margin:0;">
  <legend class="input-label">Filter by release date</legend>
  <div style="display:flex; gap:12px;">

    <div class="date-picker-wrap">
      <label for="dp-from" class="input-label">From</label>
      <div class="date-picker-input-wrap">
        <input id="dp-from" class="input-field" type="text" placeholder="DD MMM YYYY"
          readonly aria-haspopup="dialog" aria-expanded="true" aria-controls="dp-range-cal"
          value="10 Jun 2026" />
        <button class="dp-clear-btn" aria-label="Clear from date">×</button>
        <svg class="date-picker-icon" aria-hidden="true">...</svg>
      </div>
    </div>

    <div class="date-picker-wrap">
      <label for="dp-to" class="input-label">To</label>
      <div class="date-picker-input-wrap">
        <input id="dp-to" class="input-field" type="text" placeholder="DD MMM YYYY"
          readonly aria-haspopup="dialog" aria-expanded="false" aria-controls="dp-range-cal" />
        <svg class="date-picker-icon" aria-hidden="true">...</svg>
      </div>
    </div>

  </div>
  <!-- Shared calendar popover for range -->
  <div id="dp-range-cal" class="date-picker-popover" role="dialog" aria-modal="true"
    aria-label="Choose date range">
    <div class="calendar">...range-enabled calendar...</div>
    <div class="date-picker-actions">
      <button class="btn btn--ghost btn--s">Clear</button>
      <button class="btn btn--primary btn--s">Done</button>
    </div>
  </div>
</fieldset>
````

````
<!-- With a selected date — shows clear button -->
<div class="date-picker-input-wrap">
  <input class="input-field" type="text" value="15 Jun 2026"
    aria-haspopup="dialog" aria-expanded="false" readonly />
  <button
    class="dp-clear-btn"
    aria-label="Clear date"
    onclick="this.closest('.date-picker-wrap').querySelector('input').value='';
             this.style.display='none';"
  >×</button>
  <svg class="date-picker-icon" aria-hidden="true">...</svg>
</div>

<!-- Error state -->
<div class="date-picker-input-wrap">
  <input class="input-field input-field--error" type="text" value="32 Jun 2026"
    aria-haspopup="dialog" aria-expanded="false" aria-describedby="dp-error" readonly />
  <svg class="date-picker-icon" aria-hidden="true" style="color:var(--negative);">...</svg>
</div>
<span id="dp-error" class="input-error" role="alert">Enter a valid date</span>
````

## Changelog

Initial draft. Single date, date range, and read-only variants. M and L input sizes. Six states documented. India-first date format rule (DD MMM YYYY) established. Mobile native picker guidance included.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--surface-2`
- `--text`
- `--text-inv`
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

#!/usr/bin/env python3
"""inject_a11y.py — injects Accessibility section into DLS component pages."""
import os, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP  = '/tmp/jiogames-dls-preview'

def make_a11y(aria_rows, keyboard_rows, notes):
    aria_trs = ''.join(
        f'<tr><td><code style="font-family:monospace;font-size:11px;color:var(--jio);background:rgba(0,168,89,.1);padding:2px 5px;border-radius:3px">{r[0]}</code></td><td style="color:var(--text2);font-size:12px">{r[1]}</td><td style="color:var(--text3);font-size:12px">{r[2]}</td></tr>'
        for r in aria_rows
    )
    kb_trs = ''.join(
        f'<tr><td><kbd style="font-family:monospace;font-size:11px;background:var(--surface-2);border:1px solid var(--border-subtle);border-radius:3px;padding:2px 6px;color:var(--text)">{r[0]}</kbd></td><td style="color:var(--text2);font-size:12px">{r[1]}</td></tr>'
        for r in keyboard_rows
    )
    notes_html = ''.join(
        f'<li style="font-size:13px;color:var(--text2);line-height:1.6;padding:5px 0;border-bottom:.5px solid var(--border-subtle)">{n}</li>'
        for n in notes
    )
    kb_section = f'''
    <h3 style="font-size:13px;font-weight:700;color:var(--text);margin:24px 0 10px">Keyboard interaction</h3>
    <table style="width:100%;border-collapse:collapse;border:1px solid var(--border-subtle);border-radius:var(--r3);overflow:hidden;font-size:12px">
      <thead><tr style="background:var(--surface-2)"><th style="text-align:left;padding:8px 12px;color:var(--text3);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">Key</th><th style="text-align:left;padding:8px 12px;color:var(--text3);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">Action</th></tr></thead>
      <tbody>{kb_trs}</tbody>
    </table>''' if keyboard_rows else ''

    return f'''
  <!-- ACCESSIBILITY -->
  <section class="ds-section" id="accessibility">
    <h2 class="ds-section-title">Accessibility</h2>
    <h3 style="font-size:13px;font-weight:700;color:var(--text);margin:16px 0 10px">ARIA attributes</h3>
    <table style="width:100%;border-collapse:collapse;border:1px solid var(--border-subtle);border-radius:var(--r3);overflow:hidden;font-size:12px">
      <thead><tr style="background:var(--surface-2)"><th style="text-align:left;padding:8px 12px;color:var(--text3);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">Attribute</th><th style="text-align:left;padding:8px 12px;color:var(--text3);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">Element</th><th style="text-align:left;padding:8px 12px;color:var(--text3);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">Value / notes</th></tr></thead>
      <tbody>{aria_trs}</tbody>
    </table>{kb_section}
    <h3 style="font-size:13px;font-weight:700;color:var(--text);margin:24px 0 10px">Guidelines</h3>
    <ul style="list-style:none;padding:0;margin:0">{notes_html}</ul>
  </section>
'''

# ── Component a11y data ────────────────────────────────────────────────────────

A11Y = {

'accordion': dict(
  aria=[
    ('role="region"', 'Panel body', 'Associates body with its trigger'),
    ('aria-expanded', 'Trigger button', '"true" when open, "false" when closed'),
    ('aria-controls', 'Trigger button', 'Points to the panel body ID'),
    ('aria-labelledby', 'Panel body', 'Points to the trigger button ID'),
    ('aria-disabled', 'Trigger button', '"true" when item is disabled'),
  ],
  kb=[
    ('Enter / Space', 'Toggle open/close state of focused item'),
    ('Tab', 'Move focus to next focusable element'),
    ('Shift+Tab', 'Move focus to previous focusable element'),
  ],
  notes=[
    'Trigger is a <button> element — not a div or span with a click handler',
    'Screen reader announces: "How does JioGames Pass work? collapsed button"',
    'Do not use aria-hidden on the panel body when open — content must be reachable',
    'Disabled items use aria-disabled="true", not the HTML disabled attribute (keeps it focusable)',
  ],
),

'badges': dict(
  aria=[
    ('aria-label', 'Badge element', 'Full description e.g. "12 unread notifications"'),
    ('aria-live="polite"', 'Badge wrapper', 'Announces count changes to screen readers'),
    ('aria-hidden="true"', 'Decorative badge', 'When parent element label already includes count'),
    ('role="status"', 'Live badge container', 'For badges that update dynamically'),
  ],
  kb=[],
  notes=[
    'Do not rely on color alone — badge shape and position also convey status',
    'Count-only badges need aria-label with the full context: "3 new messages"',
    'Live badge updates should use aria-live="polite" — not "assertive" (too disruptive)',
    'When badge is purely decorative (parent already announces count), add aria-hidden="true"',
  ],
),

'banners': dict(
  aria=[
    ('role="banner"', 'Root element (page-level)', 'Use for page-wide system messages'),
    ('role="alert"', 'Root element (error)', 'Announces immediately to screen readers'),
    ('role="status"', 'Root element (success/info)', 'Announces politely on next idle'),
    ('aria-live="assertive"', 'Error banners', 'Urgent messages read immediately'),
    ('aria-live="polite"', 'Info/success banners', 'Non-urgent — read after current speech'),
    ('aria-label', 'Dismiss button', '"Dismiss banner"'),
  ],
  kb=[
    ('Tab', 'Move focus to dismiss button or action link inside banner'),
    ('Enter / Space', 'Activate dismiss or action CTA'),
    ('Escape', 'Dismiss banner (if dismissible)'),
  ],
  notes=[
    'Error banners use role="alert" — they interrupt screen reader speech immediately',
    'Info/success banners use role="status" — polite, non-interrupting announcement',
    'Auto-dismissing banners must give screen reader users enough time to read (min 8s)',
    'Dismiss button must have a visible focus ring and descriptive aria-label',
  ],
),

'calendar': dict(
  aria=[
    ('role="grid"', 'Day grid table', 'Identifies the calendar as a grid widget'),
    ('role="gridcell"', 'Each day cell', 'Individual selectable cells'),
    ('aria-selected="true"', 'Selected day', 'Marks currently selected date'),
    ('aria-disabled="true"', 'Disabled day', 'Out-of-range or blocked dates'),
    ('aria-label', 'Day cell', 'Full date: "June 15, 2025"'),
    ('aria-current="date"', 'Today cell', 'Marks the current date'),
    ('aria-live="polite"', 'Month heading', 'Announces month change on navigation'),
  ],
  kb=[
    ('Arrow keys', 'Navigate between day cells'),
    ('Enter / Space', 'Select focused day'),
    ('Page Up', 'Go to previous month'),
    ('Page Down', 'Go to next month'),
    ('Home', 'Go to first day of current week'),
    ('End', 'Go to last day of current week'),
    ('Escape', 'Close calendar popover'),
  ],
  notes=[
    'Screen reader announces date in full: "15 June 2025, Sunday"',
    'Selected range announces start and end: "June 15 to June 20 selected"',
    'Month navigation buttons need aria-label: "Previous month", "Next month"',
    'Today indicator must also be conveyed in text, not just visually',
  ],
),

'cards': dict(
  aria=[
    ('role="article"', 'Interactive card', 'When card represents a self-contained item'),
    ('aria-label', 'Card link/button', 'Full card description if title is not sufficient'),
    ('aria-describedby', 'Card container', 'Points to metadata (rating, genre) for richer context'),
    ('tabindex="0"', 'Non-anchor interactive card', 'Makes div-based card keyboard focusable'),
  ],
  kb=[
    ('Tab', 'Move focus to next card'),
    ('Enter', 'Activate card link or action'),
    ('Space', 'Activate card button (if not a link)'),
  ],
  notes=[
    'Interactive cards should be <a> elements — not <div> with onClick',
    'Card title must be unique across the page — duplicate "View game" links fail accessibility',
    'Badge overlays need aria-label on the card or badge itself: "New — Tomb Raider"',
    'Images inside cards need descriptive alt text: alt="Tomb Raider game cover art"',
    'Locked/unavailable cards need aria-disabled and explanation in aria-describedby',
  ],
),

'carousel-component': dict(
  aria=[
    ('role="region"', 'Root carousel', 'With aria-label="Featured games carousel"'),
    ('aria-label', 'Root carousel', 'Describes the carousel purpose'),
    ('aria-roledescription="slide"', 'Each slide', 'Announces "slide" instead of "group"'),
    ('aria-label', 'Each slide', '"Slide N of M" — e.g. "Slide 1 of 5"'),
    ('aria-live="polite"', 'Slide region', 'Announces slide changes during auto-play'),
    ('aria-label', 'Prev/next buttons', '"Previous slide" / "Next slide"'),
    ('aria-current="true"', 'Active dot', 'Marks active page dot'),
  ],
  kb=[
    ('Tab', 'Move focus to interactive elements within slides'),
    ('Arrow Left/Right', 'Advance slides when carousel region is focused'),
    ('Enter / Space', 'Activate slide CTA or navigate to game'),
  ],
  notes=[
    'Auto-play must pause when carousel receives keyboard focus or hover',
    'Auto-play must respect prefers-reduced-motion — disable animation if set',
    'Provide a pause/play button for auto-playing carousels',
    'Each slide must have a unique, meaningful label — not just "Slide 1"',
  ],
),

'chart': dict(
  aria=[
    ('role="img"', 'Chart canvas', 'Identifies canvas as an image for screen readers'),
    ('aria-label', 'Chart canvas', 'Summary of what the chart shows'),
    ('aria-describedby', 'Chart canvas', 'Points to a hidden text description of the data'),
    ('aria-hidden="true"', 'Decorative legend swatches', 'Color boxes are visual only'),
  ],
  kb=[
    ('Tab', 'Focus the chart canvas element'),
    ('Arrow keys', 'Navigate data points (if interactive chart)'),
  ],
  notes=[
    'Every chart must have a text alternative: aria-label or a visually-hidden description',
    'Do not rely on color alone to distinguish series — use pattern fills or distinct shapes',
    'Provide a data table fallback below the chart for users who cannot interpret visuals',
    'Tooltip data must be reachable without hovering — consider always-visible data labels',
    'Color palette must pass WCAG AA contrast against the dark background',
  ],
),

'chips': dict(
  aria=[
    ('role="option"', 'Filter chip in group', 'When chips are inside a listbox'),
    ('aria-selected', 'Filter chip', '"true" when selected, "false" when not'),
    ('aria-pressed', 'Toggle chip', '"true" / "false" for standalone toggle chips'),
    ('aria-label', 'Input chip dismiss', '"Remove Action genre filter"'),
    ('role="listbox"', 'Chip group container', 'When chips represent selectable options'),
    ('aria-multiselectable="true"', 'Chip group', 'Allows multiple selections'),
  ],
  kb=[
    ('Enter / Space', 'Toggle chip selected state'),
    ('Delete / Backspace', 'Remove chip (input/removable chips)'),
    ('Tab', 'Move focus to next chip or element'),
  ],
  notes=[
    'Selected state must not rely on color alone — use aria-selected plus a visible indicator',
    'Chip group needs an accessible name: aria-label="Filter by genre"',
    'Removable chips: the × button needs its own label — not just "×"',
    'Screen reader announces: "Action, selected, 1 of 8" in a listbox context',
  ],
),

'collapsible': dict(
  aria=[
    ('aria-expanded', 'Trigger button', '"true" when open, "false" when closed'),
    ('aria-controls', 'Trigger button', 'ID of the collapsible content panel'),
    ('aria-hidden', 'Chevron icon', '"true" — decorative; direction conveyed by aria-expanded'),
  ],
  kb=[
    ('Enter / Space', 'Toggle open/close'),
    ('Tab', 'Move to next focusable element'),
  ],
  notes=[
    'Trigger must be a <button> — not a styled div',
    'Content panel is not aria-hidden when closed — use CSS max-height:0 + overflow:hidden',
    'Screen reader announces: "Show advanced options, collapsed, button"',
    'If used for show-more text, ensure collapsed state does not cut off mid-sentence',
  ],
),

'combobox': dict(
  aria=[
    ('role="combobox"', 'Input field', 'Identifies the pattern'),
    ('aria-expanded', 'Input field', '"true" when dropdown is open'),
    ('aria-haspopup="listbox"', 'Input field', 'Signals dropdown type'),
    ('aria-autocomplete="list"', 'Input field', 'Filtering behavior'),
    ('aria-activedescendant', 'Input field', 'ID of currently highlighted option'),
    ('role="listbox"', 'Options container', 'Contains all option elements'),
    ('role="option"', 'Each option', 'Individual selectable item'),
    ('aria-selected', 'Each option', '"true" for selected item(s)'),
  ],
  kb=[
    ('Alt+Down', 'Open dropdown'),
    ('Escape', 'Close dropdown, retain value'),
    ('Arrow Down/Up', 'Navigate options'),
    ('Enter', 'Select highlighted option'),
    ('Delete/Backspace', 'Remove last chip (multi-select)'),
  ],
  notes=[
    'Full combobox ARIA pattern per WAI-ARIA 1.2 spec',
    'Do not set aria-activedescendant to an ID that does not exist in the DOM',
    'Empty results state must be announced: role="status" with "No results found"',
    'Multi-select selected count announced: "3 genres selected"',
  ],
),

'command': dict(
  aria=[
    ('role="dialog"', 'Command palette root', 'Modal dialog pattern'),
    ('aria-modal="true"', 'Root', 'Prevents background content access'),
    ('aria-label', 'Root', '"Command palette"'),
    ('aria-label', 'Search input', '"Search commands"'),
    ('role="listbox"', 'Results container', 'Contains result options'),
    ('role="option"', 'Each result', 'Individual command option'),
    ('aria-selected', 'Highlighted result', '"true" on active item'),
    ('aria-live="polite"', 'Result count', 'Announces "N results" as user types'),
  ],
  kb=[
    ('⌘K / Ctrl+K', 'Open palette'),
    ('Escape', 'Close palette'),
    ('Arrow Down/Up', 'Navigate results'),
    ('Enter', 'Execute highlighted command'),
  ],
  notes=[
    'Focus must move into the search input on open; return to trigger on close',
    'Focus must be trapped inside the palette while open',
    'Screen reader announces result count on each filter change',
    'Keyboard shortcut labels are decorative — aria-hidden="true" on kbd elements',
  ],
),

'context-menu': dict(
  aria=[
    ('role="menu"', 'Menu panel', 'Context menu container'),
    ('role="menuitem"', 'Each item', 'Standard action item'),
    ('role="menuitemcheckbox"', 'Checkable item', 'Toggle action item'),
    ('aria-haspopup="menu"', 'Submenu trigger', 'Signals nested menu'),
    ('aria-expanded', 'Submenu trigger', '"true" when submenu is open'),
    ('aria-disabled', 'Disabled item', '"true" — keeps focusable but non-actionable'),
  ],
  kb=[
    ('Arrow Down/Up', 'Navigate menu items'),
    ('Enter / Space', 'Activate focused item'),
    ('Escape', 'Close menu'),
    ('Arrow Right', 'Open submenu'),
    ('Arrow Left / Escape', 'Close submenu, return focus to parent'),
  ],
  notes=[
    'Focus moves to first item on open; returns to trigger element on close',
    'Long-press trigger on mobile — announce as: "double tap to open menu"',
    'Destructive items should have aria-label clarifying the action: "Delete game save"',
    'Screen reader announces: "Context menu, Share game, menu item, 1 of 5"',
  ],
),

'data-table': dict(
  aria=[
    ('role="grid"', 'Table root (interactive)', 'For sortable/selectable tables'),
    ('aria-sort="ascending"', 'Sorted column header', '"ascending" | "descending" | "none"'),
    ('aria-selected', 'Row checkbox', '"true" when row is selected'),
    ('aria-label', 'Table root', 'Describes table purpose: "Game library"'),
    ('aria-rowcount', 'Table root', 'Total rows including paginated (if known)'),
    ('aria-rowindex', 'Each row', 'Row position in full dataset'),
    ('scope="col"', 'Column <th>', 'Associates header with column cells'),
  ],
  kb=[
    ('Tab', 'Move focus between interactive cells/controls'),
    ('Arrow keys', 'Navigate cells in grid mode'),
    ('Enter / Space', 'Activate sort or select row checkbox'),
    ('Shift+Space', 'Select current row'),
    ('Ctrl+A', 'Select all rows'),
  ],
  notes=[
    'Use <table>, <thead>, <tbody>, <th scope="col"> — not div-based table',
    'Sortable headers announce: "Game title, sort button, ascending"',
    'Empty state row spans all columns with role="status" message',
    'Pagination controls need aria-label: "Go to page 3 of 12"',
  ],
),

'date-picker': dict(
  aria=[
    ('role="combobox"', 'Date input field', 'Input that controls calendar popup'),
    ('aria-expanded', 'Date input', '"true" when calendar is open'),
    ('aria-haspopup="dialog"', 'Date input', 'Calendar renders as dialog'),
    ('aria-label', 'Date input', '"Select date" or field label'),
    ('role="dialog"', 'Calendar popup', 'Modal calendar container'),
    ('aria-modal="true"', 'Calendar popup', 'Traps focus inside calendar'),
    ('aria-label', 'Calendar dialog', 'E.g. "Choose booking date"'),
  ],
  kb=[
    ('Enter / Space', 'Open calendar from input'),
    ('Escape', 'Close calendar, return focus to input'),
    ('Arrow keys', 'Navigate days within calendar'),
    ('Page Up/Down', 'Navigate months'),
    ('Tab', 'Move between calendar controls (nav, days, close)'),
  ],
  notes=[
    'Input shows formatted date string — screen reader reads the formatted value',
    'Calendar dialog traps focus while open',
    'Disabled dates announced: "June 10, unavailable"',
    'After selection, focus returns to the date input field',
  ],
),

'dropdown-menu': dict(
  aria=[
    ('role="menu"', 'Dropdown panel', 'Menu widget container'),
    ('role="menuitem"', 'Standard item', 'Action item'),
    ('role="menuitemcheckbox"', 'Checkable item', 'Toggle item with aria-checked'),
    ('role="menuitemradio"', 'Radio group item', 'Exclusive selection item'),
    ('aria-haspopup="menu"', 'Trigger button', 'Signals dropdown type'),
    ('aria-expanded', 'Trigger button', '"true" when menu is open'),
    ('aria-disabled', 'Disabled item', '"true"'),
  ],
  kb=[
    ('Enter / Space / Arrow Down', 'Open menu, focus first item'),
    ('Escape', 'Close menu, return focus to trigger'),
    ('Arrow Down/Up', 'Navigate items'),
    ('Enter / Space', 'Activate item'),
    ('Arrow Right', 'Open submenu'),
  ],
  notes=[
    'Trigger must be a <button> with aria-haspopup and aria-expanded',
    'Menu opens with focus on first non-disabled item',
    'Screen reader announces: "More options menu button" then items as user navigates',
    'Checkable items announce checked state: "Dark mode, checked, menu item checkbox"',
  ],
),

'forms': dict(
  aria=[
    ('aria-required="true"', 'Required field inputs', 'Announces required before field label'),
    ('aria-invalid="true"', 'Error state inputs', 'Triggers error announcement'),
    ('aria-describedby', 'Input with hint/error', 'Points to hint or error message ID'),
    ('aria-errormessage', 'Input with error', 'Points to error message element'),
    ('aria-busy="true"', 'Form during submit', 'Announces form is processing'),
    ('role="alert"', 'Error summary', 'Read immediately on validation failure'),
    ('aria-labelledby', 'Fieldset/group', 'Labels a group of related fields'),
  ],
  kb=[
    ('Tab / Shift+Tab', 'Move between form fields'),
    ('Enter', 'Submit form (from any text field)'),
    ('Space', 'Toggle checkboxes and radio buttons'),
    ('Escape', 'Cancel inline edit (if applicable)'),
  ],
  notes=[
    'Error messages must be associated with their field via aria-describedby',
    'Required fields: use aria-required="true" — not just a visual asterisk',
    'On validation failure: focus moves to error summary or first error field',
    'Success state: announce via role="status" — "Profile saved successfully"',
    'Never use placeholder as the only label — it disappears on focus',
  ],
),

'hover-card': dict(
  aria=[
    ('role="tooltip"', 'Hover card root', 'If content is purely informational'),
    ('role="dialog"', 'Hover card root', 'If card contains interactive elements'),
    ('aria-describedby', 'Trigger element', 'Points to hover card ID for tooltip role'),
    ('aria-haspopup="dialog"', 'Trigger element', 'If card contains interactive content'),
    ('id', 'Hover card root', 'Required for aria-describedby association'),
  ],
  kb=[
    ('Tab', 'Focus trigger element — card opens'),
    ('Tab (inside card)', 'Navigate interactive elements within card'),
    ('Escape', 'Close card'),
  ],
  notes=[
    'Tooltip-role cards must not contain interactive elements — use dialog role instead',
    'Card must be keyboard accessible — appears on focus, not just hover',
    'Content inside card reachable by keyboard before card auto-closes',
    'Do not use hover card for critical information — touch users may never see it',
  ],
),

'lists': dict(
  aria=[
    ('role="list"', 'List container', 'Explicit list role (needed if CSS resets list styles)'),
    ('role="listitem"', 'Each row', 'Explicit list item role'),
    ('aria-label', 'List container', 'Describes list purpose: "Game library, 48 items"'),
    ('aria-selected', 'Selectable row', '"true" when row is selected'),
    ('aria-disabled', 'Disabled row', '"true"'),
    ('aria-live="polite"', 'List container', 'For dynamically updating lists'),
  ],
  kb=[
    ('Tab', 'Move focus to next focusable element in/after list'),
    ('Arrow Down/Up', 'Navigate rows (in grid/listbox pattern)'),
    ('Enter / Space', 'Activate row action'),
    ('Delete', 'Remove item (if swipe-to-delete equivalent)'),
  ],
  notes=[
    'Use <ul>/<li> elements — not <div> — for correct screen reader list semantics',
    'List count announced on focus: "Game library, list, 48 items"',
    'Section headers (grouped list) use role="group" with aria-label',
    'Swipe-to-delete actions need a keyboard equivalent (e.g. Delete key or action button)',
  ],
),

'menubar': dict(
  aria=[
    ('role="menubar"', 'Root bar', 'Identifies the bar as a menubar widget'),
    ('role="menu"', 'Each dropdown panel', 'Submenu container'),
    ('role="menuitem"', 'Each item', 'Standard menu action'),
    ('role="menuitemcheckbox"', 'Toggle item', 'Checkable menu item'),
    ('aria-haspopup="menu"', 'Top-level trigger', 'Signals dropdown'),
    ('aria-expanded', 'Top-level trigger', '"true" when menu is open'),
  ],
  kb=[
    ('Tab / Arrow Right', 'Move to next top-level menu trigger'),
    ('Enter / Space / Arrow Down', 'Open menu, focus first item'),
    ('Arrow Down/Up', 'Navigate open menu items'),
    ('Escape / Arrow Left', 'Close menu, return focus to trigger'),
    ('Arrow Left/Right (in menu)', 'Move to adjacent top-level menu'),
  ],
  notes=[
    'Full WAI-ARIA menubar pattern required — arrow key navigation within menus',
    'Keyboard shortcuts (⌘S etc.) are decorative — add aria-hidden="true" to kbd elements',
    'Screen reader announces: "File menu button, has popup menu"',
    'On close, focus must return to the trigger that opened the menu',
  ],
),

'navigation-menu': dict(
  aria=[
    ('role="navigation"', 'Root nav element', 'Landmark for screen reader navigation'),
    ('aria-label', 'Root nav', 'Distinguishes from other navs: "Main navigation"'),
    ('aria-haspopup="true"', 'Sub-menu trigger', 'Signals expandable content'),
    ('aria-expanded', 'Sub-menu trigger', '"true" when sub-menu is open'),
    ('aria-current="page"', 'Active nav link', 'Marks current page link'),
  ],
  kb=[
    ('Tab', 'Move between top-level nav items'),
    ('Enter / Space', 'Activate link or open sub-menu'),
    ('Arrow Down', 'Move into open sub-menu'),
    ('Arrow Up/Down', 'Navigate sub-menu items'),
    ('Escape', 'Close sub-menu, return to trigger'),
  ],
  notes=[
    'Use <nav> element — not <div role="navigation">',
    'Skip-nav link should appear before the menubar for keyboard users',
    'Active page link has aria-current="page" — screen reader announces "(current)"',
    'Mega-menu sub-panels use role="group" with aria-label per section',
  ],
),

'page-dots': dict(
  aria=[
    ('role="tablist"', 'Dots container', 'When dots control visible carousel panels'),
    ('role="tab"', 'Each dot', 'Selectable panel indicator'),
    ('aria-selected', 'Active dot', '"true" on current slide dot'),
    ('aria-label', 'Each dot', '"Go to slide N" or "Slide N of M"'),
    ('aria-controls', 'Each dot', 'ID of the slide panel it controls'),
    ('aria-label', 'Dots container', '"Slide navigation"'),
  ],
  kb=[
    ('Tab', 'Focus the dot indicator group'),
    ('Arrow Left/Right', 'Navigate between dots'),
    ('Enter / Space', 'Jump to selected slide'),
  ],
  notes=[
    'Purely decorative dots (when carousel has arrow buttons): role="presentation" on container',
    'Active dot must be distinguishable without color alone',
    'Screen reader announces: "Slide 1 of 5, selected" / "Slide 2 of 5"',
    'Carousel slide changes via dots are announced via aria-live on the slide region',
  ],
),

'popover': dict(
  aria=[
    ('role="dialog"', 'Popover panel (interactive)', 'When content includes form controls'),
    ('role="tooltip"', 'Popover panel (info only)', 'When purely informational'),
    ('aria-modal="true"', 'Dialog popover', 'Traps focus'),
    ('aria-label', 'Popover panel', 'Describes popover purpose'),
    ('aria-haspopup="dialog"', 'Trigger', 'Signals popover type'),
    ('aria-expanded', 'Trigger', '"true" when open'),
    ('aria-controls', 'Trigger', 'ID of popover panel'),
  ],
  kb=[
    ('Enter / Space', 'Open popover'),
    ('Escape', 'Close popover'),
    ('Tab', 'Navigate inside popover (dialog mode)'),
    ('Shift+Tab', 'Navigate backwards inside popover'),
  ],
  notes=[
    'Focus moves into popover on open; returns to trigger on close',
    'Dialog popovers trap focus — Tab must not escape the popover',
    'Tooltip popovers: no focus trap; Escape closes; focus stays on trigger',
    'Close button needs aria-label: "Close color picker"',
  ],
),

'resizable': dict(
  aria=[
    ('role="separator"', 'Drag handle', 'With aria-orientation'),
    ('aria-orientation', 'Drag handle', '"horizontal" | "vertical"'),
    ('aria-valuenow', 'Drag handle', 'Current panel size as percentage'),
    ('aria-valuemin', 'Drag handle', 'Minimum panel size (minSize prop)'),
    ('aria-valuemax', 'Drag handle', '"100" or available maximum'),
    ('aria-label', 'Drag handle', '"Resize panels" or contextual label'),
  ],
  kb=[
    ('Tab', 'Focus the resize handle'),
    ('Arrow Left/Right', 'Adjust horizontal split by 1%'),
    ('Arrow Up/Down', 'Adjust vertical split by 1%'),
    ('Home', 'Collapse panel to minimum size'),
    ('End', 'Expand panel to maximum size'),
  ],
  notes=[
    'Keyboard resize must be possible — drag-only is not accessible',
    'Handle announces current size: "Resize panels, 40 percent"',
    'After keyboard resize, focus stays on the handle',
    'Collapsed panel content must be hidden from screen readers (aria-hidden or display:none)',
  ],
),

'scroll-area': dict(
  aria=[
    ('role="region"', 'Scroll container', 'With aria-label for named scroll regions'),
    ('aria-label', 'Scroll container', '"Game list, scrollable" for named regions'),
    ('tabindex="0"', 'Scroll viewport', 'Makes scroll area keyboard focusable'),
    ('aria-orientation', 'Scrollbar', '"vertical" | "horizontal"'),
  ],
  kb=[
    ('Tab', 'Focus the scroll area viewport'),
    ('Arrow Up/Down', 'Scroll vertically'),
    ('Arrow Left/Right', 'Scroll horizontally'),
    ('Page Up/Down', 'Scroll by viewport height'),
    ('Home / End', 'Jump to scroll start/end'),
  ],
  notes=[
    'Scroll area viewport needs tabindex="0" to receive keyboard focus',
    'Custom scrollbar is visual only — keyboard scroll operates independently',
    'Screen reader announces: "Game list, scrollable region"',
    'Ensure content inside scroll area is not trapped — Tab must exit the region',
  ],
),

'select': dict(
  aria=[
    ('role="combobox"', 'Trigger button', 'Identifies select pattern'),
    ('aria-haspopup="listbox"', 'Trigger button', 'Signals dropdown type'),
    ('aria-expanded', 'Trigger button', '"true" when open'),
    ('aria-labelledby', 'Trigger button', 'Points to associated <label> element'),
    ('role="listbox"', 'Options container', 'Contains option elements'),
    ('role="option"', 'Each option', 'Selectable item'),
    ('aria-selected', 'Selected option', '"true"'),
    ('aria-disabled', 'Disabled option', '"true"'),
  ],
  kb=[
    ('Enter / Space / Arrow Down', 'Open dropdown'),
    ('Arrow Down/Up', 'Navigate options'),
    ('Enter / Space', 'Select focused option'),
    ('Escape', 'Close without changing selection'),
    ('Home / End', 'Jump to first/last option'),
    ('Type character', 'Jump to option starting with that letter'),
  ],
  notes=[
    'Screen reader announces: "Sort by, combo box, Relevance, collapsed"',
    'Type-ahead character search must work for finding options quickly',
    'Selected option announced on close: "Relevance, selected"',
    'Groups use role="group" + aria-label within the listbox',
  ],
),

'slider': dict(
  aria=[
    ('role="slider"', 'Thumb element', 'Identifies the slider control'),
    ('aria-valuenow', 'Thumb', 'Current numeric value'),
    ('aria-valuemin', 'Thumb', 'Minimum value'),
    ('aria-valuemax', 'Thumb', 'Maximum value'),
    ('aria-valuetext', 'Thumb', 'Human-readable value: "75%" or "High"'),
    ('aria-label', 'Thumb', '"Volume" or descriptive name'),
    ('aria-orientation', 'Root', '"horizontal" (default) | "vertical"'),
  ],
  kb=[
    ('Arrow Right/Up', 'Increase value by one step'),
    ('Arrow Left/Down', 'Decrease value by one step'),
    ('Page Up', 'Increase by 10 steps'),
    ('Page Down', 'Decrease by 10 steps'),
    ('Home', 'Set to minimum value'),
    ('End', 'Set to maximum value'),
  ],
  notes=[
    'aria-valuetext is preferred over aria-valuenow for non-numeric display values',
    'Screen reader announces on change: "Volume slider, 75 percent"',
    'Range slider: each thumb needs its own aria-label ("Start value" / "End value")',
    'Value tooltip during drag is aria-live — announced as value changes',
  ],
),

'tab-bar': dict(
  aria=[
    ('role="tablist"', 'Tab bar container', 'Identifies the navigation as a tab list'),
    ('role="tab"', 'Each tab item', 'Individual tab button'),
    ('aria-selected', 'Active tab', '"true" on current tab, "false" on others'),
    ('aria-controls', 'Each tab', 'ID of the associated tab panel (screen content)'),
    ('aria-label', 'Tab bar', '"Main navigation" or "App navigation"'),
    ('tabindex', 'Tabs', '0 on active tab, -1 on inactive (roving tabindex)'),
  ],
  kb=[
    ('Tab', 'Enter tab bar; focus active tab'),
    ('Arrow Left/Right', 'Navigate between tabs'),
    ('Enter / Space', 'Activate focused tab'),
    ('Home / End', 'Jump to first/last tab'),
  ],
  notes=[
    'Uses roving tabindex — only active tab is in tab order; arrows navigate others',
    'Screen reader announces: "Home, tab, 1 of 4, selected"',
    'Badge count announced as part of tab label: "Library, 3 new items, tab"',
    'Tab panels (screen content) need aria-labelledby pointing to their tab',
  ],
),

'tabs': dict(
  aria=[
    ('role="tablist"', 'Tab list container', 'Identifies the tab group'),
    ('role="tab"', 'Each tab trigger', 'Individual tab button'),
    ('aria-selected', 'Active tab', '"true" / "false"'),
    ('aria-controls', 'Tab trigger', 'ID of associated panel'),
    ('role="tabpanel"', 'Panel container', 'Content shown for active tab'),
    ('aria-labelledby', 'Tab panel', 'Points to its tab trigger ID'),
    ('tabindex', 'Tab panel', '0 — makes panel keyboard focusable'),
  ],
  kb=[
    ('Tab', 'Move focus to active tab trigger'),
    ('Arrow Left/Right', 'Navigate between tabs (activates automatically)'),
    ('Tab (from tab list)', 'Move focus into active tab panel content'),
    ('Home / End', 'Jump to first/last tab'),
  ],
  notes=[
    'Tabs follow WAI-ARIA Tab design pattern with automatic activation on arrow key',
    'Screen reader: "Overview, tab, 1 of 3, selected"',
    'Tab panel content reachable via Tab key after leaving the tab list',
    'Disabled tabs: aria-disabled="true"; do not remove from DOM — keep in focus order',
  ],
),

'textarea': dict(
  aria=[
    ('aria-required', 'Textarea', '"true" for required fields'),
    ('aria-invalid', 'Textarea', '"true" when validation fails'),
    ('aria-describedby', 'Textarea', 'Points to hint text and error message IDs'),
    ('aria-label', 'Textarea (no visible label)', 'Accessible name fallback'),
    ('aria-multiline="true"', 'Textarea', 'Redundant but harmless — already implicit'),
    ('aria-rowcount', 'Textarea', 'Current row count if dynamically announced'),
  ],
  kb=[
    ('Tab', 'Move focus into / out of textarea'),
    ('Shift+Tab', 'Move focus backwards'),
    ('Enter', 'Insert newline within textarea'),
    ('Ctrl+A', 'Select all text'),
  ],
  notes=[
    'Always use a visible <label> associated via htmlFor — placeholder is not a label',
    'Character count announced via aria-live="polite" as user types: "120 of 280 characters"',
    'Error message shown via aria-describedby — screen reader reads it on focus',
    'At max length: announce "Character limit reached" via role="alert"',
  ],
),

'toggle-group': dict(
  aria=[
    ('role="group"', 'Root container', 'Groups related toggle buttons'),
    ('aria-label', 'Root container', 'Describes purpose: "View mode"'),
    ('aria-pressed', 'Each toggle item', '"true" when selected, "false" when not'),
    ('aria-disabled', 'Disabled item', '"true"'),
  ],
  kb=[
    ('Tab', 'Enter group; focus first (or active) item'),
    ('Arrow Left/Right', 'Navigate between items (single-select: activates on move)'),
    ('Enter / Space', 'Toggle item state (multi-select mode)'),
    ('Home / End', 'Jump to first/last item'),
  ],
  notes=[
    'Single-select group: announce active item — "Grid view, pressed, 1 of 2"',
    'Multi-select group: announce state per item — "Bold, pressed"',
    'Group label narrows context: screen reader reads "View mode, Grid view, pressed"',
    'Icon-only items must have aria-label — tooltip text is not enough',
  ],
),

'tooltip': dict(
  aria=[
    ('role="tooltip"', 'Tooltip element', 'Identifies tooltip content'),
    ('aria-describedby', 'Trigger element', 'Points to tooltip ID'),
    ('id', 'Tooltip element', 'Required for aria-describedby reference'),
    ('aria-hidden="true"', 'Tooltip (when closed)', 'Prevents double-reading when trigger already has label'),
  ],
  kb=[
    ('Tab / focus', 'Show tooltip on trigger focus'),
    ('Escape', 'Dismiss tooltip'),
    ('Blur / Tab away', 'Hide tooltip'),
  ],
  notes=[
    'Tooltip text supplements the trigger label — it does not replace it',
    'Trigger element must have its own accessible name (button label or aria-label)',
    'Screen reader reads both trigger label and tooltip: "Share button, Share this game to social media"',
    'Do not put interactive content inside a tooltip — use Popover instead',
    'Max length ~80 characters — longer content should be in a Popover',
  ],
),

'tv-focus': dict(
  aria=[
    ('aria-label', 'Focusable element', 'Required when element has no visible text label'),
    ('tabindex="0"', 'Custom focusable element', 'Makes non-interactive elements focusable'),
    ('aria-pressed', 'Toggle button', '"true" / "false" state announcement'),
    ('aria-selected', 'Selectable card', '"true" when selected in a group'),
    ('aria-live="polite"', 'Dynamic content area', 'Announces content changes on D-pad navigation'),
  ],
  kb=[
    ('D-pad Up/Down/Left/Right', 'Move focus between elements'),
    ('OK / Enter', 'Activate focused element'),
    ('Back', 'Navigate back or cancel'),
    ('Options/Menu button', 'Open context actions for focused item'),
  ],
  notes=[
    'Focus ring must always be visible — never remove for aesthetic reasons on TV',
    'All interactive elements must be reachable via D-pad — no mouse-only interactions',
    'Focus order must be logical and predictable — follows visual layout',
    'Screen reader on TV reads focused element label and role on each D-pad move',
    'Spatial navigation: ensure no focus traps except modal dialogs',
    'Minimum WCAG AA contrast ratio 4.5:1 for text; 3:1 for UI components at 10-foot viewing',
  ],
),

}

# ── Injection logic ─────────────────────────────────────────────────────────────

def inject(comp_name, data, dry_run=False):
    path = os.path.join(BASE, comp_name, 'index.html')
    if not os.path.exists(path):
        return 'SKIP — not found'
    html = open(path, encoding='utf-8').read()
    if 'id="accessibility"' in html:
        return 'already complete'

    section = make_a11y(data['aria'], data['kb'], data['notes'])
    anchors = ['id="code-examples"', 'id="code"', 'id="api"', 'id="platform"']
    inserted = False
    for anchor in anchors:
        idx = html.find(anchor)
        if idx != -1:
            start = html.rfind('\n  <', 0, idx)
            if start != -1:
                html = html[:start] + section + html[start:]
                inserted = True
                break
    if not inserted:
        html = html.replace('</main>', section + '</main>', 1)

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        tmp_path = os.path.join(TMP, comp_name, 'index.html')
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        shutil.copy2(path, tmp_path)
    return 'injected'


if __name__ == '__main__':
    args = sys.argv[1:]
    targets = list(A11Y.keys()) if ('--all' in args or not args) else args
    print(f"\n{'Component':<24} Result")
    print('-' * 50)
    for name in targets:
        if name not in A11Y:
            print(f"  {name:<22} NOT IN DATA — skipped")
            continue
        print(f"  {name:<22} {inject(name, A11Y[name])}")
    print()

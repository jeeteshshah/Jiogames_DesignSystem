#!/usr/bin/env python3
"""
inject_vss.py — injects Variants, Sizes, States sections into DLS component pages.
Usage: python3 tools/inject_vss.py [component1 component2 ...]
       python3 tools/inject_vss.py --all
"""
import os, re, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP  = '/tmp/jiogames-dls-preview'

# ── Section builders ───────────────────────────────────────────────────────────

def chip(label, extra=''):
    return f'<span class="ds-variant-chip" style="display:inline-flex;align-items:center;gap:6px;background:var(--surface-1);border:1px solid var(--border-subtle);border-radius:var(--pill);padding:4px 12px;font-size:12px;font-weight:600;color:var(--text2);margin:4px 4px 0 0;{extra}">{label}</span>'

def make_variants(items):
    chips_html = ''.join(chip(v) for v in items)
    return f'''
  <!-- VARIANTS -->
  <section class="ds-section" id="variants">
    <h2 class="ds-section-title">Variants</h2>
    <div style="margin-top:16px;">{chips_html}</div>
  </section>
'''

def make_sizes(rows):
    trs = ''
    for r in rows:
        trs += f'\n        <tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3] if len(r)>3 else "-"}</td></tr>'
    return f'''
  <!-- SIZES -->
  <section class="ds-section" id="sizes">
    <h2 class="ds-section-title">Sizes</h2>
    <table class="ds-api-table" style="margin-top:16px;">
      <thead><tr><th>Size</th><th>Token / Height</th><th>Use case</th><th>Platform</th></tr></thead>
      <tbody>{trs}
      </tbody>
    </table>
  </section>
'''

def make_states(state_items):
    items_html = ''
    for s in state_items:
        name, desc = s[0], s[1]
        items_html += f'''
      <div style="background:var(--surface-1);border:1px solid var(--border-subtle);border-radius:var(--r3);padding:16px;">
        <p style="font-size:12px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:.6px;margin:0 0 6px;">{name}</p>
        <p style="font-size:13px;color:var(--text2);margin:0;line-height:1.5;">{desc}</p>
      </div>'''
    return f'''
  <!-- STATES -->
  <section class="ds-section" id="states">
    <h2 class="ds-section-title">States</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin-top:16px;">{items_html}
    </div>
  </section>
'''

# ── Component VSS data ─────────────────────────────────────────────────────────

VSS = {

'accordion': dict(
  variants=['Single (exclusive)', 'Multiple (non-exclusive)', 'Flush (no border)', 'Contained (card border)'],
  sizes=[
    ('Default', '56px row height', 'FAQ, settings', 'All'),
    ('Compact', '44px row height', 'Dense settings lists', 'Web / TV'),
  ],
  states=[
    ('Default', 'All items closed; trigger shows chevron pointing down'),
    ('Expanded', 'Item open; chevron rotates 180°; body slides down; trigger turns jio-green'),
    ('Disabled', '38% opacity on trigger; pointer-events none; body inaccessible'),
    ('Focus', '2px jio-green outline on trigger via :focus-visible'),
    ('Hover', 'Glass-1 background on trigger; subtle affordance'),
  ],
),

'aspect-ratio': dict(
  variants=['16:9 (default)', '4:3', '1:1 (square)', '3:4 (portrait)', '21:9 (cinematic)'],
  sizes=[
    ('16:9', 'padding-top 56.25%', 'Game hero, video', 'All'),
    ('4:3', 'padding-top 75%', 'Legacy thumbnails', 'All'),
    ('1:1', 'padding-top 100%', 'Avatar, icon tile', 'All'),
    ('3:4', 'padding-top 133%', 'Cover art portrait', 'Mobile'),
  ],
  states=[
    ('Loading', 'Shows skeleton shimmer at the enforced ratio while image loads'),
    ('Loaded', 'Image fades in at full opacity; maintains ratio'),
    ('Error', 'Fallback placeholder icon centred in the ratio container'),
    ('Empty', 'Transparent container maintains layout space'),
  ],
),

'badges': dict(
  variants=['Default (count)', 'Dot (no text)', 'New', 'Hot', 'Live (pulsing)', 'Sale', 'Pass tier'],
  sizes=[
    ('Dot', '8px circle', 'Unread indicator on icon', 'All'),
    ('Small', '16px height', 'Inline status label', 'All'),
    ('Default', '20px height', 'Notification count', 'All'),
  ],
  states=[
    ('Default', 'Visible with count or label text'),
    ('Zero (hidden)', 'count=0 without showZero prop hides the badge entirely'),
    ('Overflow (99+)', 'Counts above max prop show "99+" or configured max+"+"'),
    ('Live (pulsing)', 'Red badge with radial pulse animation for real-time events'),
    ('Disabled parent', 'Badge remains visible even when parent element is disabled'),
  ],
),

'banners': dict(
  variants=['Info (blue)', 'Success (green)', 'Warning (amber)', 'Error (red)', 'Pass promo (green gradient)'],
  sizes=[
    ('Default', '56–80px height', 'Full-width system message', 'All'),
    ('Compact', '44px height', 'Slim notification strip', 'Web / TV'),
  ],
  states=[
    ('Visible', 'Banner fully rendered at top of screen or section'),
    ('Dismissing', 'Slides up/fades out on dismiss; max-height collapses'),
    ('Dismissed', 'Removed from DOM; no space reserved'),
    ('With action', 'Inline link CTA on the right; tappable'),
    ('Loading (pass)', 'Skeleton shimmer while pass status resolves'),
  ],
),

'bottom-sheet': dict(
  variants=['Default (half-height)', 'Full-height', 'Snap multi-point', 'Inline (no scrim)', 'Pass upsell'],
  sizes=[
    ('Half', '50vh default height', 'Context actions, filters', 'Mobile'),
    ('Three-quarter', '75vh snap point', 'Rich content panels', 'Mobile'),
    ('Full', '90vh snap point', 'Full-screen overlays', 'Mobile'),
  ],
  states=[
    ('Closed', 'Translated 100% off-screen; scrim hidden'),
    ('Opening', 'Slides up with ease-out; scrim fades in simultaneously'),
    ('Open', 'Resting at default snap point; draggable handle visible'),
    ('Dragging', 'Follows finger position in real time; no animation'),
    ('Snapping', 'Releases to nearest snap point with ease-out spring'),
    ('Closing', 'Slides down; scrim fades out'),
  ],
),

'calendar': dict(
  variants=['Single date', 'Date range', 'Multiple dates', 'Embedded (no popover)', 'With presets'],
  sizes=[
    ('Default', '280px width, 36px day cells', 'Forms, popovers', 'Web / Mobile'),
    ('Compact', '240px width, 28px day cells', 'Dense panels', 'Web'),
    ('Large', '320px width, 44px day cells', 'Standalone pickers', 'Web / TV'),
  ],
  states=[
    ('Default', 'Current month displayed; today highlighted with green ring'),
    ('Day selected', 'Solid jio-green fill on selected day cell'),
    ('Range start/end', 'Filled endpoints with green tint on in-between cells'),
    ('Disabled day', '38% opacity; not clickable; cursor not-allowed'),
    ('Hover', 'Light glass-1 background on hovered day cell'),
    ('Focus', '2px jio-green outline on focused day via keyboard'),
    ('Out of month', 'Days from adjacent months shown at 30% opacity'),
  ],
),

'cards': dict(
  variants=['Game tile (landscape)', 'Cover (portrait)', 'Pass plan', 'Editorial (wide)', 'Leaderboard row', 'Continue card'],
  sizes=[
    ('Wide landscape', '210×128px', 'Rails, continue rows', 'Mobile'),
    ('Portrait cover', '120×180px', 'Browse grid', 'Mobile'),
    ('Standard', '160×200px', 'Grid layouts', 'Web'),
    ('TV card', '240×150px', 'TV rail', 'TV'),
  ],
  states=[
    ('Default', 'Resting state; border-subtle; surface-1 background'),
    ('Hover', 'Scale 1.02; elevated shadow; image brightens slightly'),
    ('Pressed', 'Scale 0.97 with ease-out; quick feedback tap'),
    ('TV focused', 'Scale 1.06; jio-glow box-shadow ring'),
    ('Loading (skeleton)', 'Shimmer placeholder at card dimensions'),
    ('Unavailable', '50% overlay with lock icon; muted title'),
  ],
),

'carousel-component': dict(
  variants=['Full-width hero', 'Card carousel (partial peek)', 'Fade transition', 'Auto-play', 'Manual only'],
  sizes=[
    ('Hero', 'Full viewport width, 200–400px height', 'Home hero banner', 'Mobile / Web'),
    ('Card peek', 'Card width + 24px margin peek', 'Feature highlights', 'Mobile'),
    ('TV hero', '100% width, 40vh height', 'TV home screen', 'TV'),
  ],
  states=[
    ('Default', 'First slide visible; dot indicator shows position 1'),
    ('Sliding', 'Track translates with ease-out; active dot transitions'),
    ('Auto-playing', 'Timer running; pauses on user interaction for 8s'),
    ('Paused', 'Auto-play suspended; user is interacting'),
    ('Last slide (no loop)', 'Next arrow/swipe disabled; dot shows end position'),
    ('Loading', 'Skeleton at full carousel dimensions until images load'),
  ],
),

'chart': dict(
  variants=['Bar', 'Line', 'Area', 'Donut', 'Radial / gauge'],
  sizes=[
    ('Compact', '120px height', 'Sparkline / inline stat', 'Web'),
    ('Default', '240px height', 'Dashboard cards', 'Web'),
    ('Large', '360px height', 'Full-width analytics view', 'Web / TV'),
  ],
  states=[
    ('Loading', 'Skeleton rectangle at chart dimensions while data fetches'),
    ('Loaded', 'Chart renders with entrance animation (bars grow, lines draw)'),
    ('Empty', 'Centered empty state — "No data for this period"'),
    ('Error', 'Error icon + retry CTA at chart area'),
    ('Hover (tooltip)', 'Data point or bar highlighted; tooltip appears with values'),
    ('Legend item toggled', 'Associated series dims to 40% opacity'),
  ],
),

'chips': dict(
  variants=['Filter chip (toggle)', 'Input chip (removable)', 'Status chip (read-only)', 'Suggestion chip'],
  sizes=[
    ('Small', '28px height, 12px font', 'Dense filter rows', 'Mobile / Web'),
    ('Default', '36px height, 13px font', 'Standard filter pills', 'All'),
  ],
  states=[
    ('Default', 'Surface-1 background; border-subtle; text2 label'),
    ('Selected', 'Jio-green fill; white label; green border'),
    ('Hover', 'Glass-1 background tint; cursor pointer'),
    ('Pressed', 'Scale 0.95; immediate feedback'),
    ('Disabled', '38% opacity; no pointer events'),
    ('Focus', '2px jio-green outline via :focus-visible'),
    ('With remove (hover)', 'X icon brightens to full opacity on chip hover'),
  ],
),

'collapsible': dict(
  variants=['Default (chevron trigger)', 'Custom trigger', 'With icon', 'Borderless'],
  sizes=[
    ('Default', 'Content height auto', 'General purpose', 'All'),
    ('Compact trigger', '40px trigger height', 'Dense settings', 'Web'),
  ],
  states=[
    ('Closed', 'Content height 0; overflow hidden; chevron points down'),
    ('Open', 'Content fully visible; chevron rotates 180deg'),
    ('Animating open', 'max-height expanding with ease-out'),
    ('Animating close', 'max-height collapsing with ease-in'),
    ('Disabled', 'Trigger not clickable; 38% opacity'),
  ],
),

'combobox': dict(
  variants=['Single select', 'Multi-select (chips)', 'Creatable (add new)', 'Async (search API)', 'Grouped options'],
  sizes=[
    ('Default', '48px trigger height', 'Standard forms', 'All'),
    ('Compact', '36px trigger height', 'Inline selectors', 'Web'),
  ],
  states=[
    ('Closed', 'Shows selected value or placeholder; chevron down'),
    ('Open', 'Dropdown visible; input focused; options listed'),
    ('Typing', 'Options filtered by query; loading spinner if async'),
    ('Option highlighted', 'Glass-1 background on keyboard/hover active option'),
    ('Option selected', 'Checkmark on selected item; chip added if multi'),
    ('Empty', 'No results message with optional "Add" CTA'),
    ('Disabled', '38% opacity; dropdown does not open'),
    ('Error', 'Red border on trigger; error message below'),
  ],
),

'command': dict(
  variants=['Default (⌘K palette)', 'Search-only', 'With groups', 'With shortcuts display'],
  sizes=[
    ('Default', '480px max-width, 400px max-height', 'Web command palette', 'Web'),
    ('Compact', '360px width', 'Embedded panel', 'Web'),
  ],
  states=[
    ('Closed', 'Not rendered; keyboard shortcut awaited'),
    ('Open', 'Centered overlay with scrim; input auto-focused'),
    ('Typing', 'Results filter in real time below input'),
    ('Item highlighted', 'Glass-1 background on arrow-key or hover selection'),
    ('Empty', 'Centered "No results" message'),
    ('Loading', 'Spinner in input trailing area for async search'),
  ],
),

'context-menu': dict(
  variants=['Default', 'With icons', 'With submenus', 'Destructive actions', 'Checkable items'],
  sizes=[
    ('Default', '200px min-width, 40px item height', 'Standard context', 'Web / TV'),
    ('Compact', '160px min-width, 32px item height', 'Dense toolbars', 'Web'),
  ],
  states=[
    ('Closed', 'Not rendered; trigger awaits right-click / long-press'),
    ('Open', 'Positioned at cursor; items visible; scrim optional'),
    ('Item hover/focus', 'Glass-1 background; cursor pointer'),
    ('Item disabled', '38% opacity; not clickable'),
    ('Destructive item', 'Red label; requires confirmation or extra tap'),
    ('Submenu trigger', 'Chevron-right; submenu opens on hover/arrow-right'),
  ],
),

'data-table': dict(
  variants=['Default', 'Sortable columns', 'Selectable rows', 'Expandable rows', 'Paginated', 'Scrollable (fixed header)'],
  sizes=[
    ('Compact', '36px row height', 'Dense analytics tables', 'Web'),
    ('Default', '48px row height', 'Standard data grids', 'Web / TV'),
    ('Comfortable', '56px row height', 'Readable content rows', 'Web'),
  ],
  states=[
    ('Default', 'All rows visible; no selection; no hover highlight'),
    ('Row hover', 'Glass-1 background on hovered row'),
    ('Row selected', 'Jio-green tint background; checkbox checked'),
    ('All selected', 'Header checkbox in indeterminate → checked state'),
    ('Sorted ascending', 'Column header shows up-arrow indicator'),
    ('Sorted descending', 'Column header shows down-arrow indicator'),
    ('Loading', 'Skeleton rows at table dimensions'),
    ('Empty', 'Centered empty state spanning full table width'),
    ('Error', 'Error message row with retry action'),
  ],
),

'date-picker': dict(
  variants=['Single date', 'Date range', 'With time (datetime)', 'Month picker', 'Year picker'],
  sizes=[
    ('Default', '48px input height, 280px calendar', 'Standard forms', 'All'),
    ('Compact', '36px input height, 240px calendar', 'Dense panels', 'Web'),
  ],
  states=[
    ('Closed', 'Displays formatted date or placeholder; calendar hidden'),
    ('Open', 'Calendar popover visible; trigger has jio border'),
    ('Date selected', 'Formatted date in input; calendar shows filled day'),
    ('Range in progress', 'Start date set; end date hover shows range preview'),
    ('Range complete', 'Both dates selected; formatted range string in input'),
    ('Disabled date', 'Day cell not clickable; 38% opacity'),
    ('Disabled input', '38% opacity input; calendar does not open'),
    ('Error', 'Red input border; error message below'),
  ],
),

'drawer': dict(
  variants=['Left nav drawer', 'Right filter drawer', 'Full-height', 'Partial-height (modal)'],
  sizes=[
    ('Narrow', '240px width', 'Nav / quick filter', 'Web'),
    ('Default', '320px width', 'Standard side panel', 'Web'),
    ('Wide', '480px width', 'Rich settings panel', 'Web'),
  ],
  states=[
    ('Closed', 'Off-screen at -100% translateX; scrim hidden'),
    ('Opening', 'Slides in with ease-out; scrim fades in'),
    ('Open', 'Fully visible; focus trapped inside drawer'),
    ('Closing', 'Slides out with ease-in; scrim fades out'),
    ('Scrolled', 'Header stays fixed; body scrolls independently'),
  ],
),

'dropdown-menu': dict(
  variants=['Default', 'With icons', 'With keyboard shortcuts', 'Checkable items', 'Radio group', 'With submenus'],
  sizes=[
    ('Default', '200px min-width, 40px item height', 'Standard menus', 'All'),
    ('Compact', '160px min-width, 32px item height', 'Toolbar menus', 'Web'),
  ],
  states=[
    ('Closed', 'Trigger in default state; menu not rendered'),
    ('Open', 'Panel visible; first item focused; ARIA expanded'),
    ('Item hover/focus', 'Glass-1 background; cursor pointer'),
    ('Item checked', 'Checkmark icon leading; green text'),
    ('Item disabled', '38% opacity; aria-disabled; not interactive'),
    ('Submenu open', 'Submenu panel appears to side; parent item highlighted'),
  ],
),

'forms': dict(
  variants=['Vertical (default)', 'Horizontal (label left)', 'Inline (compact row)', 'Multi-section', 'Wizard (multi-step)'],
  sizes=[
    ('Default', '480px max-width', 'Standard forms', 'Mobile / Web'),
    ('Narrow', '320px max-width', 'Short forms (login, OTP)', 'Mobile'),
    ('Wide', '680px max-width', 'Complex settings', 'Web'),
  ],
  states=[
    ('Idle', 'All fields in default state; no validation shown'),
    ('Active', 'A field is focused; its label and border are highlighted'),
    ('Validation error', 'Invalid field shows red border + error message below'),
    ('Validation success', 'Valid field shows green border + checkmark (optional)'),
    ('Submitting', 'Submit button shows spinner; all fields disabled'),
    ('Submitted', 'Success state — fields cleared or replaced with confirmation'),
    ('Disabled', 'All fields at 38% opacity; no interaction possible'),
  ],
),

'hover-card': dict(
  variants=['Game preview (thumbnail + meta)', 'User profile (avatar + stats)', 'Link preview (title + URL)', 'Minimal (text only)'],
  sizes=[
    ('Small', '240px width', 'Compact previews', 'Web'),
    ('Default', '320px width', 'Game / user cards', 'Web'),
    ('Wide', '400px width', 'Rich previews with image', 'Web'),
  ],
  states=[
    ('Closed', 'Not rendered; trigger in default state'),
    ('Opening (delay)', 'After 300ms hover delay; fades in with translateY'),
    ('Open', 'Fully visible; content loaded; mouse can enter card'),
    ('Loading', 'Skeleton inside card while async content fetches'),
    ('Closing', 'Fades out after mouse leaves trigger + card area'),
  ],
),

'icons': dict(
  variants=['Fill (solid)', 'Outline', 'Duotone', 'Animated (spinner, loading)'],
  sizes=[
    ('16px', '--icon-sm', 'Inline labels, badges', 'All'),
    ('20px', '--icon-md (default)', 'Standard UI icons', 'All'),
    ('24px', '--icon-lg', 'AppBar actions, nav', 'All'),
    ('32px', '--icon-xl', 'Feature icons, empty states', 'All'),
    ('48px', '--icon-2xl', 'Hero / onboarding illustrations', 'All'),
  ],
  states=[
    ('Default', 'currentColor fill; inherits parent text color'),
    ('Hover (interactive)', 'Parent button/link changes color; icon inherits'),
    ('Active', 'Parent pressed state; icon scales with parent'),
    ('Disabled', 'text3 color at 38% opacity'),
    ('Loading (spinner)', 'Continuous 360deg rotation at 600ms linear'),
  ],
),

'lists': dict(
  variants=['Basic (text only)', 'With leading icon/avatar', 'With thumbnail', 'With trailing action', 'Grouped with headers', 'Swipeable (mobile)'],
  sizes=[
    ('Compact', '44px min-height', 'Dense settings lists', 'Web'),
    ('Default', '56px min-height', 'Standard list items', 'All'),
    ('Comfortable', '72px min-height', 'Items with subtitle', 'All'),
    ('Media', '80px min-height', 'Thumbnail rows', 'All'),
  ],
  states=[
    ('Default', 'Surface bg; no affordance unless interactive'),
    ('Hover', 'Glass-1 background on interactive rows'),
    ('Pressed', 'Scale 0.99; darker bg for tap feedback'),
    ('Selected', 'Jio-green leading indicator or checkmark'),
    ('Disabled', '38% opacity; not interactive'),
    ('Swipe revealed', 'Action buttons visible behind row (delete, archive)'),
    ('Loading', 'Skeleton rows at list item height'),
  ],
),

'menubar': dict(
  variants=['Default (horizontal)', 'With icons', 'With keyboard shortcuts', 'Compact'],
  sizes=[
    ('Default', '44px bar height, 36px trigger height', 'Desktop app bar', 'Web'),
    ('Compact', '36px bar height, 28px trigger height', 'Dense utility bars', 'Web'),
  ],
  states=[
    ('Default', 'Bar visible; all triggers in rest state'),
    ('Trigger hover', 'Glass-1 background on hovered menu trigger'),
    ('Menu open', 'Trigger shows active/pressed bg; dropdown panel visible'),
    ('Item hover/focus', 'Glass-1 background; cursor pointer'),
    ('Item disabled', '38% opacity; not interactive'),
    ('Item checked', 'Checkmark icon; indicates active toggle state'),
  ],
),

'navigation-menu': dict(
  variants=['Horizontal (desktop top nav)', 'Vertical (sidebar)', 'With mega-menu', 'Simple (no sub-items)'],
  sizes=[
    ('Default', '44px item height', 'Standard top nav', 'Web'),
    ('Compact', '36px item height', 'Dense sidebar', 'Web'),
  ],
  states=[
    ('Default', 'All top-level items at rest; no sub-menus open'),
    ('Item hover', 'Background highlight; sub-menu trigger shows chevron'),
    ('Sub-menu open', 'Panel appears below/beside trigger; content visible'),
    ('Item active', 'Current route highlighted with jio-green indicator'),
    ('Item focus', 'Keyboard focus ring on current item'),
    ('Sub-menu item hover', 'Glass-1 bg on hovered child item'),
  ],
),

'page-dots': dict(
  variants=['Pill expand (default)', 'Circle only', 'Numbered', 'Line segments'],
  sizes=[
    ('Small', '4px dots, 12px active pill', 'Subtle indicators', 'Mobile'),
    ('Default', '6px dots, 18px active pill', 'Standard carousel', 'All'),
    ('Large', '8px dots, 24px active pill', 'Prominent indicators', 'Web / TV'),
  ],
  states=[
    ('Inactive dot', 'Small circle; text3 color'),
    ('Active dot', 'Expands to pill shape; jio-green fill'),
    ('Transitioning', 'Active pill slides to new position with ease-out'),
    ('Clickable', 'cursor:pointer; hover shows slight scale'),
    ('Disabled', 'Static; no click events; decorative only'),
  ],
),

'popover': dict(
  variants=['Default (content only)', 'With title + close', 'Form popover', 'Callout / onboarding', 'Tooltip-style (minimal)'],
  sizes=[
    ('Small', '200px width', 'Simple text popovers', 'Web'),
    ('Default', '320px width', 'Form controls, editing', 'Web'),
    ('Large', '480px width', 'Rich content panels', 'Web'),
  ],
  states=[
    ('Closed', 'Not rendered; trigger at rest'),
    ('Opening', 'Fades in + translateY with ease-out after trigger click'),
    ('Open', 'Fully visible; content interactive; focus trapped if form'),
    ('Repositioned', 'Flips side if viewport collision detected'),
    ('Closing', 'Fades out on trigger click or Escape key'),
  ],
),

'resizable': dict(
  variants=['Horizontal split (default)', 'Vertical split', 'Multi-pane (3+)', 'Collapsible pane'],
  sizes=[
    ('Narrow panel', '15–30% width', 'Sidebar + main', 'Web'),
    ('Equal split', '50% / 50%', 'Side-by-side editors', 'Web'),
    ('Wide panel', '60–80% width', 'Primary + reference', 'Web'),
  ],
  states=[
    ('Default', 'Panels at defaultLayout sizes; handle at rest'),
    ('Handle hover', 'Handle widens to 4px; jio-green tint'),
    ('Dragging', 'Handle highlighted; cursor col-resize; panels resize live'),
    ('Collapsed', 'Panel at minSize (0 or set value); content scrolls if needed'),
    ('At min size', 'Drag handle no longer moves in that direction'),
  ],
),

'scroll-area': dict(
  variants=['Vertical scroll (default)', 'Horizontal scroll', 'Both axes', 'Custom scrollbar color'],
  sizes=[
    ('Scrollbar thin', '4px thumb width', 'Code, logs', 'Web'),
    ('Scrollbar default', '8px thumb width', 'Standard panels', 'Web'),
  ],
  states=[
    ('Idle', 'Scrollbar invisible or very subtle (type:hover)'),
    ('Scrolling', 'Scrollbar thumb visible; smooth momentum'),
    ('Scrollbar hover', 'Thumb brightens; cursor default'),
    ('Scrollbar dragging', 'Thumb follows pointer; cursor grabbing'),
    ('Scroll end', 'At max scroll position; no further movement possible'),
    ('Overflow hidden', 'Content does not overflow container; no scrollbar needed'),
  ],
),

'select': dict(
  variants=['Default', 'With leading icon', 'With placeholder', 'Grouped options', 'Native (mobile fallback)'],
  sizes=[
    ('Compact', '36px height', 'Inline selectors, toolbars', 'Web'),
    ('Default', '48px height', 'Standard form fields', 'All'),
  ],
  states=[
    ('Closed', 'Shows selected value or placeholder; chevron down'),
    ('Open', 'Dropdown visible; chevron rotates 180deg; jio border on trigger'),
    ('Option highlighted', 'Glass-1 background on keyboard/hover option'),
    ('Option selected', 'Checkmark + jio text on chosen item'),
    ('Disabled', '38% opacity; dropdown does not open'),
    ('Error', 'Red border on trigger; error message below'),
    ('Loading', 'Spinner inside trigger while options fetch asynchronously'),
  ],
),

'separator': dict(
  variants=['Horizontal (default)', 'Vertical', 'Dashed', 'With label (section divider)', 'Decorative (aria-hidden)'],
  sizes=[
    ('Thin', '1px', 'Standard content divider', 'All'),
    ('Thick', '4px', 'Major section break', 'Web'),
  ],
  states=[
    ('Default', '1px border-subtle; full width (horizontal) or height (vertical)'),
    ('Decorative', 'aria-hidden=true; role=none; invisible to screen readers'),
    ('With label', 'Text centred on separator; padding interrupts line'),
  ],
),

'slider': dict(
  variants=['Single thumb', 'Range (two thumbs)', 'With value tooltip', 'Step marks', 'Vertical'],
  sizes=[
    ('Thin track', '2px track height', 'Playback scrubber', 'All'),
    ('Default track', '4px track height', 'Standard controls', 'All'),
    ('Thick track', '8px track height', 'Volume / accessibility', 'All'),
  ],
  states=[
    ('Default', 'Track fill at current value; thumb at rest'),
    ('Hover', 'Thumb scales to 1.1; jio glow shadow appears'),
    ('Dragging', 'Thumb follows pointer; value tooltip visible; cursor grabbing'),
    ('Focus', '2px jio-green outline on thumb via :focus-visible'),
    ('Disabled', '38% opacity; thumb not draggable'),
    ('At min', 'Fill is 0%; thumb at leftmost position'),
    ('At max', 'Fill is 100%; thumb at rightmost position'),
  ],
),

'tab-bar': dict(
  variants=['Bottom nav (mobile)', 'Top nav (web)', 'Icon only', 'Icon + label (default)', 'With badge'],
  sizes=[
    ('Mobile', '56px height, 24px icons', 'Primary mobile nav', 'Mobile'),
    ('Web top bar', '48px height, 20px icons', 'Web app top nav', 'Web'),
    ('TV', '72px height, 32px icons', 'TV primary nav', 'TV'),
  ],
  states=[
    ('Default (inactive)', 'Icon and label at text3 color; no indicator'),
    ('Active', 'Icon and label turn jio-green; indicator dot or underline'),
    ('Hover', 'Slight background tint; cursor pointer'),
    ('Pressed', 'Icon scales down to 0.88 momentarily on tap'),
    ('With badge', 'Count badge overlays icon top-right'),
    ('Badge cleared', 'Badge animates out on read/clear action'),
    ('Hidden (scroll)', 'Translated 100% down; revealed on scroll-up'),
  ],
),

'tabs': dict(
  variants=['Underline (default)', 'Pill / segment', 'Card tabs', 'Vertical tabs', 'Scrollable tabs'],
  sizes=[
    ('Compact', '36px trigger height, 12px font', 'Dense in-page tabs', 'Web'),
    ('Default', '44px trigger height, 13px font', 'Standard content tabs', 'All'),
    ('Large', '52px trigger height, 15px font', 'Prominent section tabs', 'Web / TV'),
  ],
  states=[
    ('Default (inactive)', '13px 600; text3 color; no underline'),
    ('Active', 'Jio-green text; 2px jio-green underline indicator'),
    ('Hover', 'Text shifts to text2; subtle background tint'),
    ('Pressed', 'Scale 0.95 on click'),
    ('Focus', '2px jio-green outline via :focus-visible'),
    ('Disabled', '38% opacity; not clickable'),
  ],
),

'textarea': dict(
  variants=['Default', 'Auto-resize', 'Fixed height', 'With character count', 'Rich text (editor)'],
  sizes=[
    ('Small', '3 rows (80px)', 'Short feedback, notes', 'All'),
    ('Default', '5 rows (128px)', 'Standard text input', 'All'),
    ('Large', '8 rows (200px)', 'Long descriptions, reviews', 'Web'),
  ],
  states=[
    ('Default', 'Surface-1 bg; border-subtle; placeholder text3'),
    ('Focus', 'Jio-green outline + border; placeholder fades'),
    ('Filled', 'Text content visible; character counter updates'),
    ('Error', 'Red border; error message below; character counter turns red'),
    ('Disabled', '38% opacity; resize none; not editable'),
    ('At max length', 'Character counter red; no more typing accepted'),
  ],
),

'toggle-group': dict(
  variants=['Single select (default)', 'Multi select', 'Icon only', 'Icon + label', 'Vertical'],
  sizes=[
    ('Small', '28px height, 12px font', 'Toolbar toggles', 'Web'),
    ('Default', '36px height, 13px font', 'Standard controls', 'All'),
    ('Large', '44px height, 15px font', 'Prominent selectors', 'Web / TV'),
  ],
  states=[
    ('Default (inactive)', 'Surface-1 bg; border-subtle; text2 label'),
    ('Active', 'Jio-soft bg; jio-green text; jio border'),
    ('Hover', 'Glass-1 background tint'),
    ('Pressed', 'Scale 0.95; immediate feedback'),
    ('Disabled (all)', '38% opacity group; no items selectable'),
    ('Disabled (item)', 'Individual item 38% opacity; others still work'),
    ('Focus', '2px jio-green outline on focused item'),
  ],
),

'tooltip': dict(
  variants=['Default (text)', 'With keyboard shortcut', 'Rich (icon + text)', 'Arrow pointing up/down/left/right'],
  sizes=[
    ('Default', '12px font, max-width 200px', 'Standard tooltips', 'Web'),
    ('Wide', '12px font, max-width 320px', 'Longer explanations', 'Web'),
  ],
  states=[
    ('Closed', 'Not rendered; trigger at rest'),
    ('Opening (300ms delay)', 'After hover delay; fades in + small scale'),
    ('Open', 'Fully visible; persists while cursor is on trigger'),
    ('Closing', 'Fades out when cursor leaves trigger'),
    ('Disabled trigger', 'Tooltip does not open on disabled elements; explain inline'),
  ],
),

'tv-focus': dict(
  variants=['Card focus (scale + ring)', 'Button focus (ring only)', 'Nav item focus', 'Full-screen item (no scale)'],
  sizes=[
    ('Ring thin', '2px + 8px spread', 'Compact UI elements', 'TV'),
    ('Ring default', '3px + 16px glow spread', 'Cards, buttons', 'TV'),
    ('Ring prominent', '4px + 24px glow spread', 'Hero items, featured', 'TV'),
  ],
  states=[
    ('Unfocused', 'No ring; element at rest scale (1.0)'),
    ('Focused', '3px jio-green ring + 0 0 24px rgba(0,168,89,.4) glow; scale 1.08 for cards'),
    ('Selected (pressed OK)', 'Brief scale pulse 0.95 → 1.0 + ring flash white → jio'),
    ('Focused + loading', 'Ring maintained; content shows spinner overlay'),
    ('Focus lost', 'Ring fades out with ease-in; scale returns to 1.0'),
  ],
),

}

# ── Injection logic ─────────────────────────────────────────────────────────────

def inject_vss(comp_name, data, dry_run=False):
    path = os.path.join(BASE, comp_name, 'index.html')
    if not os.path.exists(path):
        return 'SKIP — file not found'

    html = open(path, encoding='utf-8').read()
    changes = []

    def insert_before(new_section, *anchors):
        nonlocal html
        for anchor in anchors:
            idx = html.find(anchor)
            if idx != -1:
                start = html.rfind('\n  <', 0, idx)
                if start != -1:
                    html = html[:start] + new_section + html[start:]
                    return True
        html = html.replace('</main>', new_section + '</main>', 1)
        return True

    # Variants — insert before sizes, states, motion, best-practices, or when-to-use
    if 'id="variants"' not in html:
        s = make_variants(data['variants'])
        insert_before(s, 'id="sizes"', 'id="states"', 'id="motion"', 'id="best-practices"', 'id="when-to-use"')
        changes.append('variants')

    # Sizes — insert before states, motion, best-practices
    if 'id="sizes"' not in html:
        s = make_sizes(data['sizes'])
        insert_before(s, 'id="states"', 'id="motion"', 'id="best-practices"', 'id="when-to-use"')
        changes.append('sizes')

    # States — insert before motion, best-practices
    if 'id="states"' not in html:
        s = make_states(data['states'])
        insert_before(s, 'id="motion"', 'id="best-practices"', 'id="when-to-use"')
        changes.append('states')

    if not dry_run and changes:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        tmp_path = os.path.join(TMP, comp_name, 'index.html')
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        shutil.copy2(path, tmp_path)

    return ', '.join(changes) if changes else 'already complete'


# ── Main ────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    args = sys.argv[1:]
    targets = list(VSS.keys()) if ('--all' in args or not args) else args

    print(f"\n{'Component':<24} {'Injected'}")
    print('-' * 60)
    for name in targets:
        if name not in VSS:
            print(f"  {name:<22} NOT IN DATA — skipped")
            continue
        result = inject_vss(name, VSS[name])
        print(f"  {name:<22} {result}")
    print()

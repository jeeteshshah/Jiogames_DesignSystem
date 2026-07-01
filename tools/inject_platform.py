#!/usr/bin/env python3
"""
inject_platform.py — injects Platform section into DLS component pages.
Usage: python3 tools/inject_platform.py --all
       python3 tools/inject_platform.py accordion badges ...
"""
import os, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP  = '/tmp/jiogames-dls-preview'

def make_platform(cards):
    """cards = list of (platform, color, rules_list)"""
    COLORS = {'Mobile': '#3B82F6', 'Web': '#8B5CF6', 'TV': '#F59E0B'}
    cards_html = ''
    for platform, rules in cards:
        color = COLORS.get(platform, '#888')
        items = ''.join(f'<li style="font-size:13px;color:var(--text2);line-height:1.6;padding:4px 0;border-bottom:.5px solid var(--border-subtle);margin:0">{r}</li>' for r in rules)
        cards_html += f'''
      <div style="border:1px solid var(--border-subtle);border-top:2px solid {color};border-radius:var(--r4);padding:20px;background:var(--surface-1);">
        <p style="font-size:12px;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:.6px;margin:0 0 12px;">{platform}</p>
        <ul style="list-style:none;padding:0;margin:0;">{items}</ul>
      </div>'''
    return f'''
  <!-- PLATFORM -->
  <section class="ds-section" id="platform">
    <h2 class="ds-section-title">Platform rules</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;margin-top:16px;">{cards_html}
    </div>
  </section>
'''

# ── Platform data ──────────────────────────────────────────────────────────────

PLATFORM = {

'accordion': [
  ('Mobile', [
    '56px min row height — comfortable touch target',
    'Full-width; body scrolls if content is tall',
    'Single-open (exclusive) preferred to avoid tall stacked content',
    'Swipe-to-dismiss not applicable — use tap on trigger only',
  ]),
  ('Web', [
    'Keyboard: Enter/Space toggles; arrow keys navigate items',
    'Both single and multiple-open modes supported',
    'Compact (44px) variant available for dense settings panels',
    'Hover state on trigger is meaningful — show glass-1 bg',
  ]),
  ('TV', [
    'D-pad Up/Down navigates between items; OK expands',
    'Focus ring required on every trigger — use ds-tv-focus',
    'Avoid deeply nested accordions — spatial nav becomes confusing',
    'Ensure expanded body text is large enough at 10-foot distance (min 20px)',
  ]),
],

'badges': [
  ('Mobile', [
    'Touch target of parent must be ≥44×44px — badge is decorative overlay',
    'Dot badge preferred on small icons; count badge on tab bar items',
    'Max count shows "99+" to avoid badge overflow on small targets',
  ]),
  ('Web', [
    'Hover on parent shows badge tooltip with full count if truncated',
    'Keyboard focus on badged element reads count via aria-label',
    'Larger badge sizes (20px+) acceptable in spacious web layouts',
  ]),
  ('TV', [
    'Badges must be large enough to read at 10 feet — min 20px height',
    'Do not rely on badge color alone — pair with icon or text',
    'Live badge pulse animation must respect prefers-reduced-motion',
  ]),
],

'banners': [
  ('Mobile', [
    'Slides in from top — sits below the status bar, above the AppBar',
    'Full viewport width; dismiss X in top-right corner (44×44px touch target)',
    'Max 2 lines of body text — truncate longer messages',
    'Auto-dismiss after 8s for non-critical banners',
  ]),
  ('Web', [
    'Can be fixed or inline depending on scope (page vs. section)',
    'Action link on the right side of the banner row',
    'Wider layouts can show icon + title + body in a single row',
  ]),
  ('TV', [
    'Banners not recommended on TV — use Toast or overlay Dialog instead',
    'If used, position at bottom of screen; top area reserved for content',
    'Must not auto-dismiss faster than 10s — remote users read slower',
  ]),
],

'buttons': [
  ('Mobile', [
    'Minimum touch target 44×44px — use var(--ctrl-h) 48px default height',
    'Full-width CTAs in sheets and bottom panels (width:100%)',
    'Avoid more than 2 buttons stacked vertically — use bottom-sheet actions',
    'Loading state shows spinner inside button — do not disable without feedback',
  ]),
  ('Web', [
    'Hover state required — scale(1.02) or bg shift on primary/secondary',
    'Focus ring via :focus-visible — 2px jio-green outline, 2px offset',
    'Icon-only buttons must have tooltip or aria-label',
    'Min width 120px to avoid very narrow pill buttons',
  ]),
  ('TV', [
    'Height uses var(--ctrl-h-tv) — taller for D-pad navigation comfort',
    'Focus ring uses jio-glow box-shadow — visible at 10-foot distance',
    'Only Primary and Ghost variants used on TV — avoid subtle differences',
    'Pressed state on OK button: scale(0.95) flash then return',
  ]),
],

'calendar': [
  ('Mobile', [
    'Full-width embedded calendar preferred — no popover on small screens',
    'Day cells minimum 44×44px touch target',
    'Month navigation: swipe left/right or tap chevrons',
    'Range selection: tap start, then tap end — no drag-to-select',
  ]),
  ('Web', [
    'Popover calendar anchored to date input field',
    'Keyboard: arrow keys navigate days; Enter selects; Escape closes',
    'Range drag-to-select supported with mouse',
    'Compact variant (240px) available for filter panels',
  ]),
  ('TV', [
    'Not recommended on TV — date inputs are complex with D-pad',
    'If required, use a large cell size (56px+) and simplified month view',
    'OK selects day; back button cancels; no range mode on TV',
  ]),
],

'cards': [
  ('Mobile', [
    'Wide landscape cards: 210×128px in horizontal rails',
    'Portrait cover cards: 120×180px in browse grids',
    'Tap target is the full card — no sub-tap-targets inside the card',
    'Image placeholder skeleton shown until asset loads',
  ]),
  ('Web', [
    'Hover: scale(1.02) + shadow lift for interactive cards',
    'Standard grid card: 160×200px with 16px gutters',
    'Right-click opens Context Menu with card actions',
    'Keyboard focus: Enter activates, Tab navigates between cards',
  ]),
  ('TV', [
    'Card size: 240×150px minimum — readable artwork at 10 feet',
    'Focus: scale(1.06) + jio-glow ring via ds-tv-focus',
    'Only one card focusable at a time — D-pad moves focus laterally',
    'Title text minimum 20px — must be legible without squinting',
  ]),
],

'carousel-component': [
  ('Mobile', [
    'Swipe left/right to advance — native touch scroll with scroll-snap',
    'Partial card peek (24px) indicates more content horizontally',
    'Dot indicators below — tap dots for direct navigation',
    'Auto-play pauses on any touch interaction; resumes after 8s',
  ]),
  ('Web', [
    'Arrow buttons visible on hover (left/right edges)',
    'Keyboard: arrow keys advance slides when carousel is focused',
    'Mouse drag or click-drag supported',
    'Reduced-motion: disable auto-play, replace slide with instant switch',
  ]),
  ('TV', [
    'D-pad Left/Right moves between slides; OK enters the active card',
    'Arrow button focus indicators required on prev/next controls',
    'Auto-play disabled on TV — users control pace with remote',
    'Hero carousel minimum 40vh height for cinematic impact',
  ]),
],

'chart': [
  ('Mobile', [
    'Compact height (120–180px) — detailed charts belong on dedicated screens',
    'Tap on bar/point shows tooltip overlay; pinch-zoom not supported',
    'Horizontal bar charts preferred over vertical when labels are long',
    'Legend below chart — avoid side legends that waste horizontal space',
  ]),
  ('Web', [
    'Hover shows tooltip with precise values',
    'Legend items clickable to toggle series visibility',
    'Keyboard: Tab focuses chart; arrow keys navigate data points',
    'Full 360px height available for analytics dashboards',
  ]),
  ('TV', [
    'Charts on TV: read-only only — no interactive hover/tooltip',
    'Large fonts (min 20px) for axis labels and legend',
    'High-contrast color palette — distinguish series at 10 feet',
    'Animated entrance only on first load — not on every D-pad move',
  ]),
],

'chips': [
  ('Mobile', [
    '36px default height — minimum 44px touch target via padding extension',
    'Horizontal scrolling chip row — no wrapping (avoids layout shift)',
    'Selected chips move to front of list for visibility',
    'Dismiss X is 24×24px — adequate tap target within chip bounds',
  ]),
  ('Web', [
    'Hover state: glass-1 background tint',
    'Keyboard: Space/Enter toggles; Delete/Backspace removes (input chips)',
    'Wrapping allowed on web when space permits',
    'Focus ring via :focus-visible on chip container',
  ]),
  ('TV', [
    'D-pad navigates between chips; OK toggles selected state',
    'Focus ring via ds-tv-focus — scale(1.06) + jio-glow',
    'Selected state must be clearly distinct at 10 feet — not just border change',
    'Avoid long chip rows — grid layout preferred for TV',
  ]),
],

'collapsible': [
  ('Mobile', [
    'Trigger height minimum 44px — comfortable tap target',
    'Body content scrolls within the page — no fixed max-height',
    'Avoid multiple open collapsibles stacking long content on mobile',
  ]),
  ('Web', [
    'Keyboard: Enter/Space toggles; chevron rotates on expand',
    'Hover state on trigger — glass-1 background',
    'Compact 40px trigger variant for dense settings panels',
  ]),
  ('TV', [
    'D-pad OK expands/collapses; Up/Down navigates to next item',
    'Focus ring on trigger required',
    'Expanded content must be fully visible — scroll within panel if needed',
  ]),
],

'combobox': [
  ('Mobile', [
    'Opens a full-screen picker sheet instead of inline dropdown',
    'Search field at top of sheet — keyboard auto-shown on open',
    'Options list with 56px min row height for touch',
    'Multi-select shows selected count in trigger chip',
  ]),
  ('Web', [
    'Dropdown anchored to trigger — max 320px height with internal scroll',
    'Keyboard: type to filter; arrow keys navigate; Enter selects; Escape closes',
    'Creatable mode shows "Add X" as first result when no match',
  ]),
  ('TV', [
    'Not recommended on TV — use a simplified Radio group or picker sheet',
    'If used, opens full-screen overlay with large option rows (56px+)',
    'D-pad Up/Down navigates; OK selects; Back closes',
  ]),
],

'command': [
  ('Mobile', [
    'Not used on mobile — use AppBar search or Bottom Sheet actions instead',
    'If triggered programmatically, renders as full-screen search overlay',
  ]),
  ('Web', [
    '⌘K (Mac) / Ctrl+K (Windows) opens palette — standard power-user shortcut',
    'Escape always closes; arrow keys navigate results',
    'Groups labelled with 10px uppercase section headers',
    'Max 8 visible results before internal scroll',
  ]),
  ('TV', [
    'Not applicable on TV — voice search or D-pad search used instead',
  ]),
],

'context-menu': [
  ('Mobile', [
    'Triggered by long-press (500ms) on the target element',
    'Renders as Bottom Sheet — not a floating panel',
    'Items: 56px height; icon + label layout',
    'Always include a visible Cancel item at the bottom',
  ]),
  ('Web', [
    'Triggered by right-click on the target element',
    'Floating panel — positioned at cursor, flips if near edge',
    'Keyboard: arrow keys navigate; Enter activates; Escape closes',
    'Max 8 items before needing a separator + submenu pattern',
  ]),
  ('TV', [
    'Triggered by pressing the Options/Menu button on remote',
    'Renders as a focused side panel or Bottom Sheet equivalent',
    'D-pad Up/Down navigates; OK activates; Back closes',
  ]),
],

'data-table': [
  ('Mobile', [
    'Collapse to single-column card layout below 480px',
    'Show only 3–4 most important columns; hide rest behind row expand',
    'Horizontal scroll table only for simple data (max 4 columns)',
    'Sticky first column if horizontal scroll is used',
  ]),
  ('Web', [
    'Full multi-column layout with sortable headers',
    'Fixed header on scroll for tables taller than viewport',
    'Row hover, selection, and expand all supported',
    'Keyboard: Tab navigates columns; Enter/Space sorts or selects',
  ]),
  ('TV', [
    'Read-only mode — no sorting, selection, or column resize',
    'Large font (min 18px) for cell content',
    'D-pad Up/Down navigates rows; OK expands row detail',
    'Max 4 columns — wider tables not readable at 10 feet',
  ]),
],

'date-picker': [
  ('Mobile', [
    'Input triggers full-screen calendar sheet — no floating popover',
    'Formatted date string shown in input after selection',
    'Range: two sequential taps (start → end)',
    'Month navigation via swipe or tap chevrons',
  ]),
  ('Web', [
    'Floating popover calendar anchored to input field',
    'Keyboard fully supported: arrow keys, Enter, Escape',
    'Range drag supported with mouse',
    'fromDate/toDate constraints disable out-of-range days',
  ]),
  ('TV', [
    'Replaced by a simplified spinner-style day/month/year selector',
    'D-pad Up/Down increments value; Left/Right moves between fields',
    'Large numeric display — minimum 28px for year/month values',
  ]),
],

'drawer': [
  ('Mobile', [
    'Not used on mobile — use Bottom Sheet instead',
    'Exception: full-screen nav drawer (hamburger menu) on mobile web',
  ]),
  ('Web', [
    'Left drawer: primary nav — persists or overlays on smaller screens',
    'Right drawer: filters, settings, detail panels',
    'Keyboard: Escape closes; focus trapped inside while open',
    'Overlay scrim on widths below 1024px; push layout on wider screens',
  ]),
  ('TV', [
    'Not used on TV — use a fullscreen overlay or focused side panel',
  ]),
],

'dropdown-menu': [
  ('Mobile', [
    'Renders as Bottom Sheet on mobile — not a floating dropdown',
    'Items: 56px height; full width; icon + label',
    'Cancel item always last in the sheet',
  ]),
  ('Web', [
    'Floating panel anchored to trigger button',
    'Keyboard: arrow keys navigate; Enter activates; Escape closes',
    'Submenus open on hover or arrow-right key',
    'Min width matches trigger button width',
  ]),
  ('TV', [
    'Renders as focused side panel or overlay list',
    'D-pad Up/Down navigates; OK selects; Back closes',
    'Submenus not recommended on TV — flatten the hierarchy',
  ]),
],

'forms': [
  ('Mobile', [
    'Single-column layout only — no side-by-side fields',
    'Keyboard-aware: active field scrolls into view above soft keyboard',
    'Submit button fixed at bottom or inside the scroll area',
    'Input fields: 48px height (var(--ctrl-h)) for comfortable touch',
  ]),
  ('Web', [
    'Two-column grid allowed for related field pairs (first/last name)',
    'Inline validation on blur (not on every keystroke)',
    'Tab order follows visual reading order — test without a mouse',
    'Error summary at top of form for screen-reader users',
  ]),
  ('TV', [
    'Single-field-per-screen wizard style preferred on TV',
    'On-screen keyboard renders when text field is focused',
    'Large fields (56px height), large labels (min 20px)',
    'Avoid complex multi-field forms — redirect to companion app where possible',
  ]),
],

'hover-card': [
  ('Mobile', [
    'Not used on mobile — hover does not exist',
    'Replace with tap-triggered Popover or navigate to detail screen',
  ]),
  ('Web', [
    'Opens after 300ms hover delay — avoids flicker on mouse pass-through',
    'Stays open while cursor is on trigger or card itself',
    'Max card width 320px — wider pushes off-screen on smaller viewports',
    'Keyboard: not shown on keyboard navigation — use Popover instead',
  ]),
  ('TV', [
    'Not used on TV — use an info panel that appears on D-pad focus',
  ]),
],

'icons': [
  ('Mobile', [
    'Minimum 24px render size — smaller icons are not legible on phone screens',
    'Touch targets for icon-only buttons: 44×44px wrapper around 20–24px icon',
    'Use fill variants for primary actions; outline for secondary',
    'ic_ snake_case naming — always use sprite reference, never inline SVG paths',
  ]),
  ('Web', [
    '16px icons acceptable inline with text labels (breadcrumbs, table cells)',
    'Hover-state color inherits from parent — no separate icon hover CSS needed',
    'SVG sprite loaded once via sprite-loader.js — no per-icon HTTP requests',
  ]),
  ('TV', [
    'Minimum 32px at 1x — scales to 40px+ for nav and hero icons',
    'Fill icons only on TV — outline detail disappears at 10-foot viewing distance',
    'High contrast: always use --text or --jio color — avoid text3 on TV',
  ]),
],

'inputs': [
  ('Mobile', [
    '48px height (var(--ctrl-h)) — mandatory for comfortable touch',
    'Keyboard type: use type=email, type=tel, type=number for correct soft keyboard',
    'Auto-scroll: focused input scrolls above soft keyboard automatically',
    'Clear button (×) appears in trailing slot when field has value',
  ]),
  ('Web', [
    'Focus ring: 2px jio-green outline via :focus-visible',
    'Inline validation: show error on blur, clear error on fix',
    'Password show/hide toggle in trailing slot',
    'Autofill styled consistently — override browser yellow with surface-1 bg',
  ]),
  ('TV', [
    'On-screen keyboard shown automatically on focus',
    '56px height variant for TV — larger touch/remote target',
    'Avoid mandatory text fields on TV — prefer radio or select patterns',
    'Cursor blink must be visible: use jio-green, 2px wide, standard blink rate',
  ]),
],

'lists': [
  ('Mobile', [
    'Minimum 56px row height — 44px touch target with vertical padding',
    'Leading thumbnail: 48×48px for media rows; 40×40px for avatar rows',
    'Swipe-to-reveal: 80px action zone on right edge for delete/archive',
    'Pull-to-refresh at top of list — native scroll behavior',
  ]),
  ('Web', [
    'Hover state: glass-1 background on interactive rows',
    'Keyboard: Up/Down arrows navigate rows; Enter activates',
    'Right-click opens Context Menu on list items',
    'Compact 44px rows available for dense settings lists',
  ]),
  ('TV', [
    'D-pad Up/Down navigates rows; OK activates',
    'Focus ring on active row — full-width highlight preferred over ring',
    'Row height 64px minimum on TV — content must be legible at 10 feet',
    'No swipe-to-reveal on TV — use Options button for item actions',
  ]),
],

'menubar': [
  ('Mobile', [
    'Not used on mobile — use Tab Bar and Bottom Sheet action sheets instead',
  ]),
  ('Web', [
    'Sits at the very top of the app frame — consistent position across screens',
    'Keyboard: Alt+letter mnemonics open menus; arrow keys navigate',
    'Submenus open on hover or arrow-right key',
    'Keyboard shortcut labels right-aligned in menu item rows',
  ]),
  ('TV', [
    'Not used on TV — side navigation panel or full-screen menu used instead',
  ]),
],

'navigation': [
  ('Mobile', [
    'Tab Bar at bottom: 56px height, 3–5 items, icon + label',
    'Active indicator: jio-green icon and label color',
    'Tab bar hides on downward scroll, reveals on upward scroll',
    'Badge count overlays icon — 44×44px tap target per item',
  ]),
  ('Web', [
    'Top horizontal nav bar or left sidebar depending on app complexity',
    'Keyboard: Tab navigates items; Enter/Space activates',
    'Active route: jio-green underline or filled background indicator',
    'Breadcrumbs used on secondary pages alongside primary nav',
  ]),
  ('TV', [
    'Left sidebar nav — always visible, D-pad Left enters nav from any screen',
    'Nav items: 64px height, 32px icons, 18px+ labels',
    'Focus moves left into nav, right exits nav to content',
    'Selected item: jio-green fill background on the nav item',
  ]),
],

'navigation-menu': [
  ('Mobile', [
    'Not used on mobile — Drawer + Tab Bar combination used instead',
  ]),
  ('Web', [
    'Horizontal top nav with hover-reveal sub-menus',
    'Sub-menu panel: max 3 columns of grouped links',
    'Keyboard: Tab to trigger; Enter/Space opens; arrow keys navigate sub-items',
    'Active route highlighted with jio-green indicator on top-level item',
  ]),
  ('TV', [
    'Not used on TV — side nav panel used instead',
  ]),
],

'page-dots': [
  ('Mobile', [
    'Below carousel or hero — tappable dots jump to specific slide',
    'Default 6px dots, 18px active pill — visible against dark hero backgrounds',
    'Use white fill on dark hero images; jio-green on surface backgrounds',
  ]),
  ('Web', [
    'Keyboard: left/right arrow keys when carousel is focused advances dots',
    'Dots clickable with cursor — pointer cursor on hover',
    'Larger 8px dots optional for prominent hero carousels',
  ]),
  ('TV', [
    'D-pad Left/Right advances carousel — dots are decorative/read-only on TV',
    'Larger 10px dots with 28px active pill — readable at 10-foot distance',
    'Ensure sufficient contrast against background image',
  ]),
],

'pass-cards': [
  ('Mobile', [
    'Full-width single card per screen or stacked vertically with 16px gap',
    'Recommended badge at top of card — not inside header',
    'CTA button: full width, primary variant, 48px height',
    'Price displayed large (28px 700) — key decision driver',
  ]),
  ('Web', [
    'Side-by-side two-column layout for Mobile vs. Ultimate comparison',
    'Hover: scale(1.02) + deeper border glow on selected card',
    'Feature list: max 6 items — truncate or link to full details',
  ]),
  ('TV', [
    'Full-screen upsell layout — one card per screen or vertical compare',
    'D-pad Up/Down navigates feature list; Left/Right switches plan',
    'CTA button: 64px height TV variant; prominent jio-green fill',
    'Price and plan name: min 28px and 24px — readable at 10 feet',
  ]),
],

'popover': [
  ('Mobile', [
    'Replace with Bottom Sheet on mobile — floating popovers are too small',
    'Exception: small tooltip-style popovers (max 180px wide) on icon buttons',
  ]),
  ('Web', [
    'Anchored to trigger with 8px offset — flips side on viewport collision',
    'Focus trapped inside if form content is present',
    'Keyboard: Escape closes; Tab cycles within popover',
    'Arrow pointer indicates relationship to trigger element',
  ]),
  ('TV', [
    'Not used on TV — use a focused side panel or dialog overlay',
  ]),
],

'rails': [
  ('Mobile', [
    'Horizontal scroll with scroll-snap-type: x mandatory',
    'Card sizes: wide 210×128px; portrait 120×180px',
    'Peek of next card (24px) visible at right edge',
    'Scrollbar hidden — momentum scrolling native',
    'Rail title 16px 700; See All link right-aligned',
  ]),
  ('Web', [
    'Arrow buttons appear on rail hover (left/right edges) for mouse nav',
    'Keyboard: Tab focuses rail; arrow keys scroll cards',
    'Cards may be larger (240×150px) with wider gutters on desktop',
    'Loading: show 5 skeleton cards at standard dimensions',
  ]),
  ('TV', [
    'Horizontal D-pad navigation — Left/Right moves card focus',
    'Focused card: scale(1.08) + jio-glow ring',
    'Rail title 20px minimum — readable during D-pad focus state',
    'At least 5 cards visible simultaneously on TV viewport',
    'Auto-scroll rail to keep focused card fully visible',
  ]),
],

'resizable': [
  ('Mobile', [
    'Not used on mobile — use fixed layout or Bottom Sheet panels instead',
  ]),
  ('Web', [
    'Drag handle 4px wide, extends to full panel height',
    'cursor: col-resize on handle hover; ew-resize while dragging',
    'Double-click handle collapses/restores panel to default size',
    'Min panel size enforced — drag stops at minSize boundary',
  ]),
  ('TV', [
    'Not used on TV — fixed layout panels only',
  ]),
],

'scroll-area': [
  ('Mobile', [
    'Native scroll preferred — use ScrollArea only for custom scrollbar styling',
    'Scrollbar not shown on mobile — native momentum scroll used',
    'Horizontal scroll areas: ensure swipe does not conflict with page navigation',
  ]),
  ('Web', [
    'Custom scrollbar: 8px wide thumb, glass-2 bg, visible on hover',
    'Auto-hide after 600ms idle — smooth opacity transition',
    'Both-axis scroll: corner piece prevents overlap of both scrollbars',
    'Keyboard: Page Up/Down, Home/End supported via viewport focus',
  ]),
  ('TV', [
    'Scrollbar hidden on TV — D-pad navigation drives scroll position',
    'Content scrolls when focused item reaches edge of container',
    'Ensure scroll position updates are smooth — no jarring jumps',
  ]),
],

'search': [
  ('Mobile', [
    'AppBar integration: tapping search icon expands input full-width',
    'Results dropdown becomes full-screen overlay on mobile',
    'Keyboard auto-opens on search field focus',
    'Clear button (×) in trailing slot — 44×44px touch target',
  ]),
  ('Web', [
    'Inline dropdown results anchored below input — max 480px height',
    'Keyboard: arrow keys navigate results; Enter opens; Escape closes dropdown',
    'Debounce 300ms before firing search query',
    'Result items: 48px height with thumbnail, title, and meta',
  ]),
  ('TV', [
    'Dedicated search screen — not inline in AppBar',
    'On-screen keyboard or voice search integration',
    'Results rendered as card grid navigable with D-pad',
    'Recent searches shown when query is empty',
  ]),
],

'select': [
  ('Mobile', [
    'Tapping trigger opens a native bottom-sheet picker or custom sheet',
    'Avoid system native <select> — styling is uncontrollable',
    'Item rows: 56px height inside the bottom sheet',
    'Selected item shows checkmark on the right',
  ]),
  ('Web', [
    'Floating dropdown anchored to trigger — max 320px height, internal scroll',
    'Keyboard: Up/Down navigate; Enter selects; Escape closes',
    'Chevron rotates 180deg on open — visual affordance',
    'Min width matches trigger; options wrap text if longer',
  ]),
  ('TV', [
    'Renders as full-screen option list with D-pad navigation',
    'Item rows 56px height; selected item shows jio-green checkmark',
    'Back button cancels without changing selection',
  ]),
],

'slider': [
  ('Mobile', [
    'Thumb size: 24px circle — large enough for finger press',
    'Thumb drag follows touch position — no snap unless step is set',
    'Value tooltip appears above thumb during drag',
    'Horizontal only — vertical sliders not used on mobile',
  ]),
  ('Web', [
    'Keyboard: focused thumb responds to arrow keys (step size)',
    'Page Up/Down: 10× step; Home/End: min/max jump',
    'Hover: thumb scale(1.1) + glow shadow',
    'Vertical slider available for volume-style controls',
  ]),
  ('TV', [
    'D-pad Left/Right adjusts value by step size; hold for fast repeat',
    'Thumb size 32px minimum — focused state shows jio-glow ring',
    'Value label always visible on TV — not just during drag',
    'Avoid sliders for precise values on TV — use stepper input instead',
  ]),
],

'tab-bar': [
  ('Mobile', [
    'Fixed at bottom — 56px height, safe area inset respected',
    'Items: flex:1 equal width; icon centered above label',
    'Hides on scroll down within content; reveals on scroll up',
    'Max 5 items — more items require overflow/more menu pattern',
  ]),
  ('Web', [
    'Top horizontal position or left sidebar depending on viewport',
    'Keyboard: Tab navigates items; Enter/Space activates',
    'Active underline or filled background indicator',
    'Badge count shown as superscript on icon',
  ]),
  ('TV', [
    'Left sidebar nav replaces bottom tab bar on TV',
    'Items: 72px height; 32px icons; 18px labels',
    'D-pad Up/Down navigates; OK enters section; Left re-enters nav from content',
    'Active item: jio-green full background fill on the sidebar row',
  ]),
],

'tabs': [
  ('Mobile', [
    'Horizontal scrolling tabs if more than 4 items — no wrapping',
    '44px trigger height — comfortable tap target',
    'Active underline indicator: 2px jio-green, width matches label text',
    'Panel content uses full available width below tab list',
  ]),
  ('Web', [
    'Keyboard: Left/Right arrow keys move between tabs; Enter/Space activates',
    'Tab panel: focus moves into panel content after activation',
    'Vertical tabs available for sidebar settings navigation',
    'Scrollable tabs: show gradient fade at edges to indicate more',
  ]),
  ('TV', [
    'D-pad Left/Right navigates tabs; OK selects; Down enters panel content',
    'Larger tabs: 52px height; 15px labels',
    'Active indicator: full-width underline or filled pill',
    'Avoid more than 4 tabs on TV — spatial nav across many tabs is tiring',
  ]),
],

'textarea': [
  ('Mobile', [
    'Minimum 3 rows (80px) — expands with content up to 6 rows then scrolls',
    'Soft keyboard pushes layout up — field stays visible above keyboard',
    'Character counter in bottom-right corner of the textarea wrapper',
    'Avoid fixed-height textareas that crop typed content',
  ]),
  ('Web', [
    'Resize handle visible in bottom-right corner (resize: vertical)',
    'Auto-resize option available — grows with content, no manual resize',
    'Max-height cap with internal scroll for auto-resize mode',
    'Keyboard: Tab moves focus out; Shift+Tab re-enters field',
  ]),
  ('TV', [
    'On-screen keyboard shown on focus — textarea must be large enough to see input',
    'Fixed height (5 rows minimum) — no auto-resize on TV',
    'Avoid textareas on TV where possible — redirect to companion app for text entry',
  ]),
],

'toggle-group': [
  ('Mobile', [
    'Horizontal layout with full-width stretching (flex:1 per item)',
    '36px height — adequate touch target with horizontal padding',
    'Max 4 items in a row on mobile — more items cause label truncation',
    'Selected item must be clearly distinct — not just border change',
  ]),
  ('Web', [
    'Keyboard: Left/Right arrow keys navigate; Enter/Space toggles',
    'Hover: glass-1 background tint on non-selected items',
    'Compact 28px variant for toolbar contexts',
    'Tooltip on icon-only variants — aria-label required',
  ]),
  ('TV', [
    'D-pad Left/Right navigates items; OK toggles',
    'Focus ring on currently focused item within the group',
    'Large variant (44px) recommended on TV',
    'Selected state: jio-green fill — must be visible at 10 feet',
  ]),
],

'tooltip': [
  ('Mobile', [
    'Not triggered by hover — use long-press to show, tap-outside to dismiss',
    'Alternatively replace with a visible caption or hint text below the element',
    'Do not rely solely on tooltip for critical mobile guidance',
  ]),
  ('Web', [
    'Opens after 300ms hover delay; closes immediately on mouse-leave',
    'Position flips automatically on viewport collision (top ↔ bottom)',
    'Keyboard focus shows tooltip — same as hover state',
    'Max 200px width, single line preferred; use Popover for longer content',
  ]),
  ('TV', [
    'Not used on TV — show a persistent caption below the focused element instead',
    'If info is critical, show it inline rather than on demand',
  ]),
],

'tv-focus': [
  ('Mobile', [
    'Not used — mobile focus is handled via :focus-visible CSS natively',
  ]),
  ('Web', [
    'Not used on web — web focus ring uses standard :focus-visible + jio-green outline',
    'TV focus component is TV-only; do not apply on web-targeted elements',
  ]),
  ('TV', [
    'Apply to every interactive element — cards, buttons, list items, nav items',
    'Ring: box-shadow 0 0 0 3px var(--jio), 0 0 24px rgba(0,168,89,.4)',
    'Scale: 1.08 for cards; 1.06 for buttons; 1.0 for full-width items',
    'D-pad spatial navigation: register elements in the nav grid',
    'Never remove the focus ring — required for accessibility on TV',
    'Pressed (OK): scale(0.95) flash then return to focused scale',
  ]),
],

}

# ── Injection logic ─────────────────────────────────────────────────────────────

def inject(comp_name, data, dry_run=False):
    path = os.path.join(BASE, comp_name, 'index.html')
    if not os.path.exists(path):
        return 'SKIP — not found'
    html = open(path, encoding='utf-8').read()
    if 'id="platform"' in html:
        return 'already complete'

    section_html = make_platform(data)
    anchors = ['id="accessibility"', 'id="code-examples"', 'id="code"', 'id="api"']
    inserted = False
    for anchor in anchors:
        idx = html.find(anchor)
        if idx != -1:
            start = html.rfind('\n  <', 0, idx)
            if start != -1:
                html = html[:start] + section_html + html[start:]
                inserted = True
                break
    if not inserted:
        html = html.replace('</main>', section_html + '</main>', 1)

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        tmp_path = os.path.join(TMP, comp_name, 'index.html')
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        shutil.copy2(path, tmp_path)

    return 'injected platform'


if __name__ == '__main__':
    args = sys.argv[1:]
    targets = list(PLATFORM.keys()) if ('--all' in args or not args) else args
    print(f"\n{'Component':<24} Result")
    print('-' * 50)
    for name in targets:
        if name not in PLATFORM:
            print(f"  {name:<22} NOT IN DATA — skipped")
            continue
        print(f"  {name:<22} {inject(name, PLATFORM[name])}")
    print()

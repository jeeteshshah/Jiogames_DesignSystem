#!/usr/bin/env python3
"""
inject_batch.py — injects missing sections into DLS component pages.
Usage: python3 tools/inject_batch.py [component1 component2 ...]
       python3 tools/inject_batch.py --all
"""
import os, re, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP  = '/tmp/jiogames-dls-preview'

FIGMA_CHIP = '''<a href="#" class="component-figma-chip" style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.05);border:1px solid var(--border-subtle);border-radius:var(--pill);padding:4px 10px;font-size:10px;font-weight:700;color:var(--text3);text-decoration:none;margin-top:4px;" aria-label="View in Figma">
        <svg width="10" height="14" viewBox="0 0 10 14" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M5 7C5 5.89 5.895 5 7 5C8.105 5 9 5.895 9 7C9 8.105 8.105 9 7 9C5.895 9 5 8.105 5 7Z" fill="#1ABCFE"/><path d="M1 11C1 9.895 1.895 9 3 9H5V11C5 12.105 4.105 13 3 13C1.895 13 1 12.105 1 11Z" fill="#0ACF83"/><path d="M5 1V5H7C8.105 5 9 4.105 9 3C9 1.895 8.105 1 7 1H5Z" fill="#FF7262"/><path d="M1 3C1 4.105 1.895 5 3 5H5V1H3C1.895 1 1 1.895 1 3Z" fill="#F24E1E"/><path d="M1 7C1 8.105 1.895 9 3 9H5V5H3C1.895 5 1 5.895 1 7Z" fill="#A259FF"/></svg>
        DLS / {category} / {name}
      </a>'''

def make_when_to_use(use_items, dont_items):
    use_li  = ''.join(f'\n              <li>{x}</li>' for x in use_items)
    dont_li = ''.join(f'\n              <li>{x}</li>' for x in dont_items)
    return f'''
  <!-- WHEN TO USE -->
  <section class="ds-section" id="when-to-use">
    <h2 class="ds-section-title">When to use</h2>
    <div class="ds-usage-grid">
      <div class="ds-usage-card ds-usage-card--do">
        <p class="ds-usage-label ds-usage-label--do">Use when</p>
        <ul class="ds-usage-list">{use_li}
        </ul>
      </div>
      <div class="ds-usage-card ds-usage-card--dont">
        <p class="ds-usage-label ds-usage-label--dont">Don't use when</p>
        <ul class="ds-usage-list">{dont_li}
        </ul>
      </div>
    </div>
  </section>
'''

def make_motion(rows):
    trs = ''
    for r in rows:
        trs += f'\n        <tr><td>{r[0]}</td><td><code>{r[1]}</code></td><td><code>{r[2]}</code></td><td>{r[3]}</td></tr>'
    return f'''
  <!-- MOTION -->
  <section class="ds-section" id="motion">
    <h2 class="ds-section-title">Motion</h2>
    <table class="ds-motion-table">
      <thead><tr><th>Interaction</th><th>Easing</th><th>Duration</th><th>Property</th></tr></thead>
      <tbody>{trs}
      </tbody>
    </table>
  </section>
'''

def make_api(css_rows, react_rows):
    css_trs = ''
    for r in css_rows:
        css_trs += f'\n        <tr><td><code>{r[0]}</code></td><td>{r[1]}</td></tr>'
    react_trs = ''
    for r in react_rows:
        react_trs += f'\n        <tr><td><code>{r[0]}</code></td><td><span class="api-type">{r[1]}</span></td><td><span class="api-default">{r[2]}</span></td><td>{r[3]}</td></tr>'
    return f'''
  <!-- API -->
  <section class="ds-section" id="api">
    <h2 class="ds-section-title">API</h2>
    <h3 class="ds-section-subtitle" style="font-size:13px;font-weight:700;color:var(--text);margin:0 0 12px;">CSS classes</h3>
    <table class="ds-api-table">
      <thead><tr><th>Class</th><th>Description</th></tr></thead>
      <tbody>{css_trs}
      </tbody>
    </table>
    <h3 class="ds-section-subtitle" style="font-size:13px;font-weight:700;color:var(--text);margin:24px 0 12px;">React props</h3>
    <table class="ds-api-table">
      <thead><tr><th>Prop</th><th>Type</th><th>Default</th><th>Description</th></tr></thead>
      <tbody>{react_trs}
      </tbody>
    </table>
  </section>
'''

# ── Component data ─────────────────────────────────────────────────────────────

COMPONENTS = {

'accordion': dict(
  figma_cat='Components', figma_name='Accordion',
  use=[
    'Displaying FAQs, settings categories, or grouped help content',
    'Collapsing secondary content to reduce initial visual load',
    'Navigation menus with expandable sub-items',
    'Long-form content that benefits from progressive disclosure',
  ],
  dont=[
    'Critical content that users must see — use a visible section instead',
    'Fewer than 2 items — just show the content directly',
    'Deeply nested accordions (more than 2 levels)',
    'Content that changes frequently — use tabs instead',
  ],
  motion=[
    ('Expand', '--ease-out', '--dur-fast', 'max-height, opacity'),
    ('Collapse', '--ease-in', '--dur-fast', 'max-height, opacity'),
    ('Chevron rotate', '--ease-out', '--dur-fast', 'transform rotate(180deg)'),
    ('Hover', '--ease-out', '100ms', 'background'),
    ('Focus ring', 'instant', '0ms', 'outline'),
  ],
  css=[
    ('.ds-accordion', 'Root container — stacked accordion items'),
    ('.ds-accordion-item', 'Single expandable row'),
    ('.ds-accordion-trigger', 'Clickable header button'),
    ('.ds-accordion-trigger[aria-expanded="true"]', 'Open state — green title text'),
    ('.ds-accordion-body', 'Collapsible content area'),
    ('.ds-accordion-item--disabled', 'Disabled item — 38% opacity, no pointer events'),
  ],
  react=[
    ('type', '"single" | "multiple"', '"single"', 'Allow one or multiple items open at once'),
    ('defaultValue', 'string | string[]', 'undefined', 'Initially open item(s)'),
    ('value', 'string | string[]', 'undefined', 'Controlled open state'),
    ('onValueChange', '(value) => void', 'undefined', 'Fired when open state changes'),
    ('disabled', 'boolean', 'false', 'Disable all items'),
    ('collapsible', 'boolean', 'false', 'Allow closing the open item in single mode'),
  ],
),

'appbar': dict(
  figma_cat='Components', figma_name='App Bar',
  use=[
    'Top navigation on every primary screen — provides consistent wayfinding',
    'Back navigation with a title on detail or secondary screens',
    'Search entry point — tapping the bar activates search mode',
    'Action icons (share, filter, overflow) when there are ≤3 actions',
  ],
  dont=[
    'Hiding the bar on content screens — users lose navigation context',
    'More than 3 right-side icon buttons — use an overflow menu instead',
    'Long page titles — truncate to one line with ellipsis',
    'Using a custom header that breaks the consistent bar height (64px mobile)',
  ],
  motion=[
    ('Scroll hide', '--ease-in', '--dur-base', 'transform translateY(-100%)'),
    ('Scroll reveal', '--ease-out', '--dur-base', 'transform translateY(0)'),
    ('Search expand', '--ease-out', '--dur-fast', 'width, opacity'),
    ('Cinematic fade-in', '--ease-out', '--dur-slow', 'opacity'),
    ('Icon press', '--ease-out', '80ms', 'transform scale(0.9)'),
    ('TV focus ring', '--ease-out', '--dur-fast', 'box-shadow'),
  ],
  css=[
    ('.ds-appbar', 'Root bar container — 64px height, full width'),
    ('.ds-appbar--transparent', 'Transparent background (cinematic screens)'),
    ('.ds-appbar--search', 'Search-active state — surface-2 background'),
    ('.ds-appbar__title', 'Screen title — truncated single line'),
    ('.ds-appbar__icon-btn', '44×44px touch target icon button'),
    ('.ds-appbar__search-input', 'Inline search field inside the bar'),
  ],
  react=[
    ('variant', '"default" | "transparent" | "search"', '"default"', 'Visual variant'),
    ('title', 'string', 'undefined', 'Screen title shown in the bar'),
    ('onBack', '() => void', 'undefined', 'Render back button and fire on press'),
    ('actions', 'ReactNode[]', '[]', 'Right-side icon buttons (max 3)'),
    ('searchValue', 'string', 'undefined', 'Controlled search input value'),
    ('onSearchChange', '(v: string) => void', 'undefined', 'Fired on search input change'),
  ],
),

'aspect-ratio': dict(
  figma_cat='Layout', figma_name='Aspect Ratio',
  use=[
    'Game thumbnails and hero images — enforce 16:9 or 4:3 without layout shift',
    'Video players and embedded media that must maintain proportions',
    'Cards with image areas where content varies in size',
    'Skeleton loaders that must match the final image dimensions',
  ],
  dont=[
    'Text-only containers — let content determine height naturally',
    'UI chrome (buttons, inputs) — fixed heights are more appropriate',
    'Containers where the ratio is unknown at design time',
    'TV full-screen hero areas — use fill/cover directly',
  ],
  motion=[
    ('Image load fade', '--ease-out', '--dur-base', 'opacity'),
    ('Skeleton pulse', 'linear', '1400ms infinite', 'opacity 1 → 0.4 → 1'),
  ],
  css=[
    ('.ds-aspect-ratio', 'Root — sets padding-top to enforce ratio'),
    ('.ds-aspect-ratio--16-9', '16:9 ratio (56.25% padding-top)'),
    ('.ds-aspect-ratio--4-3', '4:3 ratio (75% padding-top)'),
    ('.ds-aspect-ratio--1-1', 'Square ratio (100% padding-top)'),
    ('.ds-aspect-ratio__inner', 'Absolutely positioned content layer'),
  ],
  react=[
    ('ratio', 'number', '16/9', 'Width-to-height ratio (e.g. 16/9, 4/3, 1)'),
    ('children', 'ReactNode', 'required', 'Content to fill the constrained area'),
    ('className', 'string', 'undefined', 'Additional class on the root element'),
  ],
),

'avatar': dict(
  figma_cat='Components', figma_name='Avatar',
  use=[
    'User identity in comments, reviews, leaderboards, and chat',
    'Profile headers and account settings screens',
    'Multiplayer lobby participant slots',
    'Activity feeds showing who did what',
  ],
  dont=[
    'Decorative illustrations — use an image component instead',
    'More than 5 stacked avatars without a +N overflow indicator',
    'Sizes smaller than 24px — the fallback initials become unreadable',
    'As a button on its own without an accessible label',
  ],
  motion=[
    ('Image load fade', '--ease-out', '--dur-base', 'opacity'),
    ('Presence ring pulse', 'ease-in-out', '2s infinite', 'box-shadow scale'),
    ('Hover scale', '--ease-out', '--dur-fast', 'transform scale(1.05)'),
    ('Focus ring', 'instant', '0ms', 'outline'),
  ],
  css=[
    ('.ds-avatar', 'Root — circular container with overflow hidden'),
    ('.ds-avatar--sm', '24×24px'),
    ('.ds-avatar--md', '36×36px (default)'),
    ('.ds-avatar--lg', '48×48px'),
    ('.ds-avatar--xl', '64×64px'),
    ('.ds-avatar__fallback', 'Initials or icon shown when image fails'),
    ('.ds-avatar--online', 'Green presence ring'),
    ('.ds-avatar--offline', 'Grey presence ring'),
  ],
  react=[
    ('src', 'string', 'undefined', 'Image URL'),
    ('alt', 'string', 'required', 'Accessible description of the user'),
    ('fallback', 'string | ReactNode', 'undefined', 'Shown when image fails to load'),
    ('size', '"sm" | "md" | "lg" | "xl"', '"md"', 'Diameter preset'),
    ('presence', '"online" | "offline" | "none"', '"none"', 'Presence ring color'),
  ],
),

'badges': dict(
  figma_cat='Components', figma_name='Badge',
  use=[
    'Unread notification counts on tab bar icons or list items',
    'Status labels on game cards (New, Hot, Live, Sale)',
    'Pass tier indicators (Mobile Pass, Ultimate Pass)',
    'Achievement unlock indicators on profile screens',
  ],
  dont=[
    'Long text (more than ~12 characters) — use a chip or label instead',
    'Critical error messages — use a banner or toast instead',
    'Decorative only uses without meaningful status information',
    'Stacking multiple badges on one element — pick the most important',
  ],
  motion=[
    ('Count change', '--ease-out', '--dur-fast', 'transform scale(1.3 → 1)'),
    ('Appear', '--ease-out', '--dur-fast', 'transform scale(0 → 1), opacity'),
    ('Dismiss', '--ease-in', '--dur-fast', 'transform scale(1 → 0), opacity'),
  ],
  css=[
    ('.ds-badge', 'Root badge — pill shape, numeric or short text'),
    ('.ds-badge--dot', 'Dot-only badge (no text, for unread indicator)'),
    ('.ds-badge--new', 'Green "New" label'),
    ('.ds-badge--hot', 'Amber "Hot" label'),
    ('.ds-badge--live', 'Red pulsing "Live" label'),
    ('.ds-badge--sale', 'Purple "Sale" label'),
    ('.ds-badge--pass', 'JioGames Pass tier badge'),
  ],
  react=[
    ('variant', '"default" | "dot" | "new" | "hot" | "live" | "sale" | "pass"', '"default"', 'Visual style'),
    ('count', 'number', 'undefined', 'Numeric count — shows "99+" above 99'),
    ('max', 'number', '99', 'Threshold before showing "+" suffix'),
    ('showZero', 'boolean', 'false', 'Show badge even when count is 0'),
    ('children', 'ReactNode', 'undefined', 'Element to attach the badge to'),
  ],
),



# ── BATCH 2 ────────────────────────────────────────────────────────────────────

'banners': dict(
  figma_cat='Components', figma_name='Banner',
  use=[
    'System-level messages affecting the whole screen (maintenance, offline, subscription)',
    'Dismissible promotional messages at the top of a screen',
    'Pass activation confirmations after login',
    'Non-blocking warnings that require no immediate action',
  ],
  dont=[
    'Transient feedback (success/error after an action) — use Toast instead',
    'Destructive confirmations — use a Dialog',
    'More than one banner at a time — stack creates visual noise',
    'Marketing messages inside content areas — use a Card instead',
  ],
  motion=[
    ('Slide in (top)', '--ease-out', '--dur-base', 'transform translateY(-100% → 0)'),
    ('Slide out (top)', '--ease-in', '--dur-fast', 'transform translateY(0 → -100%)'),
    ('Fade in', '--ease-out', '--dur-base', 'opacity'),
    ('Dismiss', '--ease-in', '--dur-fast', 'opacity, max-height'),
  ],
  css=[
    ('.ds-banner', 'Root banner — full width, top of screen'),
    ('.ds-banner--info', 'Informational — blue accent'),
    ('.ds-banner--success', 'Success — green accent'),
    ('.ds-banner--warning', 'Warning — amber accent'),
    ('.ds-banner--error', 'Error — red accent'),
    ('.ds-banner--pass', 'JioGames Pass promotion — green gradient'),
    ('.ds-banner__dismiss', 'Close button — top-right'),
  ],
  react=[
    ('variant', '"info" | "success" | "warning" | "error" | "pass"', '"info"', 'Semantic color variant'),
    ('dismissible', 'boolean', 'true', 'Show close button'),
    ('onDismiss', '() => void', 'undefined', 'Fired when banner is closed'),
    ('icon', 'ReactNode', 'undefined', 'Leading icon override'),
    ('action', '{ label: string; onClick: () => void }', 'undefined', 'Optional CTA link'),
  ],
),

'bottom-sheet': dict(
  figma_cat='Overlays', figma_name='Bottom Sheet',
  use=[
    'Contextual actions for a selected item (share, report, save)',
    'Multi-step flows that should not block the full screen',
    'Filters and sort options on list/grid screens',
    'Pass upsell panels that slide up over content',
  ],
  dont=[
    'Full app flows with many steps — use a dedicated screen',
    'Confirmation dialogs — use Dialog for destructive actions',
    'Content taller than 90vh without internal scrolling',
    'Nesting one bottom sheet inside another',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-base', 'transform translateY(100% → 0)'),
    ('Close (swipe/button)', '--ease-in', '--dur-fast', 'transform translateY(0 → 100%)'),
    ('Scrim fade in', '--ease-out', '--dur-base', 'opacity'),
    ('Snap expand', '--ease-out', '--dur-base', 'height'),
    ('Handle drag', 'none', 'realtime', 'transform translateY'),
  ],
  css=[
    ('.ds-bottom-sheet', 'Root sheet — fixed bottom, full width'),
    ('.ds-bottom-sheet__handle', '40×4px drag handle — centered top'),
    ('.ds-bottom-sheet__header', 'Optional title row'),
    ('.ds-bottom-sheet__body', 'Scrollable content area'),
    ('.ds-bottom-sheet__scrim', 'Full-screen backdrop'),
    ('.ds-bottom-sheet--open', 'Visible state — translateY(0)'),
  ],
  react=[
    ('open', 'boolean', 'required', 'Controls sheet visibility'),
    ('onClose', '() => void', 'required', 'Fired on scrim tap or swipe down'),
    ('snapPoints', 'number[]', '[0.5, 0.9]', 'Snap heights as fraction of viewport'),
    ('defaultSnap', 'number', '0', 'Index into snapPoints for initial open height'),
    ('title', 'string', 'undefined', 'Optional header title'),
    ('children', 'ReactNode', 'required', 'Sheet body content'),
  ],
),

'calendar': dict(
  figma_cat='Complex', figma_name='Calendar',
  use=[
    'Event scheduling and date selection in forms',
    'Date range pickers for filters (e.g. subscription history)',
    'Booking flows where specific dates must be selected',
  ],
  dont=[
    'Selecting only a year or month — use a simpler select/dropdown',
    'Read-only date display — use a formatted text label',
    'Multiple independent calendars on the same screen',
  ],
  motion=[
    ('Month change (next)', '--ease-out', '--dur-fast', 'transform translateX(-100% → 0), opacity'),
    ('Month change (prev)', '--ease-out', '--dur-fast', 'transform translateX(100% → 0), opacity'),
    ('Day select', '--ease-out', '80ms', 'background, transform scale'),
    ('Range highlight', '--ease-out', '--dur-fast', 'background'),
    ('Focus ring', 'instant', '0ms', 'outline'),
  ],
  css=[
    ('.ds-calendar', 'Root calendar container'),
    ('.ds-calendar__nav', 'Month/year navigation row'),
    ('.ds-calendar__grid', '7-column day grid'),
    ('.ds-calendar__day', 'Individual day cell — 40×40px touch target'),
    ('.ds-calendar__day--selected', 'Selected day — green fill'),
    ('.ds-calendar__day--today', 'Today — green ring'),
    ('.ds-calendar__day--range', 'In-range days — green tint fill'),
    ('.ds-calendar__day--disabled', 'Non-selectable day — 38% opacity'),
  ],
  react=[
    ('mode', '"single" | "range" | "multiple"', '"single"', 'Selection mode'),
    ('selected', 'Date | DateRange | Date[]', 'undefined', 'Controlled selected value'),
    ('onSelect', '(date) => void', 'undefined', 'Fired on day selection'),
    ('disabled', 'Matcher | Matcher[]', 'undefined', 'Disable specific dates or ranges'),
    ('fromDate', 'Date', 'undefined', 'Minimum selectable date'),
    ('toDate', 'Date', 'undefined', 'Maximum selectable date'),
  ],
),

'cards': dict(
  figma_cat='Components', figma_name='Card',
  use=[
    'Game tiles in horizontal rails and grid layouts',
    'Pass plan comparison with price and features',
    'Content previews with thumbnail, title, and metadata',
    'Leaderboard entries, achievement items, and list rows with rich media',
  ],
  dont=[
    'Full-bleed editorial sections — use a section layout instead',
    'Single lines of text with no visual hierarchy — use a List item',
    'Deeply nested cards (card inside card)',
    'Interactive cards without a visible affordance (hover/focus state)',
  ],
  motion=[
    ('Hover lift', '--ease-out', '--dur-fast', 'transform scale(1.02), box-shadow'),
    ('Press', '--ease-out', '80ms', 'transform scale(0.97)'),
    ('TV focus scale', '--ease-out', '--dur-fast', 'transform scale(1.06)'),
    ('Image load fade', '--ease-out', '--dur-base', 'opacity'),
    ('Skeleton shimmer', 'linear', '1400ms infinite', 'background-position'),
  ],
  css=[
    ('.ds-card', 'Base card — surface-1 bg, border-subtle, r4 radius'),
    ('.ds-card--game', 'Game tile — 16:9 thumbnail + title + metadata'),
    ('.ds-card--pass', 'Pass plan card — gradient header, feature list'),
    ('.ds-card--wide', 'Landscape card for horizontal rails (210×128px)'),
    ('.ds-card--portrait', 'Portrait cover card (120×180px)'),
    ('.ds-card__thumbnail', 'Image container — aspect-ratio enforced'),
    ('.ds-card__body', 'Text content area — padding 12px'),
    ('.ds-card__title', 'Card title — 13px 600 weight'),
    ('.ds-card__meta', 'Secondary info row — 11px text3'),
  ],
  react=[
    ('variant', '"game" | "pass" | "wide" | "portrait" | "default"', '"default"', 'Card layout preset'),
    ('href', 'string', 'undefined', 'Makes card a link — wraps in anchor'),
    ('onClick', '() => void', 'undefined', 'Press handler'),
    ('thumbnail', 'string', 'undefined', 'Image URL for the card hero'),
    ('title', 'string', 'required', 'Card headline text'),
    ('meta', 'string | ReactNode', 'undefined', 'Secondary descriptor below title'),
    ('badge', 'ReactNode', 'undefined', 'Overlay badge (New, Hot, Live)'),
  ],
),

'carousel-component': dict(
  figma_cat='Components', figma_name='Carousel',
  use=[
    'Featured game highlights on the home screen hero area',
    'Onboarding steps or feature introduction slides',
    'Image galleries on game detail pages',
    'Horizontal scrolling when items overflow the viewport',
  ],
  dont=[
    'Primary navigation — carousels hide content from users',
    'More than 7-8 slides without clear navigation affordance',
    'Auto-advancing carousels with content users need to read',
    'Nested carousels',
  ],
  motion=[
    ('Swipe slide', '--ease-out', '--dur-base', 'transform translateX'),
    ('Auto-advance', '--ease-in-out', '--dur-slow', 'transform translateX'),
    ('Dot indicator', '--ease-out', '--dur-fast', 'width (active dot expands)'),
    ('Arrow button press', '--ease-out', '80ms', 'transform scale(0.92)'),
    ('Fade transition (alt)', '--ease-out', '--dur-base', 'opacity'),
  ],
  css=[
    ('.ds-carousel', 'Root — overflow hidden wrapper'),
    ('.ds-carousel__track', 'Flex row of slides — transform driven'),
    ('.ds-carousel__slide', 'Single slide — flex-shrink:0, full width'),
    ('.ds-carousel__dots', 'Dot indicator row — centered below'),
    ('.ds-carousel__dot', 'Individual dot — 6px circle'),
    ('.ds-carousel__dot--active', 'Active dot — expands to 18px width'),
    ('.ds-carousel__arrow', 'Previous/next button'),
  ],
  react=[
    ('autoPlay', 'boolean', 'false', 'Enable auto-advance'),
    ('interval', 'number', '4000', 'Auto-advance delay in ms'),
    ('loop', 'boolean', 'true', 'Wrap around at start/end'),
    ('showDots', 'boolean', 'true', 'Show dot indicators'),
    ('showArrows', 'boolean', 'false', 'Show prev/next arrow buttons'),
    ('index', 'number', 'undefined', 'Controlled current slide index'),
    ('onIndexChange', '(i: number) => void', 'undefined', 'Fired on slide change'),
  ],
),

# ── BATCH 3 ────────────────────────────────────────────────────────────────────

'chart': dict(
  figma_cat='Data', figma_name='Chart',
  use=[
    'Pass usage statistics and game time analytics in profile',
    'Leaderboard score progression over time',
    'Revenue/download metrics in internal dashboards',
    'Achievement completion rates as radial or bar charts',
  ],
  dont=[
    'Replacing data tables when exact values matter more than trends',
    'More than 7 data series on a single chart — cognitive overload',
    'Purely decorative data visualization without accessible text fallback',
  ],
  motion=[
    ('Bar grow', '--ease-out', '--dur-slow', 'height (staggered per bar)'),
    ('Line draw', '--ease-out', '--dur-slow', 'stroke-dashoffset'),
    ('Tooltip appear', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px)'),
    ('Legend item hover', '--ease-out', '--dur-fast', 'opacity (others dim to 0.4)'),
  ],
  css=[
    ('.ds-chart', 'Root chart wrapper — sets height and position:relative'),
    ('.ds-chart__canvas', 'Chart.js canvas element'),
    ('.ds-chart__legend', 'Custom legend row above/below chart'),
    ('.ds-chart__legend-item', 'Color swatch + label pair'),
    ('.ds-chart__tooltip', 'Custom tooltip overlay'),
  ],
  react=[
    ('type', '"bar" | "line" | "area" | "donut" | "radial"', '"bar"', 'Chart type'),
    ('data', 'ChartData', 'required', 'Chart.js-compatible data object'),
    ('height', 'number', '240', 'Canvas height in px'),
    ('legend', 'boolean', 'true', 'Show custom legend'),
    ('animate', 'boolean', 'true', 'Enable enter animations'),
  ],
),

'checkbox': dict(
  figma_cat='Forms', figma_name='Checkbox',
  use=[
    'Selecting multiple items from a list (genres, platforms, filters)',
    'Terms and conditions acceptance in forms',
    'Preference settings where options are independent of each other',
    'Bulk-select actions in data tables',
  ],
  dont=[
    'Mutually exclusive choices — use Radio instead',
    'Binary on/off settings — use Toggle/Switch instead',
    'More than ~12 options without grouping or search',
  ],
  motion=[
    ('Check mark draw', '--ease-out', '--dur-fast', 'stroke-dashoffset'),
    ('Box fill', '--ease-out', '--dur-fast', 'background, border-color'),
    ('Indeterminate line', '--ease-out', '--dur-fast', 'transform scaleX'),
    ('Focus ring', 'instant', '0ms', 'outline'),
    ('Hover', '--ease-out', '100ms', 'background'),
  ],
  css=[
    ('.ds-checkbox', 'Root — flex row, label + control'),
    ('.ds-checkbox__control', '20×20px box — border-subtle, r2'),
    ('.ds-checkbox__control--checked', 'Green fill, white checkmark'),
    ('.ds-checkbox__control--indeterminate', 'Green fill, white dash'),
    ('.ds-checkbox__control--disabled', '38% opacity, pointer-events none'),
    ('.ds-checkbox__label', 'Text label — 14px text2'),
  ],
  react=[
    ('checked', 'boolean | "indeterminate"', 'undefined', 'Controlled checked state'),
    ('defaultChecked', 'boolean', 'false', 'Uncontrolled initial state'),
    ('onCheckedChange', '(v: boolean | "indeterminate") => void', 'undefined', 'Change handler'),
    ('disabled', 'boolean', 'false', 'Disable interaction'),
    ('id', 'string', 'undefined', 'Links to a <label> element'),
  ],
),

'chips': dict(
  figma_cat='Components', figma_name='Chip',
  use=[
    'Genre and platform filter pills on discovery screens',
    'Active filter tags that can be dismissed',
    'Multi-select input values shown as removable tags',
    'Status indicators inside list items (inline metadata)',
  ],
  dont=[
    'Primary CTAs — use Button instead',
    'Long text (more than ~20 chars) — truncate or use a different pattern',
    'More than ~10 chips in a single row without horizontal scroll',
    'Replacing navigation tabs — use Tab Bar instead',
  ],
  motion=[
    ('Select (toggle on)', '--ease-out', '--dur-fast', 'background, border-color, color'),
    ('Deselect (toggle off)', '--ease-out', '--dur-fast', 'background, border-color'),
    ('Dismiss/remove', '--ease-in', '--dur-fast', 'transform scale(0), opacity, max-width'),
    ('Appear', '--ease-out', '--dur-fast', 'transform scale(0.85 → 1), opacity'),
    ('Press', '--ease-out', '80ms', 'transform scale(0.95)'),
  ],
  css=[
    ('.ds-chip', 'Base chip — pill shape, border-subtle'),
    ('.ds-chip--selected', 'Active state — jio-green fill, white text'),
    ('.ds-chip--sm', 'Small — 28px height, 12px font'),
    ('.ds-chip--md', 'Default — 36px height, 13px font'),
    ('.ds-chip__icon', 'Leading icon — 16px, inherits color'),
    ('.ds-chip__dismiss', 'Trailing × button — 16px, only shown when removable'),
  ],
  react=[
    ('selected', 'boolean', 'false', 'Active/selected state'),
    ('onSelect', '() => void', 'undefined', 'Toggle handler'),
    ('onRemove', '() => void', 'undefined', 'Shows × button and fires on click'),
    ('size', '"sm" | "md"', '"md"', 'Height preset'),
    ('icon', 'ReactNode', 'undefined', 'Leading icon element'),
    ('disabled', 'boolean', 'false', 'Disable interaction'),
  ],
),

'collapsible': dict(
  figma_cat='Components', figma_name='Collapsible',
  use=[
    'Showing/hiding optional secondary content below a trigger',
    'Expandable code blocks or long descriptions',
    'Advanced options sections in settings forms',
    'Read more / show less patterns for truncated text',
  ],
  dont=[
    'Multiple related collapsible sections — use Accordion instead',
    'Critical information that should always be visible',
    'Navigation items with sub-sections — use NavigationMenu instead',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-fast', 'max-height, opacity'),
    ('Close', '--ease-in', '--dur-fast', 'max-height, opacity'),
    ('Chevron rotate', '--ease-out', '--dur-fast', 'transform rotate(180deg)'),
  ],
  css=[
    ('.ds-collapsible', 'Root container'),
    ('.ds-collapsible__trigger', 'Toggle button — full width or inline'),
    ('.ds-collapsible__content', 'Collapsible content area — overflow hidden'),
    ('.ds-collapsible__content--open', 'Expanded state'),
  ],
  react=[
    ('open', 'boolean', 'undefined', 'Controlled open state'),
    ('defaultOpen', 'boolean', 'false', 'Uncontrolled initial state'),
    ('onOpenChange', '(open: boolean) => void', 'undefined', 'Change handler'),
    ('disabled', 'boolean', 'false', 'Prevent toggling'),
  ],
),

'combobox': dict(
  figma_cat='Forms', figma_name='Combobox',
  use=[
    'Searchable select for large option sets (countries, games, genres)',
    'Tag/token input where users type and pick from suggestions',
    'Game search with autocomplete suggestions',
    'Any select with more than ~10 options where filtering helps',
  ],
  dont=[
    'Small option sets (≤8 items) — use Select instead',
    'Simple yes/no or binary choices — use Toggle or Radio',
    'Freeform text input where no predefined options exist — use Input',
  ],
  motion=[
    ('Dropdown open', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Dropdown close', '--ease-in', '--dur-fast', 'opacity'),
    ('Option highlight', '--ease-out', '80ms', 'background'),
    ('Selection chip appear', '--ease-out', '--dur-fast', 'transform scale(0.85 → 1), opacity'),
  ],
  css=[
    ('.ds-combobox', 'Root container'),
    ('.ds-combobox__input', 'Text input — triggers dropdown'),
    ('.ds-combobox__dropdown', 'Options list — surface-2, shadow, r4'),
    ('.ds-combobox__option', 'Single option row — 40px height'),
    ('.ds-combobox__option--active', 'Highlighted option — glass-1 bg'),
    ('.ds-combobox__option--selected', 'Chosen option — green checkmark'),
    ('.ds-combobox__empty', 'No results message'),
  ],
  react=[
    ('value', 'string | string[]', 'undefined', 'Controlled selected value(s)'),
    ('onValueChange', '(v: string | string[]) => void', 'undefined', 'Selection change handler'),
    ('options', '{ value: string; label: string }[]', 'required', 'Available options'),
    ('multiple', 'boolean', 'false', 'Enable multi-select'),
    ('placeholder', 'string', '"Search…"', 'Input placeholder text'),
    ('disabled', 'boolean', 'false', 'Disable the control'),
  ],
),

# ── BATCH 4 ────────────────────────────────────────────────────────────────────

'command': dict(
  figma_cat='Overlays', figma_name='Command',
  use=[
    'Global search palette triggered by keyboard shortcut (⌘K)',
    'Quick action launcher for power users on web/desktop',
    'In-app navigation shortcut across all screens',
  ],
  dont=[
    'Mobile as primary search — use the AppBar search instead',
    'Replacing contextual menus (right-click or long-press)',
    'Exposing commands users do not need frequently',
  ],
  motion=[
    ('Dialog open', '--ease-out', '--dur-fast', 'opacity, transform scale(0.96 → 1)'),
    ('Dialog close', '--ease-in', '--dur-fast', 'opacity, transform scale(1 → 0.96)'),
    ('Scrim fade', '--ease-out', '--dur-fast', 'opacity'),
    ('Item highlight', '--ease-out', '60ms', 'background'),
    ('Group header appear', '--ease-out', '--dur-fast', 'opacity'),
  ],
  css=[
    ('.ds-command', 'Root dialog wrapper — centered overlay'),
    ('.ds-command__input', 'Search text field — top of palette'),
    ('.ds-command__list', 'Scrollable results area'),
    ('.ds-command__group', 'Labelled result section'),
    ('.ds-command__item', 'Single result row — 40px height'),
    ('.ds-command__item--selected', 'Keyboard-highlighted item'),
    ('.ds-command__empty', 'No results state'),
    ('.ds-command__scrim', 'Full-screen backdrop'),
  ],
  react=[
    ('open', 'boolean', 'required', 'Controls palette visibility'),
    ('onOpenChange', '(open: boolean) => void', 'required', 'Close handler'),
    ('placeholder', 'string', '"Search commands…"', 'Input placeholder'),
    ('onSelect', '(value: string) => void', 'undefined', 'Fired when item chosen'),
    ('children', 'ReactNode', 'required', 'CommandGroup and CommandItem nodes'),
  ],
),

'context-menu': dict(
  figma_cat='Overlays', figma_name='Context Menu',
  use=[
    'Right-click or long-press actions on game cards and list items',
    'Quick actions: add to wishlist, share, remove from list',
    'Contextual options that do not warrant a permanent UI element',
  ],
  dont=[
    'Primary or frequently used actions — put them in the main UI',
    'Mobile as the only way to access an action — must have a visible alternative',
    'More than ~8 items — split into submenus or a sheet',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-fast', 'opacity, transform scale(0.95 → 1)'),
    ('Close', '--ease-in', '--dur-fast', 'opacity'),
    ('Item highlight', '--ease-out', '60ms', 'background'),
    ('Submenu open', '--ease-out', '--dur-fast', 'opacity, transform translateX(-4px → 0)'),
  ],
  css=[
    ('.ds-context-menu', 'Root floating panel — surface-2, shadow, r4'),
    ('.ds-context-menu__item', 'Menu row — 40px height, padding 0 12px'),
    ('.ds-context-menu__item--destructive', 'Red label for delete actions'),
    ('.ds-context-menu__item--disabled', '38% opacity, no pointer events'),
    ('.ds-context-menu__separator', '1px border-subtle horizontal divider'),
    ('.ds-context-menu__label', 'Non-interactive section header — text3'),
  ],
  react=[
    ('children', 'ReactNode', 'required', 'Trigger element (wraps the target)'),
    ('items', 'MenuItem[]', 'required', 'Menu item definitions'),
    ('onSelect', '(item: MenuItem) => void', 'undefined', 'Item selection handler'),
  ],
),

'data-table': dict(
  figma_cat='Data', figma_name='Data Table',
  use=[
    'Sortable game library lists with multiple metadata columns',
    'Transaction history and subscription records',
    'Leaderboard rankings with stats columns',
    'Admin/internal dashboards with tabular data',
  ],
  dont=[
    'Mobile as a dense multi-column layout — collapse to cards or single column',
    'Simple 2-column key-value data — use a Description List',
    'Fewer than 3 rows — use a List instead',
  ],
  motion=[
    ('Row hover', '--ease-out', '80ms', 'background'),
    ('Sort arrow', '--ease-out', '--dur-fast', 'transform rotate, opacity'),
    ('Row select', '--ease-out', '--dur-fast', 'background'),
    ('Expand row', '--ease-out', '--dur-fast', 'max-height'),
    ('Column resize drag', 'none', 'realtime', 'width'),
  ],
  css=[
    ('.ds-table', 'Root table — border-collapse, full width'),
    ('.ds-table__head', 'Header row — surface-2 bg'),
    ('.ds-table th', 'Header cell — 11px 700 uppercase text3'),
    ('.ds-table td', 'Data cell — 13px text2, 48px row height'),
    ('.ds-table__row--selected', 'Selected row — jio-green tint bg'),
    ('.ds-table__row--hover', 'Hovered row — glass-1 bg'),
    ('.ds-table__sort-icon', 'Sort direction indicator'),
    ('.ds-table__empty', 'Empty state row — centered message'),
  ],
  react=[
    ('columns', 'ColumnDef[]', 'required', 'Column schema with id, header, accessor'),
    ('data', 'TData[]', 'required', 'Row data array'),
    ('sorting', 'SortingState', 'undefined', 'Controlled sort state'),
    ('onSortingChange', '(s: SortingState) => void', 'undefined', 'Sort change handler'),
    ('rowSelection', 'RowSelectionState', 'undefined', 'Controlled row selection'),
    ('onRowSelectionChange', '(s) => void', 'undefined', 'Selection change handler'),
    ('pageSize', 'number', '20', 'Rows per page'),
  ],
),

'date-picker': dict(
  figma_cat='Complex', figma_name='Date Picker',
  use=[
    'Subscription start/end date selection in settings',
    'Event scheduling forms',
    'Filter panels with date range inputs',
    'Birthday or account creation date fields',
  ],
  dont=[
    'Relative time inputs ("in 3 days") — use a different control',
    'Date-only display without user interaction — use a formatted label',
    'Inline date selection in compact UI — use Calendar component directly',
  ],
  motion=[
    ('Popover open', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Popover close', '--ease-in', '--dur-fast', 'opacity'),
    ('Month navigate', '--ease-out', '--dur-fast', 'transform translateX, opacity'),
    ('Day select', '--ease-out', '80ms', 'background scale'),
  ],
  css=[
    ('.ds-date-picker', 'Root — input + calendar popover'),
    ('.ds-date-picker__input', 'Trigger input field showing formatted date'),
    ('.ds-date-picker__popover', 'Floating calendar panel — surface-2, r4'),
    ('.ds-date-picker__calendar', 'Embedded Calendar component'),
  ],
  react=[
    ('value', 'Date | undefined', 'undefined', 'Controlled selected date'),
    ('onChange', '(date: Date | undefined) => void', 'undefined', 'Change handler'),
    ('placeholder', 'string', '"Pick a date"', 'Trigger input placeholder'),
    ('format', 'string', '"dd MMM yyyy"', 'Display format string'),
    ('disabled', '(date: Date) => boolean', 'undefined', 'Disable specific dates'),
    ('fromDate', 'Date', 'undefined', 'Minimum selectable date'),
    ('toDate', 'Date', 'undefined', 'Maximum selectable date'),
  ],
),

'dialogs': dict(
  figma_cat='Overlays', figma_name='Dialog',
  use=[
    'Destructive action confirmation (delete account, cancel subscription)',
    'Critical decisions requiring explicit user acknowledgement',
    'Short forms that should not navigate away from the current screen',
    'Error states requiring immediate user response',
  ],
  dont=[
    'Non-critical messages — use Toast or Banner instead',
    'Large forms or multi-step flows — use a dedicated screen or Bottom Sheet',
    'Stacking multiple dialogs — resolve one before showing another',
    'Auto-showing on page load without user trigger',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-fast', 'opacity, transform scale(0.95 → 1)'),
    ('Close', '--ease-in', '--dur-fast', 'opacity, transform scale(1 → 0.95)'),
    ('Scrim fade in', '--ease-out', '--dur-fast', 'opacity'),
    ('Scrim fade out', '--ease-in', '--dur-fast', 'opacity'),
    ('Shake (error)', '--ease-out', '400ms', 'transform translateX (keyframes)'),
  ],
  css=[
    ('.ds-dialog', 'Root dialog panel — surface-2, r5, max-w 480px'),
    ('.ds-dialog__scrim', 'Full-screen backdrop — rgba(0,0,0,.6)'),
    ('.ds-dialog__header', 'Title + optional icon row'),
    ('.ds-dialog__title', 'Dialog title — 18px 700'),
    ('.ds-dialog__body', 'Content area — 14px text2'),
    ('.ds-dialog__footer', 'Action buttons row — flex end'),
    ('.ds-dialog__close', 'Top-right × button'),
  ],
  react=[
    ('open', 'boolean', 'required', 'Controls dialog visibility'),
    ('onOpenChange', '(open: boolean) => void', 'required', 'Close handler'),
    ('title', 'string', 'required', 'Dialog heading'),
    ('description', 'string', 'undefined', 'Body copy below title'),
    ('actions', 'ReactNode', 'undefined', 'Footer button row'),
    ('size', '"sm" | "md" | "lg"', '"md"', 'Max-width preset'),
  ],
),

# ── BATCH 5 ────────────────────────────────────────────────────────────────────

'drawer': dict(
  figma_cat='Overlays', figma_name='Drawer',
  use=[
    'Side navigation panel on web/tablet (slides in from left)',
    'Settings panel on desktop that doesn\'t hide the main content entirely',
    'Filter panel on browse/discovery screens (slides from right)',
  ],
  dont=[
    'Mobile primary navigation — use Tab Bar instead',
    'Replacing Bottom Sheet on mobile — Drawer is a web/tablet pattern',
    'Content that should be always visible — use a sidebar layout',
  ],
  motion=[
    ('Open (left)', '--ease-out', '--dur-base', 'transform translateX(-100% → 0)'),
    ('Open (right)', '--ease-out', '--dur-base', 'transform translateX(100% → 0)'),
    ('Close', '--ease-in', '--dur-fast', 'transform translateX'),
    ('Scrim fade', '--ease-out', '--dur-base', 'opacity'),
    ('Content stagger', '--ease-out', '--dur-fast', 'opacity (items delayed 40ms each)'),
  ],
  css=[
    ('.ds-drawer', 'Root panel — fixed side, full height, surface-1'),
    ('.ds-drawer--left', 'Slides from left edge'),
    ('.ds-drawer--right', 'Slides from right edge'),
    ('.ds-drawer__header', 'Title row with close button'),
    ('.ds-drawer__body', 'Scrollable content area'),
    ('.ds-drawer__scrim', 'Full-screen backdrop'),
  ],
  react=[
    ('open', 'boolean', 'required', 'Controls drawer visibility'),
    ('onClose', '() => void', 'required', 'Close handler'),
    ('side', '"left" | "right"', '"left"', 'Slide direction'),
    ('width', 'number | string', '320', 'Panel width in px or CSS string'),
    ('title', 'string', 'undefined', 'Header title text'),
    ('children', 'ReactNode', 'required', 'Drawer body content'),
  ],
),

'dropdown-menu': dict(
  figma_cat='Overlays', figma_name='Dropdown Menu',
  use=[
    'Overflow action menus (⋯) on cards and list items',
    'Sort-by and view-toggle menus in toolbars',
    'User account menu in the AppBar (profile, settings, logout)',
    'Any set of ≤8 related actions triggered by a single button',
  ],
  dont=[
    'Primary navigation — use Tab Bar or NavigationMenu',
    'More than 8 items — use Command palette or a dedicated screen',
    'Single toggle actions — use a Switch/Toggle instead',
    'Destructive-only menus — always provide a safe cancel option',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-fast', 'opacity, transform scale(0.95 → 1) + translateY(-4px → 0)'),
    ('Close', '--ease-in', '--dur-fast', 'opacity, transform scale(1 → 0.95)'),
    ('Item highlight', '--ease-out', '60ms', 'background'),
    ('Submenu open', '--ease-out', '--dur-fast', 'opacity, transform translateX(-4px → 0)'),
    ('Chevron rotate', '--ease-out', '--dur-fast', 'transform rotate(0 → -180deg)'),
  ],
  css=[
    ('.ds-dropdown', 'Root floating panel — surface-2, r4, border-subtle'),
    ('.ds-dropdown__item', 'Menu row — 40px, padding 0 12px'),
    ('.ds-dropdown__item--destructive', 'Red color for delete items'),
    ('.ds-dropdown__item--disabled', '38% opacity'),
    ('.ds-dropdown__separator', '1px border-subtle divider'),
    ('.ds-dropdown__label', 'Non-interactive section header'),
    ('.ds-dropdown__check', 'Checkmark for toggle items'),
  ],
  react=[
    ('trigger', 'ReactNode', 'required', 'Element that opens the menu'),
    ('items', 'DropdownItem[]', 'required', 'Menu item definitions'),
    ('align', '"start" | "center" | "end"', '"end"', 'Horizontal alignment relative to trigger'),
    ('onSelect', '(item: DropdownItem) => void', 'undefined', 'Item selection handler'),
    ('open', 'boolean', 'undefined', 'Controlled open state'),
    ('onOpenChange', '(open: boolean) => void', 'undefined', 'Open state change handler'),
  ],
),

'forms': dict(
  figma_cat='Forms', figma_name='Form',
  use=[
    'Multi-field data collection: registration, profile edit, payment',
    'Structured settings pages with labelled controls',
    'Feedback and support request flows',
    'Search filter panels with multiple input types',
  ],
  dont=[
    'Single-field interactions — use the Input component directly',
    'Wizard-style flows with more than 5 steps — split into separate screens',
    'Read-only data display — use a Description List instead',
  ],
  motion=[
    ('Validation error shake', '--ease-out', '400ms', 'transform translateX (keyframes)'),
    ('Error message appear', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Success checkmark', '--ease-out', '--dur-fast', 'stroke-dashoffset, opacity'),
    ('Submit spinner', 'linear', '600ms infinite', 'transform rotate'),
  ],
  css=[
    ('.ds-form', 'Root form container — flex column, gap 24px'),
    ('.ds-form-field', 'Single field wrapper — flex column, gap 6px'),
    ('.ds-form-label', 'Field label — 13px 600'),
    ('.ds-form-hint', 'Helper text below input — 12px text3'),
    ('.ds-form-error', 'Validation error — 12px negative color'),
    ('.ds-form-section', 'Grouped fields with a section title'),
    ('.ds-form-actions', 'Submit/cancel button row'),
  ],
  react=[
    ('onSubmit', '(data: FormData) => void', 'required', 'Submit handler'),
    ('defaultValues', 'Record<string, unknown>', 'undefined', 'Initial field values'),
    ('resolver', 'Resolver', 'undefined', 'Validation schema (zod, yup)'),
    ('disabled', 'boolean', 'false', 'Disable all fields'),
    ('children', 'ReactNode', 'required', 'Form fields and actions'),
  ],
),

'genre-tiles': dict(
  figma_cat='Components', figma_name='Genre Tile',
  use=[
    'Genre selection in onboarding preference screens',
    'Genre navigation on the discovery/browse home screen',
    'Platform selection (Mobile, Web, TV) in onboarding',
    'Category quick-links in rail headers',
  ],
  dont=[
    'Filter chips (for filtering content, not navigation) — use Chip instead',
    'More than 12 tiles in a single screen without scrolling',
    'Text-only without icon/illustration — tiles need a visual anchor',
  ],
  motion=[
    ('Select toggle', '--ease-out', '--dur-fast', 'border-color, background, transform scale(1.04)'),
    ('Deselect', '--ease-out', '--dur-fast', 'border-color, background'),
    ('Press', '--ease-out', '80ms', 'transform scale(0.95)'),
    ('TV focus', '--ease-out', '--dur-fast', 'transform scale(1.1), box-shadow'),
    ('Appear (staggered)', '--ease-out', '--dur-fast', 'opacity, transform translateY(8px → 0)'),
  ],
  css=[
    ('.ds-genre-tile', 'Root — square tile, surface-1, border-subtle, r4'),
    ('.ds-genre-tile--selected', 'Green border, jio-soft bg, green icon'),
    ('.ds-genre-tile__icon', '32px icon or illustration'),
    ('.ds-genre-tile__label', '12px 700 text, centered below icon'),
    ('.ds-genre-tile--sm', 'Small variant — 72×72px'),
    ('.ds-genre-tile--md', 'Default — 96×96px'),
    ('.ds-genre-tile--lg', 'Large — 120×120px'),
  ],
  react=[
    ('label', 'string', 'required', 'Genre name displayed below icon'),
    ('icon', 'ReactNode', 'required', 'Icon or illustration'),
    ('selected', 'boolean', 'false', 'Active/selected state'),
    ('onSelect', '() => void', 'undefined', 'Toggle handler'),
    ('size', '"sm" | "md" | "lg"', '"md"', 'Tile size preset'),
    ('disabled', 'boolean', 'false', 'Disable interaction'),
  ],
),

'hover-card': dict(
  figma_cat='Overlays', figma_name='Hover Card',
  use=[
    'Rich game previews on hover over a game title or thumbnail',
    'User profile previews on hover over avatars in leaderboards',
    'Extended metadata tooltips for data table cells',
    'Preview cards for link text in editorial content',
  ],
  dont=[
    'Mobile — hover doesn\'t exist; use a tap-triggered Popover instead',
    'Critical information that shouldn\'t be hidden behind hover',
    'Auto-playing video or heavy media inside the card',
    'Forms or interactive controls inside the hover card',
  ],
  motion=[
    ('Open (delay 300ms)', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Close', '--ease-in', '--dur-fast', 'opacity'),
    ('Image load', '--ease-out', '--dur-base', 'opacity'),
  ],
  css=[
    ('.ds-hover-card', 'Root floating panel — surface-2, r4, max-w 320px'),
    ('.ds-hover-card__thumbnail', 'Game screenshot or avatar image area'),
    ('.ds-hover-card__body', 'Text content — padding 12px'),
    ('.ds-hover-card__title', '14px 700 text'),
    ('.ds-hover-card__meta', '12px text3 secondary info'),
  ],
  react=[
    ('trigger', 'ReactNode', 'required', 'Element that triggers the card on hover'),
    ('openDelay', 'number', '300', 'Delay in ms before opening'),
    ('closeDelay', 'number', '100', 'Delay in ms before closing'),
    ('align', '"start" | "center" | "end"', '"center"', 'Horizontal alignment'),
    ('side', '"top" | "bottom" | "left" | "right"', '"bottom"', 'Preferred side'),
    ('children', 'ReactNode', 'required', 'Card content'),
  ],
),

# ── BATCH 6 ────────────────────────────────────────────────────────────────────

'icons': dict(
  figma_cat='Foundations', figma_name='Icon',
  use=[
    'Communicating actions and states without relying solely on text',
    'Leading icons in buttons, inputs, and navigation items',
    'Status indicators in list items and toasts',
    'Decorative supporting visuals alongside text headings',
  ],
  dont=[
    'Icons alone without labels for ambiguous actions — always pair with accessible text',
    'Mixing icon styles (outline vs filled) within one UI surface',
    'Custom-coloured icons outside the token system — use currentColor',
    'Icons smaller than 16px — readability breaks below this size',
  ],
  motion=[
    ('Loading spinner', 'linear', '600ms infinite', 'transform rotate(360deg)'),
    ('Appear', '--ease-out', '--dur-fast', 'opacity, transform scale(0.8 → 1)'),
    ('State change (e.g. mute toggle)', '--ease-out', '--dur-fast', 'opacity crossfade'),
  ],
  css=[
    ('.ds-icon', 'Wrapper — inline-flex, currentColor fill'),
    ('.ds-icon--16', '16×16px'),
    ('.ds-icon--20', '20×20px (default)'),
    ('.ds-icon--24', '24×24px'),
    ('.ds-icon--32', '32×32px'),
    ('.ds-icon--spin', 'Rotation animation for loading states'),
  ],
  react=[
    ('name', 'IconName', 'required', 'Icon identifier from the sprite (e.g. "ic_play_fill")'),
    ('size', '16 | 20 | 24 | 32', '20', 'Width and height in px'),
    ('color', 'string', 'currentColor', 'Fill color — use CSS token or "currentColor"'),
    ('aria-label', 'string', 'undefined', 'Accessible label for non-decorative icons'),
    ('aria-hidden', 'boolean', 'true', 'Hide from screen readers when decorative'),
  ],
),

'inputs': dict(
  figma_cat='Forms', figma_name='Input',
  use=[
    'Single-line text entry: search, username, email, OTP',
    'Numeric entry: PIN, age, quantity',
    'Password fields with show/hide toggle',
    'Any field that needs a label, hint text, and error state',
  ],
  dont=[
    'Multi-line text — use Textarea instead',
    'Structured selections (dates, options) — use DatePicker or Select',
    'Search bars in the AppBar — use the AppBar search pattern',
    'Inputs without visible labels (placeholder-only) — accessibility violation',
  ],
  motion=[
    ('Focus ring', 'instant', '0ms', 'outline (2px jio-green)'),
    ('Error shake', '--ease-out', '400ms', 'transform translateX keyframes'),
    ('Error message slide in', '--ease-out', '--dur-fast', 'opacity, max-height'),
    ('Clear button appear', '--ease-out', '--dur-fast', 'opacity'),
    ('Password toggle', '--ease-out', '--dur-fast', 'opacity crossfade'),
  ],
  css=[
    ('.ds-input', 'Root input element — 48px height, surface-1, border-subtle, r3'),
    ('.ds-input:focus', 'Green outline, border-color: jio'),
    ('.ds-input--error', 'Red border and error message below'),
    ('.ds-input--disabled', '38% opacity, no pointer events'),
    ('.ds-input-wrapper', 'Container for leading/trailing icon slots'),
    ('.ds-input__leading', 'Leading icon or prefix text'),
    ('.ds-input__trailing', 'Trailing icon, clear button, or unit label'),
  ],
  react=[
    ('value', 'string', 'undefined', 'Controlled value'),
    ('onChange', '(e: ChangeEvent) => void', 'undefined', 'Change handler'),
    ('type', '"text" | "password" | "email" | "number" | "search"', '"text"', 'Input type'),
    ('placeholder', 'string', 'undefined', 'Placeholder text'),
    ('error', 'string | boolean', 'undefined', 'Error message or boolean error state'),
    ('hint', 'string', 'undefined', 'Helper text below field'),
    ('leading', 'ReactNode', 'undefined', 'Leading slot content'),
    ('trailing', 'ReactNode', 'undefined', 'Trailing slot content'),
    ('disabled', 'boolean', 'false', 'Disable the field'),
  ],
),

'label': dict(
  figma_cat='Forms', figma_name='Label',
  use=[
    'Field labels above or beside form controls',
    'Required field indicators (* suffix)',
    'Accessible association between a label and its input (htmlFor)',
    'Group labels for radio/checkbox sets',
  ],
  dont=[
    'Placeholder text as a substitute for a visible label — accessibility violation',
    'Decorative section headings — use an h2/h3 instead',
    'More than one line of label text — keep labels concise',
  ],
  motion=[
    ('Required asterisk pulse (error)', '--ease-out', '--dur-fast', 'color transition to red'),
  ],
  css=[
    ('.ds-label', 'Root — 13px 600, text color var(--text)'),
    ('.ds-label--required::after', 'Appends " *" in jio-green'),
    ('.ds-label--error', 'Red color for error-state labels'),
    ('.ds-label--disabled', 'text3 color, 38% opacity'),
  ],
  react=[
    ('htmlFor', 'string', 'required', 'ID of the associated form control'),
    ('required', 'boolean', 'false', 'Appends required asterisk'),
    ('disabled', 'boolean', 'false', 'Muted appearance when field is disabled'),
    ('children', 'ReactNode', 'required', 'Label text content'),
  ],
),

'lists': dict(
  figma_cat='Components', figma_name='List',
  use=[
    'Game library rows with thumbnail, title, and metadata',
    'Notification feed items',
    'Settings menu rows with icon, label, and trailing action',
    'Search result items',
  ],
  dont=[
    'Tabular data with multiple sortable columns — use Data Table',
    'Flat text-only bullet lists — use a plain ul/ol in prose',
    'Grid-layout game tiles — use Card in a grid',
    'More than 5 trailing actions per item — simplify the action model',
  ],
  motion=[
    ('Row hover', '--ease-out', '80ms', 'background'),
    ('Press/tap', '--ease-out', '60ms', 'transform scale(0.99), background'),
    ('Swipe to delete', '--ease-out', '--dur-base', 'transform translateX, opacity'),
    ('Item appear (stagger)', '--ease-out', '--dur-fast', 'opacity, transform translateY(8px → 0)'),
    ('Expand (nested list)', '--ease-out', '--dur-fast', 'max-height'),
  ],
  css=[
    ('.ds-list', 'Root list container — flex column'),
    ('.ds-list-item', 'Single row — flex, min-height 56px, padding 0 16px'),
    ('.ds-list-item__leading', 'Leading slot — icon, avatar, or thumbnail'),
    ('.ds-list-item__body', 'Text stack — flex column, flex:1'),
    ('.ds-list-item__title', '14px 600 text'),
    ('.ds-list-item__subtitle', '12px text3'),
    ('.ds-list-item__trailing', 'Trailing slot — chevron, badge, toggle'),
    ('.ds-list-item--destructive', 'Red title for delete actions'),
  ],
  react=[
    ('items', 'ListItem[]', 'required', 'Array of item data objects'),
    ('onItemPress', '(item: ListItem) => void', 'undefined', 'Tap/click handler'),
    ('leading', '(item: ListItem) => ReactNode', 'undefined', 'Leading slot renderer'),
    ('trailing', '(item: ListItem) => ReactNode', 'undefined', 'Trailing slot renderer'),
    ('divider', 'boolean', 'true', 'Show separator lines between items'),
  ],
),

'menubar': dict(
  figma_cat='Navigation', figma_name='Menubar',
  use=[
    'Desktop web app top menu (File, Edit, View style navigation)',
    'Admin dashboard primary navigation for complex tooling',
    'Web-only utility bars with grouped command menus',
  ],
  dont=[
    'Mobile — no space, use Tab Bar or Bottom Sheet actions instead',
    'Simple apps with fewer than 3 menu groups — a Toolbar suffices',
    'Replacing primary game navigation — menubar is a utility pattern',
  ],
  motion=[
    ('Menu open', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Menu close', '--ease-in', '--dur-fast', 'opacity'),
    ('Item hover', '--ease-out', '60ms', 'background'),
    ('Trigger active', '--ease-out', '80ms', 'background'),
  ],
  css=[
    ('.ds-menubar', 'Root bar — flex row, surface-1, border-bottom'),
    ('.ds-menubar__trigger', 'Menu title button — 36px height, px 10'),
    ('.ds-menubar__trigger--open', 'Active open state — glass-1 bg'),
    ('.ds-menubar__content', 'Dropdown panel — surface-2, r3, shadow'),
    ('.ds-menubar__item', 'Menu row — 36px, padding 0 10px'),
    ('.ds-menubar__item--disabled', '38% opacity'),
    ('.ds-menubar__separator', '1px border-subtle divider'),
    ('.ds-menubar__shortcut', 'Keyboard shortcut label — text3, monospace'),
  ],
  react=[
    ('items', 'MenubarMenu[]', 'required', 'Array of menu group definitions'),
    ('onSelect', '(value: string) => void', 'undefined', 'Item selection handler'),
  ],
),

# ── BATCH 7 ────────────────────────────────────────────────────────────────────

'navigation': dict(
  figma_cat='Navigation', figma_name='Navigation',
  use=[
    'Primary app-level navigation between 3-5 top-level screens',
    'Tab bar at the bottom on mobile (Home, Browse, Library, Profile)',
    'Side nav on web for persistent top-level wayfinding',
  ],
  dont=[
    'More than 5 top-level destinations — creates cognitive overload',
    'Secondary/contextual navigation — use tabs, segmented control, or breadcrumbs',
    'Navigation items without icon and label — icons alone are ambiguous',
  ],
  motion=[
    ('Tab switch', '--ease-out', '--dur-fast', 'indicator translateX'),
    ('Active indicator', '--ease-out', '--dur-fast', 'width, opacity'),
    ('Icon press', '--ease-out', '80ms', 'transform scale(0.88 → 1)'),
    ('Badge update', '--ease-out', '--dur-fast', 'transform scale(1.3 → 1)'),
    ('Tab bar hide (scroll)', '--ease-in', '--dur-base', 'transform translateY(100%)'),
    ('Tab bar show', '--ease-out', '--dur-base', 'transform translateY(0)'),
  ],
  css=[
    ('.ds-tab-bar', 'Root — fixed bottom, full width, surface-1, border-top'),
    ('.ds-tab-bar__item', 'Single tab — flex column, center, flex:1'),
    ('.ds-tab-bar__icon', '24px icon — text3 default, jio active'),
    ('.ds-tab-bar__label', '10px 700 — text3 default, jio active'),
    ('.ds-tab-bar__item--active', 'Active state — jio icon + label'),
    ('.ds-tab-bar__badge', 'Unread count badge over icon'),
  ],
  react=[
    ('items', 'NavItem[]', 'required', 'Tab definitions with icon, label, href'),
    ('activeItem', 'string', 'required', 'Active tab identifier'),
    ('onItemChange', '(id: string) => void', 'required', 'Tab switch handler'),
    ('badge', 'Record<string, number>', 'undefined', 'Badge counts keyed by item id'),
  ],
),

'navigation-menu': dict(
  figma_cat='Navigation', figma_name='Navigation Menu',
  use=[
    'Mega-nav on desktop web with expandable sub-sections',
    'Web app top navigation with hover-reveal sub-pages',
    'Breadcrumb-style wayfinding in multi-level content hierarchies',
  ],
  dont=[
    'Mobile primary navigation — use Tab Bar + Drawer',
    'Simple flat navigation with no sub-sections — use a standard menu/nav',
    'More than 3 levels of hierarchy — restructure information architecture',
  ],
  motion=[
    ('Sub-menu open', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Sub-menu close', '--ease-in', '--dur-fast', 'opacity'),
    ('Active indicator', '--ease-out', '--dur-fast', 'transform translateX, width'),
    ('Item hover', '--ease-out', '80ms', 'background'),
  ],
  css=[
    ('.ds-nav-menu', 'Root flex row container'),
    ('.ds-nav-menu__trigger', 'Top-level nav item with chevron'),
    ('.ds-nav-menu__content', 'Sub-menu panel — surface-2, r4, shadow'),
    ('.ds-nav-menu__item', 'Sub-menu row item'),
    ('.ds-nav-menu__link', 'Plain nav link without sub-menu'),
    ('.ds-nav-menu__indicator', 'Active underline indicator'),
  ],
  react=[
    ('items', 'NavMenuItem[]', 'required', 'Nav item tree with optional children'),
    ('value', 'string', 'undefined', 'Controlled open sub-menu identifier'),
    ('onValueChange', '(value: string) => void', 'undefined', 'Open state change handler'),
    ('orientation', '"horizontal" | "vertical"', '"horizontal"', 'Layout direction'),
  ],
),

'page-dots': dict(
  figma_cat='Components', figma_name='Page Dots',
  use=[
    'Carousel position indicator below a hero banner or feature carousel',
    'Onboarding step progress (slide 1 of 4)',
    'Image gallery position in game detail pages',
    'Walkthrough step indicators',
  ],
  dont=[
    'More than 8 steps — use a numbered step indicator instead',
    'Content hidden behind dots that users must see — provide swipe affordance',
    'As the sole navigation mechanism — pair with swipe gesture',
  ],
  motion=[
    ('Active dot expand', '--ease-out', '--dur-fast', 'width (6px → 18px), border-radius'),
    ('Inactive dot shrink', '--ease-out', '--dur-fast', 'width (18px → 6px)'),
    ('Dot transition on slide', '--ease-out', '--dur-base', 'transform translateX, opacity'),
  ],
  css=[
    ('.ds-page-dots', 'Root — flex row, gap 6px, center aligned'),
    ('.ds-page-dot', 'Single dot — 6px circle, text3 color'),
    ('.ds-page-dot--active', 'Active dot — 18px wide pill, jio-green'),
  ],
  react=[
    ('count', 'number', 'required', 'Total number of slides/pages'),
    ('active', 'number', 'required', 'Current active index (0-based)'),
    ('onDotClick', '(index: number) => void', 'undefined', 'Dot click handler for manual navigation'),
  ],
),

'pass-cards': dict(
  figma_cat='Components', figma_name='Pass Card',
  use=[
    'Pass subscription plan selection on upsell screens',
    'Pass status display in account/profile settings',
    'Comparison between Mobile Pass and Ultimate Pass tiers',
    'Renewal prompts on lapsed subscriber re-engagement screens',
  ],
  dont=[
    'Generic marketing cards unrelated to subscription plans',
    'More than 2 pass tiers side by side on mobile',
    'Showing pricing without clearly indicating the billing period',
  ],
  motion=[
    ('Card select', '--ease-out', '--dur-fast', 'border-color, box-shadow'),
    ('Recommended badge pulse', 'ease-in-out', '2s infinite', 'box-shadow scale'),
    ('Price reveal', '--ease-out', '--dur-base', 'opacity, transform translateY(8px → 0)'),
    ('CTA hover', '--ease-out', '--dur-fast', 'background, transform scale(1.02)'),
  ],
  css=[
    ('.ds-pass-card', 'Root — surface-1, border-subtle, r5, overflow hidden'),
    ('.ds-pass-card--mobile', 'Mobile Pass — jio-green accent header'),
    ('.ds-pass-card--ultimate', 'Ultimate Pass — gold/premium gradient header'),
    ('.ds-pass-card--selected', 'Selected state — jio border, jio-soft bg tint'),
    ('.ds-pass-card__header', 'Colored top section with pass name and icon'),
    ('.ds-pass-card__price', 'Large price display — 28px 700'),
    ('.ds-pass-card__features', 'Feature list — bullet items'),
    ('.ds-pass-card__cta', 'Subscribe button — full width, primary'),
  ],
  react=[
    ('tier', '"mobile" | "ultimate"', 'required', 'Pass tier'),
    ('price', 'string', 'required', 'Formatted price string (e.g. "₹299/mo")'),
    ('features', 'string[]', 'required', 'Feature bullet points'),
    ('selected', 'boolean', 'false', 'Highlighted/chosen state'),
    ('onSelect', '() => void', 'undefined', 'Selection handler'),
    ('recommended', 'boolean', 'false', 'Show "Recommended" badge'),
    ('ctaLabel', 'string', '"Subscribe"', 'CTA button text'),
    ('onCta', '() => void', 'undefined', 'CTA button handler'),
  ],
),

'popover': dict(
  figma_cat='Overlays', figma_name='Popover',
  use=[
    'Rich form controls floating near their trigger (color picker, tag editor)',
    'Contextual detail panels anchored to a button or icon',
    'Floating tip/callout for onboarding highlights',
    'Quick edit panels for inline data (rename, date edit)',
  ],
  dont=[
    'Simple single-line text tooltips — use Tooltip instead',
    'Full-screen overlays — use Dialog or Bottom Sheet',
    'Permanent UI that users will interact with frequently — embed it inline',
    'Mobile as a large overlay — use Bottom Sheet instead',
  ],
  motion=[
    ('Open', '--ease-out', '--dur-fast', 'opacity, transform scale(0.95 → 1) + translateY/X'),
    ('Close', '--ease-in', '--dur-fast', 'opacity'),
    ('Reposition (collision)', '--ease-out', '--dur-fast', 'transform'),
  ],
  css=[
    ('.ds-popover', 'Root floating panel — surface-2, r4, border-subtle, shadow'),
    ('.ds-popover__arrow', 'Directional arrow pointer'),
    ('.ds-popover__header', 'Optional title row with close button'),
    ('.ds-popover__body', 'Content area — padding 16px'),
  ],
  react=[
    ('open', 'boolean', 'undefined', 'Controlled open state'),
    ('onOpenChange', '(open: boolean) => void', 'undefined', 'Open state handler'),
    ('trigger', 'ReactNode', 'required', 'Element that opens the popover'),
    ('align', '"start" | "center" | "end"', '"center"', 'Alignment relative to trigger'),
    ('side', '"top" | "bottom" | "left" | "right"', '"bottom"', 'Preferred side'),
    ('sideOffset', 'number', '8', 'Gap between trigger and popover in px'),
    ('children', 'ReactNode', 'required', 'Popover content'),
  ],
),

# ── BATCH 8 ────────────────────────────────────────────────────────────────────

'progress-bar': dict(
  figma_cat='Feedback', figma_name='Progress Bar',
  use=[
    'Game download and install progress',
    'Achievement completion percentage on profile',
    'Level XP fill bar in user stats',
    'Multi-step form completion indicator',
  ],
  dont=[
    'Indeterminate loading (unknown duration) — use a Skeleton or spinner',
    'Binary complete/incomplete states — use a Checkbox or badge',
    'Values that change so rapidly users can\'t read them (realtime)',
  ],
  motion=[
    ('Fill advance', '--ease-out', '--dur-slow', 'width'),
    ('Complete flash', '--ease-out', '200ms', 'background → white → jio'),
    ('Appear', '--ease-out', '--dur-fast', 'opacity'),
    ('Indeterminate shimmer', 'linear', '1400ms infinite', 'background-position'),
  ],
  css=[
    ('.ds-progress', 'Root track — surface-2, r-pill, overflow hidden'),
    ('.ds-progress__fill', 'Filled portion — jio-green bg, height 100%'),
    ('.ds-progress--sm', '4px height'),
    ('.ds-progress--md', '8px height (default)'),
    ('.ds-progress--lg', '12px height'),
    ('.ds-progress--indeterminate', 'Animated shimmer — unknown duration'),
  ],
  react=[
    ('value', 'number', 'required', 'Current progress 0–100'),
    ('max', 'number', '100', 'Maximum value'),
    ('size', '"sm" | "md" | "lg"', '"md"', 'Track height preset'),
    ('indeterminate', 'boolean', 'false', 'Show shimmer animation instead of fill'),
    ('color', 'string', 'var(--jio)', 'Fill color — CSS token recommended'),
    ('label', 'string', 'undefined', 'Accessible aria-label for screen readers'),
  ],
),

'radio': dict(
  figma_cat='Forms', figma_name='Radio',
  use=[
    'Mutually exclusive option selection: pass tier, sort order, gender',
    'Settings screens where only one value is valid at a time',
    'Survey or quiz single-answer questions',
  ],
  dont=[
    'Independent toggleable options — use Checkbox instead',
    'Binary on/off — use Toggle/Switch instead',
    'More than ~8 options — use Select or Combobox instead',
  ],
  motion=[
    ('Select', '--ease-out', '--dur-fast', 'transform scale(0 → 1) inner dot, border-color'),
    ('Deselect', '--ease-out', '--dur-fast', 'transform scale(1 → 0) inner dot'),
    ('Focus ring', 'instant', '0ms', 'outline'),
    ('Hover', '--ease-out', '100ms', 'background of outer ring'),
  ],
  css=[
    ('.ds-radio-group', 'Root group container — flex column gap 12px'),
    ('.ds-radio', 'Single radio row — flex, align-items center, gap 10px'),
    ('.ds-radio__control', '20px circle — border-subtle, r-pill'),
    ('.ds-radio__control--checked', 'Green border + green inner dot 10px'),
    ('.ds-radio__label', '14px text2'),
    ('.ds-radio--disabled', '38% opacity, no pointer events'),
  ],
  react=[
    ('value', 'string', 'required', 'Controlled selected value'),
    ('onValueChange', '(v: string) => void', 'required', 'Change handler'),
    ('defaultValue', 'string', 'undefined', 'Uncontrolled initial value'),
    ('disabled', 'boolean', 'false', 'Disable all options'),
    ('orientation', '"vertical" | "horizontal"', '"vertical"', 'Layout direction'),
    ('children', 'ReactNode', 'required', 'RadioItem components'),
  ],
),

'rails': dict(
  figma_cat='Layout', figma_name='Rail',
  use=[
    'Horizontal scrolling game collections on the home screen',
    'Recommended, trending, and personalised content rows',
    'Genre or platform groupings within discovery',
    '"Jump back in" continue-playing rows',
  ],
  dont=[
    'Vertical stacked card lists — use a List or grid',
    'More than 30 items in a single rail — paginate or use a dedicated screen',
    'Rails without a title — users need context for why this content is grouped',
    'Mixing card sizes within a single rail',
  ],
  motion=[
    ('Scroll (momentum)', 'native', 'realtime', 'scroll-snap'),
    ('Card hover lift', '--ease-out', '--dur-fast', 'transform scale(1.03)'),
    ('TV focus scale', '--ease-out', '--dur-fast', 'transform scale(1.08)'),
    ('Rail appear (stagger)', '--ease-out', '--dur-fast', 'opacity, transform translateX(-16px → 0)'),
    ('Arrow button press', '--ease-out', '80ms', 'transform scale(0.92)'),
  ],
  css=[
    ('.ds-rail', 'Root — flex column, gap 12px'),
    ('.ds-rail__header', 'Title row — flex, space-between, align-items center'),
    ('.ds-rail__title', '16px 700 text'),
    ('.ds-rail__see-all', '13px jio-green link'),
    ('.ds-rail__track', 'Horizontal scroll container — flex row, gap 12px, overflow-x auto, scroll-snap'),
    ('.ds-rail__track::-webkit-scrollbar', 'Hidden scrollbar'),
  ],
  react=[
    ('title', 'string', 'required', 'Rail section heading'),
    ('seeAllHref', 'string', 'undefined', 'Link for "See all" button'),
    ('cardWidth', 'number', '160', 'Card width in px for scroll-snap sizing'),
    ('children', 'ReactNode', 'required', 'Card elements in the scroll track'),
    ('loading', 'boolean', 'false', 'Show skeleton placeholder cards'),
  ],
),

'resizable': dict(
  figma_cat='Layout', figma_name='Resizable',
  use=[
    'Split-pane layouts on desktop web (sidebar + main content)',
    'Code editor panels where users resize input/preview split',
    'Admin interfaces with adjustable column widths',
  ],
  dont=[
    'Mobile — no precise drag control on touch; use fixed layout or Bottom Sheet',
    'Layouts where minimum viable content width is critical — set sensible minSize',
    'More than 3 resizable panes in sequence — too complex to manage',
  ],
  motion=[
    ('Handle hover', '--ease-out', '--dur-fast', 'background, width (2px → 4px)'),
    ('Handle drag', 'none', 'realtime', 'panel width'),
    ('Collapse snap', '--ease-out', '--dur-fast', 'width to 0 or minSize'),
  ],
  css=[
    ('.ds-resizable', 'Root flex container'),
    ('.ds-resizable__panel', 'Individual pane — overflow auto'),
    ('.ds-resizable__handle', 'Drag handle — 4px wide, border-subtle bg'),
    ('.ds-resizable__handle:hover', 'Wider handle — jio-green tint'),
    ('.ds-resizable__handle--dragging', 'Active drag state — jio-green'),
  ],
  react=[
    ('direction', '"horizontal" | "vertical"', '"horizontal"', 'Split direction'),
    ('defaultLayout', 'number[]', '[50, 50]', 'Initial panel sizes as percentages'),
    ('minSize', 'number', '10', 'Minimum panel size as percentage'),
    ('onLayout', '(sizes: number[]) => void', 'undefined', 'Fired on drag end with new sizes'),
    ('children', 'ReactNode', 'required', 'ResizablePanel components'),
  ],
),

'scroll-area': dict(
  figma_cat='Layout', figma_name='Scroll Area',
  use=[
    'Overflow containers with custom-styled scrollbars',
    'Fixed-height panels with scrollable content (modals, sidebars, dropdowns)',
    'Chat message feeds and notification lists',
    'Code blocks and log viewers',
  ],
  dont=[
    'Full-page scroll — use native browser scroll instead',
    'Horizontal scroll areas on mobile — swipe conflicts with navigation',
    'Nested scroll areas in the same axis — scroll trap issues',
  ],
  motion=[
    ('Scrollbar appear', '--ease-out', '--dur-fast', 'opacity (visible on hover/scroll)'),
    ('Scrollbar hide', '--ease-in', '600ms delay', 'opacity → 0'),
    ('Scroll momentum', 'native', 'realtime', 'scrollTop/scrollLeft'),
  ],
  css=[
    ('.ds-scroll-area', 'Root — position relative, overflow hidden'),
    ('.ds-scroll-area__viewport', 'Scrollable inner — overflow scroll'),
    ('.ds-scroll-area__scrollbar', 'Custom scrollbar track — 8px wide'),
    ('.ds-scroll-area__thumb', 'Scrollbar thumb — r-pill, glass-2 bg'),
    ('.ds-scroll-area__corner', 'Bottom-right corner where axes meet'),
  ],
  react=[
    ('type', '"auto" | "always" | "scroll" | "hover"', '"hover"', 'When scrollbar is visible'),
    ('scrollHideDelay', 'number', '600', 'ms before scrollbar hides after scroll stops'),
    ('orientation', '"vertical" | "horizontal" | "both"', '"vertical"', 'Scroll axis'),
    ('children', 'ReactNode', 'required', 'Scrollable content'),
  ],
),

# ── BATCH 9 ────────────────────────────────────────────────────────────────────

'search': dict(
  figma_cat='Components', figma_name='Search',
  use=[
    'Global game search from the AppBar or dedicated search screen',
    'Filtering items in a list or data table',
    'Command palette input (inside the Command component)',
    'Genre/title search in the game library',
  ],
  dont=[
    'Full-text content search in articles/help docs — different UX pattern needed',
    'Search as the only navigation — pair with Browse/discovery',
    'Search input without a results state (empty, loading, no results)',
  ],
  motion=[
    ('Focus expand (mobile)', '--ease-out', '--dur-fast', 'width, opacity'),
    ('Clear button appear', '--ease-out', '--dur-fast', 'opacity, transform scale(0.8 → 1)'),
    ('Results appear', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Result item stagger', '--ease-out', '--dur-fast', 'opacity (30ms delay per item)'),
    ('Loading spinner', 'linear', '600ms infinite', 'transform rotate'),
  ],
  css=[
    ('.ds-search', 'Root — relative container'),
    ('.ds-search__input', 'Input field — leading search icon, trailing clear'),
    ('.ds-search__results', 'Dropdown results panel — surface-2, r4, shadow'),
    ('.ds-search__result-item', 'Single result row — 48px, thumbnail + title + meta'),
    ('.ds-search__empty', 'No results message — centered, text3'),
    ('.ds-search__loading', 'Loading spinner inside the input trailing area'),
  ],
  react=[
    ('value', 'string', 'undefined', 'Controlled input value'),
    ('onChange', '(v: string) => void', 'undefined', 'Input change handler'),
    ('results', 'SearchResult[]', 'undefined', 'Result items to display'),
    ('onResultSelect', '(result: SearchResult) => void', 'undefined', 'Result click handler'),
    ('loading', 'boolean', 'false', 'Show loading indicator'),
    ('placeholder', 'string', '"Search games…"', 'Input placeholder'),
    ('autoFocus', 'boolean', 'false', 'Focus input on mount'),
  ],
),

'select': dict(
  figma_cat='Forms', figma_name='Select',
  use=[
    'Controlled single option selection from a small set (sort by, language, country)',
    'Form fields where the option set is ≤15 items and searchability isn\'t needed',
    'Settings dropdowns: quality, region, notification frequency',
  ],
  dont=[
    'Large option sets (>15) — use Combobox with search',
    'Multi-select — use Combobox with multiple prop',
    'Binary choices — use Toggle or Radio',
    'Options that need description/preview — use a custom dropdown',
  ],
  motion=[
    ('Dropdown open', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
    ('Dropdown close', '--ease-in', '--dur-fast', 'opacity'),
    ('Option highlight', '--ease-out', '60ms', 'background'),
    ('Chevron rotate', '--ease-out', '--dur-fast', 'transform rotate(0 → 180deg)'),
  ],
  css=[
    ('.ds-select', 'Root trigger — 48px height, surface-1, border-subtle, r3'),
    ('.ds-select--open', 'Active/open state — jio border'),
    ('.ds-select--error', 'Error state — red border'),
    ('.ds-select--disabled', '38% opacity'),
    ('.ds-select__content', 'Dropdown panel — surface-2, r4'),
    ('.ds-select__item', 'Option row — 40px, padding 0 12px'),
    ('.ds-select__item--selected', 'Green checkmark + jio text'),
    ('.ds-select__item--focused', 'Keyboard-highlighted — glass-1 bg'),
  ],
  react=[
    ('value', 'string', 'undefined', 'Controlled selected value'),
    ('onValueChange', '(v: string) => void', 'undefined', 'Change handler'),
    ('defaultValue', 'string', 'undefined', 'Uncontrolled initial value'),
    ('placeholder', 'string', '"Select…"', 'Shown when no value selected'),
    ('disabled', 'boolean', 'false', 'Disable the control'),
    ('children', 'ReactNode', 'required', 'SelectItem components'),
  ],
),

'separator': dict(
  figma_cat='Layout', figma_name='Separator',
  use=[
    'Dividing related sections within a page or card',
    'Separating action groups in menus and toolbars',
    'Visual breaks between list item groups',
  ],
  dont=[
    'Overusing — every section does not need a separator',
    'Between items where whitespace alone is sufficient',
    'As a structural layout tool — use Grid or Flex instead',
  ],
  motion=[
    ('Appear', '--ease-out', '--dur-fast', 'opacity'),
  ],
  css=[
    ('.ds-separator', 'Root — 1px border-subtle, no border/bg on other sides'),
    ('.ds-separator--horizontal', 'Full width, height 1px (default)'),
    ('.ds-separator--vertical', 'Full height, width 1px'),
    ('.ds-separator--dashed', 'Dashed border style'),
  ],
  react=[
    ('orientation', '"horizontal" | "vertical"', '"horizontal"', 'Line direction'),
    ('decorative', 'boolean', 'true', 'If true, hidden from screen readers (aria-hidden)'),
    ('className', 'string', 'undefined', 'Additional classes'),
  ],
),

'skeleton': dict(
  figma_cat='Feedback', figma_name='Skeleton',
  use=[
    'Placeholder while content is loading — matches the shape of the final content',
    'Game rail cards during initial data fetch',
    'Profile header while user data loads',
    'List items before API response arrives',
  ],
  dont=[
    'Indefinite loading states with no timeout — add an error state',
    'Shapes that don\'t match the real content — creates layout shift on load',
    'Skeleton for content that loads in under 300ms — flash is worse than no skeleton',
    'Animated skeleton on TV — reduce motion preference must be respected',
  ],
  motion=[
    ('Shimmer sweep', 'linear', '1400ms infinite', 'background-position (gradient slide)'),
    ('Fade to content', '--ease-out', '--dur-base', 'opacity crossfade'),
  ],
  css=[
    ('.ds-skeleton', 'Root — surface-2 bg, border-radius matches target, overflow hidden'),
    ('.ds-skeleton--text', 'Text line shape — height 14px, r2, full width by default'),
    ('.ds-skeleton--circle', 'Circular — equal width/height, r-pill'),
    ('.ds-skeleton--card', 'Card-shaped — full width, fixed height'),
    ('.ds-skeleton--shimmer', 'Animated sweep overlay'),
  ],
  react=[
    ('variant', '"text" | "circle" | "card" | "custom"', '"text"', 'Shape preset'),
    ('width', 'number | string', '"100%"', 'Skeleton width'),
    ('height', 'number | string', '14', 'Skeleton height in px or CSS string'),
    ('count', 'number', '1', 'Number of skeleton lines to render'),
    ('animate', 'boolean', 'true', 'Enable shimmer animation'),
    ('borderRadius', 'string', 'undefined', 'Override border-radius'),
  ],
),

'slider': dict(
  figma_cat='Forms', figma_name='Slider',
  use=[
    'Volume, brightness, or game difficulty controls',
    'Price range filters in browse/shop screens',
    'Playback progress scrubber in media players',
    'Settings with continuous numeric range (not discrete steps)',
  ],
  dont=[
    'Precise numeric input — use Input[type=number] for exact values',
    'Binary choices — use Toggle instead',
    'More than 2 thumbs (multi-range) — too complex for most use cases',
    'Sliders for age or year selection — use Select or Combobox',
  ],
  motion=[
    ('Thumb drag', 'none', 'realtime', 'transform translateX'),
    ('Thumb press scale', '--ease-out', '80ms', 'transform scale(1.3)'),
    ('Track fill', 'none', 'realtime', 'width'),
    ('Focus ring', 'instant', '0ms', 'outline on thumb'),
    ('Value tooltip appear', '--ease-out', '--dur-fast', 'opacity, transform translateY(-4px → 0)'),
  ],
  css=[
    ('.ds-slider', 'Root — relative, full width, flex align-center'),
    ('.ds-slider__track', 'Background track — 4px height, surface-2, r-pill'),
    ('.ds-slider__fill', 'Filled portion — jio-green, same height as track'),
    ('.ds-slider__thumb', '20px circle — white bg, jio border, r-pill'),
    ('.ds-slider__thumb:focus', 'Green outline ring'),
    ('.ds-slider__thumb:hover', 'Scale 1.1, jio glow shadow'),
  ],
  react=[
    ('value', 'number[]', 'required', 'Controlled value(s) — array for range support'),
    ('onValueChange', '(v: number[]) => void', 'required', 'Real-time change handler'),
    ('onValueCommit', '(v: number[]) => void', 'undefined', 'Fired on drag end'),
    ('min', 'number', '0', 'Minimum value'),
    ('max', 'number', '100', 'Maximum value'),
    ('step', 'number', '1', 'Increment step size'),
    ('disabled', 'boolean', 'false', 'Disable interaction'),
  ],
),

# ── BATCH 10 ───────────────────────────────────────────────────────────────────

'tab-bar': dict(
  figma_cat='Navigation', figma_name='Tab Bar',
  use=[
    'Primary bottom navigation on mobile: Home, Browse, Library, Profile',
    '3-5 top-level destinations that users switch between frequently',
    'Persistent navigation visible on every main screen',
  ],
  dont=[
    'More than 5 items — visual crowding, use Drawer overflow',
    'Secondary in-page navigation within a screen — use Tabs component',
    'Navigation items that are rarely used — move to Profile/Settings',
    'Hiding the tab bar on scroll for content that needs navigation',
  ],
  motion=[
    ('Active indicator slide', '--ease-out', '--dur-fast', 'transform translateX'),
    ('Icon press bounce', '--ease-out', '--dur-fast', 'transform scale(0.85 → 1.1 → 1)'),
    ('Badge count pop', '--ease-out', '--dur-fast', 'transform scale(1.4 → 1)'),
    ('Tab bar hide', '--ease-in', '--dur-base', 'transform translateY(100%)'),
    ('Tab bar show', '--ease-out', '--dur-base', 'transform translateY(0)'),
  ],
  css=[
    ('.ds-tab-bar', 'Root — fixed bottom 0, full width, 56px height, surface-1, border-top'),
    ('.ds-tab-bar__item', 'Single tab — flex column, center, flex:1, gap 3px'),
    ('.ds-tab-bar__icon', '24px SVG — text3 inactive, jio active'),
    ('.ds-tab-bar__label', '10px 700 — text3 inactive, jio active'),
    ('.ds-tab-bar__item--active', 'Active state — jio icon and label'),
    ('.ds-tab-bar__badge', 'Count badge — position absolute, top-right of icon'),
  ],
  react=[
    ('items', 'TabItem[]', 'required', 'Tab definitions: id, label, icon, badge'),
    ('active', 'string', 'required', 'Active tab id'),
    ('onChange', '(id: string) => void', 'required', 'Tab switch handler'),
    ('hideOnScroll', 'boolean', 'false', 'Hide bar when scrolling down, show on up'),
  ],
),

'tabs': dict(
  figma_cat='Navigation', figma_name='Tabs',
  use=[
    'In-page content organisation: Overview / Gameplay / Reviews tabs on game detail',
    'Filter views on the library screen (All / Installed / Wishlist)',
    'Settings categories within a screen',
    'Segmented views where content is different but related',
  ],
  dont=[
    'Primary app navigation — use Tab Bar instead',
    'More than 6 tabs on mobile — horizontal scroll becomes confusing',
    'Tabs where content on different tabs is mostly identical',
    'Tab panels that contain navigation to other screens — tabs are in-page only',
  ],
  motion=[
    ('Active indicator slide', '--ease-out', '--dur-fast', 'transform translateX'),
    ('Panel crossfade', '--ease-out', '--dur-fast', 'opacity'),
    ('Pressed tab scale', '--ease-out', '80ms', 'transform scale(0.95)'),
  ],
  css=[
    ('.ds-tabs', 'Root container — flex column'),
    ('.ds-tabs__list', 'Tab button row — flex, border-bottom'),
    ('.ds-tabs__trigger', 'Single tab button — 40px height, 13px 700'),
    ('.ds-tabs__trigger--active', 'Active tab — jio text, jio indicator underline'),
    ('.ds-tabs__indicator', 'Sliding underline — 2px jio-green, position absolute bottom'),
    ('.ds-tabs__content', 'Panel area — shown when tab active'),
  ],
  react=[
    ('value', 'string', 'required', 'Controlled active tab'),
    ('onValueChange', '(v: string) => void', 'required', 'Tab change handler'),
    ('defaultValue', 'string', 'undefined', 'Uncontrolled initial active tab'),
    ('orientation', '"horizontal" | "vertical"', '"horizontal"', 'Tab list direction'),
    ('children', 'ReactNode', 'required', 'TabsList and TabsContent components'),
  ],
),

'textarea': dict(
  figma_cat='Forms', figma_name='Textarea',
  use=[
    'Multi-line text input: reviews, feedback, bio, description fields',
    'Support request forms where users describe an issue',
    'Game description or notes fields with long content',
  ],
  dont=[
    'Single-line text — use Input instead',
    'Rich text editing — use a dedicated rich text editor',
    'Code input — use a code editor component',
    'Fixed-height textareas that can\'t grow with content',
  ],
  motion=[
    ('Focus ring', 'instant', '0ms', 'outline'),
    ('Auto-resize height', '--ease-out', '--dur-fast', 'height'),
    ('Character count color shift', '--ease-out', '--dur-fast', 'color (text3 → amber → red)'),
    ('Error message appear', '--ease-out', '--dur-fast', 'opacity, max-height'),
  ],
  css=[
    ('.ds-textarea', 'Root textarea — surface-1, border-subtle, r3, padding 12px 14px'),
    ('.ds-textarea:focus', 'Jio-green outline + border'),
    ('.ds-textarea--error', 'Red border, error message below'),
    ('.ds-textarea--disabled', '38% opacity, resize none'),
    ('.ds-textarea__counter', 'Character count — 12px text3, text-right below'),
  ],
  react=[
    ('value', 'string', 'undefined', 'Controlled value'),
    ('onChange', '(e: ChangeEvent) => void', 'undefined', 'Change handler'),
    ('rows', 'number', '3', 'Initial visible row count'),
    ('maxLength', 'number', 'undefined', 'Max character count — shows counter'),
    ('autoResize', 'boolean', 'true', 'Grow height to fit content'),
    ('error', 'string | boolean', 'undefined', 'Error message or boolean'),
    ('disabled', 'boolean', 'false', 'Disable the field'),
  ],
),

'toast': dict(
  figma_cat='Feedback', figma_name='Toast',
  use=[
    'Brief feedback after a user action (game added to library, pass activated)',
    'Transient success/error confirmations that auto-dismiss',
    'Undo prompts immediately after a reversible action',
  ],
  dont=[
    'Persistent messages that require user action — use Banner',
    'Destructive confirmations — use Dialog',
    'More than one toast at a time — queue them',
    'Toasts that contain interactive forms or multi-step flows',
  ],
  motion=[
    ('Slide in (bottom)', '--ease-out', '--dur-fast', 'transform translateY(100% → 0), opacity'),
    ('Slide out', '--ease-in', '--dur-fast', 'transform translateY(0 → 100%), opacity'),
    ('Auto-dismiss progress', 'linear', '3000ms', 'width of progress indicator'),
    ('Stack expand (multiple)', '--ease-out', '--dur-fast', 'transform translateY, scale'),
  ],
  css=[
    ('.ds-toast', 'Root — surface-2, border-subtle, r4, padding 14px 16px, shadow'),
    ('.ds-toast--success', 'Green left border accent'),
    ('.ds-toast--error', 'Red left border accent'),
    ('.ds-toast--warning', 'Amber left border accent'),
    ('.ds-toast__icon', 'Leading status icon — 20px'),
    ('.ds-toast__body', 'Text content — flex column gap 2px'),
    ('.ds-toast__title', '14px 600 text'),
    ('.ds-toast__description', '13px text3'),
    ('.ds-toast__action', 'CTA link — jio-green text'),
    ('.ds-toast__close', 'Dismiss × button'),
  ],
  react=[
    ('variant', '"default" | "success" | "error" | "warning"', '"default"', 'Semantic color'),
    ('title', 'string', 'required', 'Toast headline'),
    ('description', 'string', 'undefined', 'Optional supporting text'),
    ('duration', 'number', '3000', 'Auto-dismiss delay in ms (Infinity = persistent)'),
    ('action', '{ label: string; onClick: () => void }', 'undefined', 'Undo/CTA button'),
    ('onDismiss', '() => void', 'undefined', 'Fired on close'),
  ],
),

'toggle': dict(
  figma_cat='Forms', figma_name='Toggle',
  use=[
    'Binary on/off settings: notifications, dark mode, auto-play',
    'Feature flags or preference switches in settings screens',
    'Enabling/disabling individual items in a list',
  ],
  dont=[
    'Multi-option selection — use Radio or Checkbox instead',
    'Actions with consequences that can\'t be undone — use Button + Dialog',
    'Toggles that require explanation longer than a short label',
    'Using toggle for navigation state — use Tabs instead',
  ],
  motion=[
    ('Thumb slide (off → on)', '--ease-out', '--dur-fast', 'transform translateX'),
    ('Track fill', '--ease-out', '--dur-fast', 'background (surface-2 → jio-green)'),
    ('Thumb scale (press)', '--ease-out', '80ms', 'transform scale(0.85)'),
    ('Focus ring', 'instant', '0ms', 'outline on track'),
    ('Disabled pulse', 'none', 'static', 'opacity 0.38'),
  ],
  css=[
    ('.ds-toggle', 'Root track — 44×24px, r-pill, surface-2, transition'),
    ('.ds-toggle--checked', 'Jio-green background'),
    ('.ds-toggle__thumb', '20×20px circle — white bg, r-pill, translateX on checked'),
    ('.ds-toggle--disabled', '38% opacity, no pointer events'),
    ('.ds-toggle-row', 'Label + toggle row — flex space-between'),
  ],
  react=[
    ('checked', 'boolean', 'required', 'Controlled on/off state'),
    ('onCheckedChange', '(v: boolean) => void', 'required', 'Change handler'),
    ('defaultChecked', 'boolean', 'false', 'Uncontrolled initial state'),
    ('disabled', 'boolean', 'false', 'Disable interaction'),
    ('size', '"sm" | "md"', '"md"', 'Track size preset (sm: 36×20px, md: 44×24px)'),
  ],
),

# ── BATCH 11 ───────────────────────────────────────────────────────────────────

'toggle-group': dict(
  figma_cat='Forms', figma_name='Toggle Group',
  use=[
    'Segmented controls: view mode (grid/list), sort direction (asc/desc)',
    'Platform filter selector (Mobile / Web / TV)',
    'Mutually exclusive visual style controls in a toolbar',
    'Rating or difficulty selectors with 3-5 options',
  ],
  dont=[
    'More than 5 items — wrapping breaks the segmented control pattern',
    'Options needing explanation longer than ~15 chars each',
    'Multi-select where any combination is valid — use Checkboxes instead',
    'Primary form fields — use Radio for form data',
  ],
  motion=[
    ('Active indicator slide', '--ease-out', '--dur-fast', 'transform translateX, width'),
    ('Item press', '--ease-out', '80ms', 'transform scale(0.95)'),
    ('Selection highlight', '--ease-out', '--dur-fast', 'background, color'),
  ],
  css=[
    ('.ds-toggle-group', 'Root — flex row, surface-1, border-subtle, r3, gap 0'),
    ('.ds-toggle-group__item', 'Single option — px 12, 36px height, 13px 600'),
    ('.ds-toggle-group__item--active', 'Active item — jio-soft bg, jio text, jio border'),
    ('.ds-toggle-group__item:not(:last-child)', 'Right border-subtle divider'),
    ('.ds-toggle-group--sm', 'Small variant — 28px height'),
  ],
  react=[
    ('type', '"single" | "multiple"', '"single"', 'Selection mode'),
    ('value', 'string | string[]', 'required', 'Controlled selected value(s)'),
    ('onValueChange', '(v: string | string[]) => void', 'required', 'Change handler'),
    ('disabled', 'boolean', 'false', 'Disable all items'),
    ('size', '"sm" | "md"', '"md"', 'Height preset'),
    ('children', 'ReactNode', 'required', 'ToggleGroupItem components'),
  ],
),

'tooltip': dict(
  figma_cat='Overlays', figma_name='Tooltip',
  use=[
    'Explaining icon-only buttons (no label) in toolbars',
    'Abbreviations or jargon that need contextual definition',
    'Additional context for truncated text',
    'Keyboard shortcut hints on desktop web',
  ],
  dont=[
    'Critical information — touch users may never see it',
    'Interactive content inside the tooltip — use Popover instead',
    'Long descriptions (>2 lines) — use Popover instead',
    'Tooltips on disabled elements — explain the reason inline instead',
  ],
  motion=[
    ('Open (300ms delay)', '--ease-out', '--dur-fast', 'opacity, transform scale(0.9 → 1)'),
    ('Close', '--ease-in', '100ms', 'opacity'),
  ],
  css=[
    ('.ds-tooltip', 'Root floating label — surface-2, r2, px 8, py 5'),
    ('.ds-tooltip__text', '12px 500 text — single line max'),
    ('.ds-tooltip__arrow', 'Directional pointer triangle'),
  ],
  react=[
    ('content', 'string | ReactNode', 'required', 'Tooltip text'),
    ('side', '"top" | "bottom" | "left" | "right"', '"top"', 'Preferred position'),
    ('sideOffset', 'number', '6', 'Gap from trigger in px'),
    ('delayDuration', 'number', '300', 'ms before tooltip opens'),
    ('asChild', 'boolean', 'false', 'Merge trigger props into child element'),
    ('children', 'ReactNode', 'required', 'Trigger element'),
  ],
),

'tv-focus': dict(
  figma_cat='TV', figma_name='TV Focus',
  use=[
    'Any interactive element on TV that must be navigable via D-pad/remote',
    'Game cards, buttons, and menu items that need a visible focus ring',
    'Spatial navigation grids and carousels on TV screens',
    'TV-specific focus state that scales with the TV layout grid',
  ],
  dont=[
    'Desktop or mobile — TV focus ring is for 10-foot UI only',
    'Overriding the ring color outside the jio-glow token',
    'Focus rings on non-interactive decorative elements',
    'Removing the focus ring for any reason on TV — required for accessibility',
  ],
  motion=[
    ('Focus ring appear', '--ease-out', '--dur-fast', 'box-shadow (0 → jio-glow)'),
    ('Focus scale', '--ease-out', '--dur-fast', 'transform scale(1.08)'),
    ('Focus ring pulse (selected)', 'ease-in-out', '1.5s infinite', 'box-shadow scale'),
    ('D-pad navigation', '--ease-out', '--dur-fast', 'focus transfer between elements'),
  ],
  css=[
    ('.ds-tv-focus', 'Focus ring wrapper — applies on :focus-visible'),
    ('.ds-tv-focus:focus-visible', 'box-shadow: 0 0 0 3px var(--jio), 0 0 24px rgba(0,168,89,.4)'),
    ('.ds-tv-focus--card', 'Card-specific focus — scale(1.08) + ring'),
    ('.ds-tv-focus--btn', 'Button-specific — scale(1.06) + ring'),
    ('.ds-tv-nav-grid', 'Spatial navigation container for D-pad focus'),
  ],
  react=[
    ('as', 'ElementType', '"div"', 'Root element type to render'),
    ('focusable', 'boolean', 'true', 'Adds tabIndex and focus ring'),
    ('onFocus', '() => void', 'undefined', 'Focus handler'),
    ('onBlur', '() => void', 'undefined', 'Blur handler'),
    ('onSelect', '() => void', 'undefined', 'Fired on Enter/OK remote press'),
    ('children', 'ReactNode', 'required', 'Focusable content'),
  ],
),

}

# ── Injection logic ────────────────────────────────────────────────────────────

def inject(comp_name, data, dry_run=False):
    path = os.path.join(BASE, comp_name, 'index.html')
    if not os.path.exists(path):
        return f'  SKIP  — file not found'

    html = open(path, encoding='utf-8').read()
    changes = []

    # 1. Figma chip — insert after last </span> inside .component-platforms div
    if 'component-figma-chip' not in html:
        chip = FIGMA_CHIP.format(category=data['figma_cat'], name=data['figma_name'])
        # find the closing tag of .component-platforms
        m = re.search(r'(</div>\s*)(</div>)', html)
        # More precise: find component-platforms block
        platforms_m = re.search(r'(<div[^>]*class="component-platforms"[^>]*>.*?</div>)', html, re.DOTALL)
        if platforms_m:
            old = platforms_m.group(0)
            new = old + '\n      ' + chip
            html = html.replace(old, new, 1)
            changes.append('figma-chip')

    # 2. when-to-use — insert before id="best-practices" or id="accessibility" or first ds-section
    if 'id="when-to-use"' not in html:
        section_html = make_when_to_use(data['use'], data['dont'])
        # try anchors in order
        anchors = [
            'id="best-practices"',
            'id="accessibility"',
            'id="code-examples"',
            'id="code"',
        ]
        inserted = False
        for anchor in anchors:
            idx = html.find(anchor)
            if idx != -1:
                # walk back to find the opening <section or <div tag
                section_start = html.rfind('\n  <', 0, idx)
                if section_start != -1:
                    html = html[:section_start] + section_html + html[section_start:]
                    changes.append('when-to-use')
                    inserted = True
                    break
        if not inserted:
            # prepend before </main>
            html = html.replace('</main>', section_html + '</main>', 1)
            changes.append('when-to-use')

    # 3. motion — insert before id="accessibility"
    if 'id="motion"' not in html:
        section_html = make_motion(data['motion'])
        anchors = ['id="accessibility"', 'id="code-examples"', 'id="code"']
        inserted = False
        for anchor in anchors:
            idx = html.find(anchor)
            if idx != -1:
                section_start = html.rfind('\n  <', 0, idx)
                if section_start != -1:
                    html = html[:section_start] + section_html + html[section_start:]
                    changes.append('motion')
                    inserted = True
                    break
        if not inserted:
            html = html.replace('</main>', section_html + '</main>', 1)
            changes.append('motion')

    # 4. api — insert before id="code-examples" or id="code"
    if 'id="api"' not in html:
        section_html = make_api(data['css'], data['react'])
        anchors = ['id="code-examples"', 'id="code"']
        inserted = False
        for anchor in anchors:
            idx = html.find(anchor)
            if idx != -1:
                section_start = html.rfind('\n  <', 0, idx)
                if section_start != -1:
                    html = html[:section_start] + section_html + html[section_start:]
                    changes.append('api')
                    inserted = True
                    break
        if not inserted:
            html = html.replace('</main>', section_html + '</main>', 1)
            changes.append('api')

    if not dry_run and changes:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        # sync to /tmp
        tmp_path = os.path.join(TMP, comp_name, 'index.html')
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        shutil.copy2(path, tmp_path)

    return ', '.join(changes) if changes else 'already complete'


# ── Main ───────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--all' in args:
        targets = list(COMPONENTS.keys())
    elif args:
        targets = args
    else:
        targets = list(COMPONENTS.keys())

    print(f"\n{'Component':<22} {'Injected'}")
    print('-' * 55)
    for name in targets:
        if name not in COMPONENTS:
            print(f"  {name:<20} NOT IN DATA — skipped")
            continue
        result = inject(name, COMPONENTS[name])
        print(f"  {name:<20} {result}")
    print()

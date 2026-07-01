# Resizable — JioGames DLS spec

> Source: `resizable/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Resizable

---

A panel or area that can be resized by dragging a handle. Used in the JioGames web app for split-panel layouts — game library (list) + game detail (preview).

Resizable · horizontal split · game list left · game detail right · handle highlighted green

The Resizable component wraps two or more panels with a draggable handle between them. Users drag the handle to allocate more screen space to the panel they need. It is a web-only pattern used in the JioGames admin and game library split view. On mobile, resizable panels are replaced by stacked full-width sections with standard navigation between them.

- **Horizontal split** — left/right panels divided by a vertical 6px handle; default orientation
- **Vertical split** — top/bottom panels divided by a horizontal 6px handle
- **Three panels** — two handles dividing three panels; only in advanced layout contexts
- **Collapsible** — double-click handle to collapse a panel to its minimum or snap to 50/50

- Always set a minimum panel size (min 20% or 200px) — never allow a panel to reach 0px
- Persist panel size proportions in localStorage so the user's preference survives page reload
- Highlight the handle green on hover so users discover it is draggable
- Support double-click on the handle to snap panels back to equal split
- Provide keyboard arrow key resizing (8px steps) for users who cannot use a pointer

- Use resizable panels on mobile — stack the panels vertically with navigation between them instead
- Allow panel sizes below 20% — content becomes unreadable and interaction targets too small
- Use more than two handles (three splits) unless the layout specifically requires it — adds complexity
- Change cursor from col-resize / row-resize during drag — unexpected cursor changes disorient users
- Animate panel resize — live resize must be immediate; animation adds latency and feels broken

1. 1 Panel Required Any content area. Overflows independently. Min-size enforced by JavaScript — CSS alone cannot prevent collapse to 0. Two or three panels per container. `overflow: auto; min-width: 20%`
2. 2 Drag handle Required 6px wide (horizontal split) or 6px tall (vertical split). Default color border-subtle, green on hover and while dragging. Grip dots via ::after pseudo-element. `width: 6px; cursor: col-resize; role="separator"`
3. 3 Second panel Required Grows or shrinks to fill remaining space. Uses flex:1. Different background from Panel A helps users visually distinguish the two areas. `flex: 1; overflow: auto`
4. 4 Container Required Outer flex container with fixed height. Clips overflow. Border and border-radius applied here, not on individual panels, for a unified appearance. `display: flex; overflow: hidden; border-radius: var(--r5)`

## Variants

Three split configurations — horizontal, vertical, and three-panel. Collapsible behavior applies to any variant.

## Sizes

Panel sizes are developer-defined percentages, not fixed tokens. The handle itself has a single fixed spec.

| Property | Value | Notes |
|---|---|---|
| Handle width (horizontal) | `6px` | Fixed — wide enough to click, narrow enough to not consume space |
| Handle height (vertical) | `6px` | Same spec, rotated orientation |
| Grip indicator | `2px × 24px` | ::after pseudo-element, 50% opacity |
| Panel minimum size | `20% / 200px` | Enforced by JS — use whichever is larger for the context |
| Panel maximum size | `80%` | Prevents the other panel from becoming unworkable |
| Default split | `50% / 50%` | On first render before localStorage preference is loaded |

## States

Handle states are the primary visual feedback for the resize interaction. Panel states are layout-level, not visual.

## Content guidance

- Each panel must be independently scrollable — never rely on page scroll for panel content
- Panels must handle narrow widths gracefully — use responsive layouts within panels
- Collapsed state (min size): show an icon-only sidebar, not a blank white panel
- Avoid fixed-width content (wide tables, non-responsive images) inside resizable panels

- Store panel sizes as percentages in localStorage keyed by layout ID
- Default 50/50 split on first render — do not assume one panel is "primary"
- Double-click handle resets to default 50/50 — document this affordance with a tooltip
- On window resize, recalculate panel sizes to maintain percentage ratios, not pixel values

## Platform considerations

- Not applicable — replace with full-width stacked panels
- Navigation between panels uses tab bar or back button, not a visible split
- Game list and game detail become separate screens linked by tap navigation

- Pointer drag on handle resizes panels in real time — no preview ghost
- Arrow keys (focus on handle): ← → resize horizontal, ↑ ↓ resize vertical in 8px steps
- Double-click snaps to 50/50 equal split
- Persist sizes in `localStorage` under a stable layout key
- Minimum viewport width for split layout: 768px — stack panels below this breakpoint

- Not applicable — no pointer available for dragging
- Fixed two-column layout with D-pad focus switching between panels
- Panel proportions are fixed at design time for TV layouts

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Drag handle | `role="separator"` | Separator with `aria-orientation="vertical"` (horizontal split) or `"horizontal"` (vertical split). |
| Size value | `aria-valuenow` | Percentage of the primary panel: `aria-valuenow="40"`. Update on every resize step. |
| Min / max | `aria-valuemin / aria-valuemax` | `aria-valuemin="20" aria-valuemax="80"` matching the enforced JS constraints. |
| Label | `aria-label` | "Resize panels" — describes the action the handle performs, not the visual appearance. |
| Keyboard | Arrow keys | Handle must be focusable (`tabindex="0"`). Arrow keys move in 8px steps; Shift+Arrow in 40px steps for power users. |
| Live region | `aria-live="polite"` | Optional: announce panel percentage after keyboard resize stops — "Left panel: 45%". Debounce to avoid over-announcing during drag. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--border-subtle` | `rgba(255,255,255,.08)` | Container border, handle idle fill color |
| `--jio` | `#00A859` | Handle hover and dragging fill color |
| `--surface-1` | — | Primary panel background (list/sidebar) |
| `--bg` | `#080a10` | Secondary panel background (detail/main content) |
| `--r5` | — | Container border-radius |
| `--pill` | `100px` | Grip indicator (::after) border-radius |
| `--dur-fast` | `120ms` | Handle background color transition on hover |

## When to use

Use when

- Split-pane layouts on desktop web (sidebar + main content)
- Code editor panels where users resize input/preview split
- Admin interfaces with adjustable column widths

Don't use when

- Mobile — no precise drag control on touch; use fixed layout or Bottom Sheet
- Layouts where minimum viable content width is critical — set sensible minSize
- More than 3 resizable panes in sequence — too complex to manage

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Handle hover | `--ease-out` | `--dur-fast` | background, width (2px → 4px) |
| Handle drag | `none` | `realtime` | panel width |
| Collapse snap | `--ease-out` | `--dur-fast` | width to 0 or minSize |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-resizable` | Root flex container |
| `.ds-resizable__panel` | Individual pane — overflow auto |
| `.ds-resizable__handle` | Drag handle — 4px wide, border-subtle bg |
| `.ds-resizable__handle:hover` | Wider handle — jio-green tint |
| `.ds-resizable__handle--dragging` | Active drag state — jio-green |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `direction` | "horizontal" | "vertical" | "horizontal" | Split direction |
| `defaultLayout` | number[] | [50, 50] | Initial panel sizes as percentages |
| `minSize` | number | 10 | Minimum panel size as percentage |
| `onLayout` | (sizes: number[]) => void | undefined | Fired on drag end with new sizes |
| `children` | ReactNode | required | ResizablePanel components |

## Code examples

````html
<div class="resizable-container">

  <div class="resizable-panel" id="panel-list" style="width:40%;">
    <!-- Game list content -->
  </div>

  <div
    class="resizable-handle"
    role="separator"
    aria-orientation="vertical"
    aria-label="Resize panels"
    aria-valuenow="40"
    aria-valuemin="20"
    aria-valuemax="80"
    tabindex="0"
  ></div>

  <div class="resizable-panel" id="panel-detail" style="flex:1;">
    <!-- Game detail content -->
  </div>

</div>

<script>
const handle = document.querySelector('.resizable-handle');
const panelLeft = document.getElementById('panel-list');
const container = document.querySelector('.resizable-container');
let isDragging = false;

handle.addEventListener('mousedown', () => {
  isDragging = true;
  handle.classList.add('is-dragging');
  document.body.style.cursor = 'col-resize';
  document.body.style.userSelect = 'none';
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  const rect = container.getBoundingClientRect();
  let pct = ((e.clientX - rect.left) / rect.width) * 100;
  pct = Math.min(80, Math.max(20, pct));
  panelLeft.style.width = pct + '%';
  handle.setAttribute('aria-valuenow', Math.round(pct));
  // Persist
  localStorage.setItem('panel-split', pct);
});

document.addEventListener('mouseup', () => {
  isDragging = false;
  handle.classList.remove('is-dragging');
  document.body.style.cursor = '';
  document.body.style.userSelect = '';
});

// Keyboard resize
handle.addEventListener('keydown', (e) => {
  const step = e.shiftKey ? 40 : 8;
  const rect = container.getBoundingClientRect();
  let pct = parseFloat(panelLeft.style.width);
  if (e.key === 'ArrowLeft') pct = Math.max(20, pct - (step / rect.width * 100));
  if (e.key === 'ArrowRight') pct = Math.min(80, pct + (step / rect.width * 100));
  panelLeft.style.width = pct + '%';
  handle.setAttribute('aria-valuenow', Math.round(pct));
});

// Restore persisted size
const saved = localStorage.getItem('panel-split');
if (saved) panelLeft.style.width = saved + '%';

// Double-click to reset 50/50
handle.addEventListener('dblclick', () => {
  panelLeft.style.width = '50%';
  handle.setAttribute('aria-valuenow', 50);
  localStorage.setItem('panel-split', 50);
});
</script>
````

````html
<div class="resizable-container resizable-container--vertical">

  <div class="resizable-panel" id="panel-top" style="height:55%; width:100%;">
    <!-- Top panel content -->
  </div>

  <div
    class="resizable-handle resizable-handle--horizontal"
    role="separator"
    aria-orientation="horizontal"
    aria-label="Resize panels"
    aria-valuenow="55"
    aria-valuemin="20"
    aria-valuemax="80"
    tabindex="0"
  ></div>

  <div class="resizable-panel" style="flex:1; width:100%;">
    <!-- Bottom panel content -->
  </div>

</div>
````

````html
<div class="resizable-container">

  <div class="resizable-panel" id="panel-a" style="width:25%;">
    <!-- Sidebar / filters -->
  </div>

  <div class="resizable-handle" role="separator" aria-orientation="vertical"
    aria-label="Resize sidebar and content"
    aria-valuenow="25" aria-valuemin="15" aria-valuemax="40"
    tabindex="0"></div>

  <div class="resizable-panel" id="panel-b" style="flex:1;">
    <!-- Main content -->
  </div>

  <div class="resizable-handle" role="separator" aria-orientation="vertical"
    aria-label="Resize content and detail"
    aria-valuenow="50" aria-valuemin="15" aria-valuemax="50"
    tabindex="0"></div>

  <div class="resizable-panel" id="panel-c" style="width:30%;">
    <!-- Detail / preview -->
  </div>

</div>
````

## Changelog

Initial draft. Horizontal, vertical, and three-panel variants. Full drag + keyboard resize JS example. ARIA separator pattern with aria-valuenow/min/max. localStorage persistence guidance. Web-only scope documented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text-inv`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

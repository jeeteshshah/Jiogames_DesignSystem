# Bottom Sheet — JioGames DLS spec

> Source: `bottom-sheet/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Bottom Sheet

---

An extended overlay panel that slides up from the bottom of the screen. Supports drag-to-dismiss, snap points, scrollable content, and a sticky footer.

## Variants

Four patterns cover the full range of contextual use cases. Each is interactive below.

### Basic

Fixed-height sheet with a list of actions. Single snap point. The most common variant — used for sharing, more options, and quick selections.

Fixed height. Action list of 2–6 items. Each row has an icon, label, and optional chevron. Tapping the scrim or swiping down dismisses.

````html
<div class="bottom-sheet" role="dialog" aria-modal="true" aria-labelledby="sheet-title">
  <div class="sheet-handle" aria-hidden="true"></div>
  <div class="sheet-header">
    <h2 id="sheet-title" class="sheet-title">Share game</h2>
  </div>
  <div class="sheet-body">
    <button class="sheet-action-row">
      <div class="sheet-action-icon"><!-- icon --></div>
      <span class="sheet-action-label">Share with friends</span>
    </button>
  </div>
</div>
````

### Scrollable content

Body scrolls independently while the header and footer stay fixed. Use for settings, filters, or any list that can exceed the sheet height.

The header and footer use `flex-shrink:0`. The body takes `flex:1;overflow-y:auto;min-height:0` to enable independent scroll while footer actions stay pinned and always reachable.

````css
.bottom-sheet {
  display: flex;
  flex-direction: column;
  height: var(--sheet-height, 55vh); /* or fixed px */
}
.sheet-header { flex-shrink: 0; }
.sheet-body   { flex: 1; overflow-y: auto; min-height: 0; }
.sheet-footer { flex-shrink: 0; }
````

### Snap points

Multi-height sheet that snaps between defined heights on drag. Supports peek (25%), half (55%), and full (92%). Click the buttons below to snap between heights.

Define snap heights as percentages of the frame. On release after drag, snap to nearest point based on position and velocity. Higher velocity snaps in direction of travel regardless of midpoint.

````
const snaps = ['25%', '55%', '92%']; // of viewport height
let current = 0;

function snapTo(index) {
  current = index;
  sheet.style.height = snaps[index];
  updateIndicators();
}

// On drag end — snap by velocity
function onDragEnd(velocity, position) {
  if (velocity > 0.5) snapTo(Math.max(0, current - 1));  // fast down = lower snap
  else if (velocity < -0.5) snapTo(Math.min(2, current + 1)); // fast up = higher snap
  else snapTo(nearestSnap(position));
}
````

### Responsive dialog

Renders as a centered dialog on wide viewports (≥768px) and as a bottom sheet on mobile. One component, two presentations. Useful for flows like plan selection or confirmation.

Same content, two presentations. On mobile, the sheet slides up from the bottom with a drag handle. On desktop, the same content renders as a centered dialog with a backdrop. Implement with a single component, switching class at the 768px breakpoint.

````css
.bottom-sheet {
  /* Mobile: bottom sheet */
  position: fixed; bottom: 0; left: 0; right: 0;
  border-radius: 20px 20px 0 0;
  transform: translateY(100%);
}

@media (min-width: 768px) {
  .bottom-sheet {
    /* Desktop: centered dialog */
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 480px; border-radius: 16px;
    bottom: auto; right: auto;
  }
}
````

### Confirmation — destructive action

Used for irreversible actions: delete save, cancel subscription, clear history. Two actions only — ghost Cancel and red Confirm. No scrollable body. Never auto-open.

Icon at top signals severity immediately. Title is a direct question (3–5 words). Description explains consequence in one sentence. Ghost Cancel on left, destructive Confirm on right. Use `role="alertdialog"` — screen readers announce it with higher urgency. Focus must land on Cancel (safest action) on open.

````html
<div class="bottom-sheet" role="alertdialog"
  aria-modal="true"
  aria-labelledby="confirm-title"
  aria-describedby="confirm-desc">

  <div class="sheet-handle"></div>

  <div class="sheet-body sheet-body--centered">
    <div class="confirm-icon confirm-icon--danger"><!-- icon --></div>
    <h2 id="confirm-title">Delete save?</h2>
    <p id="confirm-desc">This can't be undone.</p>
  </div>

  <div class="sheet-footer">
    <!-- autofocus Cancel, not Delete -->
    <button autofocus class="btn btn--ghost btn--m">Cancel</button>
    <button class="btn btn--danger btn--m">Delete save</button>
  </div>
</div>
````

### Rich media — game hero

Full-bleed hero at the top of the sheet, used for game previews and promotional drawers. Hero is fixed-height; content scrolls beneath it. The drag handle overlays the hero absolutely.

Hero is `flex-shrink:0`. A gradient fade at its bottom edge blends into `--surface-2`. Drag handle overlays the hero via `position:absolute;z-index:2`. Stats row uses 4-column flex for instant reference without scroll.

````css
.sheet-hero {
  flex-shrink: 0;
  height: 200px; /* ~40vw on 375px viewport */
  position: relative;
  overflow: hidden;
}
.sheet-hero img {
  width: 100%; height: 100%;
  object-fit: cover;
}
.sheet-hero-fade {
  /* blends hero into sheet surface */
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 72px;
  background: linear-gradient(transparent, var(--surface-2));
  pointer-events: none;
}
/* Handle sits on top of hero */
.sheet-handle { position: absolute; top: 0; left: 0; right: 0; z-index: 2; }
````

## Anatomy

The component hierarchy. Required parts must always be present. Optional parts enhance specific use cases.

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-bottom-sheet` | Root sheet — fixed bottom, full width |
| `.ds-bottom-sheet__handle` | 40×4px drag handle — centered top |
| `.ds-bottom-sheet__header` | Optional title row |
| `.ds-bottom-sheet__body` | Scrollable content area |
| `.ds-bottom-sheet__scrim` | Full-screen backdrop |
| `.ds-bottom-sheet--open` | Visible state — translateY(0) |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | required | Controls sheet visibility |
| `onClose` | () => void | required | Fired on scrim tap or swipe down |
| `snapPoints` | number[] | [0.5, 0.9] | Snap heights as fraction of viewport |
| `defaultSnap` | number | 0 | Index into snapPoints for initial open height |
| `title` | string | undefined | Optional header title |
| `children` | ReactNode | required | Sheet body content |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` first.

````
<!-- Overlay -->
<div class="sheet-overlay" aria-hidden="true"></div>

<!-- Sheet -->
<div
  class="bottom-sheet"
  role="dialog"
  aria-modal="true"
  aria-labelledby="sheet-title"
  aria-describedby="sheet-desc"
>
  <div class="sheet-handle" tabindex="0" aria-label="Drag to resize" aria-hidden="false"></div>

  <div class="sheet-header">
    <h2 id="sheet-title" class="sheet-title">Filter by genre</h2>
    <p id="sheet-desc" class="sheet-description">Select one or more genres</p>
  </div>

  <div class="sheet-body">
    <!-- Scrollable content -->
  </div>

  <div class="sheet-footer">
    <button class="btn btn--ghost btn--m" onclick="closeSheet()">Reset</button>
    <button class="btn btn--primary btn--m" onclick="applyFilters()">Apply</button>
  </div>
</div>
````

````
const sheet  = document.querySelector('.bottom-sheet');
const overlay = document.querySelector('.sheet-overlay');

function openSheet() {
  sheet.classList.add('is-open');
  overlay.classList.add('is-visible');
  document.body.style.overflow = 'hidden';
  sheet.focus();
}

function closeSheet() {
  sheet.classList.remove('is-open');
  overlay.classList.remove('is-visible');
  document.body.style.overflow = '';
  document.querySelector('[data-sheet-trigger]')?.focus(); // restore focus
}

overlay.addEventListener('click', closeSheet);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSheet(); });
sheet.querySelector('.sheet-handle').addEventListener('keydown', e => {
  if (e.key === 'Escape') closeSheet();
});
````

````css
.sheet-overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,.45);
  opacity: 0; pointer-events: none;
  transition: opacity var(--dur-pop) var(--ease-out);
  z-index: 100;
}
.sheet-overlay.is-visible { opacity: 1; pointer-events: auto; }

.bottom-sheet {
  position: fixed; bottom: 0; left: 0; right: 0;
  background: var(--surface-2);
  border-radius: 20px 20px 0 0;
  border-top: 1px solid var(--border);
  transform: translateY(100%);
  transition: transform var(--dur-enter) var(--ease-emphasized);
  display: flex; flex-direction: column;
  max-height: 90vh;
  z-index: 101;
  padding-bottom: env(safe-area-inset-bottom);
}
.bottom-sheet.is-open { transform: translateY(0); }

.sheet-handle {
  width: 40px; height: 4px;
  border-radius: 2px;
  background: rgba(255,255,255,.2);
  margin: 12px auto 4px;
  flex-shrink: 0;
}
.sheet-header { flex-shrink: 0; padding: 12px 20px 8px; }
.sheet-title  { font-size: 17px; font-weight: 700; color: var(--text); margin: 0; }
.sheet-description { font-size: 13px; color: var(--text2); margin: 4px 0 0; }
.sheet-body   { flex: 1; overflow-y: auto; min-height: 0; padding: 0 20px; }
.sheet-footer {
  flex-shrink: 0; display: flex; gap: 12px;
  padding: 12px 20px 16px;
  border-top: 1px solid var(--border-subtle);
}
````

## Tokens

Design tokens that control bottom sheet appearance. Override at the platform-specific layer.

| Token | Default | Usage |
|---|---|---|
| `--surface-2` | #16181f | Sheet container background |
| `--border` | rgba(255,255,255,.1) | Top border of sheet container |
| `--r7` | 20px | Top corner radius (border-radius: 20px 20px 0 0) |
| `--overlay-scrim` | rgba(0,0,0,.45) | Backdrop scrim color |
| `--ease-out` | cubic-bezier(0.32,0.72,0,1) | Entry and snap easing (vaul-style) |
| `--spring` | cubic-bezier(0.34,1.56,0.64,1) | Bounce easing for snap to higher height |
| `--dur-slow` | 320ms | Overlay fade duration |
| `--dur-sheet` | 420ms | Sheet slide-up / snap duration |
| `--dur-default` | 200ms | Dismiss (swipe-driven, ease-in) |

## When to use

Use when

- Contextual actions for a selected item (share, report, save)
- Multi-step flows that should not block the full screen
- Filters and sort options on list/grid screens
- Pass upsell panels that slide up over content

Don't use when

- Full app flows with many steps — use a dedicated screen
- Confirmation dialogs — use Dialog for destructive actions
- Content taller than 90vh without internal scrolling
- Nesting one bottom sheet inside another

## Do / Don't

- Use for actions related to the current context
- Include a drag handle on every sheet — always
- Use scrollable variant when content may overflow
- Pin footer actions so they're always reachable
- Dismiss on scrim tap, swipe down, or Escape
- Return focus to trigger element on close
- Add `env(safe-area-inset-bottom)` at bottom
- Use snap points for variable-length content

- Nest a sheet inside another sheet
- Use on TV — bottom is outside safe zone
- Use on desktop web — use side panel or dialog
- Auto-open without a user trigger
- Omit the drag handle — it signals draggability
- Use for primary navigation or wayfinding
- Put more than 6 items without scroll or snap
- Use generic titles like "Options" or "Menu"

## Platform guidance

- Primary pattern — use freely
- Touch drag with velocity-aware snap
- Snap heights: peek / half / full
- Corner radius 20px, handle 40×4px
- Safe area bottom padding required
- Background scales to 93% when sheet is open

- Avoid on desktop viewports ≥768px
- Switch to centered dialog at 768px+
- Drag-to-dismiss not available on pointer
- Escape key must always dismiss
- Tab cycles focus within sheet (trap)
- Click outside backdrop dismisses

- Do not use — pattern not supported
- Bottom of screen is outside TV safe zone
- Use full-screen overlay instead
- No touch gestures on TV
- D-pad cannot interact with bottom-anchored drawers
- Use focused panel or dialog for confirmations

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Half | 50vh default height | Context actions, filters | Mobile |
| Three-quarter | 75vh snap point | Rich content panels | Mobile |
| Full | 90vh snap point | Full-screen overlays | Mobile |

## States

Closed

Translated 100% off-screen; scrim hidden

Opening

Slides up with ease-out; scrim fades in simultaneously

Open

Resting at default snap point; draggable handle visible

Dragging

Follows finger position in real time; no animation

Snapping

Releases to nearest snap point with ease-out spring

Closing

Slides down; scrim fades out

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-base` | transform translateY(100% → 0) |
| Close (swipe/button) | `--ease-in` | `--dur-fast` | transform translateY(0 → 100%) |
| Scrim fade in | `--ease-out` | `--dur-base` | opacity |
| Snap expand | `--ease-out` | `--dur-base` | height |
| Handle drag | `none` | `realtime` | transform translateY |

## Gesture behavior

Touch-driven interaction model. All thresholds are minimum recommendations — tune for your content density.

### Drag thresholds

| Gesture | Threshold | Outcome |
|---|---|---|
| Slow drag down, release below 40% height | < 0.3 px/ms velocity | Snap to lower snap point or dismiss |
| Fast flick down | ≥ 0.5 px/ms velocity | Dismiss regardless of position |
| Fast flick up | ≥ 0.5 px/ms velocity | Snap to next higher snap point |
| Drag up past max height | > 92 vh | Rubber-band resist — spring back to max on release |
| Drag on scrollable body at top | scrollTop === 0 | Pass drag to sheet drag handler |
| Drag on scrollable body mid-scroll | scrollTop > 0 | Scroll the body; do not move the sheet |

### Overscroll & rubber-band

Overscroll up (past max)

Resist with `Math.pow(delta, 0.7)` (damped spring). Sheet follows finger at ~35% ratio. On release, snap back to max height with spring easing `cubic-bezier(.34,1.56,.64,1)`.

Overscroll down (dismiss zone)

Sheet follows finger 1:1. Scrim opacity tracks linearly: `opacity = 0.45 * (sheetY / dismissThreshold)`. Fast flick below 40% height → dismiss with `ease-in 200ms`.

### Scroll handoff

````
let startY = 0;
let isDraggingSheet = false;

body.addEventListener('touchstart', (e) => {
  startY = e.touches[0].clientY;
  isDraggingSheet = body.scrollTop === 0; // only drag if at top
});

body.addEventListener('touchmove', (e) => {
  const dy = e.touches[0].clientY - startY;
  if (isDraggingSheet && dy > 0) {
    e.preventDefault(); // stop body scroll — hand off to sheet
    moveSheet(dy);      // translate sheet with finger
  }
  // dy  {
  if (isDraggingSheet) snapOrDismiss(velocity);
});
````

## Content guidelines

Rules for titles, action labels, item count, and copy inside a bottom sheet.

Sheet title

✓ Do

- 2–5 words, action-noun ("Share game", "Filter by genre")
- Destructive: direct question ("Delete save?")
- Sentence case, no trailing punctuation

✕ Don't

- Generic labels: "Options", "Menu", "More"
- More than 6 words — wraps awkwardly
- Title Case For Every Word

Action labels

✓ Do

- Verb-first: "Apply filters", "Save settings"
- Destructive CTA echoes the action: "Delete save"
- 1–3 words per button label

✕ Don't

- "OK" / "Yes" / "No" — ambiguous after time passes
- More than 2 footer actions
- Two primary (green) buttons side-by-side

Action list — item count

| Count | Guidance |
|---|---|
| 2–4 | Ideal — fits in half-height sheet, no scroll |
| 5–6 | Acceptable — use scroll or expand to 75vh |
| 7+ | Reconsider — add search or move to a full screen |
| 1 | Use a Toast or inline action instead |

Descriptions & helper text

✓ Do

- Max 2 lines below the title (≈ 80 chars)
- State the consequence, not the mechanic
- Omit if the title is self-evident

✕ Don't

- Repeat the sheet title verbatim
- Marketing copy ("Unlock incredible features…")
- 3+ sentences — move to a dedicated screen

## JioGames app patterns

Five real bottom-sheet patterns from the JioGames app, rebuilt against the DLS foundation.

Pass purchase

Auto-renews automatically · Cancel anytime

Duration picker · accordions · sticky pay

Subscription renewal

Radio plan selector · UPGRADE badge · half-height

Connect store

Game art bg · feature bullets · privacy note · step chip

Set reminder

Minimal — date field · two actions · step chip

30-day access unlock

Dark green surface · amber warning · step chip

Pattern notes

Sheet surface variants

Standard sheets use `--surface-2`. Game-context sheets (unlock, connect) use `#0f1a12` — a dark green tint that visually connects to the JioGames brand while distinguishing game actions from system UI.

Step chip

The green step chip (S4, S5, S7…) signals position in a multi-step flow. Tapping it collapses back to the previous step. Always docked below the footer buttons, never inside the sheet scroll area. Uses `var(--jio)` background with black text for maximum contrast.

## Accessibility

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--dur-default`
- `--dur-enter`
- `--dur-fast`
- `--dur-pop`
- `--dur-sheet`
- `--dur-slow`
- `--ease-emphasized`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r3`
- `--r4`
- `--sheet-height`
- `--space-0-5`
- `--space-1`
- `--space-1-5`
- `--space-2`
- `--surface-1`
- `--surface-2`
- `--surface-3`
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

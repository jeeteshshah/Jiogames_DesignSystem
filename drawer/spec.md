# Drawer — JioGames DLS spec

> Source: `drawer/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Drawer

---

A panel that slides in from the left or right edge of the screen. Used for filters, contextual settings, and secondary navigation without leaving the current view.

Narrow your game library

Tomb Raider · Action Adventure

Click buttons to preview drawer directions

## Variants

Two directions cover all JioGames surfaces. Direction is determined by content type — filters from the left, contextual detail from the right.

## Anatomy

The drawer is a layered system: scrim catches dismissal taps, the panel slides over content, and the internal layout follows header → scrollable body → fixed footer.

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-drawer` | Root panel — fixed side, full height, surface-1 |
| `.ds-drawer--left` | Slides from left edge |
| `.ds-drawer--right` | Slides from right edge |
| `.ds-drawer__header` | Title row with close button |
| `.ds-drawer__body` | Scrollable content area |
| `.ds-drawer__scrim` | Full-screen backdrop |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | required | Controls drawer visibility |
| `onClose` | () => void | required | Close handler |
| `side` | "left" | "right" | "left" | Slide direction |
| `width` | number | string | 320 | Panel width in px or CSS string |
| `title` | string | undefined | Header title text |
| `children` | ReactNode | required | Drawer body content |

## Code

HTML structure. Open/close is driven by toggling `.is-open` on the panel and scrim.

````
<!-- Scrim -->
<div class="drawer-scrim" data-drawer-close></div>

<!-- Panel (left or right) -->
<aside class="drawer drawer--left" role="dialog"
       aria-modal="true" aria-label="Filters">

  <div class="drawer-header">
    <h2 class="drawer-title">Filters</h2>
    <button class="drawer-close" aria-label="Close filters">
      <svg><use href="#ic_close"></use></svg>
    </button>
  </div>

  <div class="drawer-body">
    <!-- Scrollable content -->
  </div>

  <div class="drawer-footer">
    <button class="btn btn--ghost">Reset</button>
    <button class="btn btn--primary">Apply</button>
  </div>
</aside>
````

````
/* Open state */
.drawer { transform: translateX(-100%); transition: transform var(--dur-slow) var(--ease-out); }
.drawer--right { transform: translateX(100%); }
.drawer.is-open { transform: translateX(0); }
.drawer-scrim { opacity: 0; pointer-events: none; transition: opacity 280ms; }
.drawer-scrim.is-open { opacity: 1; pointer-events: auto; }
````

## Tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | Panel background | Drawer panel bg |
| `--border-subtle` | Panel edge border | Left/right border of panel |
| `--ease-emphasized` | cubic-bezier(.32,.72,0,1) | Slide-in easing |
| `--dur-slow` | 320ms | Open transition |
| `--dur-pop` | 280ms | Scrim fade |
| 280px mobile / 360px web | Width | Panel width |
| rgba(0,0,0,.6) | Scrim | Backdrop overlay |

## Guidelines

- ·Use left drawer for global filters and faceted search
- ·Always provide a close button AND scrim tap to dismiss
- ·Keep footer actions sticky — never let them scroll away
- ·Trap focus inside the drawer while open
- ·Use `aria-modal="true"` on the panel

- ·Don't stack multiple drawers — use a single layer
- ·Don't open a drawer wider than 80% of the viewport
- ·Don't use for primary content — use a full page instead
- ·Don't skip the transition — abrupt appearance feels broken
- ·Don't confuse with Bottom Sheet — Drawer is always side

## When to use

Use when

- Side navigation panel on web/tablet (slides in from left)
- Settings panel on desktop that doesn't hide the main content entirely
- Filter panel on browse/discovery screens (slides from right)

Don't use when

- Mobile primary navigation — use Tab Bar instead
- Replacing Bottom Sheet on mobile — Drawer is a web/tablet pattern
- Content that should be always visible — use a sidebar layout

## Sizes

| Size | Token / Height | Use case | Platform |
|---|---|---|---|
| Narrow | 240px width | Nav / quick filter | Web |
| Default | 320px width | Standard side panel | Web |
| Wide | 480px width | Rich settings panel | Web |

## States

Closed

Off-screen at -100% translateX; scrim hidden

Opening

Slides in with ease-out; scrim fades in

Open

Fully visible; focus trapped inside drawer

Closing

Slides out with ease-in; scrim fades out

Scrolled

Header stays fixed; body scrolls independently

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open (left) | `--ease-out` | `--dur-base` | transform translateX(-100% → 0) |
| Open (right) | `--ease-out` | `--dur-base` | transform translateX(100% → 0) |
| Close | `--ease-in` | `--dur-fast` | transform translateX |
| Scrim fade | `--ease-out` | `--dur-base` | opacity |
| Content stagger | `--ease-out` | `--dur-fast` | opacity (items delayed 40ms each) |

## Platform rules

Mobile

- Not used on mobile — use Bottom Sheet instead
- Exception: full-screen nav drawer (hamburger menu) on mobile web

Web

- Left drawer: primary nav — persists or overlays on smaller screens
- Right drawer: filters, settings, detail panels
- Keyboard: Escape closes; focus trapped inside while open
- Overlay scrim on widths below 1024px; push layout on wider screens

TV

- Not used on TV — use a fullscreen overlay or focused side panel

## Accessibility

- ·Esc closes the drawer
- ·Tab cycles through focusable elements inside
- ·Focus returns to trigger on close

- ·`role="dialog"` on panel
- ·`aria-modal="true"` to trap screen reader
- ·`aria-label` or `aria-labelledby` for title

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--ctrl-h-ghost`
- `--ctrl-h-sm`
- `--dur-fast`
- `--dur-pop`
- `--dur-slow`
- `--ease-emphasized`
- `--ease-out`
- `--gold`
- `--jio`
- `--jio-font`
- `--pill`
- `--r2`
- `--r3`
- `--r4`
- `--surface-1`
- `--surface-2`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

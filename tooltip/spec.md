# Tooltip — JioGames DLS spec

> Source: `tooltip/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Tooltip

---

Short label that appears on hover or focus near an icon or truncated text. Confirms what a control does without adding persistent UI.

Tooltip directions · Top, Bottom, Left, Right

Tooltips are transient, non-interactive labels that appear on hover or keyboard focus. They name icon-only controls, expand truncated labels, and clarify ambiguous actions — without permanently occupying layout space. Because tooltips disappear on interaction, they must never be the sole source of essential information.

- **Icon labels** — names a control whose icon is not self-explanatory
- **Truncation reveal** — shows full text when a label is clipped
- **Shortcut hint** — surfaces keyboard shortcut alongside the action name
- **Clarifying metadata** — e.g. rating meaning, timestamp details

- Keep copy under 40 characters — one short clause, no full stop
- Describe the action: "Add to wishlist", not "Wishlist button"
- Use `role="tooltip"` and `aria-describedby` on the trigger
- Show on both hover and keyboard focus so keyboard users benefit equally
- On TV, show tooltip on D-pad focus; dismiss when focus moves away

- Put interactive content (links, buttons) inside a tooltip
- Use a tooltip as the only label — visible labels are always preferred
- Show tooltips on mobile — touch has no hover; use persistent labels instead
- Exceed 40 characters — use a popover for richer explanations
- Trigger tooltip on click — click should execute the action, not describe it

1. 1 Container Required Dark surface pill with border. Uses `--surface-4` so it contrasts on both dark and mid-tone backgrounds. `background: var(--surface-4); border-radius: var(--r3)`
2. 2 Label text Required 12px semibold, sentence case, max 40 chars. No punctuation at end. Describes the control action. `font-size: 12px; font-weight: 700`
3. 3 Caret arrow Required CSS border-triangle pointing at the trigger. Direction flips with `.tooltip--bottom`, `--left`, `--right`. `::after { border: 5px solid transparent }`
4. 4 Trigger element Optional The icon button, link, or truncated label that owns the tooltip. Must have `aria-describedby` pointing to the tooltip id. `aria-describedby="tooltip-id"`

## Variants

Direction variants control which side of the trigger the tooltip appears. Choose the direction that keeps the tooltip fully visible within its scroll container.

## Sizes

Three size tiers. Default covers most use cases. S fits dense icon toolbars. L improves legibility for accessibility-focused surfaces and TV.

## States

Tooltips have two visual states: hidden (opacity 0) and visible (opacity 1). Transition is fast — 100–150ms — so it does not feel laggy on rapid hover.

## Content guidance

Tooltip copy must be the shortest possible label that completes the user's understanding of the control.

- Max 40 characters — no punctuation at end
- Sentence case: "Add to wishlist" not "Add To Wishlist"
- Describe the action: "Add to wishlist", not "Wishlist button"
- For destructive actions add the word: "Remove from library"
- Keyboard shortcut format: "Play game ⌘P" (two spaces before shortcut)
- Never put full sentences or explanations in a tooltip — use a popover

- Icon-only button → tooltip (names the control)
- Truncated text → tooltip (reveals full value)
- Rich explanation needed → use Popover instead
- Persistent info needed → use inline label or caption
- Mobile surface → persistent label or bottom sheet, never tooltip
- Error message → use form validation component, not tooltip

## Platform considerations

Tooltip interaction model varies significantly across platforms. Do not ship a single implementation across all three without platform-specific handling.

- Touch has no hover — **do not use tooltips on mobile**
- Use a persistent label beneath icon buttons instead
- For overflow-truncated text, tap expands or opens detail sheet
- Long-press tooltips are non-standard — avoid
- If the only available pattern, use a bottom sheet with the full label

- Trigger on `mouseenter` and `focus`
- Dismiss on `mouseleave`, `blur`, and `Escape`
- No delay on show — instant appearance feels responsive
- Position with `position:absolute` inside a relative wrapper
- Ensure tooltip stays within viewport — flip direction if clipped

- Show on D-pad focus, dismiss when focus moves to another element
- Always use L size (14px) — default is unreadable at 3m
- Position below focused element — top is obscured by focus ring glow
- No hover trigger — remote control only navigates via focus
- Tooltip must clear the focused element's glow shadow (20px clearance)

## Accessibility

Tooltips must be reachable by keyboard and readable by screen readers. Never rely on tooltip alone to communicate critical information.

| Requirement | Implementation | Notes |
|---|---|---|
| ARIA role | `role="tooltip"` | Applied to the tooltip element, not the trigger. |
| Trigger linkage | `aria-describedby="tooltip-id"` | Trigger element points to tooltip id. Screen reader announces tooltip content after the control label. |
| Keyboard trigger | Focus (`:focus-within`) | Tooltip appears when trigger receives keyboard focus. Keyboard users must not miss tooltips. |
| Escape to dismiss | JS `keydown Escape` | WCAG 1.4.13 — content triggered by hover must be dismissible without moving pointer/focus. |
| Pointer hoverable | Tooltip persists while pointer is over it | WCAG 1.4.13 — user must be able to move pointer onto tooltip without it dismissing. |
| Color contrast | Min 4.5:1 text on background | `--text` on `--surface-4` passes at 7.2:1. |
| Not sole info source | Label or visible text required | If tooltip is the only label for a control, add a visually hidden `aria-label` to the trigger as fallback. |

## Related tokens

Use these tokens exclusively — never hardcode hex values for tooltip styles.

| Token | Value | Usage |
|---|---|---|
| `--surface-4` | `#2A3142` | Tooltip background fill |
| `--border-subtle` | `rgba(255,255,255,.08)` | Tooltip border stroke |
| `--text` | `#f4f2ee` | Tooltip label text color |
| `--r3` | `8px` | Tooltip container border-radius |
| `--dur-fast` | `120ms` | Tooltip fade-in/out transition duration |
| `--ease-out` | `cubic-bezier(.2,0,0,1)` | Tooltip opacity transition easing |

## When to use

Use when

- Explaining icon-only buttons (no label) in toolbars
- Abbreviations or jargon that need contextual definition
- Additional context for truncated text
- Keyboard shortcut hints on desktop web

Don't use when

- Critical information — touch users may never see it
- Interactive content inside the tooltip — use Popover instead
- Long descriptions (>2 lines) — use Popover instead
- Tooltips on disabled elements — explain the reason inline instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open (300ms delay) | `--ease-out` | `--dur-fast` | opacity, transform scale(0.9 → 1) |
| Close | `--ease-in` | `100ms` | opacity |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-tooltip` | Root floating label — surface-2, r2, px 8, py 5 |
| `.ds-tooltip__text` | 12px 500 text — single line max |
| `.ds-tooltip__arrow` | Directional pointer triangle |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `content` | string | ReactNode | required | Tooltip text |
| `side` | "top" | "bottom" | "left" | "right" | "top" | Preferred position |
| `sideOffset` | number | 6 | Gap from trigger in px |
| `delayDuration` | number | 300 | ms before tooltip opens |
| `asChild` | boolean | false | Merge trigger props into child element |
| `children` | ReactNode | required | Trigger element |

## Code examples

Copy these snippets as starting points. Tooltip visibility is CSS-only via `:hover` and `:focus-within` on the wrapper.

````html
<div class="tooltip-wrap">
  <button class="icon-btn" aria-describedby="tt-play">
    <svg ...></svg>
  </button>
  <span class="tooltip" id="tt-play" role="tooltip">Play game</span>
</div>

<style>
.tooltip-wrap { position: relative; display: inline-block; }
.tooltip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--surface-4);
  color: var(--text);
  font-size: 12px;
  font-weight: 700;
  padding: 5px 10px;
  border-radius: var(--r3);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--dur-fast) var(--ease-out);
  border: 1px solid var(--border-subtle);
}
.tooltip::after {
  content: '';
  position: absolute;
  top: 100%; left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: var(--surface-4);
}
.tooltip-wrap:hover .tooltip,
.tooltip-wrap:focus-within .tooltip { opacity: 1; }
</style>
````

````
<!-- Bottom -->
<span class="tooltip tooltip--bottom" role="tooltip">Share</span>

<!-- Left -->
<span class="tooltip tooltip--left" role="tooltip">Add to wishlist</span>

<!-- Right -->
<span class="tooltip tooltip--right" role="tooltip">More options</span>

<style>
.tooltip--bottom { bottom: auto; top: calc(100% + 8px); }
.tooltip--bottom::after { top: auto; bottom: 100%; border-top-color: transparent; border-bottom-color: var(--surface-4); }

.tooltip--left { bottom: auto; left: auto; right: calc(100% + 8px); top: 50%; transform: translateY(-50%); }
.tooltip--left::after { top: 50%; left: 100%; transform: translateY(-50%); border-top-color: transparent; border-left-color: var(--surface-4); }

.tooltip--right { bottom: auto; left: calc(100% + 8px); top: 50%; transform: translateY(-50%); }
.tooltip--right::after { top: 50%; right: 100%; left: auto; transform: translateY(-50%); border-top-color: transparent; border-right-color: var(--surface-4); }
</style>
````

````
<!-- JS: dismiss on Escape for WCAG 1.4.13 compliance -->
<script>
document.querySelectorAll('.tooltip-wrap').forEach(wrap => {
  wrap.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      wrap.querySelector('.tooltip').style.opacity = '0';
      wrap.querySelector('[aria-describedby]').blur();
    }
  });
});
</script>
````

## Changelog

Initial draft. CSS-only tooltip with four direction variants (top, bottom, left, right), three size tiers (S/M/L), and full accessibility table. Mobile: no tooltip guidance documented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--r3`
- `--surface-2`
- `--surface-4`
- `--text`
- `--touch-min`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

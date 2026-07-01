# Popover — JioGames DLS spec

> Source: `popover/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Popover

---

Small floating panel triggered by a button. Contains rich content — filters, options, extra info. Dismisses on outside click or Escape.

Popover with form controls · Platform filter

Popovers are floating panels that anchor to a trigger element and contain interactive content — filter checkboxes, short forms, option lists, or contextual information. Unlike tooltips (label only), popovers can hold multiple form controls, buttons, and structured text. They are non-modal: the rest of the page remains interactive while a popover is open.

- **Filters** — compact checkbox or toggle groups anchored to a filter button
- **Quick actions** — 2–4 action items without navigating away
- **Contextual info** — extended description or help text for a nearby control
- **Mini forms** — single-field input + submit, e.g. rename or add note

- Add a close button when the popover contains interactive controls
- Dismiss on outside click and Escape key — both must work
- Keep content to 3–4 items max — use a bottom sheet for longer lists
- Give trigger `aria-expanded` and `aria-haspopup="dialog"`
- Return focus to trigger when popover closes

- Use popover for a single line of text — a tooltip is sufficient
- Open more than one popover at a time — new trigger closes the previous
- Use modal-level blocking behavior — popover is non-modal
- Place destructive-only actions in a popover without confirmation step
- Use on mobile — replace with bottom sheet (full-width, touch-friendly)

1. 1 Container Required Elevated surface with border and shadow. `--surface-2` background, `--r5` radius, `0 8px 32px rgba(0,0,0,.5)` shadow. `background: var(--surface-2); border-radius: var(--r5)`
2. 2 Title Optional 14px bold label naming the popover's purpose. Required if content alone is ambiguous. Omit for simple option lists. `font-size: 14px; font-weight: 700`
3. 3 Content slot Required Free slot for checkboxes, radios, text, or a mini form. Max 4 items before needing a bottom sheet. `padding: var(--space-2)`
4. 4 Action / close Optional Primary CTA (Apply, Save) or a close ✕ button in the top-right. Required when content has a form or multi-step interaction. `position: absolute; top: 10px; right: 10px`

## Variants

Four popover variants cover the full range of use cases from simple text to interactive forms.

This game requires JioGames Pass to access all levels.

Rated by 4,218 players. Score is the average of all ratings in the last 30 days.

## Sizes

Popover width is governed by content but constrained to three tiers. Height is always content-driven — never fixed.

| Size | min-width | Use case |
|---|---|---|
| S | `180px` | 2–3 short option items, minimal text |
| M (default) | `240px` | Filter panels, help text, short forms |
| L | `320px` | Multi-field forms, richer content blocks |

## States

Popovers toggle between closed and open. The open state has two sub-states: with content and loading (skeleton).

## Content guidance

Popovers sit between tooltips (label only) and bottom sheets (full content) in the overlay hierarchy.

- Tooltip = label only, no interaction, hover-triggered
- Popover = interactive content, click-triggered
- If content is a single sentence with no buttons → tooltip
- If content has a checkbox, button, or form → popover
- If content exceeds 4 items → bottom sheet (mobile) or drawer (web)

- Title: 2–4 words, sentence case, no verb ("Platform", not "Select platform")
- Body text: max 2 lines, 13px, muted color
- CTA labels: verb-first ("Apply filters", "Save", "Done")
- Close button: always ✕ icon only with `aria-label="Close"`
- Never put navigation links inside a popover

## Platform considerations

- Replace with bottom sheet — popovers are too small for touch targets
- Bottom sheet slides up from bottom edge, full viewport width
- Drag handle at top, close button in header
- Never use an absolute-positioned popover on a touch surface

- Anchor below trigger by default; flip upward if near bottom viewport edge
- Dismiss on `click outside` and `Escape`
- Focus first interactive element on open
- Max-width 320px — wider content needs a modal or drawer

- Replace with full-screen panel — popovers are too small at TV scale
- D-pad navigates items in the panel, Back button closes
- Focus ring must be clearly visible on each option (3px glow)
- Always show a visible "Close" action as the last item

## Accessibility

| Requirement | Implementation | Notes |
|---|---|---|
| ARIA role | `role="dialog"` | Applied to the popover container element. |
| Non-modal | `aria-modal="false"` | Popover is not modal — page content remains accessible to AT. |
| Trigger state | `aria-expanded` + `aria-haspopup="dialog"` | Toggle `aria-expanded` true/false with open/close. Screen readers announce the state change. |
| Focus management | Focus first interactive element on open | Return focus to trigger on close. Do not trap focus (non-modal). |
| Keyboard dismiss | `Escape` closes | Required. Also dismiss on click outside. |
| Accessible name | `aria-labelledby` pointing to title | If no visible title, use `aria-label` on the dialog element. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--surface-2` | `#161B26` | Popover background |
| `--border-subtle` | `rgba(255,255,255,.08)` | Popover border |
| `--r5` | `16px` | Popover border-radius |
| `--r2` | `4px` | Close button border-radius |
| `--glass-1` | `rgba(255,255,255,.04)` | Close button hover background |
| `--space-2` | `16px` | Popover internal padding |
| `--jio` | `#00A859` | Apply button background, checkbox accent |

## When to use

Use when

- Rich form controls floating near their trigger (color picker, tag editor)
- Contextual detail panels anchored to a button or icon
- Floating tip/callout for onboarding highlights
- Quick edit panels for inline data (rename, date edit)

Don't use when

- Simple single-line text tooltips — use Tooltip instead
- Full-screen overlays — use Dialog or Bottom Sheet
- Permanent UI that users will interact with frequently — embed it inline
- Mobile as a large overlay — use Bottom Sheet instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-fast` | opacity, transform scale(0.95 → 1) + translateY/X |
| Close | `--ease-in` | `--dur-fast` | opacity |
| Reposition (collision) | `--ease-out` | `--dur-fast` | transform |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-popover` | Root floating panel — surface-2, r4, border-subtle, shadow |
| `.ds-popover__arrow` | Directional arrow pointer |
| `.ds-popover__header` | Optional title row with close button |
| `.ds-popover__body` | Content area — padding 16px |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | undefined | Controlled open state |
| `onOpenChange` | (open: boolean) => void | undefined | Open state handler |
| `trigger` | ReactNode | required | Element that opens the popover |
| `align` | "start" | "center" | "end" | "center" | Alignment relative to trigger |
| `side` | "top" | "bottom" | "left" | "right" | "bottom" | Preferred side |
| `sideOffset` | number | 8 | Gap between trigger and popover in px |
| `children` | ReactNode | required | Popover content |

## Code examples

````html
<div class="popover-wrap">
  <button
    class="filter-btn"
    aria-haspopup="dialog"
    aria-expanded="false"
    aria-controls="pop-platform"
    onclick="this.setAttribute('aria-expanded','true'); document.getElementById('pop-platform').hidden=false;"
  >Filter ▾</button>

  <div
    class="popover"
    id="pop-platform"
    role="dialog"
    aria-modal="false"
    aria-labelledby="pop-platform-title"
    hidden
  >
    <p id="pop-platform-title" class="popover-title">Platform</p>
    <!-- content -->
  </div>
</div>
````

````html
<div class="popover" role="dialog" aria-modal="false" aria-labelledby="pop-filter-title">
  <p id="pop-filter-title" class="popover-title">Platform</p>
  <button class="popover-close" aria-label="Close filter">✕</button>

  <label class="popover-check-row">
    <input type="checkbox" name="platform" value="mobile" checked> Mobile
  </label>
  <label class="popover-check-row">
    <input type="checkbox" name="platform" value="web"> Web
  </label>
  <label class="popover-check-row">
    <input type="checkbox" name="platform" value="tv" checked> TV
  </label>

  <button class="popover-apply-btn">Apply filters</button>
</div>
````

````
<script>
function openPopover(triggerId, popoverId) {
  const trigger = document.getElementById(triggerId);
  const pop = document.getElementById(popoverId);
  trigger.setAttribute('aria-expanded', 'true');
  pop.hidden = false;
  // Focus first interactive element
  pop.querySelector('button,input,[tabindex]')?.focus();
}

function closePopover(triggerId, popoverId) {
  const trigger = document.getElementById(triggerId);
  const pop = document.getElementById(popoverId);
  trigger.setAttribute('aria-expanded', 'false');
  pop.hidden = true;
  trigger.focus(); // return focus to trigger
}

document.addEventListener('click', e => {
  document.querySelectorAll('.popover:not([hidden])').forEach(pop => {
    if (!pop.contains(e.target) && !e.target.matches('[aria-haspopup]')) {
      pop.hidden = true;
    }
  });
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    document.querySelectorAll('.popover:not([hidden])').forEach(pop => {
      pop.hidden = true;
    });
  }
});
</script>
````

## Changelog

Initial draft. Three size tiers (S/M/L), four variants (simple, header+close, form controls, loading skeleton), full accessibility table. Mobile bottom-sheet guidance documented.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--jio-light`
- `--r2`
- `--r3`
- `--r5`
- `--space-2`
- `--surface-2`
- `--surface-3`
- `--surface-4`
- `--text`
- `--text2`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

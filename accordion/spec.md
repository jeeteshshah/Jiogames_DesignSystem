# Accordion — JioGames DLS spec

> Source: `accordion/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Accordion

---

Vertically stacked expandable items for FAQs, settings categories, and grouped content. One item open at a time (exclusive) or multiple (non-exclusive).

Accordion · exclusive mode, first item expanded

Accordions progressively disclose content — hiding detail until the user needs it. They reduce cognitive load on dense pages like FAQs, settings screens, and help centres by showing only headings by default. Unlike Collapsible (which is a single show/hide), Accordion manages a group of related items with shared expand/collapse logic.

- **Exclusive (single-open)** — only one item can be expanded at a time. Collapsing one opens none.
- **Non-exclusive (multi-open)** — any number of items can be expanded simultaneously.
- **Flush / borderless** — no outer border; items separated by dividers only. Use inside cards.
- **With icon prefix** — leading icon on trigger for category-style accordions (e.g. Settings groups).

- Keep trigger text under 60 characters — a question or a category name.
- Use 14px / line-height 1.6 for body text — the comfortable reading standard.
- Ensure triggers are at least 48px tall for touch affordance on mobile.
- Animate the chevron icon 180° on expand — confirms state change visually.
- Use exclusive mode for FAQs; non-exclusive for settings where users compare panels.

- Nest accordions — never put an accordion inside another accordion panel.
- Use accordions for navigation — links that go to new pages belong in a nav list.
- Open all items by default — defeats the purpose of progressive disclosure.
- Use accordion for a single item — use Collapsible instead.
- Put critical actions inside accordion panels — they must be always visible.

1. 1 Trigger label Required 15px / weight 600. Active trigger: `var(--jio)`. Default: `var(--text)`. Max 60 chars. Question or category format. `font-size:15px; font-weight:700`
2. 2 Chevron icon Required 16px icon. Rotates 180° when expanded. Color matches trigger label — green when open, muted when closed. `transition: transform var(--dur-fast)`
3. 3 Body content Required 14px / line-height 1.6 / `var(--text2)`. Padding: 0 `var(--space-2)` 16px. Can contain text, links, and simple lists. `font-size:14px; line-height:1.6`
4. 4 Item divider Required 1px border between items. Uses `var(--border-subtle)`. Omit on last child. `border-bottom: 1px solid var(--border-subtle)`

## Variants

All variants use the same trigger/panel structure. Outer border and icon prefix are the only visual differences.

## Sizes

Two sizes. Default for most surfaces. Compact for dense settings panels or sidebar accordions.

## States

Each trigger has 5 states. Disabled items remain visible with reduced opacity.

## Content guidance

Trigger text should be a question or category name. Keep under 60 chars. Body text: 14px, line-height 1.6. Never nest accordions — use a flat list instead.

- Write as a question for FAQs: "How do I cancel my subscription?"
- Write as a noun for settings: "Notification preferences" not "Manage notifications".
- Max 60 characters — longer text wraps awkwardly on mobile.
- Don't start with a verb unless it's unavoidable — noun-first reads faster at a glance.

- 14px body, 1.6 line-height — comfortable reading density.
- Links are allowed inside body. Buttons are discouraged — surface critical actions above the accordion.
- Keep body text concise — if content exceeds ~200 words, consider a dedicated page instead.
- Never nest another accordion inside a panel body.

## Platform considerations

- Full-width, edge-to-edge layout.
- Minimum trigger height 48px — ensures comfortable touch tap area.
- Use default size only — compact is too dense at small screen widths.
- Expanded panels should not be taller than the viewport — allow inner scroll if needed.

- Max-width 640px recommended for FAQ-style accordions.
- Keyboard: Tab to focus trigger, Enter / Space to toggle, Tab into panel content when open.
- Add smooth `max-height` transition for expand/collapse animation.
- Right-click on trigger should not open a context menu — `` prevents this by default.

- D-pad Down navigates through triggers, OK expands/collapses.
- Expanded panel content is scrollable via D-pad when focused inside.
- Use default size minimum — compact is unreadable at 3m.
- Avoid deep content in panels on TV — prefer a new screen instead.

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Trigger | `` + `aria-expanded` | `aria-expanded="true"` when panel is open. Links to panel via `aria-controls="panel-id"`. |
| Panel | `role="region"` + `aria-labelledby` | Region label points to trigger id. Hidden panels use `hidden` attr or `display:none`. |
| Chevron | `aria-hidden="true"` | Icon is decorative — state is communicated via `aria-expanded`, not icon direction. |
| Keyboard | Enter / Space | Toggles expanded state. Tab moves into panel content when open. Shift+Tab returns to trigger. |
| Disabled | `disabled` attr | Disabled triggers are skipped by Tab. Add `aria-disabled="true"` if you want them in tab order but non-interactive. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Expanded trigger label and chevron color |
| `--border-subtle` | `rgba(255,255,255,.08)` | Outer accordion border and item dividers |
| `--glass-1` | `rgba(255,255,255,.04)` | Trigger hover background |
| `--text` | `#f4f2ee` | Default trigger label color |
| `--text2` | `rgba(244,242,238,.55)` | Body text color |
| `--text3` | `rgba(244,242,238,.32)` | Chevron icon color (collapsed) |
| `--r5` | `16px` | Outer accordion container border-radius |
| `--dur-fast` | `120ms` | Chevron rotation and hover background transition |

## When to use

Use when

- Displaying FAQs, settings categories, or grouped help content
- Collapsing secondary content to reduce initial visual load
- Navigation menus with expandable sub-items
- Long-form content that benefits from progressive disclosure

Don't use when

- Critical content that users must see — use a visible section instead
- Fewer than 2 items — just show the content directly
- Deeply nested accordions (more than 2 levels)
- Content that changes frequently — use tabs instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Expand | `--ease-out` | `--dur-fast` | max-height, opacity |
| Collapse | `--ease-in` | `--dur-fast` | max-height, opacity |
| Chevron rotate | `--ease-out` | `--dur-fast` | transform rotate(180deg) |
| Hover | `--ease-out` | `100ms` | background |
| Focus ring | `instant` | `0ms` | outline |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-accordion` | Root container — stacked accordion items |
| `.ds-accordion-item` | Single expandable row |
| `.ds-accordion-trigger` | Clickable header button |
| `.ds-accordion-trigger[aria-expanded="true"]` | Open state — green title text |
| `.ds-accordion-body` | Collapsible content area |
| `.ds-accordion-item--disabled` | Disabled item — 38% opacity, no pointer events |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `type` | "single" | "multiple" | "single" | Allow one or multiple items open at once |
| `defaultValue` | string | string[] | undefined | Initially open item(s) |
| `value` | string | string[] | undefined | Controlled open state |
| `onValueChange` | (value) => void | undefined | Fired when open state changes |
| `disabled` | boolean | false | Disable all items |
| `collapsible` | boolean | false | Allow closing the open item in single mode |

## Code examples

````html
<div class="accordion-item">
  <button class="accordion-trigger"
          aria-expanded="false"
          aria-controls="faq-1"
          id="faq-1-trigger">
    How does JioGames Pass work?
    <svg class="accordion-icon" width="16" height="16" aria-hidden="true">
      <!-- chevron-down path -->
    </svg>
  </button>
  <div class="accordion-body"
       role="region"
       id="faq-1"
       aria-labelledby="faq-1-trigger"
       hidden>
    JioGames Pass gives you access to 100+ premium games...
  </div>
</div>
````

````html
<div class="accordion">
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="true" aria-controls="p1">
      Question one
      <svg class="accordion-icon" aria-hidden="true">...</svg>
    </button>
    <div class="accordion-body" role="region" id="p1">Answer one</div>
  </div>
  <div class="accordion-item">
    <button class="accordion-trigger" aria-expanded="false" aria-controls="p2">
      Question two
      <svg class="accordion-icon" aria-hidden="true">...</svg>
    </button>
    <div class="accordion-body" role="region" id="p2" hidden>Answer two</div>
  </div>
</div>
````

````
// For non-exclusive: each trigger toggles independently
document.querySelectorAll('.accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    const expanded = trigger.getAttribute('aria-expanded') === 'true';
    const panel = document.getElementById(trigger.getAttribute('aria-controls'));
    trigger.setAttribute('aria-expanded', !expanded);
    panel.hidden = expanded;
  });
});
````

## Changelog

Initial draft. Exclusive and non-exclusive variants. Default and compact sizes. Flush / borderless variant. Icon prefix variant. Full accessibility documentation.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--r5`
- `--space-2`
- `--surface-1`
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

# Collapsible — JioGames DLS spec

> Source: `collapsible/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Collapsible

---

A single show/hide container triggered by a button. Lighter than Accordion — use for one-off expandable content like "Show advanced settings" or "Show more games".

Collapsible · text trigger, collapsed and expanded states

Collapsible is a single-instance show/hide primitive — the simplest form of progressive disclosure. Unlike Accordion, it manages only one content region and has no shared group logic. Use it for secondary or overflow content where the label alone communicates enough context: "Show 12 more games", "Show advanced filters", "Read the full description".

- **Text trigger** — a plain green inline button, inherits from its context. Most common use.
- **Button trigger** — outlined button style, for use in card surfaces or when the trigger needs more visual weight.
- **Inline** — no wrapper element; trigger sits directly in flow of text or a list row.

- Label the trigger for BOTH states — "Show 12 more games" collapses to "Hide games", not back to "Show more".
- Include the count in the collapsed label when possible: "Show 12 more" not "Show more".
- Use Collapsible for a single isolated expandable region. Use Accordion for a group.
- Position the trigger immediately before or after its content — never separated by other elements.
- Keep expanded content within the user's scrollable viewport where possible.

- Label the trigger "Toggle" — this word is meaningless to most users.
- Use "Show more / Show less" — "less" is vague. Write "Hide [noun]" instead.
- Use Collapsible for navigation or interactive controls — only for content reveal.
- Stack multiple Collapsibles — use an Accordion group instead for better structure.
- Hide critical content behind a Collapsible — it must be optional / secondary.

1. 1 Trigger label Required 14px / weight 700 / `var(--jio)`. Must describe both the collapsed and expanded state. Count-in-label preferred. `font-size:14px; font-weight:700; color:var(--jio)`
2. 2 Chevron icon Required 14px inline chevron. Rotates 180° when expanded. `aria-hidden="true"` — state communicated via `aria-expanded`. `transition: transform var(--dur-fast)`
3. 3 Content panel Required Hidden via `hidden` attr or CSS grid trick. Linked to trigger via `aria-controls` and matching `id`. `id="panel-id" — matches aria-controls`

## Variants

Three trigger styles for different surface contexts. Content panel structure is identical across all variants.

Advanced settings content appears here — resolution overrides, developer flags, cache controls.

Tomb Raider: Reloaded

Action adventure · 2.3 GB · More info

Last updated Jan 2026 · Rated 12+ · 4.8 ★ (12.4k ratings)

## Sizes

Collapsible has no independent size scale — the trigger inherits size from its surrounding context. Pair with the appropriate Button or text size for the surface.

## States

Only two functional states: collapsed and expanded. Focus ring appears on keyboard navigation.

## Content guidance

Label the trigger for both states. Never use "Toggle". Count-in-label is strongly preferred.

- Collapsed: "Show 12 more games" — includes count and noun.
- Expanded: "Hide games" — verb + noun, not "Show less" or "Collapse".
- Never use "Toggle" — meaningless without directional context.
- If count is unavailable at render time, use "Show more [noun]" with the noun always present.

- Mobile + Web: trigger and content in normal document flow — no special treatment.
- TV: if the revealed content is large, prefer a bottom sheet or new screen. Expanding in-place on TV can scroll content off-screen with no clear recovery path.
- Trigger minimum touch target on mobile: 44px height. Use `padding: 12px 0` if the text alone is too small.

## Platform considerations

- Trigger sits inline or block depending on context — both are valid.
- Min touch height 44px — add vertical padding to text triggers if needed.
- Revealed content scrolls with the page — no inner scroll needed for most cases.
- Animate expand via CSS grid trick — hardware-accelerated, no JS height calc.

- Keyboard: Tab to trigger, Enter / Space toggles, Tab into revealed content.
- Focus-visible ring: 2px solid `var(--jio)`, offset 3px.
- CSS grid animation works without JS height calculation — use `grid-template-rows: 0fr → 1fr`.
- Announced to screen readers via `aria-expanded` on the trigger.

- If expanded content exceeds viewport height, prefer a bottom sheet instead.
- D-pad OK button triggers expand/collapse.
- Ensure revealed content items are themselves D-pad navigable when focused.
- Text trigger size should be at least 14px — increase to 16px in dense TV layouts.

## Accessibility

| Element | Role / attribute | Guidance |
|---|---|---|
| Trigger | `` + `aria-expanded` | `aria-expanded="true/false"` reflects current state. Links panel via `aria-controls="panel-id"`. |
| Content panel | `id` + `hidden` | Matches `aria-controls` value. Use native `hidden` attr — screen readers skip it automatically. |
| Chevron icon | `aria-hidden="true"` | Decorative. State is communicated by `aria-expanded` — not icon direction. |
| Focus ring | `:focus-visible` | 2px solid `var(--jio)` with 3px offset. Only shown on keyboard focus, not mouse click. |
| Label change | Dynamic text | When trigger label changes ("Show" → "Hide"), screen readers re-announce. Ensure label always describes the next action. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Trigger text color and focus ring color |
| `--border-subtle` | `rgba(255,255,255,.08)` | Button variant border color |
| `--glass-1` | `rgba(255,255,255,.04)` | Button variant hover background |
| `--dur-fast` | `120ms` | Chevron rotation transition |
| `--dur-base` | `200ms` | Content reveal animation duration |
| `--r2` | `6px` | Focus ring border-radius on text trigger |
| `--r3` | `8px` | Button trigger border-radius |

## When to use

Use when

- Showing/hiding optional secondary content below a trigger
- Expandable code blocks or long descriptions
- Advanced options sections in settings forms
- Read more / show less patterns for truncated text

Don't use when

- Multiple related collapsible sections — use Accordion instead
- Critical information that should always be visible
- Navigation items with sub-sections — use NavigationMenu instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Open | `--ease-out` | `--dur-fast` | max-height, opacity |
| Close | `--ease-in` | `--dur-fast` | max-height, opacity |
| Chevron rotate | `--ease-out` | `--dur-fast` | transform rotate(180deg) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-collapsible` | Root container |
| `.ds-collapsible__trigger` | Toggle button — full width or inline |
| `.ds-collapsible__content` | Collapsible content area — overflow hidden |
| `.ds-collapsible__content--open` | Expanded state |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | boolean | undefined | Controlled open state |
| `defaultOpen` | boolean | false | Uncontrolled initial state |
| `onOpenChange` | (open: boolean) => void | undefined | Change handler |
| `disabled` | boolean | false | Prevent toggling |

## Code examples

````html
<div class="collapsible">
  <button class="collapsible-trigger"
          aria-expanded="false"
          aria-controls="more-games">
    Show 12 more games
    <svg class="collapsible-icon" width="14" height="14" aria-hidden="true">
      <!-- chevron-down path -->
    </svg>
  </button>
  <div class="collapsible-content" id="more-games" hidden>
    <!-- revealed content -->
  </div>
</div>

<script>
  document.querySelector('.collapsible-trigger').addEventListener('click', function() {
    const expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    document.getElementById('more-games').hidden = expanded;
    this.childNodes[0].textContent = expanded ? 'Show 12 more games' : 'Hide games ';
  });
</script>
````

````
<!-- CSS grid trick: animates from 0 to natural height -->
<style>
  .collapsible-content--animated {
    display: grid;
    grid-template-rows: 0fr;
    transition: grid-template-rows 200ms var(--ease-out);
  }
  .collapsible-content--animated > * { overflow: hidden; }

  /* When trigger is expanded, sibling content opens */
  .collapsible-trigger[aria-expanded="true"] + .collapsible-content--animated {
    grid-template-rows: 1fr;
  }
</style>

<div class="collapsible">
  <button class="collapsible-trigger" aria-expanded="false">Show more</button>
  <div class="collapsible-content--animated">
    <div><!-- inner wrapper required for grid trick -->
      Content here...
    </div>
  </div>
</div>
````

````
<!-- Fetch count from data, render into label before mount -->
<button class="collapsible-trigger"
        aria-expanded="false"
        aria-controls="more-games"
        data-count="12">
  Show <span class="collapsible-count">12</span> more games
  <svg class="collapsible-icon" width="14" height="14" aria-hidden="true">...</svg>
</button>
````

## Changelog

Initial draft. Text trigger, button trigger, and inline variants. CSS grid animation technique documented. Full accessibility and content guidance included.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--dur-base`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--jio`
- `--jio-font`
- `--r2`
- `--r3`
- `--r4`
- `--surface-1`
- `--surface-2`
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

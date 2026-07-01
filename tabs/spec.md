# Tabs — JioGames DLS spec

> Source: `tabs/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Tabs

---

Horizontal navigation between content panels. Used on game detail pages (Overview / Screenshots / Reviews), profile pages (Library / Activity / Friends), and settings.

Screenshots showcase environments, gameplay, and UI. Tap any image to expand it to full screen.

Tabs in context · active indicator, badge count, scrollable

Tabs let users switch between distinct views of related content without leaving the current page. They are always visible — unlike accordions — so users can see all available sections at a glance. Tabs work best when each panel contains substantively different content that a user would want to navigate between repeatedly.

- **Default / Underline** — tab strip with green bottom-border on active tab; default for all surfaces
- **With badge** — count indicator showing unread items or totals in a panel
- **With icon + label** — pairs a 16px icon with text for richer context on wider layouts
- **Pill style** — rounded background on active tab; use only in card surfaces, not page-level navigation

- Use 2–7 tabs. Below 2, use a toggle. Above 7, collapse extras into a "More" menu.
- Keep tab labels to 1–3 words. "Screenshots" not "Game Screenshots Gallery".
- Preserve tab scroll position when returning to a tab — don't reset the panel.
- Use badge counts only when a panel has genuinely new or countable items.
- Provide keyboard arrow-key navigation between tabs.

- Use tabs for 2 mutually exclusive states — use a Toggle Group instead.
- Place tabs inside a scrollable modal with other stacked tabs — causes navigation confusion.
- Use tabs as breadcrumbs or step indicators — use a Stepper component instead.
- Vary the visual weight of tab labels — all tabs should use the same font-size and weight.
- Hide tabs that have no content — disable them with `disabled` instead.

1. 1 Active indicator Required 2px bottom border in `var(--jio)` on the active tab. Sits on top of the strip border using `margin-bottom: -1px`. `border-bottom: 2px solid var(--jio)`
2. 2 Badge count Optional Compact pill showing a count. Background `var(--jio)`, text black, 10px/900. Hide when count is 0. `.tab-badge — min-width:18px; height:18px`
3. 3 Strip border Required Full-width 1px bottom border on the tab list container. Provides visual floor for all tabs. `border-bottom: 1px solid var(--border-subtle)`
4. 4 Tab label Required 14px / weight 600. Active tab uses `var(--text)`. Inactive uses `var(--text3)`. Hover: `var(--text2)`. `font-size:14px; font-weight:700`

## Variants

All variants share the same tab-list structure. Only the active indicator and container background differ.

## Sizes

Three sizes for different surface densities. S for compact headers, M (default) for most surfaces, L for prominent page-level navigation.

## States

Each tab trigger has 5 states. Disabled tabs remain visible but non-interactive — never hide them.

## Content guidance

Tabs are not breadcrumbs. Content under each tab should be substantively different.

- 1–3 words. Noun-first: "Reviews" not "Read Reviews".
- Never use verbs unless the action is the point: "Download" is acceptable.
- Don't duplicate the page title in the first tab — "Overview" is always sufficient.
- Avoid abbreviations unless the abbreviation is the known term (e.g. "DLC").

- Never use tabs for 2 items — use a toggle group instead.
- Never use tabs for more than 7 items — collapse extras into a "More" overflow menu.
- Don't nest tab groups — use a single level of tabs per page region.
- Tab order should follow content priority, not alphabetical order.

## Platform considerations

- Tab list scrolls horizontally with `overflow-x: auto` and hidden scrollbar.
- Active tab is always scrolled into view on mount.
- Swipe gesture between panels maps to tab switching.
- Minimum touch target height: 44px (use M or L size).
- Active indicator sits at bottom of tab strip.

- Same visual treatment as mobile — underline indicator at bottom.
- Keyboard: Arrow Left / Right to move between tabs, Enter / Space to select.
- Tab strip does not need to scroll on wide viewports — all tabs should be visible.
- Add `title` on truncated tab labels for tooltip on hover.

- Tabs become a D-pad–navigable horizontal row.
- Active tab gets a visible focus ring (3px, `var(--jio)`).
- Use L size minimum for legibility at 3m viewing distance.
- Do not auto-advance tabs on TV — only change on D-pad confirm.

## Accessibility

Tabs must implement full ARIA tab pattern. Screen readers announce the active panel and total tab count.

| Element | Role / attribute | Guidance |
|---|---|---|
| Tab list container | `role="tablist"` | Wraps all tab triggers. Optionally add `aria-label="Page sections"` if multiple tab groups exist. |
| Tab trigger | `role="tab"` + `aria-selected` | `aria-selected="true"` on active tab, `"false"` on others. Link to panel via `aria-controls="panel-id"`. |
| Tab panel | `role="tabpanel"` | Matches trigger via `id`. Add `aria-labelledby="trigger-id"`. Hidden panels use `hidden` or `display:none`. |
| Keyboard | Arrow keys | Left / Right arrows move focus between tabs. Home / End jump to first / last. Enter or Space activates focused tab. |
| Badge count | `aria-label` | Label the whole trigger: `aria-label="Reviews, 12 items"`. Don't rely on visual badge alone. |

## Related tokens

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Active tab indicator border-bottom color |
| `--border-subtle` | `rgba(255,255,255,.08)` | Tab strip bottom border |
| `--text` | `#f4f2ee` | Active tab label color |
| `--text2` | `rgba(244,242,238,.55)` | Hover tab label color |
| `--text3` | `rgba(244,242,238,.32)` | Default / inactive tab label color |
| `--dur-fast` | `120ms` | Color and indicator transition duration |
| `--pill` | `100px` | Tab badge border-radius |

## When to use

Use when

- In-page content organisation: Overview / Gameplay / Reviews tabs on game detail
- Filter views on the library screen (All / Installed / Wishlist)
- Settings categories within a screen
- Segmented views where content is different but related

Don't use when

- Primary app navigation — use Tab Bar instead
- More than 6 tabs on mobile — horizontal scroll becomes confusing
- Tabs where content on different tabs is mostly identical
- Tab panels that contain navigation to other screens — tabs are in-page only

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Active indicator slide | `--ease-out` | `--dur-fast` | transform translateX |
| Panel crossfade | `--ease-out` | `--dur-fast` | opacity |
| Pressed tab scale | `--ease-out` | `80ms` | transform scale(0.95) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-tabs` | Root container — flex column |
| `.ds-tabs__list` | Tab button row — flex, border-bottom |
| `.ds-tabs__trigger` | Single tab button — 40px height, 13px 700 |
| `.ds-tabs__trigger--active` | Active tab — jio text, jio indicator underline |
| `.ds-tabs__indicator` | Sliding underline — 2px jio-green, position absolute bottom |
| `.ds-tabs__content` | Panel area — shown when tab active |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | required | Controlled active tab |
| `onValueChange` | (v: string) => void | required | Tab change handler |
| `defaultValue` | string | undefined | Uncontrolled initial active tab |
| `orientation` | "horizontal" | "vertical" | "horizontal" | Tab list direction |
| `children` | ReactNode | required | TabsList and TabsContent components |

## Code examples

Copy as starting points. Always link `tokens.css`, `components.css`, and `states.css`.

````html
<div class="tabs">
  <div class="tab-list" role="tablist" aria-label="Game sections">
    <button class="tab-trigger" role="tab" id="tab-1"
            aria-selected="false" aria-controls="panel-1">Overview</button>
    <button class="tab-trigger is-active" role="tab" id="tab-2"
            aria-selected="true" aria-controls="panel-2">Screenshots</button>
    <button class="tab-trigger" role="tab" id="tab-3"
            aria-selected="false" aria-controls="panel-3">Reviews</button>
  </div>

  <div class="tab-content" role="tabpanel" id="panel-1" aria-labelledby="tab-1" hidden>
    <!-- Overview content -->
  </div>
  <div class="tab-content is-active" role="tabpanel" id="panel-2" aria-labelledby="tab-2">
    <!-- Screenshots content -->
  </div>
  <div class="tab-content" role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden>
    <!-- Reviews content -->
  </div>
</div>
````

````html
<button class="tab-trigger" role="tab"
        aria-selected="false"
        aria-label="Reviews, 12 items">
  Reviews
  <span class="tab-badge" aria-hidden="true">12</span>
</button>
````

````html
<button class="tab-trigger is-active" role="tab" aria-selected="true"
        style="display:inline-flex; align-items:center; gap:6px;">
  <svg width="14" height="14" aria-hidden="true">
    <use href="/sprite.svg#ic_library"></use>
  </svg>
  Library
</button>
````

## Changelog

Initial draft. Underline, pill, and icon+label variants. S / M / L size tiers. Full ARIA tab pattern documentation. Badge count guidance.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--jio`
- `--jio-font`
- `--pill`
- `--r4`
- `--space-3`
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

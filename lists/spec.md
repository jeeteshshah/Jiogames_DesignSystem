# Lists — JioGames DLS spec

> Source: `lists/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Lists

---

Lists present sequential items — settings, menus, game libraries — with consistent row structure.

Lists · Navigation, Detail, Toggle, Destructive row types

Lists are the backbone of settings screens, game libraries, and contextual menus across JioGames. A consistent row structure — leading content, primary label, secondary text, trailing action — lets players scan and act without friction.

- **Row anatomy is fixed.** Leading content (icon/thumbnail), primary label, optional secondary, and a single trailing action.
- **One trailing action per row.** Don't mix chevron + toggle in the same row.
- **Separator is optional.** Use only when visual grouping is unclear without it.
- **Platform-aware sizing.** Row heights differ across Mobile, Web, and TV contexts.

## Best practices

- Keep primary labels to 1 line; truncate with ellipsis if needed.
- Use secondary/meta text for context, not repetition of the label.
- Group related rows with section headers, not visual dividers alone.
- Use destructive red label for irreversible actions (Delete, Remove, Clear).
- Maintain consistent leading content type within a list section.
- Add skeleton rows during loading, not empty states.

- Don't mix icon and thumbnail rows in the same list without visual reason.
- Don't add more than one trailing action per row.
- Don't use chevron if the row triggers an action, not navigation.
- Don't truncate primary labels when secondary text is more important.
- Don't use more than 2 lines for secondary text.
- Don't add borders between every row in dense TV lists.

## Anatomy

Every list row is built from a fixed set of slots. Slots 1 and 3 are required; all others are optional and compose freely.

- Row container Required Full-width flex row. Min-height 56px mobile, 60px web, 80px TV. Receives all interaction states. `min-height: 56px (mobile default)`
- Leading icon / thumbnail Optional 36px icon container or 40–48px thumbnail. Always `flex-shrink: 0` to prevent squishing. `width: 36–48px; border-radius: --r3`
- Primary label Required Main text. One line with ellipsis overflow. font-size 14px mobile/web, 18px TV. font-weight 500. `font-size: 14px; font-weight: 500; color: --text`
- Secondary / metadata text Optional Context text beneath the primary label. font-size 12px. color --text3. Maximum 2 lines. `font-size: 12px; color: --text3`
- Trailing action Optional One of: chevron ›, toggle, badge, count, or a small button. Never two trailing elements in the same row. `flex-shrink: 0; max one per row`
- Separator Optional 1px hairline divider between rows. Use --border-subtle. Omit in dense TV lists or when section headers provide grouping. `border-bottom: 1px solid --border-subtle`

## Variants

Five row types cover every major use case across JioGames settings, libraries, and menus.

Icon + label + chevron. For settings screens, menu items, and any row that navigates to a child screen.

Label + metadata below + optional badge trailing. For game libraries, search results, and content feeds.

Leading checkbox + label. For multi-select flows like genre preferences, filter sheets, and batch operations.

Label with trailing action button. For destructive operations, confirmable actions, and secondary in-place controls.

Game art thumbnail + title + meta + trailing action. Richer than detail list; used in libraries and curated collections.

## Sizes

Row height adapts to context and platform. Standard is the default. Compact suits dense settings sheets. Large suits featured navigation or rows containing thumbnails.

| Size | Mobile | Web | TV |
|---|---|---|---|
| Compact | 48px | 52px | 68px |
| Standard | 56px | 60px | 80px |
| Large | 72px | 76px | 96px |

## States

Eight states cover the full interaction model across touch, pointer, keyboard, and TV remote. All states apply at row level, not element level.

## Content guidance

Copy in list rows follows the same economy principle as the rest of JioGames — the row must communicate at a glance.

- Maximum 1 line; overflow with ellipsis.
- Sentence case. Noun or verb phrase.
- Avoid articles — write "Account Settings" not "The Account Settings".
- For destructive rows: use imperative verb ("Clear Cache", "Delete Account").

- Context, not repetition of the label.
- Dates in relative format ("3 days ago", "Just now").
- Ratings always include the star symbol: ★4.9 not "4.9 stars".
- File sizes in human-readable form: "2.3 GB" not "2300 MB".

## Platform specifications

- Standard row height: **56px**.
- Minimum touch target: 44px (WCAG 2.5.5).
- Leading icon size: 36px.
- Swipe-to-reveal for destructive row actions (delete, archive).
- Haptic feedback on destructive confirm.

- Standard row height: **60px**.
- `cursor: pointer` on interactive rows.
- Hover state: subtle background shift (`rgba(244,242,238,.04)`).
- Keyboard navigation with arrow keys across rows.
- Focus ring on entire row, not just trailing element.

- Standard row height: **80px**.
- Focus ring on entire row via `--tv-focus-shadow`.
- No hover state — TV has no pointer device.
- D-pad navigation; enter/select to trigger row action.
- Increase primary label to **18px** for 10-foot legibility.
- Omit row separators in dense lists to reduce visual noise.

## Accessibility

Lists must be fully navigable by screen readers, keyboard, and switch access. Semantic markup is not optional.

Use `role="list"` on the container and `role="listitem"` on each row. Alternatively, use semantic `/` elements. Either approach is valid; don't use both together.

Wrap the entire row in a `` or ``. Do not attach the tap handler only to the trailing chevron — this breaks keyboard and screen reader access.

Add an `aria-label` on the row that describes the destination: `aria-label="Go to Account Settings"`. The chevron itself is `aria-hidden="true"`.

The toggle element uses `role="switch"` and `aria-checked="true|false"`. The row label should be linked via `aria-labelledby` pointing at the primary label element.

Include the destructive nature in the accessible label: `aria-label="Delete account — destructive, cannot be undone"`. This ensures screen reader users are warned before confirming.

Visible focus ring must encircle the entire row, not just inner elements. Use `outline: 2px solid var(--jio); outline-offset: 2px` on the row. Never suppress `:focus-visible` without an alternative.

## Related tokens

Design tokens used directly by the List component. Reference these in code instead of raw values.

| Token | Usage | Value |
|---|---|---|
| `--surface-1` | List container background | Surface level 1 |
| `--border-subtle` | Row separator, container border | Hairline divider |
| `--text` | Primary label color | #F4F2EE |
| `--text3` | Secondary / metadata color | 32% opacity text |
| `--r5` | List container border-radius | 16px |
| `--touch-min` | Minimum touch target height | 44px |
| `--jio` | Selected state accent, badge color, toggle on | #00A859 |
| `--negative` | Destructive row label and icon tint | #FF4757 |

## When to use

Use when

- Game library rows with thumbnail, title, and metadata
- Notification feed items
- Settings menu rows with icon, label, and trailing action
- Search result items

Don't use when

- Tabular data with multiple sortable columns — use Data Table
- Flat text-only bullet lists — use a plain ul/ol in prose
- Grid-layout game tiles — use Card in a grid
- More than 5 trailing actions per item — simplify the action model

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Row hover | `--ease-out` | `80ms` | background |
| Press/tap | `--ease-out` | `60ms` | transform scale(0.99), background |
| Swipe to delete | `--ease-out` | `--dur-base` | transform translateX, opacity |
| Item appear (stagger) | `--ease-out` | `--dur-fast` | opacity, transform translateY(8px → 0) |
| Expand (nested list) | `--ease-out` | `--dur-fast` | max-height |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-list` | Root list container — flex column |
| `.ds-list-item` | Single row — flex, min-height 56px, padding 0 16px |
| `.ds-list-item__leading` | Leading slot — icon, avatar, or thumbnail |
| `.ds-list-item__body` | Text stack — flex column, flex:1 |
| `.ds-list-item__title` | 14px 600 text |
| `.ds-list-item__subtitle` | 12px text3 |
| `.ds-list-item__trailing` | Trailing slot — chevron, badge, toggle |
| `.ds-list-item--destructive` | Red title for delete actions |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `items` | ListItem[] | required | Array of item data objects |
| `onItemPress` | (item: ListItem) => void | undefined | Tap/click handler |
| `leading` | (item: ListItem) => ReactNode | undefined | Leading slot renderer |
| `trailing` | (item: ListItem) => ReactNode | undefined | Trailing slot renderer |
| `divider` | boolean | true | Show separator lines between items |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<ul class="ds-list" role="list">
  <li class="ds-list-item">
    <svg class="icon icon--m ds-list-item__icon" aria-hidden="true">
      <use href="/sprite.svg#ic_gamepad"></use>
    </svg>
    <div class="ds-list-item__body">
      <div class="ds-list-item__label">War Thunder</div>
      <div class="ds-list-item__meta">Action · 2.1 GB</div>
    </div>
    <svg class="icon icon--m ds-list-item__trailing" aria-hidden="true">
      <use href="/sprite.svg#ic_chevron_right"></use>
    </svg>
  </li>
</ul>
````

````html
<div class="ds-list-group">
  <div class="ds-list-group-header">RECENTLY PLAYED</div>
  <ul class="ds-list" role="list">
    <li class="ds-list-item">...</li>
    <li class="ds-list-item">...</li>
  </ul>
</div>
````

## Changelog

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--jio`
- `--jio-font`
- `--negative`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
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

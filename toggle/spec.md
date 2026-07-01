# Toggle — JioGames DLS spec

> Source: `toggle/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Toggle

---

A toggle switch controls a binary on/off setting with immediate effect.

Toggle switches give players immediate, persistent control over binary settings. Unlike buttons that trigger one-time actions, a toggle persists its state until explicitly changed. Use toggles only for settings with an immediate effect — changes take effect without requiring a Save action.

- **Binary only.** Toggles control on/off states exclusively. Use a checkbox for selections, a radio for one-of-many choices.
- **Immediate effect.** The setting activates on tap. Never require a confirm step unless the action is destructive.
- **Label the setting, not the action.** “Autoplay videos” not “Enable Autoplay”.
- **Platform-aware sizing.** Mobile 24×40px track, Web 26×44px, TV 36×60px.

## When to use

Use when

- Binary on/off settings: notifications, dark mode, auto-play
- Feature flags or preference switches in settings screens
- Enabling/disabling individual items in a list

Don't use when

- Multi-option selection — use Radio or Checkbox instead
- Actions with consequences that can't be undone — use Button + Dialog
- Toggles that require explanation longer than a short label
- Using toggle for navigation state — use Tabs instead

## Best practices

Follow these rules to keep toggle usage consistent across the JioGames settings surface.

- Label the setting noun (“Autoplay videos”, “Dark mode”)
- Use sub-labels to explain the consequence in under 60 chars
- Keep toggles grouped in settings lists, not scattered across the UI
- Ensure the label still makes sense when the toggle is off
- Show a loading state when the toggle triggers an async change
- Use disabled state with a tooltip explaining why

- Don't use toggles for actions (use a button instead)
- Don't label with “Enable X” — the toggle implies enable/disable
- Don't require a Save button after a toggle change
- Don't use toggles for form inputs or multi-step flows
- Don't place toggles in dense action areas without visual separation
- Don't animate toggle thumb > 200ms

## Anatomy

The toggle is a two-part structure — a pill track and a sliding thumb — combined with an optional label group. State is communicated exclusively through track fill colour and thumb position.

## Variants

Five variants cover the full toggle usage model. Default covers 95% of cases. Only use Destructive or Loading when the specific context demands it.

## Sizes

Three platform-resolved size tiers. The toggle component class stays constant — platform context determines the actual pixel values. TV sizes are mandatory for 10-foot legibility and remote-precision.

## States

Eight states cover the full interaction model. Hover states apply on web only — never on mobile or TV. The TV focused state uses `var(--tv-focus-shadow)` glow ring on the row container.

## Content

Toggle labels are the clearest signal to players about what is being controlled. Write labels that are unambiguous whether the toggle is on or off.

- Describe the setting not the action — noun or noun phrase
- Avoid “Enable X” / “Disable X” — the toggle implies it
- “Sound effects” not “Enable sound effects”
- “Dark mode” not “Turn on dark mode”
- Label must make sense without reading surrounding UI

- Explain consequences in under 60 chars
- “Downloads will use mobile data” — not “This may use mobile data depending on your connection settings”
- Write in present tense: “Plays on game events”
- Omit if the label is already fully self-explanatory
- Never repeat the label word-for-word

## Platform

The same toggle component adapts across platforms via resolved size tokens and platform-specific interaction models.

- 40×24px track; 18px thumb
- 44px minimum touch target on the row
- Haptic feedback on toggle (implementation layer)
- No hover state — touch model only
- Full-row tap target, not just the track

- 44×26px track; 20px thumb
- Pointer cursor on hover over row
- Hover state shows brighter track (off: `var(--border)`)
- Keyboard-navigable via Tab + Space
- Focus ring on track via `:focus-visible`

- 60×36px track; 28px thumb
- Navigated via D-pad — entire row is the focus target
- Focus ring on row, not track itself
- Uses `var(--tv-focus-shadow)` glow + scale(1.02)
- 18px label for 10-foot legibility

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Thumb slide (off → on) | `--ease-out` | `--dur-fast` | transform translateX |
| Track fill | `--ease-out` | `--dur-fast` | background (surface-2 → jio-green) |
| Thumb scale (press) | `--ease-out` | `80ms` | transform scale(0.85) |
| Focus ring | `instant` | `0ms` | outline on track |
| Disabled pulse | `none` | `static` | opacity 0.38 |

## Accessibility

Toggles must be navigable and interpretable without vision. The `role="switch"` semantic is mandatory — it tells screen readers this is a binary control, not a button.

## Platform considerations

- Minimum touch target 48×48px wrapping the toggle track
- State change fires on tap-release, not tap-start
- Label always to the left; toggle to the right edge of the row
- Haptic feedback recommended on state change

- Space key toggles when focused; Enter also accepted
- Focus ring on track, not thumb
- Hover on label also activates hover state on track
- Pointer cursor on hover

- OK/Select button on remote toggles state
- TV focus ring wraps full toggle row, not just track
- Do not use toggles inside scrollable lists on TV — prefer segmented control
- Increase track width to L size minimum for 10-foot legibility

## Content guidance

### Labels

Label the setting, not the state. "Notifications" not "Enable notifications". The toggle itself communicates on/off.

### Supporting text

Use supporting text only when the setting has non-obvious consequences. Keep to one short sentence below the label.

### State labels

Do not add "On" / "Off" text inside the toggle track. Colour and position of the thumb communicate state sufficiently.

### Grouping

Group related toggles under a section header. Keep each group to 5 items or fewer. Use a list component to contain multiple toggles.

## Related tokens

All token values from `tokens/tokens.css`. Never override the on-state green — `--jio` is the sole brand accent for active toggle state.

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-toggle` | Root track — 44×24px, r-pill, surface-2, transition |
| `.ds-toggle--checked` | Jio-green background |
| `.ds-toggle__thumb` | 20×20px circle — white bg, r-pill, translateX on checked |
| `.ds-toggle--disabled` | 38% opacity, no pointer events |
| `.ds-toggle-row` | Label + toggle row — flex space-between |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `checked` | boolean | required | Controlled on/off state |
| `onCheckedChange` | (v: boolean) => void | required | Change handler |
| `defaultChecked` | boolean | false | Uncontrolled initial state |
| `disabled` | boolean | false | Disable interaction |
| `size` | "sm" | "md" | "md" | Track size preset (sm: 36×20px, md: 44×24px) |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="toggle-row">
  <label class="toggle-label" for="notif-toggle">
    <span class="toggle-label__text">Notifications</span>
    <span class="toggle-label__desc">Get alerts for new games</span>
  </label>
  <div class="switch">
    <input
      type="checkbox"
      id="notif-toggle"
      class="switch__input"
      role="switch"
      aria-checked="true"
      checked
    >
    <label for="notif-toggle" class="switch__track">
      <span class="switch__thumb"></span>
    </label>
  </div>
</div>
````

````
<ul class="ds-list" role="list">
  <li class="ds-list-item">
    <div class="ds-list-item__body">
      <div class="ds-list-item__label">Notifications</div>
    </div>
    <div class="switch">
      <input type="checkbox" id="t1" class="switch__input" role="switch" checked>
      <label for="t1" class="switch__track"><span class="switch__thumb"></span></label>
    </div>
  </li>
  <li class="ds-list-item">
    <div class="ds-list-item__body">
      <div class="ds-list-item__label">Auto-play trailers</div>
    </div>
    <div class="switch">
      <input type="checkbox" id="t2" class="switch__input" role="switch">
      <label for="t2" class="switch__track"><span class="switch__thumb"></span></label>
    </div>
  </li>
</ul>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border`
- `--border-subtle`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--r4`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--tv-focus-shadow`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

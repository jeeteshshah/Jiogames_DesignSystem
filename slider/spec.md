# Slider — JioGames DLS spec

> Source: `slider/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Slider

---

Continuous value selector for volume, brightness, difficulty, and audio/video settings. Single-thumb and range variants.

Slider in settings context · Volume, Brightness, Difficulty

The Slider is a native `` element styled to match the JioGames design language. It allows users to select a continuous value between a defined minimum and maximum. Sliders are used in settings panels — never as filters in a browse or discovery context (use Chips or Select for that).

- **Audio settings** — volume, music/SFX balance, voice chat level
- **Display settings** — brightness, contrast, field of view
- **Gameplay** — difficulty level, aim sensitivity, camera speed
- **Range selection** — price or level range filter (two-thumb variant)

- Always show the current numeric value alongside the slider — never leave users guessing
- Use round step values where possible: 5, 10, 25 increments rather than 1-unit steps for coarse settings
- Label the slider with a visible text label — `aria-label` alone is not enough for sighted users
- Update the displayed value in real time as the thumb moves, not just on release
- Use the thick (6px) variant only for prominent standalone settings, not inline in dense lists

- Use a Slider for binary settings — use a Toggle instead
- Use a Slider for selecting from a short named list — use Radio or Select
- Show a Slider without a label — value alone gives no context
- Use Slider on TV — d-pad navigation makes continuous range selection frustrating; use a +/− button pair
- Stack more than 4 sliders in a single panel without a visual separator between groups

1. 1 Label Required Left-aligned text label describing what the slider controls. 13px/700 weight, paired with the value on the right. `font-size: 13px; font-weight: 700; color: var(--text2)`
2. 2 Live value Required Right-aligned numeric display that updates on every `input` event. Green accent color to signal interactivity. `font-size: 13px; font-weight: 700; color: var(--jio)`
3. 3 Track Required 4px high, pill-shaped track. The filled portion (left of thumb) is `var(--jio)`; unfilled is `var(--surface-3)`. Achieved via `background` gradient. `height: 4px; border-radius: var(--pill)`
4. 4 Thumb Required 20px circle, green fill, white border, soft green glow ring. On mobile increases to 28px for touch target compliance. `width: 20px; height: 20px; border-radius: var(--pill)`

## Variants

Four variants. Default covers the majority of settings. Step marks help when discrete named values matter. Range suits price or level filters.

## Sizes

Track height is the only size dimension that varies. Thumb size adjusts proportionally. Thumb touch target on mobile is always 28px regardless of track size.

## States

Five interaction states. The dragging state is visually identical to hover — the distinction is behavioral (pointer is down and moving).

| State | Visual change | When |
|---|---|---|
| Default | Thumb at rest, no glow ring visible | Unfocused, not interacting |
| Hover | Thumb scales 1.1× via `transform: scale(1.1)` | Pointer enters thumb hit area |
| Focused | Green outline ring `2px solid var(--jio)` with 6px offset | Keyboard focus, arrow keys move thumb |
| Dragging | Thumb scale 1.1×, track fill updates live | Pointer down and moving on track |
| Disabled | Opacity `var(--state-disabled-opacity)`, no pointer events | Setting locked (e.g., requires premium) |

## Content guidance

Labels and value displays are the only text surfaces on a slider.

- Use a single noun or noun phrase: "Volume", "Brightness", "Aim sensitivity"
- Never use a verb: not "Set volume" — just "Volume"
- Capitalise the first word only — not title case for every word
- Keep label under 24 characters to avoid wrapping on mobile

- For percentage sliders: append % — "72%"
- For named steps: show the step name — "Normal", "Hard"
- For sensitivity: show decimal if needed — "1.5×"
- Always show current value; never leave it blank even at 0
- Round to nearest integer unless the precision is meaningful

## Platform considerations

Thumb size and interaction model differ substantially across platforms.

- Increase thumb to 28px via `@media (pointer: coarse)` — minimum touch target is 44px effective area
- Full-width track — never constrain to less than the column width
- Haptic feedback on step marks where platform APIs allow
- Show value tooltip above the thumb while dragging on long settings panels

- 20px thumb is fine for pointer — no size increase needed on desktop
- Keyboard navigation via arrow keys is native on `` — do not suppress it
- Show value tooltip on hover for accessibility on dense settings pages
- Max-width 480px in single-column layout; full-width in form grids

- No Slider on TV — d-pad cannot drag a continuous thumb accurately
- Replace with a +/− button pair: two large icon buttons flanking the current value label
- Step granularity on TV: 10-unit steps for volume, 25% for brightness
- If slider must appear (e.g., playback scrubber), use left/right d-pad for 5-second seek steps with clear focus indicator

## Accessibility

Native `` carries most semantic attributes automatically. Supplement with ARIA for value labels and live updates.

| Requirement | Implementation | Notes |
|---|---|---|
| Label | `aria-label` or `` | Visible label preferred. `aria-label` only if label is visually suppressed. |
| Value range | `aria-valuemin`, `aria-valuemax`, `aria-valuenow` | Native `min`, `max`, `value` attributes map automatically — no extra ARIA needed for numeric sliders. |
| Named value | `aria-valuetext` | For step sliders with named values (Easy/Normal/Hard), add `aria-valuetext="Normal"` updated via JS so screen readers announce the name not the number. |
| Keyboard | Arrow keys native on `type="range"` | Left/Down decreases, Right/Up increases. Home = min, End = max. Never suppress default key handling. |
| Focus visibility | `:focus-visible` outline | Green 2px outline with 6px offset is visible against both dark and light surfaces. Do not suppress. |

## Related tokens

Use these tokens when implementing slider styles.

| Token | Value | Usage |
|---|---|---|
| `--jio` | `#00A859` | Thumb fill, filled track portion, live value color |
| `--surface-3` | Surface tier 3 | Unfilled track background |
| `--bg` | `#080a10` | Thumb inner border to create separation from track |
| `--pill` | `100px` | Track and thumb border-radius |
| `--text2` | `rgba(244,242,238,.55)` | Slider label text color |
| `--state-disabled-opacity` | `.38` | Disabled state opacity applied to full slider-wrap |

## When to use

Use when

- Volume, brightness, or game difficulty controls
- Price range filters in browse/shop screens
- Playback progress scrubber in media players
- Settings with continuous numeric range (not discrete steps)

Don't use when

- Precise numeric input — use Input[type=number] for exact values
- Binary choices — use Toggle instead
- More than 2 thumbs (multi-range) — too complex for most use cases
- Sliders for age or year selection — use Select or Combobox

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Thumb drag | `none` | `realtime` | transform translateX |
| Thumb press scale | `--ease-out` | `80ms` | transform scale(1.3) |
| Track fill | `none` | `realtime` | width |
| Focus ring | `instant` | `0ms` | outline on thumb |
| Value tooltip appear | `--ease-out` | `--dur-fast` | opacity, transform translateY(-4px → 0) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-slider` | Root — relative, full width, flex align-center |
| `.ds-slider__track` | Background track — 4px height, surface-2, r-pill |
| `.ds-slider__fill` | Filled portion — jio-green, same height as track |
| `.ds-slider__thumb` | 20px circle — white bg, jio border, r-pill |
| `.ds-slider__thumb:focus` | Green outline ring |
| `.ds-slider__thumb:hover` | Scale 1.1, jio glow shadow |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | number[] | required | Controlled value(s) — array for range support |
| `onValueChange` | (v: number[]) => void | required | Real-time change handler |
| `onValueCommit` | (v: number[]) => void | undefined | Fired on drag end |
| `min` | number | 0 | Minimum value |
| `max` | number | 100 | Maximum value |
| `step` | number | 1 | Increment step size |
| `disabled` | boolean | false | Disable interaction |

## Code examples

Link `tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="slider-wrap">
  <div class="slider-header">
    <label class="slider-label" for="vol">Volume</label>
    <span class="slider-value">72%</span>
  </div>
  <input
    type="range"
    id="vol"
    class="slider"
    min="0"
    max="100"
    value="72"
    aria-valuemin="0"
    aria-valuemax="100"
    aria-valuenow="72"
    aria-label="Volume"
  >
</div>
````

````html
<div class="slider-wrap">
  <div class="slider-header">
    <label class="slider-label" for="bright">Brightness</label>
    <span class="slider-value" id="bright-val">55%</span>
  </div>
  <input
    type="range"
    id="bright"
    class="slider"
    min="0" max="100" value="55"
    style="background:linear-gradient(to right,var(--jio) 55%,var(--surface-3) 55%)"
    oninput="
      const v = this.value;
      document.getElementById('bright-val').textContent = v + '%';
      this.style.background =
        'linear-gradient(to right,var(--jio) ' + v + '%,var(--surface-3) ' + v + '%)';
      this.setAttribute('aria-valuenow', v);
    "
  >
</div>
````

````
<!-- Two overlapping range inputs; JS constrains min/max to each other -->
<div class="slider-wrap" style="position:relative;">
  <div class="slider-header">
    <span class="slider-label">Price range</span>
    <span class="slider-value" id="range-display">₹0 – ₹500</span>
  </div>
  <div style="position:relative; height:20px;">
    <input type="range" id="range-min" class="slider"
      min="0" max="1000" value="0" step="50"
      style="position:absolute; width:100%; pointer-events:none;">
    <input type="range" id="range-max" class="slider"
      min="0" max="1000" value="500" step="50"
      style="position:absolute; width:100%; pointer-events:none;">
  </div>
</div>
<script>
  const rMin = document.getElementById('range-min');
  const rMax = document.getElementById('range-max');
  const display = document.getElementById('range-display');
  function update() {
    if (+rMin.value > +rMax.value) rMin.value = rMax.value;
    if (+rMax.value < +rMin.value) rMax.value = rMin.value;
    display.textContent = '₹' + rMin.value + ' – ₹' + rMax.value;
  }
  rMin.addEventListener('input', update);
  rMax.addEventListener('input', update);
</script>
````

## Changelog

Initial draft. Includes Default, Step-marks, Disabled, and Range variant documentation. Thin / Default / Thick size tiers. Five states. Platform, accessibility, and token tables. Three code examples including two-thumb range pattern.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--jio`
- `--jio-font`
- `--pill`
- `--r4`
- `--state-disabled-opacity`
- `--surface-1`
- `--surface-3`
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

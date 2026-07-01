# Textarea — JioGames DLS spec

> Source: `textarea/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Textarea

---

Multi-line text input for game reviews, support messages, and profile bios. Always resizable vertically, never horizontally.

Focused textarea with character counter · Tomb Raider review

The Textarea is a multi-line text input element. It accepts freeform text across game reviews, bug reports, player bios, and support forms. Unlike a single-line Input, the Textarea grows vertically and signals to users that a longer response is expected. Horizontal resizing is always disabled to protect layout integrity.

- **Reviews and ratings** — long-form player feedback with optional character counter
- **Profile bio** — up to 160 characters, compact height
- **Support and bug reports** — uncapped or generous limit, error state on validation failure
- **Community posts** — L size at 144px min-height, full-width on mobile

- Always pair with a visible `` — placeholder alone is not sufficient
- Show a character counter when there is a limit users need to be aware of
- Use the L size (144px) for reviews and bios; M for shorter structured inputs
- Apply `aria-invalid="true"` and `aria-describedby` on the error state
- Disable horizontal resize via `resize: vertical` to protect layout

- Use placeholder copy like "Enter text here" — write format hints instead
- Show a counter that starts at 0/500 before the user has typed — add it on first keystroke
- Allow horizontal resize — it breaks column layouts on web
- Use Textarea for single-line inputs — use Input instead
- Set `resize: none` — vertical resize is expected and helps users on web

1. 1 Label Required Visible `` element linked via `for`/`id`. Displayed above the field at 12px/500 weight. `font-size: 12px; color: var(--text2)`
2. 2 Container Required The `` element with glass-tinted background and 1.5px border. Vertically resizable. Border color changes on focus and error. `border-radius: var(--r5); resize: vertical`
3. 3 Placeholder Optional Copy that shows expected format, not just "Enter text". Disappears on first keystroke. `color: var(--text3); font-weight: 500`
4. 4 Character counter Optional Right-aligned count below the field. Turns red when over limit. Linked via `aria-describedby`. `font-size: 11px; color: var(--text3)`

## Variants

Five variants cover all standard textarea states. Each maps to a distinct visual treatment — never mix error and disabled styles.

## Sizes

Three height tiers. Match size to the expected input length — S for short structured answers, M for default, L for long-form reviews and bios.

## States

Six interactive states. The count-over-limit state works in conjunction with the error state when the user exceeds the maximum character count.

| State | Visual change | When |
|---|---|---|
| Default | Border `var(--border-subtle)` | Unfocused, no value |
| Hover | Border `var(--border)` | Pointer over field |
| Focus | Border `var(--jio)`, green glow ring | Field is active / caret visible |
| Error | Border `var(--negative)`, red hint text | Validation fails on submit or blur |
| Disabled | Opacity `var(--state-disabled-opacity)`, no events | Feature locked or read-only context |
| Count over limit | Counter text turns `var(--negative)`, border turns error red | User types past `maxlength` enforced by JS |

## Content guidance

Placeholder copy is the only editorial text in the textarea. Write it to model the expected format, not to restate the label.

- Show the *format* expected: "Share what you loved or didn't…"
- Never write "Enter text here" or "Type something"
- For reviews: "Share what you loved or didn't…"
- For bio: "Tell the JioGames community about yourself…"
- For bug reports: "Describe what happened and when…"
- Keep placeholder under 10 words — it vanishes on first keystroke

- Show counter only when there is a meaningful limit (e.g., 160 bio, 500 review)
- Display as "used / max" format: "124 / 500"
- Reveal counter on first keystroke, not on page load
- When over limit: counter turns red, submit button disables
- Error message: "Review must be under 500 characters" — never just turn the counter red with no label

## Platform considerations

Resize behavior and input method vary significantly across platforms. Textarea is a web-first component.

- Disable horizontal resize — it is the default on mobile but verify in custom implementations
- Set `inputmode="text"` to trigger the correct soft keyboard
- The field will auto-scroll into view when focused; account for keyboard offset in bottom-sheet contexts
- Use full-width layout — never constrain to less than 100% column width on mobile

- Allow vertical resize only — `resize: vertical` is the expected system behavior
- Set a `max-height` so the textarea doesn't grow to fill the viewport on long pastes
- Character counter updates on every `input` event, not just blur
- Max-width 640px in single-column document layout; full width in form contexts

- No Textarea on TV — use voice input flow or route to mobile companion app for long text
- If a physical keyboard is connected, the field renders but without resize handle (TV cursor model doesn't support drag)
- Never show character counter on TV — text is too small at 3m viewing distance

## Accessibility

Always associate a label and link error and counter messages programmatically.

| Requirement | Implementation | Notes |
|---|---|---|
| Label association | `` | Never use `placeholder` as the only label. Label must remain visible at all times. |
| Error announcement | `aria-invalid="true"` + `aria-describedby="err-id"` | The error hint element carries the full message. Screen readers announce it after the field label on focus. |
| Character counter | `aria-describedby="count-id"` + `aria-live="polite"` on counter | Counter updates must be announced without interrupting typing. Use `polite`, not `assertive`. |
| Disabled state | `disabled` attribute | Prefer `readonly` when content should be visible but not editable — disabled fields are skipped by screen readers. |
| Focus visibility | Custom focus ring via `box-shadow` | Do not suppress `:focus-visible` without a visible alternative. The green glow ring meets WCAG 2.4.11. |

## Related tokens

Use these tokens to implement textarea styles. Never hardcode hex values.

| Token | Value | Usage |
|---|---|---|
| `--input-bg` | `var(--glass-1)` | Textarea background fill |
| `--input-border` | `var(--border-subtle)` | Default border color |
| `--input-text` | `var(--text)` | User-typed text color |
| `--jio` | `#00A859` | Focus border and glow accent |
| `--negative` | `#FF4757` | Error border and over-limit counter color |
| `--r5` | Border radius tier 5 | Container border-radius |
| `--text3` | `rgba(244,242,238,.32)` | Placeholder and counter muted text |
| `--state-disabled-opacity` | `.38` | Disabled state opacity |

## When to use

Use when

- Multi-line text input: reviews, feedback, bio, description fields
- Support request forms where users describe an issue
- Game description or notes fields with long content

Don't use when

- Single-line text — use Input instead
- Rich text editing — use a dedicated rich text editor
- Code input — use a code editor component
- Fixed-height textareas that can't grow with content

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Focus ring | `instant` | `0ms` | outline |
| Auto-resize height | `--ease-out` | `--dur-fast` | height |
| Character count color shift | `--ease-out` | `--dur-fast` | color (text3 → amber → red) |
| Error message appear | `--ease-out` | `--dur-fast` | opacity, max-height |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-textarea` | Root textarea — surface-1, border-subtle, r3, padding 12px 14px |
| `.ds-textarea:focus` | Jio-green outline + border |
| `.ds-textarea--error` | Red border, error message below |
| `.ds-textarea--disabled` | 38% opacity, resize none |
| `.ds-textarea__counter` | Character count — 12px text3, text-right below |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | string | undefined | Controlled value |
| `onChange` | (e: ChangeEvent) => void | undefined | Change handler |
| `rows` | number | 3 | Initial visible row count |
| `maxLength` | number | undefined | Max character count — shows counter |
| `autoResize` | boolean | true | Grow height to fit content |
| `error` | string | boolean | undefined | Error message or boolean |
| `disabled` | boolean | false | Disable the field |

## Code examples

Link `tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="field-wrap">
  <label class="input-label" for="review">Your review</label>
  <textarea
    id="review"
    class="textarea textarea--l"
    placeholder="Share what you loved or didn't…"
    maxlength="500"
  ></textarea>
</div>
````

````html
<div class="field-wrap">
  <label class="input-label" for="bio">Profile bio</label>
  <textarea
    id="bio"
    class="textarea textarea--m"
    placeholder="Tell the JioGames community about yourself…"
    aria-describedby="bio-count"
    maxlength="160"
    oninput="
      const c = document.getElementById('bio-count');
      const n = this.value.length;
      c.textContent = n + ' / 160';
      c.classList.toggle('is-over', n > 160);
    "
  ></textarea>
  <div id="bio-count" class="textarea-count" aria-live="polite">0 / 160</div>
</div>
````

````html
<div class="field-wrap">
  <label class="input-label" for="report">Describe the issue</label>
  <textarea
    id="report"
    class="textarea is-error"
    aria-invalid="true"
    aria-describedby="report-err"
    placeholder="Describe what happened and when…"
  >This review contains banned words.</textarea>
  <div id="report-err" class="input-hint" style="color:var(--negative);">
    Your text contains restricted content. Please revise before submitting.
  </div>
</div>
````

## Changelog

Initial draft. Includes Default, Focused, Error, Disabled, and Character-count variants. S / M / L size tiers. Anatomy, platform guidance, accessibility table, and three code examples.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border`
- `--border-subtle`
- `--dur-fast`
- `--ease-out`
- `--glass-1`
- `--input-bg`
- `--input-border`
- `--input-text`
- `--jio`
- `--jio-font`
- `--negative`
- `--r5`
- `--space-2`
- `--state-disabled-opacity`
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

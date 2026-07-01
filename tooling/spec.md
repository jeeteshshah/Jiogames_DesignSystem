# Tooling — JioGames DLS spec

> Source: `tooling/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Tooling

---

Scripts and validators that keep DLS implementations consistent and production-safe.

## validate.sh — drift validator

A zero-dependency shell script that greps your CSS and HTML for DLS violations. Run it before every ship. Exit 0 = clean. Exit 1 = blocking violations.

### Usage

````
# Check a single file
bash tokens/validate.sh path/to/screen.html

# Check a directory (recursive)
bash tokens/validate.sh components/

# Strict mode — WARNs become ERRs (use before external ship)
bash tokens/validate.sh --strict path/to/screen.html

# Check current directory
bash tokens/validate.sh .
````

### 14 checks

### Strict mode (additional checks)

Activated with `--strict`. Upgrades all WARNs to ERRs and adds:

- ·HTML files missing `tokens/tokens.css` import
- ·Directories with `index.html` missing `qa-report.md`
- ·Directories with `index.html` missing `README.md`

### Expected output

````
JioGames DLS — validating drift…
────────────────────────────────
✗ ERROR  background:#000 — page bg must be --bg (#06080F), never pure black
    screens/home.html:42: background: #000000;
⚠ WARN   Raw hex literal — prefer var(--token) from tokens.css
    screens/home.html:87: color: #A8ADBA;
────────────────────────────────
✗ Blocking violations found — fix before shipping.
````

## build.py — token generator

Reads `tokens/tokens.json` and generates `tokens/tokens.css`. Run after any change to `tokens.json`.

````
# Regenerate tokens.css
python3 tokens/build.py

# Watch mode (requires watchdog: pip install watchdog)
python3 tokens/build.py --watch
````

The generated file includes: CSS custom properties, web platform overrides (`@media min-width:768px`), TV overrides (`@media min-width:1280px + min-height:720px`), reduced-motion overrides, and stack utility classes.

## version.sh — snapshot versioning

Saves named snapshots of generated screens. Useful for visual regression checks between DLS versions.

````
# Save a snapshot of a screen
bash tools/version.sh save home-screen "v1.1 rail spacing update"

# List saved snapshots
bash tools/version.sh list
````

## ci.sh — CI integration

Wraps `validate.sh` for CI pipelines. Returns non-zero on any ERR, prints structured output for log parsing.

````
# In CI (GitHub Actions, etc.)
bash tools/ci.sh path/to/screens/
````

To add DLS validation to a GitHub Actions workflow:

````
- name: DLS lint
  run: bash tokens/validate.sh --strict screens/
````

## will-change guidance

`will-change` promotes elements to their own compositor layer. Used correctly it eliminates jank on animations. Used incorrectly it wastes GPU memory and can make performance worse.

### When to use

| Element | Property | Reason |
|---|---|---|
| Bottom sheet | `will-change: transform` | Slides up on open — compositor-driven. |
| Pass card hero | `will-change: transform` | Scale on press, parallax on scroll. |
| Loading spinner | `will-change: transform` | Continuous rotation. |
| Toast | `will-change: transform, opacity` | Slide + fade in/out. |
| Skeleton shimmer | `will-change: background-position` | Continuous shimmer loop. |

### When NOT to use

### Correct pattern

````
// Add before animation
element.style.willChange = 'transform';
element.animate([{transform:'translateY(100%)'},{transform:'translateY(0)'}], {
  duration: 420, easing: 'cubic-bezier(.22,1,.36,1)'
}).onfinish = () => {
  element.style.willChange = 'auto'; // Remove after
};
````

validate.sh does not check `will-change` usage — this is a code-review concern, not a lint concern.

## Pre-commit hook

Install the pre-commit hook to run validation before every git commit on `.css` and `.html` files.

````
# Install hook
bash tools/install-hooks.sh

# The hook runs validate.sh on staged CSS/HTML files
# Commit is blocked if ERRs are found
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--border-subtle`
- `--card-sq`
- `--ctrl-h`
- `--jio`
- `--jio-font`
- `--r3`
- `--r4`
- `--status-negative`
- `--status-warning`
- `--surface-1`
- `--text`
- `--text2`
- `--token`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

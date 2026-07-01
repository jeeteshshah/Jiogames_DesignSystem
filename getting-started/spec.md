# Getting Started — JioGames DLS spec

> Source: `getting-started/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Getting Started

---

Everything an engineer or designer needs to adopt the JioGames DLS in a new project.

## What is JioGames DLS?

The JioGames Design Language System is the single source of truth for UI across Mobile, Web, and TV. It defines tokens, components, patterns, and guidelines so every team ships consistent, accessible, premium experiences without reinventing decisions.

## Installation

The DLS ships as a static CSS file. No build step, no npm package required for adoption.

### 1. Import tokens.css

Add this as the first stylesheet on every page. All CSS custom properties are declared on `:root`.

````
<link rel="stylesheet" href="/tokens/tokens.css">
````

### 2. Import components.css

Component classes live here. Only import what you need — or import the full file and rely on browser CSS opt-in.

````
<link rel="stylesheet" href="/components.css">
````

### 3. Set root styles

````
html, body {
  background: var(--bg);       /* #06080F dark base */
  color: var(--text);          /* #F4F2EE off-white */
  font-family: var(--jio-font); /* JioType, system fallback */
  margin: 0;
}
````

### 4. Platform class (TV only)

On TV surfaces, add `.platform-tv` to `` or ``. This activates TV-specific token overrides for sizing and spacing.

````
<html class="platform-tv">
````

## Three-tier token model

Never use raw hex or px values in component code. Every value must come from a token.

## First 5 components to learn

Start here before building any screen. These 5 cover 80% of JioGames surfaces.

## Platform rules overview

The DLS uses the same class names and token names on all three platforms. Platform differences are expressed through token overrides, not separate codebases.

Mobile

- Touch targets: min 44×44px (`--touch-min`)
- Gutter: 16px (`--gutter`)
- Bottom tab bar always present
- Safe area insets via `--safe-bot`
- No hover states — use active/pressed only

Web

- Gutter: 40px (`--gutter` overridden at 768px)
- Max container: 1280px (`--container-web`)
- Hover states required (`--state-hover-bg`)
- Focus ring: 2px jio-green, 2px offset
- Sidebar navigation instead of tab bar

TV

- Add `.platform-tv` to ``
- TV safe zone: 80px (`--tv-safe`)
- Focus ring: 3px + glow (`--tv-focus-shadow`)
- All interactive elements must be D-pad reachable
- 10-foot test: text must be readable at distance

## TV focus gotchas

TV is the hardest platform to get right. These are the most common mistakes.

## Copying code correctly

Code examples in this DLS show the correct HTML structure and class names. A few rules when copying:

## Requesting components and tokens

Before requesting anything new, check that it does not already exist under a different name.

## Pre-ship checklist

Run through this before every feature ship. The full release checklist lives in [Governance](../governance/).

## Font loading

JioGames DLS uses **JioType** exclusively. Correct loading prevents FOUT (flash of unstyled text) and layout shift.

### Required weights

| Weight | Name | Usage |
|---|---|---|
| 300 | Light | Large hero sub-copy, legal text. |
| 500 | Medium | Body text, captions, secondary labels. |
| 700 | Bold | Headings, section titles, CTAs. |
| 900 | Black | Hero titles, stat numbers, display text. |

Do not load 400 (Regular) or 600 (SemiBold) — DLS does not use them. Loading unused weights wastes ~60KB per variant.

### Recommended @font-face

````
@font-face {
  font-family: 'JioType';
  src: url('/fonts/JioType-Light.woff2') format('woff2');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'JioType';
  src: url('/fonts/JioType-Medium.woff2') format('woff2');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'JioType';
  src: url('/fonts/JioType-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'JioType';
  src: url('/fonts/JioType-Black.woff2') format('woff2');
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}
````

### Preload critical weights

Preload Bold and Black — they render above-the-fold hero text. Light and Medium can load normally.

````
<link rel="preload" href="/fonts/JioType-Bold.woff2"
      as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/JioType-Black.woff2"
      as="font" type="font/woff2" crossorigin>
````

### Fallback stack

````
/* Already in tokens.css */
--jio-font: 'JioType', 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
````

Outfit is the closest public fallback — similar proportions. Do not substitute Inter or Roboto.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--action-primary`
- `--amber`
- `--bg`
- `--bg2`
- `--border`
- `--border-subtle`
- `--btn-primary-bg`
- `--gold`
- `--jio`
- `--jio-font`
- `--jio-soft`
- `--positive`
- `--r2`
- `--r3`
- `--r4`
- `--r5`
- `--status-negative`
- `--status-positive`
- `--status-warning`
- `--surface-1`
- `--text`
- `--text-placeholder`
- `--text2`
- `--text3`
- `--token`
- `--tv-focus-shadow`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

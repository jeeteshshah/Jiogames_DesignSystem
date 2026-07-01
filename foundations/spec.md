# Foundations — JioGames DLS spec

> Source: `foundations/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Foundations

---

The design language behind JioGames — why we make the choices we make, how tokens flow from raw value to component, and the principles that govern every decision across Mobile, Web, and TV.

## Brand Principles

Five non-negotiables that define what JioGames looks and feels like. Violating any one of these breaks the identity.

## Product Principles

Six principles that govern product decisions — what to build, what to show, and in what order.

## Platform Principles

Each platform has a different input model, viewing distance, and interaction contract. Design for all three — not a single lowest common denominator.

- Touch targets ≥ 44px at all times
- Bottom navigation — never a sidebar
- Swipe gestures supplement tap, never replace
- Safe areas respected (notch, home indicator)
- Thumb reach zone is the hero interaction zone
- AppBar collapses on scroll — screen space is precious

- Hover states on all interactive elements
- Full keyboard navigation — Tab, arrows, Enter, Escape
- Right-click / context menus supported where appropriate
- Desktop content density is acceptable — more per screen
- Mouse precision allows smaller secondary targets (min 32px)
- AppBar is always visible — sticky at top

- D-pad only — no mouse, no touch input
- Focus ring is the sole affordance — never rely on hover
- Minimum focusable target: 60px
- Remote latency: never assume instant response
- 10-foot rule: all text ≥ 24px, all icons ≥ 32px
- No hover interactions — all states must be focus-driven

## Token Philosophy

Tokens are the bridge between design decisions and code. The system uses three layers — primitive, semantic, and component — so that a single colour change propagates everywhere it is used.

## Accessibility Principles

Accessibility is built in at the token and component level — not added after the fact. These four commitments apply to every component in the system.

## Motion Principles

Animation communicates state and creates cinematic weight. It is never decorative. Every duration and easing is a token.

## Component Maturity Model

Every component carries a maturity level. Use only Level 3 (Ready) components in production. Levels 1–2 exist for design and engineering alignment — not user-facing code.

| Level | Name | Meaning | Badge |
|---|---|---|---|
| 0 | Idea | Under discussion. Not yet designed or specified. | — |
| 1 | Draft | Design in progress. No implementation. Do not use in production. | Draft |
| 2 | Beta | Implemented and testable. Needs real usage to validate. API may change. | Beta |
| 3 | Ready | Stable. Validated in production. Safe to use across all surfaces. | Ready |
| 4 | Deprecated | Will be removed in the next major version. Migrate now. | Deprecated |

## Non-Negotiable Rules

These are hard constraints — not guidelines. Every violation degrades the system's integrity.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--pill`
- `--r3`
- `--surface-2`
- `--text3`
- `--text4`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

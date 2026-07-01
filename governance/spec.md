# Governance — JioGames DLS spec

> Source: `governance/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Governance

---

Token naming conventions, versioning policy, the process for adding new tokens, component contracts, and deprecation patterns.

RFC → REVIEW → BUILD → SHIP · SEMVER · DEPRECATION POLICY

## Contribution Process

All new components and tokens follow this four-step process. Nothing ships without completing each gate.

### RFC template

## Versioning

The DLS follows semver. Every release must include a changelog entry. Breaking changes require a migration guide in the changelog.

| Version bump | Triggers | Example |
|---|---|---|
| MAJOR | Token or component API breaking change — rename, removal, semantic meaning change | `--ctrl-h` renamed to `--btn-h-lg` |
| MINOR | New component added, new token added, new platform variant | Adding `--card-continue-progress` |
| PATCH | Bug fix, doc update, correcting a wrong token value | Fixing `--r5` from 14px to 16px |

### Deprecation policy

- Deprecated tokens and components are kept for **2 minor versions** after deprecation, with a `console.warn` in JS tooling pointing to the replacement.
- On removal (MAJOR version), the old name is kept as a CSS alias for **1 full major version** pointing to the new token: `--old-token: var(--new-token);`
- Every deprecated item gets a deprecation notice in its DLS page — yellow banner with the version it was deprecated in and the replacement name.
- Removing a token or component without a migration guide in the changelog.

## Component Maturity

Every component has a maturity status. Status gates what teams can do with it — Experimental components may change without notice.

### Maturity levels

| Status | Chip | Meaning | Can teams adopt? |
|---|---|---|---|
| Experimental | Experimental | Under active design/development. API and tokens may change without notice. No migration guarantee. | Opt-in only — expect churn |
| Ready | Ready | Stable contract, documented states, WCAG checked, TV variant specified. Safe to adopt. | Yes — stable API |
| Deprecated | Deprecated | Scheduled for removal. Replacement documented. Do not adopt in new work. | Migrate away — removal scheduled |

### How maturity appears in nav

## Token Governance

Tokens follow a strict three-tier hierarchy. Component CSS must never reference primitive tokens directly.

### Three-tier model

### Rules for new tokens

- A value warrants a token only when it is used in **3 or more** distinct places — otherwise hard-code the semantic token directly.
- Component CSS must reference Tier 2 (semantic) or Tier 3 (component) tokens only — never raw Tier 1 primitives.
- Raw hex values in component CSS — always go through a semantic token.
- Raw `px` values for controlled dimensions (radius, spacing, icon sizes) — use a spacing or radius token.
- Font family strings other than `JioType` — never reference `Outfit`, `Inter`, or any other font name in component CSS.

## Release Checklist

Every component or token release must clear all items before the version is tagged. This is the minimum bar — not a suggested shortcut list.

## Token Naming

Format: `--[category]-[property]-[modifier]`. Categories keep tokens grouped and discoverable.

## Versioning

The DLS follows semver. Breaking changes require a major bump and migration guide.

| Type | What changes | Example |
|---|---|---|
| PATCH | Bug fix, documentation update | Fixing wrong value stored in a token |
| MINOR | New component, new token added | Adding `--card-continue-progress` |
| MAJOR | Breaking: token rename or removal | `--ctrl-h` → `--btn-h-lg` |

## Adding a New Token

Follow this process to avoid token sprawl.

1. **Check primitives** — does an existing primitive already cover this? If yes, create a semantic alias pointing to it.
2. **Check semantics** — does a semantic token already exist? If yes, use it directly — do not create a duplicate.
3. **RFC** — if a new primitive is genuinely needed, open an RFC and get review from at least one other platform engineer.
4. **Document** — record name, value, purpose, and which platforms it applies to.
5. **Ship** — add to `tokens.css`, update CHANGELOG with version bump.

## Component Contract

Every shipped component must have a filled contract. This is the minimum required documentation.

|   |   |
|---|---|
| Component | Toggle |
| Status | Ready |
| Platforms | Mobile, Web |
| Touch target | 52×44px (visual 52×30px + padding) |
| Tokens | --jio, --surface-3, --text-inv |
| States | default-off, default-on, hover, focus, disabled |
| ARIA | role="switch" aria-checked="true|false" |
| TV | Not recommended — use segmented control |

## Deprecation Notice

Use this banner pattern when a token or component is deprecated but not yet removed.

## Review Checklist

Every component must pass this checklist before status is set to Ready.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border`
- `--border-subtle`
- `--error-text`
- `--jio`
- `--jio-light`
- `--jio-soft`
- `--new-token`
- `--pill`
- `--r3`
- `--r4`
- `--r5`
- `--success-text`
- `--surface-1`
- `--surface-2`
- `--surface-3`
- `--text`
- `--text2`
- `--text3`
- `--text4`
- `--warning-text`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

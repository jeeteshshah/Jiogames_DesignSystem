# Pass Cards — JioGames DLS spec

> Source: `pass-cards/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Pass Cards

---

Pass cards present JioGames subscription plans — Mobile, Ultimate, and All Screen — with pricing, benefits, and clear CTAs.

- 100+ games
- Mobile only
- Cancel anytime
- No ads

- 300+ games
- Mobile + TV + Web
- Family sharing
- No ads
- Early access

Pass cards are the primary conversion surface for JioGames subscriptions. They must communicate value clearly, highlight differentiation, and drive confident subscription decisions.

- **Three pass tiers** — Mobile, Ultimate, and All Screen — each with distinct visual treatment.
- **Current plan state** suppresses the CTA and shows a "Current plan" badge instead.
- **Expired state** uses muted treatment and a "Renew" CTA.
- **Recommended pass** gets visual emphasis via the "Most Popular" ribbon and elevated shadow.

## When to use

Use when

- Pass subscription plan selection on upsell screens
- Pass status display in account/profile settings
- Comparison between Mobile Pass and Ultimate Pass tiers
- Renewal prompts on lapsed subscriber re-engagement screens

Don't use when

- Generic marketing cards unrelated to subscription plans
- More than 2 pass tiers side by side on mobile
- Showing pricing without clearly indicating the billing period

## Best practices

Pass cards are conversion-critical. Clarity and hierarchy drive decisions — never sacrifice either for decoration.

- Lead with plan name, then price, then benefits
- Highlight the recommended plan with a "Most Popular" ribbon
- Keep benefits to 3–5 items
- Use specific CTAs ("Get Mobile Pass" not "Subscribe")
- Show current plan state clearly with a badge

- Use identical visual weight for all pass tiers
- Show price without billing period (always "₹99/month")
- List more than 5 benefits — overwhelming
- Use a generic "Subscribe" CTA
- Show expired and active plans at the same visual prominence

## Anatomy

All pass cards share the same six-slot structure. The container, plan badge, price display, benefits list, and CTA are required. The ribbon is optional.

- 100+ games
- Mobile only
- Cancel anytime

## Variants

Five variants cover all subscription contexts. Each has distinct visual treatment to communicate tier, status, and availability.

- 100+ games
- Mobile only
- No ads

- 300+ games
- All platforms
- Family sharing

- 500+ games
- All screens
- 6 profiles

## Sizes

Pass cards have two sizes. Use the full card on selection and upsell screens; use the compact card inside bottom sheets, drawers, and account summary rows.

- Min width: 280px · max width: 100% of container
- Internal padding: `var(--card-padding)` = 20px
- Border-radius: `var(--r5)`
- Used on: pass selection, upsell sheet, onboarding

- Fixed height: 72px · full width of container
- Internal padding: 12px 16px
- Border-radius: `var(--r4)`
- Used on: account summary, bottom sheet header, plan row in settings

- Min width: 360px · full card layout
- Larger text: pass name 20px, price 36px
- All interactive elements must be focus-ring navigable
- Used on: TV pass selection screen only

## States

Pass cards respond to five states. The current and recommended states use visual emphasis; expired and loading suppress or simplify the card.

## Content

Pass card copy must be precise and action-oriented. Every word affects conversion.

- ·All caps, 9px, letter-spacing 1.5px
- ·Color per tier (green / violet / violet)
- ·Never abbreviate — "Mobile Pass" not "Mobile"

- ·Large price: 32px, weight 900
- ·Always include billing period (₹99/month)
- ·Show savings badge for annual plans if applicable

- ·Present tense, action-oriented ("Play on mobile")
- ·3–5 items maximum
- ·Lead with the most differentiating benefit

- ·Default: "Get [Plan Name]"
- ·Current: "Manage plan"
- ·Expired: "Renew [Plan Name]"

## Platform considerations

Pass card layout adapts significantly across platforms. Mobile shows one card at a time; web compares side-by-side; TV uses a full-screen format.

- Full-width stacked cards, one per screen
- Swipe between plans (carousel)
- Sticky CTA at bottom
- Progress dots show plan position
- Touch target on CTA: min 54px height

- 2–3 cards side-by-side
- Max-width 480px each card
- Hover state: slight scale (1.01) + shadow
- Recommended card is visually elevated
- CTA triggers subscription flow in drawer

- Full-screen plan comparison layout
- Card width 640px for 10-foot readability
- Focus ring 3px, clearly visible
- D-pad left/right switches plans
- Selected state + focused states combined

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Card select | `--ease-out` | `--dur-fast` | border-color, box-shadow |
| Recommended badge pulse | `ease-in-out` | `2s infinite` | box-shadow scale |
| Price reveal | `--ease-out` | `--dur-base` | opacity, transform translateY(8px → 0) |
| CTA hover | `--ease-out` | `--dur-fast` | background, transform scale(1.02) |

## Platform rules

Mobile

- Full-width single card per screen or stacked vertically with 16px gap
- Recommended badge at top of card — not inside header
- CTA button: full width, primary variant, 48px height
- Price displayed large (28px 700) — key decision driver

Web

- Side-by-side two-column layout for Mobile vs. Ultimate comparison
- Hover: scale(1.02) + deeper border glow on selected card
- Feature list: max 6 items — truncate or link to full details

TV

- Full-screen upsell layout — one card per screen or vertical compare
- D-pad Up/Down navigates feature list; Left/Right switches plan
- CTA button: 64px height TV variant; prominent jio-green fill
- Price and plan name: min 28px and 24px — readable at 10 feet

## Accessibility

Pass cards present financial decisions. Every element must be correctly announced to screen reader users, with pricing clearly labeled.

- Tab — moves between plan cards and CTAs
- Enter — activates the CTA
- Focus ring 2px solid `var(--jio)`, offset 3px on CTA button

## Related tokens

Pass card visual treatment is defined via these design tokens. Tier-specific gradient and border values are set per plan.

| Token | Value | Swatch | Usage |
|---|---|---|---|
| --jio | #00A859 |   | Mobile Pass accent, benefits dot, CTA |
| --violet | #8E5BFF |   | Ultimate + All Screen Pass accent |
| --popular-gold | #F7AB20 |   | "Most Popular" ribbon background |
| --r7 | 20px | — | Pass card border-radius |
| --premium-gradient | linear-gradient(145deg, #0d0a20, #1a1040) |   | Ultimate / All Screen card background |
| --premium-border | rgba(138,91,255,.4) |   | Ultimate Pass card border |
| --premium-glow | 0 0 24px rgba(142,91,255,.25) | — | Recommended card elevated shadow |
| --negative | #FF4757 |   | "Expired" status label |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-pass-card` | Root — surface-1, border-subtle, r5, overflow hidden |
| `.ds-pass-card--mobile` | Mobile Pass — jio-green accent header |
| `.ds-pass-card--ultimate` | Ultimate Pass — gold/premium gradient header |
| `.ds-pass-card--selected` | Selected state — jio border, jio-soft bg tint |
| `.ds-pass-card__header` | Colored top section with pass name and icon |
| `.ds-pass-card__price` | Large price display — 28px 700 |
| `.ds-pass-card__features` | Feature list — bullet items |
| `.ds-pass-card__cta` | Subscribe button — full width, primary |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `tier` | "mobile" | "ultimate" | required | Pass tier |
| `price` | string | required | Formatted price string (e.g. "₹299/mo") |
| `features` | string[] | required | Feature bullet points |
| `selected` | boolean | false | Highlighted/chosen state |
| `onSelect` | () => void | undefined | Selection handler |
| `recommended` | boolean | false | Show "Recommended" badge |
| `ctaLabel` | string | "Subscribe" | CTA button text |
| `onCta` | () => void | undefined | CTA button handler |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````html
<div class="pass-mobile">
  <div class="pass-card__eyebrow">Mobile Pass</div>
  <div class="pass-card__price">
    <span class="pass-card__currency">₹</span>
    <span class="pass-card__amount">99</span>
    <span class="pass-card__period">/month</span>
  </div>
  <ul class="pass-card__perks">
    <li>Play on 1 mobile device</li>
    <li>300+ games included</li>
    <li>Cancel anytime</li>
  </ul>
  <button class="btn btn--primary btn--m btn--full">Get Mobile Pass</button>
</div>
````

````html
<div class="pass-ultimate">
  <div class="pass-card__eyebrow">
    Ultimate Pass
    <span class="upsell-popular">Most popular</span>
  </div>
  <div class="pass-card__price">
    <span class="pass-card__currency">₹</span>
    <span class="pass-card__amount">199</span>
    <span class="pass-card__period">/month</span>
  </div>
  <ul class="pass-card__perks">
    <li>Play on 5 screens</li>
    <li>Mobile + TV + Web</li>
    <li>Exclusive titles included</li>
  </ul>
  <button class="btn btn--primary btn--m btn--full">Get Ultimate Pass</button>
</div>
````

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--amber`
- `--bg`
- `--border-subtle`
- `--card-padding`
- `--gold`
- `--jio`
- `--jio-font`
- `--negative`
- `--pill`
- `--popular-gold`
- `--r4`
- `--r5`
- `--r7`
- `--surface-1`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`
- `--text4`
- `--violet`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

# JioGames Design Language System — JioGames DLS spec

> Source: `overview/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

---

[↓ Download MD](data:text/markdown;charset=utf-8;base64,IyBKaW9HYW1lcyBEZXNpZ24gTGFuZ3VhZ2UgU3lzdGVtIOKAlCBKaW9HYW1lcyBETFMgc3BlYwoKPiBTb3VyY2U6IGBvdmVydmlldy9pbmRleC5odG1sYCBpbiB0aGUgSmlvR2FtZXMgRGVzaWduIFN5c3RlbS4KPiBUaGlzIHNwZWMgaXMgZ2VuZXJhdGVkIHZlcmJhdGltIGZyb20gdGhlIHBhZ2Ug4oCUIGRvIG5vdCBpbnZlbnQgdmFsdWVzIG5vdCBsaXN0ZWQgaGVyZS4KCi0tLQoKVGhlIHNpbmdsZSBzb3VyY2Ugb2YgdHJ1dGggZm9yIEppb0dhbWVzIFVJIGFjcm9zcyBNb2JpbGUsIFdlYiwgYW5kIFRWLgoKIyMgQnVpbHQgb24gdGhyZWUgbm9uLW5lZ290aWFibGVzCgpFdmVyeSBkZWNpc2lvbiBpbiB0aGUgRExTIGZsb3dzIGZyb20gdGhlc2UgcHJpbmNpcGxlcy4gV2hlbiBpbiBkb3VidCwgcmV0dXJuIHRvIHRoZW0uCgpBbGwgc3VyZmFjZXMgYXJlIGRhcmsuIEppb0dhbWVzIGdyZWVuIGlzIHRoZSBzb2xlIGJyYW5kIGFjY2VudCDigJQgbmV2ZXIgYmx1ZSBvciBwdXJwbGUuIEV2ZXJ5IGNvbG91ciBkZWNpc2lvbiByZWluZm9yY2VzIHRoZSBnYW1pbmcgYXRtb3NwaGVyZS4KCkV2ZXJ5IGFuaW1hdGlvbiBoYXMgYSB0b2tlbi4gU3ByaW5nIGVhc2luZyBmb3IgZW50ZXJzLCBpbnN0YW50IGZvciBUViBmb2N1cy4gQW5pbWF0aW9uIG11c3QgZWFybiBpdHMgcGxhY2Ug4oCUIG5ldmVyIGZvciBpdHMgb3duIHNha2UuCgpNb2JpbGUgdG91Y2gsIFdlYiBwb2ludGVyICsga2V5Ym9hcmQsIFRWIEQtcGFkLiBFYWNoIHBsYXRmb3JtIGhhcyBpdHMgb3duIHNwYWNpbmcsIHNpemluZywgYW5kIG1vdGlvbiBydWxlcy4gTm8gb25lLXNpemUtZml0cy1hbGwuCgojIyBRdWljayByZWZlcmVuY2UKCkNvcmUgdG9rZW5zIGF0IGEgZ2xhbmNlLiBTZWUgW0NvbG91cnMg4oaSXSguLi9jb2xvdXJzLykgZm9yIHRoZSBmdWxsIHN5c3RlbS4KCiMjIENvcmUgYnVpbGRpbmcgYmxvY2tzCgpDb2xvdXIsIHR5cGUsIHNwYWNpbmcsIG1vdGlvbiDigJQgdGhlIHJhdyBtYXRlcmlhbCBldmVyeSBjb21wb25lbnQgaXMgYnVpbHQgZnJvbS4KCiMjIFByb2R1Y3Rpb24tcmVhZHkgY29tcG9uZW50cwoKQWxsIGNvbXBvbmVudHMgc2hpcCB3aXRoIHRva2VuIHNwZWNzLCBwbGF0Zm9ybSB2YXJpYW50cywgc3RhdGVzLCBhbmQgZG8vZG9uJ3QgZ3VpZGFuY2UuCgojIyBNdWx0aS1jb21wb25lbnQgVVggZmxvd3MKCkVuZC10by1lbmQgaW50ZXJhY3Rpb24gcGF0dGVybnMgYnVpbHQgZnJvbSBETFMgY29tcG9uZW50cy4gUmVmZXJlbmNlIGJlZm9yZSBkZXNpZ25pbmcgbmV3IGZsb3dzLgoKLS0tCgojIyBUb2tlbnMgcmVmZXJlbmNlZCBvbiB0aGlzIHBhZ2UKClVzZSB0aGVzZSBleGFjdCB0b2tlbnMg4oCUIGRlZmluZWQgaW4gYHRva2Vucy90b2tlbnMuY3NzYC4gRG8gbm90IHN1YnN0aXR1dGUgcmF3IHZhbHVlcy4KCi0gYC0tYmdgCi0gYC0tYm9yZGVyLXN1YnRsZWAKLSBgLS1jYXJkLWJnYAotIGAtLWppb2AKLSBgLS1qaW8tc29mdGAKLSBgLS1waWxsYAotIGAtLXIzYAotIGAtLXI1YAotIGAtLXRleHRgCi0gYC0tdGV4dDJgCi0gYC0tdGV4dDNgCi0gYC0tdGV4dDRgCgotLS0KCiMjIEJ1aWxkIHJ1bGVzIChiaW5kaW5nKQoKMS4gVXNlICoqb25seSoqIHRoZSB0b2tlbnMgbGlzdGVkIGFib3ZlLiBJZiBhIHZhbHVlIHlvdSBuZWVkIGlzIG5vdCBsaXN0ZWQsIHN0b3AgYW5kIGFzayDigJQgZG8gbm90IGludHJvZHVjZSBhIHJhdyB2YWx1ZS4KMi4gRm9udCBpcyAqKkppb1R5cGUqKiBvbmx5LiBXZWlnaHRzOiAzMDAsIDUwMCwgNzAwLCA5MDAuCjMuIFJldXNlIHRoZSBjb21wb25lbnQgQ1NTIHBhdHRlcm5zIHNob3duIG9uIHRoZSBzb3VyY2UgcGFnZTsgZG8gbm90IHJlZGVzaWduLgo0LiBNYXRjaCBldmVyeSBzdGF0ZSAoZGVmYXVsdCwgaG92ZXIsIGZvY3VzLCBhY3RpdmUsIGRpc2FibGVkLCBsb2FkaW5nKSBzaG93biBvbiB0aGUgcGFnZS4KNS4gQWNjZXNzaWJpbGl0eSByZXF1aXJlbWVudHMgb24gdGhlIHBhZ2UgYXJlIG1hbmRhdG9yeSwgbm90IG9wdGlvbmFsLgo=)

The single source of truth for JioGames UI across Mobile, Web, and TV.

## Built on three non-negotiables

Every decision in the DLS flows from these principles. When in doubt, return to them.

All surfaces are dark. JioGames green is the sole brand accent — never blue or purple. Every colour decision reinforces the gaming atmosphere.

Every animation has a token. Spring easing for enters, instant for TV focus. Animation must earn its place — never for its own sake.

Mobile touch, Web pointer + keyboard, TV D-pad. Each platform has its own spacing, sizing, and motion rules. No one-size-fits-all.

## Quick reference

Core tokens at a glance. See [Colours →](../colours/) for the full system.

## Core building blocks

Colour, type, spacing, motion — the raw material every component is built from.

## Production-ready components

All components ship with token specs, platform variants, states, and do/don't guidance.

## Multi-component UX flows

End-to-end interaction patterns built from DLS components. Reference before designing new flows.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--bg`
- `--border-subtle`
- `--card-bg`
- `--jio`
- `--jio-soft`
- `--pill`
- `--r3`
- `--r5`
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

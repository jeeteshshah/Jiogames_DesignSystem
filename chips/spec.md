# Chips — JioGames DLS spec

> Source: `chips/index.html` in the JioGames Design System.
> This spec is generated verbatim from the page — do not invent values not listed here.

**Path:** JioGames DLS › Components › Chips

---

[↓ Download MD](data:text/markdown;charset=utf-8;base64,IyBDaGlwcyDigJQgSmlvR2FtZXMgRExTIHNwZWMKCj4gU291cmNlOiBgY2hpcHMvaW5kZXguaHRtbGAgaW4gdGhlIEppb0dhbWVzIERlc2lnbiBTeXN0ZW0uCj4gVGhpcyBzcGVjIGlzIGdlbmVyYXRlZCB2ZXJiYXRpbSBmcm9tIHRoZSBwYWdlIOKAlCBkbyBub3QgaW52ZW50IHZhbHVlcyBub3QgbGlzdGVkIGhlcmUuCgoqKlBhdGg6KiogSmlvR2FtZXMgRExTIOKAuiBDb21wb25lbnRzIOKAuiBDaGlwcwoKLS0tCgpDaGlwcyBhcmUgY29tcGFjdCwgaW50ZXJhY3RpdmUgbGFiZWxzIGZvciBmaWx0ZXJpbmcsIHNlbGVjdGluZywgYW5kIGRpc3BsYXlpbmcgY2F0ZWdvcml6ZWQgY29udGVudC4KCkZpbHRlciBjaGlwcyDCtyAxOjEgc2NhbGUgYXQgTW9iaWxlIE0KCkNoaXBzIGFyZSB0aGUgcHJpbWFyeSBmaWx0ZXIgYWZmb3JkYW5jZSBpbiBKaW9HYW1lcyBob3Jpem9udGFsIHJhaWxzLiBUaGV5IGFwcGVhciBpbiBzY3JvbGxhYmxlIHJvd3MgYWJvdmUgZ2FtZSBjYXRhbG9ndWVzLCBsZXR0aW5nIHVzZXJzIG5hcnJvdyBjb250ZW50IGJ5IGdlbnJlLCBwbGF0Zm9ybSwgcHJpY2UsIG9yIG90aGVyIGF0dHJpYnV0ZXMgd2l0aG91dCBuYXZpZ2F0aW5nIGF3YXkuIFVubGlrZSBidXR0b25zLCBjaGlwcyByZXByZXNlbnQgcGVyc2lzdGVudCBzdGF0ZSDigJQgYSBzZWxlY3RlZCBjaGlwIHN0YXlzIGFjdGl2ZSB1bnRpbCBleHBsaWNpdGx5IGRpc21pc3NlZCBvciByZXBsYWNlZC4KCi0gKipGaWx0ZXIqKiDigJQgbmFycm93IGEgZ2FtZSBjYXRhbG9ndWUgYnkgZ2VucmUsIHByaWNlIHRpZXIsIG9yIHBsYXRmb3JtIGluIGEgaG9yaXpvbnRhbCBzY3JvbGwgcmFpbAotICoqU2VsZWN0Kiog4oCUIGluZGljYXRlIGEgY2hvc2VuIHByZWZlcmVuY2UgZHVyaW5nIG9uYm9hcmRpbmcgKGdlbnJlIG9yIHBsYXRmb3JtIHNlbGVjdGlvbiBmbG93cykKLSAqKlRhZyoqIOKAlCBkaXNwbGF5IG5vbi1pbnRlcmFjdGl2ZSBtZXRhZGF0YSBsYWJlbHMgb24gZ2FtZSBjYXJkcyAoZS5nLiAiRnJlZSIsICJOZXciLCAiQmV0YSIpCi0gKipSZW1vdmUqKiDigJQgbGV0IHVzZXJzIGNsZWFyIGFuIGFwcGxpZWQgZmlsdGVyIHZpYSBhIHRyYWlsaW5nIGRpc21pc3MgYnV0dG9uIG9uIHJlbW92YWJsZSBjaGlwcwoKIyMgQmVzdCBwcmFjdGljZXMKCi0gVXNlIG5vdW5zIGZvciBmaWx0ZXIgbGFiZWxzIOKAlCAiQWN0aW9uIiwgIlJhY2luZyIsICJGcmVlIHRvIHBsYXkiCi0gS2VlcCBsYWJlbHMgMeKAkzIgd29yZHMgZm9yIHNjYW5uYWJpbGl0eSBpbiBkZW5zZSByYWlscwotIEFsd2F5cyBwYWlyIGNvbG91ciBjaGFuZ2Ugd2l0aCB0ZXh0IGNvbG91ciBjaGFuZ2UgZm9yIHNlbGVjdGlvbiBzdGF0ZSAobmV2ZXIgcmVseSBvbiBjb2xvdXIgYWxvbmUpCi0gVXNlIGAuaXMtYWN0aXZlYCBmb3IgdGhlIHNlbGVjdGVkIHN0YXRlIHNvIHN0YXRlcy5jc3MgaGFuZGxlcyBhbGwgdmlzdWFsIGNoYW5nZXMKLSBNYWludGFpbiBhIG1pbmltdW0gNDRweCB0b3VjaCB0YXJnZXQgaGVpZ2h0IG9uIE1vYmlsZSB1c2luZyBpbnRlcm5hbCBwYWRkaW5nIHdoZW4gY2hpcCB2aXN1YWwgc2l6ZSBpcyBzbWFsbGVyCgotIERvbid0IHVzZSBjaGlwcyBmb3IgcHJpbWFyeSBDVEFzIOKAlCB1c2UgQnV0dG9uIGNvbXBvbmVudHMgaW5zdGVhZAotIERvbid0IHVzZSB2ZXJiIGxhYmVscyAoIkZpbHRlciBieSIsICJDaG9vc2UgZ2VucmUiKSDigJQgY2hpcHMgbmFtZSBjb250ZW50LCBub3QgYWN0aW9ucwotIERvbid0IGFsbG93IGNoaXAgbGFiZWxzIHRvIGV4Y2VlZCAyIGxpbmVzIG9mIHRleHQg4oCUIHRydW5jYXRlIHdpdGggZWxsaXBzaXMgYXQgbWF4LXdpZHRoCi0gRG9uJ3QgcmVwdXJwb3NlIGNoaXBzIGFzIG5hdmlnYXRpb24gdGFicyDigJQgdXNlIGEgVGFiIEJhciBjb21wb25lbnQgZm9yIGRlc3RpbmF0aW9uIHN3aXRjaGluZwotIERvbid0IG1peCBjaGlwIHZhcmlhbnRzIGluIHRoZSBzYW1lIGhvcml6b250YWwgcm93IChlLmcuIGZpbHRlciBjaGlwcyBhbmQgZ2VucmUgY2hpcHMgdG9nZXRoZXIpCgojIyBBbmF0b215CgpBIGNoaXAgaXMgYnVpbHQgZnJvbSB1cCB0byBmaXZlIG5hbWVkIHBhcnRzLiBDb250YWluZXIgYW5kIGxhYmVsIGFyZSBhbHdheXMgcHJlc2VudDsgbGVhZGluZyBpY29uLCB0cmFpbGluZyByZW1vdmUsIGFuZCBzZWxlY3Rpb24gaW5kaWNhdG9yIGFwcGVhciBwZXIgdmFyaWFudC4KCjEuIDEgQ29udGFpbmVyIFJlcXVpcmVkIFBpbGwtc2hhcGVkIGJvdW5kYXJ5IHdpdGggZnVsbCBib3JkZXItcmFkaXVzLiBGaWxsLCBib3JkZXIsIGFuZCBvcGFjaXR5IHNoaWZ0IGFjcm9zcyBzdGF0ZXMuIGAtLWNoaXAtYmcgwrcgLS1jaGlwLWJvcmRlciDCtyAtLXBpbGxgCjIuIDIgTGVhZGluZyBpY29uIE9wdGlvbmFsIDEy4oCTMTRweCBTVkcgaWNvbiB1c2luZyBgZmlsbDpjdXJyZW50Q29sb3JgLiBPbmx5IHByZXNlbnQgb24gYC5jaGlwLS1pY29uYCB2YXJpYW50LiBJY29uIG11c3QgYmUgZnJvbSB0aGUgRExTIGljb24gc2V0LiBgLS1jaGlwLXRleHRgCjMuIDMgTGFiZWwgdGV4dCBSZXF1aXJlZCBOb3VuLWJhc2VkIGxhYmVsLCAx4oCTMiB3b3JkcywgbWF4IDIwIGNoYXJhY3RlcnMuIE5ldmVyIHdyYXBzLiBUcnVuY2F0ZSB3aXRoIGVsbGlwc2lzIGlmIG5lY2Vzc2FyeS4gQ29sb3VyIGNoYW5nZXMgdG8gYHZhcigtLXRleHQtaW52KWAgb24gc29saWQgYHZhcigtLWppbylgIGJhY2tncm91bmQgd2hlbiBzZWxlY3RlZC4gYC0tY2hpcC10ZXh0IMK3IC0tc3RhdGUtc2VsZWN0ZWQtdGV4dGAKNC4gNCBUcmFpbGluZyBpY29uIC8gcmVtb3ZlIE9wdGlvbmFsIFJlbW92ZSBidXR0b24gKMOXKSBvbiBgLmNoaXAtLXJlbW92YWJsZWAuIE11c3QgY2FycnkgYGFyaWEtbGFiZWw9IlJlbW92ZSBbbmFtZV0iYC4gQSB0cmFpbGluZyBjaGV2cm9uIG1heSBiZSB1c2VkIG9uIGRyb3Bkb3duLXRyaWdnZXIgY2hpcHMuIGAtLWNoaXAtYm9yZGVyYAo1LiA1IFNlbGVjdGlvbiBpbmRpY2F0b3IgT3B0aW9uYWwgQWN0aXZlIHN0YXRlIHZpc3VhbCDigJQgYmFja2dyb3VuZCBhbmQgYm9yZGVyIGJlY29tZSBgdmFyKC0tamlvKWAsIHRleHQgYmVjb21lcyBgdmFyKC0tdGV4dC1pbnYpYCAoYmxhY2spLiBNYXRjaGVzIHRoZSBwcmltYXJ5IGJ1dHRvbiBmb3Igc3Ryb25nIHNlbGVjdGlvbiBhZmZvcmRhbmNlLiBgLS1qaW8gwrcgLS10ZXh0LWludmAKCiMjIFZhcmlhbnRzCgpGaXZlIGNoaXAgdmFyaWFudHMgY292ZXIgZmlsdGVyaW5nLCBzZWxlY3Rpb24sIGljb24tbGVkIGxhYmVsbGluZywgcmVtb3ZhYmxlIHRhZ3MsIGFuZCBsb2FkaW5nIHNrZWxldG9uIHVzZSBjYXNlcy4KCiMjIFNpemVzCgpGb3VyIGhlaWdodCB0aWVycyBhY3Jvc3MgdGhyZWUgcGxhdGZvcm1zLiBUViB2YWx1ZXMgYXJlIHNpZ25pZmljYW50bHkgbGFyZ2VyIGZvciBsZWdpYmlsaXR5IGF0IDEwLWZvb3Qgdmlld2luZyBkaXN0YW5jZSBhbmQgY29tZm9ydGFibGUgRC1wYWQgdGFwIHRhcmdldHMuCgojIyBTdGF0ZXMKCkFsbCBpbnRlcmFjdGl2ZSBzdGF0ZXMgYXJlIGFwcGxpZWQgdmlhIGAuaXMtKmAgaGVscGVyIGNsYXNzZXMgZnJvbSBgc3RhdGVzLmNzc2AuIE5ldmVyIGhhcmRjb2RlIHN0YXRlIGNvbG91cnMgaW5saW5lLgoKIyMgQ29udGVudCBndWlkYW5jZQoKIyMjIExhYmVsIHdyaXRpbmcKCi0gVXNlIG5vdW5zOiAiQWN0aW9uIiwgIlJhY2luZyIsICJGcmVlIHRvIHBsYXkiLCAiTXVsdGlwbGF5ZXIiCi0gMeKAkzIgd29yZHMgaXMgaWRlYWwg4oCUIDMgd29yZHMgbWF4aW11bQotIE5vIHZlcmJzOiBhdm9pZCAiRmlsdGVyIGJ5IGdlbnJlIiBvciAiQ2hvb3NlIHBsYXRmb3JtIgotIE5vIHB1bmN0dWF0aW9uOiBubyBwZXJpb2RzLCBjb21tYXMsIG9yIGV4Y2xhbWF0aW9uIG1hcmtzCi0gVGl0bGUgY2FzZSBmb3IgZ2VucmVzOyBzZW50ZW5jZSBjYXNlIGZvciBkZXNjcmlwdGl2ZSB0YWdzCi0gVHJ1bmNhdGUgd2l0aCBlbGxpcHNpcyBpZiBsYWJlbCBtdXN0IGV4Y2VlZCAyMCBjaGFyYWN0ZXJzCgojIyMgQWNjZXNzaWJpbGl0eQoKLSBVc2UgYGFyaWEtcHJlc3NlZD0idHJ1ZS9mYWxzZSJgIG9uIHRvZ2dsZSBjaGlwcyB0byBhbm5vdW5jZSBzZWxlY3RlZCBzdGF0ZQotIFJlbW92ZSBidXR0b25zIG11c3QgY2FycnkgYGFyaWEtbGFiZWw9IlJlbW92ZSBbY2hpcCBuYW1lXSJgCi0gTWluaW11bSA0NMOXNDRweCB0b3VjaCB0YXJnZXQgb24gTW9iaWxlIOKAlCB1c2UgcGFkZGluZyBvbiBzbWFsbGVyIHZpc3VhbCBzaXplcwotIE5ldmVyIHJlbHkgb24gY29sb3VyIGFsb25lIOKAlCBwYWlyIGNvbG91ciBjaGFuZ2Ugd2l0aCB0ZXh0IHdlaWdodCBvciBpY29uIGNoYW5nZQotIEljb24tb25seSBjaGlwcyBtdXN0IGNhcnJ5IGEgdmlzaWJsZSBsYWJlbCBvciBgYXJpYS1sYWJlbGAKCiMjIFBsYXRmb3JtIGNvbnNpZGVyYXRpb25zCgojIyMgTW9iaWxlCgotIENoaXBzIGxpdmUgaW4gaG9yaXpvbnRhbCBzY3JvbGwgcmFpbHMgd2l0aCBgb3ZlcmZsb3cteDphdXRvYCBhbmQgbm8gdmlzaWJsZSBzY3JvbGxiYXIKLSBUb3VjaCB0YXJnZXQgbWluaW11bSA0NHB4IOKAlCBwYWQgdmVydGljYWxseSB3aGVuIGNoaXAgdmlzdWFsIGhlaWdodCBpcyBNICgzNnB4KSBvciBzbWFsbGVyCi0gRGVmYXVsdCBzaXplIHRpZXIgaXMgTSAoMzZweCBoZWlnaHQpCi0gU3dpcGUgbW9tZW50dW0gbXVzdCBmZWVsIG5hdGl2ZSDigJQgZG8gbm90IGJsb2NrIHNjcm9sbCBwcm9wYWdhdGlvbgotIEZpcnN0IGNoaXAgaW4gYSBmaWx0ZXIgcmFpbCBpcyBhbHdheXMgIkFsbCIgaW4gYWN0aXZlIHN0YXRlCgojIyMgV2ViCgotIEFwcGx5IGBjdXJzb3I6cG9pbnRlcmAgb24gYWxsIGludGVyYWN0aXZlIGNoaXBzCi0gSG92ZXIgc3RhdGUgdmlhIGA6aG92ZXJgIHBzZXVkby1jbGFzcyBvciBgLmlzLWhvdmVyYCBmb3IgSlMtZHJpdmVuIHN0YXRlcwotIFRvb2x0aXAgdmlhIGB0aXRsZWAgYXR0cmlidXRlIHdoZW4gbGFiZWwgaXMgdHJ1bmNhdGVkCi0gV2ViIHNpemUgdGllciB1c2VzIE0gKDM2cHgpIGJ5IGRlZmF1bHQsIHNhbWUgYXMgbW9iaWxlCi0gS2V5Ym9hcmQgbmF2aWdhdGlvbjogVGFiIHRvIGZvY3VzLCBTcGFjZSBvciBFbnRlciB0byB0b2dnbGUKCiMjIyBUVgoKLSBNaW5pbXVtIHNpemUgTCAoNjhweCkg4oCUIG5ldmVyIHVzZSBYUyBvciBTIG9uIFRWCi0gRm9jdXMgcmluZyBpcyBtYW5kYXRvcnkg4oCUIHVzZSBgLS10di1mb2N1cy1yaW5nYCB0b2tlbiBmb3IgdGhlIGhpZ2gtY29udHJhc3QgZ2xvdwotIEQtcGFkIGxlZnQvcmlnaHQgbmF2aWdhdGlvbiB3aXRoaW4gY2hpcCByb3dzIHVzaW5nIGByb2xlPSJ0b29sYmFyImAKLSBTZWxlY3RlZCBzdGF0ZSBtdXN0IGJlIGNsZWFybHkgbGVnaWJsZSBhdCAxMC1mb290IHZpZXdpbmcgZGlzdGFuY2UKLSBJbmNyZWFzZSBnYXAgYmV0d2VlbiBjaGlwcyB0byAxMnB4IG1pbmltdW0gZm9yIFRWIGxheW91dHMKCiMjIEFjY2Vzc2liaWxpdHkKCkNoaXBzIG11c3QgYmUgZnVsbHkgb3BlcmFibGUgYnkga2V5Ym9hcmQsIGFzc2lzdGl2ZSB0ZWNobm9sb2d5LCBhbmQgRC1wYWQgb24gVFYuIFRoZSB0YWJsZSBiZWxvdyBzcGVjaWZpZXMgdGhlIHJlcXVpcmVkIEFSSUEgcm9sZXMgYW5kIGludGVyYWN0aW9uIG1vZGVsLgoKfCBDb25jZXJuIHwgUmVxdWlyZW1lbnQgfCBOb3RlcyB8CnwtLS18LS0tfC0tLXwKfCBSb2xlIHwgYGJ1dHRvbmAgb3IgaW5zaWRlIGBsaXN0Ym94YCB8IFVzZSBgcm9sZT0iYnV0dG9uImAgZm9yIHRvZ2dsZSBjaGlwczsgYHJvbGU9Im9wdGlvbiJgIGluc2lkZSBhIGByb2xlPSJsaXN0Ym94ImAgZm9yIHNpbmdsZS1zZWxlY3QgZmlsdGVyIHJvd3MgfAp8IFNlbGVjdGlvbiBzdGF0ZSB8IGBhcmlhLXByZXNzZWQ9InRydWV8ZmFsc2UiYCB8IEFubm91bmNlcyB0b2dnbGUgc3RhdGUgdG8gc2NyZWVuIHJlYWRlcnMgb24gZWFjaCBjaGFuZ2UuIFVwZGF0ZSBkeW5hbWljYWxseSB2aWEgSlMuIHwKfCBSZW1vdmUgYnV0dG9uIHwgYGFyaWEtbGFiZWw9IlJlbW92ZSBbbmFtZV0iYCB8IFdpdGhvdXQgYSB2aXNpYmxlIGxhYmVsLCB0aGUgw5cgYnV0dG9uIGlzIG1lYW5pbmdsZXNzIHRvIHNjcmVlbiByZWFkZXJzLiBBbHdheXMgaW5jbHVkZSB0aGUgY2hpcCBuYW1lIGluIHRoZSBsYWJlbC4gfAp8IEtleWJvYXJkIOKAlCB0b2dnbGUgfCBTcGFjZSBvciBFbnRlciB8IEJvdGgga2V5cyBtdXN0IGFjdGl2YXRlIHRoZSBjaGlwLiBEbyBub3QgaW50ZXJjZXB0IG90aGVyIGtleXMgd2l0aGluIHRoZSBjaGlwIGl0c2VsZi4gfAp8IEtleWJvYXJkIOKAlCByZW1vdmUgfCBEZWxldGUgb3IgQmFja3NwYWNlIHwgV2hlbiBmb2N1cyBpcyBvbiB0aGUgY2hpcCBjb250YWluZXIsIERlbGV0ZSByZW1vdmVzIGl0LiBXaGVuIGZvY3VzIGlzIG9uIHRoZSDDlyBidXR0b24sIEVudGVyIG9yIFNwYWNlIHJlbW92ZXMgaXQuIHwKfCBGb2N1cyB2aXNpYmxlIHwgMnB4IGBvdXRsaW5lYCB1c2luZyBgdmFyKC0tamlvKWAgfCBOZXZlciBzdXBwcmVzcyBgOmZvY3VzLXZpc2libGVgLiBUViBmb2N1cyByaW5nIG11c3QgbWVldCAzOjEgY29udHJhc3Qgb24gZGFyayBiYWNrZ3JvdW5kcy4gfAoKIyMgUmVsYXRlZCB0b2tlbnMKClRva2VuIHNldCBnb3Zlcm5pbmcgY2hpcCBhcHBlYXJhbmNlIGFjcm9zcyBhbGwgc3RhdGVzLiBSZXNvbHZlZCBmcm9tIGB0b2tlbnMvdG9rZW5zLmNzc2AuCgp8IFRva2VuIHwgVmFsdWUgfCBVc2FnZSB8CnwtLS18LS0tfC0tLXwKfCBgLS1jaGlwLW0taGAgfCAzNnB4IChtb2JpbGUpIHwgRGVmYXVsdCBoZWlnaHQg4oCUIGdhbWUgY2F0YWxvZ3VlIGZpbHRlciByb3dzIHwKfCBgLS1zdGF0ZS1zZWxlY3RlZC1iZ2AgfCB2YXIoLS1qaW8pIOKAlCAjMDBBODU5IHwgQWN0aXZlIC8gc2VsZWN0ZWQgYmFja2dyb3VuZCBmaWxsIHwKfCBgLS1zdGF0ZS1zZWxlY3RlZC1ib3JkZXJgIHwgdmFyKC0tamlvKSDigJQgIzAwQTg1OSB8IEFjdGl2ZSAvIHNlbGVjdGVkIGJvcmRlciBzdHJva2UgfAp8IGAtLWNoaXAtYmdgIHwgIzBjMGYxNCB8IENoaXAgc3VyZmFjZSDigJQgcmVzdGluZyBmaWxsIHwKfCBgLS1waWxsYCB8IDEwMHB4IHwgQm9yZGVyIHJhZGl1cyDigJQgZnVsbCBwaWxsIHJvdW5kaW5nIHwKfCBgLS1jaGlwLXhzLWgtbW9iaWxlYCB8IDI0cHggfCBYUyBoZWlnaHQgb24gbW9iaWxlIOKAlCBkZW5zZSBtZXRhZGF0YSByb3dzIHwKfCBgLS1jaGlwLXMtaC1tb2JpbGVgIHwgMzBweCB8IFMgaGVpZ2h0IG9uIG1vYmlsZSDigJQgY29tcGFjdCBmaWx0ZXIgYmFycyB8CnwgYC0tY2hpcC1sLWgtbW9iaWxlYCB8IDQ0cHggfCBMIGhlaWdodCBvbiBtb2JpbGUg4oCUIG9uYm9hcmRpbmcgcHJlZmVyZW5jZSBwaWNrZXJzIHwKfCBgLS1jaGlwLW0taC10dmAgfCA2MHB4IHwgRGVmYXVsdCBUViBoZWlnaHQg4oCUIG1lZXRzIEQtcGFkIHRhcCB0YXJnZXQgc3BlYyB8CnwgYC0tY2hpcC1sLWgtdHZgIHwgNjhweCB8IEwgaGVpZ2h0IG9uIFRWIOKAlCBnZW5yZSBwaWNrZXJzLCBwcm9taW5lbnQgZmlsdGVycyB8CnwgYC0tc3RhdGUtc2VsZWN0ZWQtdGV4dGAgfCB2YXIoLS1qaW8pIC8gIzAwQTg1OSB8IExhYmVsIGNvbG91ciBpbiBzZWxlY3RlZCBzdGF0ZSB8CgojIyBXaGVuIHRvIHVzZQoKVXNlIHdoZW4KCi0gR2VucmUgYW5kIHBsYXRmb3JtIGZpbHRlciBwaWxscyBvbiBkaXNjb3Zlcnkgc2NyZWVucwotIEFjdGl2ZSBmaWx0ZXIgdGFncyB0aGF0IGNhbiBiZSBkaXNtaXNzZWQKLSBNdWx0aS1zZWxlY3QgaW5wdXQgdmFsdWVzIHNob3duIGFzIHJlbW92YWJsZSB0YWdzCi0gU3RhdHVzIGluZGljYXRvcnMgaW5zaWRlIGxpc3QgaXRlbXMgKGlubGluZSBtZXRhZGF0YSkKCkRvbid0IHVzZSB3aGVuCgotIFByaW1hcnkgQ1RBcyDigJQgdXNlIEJ1dHRvbiBpbnN0ZWFkCi0gTG9uZyB0ZXh0IChtb3JlIHRoYW4gfjIwIGNoYXJzKSDigJQgdHJ1bmNhdGUgb3IgdXNlIGEgZGlmZmVyZW50IHBhdHRlcm4KLSBNb3JlIHRoYW4gfjEwIGNoaXBzIGluIGEgc2luZ2xlIHJvdyB3aXRob3V0IGhvcml6b250YWwgc2Nyb2xsCi0gUmVwbGFjaW5nIG5hdmlnYXRpb24gdGFicyDigJQgdXNlIFRhYiBCYXIgaW5zdGVhZAoKIyMgTW90aW9uCgp8IEludGVyYWN0aW9uIHwgRWFzaW5nIHwgRHVyYXRpb24gfCBQcm9wZXJ0eSB8CnwtLS18LS0tfC0tLXwtLS18CnwgU2VsZWN0ICh0b2dnbGUgb24pIHwgYC0tZWFzZS1vdXRgIHwgYC0tZHVyLWZhc3RgIHwgYmFja2dyb3VuZCwgYm9yZGVyLWNvbG9yLCBjb2xvciB8CnwgRGVzZWxlY3QgKHRvZ2dsZSBvZmYpIHwgYC0tZWFzZS1vdXRgIHwgYC0tZHVyLWZhc3RgIHwgYmFja2dyb3VuZCwgYm9yZGVyLWNvbG9yIHwKfCBEaXNtaXNzL3JlbW92ZSB8IGAtLWVhc2UtaW5gIHwgYC0tZHVyLWZhc3RgIHwgdHJhbnNmb3JtIHNjYWxlKDApLCBvcGFjaXR5LCBtYXgtd2lkdGggfAp8IEFwcGVhciB8IGAtLWVhc2Utb3V0YCB8IGAtLWR1ci1mYXN0YCB8IHRyYW5zZm9ybSBzY2FsZSgwLjg1IOKGkiAxKSwgb3BhY2l0eSB8CnwgUHJlc3MgfCBgLS1lYXNlLW91dGAgfCBgODBtc2AgfCB0cmFuc2Zvcm0gc2NhbGUoMC45NSkgfAoKIyMgQVBJCgojIyMgQ1NTIGNsYXNzZXMKCnwgQ2xhc3MgfCBEZXNjcmlwdGlvbiB8CnwtLS18LS0tfAp8IGAuZHMtY2hpcGAgfCBCYXNlIGNoaXAg4oCUIHBpbGwgc2hhcGUsIGJvcmRlci1zdWJ0bGUgfAp8IGAuZHMtY2hpcC0tc2VsZWN0ZWRgIHwgQWN0aXZlIHN0YXRlIOKAlCBqaW8tZ3JlZW4gZmlsbCwgd2hpdGUgdGV4dCB8CnwgYC5kcy1jaGlwLS1zbWAgfCBTbWFsbCDigJQgMjhweCBoZWlnaHQsIDEycHggZm9udCB8CnwgYC5kcy1jaGlwLS1tZGAgfCBEZWZhdWx0IOKAlCAzNnB4IGhlaWdodCwgMTNweCBmb250IHwKfCBgLmRzLWNoaXBfX2ljb25gIHwgTGVhZGluZyBpY29uIOKAlCAxNnB4LCBpbmhlcml0cyBjb2xvciB8CnwgYC5kcy1jaGlwX19kaXNtaXNzYCB8IFRyYWlsaW5nIMOXIGJ1dHRvbiDigJQgMTZweCwgb25seSBzaG93biB3aGVuIHJlbW92YWJsZSB8CgojIyMgUmVhY3QgcHJvcHMKCnwgUHJvcCB8IFR5cGUgfCBEZWZhdWx0IHwgRGVzY3JpcHRpb24gfAp8LS0tfC0tLXwtLS18LS0tfAp8IGBzZWxlY3RlZGAgfCBib29sZWFuIHwgZmFsc2UgfCBBY3RpdmUvc2VsZWN0ZWQgc3RhdGUgfAp8IGBvblNlbGVjdGAgfCAoKSA9PiB2b2lkIHwgdW5kZWZpbmVkIHwgVG9nZ2xlIGhhbmRsZXIgfAp8IGBvblJlbW92ZWAgfCAoKSA9PiB2b2lkIHwgdW5kZWZpbmVkIHwgU2hvd3Mgw5cgYnV0dG9uIGFuZCBmaXJlcyBvbiBjbGljayB8CnwgYHNpemVgIHwgInNtIiB8ICJtZCIgfCAibWQiIHwgSGVpZ2h0IHByZXNldCB8CnwgYGljb25gIHwgUmVhY3ROb2RlIHwgdW5kZWZpbmVkIHwgTGVhZGluZyBpY29uIGVsZW1lbnQgfAp8IGBkaXNhYmxlZGAgfCBib29sZWFuIHwgZmFsc2UgfCBEaXNhYmxlIGludGVyYWN0aW9uIHwKCiMjIENvZGUgZXhhbXBsZXMKCkNvcHkgdGhlc2Ugc25pcHBldHMgYXMgc3RhcnRpbmcgcG9pbnRzLiBBbHdheXMgbGluayBgdG9rZW5zL3Rva2Vucy5jc3NgLCBgY29tcG9uZW50cy5jc3NgLCBhbmQgYHN0YXRlcy5jc3NgIGJlZm9yZSB1c2luZyBjb21wb25lbnQgY2xhc3Nlcy4KCmBgYAo8IS0tIFVuc2VsZWN0ZWQgLS0+CjxidXR0b24gY2xhc3M9ImNoaXAiIHR5cGU9ImJ1dHRvbiI+QWN0aW9uPC9idXR0b24+Cgo8IS0tIFNlbGVjdGVkIC0tPgo8YnV0dG9uIGNsYXNzPSJjaGlwIGlzLXNlbGVjdGVkIiB0eXBlPSJidXR0b24iIGFyaWEtcHJlc3NlZD0idHJ1ZSI+QWR2ZW50dXJlPC9idXR0b24+CmBgYAoKYGBgCjxkaXYgcm9sZT0iZ3JvdXAiIGFyaWEtbGFiZWw9IkdlbnJlIGZpbHRlcnMiIHN0eWxlPSJkaXNwbGF5OmZsZXg7Z2FwOjhweDtvdmVyZmxvdy14OmF1dG87c2Nyb2xsYmFyLXdpZHRoOm5vbmUiPgogIDxidXR0b24gY2xhc3M9ImNoaXAgaXMtc2VsZWN0ZWQiIHR5cGU9ImJ1dHRvbiIgYXJpYS1wcmVzc2VkPSJ0cnVlIj5BbGw8L2J1dHRvbj4KICA8YnV0dG9uIGNsYXNzPSJjaGlwIiB0eXBlPSJidXR0b24iIGFyaWEtcHJlc3NlZD0iZmFsc2UiPkFjdGlvbjwvYnV0dG9uPgogIDxidXR0b24gY2xhc3M9ImNoaXAiIHR5cGU9ImJ1dHRvbiIgYXJpYS1wcmVzc2VkPSJmYWxzZSI+QWR2ZW50dXJlPC9idXR0b24+CiAgPGJ1dHRvbiBjbGFzcz0iY2hpcCIgdHlwZT0iYnV0dG9uIiBhcmlhLXByZXNzZWQ9ImZhbHNlIj5SYWNpbmc8L2J1dHRvbj4KICA8YnV0dG9uIGNsYXNzPSJjaGlwIiB0eXBlPSJidXR0b24iIGFyaWEtcHJlc3NlZD0iZmFsc2UiPlNwb3J0czwvYnV0dG9uPgo8L2Rpdj4KYGBgCgojIyBDaGFuZ2Vsb2cKCkFkZGVkIGAuaXMtYWN0aXZlYCBzdGF0ZSB0b2tlbnMgdG8gYWxpZ24gd2l0aCBzdGF0ZXMuY3NzIHYyIG5hbWluZy4gRGVwcmVjYXRlZCBgLmlzLXNlbGVjdGVkYCBjbGFzcyDigJQgdXNlIGAuaXMtYWN0aXZlYCBnb2luZyBmb3J3YXJkLiBVcGRhdGVkIGAtLXN0YXRlLXNlbGVjdGVkLWJnYCBvcGFjaXR5IGZyb20gMC4wOCB0byAwLjEyIGZvciBpbXByb3ZlZCBjb250cmFzdCBvbiBkYXJrIGJhY2tncm91bmRzLgoKSW5pdGlhbCBjb21wb25lbnQuIERlZmluZXMgZmlsdGVyLCBpY29uLCByZW1vdmFibGUsIGFuZCBza2VsZXRvbiB2YXJpYW50cy4gRXN0YWJsaXNoZXMgWFMvUy9NL0wgc2l6ZSB0aWVycyB3aXRoIHNlcGFyYXRlIHRva2VuIHZhbHVlcyBmb3IgTW9iaWxlLCBXZWIsIGFuZCBUViBwbGF0Zm9ybXMuCgotLS0KCiMjIFRva2VucyByZWZlcmVuY2VkIG9uIHRoaXMgcGFnZQoKVXNlIHRoZXNlIGV4YWN0IHRva2VucyDigJQgZGVmaW5lZCBpbiBgdG9rZW5zL3Rva2Vucy5jc3NgLiBEbyBub3Qgc3Vic3RpdHV0ZSByYXcgdmFsdWVzLgoKLSBgLS1qaW9gCi0gYC0tdGV4dGAKLSBgLS10ZXh0LWludmAKLSBgLS10ZXh0MmAKLSBgLS10ZXh0M2AKCi0tLQoKIyMgQnVpbGQgcnVsZXMgKGJpbmRpbmcpCgoxLiBVc2UgKipvbmx5KiogdGhlIHRva2VucyBsaXN0ZWQgYWJvdmUuIElmIGEgdmFsdWUgeW91IG5lZWQgaXMgbm90IGxpc3RlZCwgc3RvcCBhbmQgYXNrIOKAlCBkbyBub3QgaW50cm9kdWNlIGEgcmF3IHZhbHVlLgoyLiBGb250IGlzICoqSmlvVHlwZSoqIG9ubHkuIFdlaWdodHM6IDMwMCwgNTAwLCA3MDAsIDkwMC4KMy4gUmV1c2UgdGhlIGNvbXBvbmVudCBDU1MgcGF0dGVybnMgc2hvd24gb24gdGhlIHNvdXJjZSBwYWdlOyBkbyBub3QgcmVkZXNpZ24uCjQuIE1hdGNoIGV2ZXJ5IHN0YXRlIChkZWZhdWx0LCBob3ZlciwgZm9jdXMsIGFjdGl2ZSwgZGlzYWJsZWQsIGxvYWRpbmcpIHNob3duIG9uIHRoZSBwYWdlLgo1LiBBY2Nlc3NpYmlsaXR5IHJlcXVpcmVtZW50cyBvbiB0aGUgcGFnZSBhcmUgbWFuZGF0b3J5LCBub3Qgb3B0aW9uYWwuCg==)

Chips are compact, interactive labels for filtering, selecting, and displaying categorized content.

Filter chips · 1:1 scale at Mobile M

Chips are the primary filter affordance in JioGames horizontal rails. They appear in scrollable rows above game catalogues, letting users narrow content by genre, platform, price, or other attributes without navigating away. Unlike buttons, chips represent persistent state — a selected chip stays active until explicitly dismissed or replaced.

- **Filter** — narrow a game catalogue by genre, price tier, or platform in a horizontal scroll rail
- **Select** — indicate a chosen preference during onboarding (genre or platform selection flows)
- **Tag** — display non-interactive metadata labels on game cards (e.g. "Free", "New", "Beta")
- **Remove** — let users clear an applied filter via a trailing dismiss button on removable chips

## Best practices

- Use nouns for filter labels — "Action", "Racing", "Free to play"
- Keep labels 1–2 words for scannability in dense rails
- Always pair colour change with text colour change for selection state (never rely on colour alone)
- Use `.is-active` for the selected state so states.css handles all visual changes
- Maintain a minimum 44px touch target height on Mobile using internal padding when chip visual size is smaller

- Don't use chips for primary CTAs — use Button components instead
- Don't use verb labels ("Filter by", "Choose genre") — chips name content, not actions
- Don't allow chip labels to exceed 2 lines of text — truncate with ellipsis at max-width
- Don't repurpose chips as navigation tabs — use a Tab Bar component for destination switching
- Don't mix chip variants in the same horizontal row (e.g. filter chips and genre chips together)

## Anatomy

A chip is built from up to five named parts. Container and label are always present; leading icon, trailing remove, and selection indicator appear per variant.

1. 1 Container Required Pill-shaped boundary with full border-radius. Fill, border, and opacity shift across states. `--chip-bg · --chip-border · --pill`
2. 2 Leading icon Optional 12–14px SVG icon using `fill:currentColor`. Only present on `.chip--icon` variant. Icon must be from the DLS icon set. `--chip-text`
3. 3 Label text Required Noun-based label, 1–2 words, max 20 characters. Never wraps. Truncate with ellipsis if necessary. Colour changes to `var(--text-inv)` on solid `var(--jio)` background when selected. `--chip-text · --state-selected-text`
4. 4 Trailing icon / remove Optional Remove button (×) on `.chip--removable`. Must carry `aria-label="Remove [name]"`. A trailing chevron may be used on dropdown-trigger chips. `--chip-border`
5. 5 Selection indicator Optional Active state visual — background and border become `var(--jio)`, text becomes `var(--text-inv)` (black). Matches the primary button for strong selection affordance. `--jio · --text-inv`

## Variants

Five chip variants cover filtering, selection, icon-led labelling, removable tags, and loading skeleton use cases.

## Sizes

Four height tiers across three platforms. TV values are significantly larger for legibility at 10-foot viewing distance and comfortable D-pad tap targets.

## States

All interactive states are applied via `.is-*` helper classes from `states.css`. Never hardcode state colours inline.

## Content guidance

### Label writing

- Use nouns: "Action", "Racing", "Free to play", "Multiplayer"
- 1–2 words is ideal — 3 words maximum
- No verbs: avoid "Filter by genre" or "Choose platform"
- No punctuation: no periods, commas, or exclamation marks
- Title case for genres; sentence case for descriptive tags
- Truncate with ellipsis if label must exceed 20 characters

### Accessibility

- Use `aria-pressed="true/false"` on toggle chips to announce selected state
- Remove buttons must carry `aria-label="Remove [chip name]"`
- Minimum 44×44px touch target on Mobile — use padding on smaller visual sizes
- Never rely on colour alone — pair colour change with text weight or icon change
- Icon-only chips must carry a visible label or `aria-label`

## Platform considerations

### Mobile

- Chips live in horizontal scroll rails with `overflow-x:auto` and no visible scrollbar
- Touch target minimum 44px — pad vertically when chip visual height is M (36px) or smaller
- Default size tier is M (36px height)
- Swipe momentum must feel native — do not block scroll propagation
- First chip in a filter rail is always "All" in active state

### Web

- Apply `cursor:pointer` on all interactive chips
- Hover state via `:hover` pseudo-class or `.is-hover` for JS-driven states
- Tooltip via `title` attribute when label is truncated
- Web size tier uses M (36px) by default, same as mobile
- Keyboard navigation: Tab to focus, Space or Enter to toggle

### TV

- Minimum size L (68px) — never use XS or S on TV
- Focus ring is mandatory — use `--tv-focus-ring` token for the high-contrast glow
- D-pad left/right navigation within chip rows using `role="toolbar"`
- Selected state must be clearly legible at 10-foot viewing distance
- Increase gap between chips to 12px minimum for TV layouts

## Accessibility

Chips must be fully operable by keyboard, assistive technology, and D-pad on TV. The table below specifies the required ARIA roles and interaction model.

| Concern | Requirement | Notes |
|---|---|---|
| Role | `button` or inside `listbox` | Use `role="button"` for toggle chips; `role="option"` inside a `role="listbox"` for single-select filter rows |
| Selection state | `aria-pressed="true|false"` | Announces toggle state to screen readers on each change. Update dynamically via JS. |
| Remove button | `aria-label="Remove [name]"` | Without a visible label, the × button is meaningless to screen readers. Always include the chip name in the label. |
| Keyboard — toggle | Space or Enter | Both keys must activate the chip. Do not intercept other keys within the chip itself. |
| Keyboard — remove | Delete or Backspace | When focus is on the chip container, Delete removes it. When focus is on the × button, Enter or Space removes it. |
| Focus visible | 2px `outline` using `var(--jio)` | Never suppress `:focus-visible`. TV focus ring must meet 3:1 contrast on dark backgrounds. |

## Related tokens

Token set governing chip appearance across all states. Resolved from `tokens/tokens.css`.

| Token | Value | Usage |
|---|---|---|
| `--chip-m-h` | 36px (mobile) | Default height — game catalogue filter rows |
| `--state-selected-bg` | var(--jio) — #00A859 | Active / selected background fill |
| `--state-selected-border` | var(--jio) — #00A859 | Active / selected border stroke |
| `--chip-bg` | #0c0f14 | Chip surface — resting fill |
| `--pill` | 100px | Border radius — full pill rounding |
| `--chip-xs-h-mobile` | 24px | XS height on mobile — dense metadata rows |
| `--chip-s-h-mobile` | 30px | S height on mobile — compact filter bars |
| `--chip-l-h-mobile` | 44px | L height on mobile — onboarding preference pickers |
| `--chip-m-h-tv` | 60px | Default TV height — meets D-pad tap target spec |
| `--chip-l-h-tv` | 68px | L height on TV — genre pickers, prominent filters |
| `--state-selected-text` | var(--jio) / #00A859 | Label colour in selected state |

## When to use

Use when

- Genre and platform filter pills on discovery screens
- Active filter tags that can be dismissed
- Multi-select input values shown as removable tags
- Status indicators inside list items (inline metadata)

Don't use when

- Primary CTAs — use Button instead
- Long text (more than ~20 chars) — truncate or use a different pattern
- More than ~10 chips in a single row without horizontal scroll
- Replacing navigation tabs — use Tab Bar instead

## Motion

| Interaction | Easing | Duration | Property |
|---|---|---|---|
| Select (toggle on) | `--ease-out` | `--dur-fast` | background, border-color, color |
| Deselect (toggle off) | `--ease-out` | `--dur-fast` | background, border-color |
| Dismiss/remove | `--ease-in` | `--dur-fast` | transform scale(0), opacity, max-width |
| Appear | `--ease-out` | `--dur-fast` | transform scale(0.85 → 1), opacity |
| Press | `--ease-out` | `80ms` | transform scale(0.95) |

## API

### CSS classes

| Class | Description |
|---|---|
| `.ds-chip` | Base chip — pill shape, border-subtle |
| `.ds-chip--selected` | Active state — jio-green fill, white text |
| `.ds-chip--sm` | Small — 28px height, 12px font |
| `.ds-chip--md` | Default — 36px height, 13px font |
| `.ds-chip__icon` | Leading icon — 16px, inherits color |
| `.ds-chip__dismiss` | Trailing × button — 16px, only shown when removable |

### React props

| Prop | Type | Default | Description |
|---|---|---|---|
| `selected` | boolean | false | Active/selected state |
| `onSelect` | () => void | undefined | Toggle handler |
| `onRemove` | () => void | undefined | Shows × button and fires on click |
| `size` | "sm" | "md" | "md" | Height preset |
| `icon` | ReactNode | undefined | Leading icon element |
| `disabled` | boolean | false | Disable interaction |

## Code examples

Copy these snippets as starting points. Always link `tokens/tokens.css`, `components.css`, and `states.css` before using component classes.

````
<!-- Unselected -->
<button class="chip" type="button">Action</button>

<!-- Selected -->
<button class="chip is-selected" type="button" aria-pressed="true">Adventure</button>
````

````html
<div role="group" aria-label="Genre filters" style="display:flex;gap:8px;overflow-x:auto;scrollbar-width:none">
  <button class="chip is-selected" type="button" aria-pressed="true">All</button>
  <button class="chip" type="button" aria-pressed="false">Action</button>
  <button class="chip" type="button" aria-pressed="false">Adventure</button>
  <button class="chip" type="button" aria-pressed="false">Racing</button>
  <button class="chip" type="button" aria-pressed="false">Sports</button>
</div>
````

## Changelog

Added `.is-active` state tokens to align with states.css v2 naming. Deprecated `.is-selected` class — use `.is-active` going forward. Updated `--state-selected-bg` opacity from 0.08 to 0.12 for improved contrast on dark backgrounds.

Initial component. Defines filter, icon, removable, and skeleton variants. Establishes XS/S/M/L size tiers with separate token values for Mobile, Web, and TV platforms.

---

## Tokens referenced on this page

Use these exact tokens — defined in `tokens/tokens.css`. Do not substitute raw values.

- `--jio`
- `--text`
- `--text-inv`
- `--text2`
- `--text3`

---

## Build rules (binding)

1. Use **only** the tokens listed above. If a value you need is not listed, stop and ask — do not introduce a raw value.
2. Font is **JioType** only. Weights: 300, 500, 700, 900.
3. Reuse the component CSS patterns shown on the source page; do not redesign.
4. Match every state (default, hover, focus, active, disabled, loading) shown on the page.
5. Accessibility requirements on the page are mandatory, not optional.

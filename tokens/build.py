#!/usr/bin/env python3
"""
JioGames DLS — tokens/build.py
Reads tokens.json → writes tokens.css

Usage:
  python3 tokens/build.py
  python3 tokens/build.py --watch      # rebuild on file change (requires watchdog)
"""

import json, sys, os, textwrap
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
SRC  = ROOT / "tokens.json"
OUT  = ROOT / "tokens.css"


# ── Helpers ──────────────────────────────────────────────────────────────────

def css_var(name, value, indent=2):
    return " " * indent + f"--{name}: {value};"

def section(title):
    bar = "=" * 60
    return f"\n/* {bar}\n   {title}\n   {bar} */\n"

def subsection(title):
    return f"\n  /* ── {title} ── */"


# ── Font faces ───────────────────────────────────────────────────────────────

FONT_FACES = textwrap.dedent("""\
    @font-face { font-family:'JioType'; src:url('../font/JioType-Light.ttf'); font-weight:300; font-display:swap; }
    @font-face { font-family:'JioType'; src:url('../font/JioType-LightItalic.ttf'); font-weight:300; font-style:italic; font-display:swap; }
    @font-face { font-family:'JioType'; src:url('../font/JioType-Medium.ttf'); font-weight:500; font-display:swap; }
    @font-face { font-family:'JioType'; src:url('../font/JioType-MediumItalic.ttf'); font-weight:500; font-style:italic; font-display:swap; }
    @font-face { font-family:'JioType'; src:url('../font/JioType-Bold.ttf'); font-weight:700; font-display:swap; }
    @font-face { font-family:'JioType'; src:url('../font/JioType-Black.ttf'); font-weight:900; font-display:swap; }
""")


# ── Builders ─────────────────────────────────────────────────────────────────

def build_color(d):
    lines = [subsection("Brand green")]
    for k, v in d.items():
        if k.startswith("_comment"):
            label = v.replace("Brand green","Brand green").strip()
            lines.append(subsection(label))
            continue
        lines.append(css_var(k, v))
    return lines

def build_spacing(d):
    lines = [subsection("Spacing scale (8px base)")]
    for k, v in d.items():
        lines.append(css_var(f"space-{k}", v))
    return lines

def build_semantic_spacing(d):
    lines = [subsection("Semantic spacing aliases (mobile base; see @media below)")]
    for k, v in d.items():
        if k.startswith("_"): continue
        alias = "rail-gap" if k == "section-gap" else None
        lines.append(css_var(k, v))
        if alias:
            lines.append(css_var(alias, f"var(--{k})"))
    return lines

def build_radius(d):
    lines = [subsection("Radius")]
    for k, v in d.items():
        lines.append(css_var(k, v))
    return lines

def build_layout(d):
    lines = [subsection("Layout / grid")]
    for k, v in d.items():
        lines.append(css_var(k, v))
    lines.append(css_var("safe-top", "env(safe-area-inset-top, 0px)"))
    lines.append(css_var("safe-bot", "env(safe-area-inset-bottom, 0px)"))
    return lines

def build_z_index(d):
    lines = [subsection("Z-index scale — stacking order")]
    for k, v in d.items():
        if k.startswith("_"): continue
        lines.append(css_var(f"z-{k}", v))
    return lines

def build_size(d):
    lines = [subsection("Control sizes (mobile base; TV overrides via @media)")]
    for k, v in d.items():
        if k.startswith("_"): continue
        lines.append(css_var(k, v))
    return lines

def build_font(d):
    lines = [subsection("Font")]
    lines.append(css_var("jio-font", d["family"]))
    return lines

def build_motion(d):
    lines = [subsection("Motion — easing")]
    for k, v in d["easing"].items():
        lines.append(css_var(k, v))
    lines.append(subsection("Motion — duration (use tokens; raw ms only inside approved keyframe recipes)"))
    for k, v in d["duration"].items():
        lines.append(css_var(f"dur-{k}", v))
    lines.append(css_var("stagger-start", d["stagger"]["start"]))
    lines.append(css_var("stagger-step",  d["stagger"]["step"]))
    if "distance" in d:
        lines.append(subsection("Motion — movement distance (translate offsets; use var(--move-*) in keyframes)"))
        for k, v in d["distance"].items():
            lines.append(css_var(f"move-{k}", v))
    if "scale" in d:
        lines.append(subsection("Motion — interactive scale (governed feedback; never exceed — see motion.md §8)"))
        for k, v in d["scale"].items():
            lines.append(css_var(f"scale-{k}", v))
    return lines

def build_semantic(d):
    lines = []

    focus = d["focus"]
    lines += [
        subsection("Focus ring"),
        css_var("focus-ring-color",  focus["ring-color"]),
        css_var("focus-ring-width",  focus["ring-width"]),
        css_var("focus-ring-offset", focus["ring-offset"]),
        css_var("focus-ring-tv",     focus["ring-tv"]),
        css_var("focus-glow-tv",     focus["glow-tv"]),
    ]

    btn = d["button"]
    lines += [subsection("Button tokens")]
    for k, v in btn.items():
        lines.append(css_var(f"btn-{k}", v))

    lines += [subsection("Button heights (deprecated — use platform-aware aliases)")]
    legacy = [("h-xs","28px"),("h-sm","36px"),("h-md","44px"),("h-lg","54px"),("h-xl","64px"),("h-tv","72px")]
    for k, v in legacy:
        lines.append(css_var(f"btn-{k}", v))

    card = d["card"]
    lines += [subsection("Card tokens")]
    for k, v in card.items():
        lines.append(css_var(f"card-{k}", v))

    inp = d["input"]
    lines += [subsection("Input/form tokens")]
    for k, v in inp.items():
        lines.append(css_var(f"input-{k}", v))

    surf = d["surface"]
    lines += [subsection("Surface semantics")]
    for k, v in surf.items():
        lines.append(css_var(f"surface-{k}", v))

    txt = d["text"]
    lines += [subsection("Text semantics")]
    for k, v in txt.items():
        lines.append(css_var(f"text-{k}", v))

    shad = d["shadow"]
    lines += [subsection("Elevation shadows")]
    for k, v in shad.items():
        lines.append(css_var(f"shadow-{k}", v))

    foc = d["focus-state"]
    lines += [subsection("State: Focus")]
    lines.append(css_var("focus-shadow",      foc["shadow"]))
    lines.append(css_var("tv-focus-ring-color",foc["tv-ring-color"]))
    lines.append(css_var("tv-focus-shadow",   foc["tv-shadow"]))
    lines.append(css_var("tv-focus-scale",    foc["tv-scale"]))

    st = d["state"]
    lines += [subsection("State: Hover")]
    for k in ("hover-bg","hover-border","hover-text"):
        lines.append(css_var(f"state-{k}", st[k]))
    lines += [subsection("State: Pressed")]
    for k in ("pressed-bg","pressed-scale","pressed-opacity"):
        lines.append(css_var(f"state-{k}", st[k]))
    lines += [subsection("State: Selected")]
    for k in ("selected-bg","selected-border","selected-text"):
        lines.append(css_var(f"state-{k}", st[k]))
    lines += [subsection("State: Disabled")]
    for k in ("disabled-bg","disabled-border","disabled-text","disabled-opacity"):
        lines.append(css_var(f"state-{k}", st[k]))
    lines += [subsection("State: Loading")]
    lines.append(css_var("state-loading-bg", st["loading-bg"]))

    sp = d["spinner"]
    lines += [subsection("State: Loading — spinner")]
    for k, v in sp.items():
        lines.append(css_var(f"spinner-{k}", v))

    for state_name, prefix in [("success","success"),("warning","warning"),("error","error"),("destructive","destructive"),("premium","premium")]:
        s = d[state_name]
        lines.append(subsection(f"State: {state_name.title()}"))
        for k, v in s.items():
            lines.append(css_var(f"{prefix}-{k}" if k != "color" else prefix, v))

    lock = d["locked"]
    lines += [subsection("State: Locked / Unavailable")]
    lines.append(css_var("locked-bg",           lock["bg"]))
    lines.append(css_var("locked-overlay",       lock["overlay"]))
    lines.append(css_var("unavailable-opacity",  lock["unavailable-opacity"]))
    lines.append(css_var("unavailable-overlay",  lock["unavailable-overlay"]))

    sk = d["skeleton"]
    lines += [subsection("State: Skeleton")]
    for k, v in sk.items():
        lines.append(css_var(f"skeleton-{k}", v))

    ov = d["overlay"]
    lines += [subsection("Overlays")]
    for k, v in ov.items():
        lines.append(css_var(f"overlay-{k}", v))

    if "status" in d:
        lines += [subsection("Status tokens — decoupled from brand (use these in components, not --jio directly)")]
        for k, v in d["status"].items():
            if k.startswith("_"): continue
            lines.append(css_var(f"status-{k}", v))

    if "action" in d:
        lines += [subsection("Action tokens — semantic layer over brand (use --action-primary, not --jio, in interactive components)")]
        for k, v in d["action"].items():
            if k.startswith("_"): continue
            lines.append(css_var(f"action-{k}", v))

    return lines


def build_platform_size(d):
    sizes = ["xs","s","m","l","xl"]
    lines = []

    btn = d["button"]
    for dim, var_name in [("height","h"),("padding","px"),("fontSize","fs")]:
        for sz in sizes:
            for plat in ("mobile","web","tv"):
                val = btn[dim][plat].get(sz)
                if val:
                    lines.append(css_var(f"btn-{sz}-{var_name}-{plat}", val))

    icon = d["icon"]
    for dim, var_name in [("size",""),("wrap","wrap-")]:
        for sz in sizes:
            for plat in ("mobile","web","tv"):
                val = icon[dim][plat].get(sz)
                if val:
                    pfx = f"icon-{var_name}{sz}-{plat}"
                    lines.append(css_var(pfx, val))

    inp = d["input"]["height"]
    for sz in ("s","m","l"):
        for plat in ("mobile","web","tv"):
            lines.append(css_var(f"input-{sz}-h-{plat}", inp[plat][sz]))

    chip = d["chip"]["height"]
    for sz in ("xs","s","m","l"):
        for plat in ("mobile","web","tv"):
            lines.append(css_var(f"chip-{sz}-h-{plat}", chip[plat][sz]))

    # Runtime aliases (default = mobile)
    lines += [subsection("Runtime aliases (default = mobile)")]
    for sz in sizes:
        for var_name in ("h","px","fs"):
            lines.append(css_var(f"btn-{sz}-{var_name}", f"var(--btn-{sz}-{var_name}-mobile)"))
    for sz in sizes:
        lines.append(css_var(f"icon-{sz}",      f"var(--icon-{sz}-mobile)"))
        lines.append(css_var(f"icon-wrap-{sz}", f"var(--icon-wrap-{sz}-mobile)"))
    for sz in ("s","m","l"):
        lines.append(css_var(f"input-{sz}-h", f"var(--input-{sz}-h-mobile)"))
    for sz in ("xs","s","m","l"):
        lines.append(css_var(f"chip-{sz}-h", f"var(--chip-{sz}-h-mobile)"))

    return lines


def build_web_overrides(data):
    sp = data["semanticSpacing"]["_web"]
    ps = data["platformSize"]
    sizes = ["xs","s","m","l","xl"]
    lines = ["\n/* ── Web platform overrides ── */"]
    lines.append("@media (min-width: 768px) {")
    lines.append("  :root {")
    for k, v in sp.items():
        alias = "rail-gap" if k == "section-gap" else None
        lines.append(css_var(k, v, 4))
        if alias:
            lines.append(css_var(alias, f"var(--{k})", 4))
    for sz in sizes:
        for var_name in ("h","px","fs"):
            lines.append(css_var(f"btn-{sz}-{var_name}", f"var(--btn-{sz}-{var_name}-web)", 4))
    for sz in sizes:
        lines.append(css_var(f"icon-{sz}",      f"var(--icon-{sz}-web)", 4))
        lines.append(css_var(f"icon-wrap-{sz}", f"var(--icon-wrap-{sz}-web)", 4))
    for sz in ("s","m","l"):
        lines.append(css_var(f"input-{sz}-h", f"var(--input-{sz}-h-web)", 4))
    for sz in ("xs","s","m","l"):
        lines.append(css_var(f"chip-{sz}-h", f"var(--chip-{sz}-h-web)", 4))
    lines.append("  }")
    lines.append("}")
    return lines


def build_tv_overrides(data):
    sp  = data["semanticSpacing"]["_tv"]
    sz  = data["size"]["_tv"]
    ps  = data["platformSize"]
    sizes = ["xs","s","m","l","xl"]
    lines = ["\n/* ── TV semantic overrides ── */"]
    lines.append("@media (min-width: 1280px) and (min-height: 720px) {")
    lines.append("  :root {")
    for k, v in sp.items():
        alias = "rail-gap" if k == "section-gap" else None
        lines.append(css_var(k, v, 4))
        if alias:
            lines.append(css_var(alias, f"var(--{k})", 4))
    for k, v in sz.items():
        lines.append(css_var(k, v, 4))
    lines.append("    --focus-ring-width: 3px;")
    lines.append("    --focus-ring-offset: 4px;")
    lines.append("    --icon-wrap-touch: var(--icon-wrap-tv);")
    lines.append("    --input-h: var(--btn-m-h);")
    lines.append("  }")
    lines.append("}")

    lines += ["\n/* ── TV platform overrides (class-based) ── */"]
    lines.append("/* Add .platform-tv to <html> or <body> in TV contexts */")
    lines.append(".platform-tv {")
    for sz_name in sizes:
        for var_name in ("h","px","fs"):
            lines.append(css_var(f"btn-{sz_name}-{var_name}", f"var(--btn-{sz_name}-{var_name}-tv)", 2))
    for sz_name in sizes:
        lines.append(css_var(f"icon-{sz_name}",      f"var(--icon-{sz_name}-tv)", 2))
        lines.append(css_var(f"icon-wrap-{sz_name}", f"var(--icon-wrap-{sz_name}-tv)", 2))
    for sz_name in ("s","m","l"):
        lines.append(css_var(f"input-{sz_name}-h", f"var(--input-{sz_name}-h-tv)", 2))
    for sz_name in ("xs","s","m","l"):
        lines.append(css_var(f"chip-{sz_name}-h", f"var(--chip-{sz_name}-h-tv)", 2))
    lines.append("  --focus-ring-width: 3px;")
    lines.append("  --focus-ring-offset: 4px;")
    lines.append("}")
    return lines


REDUCED_MOTION = textwrap.dedent("""\

    @media (prefers-reduced-motion: reduce) {
      :root {
        --dur-instant: 0ms; --dur-fast: 0ms; --dur-default: 0ms; --dur-tv-enter: 0ms;
        --dur-pop: 0ms; --dur-slow: 0ms; --dur-error: 0ms;
        --dur-enter: 0ms; --dur-screen: 0ms; --dur-sheet: 100ms;
      }
      /* Ambient loops must be stopped in component CSS — tokens alone cannot pause infinite animations. */
      /* See motion.md §11 for ambient, shimmer, and stagger reduced-motion patterns. */
    }
""")

STACK_UTILITIES = textwrap.dedent("""\

    /* ============================================================
       Stack utilities — vertical rhythm from parent gap, not child margins.
       ============================================================ */
    .page-stack { display: flex; flex-direction: column; gap: var(--section-gap); }  /* major sections */
    .hero-stack { display: flex; flex-direction: column; gap: var(--hero-gap); }  /* hero / major break */
    .component-stack { display: flex; flex-direction: column; gap: var(--component-padding); }  /* components in a section */
    .content-stack { display: flex; flex-direction: column; gap: var(--space-1-5); }  /* related elements (title+body) */
    .tight-stack { display: flex; flex-direction: column; gap: var(--space-1); }  /* tight group (label+value) */
""")


# ── Main ─────────────────────────────────────────────────────────────────────

COMPAT_ALIASES = textwrap.dedent("""\

    /* ============================================================
       COMPATIBILITY ALIASES
       Legacy/variant token names still referenced by some doc pages.
       Each maps to its canonical token so pages render correctly.
       Prefer the canonical name in new work.
       ============================================================ */
    :root {
      --bg2: #0e1118;                 /* legacy dark surface — = --sheet-bg */
      --dur-base: var(--dur-default);  /* legacy duration name */
      --dur-skeleton: var(--dur-shimmer);
      --jio-light: var(--jio-bright);  /* legacy bright-green name */
      --ctrl-h-tv: 72px;               /* TV primary-button height */
      --violet: var(--ultimate);       /* on-brand: Ultimate-tier accent is green, never purple */
    }
""")

def build():
    with open(SRC) as f:
        data = json.load(f)

    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    header = textwrap.dedent(f"""\
        /* ============================================================
           JioGames DLS — tokens.css
           GENERATED by tokens/build.py from tokens.json. DO NOT EDIT.
           Run: python3 tokens/build.py
           Generated: {now}
           ============================================================ */
    """)

    root_lines = []
    root_lines += build_color(data["color"])
    root_lines += build_spacing(data["spacing"])
    root_lines += build_semantic_spacing(data["semanticSpacing"])
    root_lines += build_radius(data["radius"])
    root_lines += build_layout(data["layout"])
    root_lines += build_z_index(data.get("zIndex", {}))
    root_lines += build_size(data["size"])
    root_lines += build_font(data["font"])
    root_lines += build_motion(data["motion"])

    sem_section  = section("SEMANTIC TOKENS\n   Purpose-named tokens that map to primitives.\n   Change the semantic token; components update automatically.")
    sem_lines    = build_semantic(data["semantic"])

    ps_section   = section("PLATFORM-AWARE SIZE SYSTEM\n   Principle: size names (xs/s/m/l/xl) describe HIERARCHY.\n   Platform determines actual pixel values via media query / wrapper.\n   Never use platform name as a size name.")
    ps_lines     = build_platform_size(data["platformSize"])

    # Compose
    out = header + "\n"
    out += FONT_FACES + "\n"
    out += ":root {\n"
    out += "\n".join(root_lines)
    out += "\n}\n"
    out += sem_section
    out += ":root {\n"
    out += "\n".join(sem_lines)
    out += "\n}\n"
    out += ps_section
    out += ":root {\n"
    out += "\n".join(ps_lines)
    out += "\n}\n"
    out += "\n".join(build_web_overrides(data))
    out += "\n"
    out += "\n".join(build_tv_overrides(data))
    out += "\n"
    out += REDUCED_MOTION
    out += COMPAT_ALIASES
    out += STACK_UTILITIES

    with open(OUT, "w") as f:
        f.write(out)

    print(f"✓ tokens.css written ({OUT.stat().st_size // 1024}KB) — {now}")


def watch():
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("Install watchdog: pip install watchdog")
        sys.exit(1)

    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path.endswith("tokens.json"):
                print("Change detected, rebuilding…")
                try:
                    build()
                except Exception as e:
                    print(f"Error: {e}")

    build()
    obs = Observer()
    obs.schedule(Handler(), str(ROOT), recursive=False)
    obs.start()
    print(f"Watching {SRC} — Ctrl-C to stop")
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obs.stop()
    obs.join()


if __name__ == "__main__":
    if "--watch" in sys.argv:
        watch()
    else:
        build()

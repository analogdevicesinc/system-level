# adi-figure CSS reference

The styles consumed by every diagram this skill produces are defined in
`docs/_static/custom.css` under `.svg svg.adi-figure { ... }`, with
matching dark-mode overrides under `body.dark .svg svg.adi-figure` and
`@media (prefers-color-scheme: dark) { body:not(.light) .svg svg.adi-figure { ... } }`.

This file is a quick reference; the source of truth is the CSS file
itself.

## CSS variables

Use these via `fill="var(--adi-...)"` or `stroke="var(--adi-...)"` in
SVG attributes — *never* hardcode hex colours. The variables resolve to
different values in light vs. dark mode automatically.

### Surfaces and structure

| Variable | Light | Dark | Use for |
|---|---|---|---|
| `--adi-panel-bg` | cream | dark navy | Outer panel rect fill |
| `--adi-panel-stroke` | warm grey | desaturated navy | Outer panel rect stroke |
| `--adi-panel-label` | warm grey-brown | light grey | Panel-label / sublabel text colour |
| `--adi-box-stroke` | warm beige | mid-grey | Default stroke on `.box` rects |
| `--adi-dot-fill` | cream | dark navy | Inner fill of `.dot` circles |

### Text

| Variable | Light | Dark | Use for |
|---|---|---|---|
| `--adi-text-strong` | near-black | near-white | Primary box titles (`.box-text`) |
| `--adi-text` | dark warm grey | light grey | Body text |
| `--adi-text-muted` | medium grey | medium grey | Descriptions (`.box-desc`), notes |

### Arrows / accents

| Variable | Light | Dark | Use for |
|---|---|---|---|
| `--adi-arrow` | warm grey | medium-cool grey | Arrow stroke + arrowhead fill |
| `--adi-accent` | muted blue | lighter muted blue | `.accent-arrow` / `.accent-text` |
| `--adi-good-text` | sage green | sage green | "Strengths" / positive list items |
| `--adi-warn-text` | dusty rose | dusty rose | "Weaknesses" / warning list items |

### Semantic fills

These map a meaning to a hue. Pick by *role*, not just by colour you
like — that's how dark-mode preserves the palette correctly.

| Variable | Hue (light) | Use for |
|---|---|---|
| `--adi-fill-hw` | peach | ADI silicon, signal-chain hardware, ADCs/DACs |
| `--adi-fill-hw-alt` | mint | Alternate hardware / DUT |
| `--adi-fill-mcu` | warm yellow | FPGA SoC, processor, MCU compute platform |
| `--adi-fill-hdl` | green | HDL, firmware, no-OS, kernel drivers |
| `--adi-fill-drv` | blue | Drivers, libiio, hardware-abstraction libraries |
| `--adi-fill-app` | lavender | Applications, end-user code |
| `--adi-fill-app-alt` | rose | Alternate application / emphasis |
| `--adi-fill-info` | light blue | Network bar, host PC, generic info |
| `--adi-fill-note` | yellow note | Highlighted side-note / call-out |
| `--adi-fill-note-warm` | warm cream | Alternate note |
| `--adi-fill-good` | light green | Strengths / positive |
| `--adi-fill-warn` | rose | Weaknesses / warning |
| `--adi-fill-muted` | neutral beige | "Not applicable", placeholder, disabled |
| `--adi-fill-blank` | white | Sub-panel cards inside the cream panel |

### DataX scope band

| Variable | Light | Dark | Use for |
|---|---|---|---|
| `--adi-datax-bg` | very light blue | dark slate-blue | `.adi-datax-band` rect fill |
| `--adi-datax-stroke` | desaturated blue | mid slate-blue | `.adi-datax-band` rect stroke |
| `--adi-datax-label` | deep blue-grey | light slate-blue | `.adi-datax-label` text fill |

## Helper classes

Apply via `class="..."` on the matching SVG element type.

### Panel and titles

| Class | On | What it does |
|---|---|---|
| `.adi-panel` | `<rect>` | Cream panel — fill, stroke, 1.25 px |
| `.adi-panel-label` | `<text>` | Top-left panel label, 13 px, semibold |
| `.adi-panel-sublabel` | `<text>` | Subtitle under the panel-label, 11 px |
| `.adi-title` | `<text>` | Centred main title, 18 px, semibold |
| `.adi-subtitle` | `<text>` | Centred subtitle under `.adi-title`, 13 px |
| `.adi-section-label` | `<text>` | Section / column label, 11 px semibold uppercase-ish |

### Layer / column captions

| Class | On | What it does |
|---|---|---|
| `.layer-label` | `<text>` | Small left-margin caption ("Layer 1", "Layer 2", ...) |
| `.section-label` | `<text>` | Section caption — same style as `.adi-section-label` |

### Boxes and arrows

| Class | On | What it does |
|---|---|---|
| `.box` | `<rect>` | Generic box: stroke 1.25 px from `--adi-box-stroke` |
| `.box-text` | `<text>` | Box title, 13 px, semibold |
| `.box-desc` | `<text>` | Box description, 11 px, muted |
| `.arrow` | `<line>` / `<path>` | Standard slim arrow body, 1.5 px |
| `.arrow-label` | `<text>` | Italic 10 px label sitting next to an arrow |
| `.accent-arrow` | `<line>` / `<path>` | Accented arrow, 1.75 px in `--adi-accent` |
| `.accent-text` | `<text>` | Text in `--adi-accent` |
| `.good-text` | `<text>` | Text in `--adi-good-text` |
| `.warn-text` | `<text>` | Text in `--adi-warn-text` |
| `.note-text` | `<text>` | Italic 11 px footer note |
| `.dot` | `<circle>` | Small "joint" circle on an arrow start |

### Markers (arrowheads)

Markers are SVG-level definitions, not classes. Define inside `<defs>`,
reference with `marker-end="url(#<id>)"`. The polygon inside the marker
gets a class so its fill follows the theme.

| Class | On | What it does |
|---|---|---|
| `.arrowhead-fill` | `<polygon>` inside `<marker>` | Fill of the standard arrowhead |
| `.accent-arrowhead-fill` | `<polygon>` inside `<marker>` | Fill of the accent arrowhead |

### DataX scope band

| Class | On | What it does |
|---|---|---|
| `.adi-datax-band` | `<rect>` | Tinted blue overlay; place BEFORE the boxes it wraps |
| `.adi-datax-label` | `<text>` | Rotated "ADI DataX™" label on the band's left edge |

## Composition cheatsheet

Putting it together — the standard skeleton for a diagram in this style:

```xml
<svg xmlns="..." class="adi-figure no-background"
     viewBox="0 0 W H"
     width="100%" style="max-width: <px>; height: auto;">
  <defs>
    <marker id="<stem>-arrowhead"
            markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" class="arrowhead-fill"/>
    </marker>
  </defs>

  <rect x="..." y="..." width="..." height="..." rx="14" class="adi-panel"/>
  <text x="..." y="..." class="adi-panel-label">…</text>
  <text x="..." y="..." class="adi-panel-sublabel">…</text>

  <!-- (optional) DataX band BEFORE the boxes it wraps -->
  <rect x="..." y="..." width="..." height="..." rx="10" class="adi-datax-band"/>
  <text … class="adi-datax-label" transform="rotate(-90 cx cy)">ADI DataX™</text>

  <!-- Content boxes -->
  <rect class="box" fill="var(--adi-fill-hw)" .../>
  <text class="box-text" text-anchor="middle" …>Title</text>
  <text class="box-desc" text-anchor="middle" …>Description</text>

  <!-- Arrows between -->
  <line class="arrow" marker-end="url(#<stem>-arrowhead)" .../>
</svg>
```

## Why follow these conventions

- **Dark mode**: every fill, stroke, and text colour is a CSS variable
  with a dark-mode override. Hardcoded hex breaks dark mode.
- **Theme migration**: if the palette is ever retuned (e.g. a new brand
  refresh), one CSS edit propagates everywhere — diagrams stay in step.
- **Cosmic theme white-background bug**: the `no-background` class is
  the documented opt-out for the cosmic theme rule
  (`harmonic/style/element.scss`, lines 175–177) that puts a white
  background on every dark-mode SVG. Without it, the SVG renders inside
  a white card on a dark page.
- **Marker isolation**: per-diagram unique marker ids (`<stem>-arrowhead`)
  avoid cross-figure leakage when multiple diagrams render on the same
  Sphinx page. A second `<marker id="arrowhead">` would shadow the
  first.

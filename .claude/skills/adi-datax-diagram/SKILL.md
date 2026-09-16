---
name: adi-datax-diagram
description: Create SVG diagrams in the ADI DataX / overview-section style — cream panel, soft pastel boxes, slim arrows, dark-mode-aware via the repo's shared CSS palette. Invoke this whenever you need to add or edit a diagram for docs/overview/, docs/index.rst, or any page that uses the `.. svg::` directive in this repo. Triggers on phrases like "create overview diagram", "draw a stack diagram", "make an adi/datax diagram", "datax-style diagram", "diagram in the overview style", "add a diagram showing X" when working on docs/overview/* or docs/index.rst, "draw the layered architecture for Y", or anyone asking for a new SVG to drop into the docs. Prefer this skill over hand-rolling SVGs from scratch — it bakes in the conventions (no-background class, CSS-variable fills, slim arrowheads, lowercase filenames) that the rest of the section relies on.
---

# adi-datax-diagram

Build SVG diagrams that match the visual style we use across `docs/overview/`
and `docs/ecosystem-intro.svg` — cream-panel container, soft pastel fills via
shared CSS variables, slim 1.25 px strokes, slim 8×8 arrowhead markers, dark
text on light fills, light/dark theme-aware automatically.

This skill writes only the `.svg` file. It does *not* update the including
`.rst` — the caller should embed the result with the `.. svg::` directive
described below.

## When to use

Use this skill any time you would otherwise write an `<svg>` blob from
scratch for the docs. It's especially right when:

- The diagram lives under `docs/overview/`, `docs/ecosystem-intro.svg`, or
  any page that uses the `.. svg::` directive.
- You're illustrating a stack, a layered architecture, a workflow, a set
  of tracks converging into a release/integration, or a side-by-side
  comparison.
- The diagram needs to render correctly in both light and dark modes
  (the cosmic theme has a default rule that puts a white background on
  every SVG in dark mode unless we opt out).

## What this skill produces

A single `.svg` file at a path the caller chose, written in the conventions
the rest of the overview section uses. The caller embeds it in an `.rst`
page; this skill does not modify `.rst` files.

## Workflow

Steps to follow when invoked:

1. **Pick a template** that matches the layout the user wants (see
   "Templates" below). Read the template file from `templates/` to use as
   a starting point.
2. **Choose a filename**: lowercase, kebab-case, descriptive
   (e.g. `device-bringup.svg`, `release-tracks.svg`). The CI lint at
   `.github/scripts/case.py` rejects uppercase filenames.
3. **Pick a save path** that's co-located with the page that will embed
   it (e.g. a workflow diagram for `docs/overview/workflows.rst` goes in
   `docs/overview/`). Confirm with the user if unclear. Don't write to
   `docs/_build/`.
4. **Customise the template** — change the title/sublabel, adjust
   `viewBox` height to fit the content, swap placeholder boxes for the
   real ones, retarget arrow coordinates, replace the marker `id` with
   one unique to this diagram (`<diagram-name>-arrowhead`).
5. **Tell the caller how to embed it.** Show the `.. svg::` snippet they
   need to paste, with the right relative path and a short caption.
6. **Mention the rebuild gotcha.** The `.. svg::` directive opens the
   file directly and doesn't register it as a Sphinx dependency, so
   editing only the SVG won't trigger the watch server to rebuild — the
   caller has to `touch` the including `.rst` (or run `make clean`).

## Required root-element conventions

Every SVG produced with this skill must include these on the root `<svg>`:

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     class="adi-figure no-background"
     viewBox="0 0 W H"
     width="100%"
     style="max-width: <px>; height: auto;">
```

Why each piece matters:

- `class="adi-figure"` — opts into the shared palette and helper classes
  defined in `docs/_static/custom.css`. Without it, every CSS variable
  is unset and you'll get unstyled black-on-white.
- `class="... no-background"` — the cosmic theme has a rule that puts a
  white background on every SVG in dark mode unless this class is set.
  Without it, the SVG turns into a white card on the dark page.
- `viewBox` — gives the diagram an intrinsic aspect ratio so it can scale
  responsively.
- `width="100%"` + inline `max-width` — combined with `viewBox`, the SVG
  fills its container up to the cap and scales down on narrow viewports.
  Pick `max-width` based on the diagram width: 680 px for compact stacks,
  880 px for wider workflows.

## Setting the rendered width

The `.. svg::` directive does **not** accept a `:width:` option (its
`option_spec` only declares `align`). Width has to live with the SVG
itself or be applied via CSS. Three ways, in order of preference:

**1. On the SVG root (preferred, per-diagram).** Edit the SVG's own
`width` and `style="max-width: ..."`:

```xml
<svg ... viewBox="0 0 800 540"
        width="100%"
        style="max-width: 680px; height: auto;">
```

The pair (`width="100%"` + a `max-width` cap + `viewBox` for aspect
ratio) gives a diagram that fills its column up to the cap and scales
down on narrow viewports. Use `max-width: <px>` for a hard cap, or
`max-width: 90%` if you want the diagram to always leave breathing room
inside the content column regardless of how wide the column gets. Keep
the size with the file so the diagram travels predictably when reused.

**2. Per-class CSS rule** (when you want to override without editing
every SVG). Tag the SVG with a custom class on its root:

```xml
<svg ... class="adi-figure no-background tight">
```

Then in `docs/_static/custom.css`:

```css
.svg svg.adi-figure.tight { max-width: 520px; }
```

Useful when several diagrams should share an overridden cap, or when a
diagram needs different sizes between pages but you don't want to fork
the SVG.

**3. Wrap with a sized container.** The `.. svg::` directive emits the
SVG inside a `<div class="svg">`. Wrap the directive in a Sphinx
container to constrain just one placement without touching the SVG:

```rst
.. container:: narrow-figure

   .. svg:: my-diagram.svg
      :align: center

      Caption text.
```

```css
.narrow-figure .svg svg { max-width: 520px; }
```

Reach for option 1 first. Options 2 and 3 are escape hatches when the
same SVG needs to render at different sizes on different pages.

## Available palette and helper classes

Use CSS variables for every fill, stroke, and text colour — never
hardcode hex. Variables and classes are defined in
`docs/_static/custom.css` under `.svg svg.adi-figure { ... }`, with
matching dark-mode overrides under `body.dark` and
`@media (prefers-color-scheme: dark)`.

Quick palette reference (full reference in `references/css-classes.md`):

| Variable | Meaning | Use for |
|---|---|---|
| `--adi-panel-bg` / `--adi-panel-stroke` | Cream container | Outer panel rect |
| `--adi-fill-hw` | Peach | ADI hardware / silicon |
| `--adi-fill-mcu` | Warm yellow | FPGA, processor, MCU |
| `--adi-fill-hdl` | Green | HDL, firmware, no-OS |
| `--adi-fill-drv` | Blue | Drivers, libiio |
| `--adi-fill-app` | Lavender | Applications |
| `--adi-fill-info` | Light blue | Network, host, generic info |
| `--adi-fill-note` | Yellow note | Highlighted note / call-out |
| `--adi-fill-good` / `--adi-fill-warn` | Green / rose | Strengths / weaknesses |
| `--adi-fill-muted` | Neutral beige | "Not applicable" cells |

Helper classes (apply to the right element type):

- `.adi-panel` (rect) — the cream container
- `.adi-panel-label` / `.adi-panel-sublabel` (text) — top-left labels
- `.adi-title` / `.adi-subtitle` (text) — centred main titles
- `.adi-section-label` / `.layer-label` (text) — small labels for
  columns or layer captions
- `.box` (rect) — generic content box (1.25 px stroke)
- `.box-text` (text) — bold caption inside a box
- `.box-desc` (text) — secondary description
- `.arrow` (line / path) — slim 1.5 px arrow body
- `.arrow-label` (text) — italic label sitting next to an arrow
- `.accent-arrow` (line / path) — accented arrow for cross-section
  transitions
- `.note-text` (text) — small italic bottom note
- `.dot` (circle) — small "joint" circle on an arrow start
- `.arrowhead-fill` (polygon inside `<marker>`) — fill for the standard
  arrowhead
- `.accent-arrowhead-fill` — fill for the accent arrowhead
- `.adi-datax-band` (rect) + `.adi-datax-label` (text) — optional blue
  overlay that wraps the DataX-scoped boxes (see "DataX scope band"
  below)

## Markers

Each SVG defines its own arrow marker so multiple diagrams on the same
page don't collide. Use the diagram's filename stem as the prefix:

```xml
<defs>
  <marker id="<stem>-arrowhead"
          markerWidth="8" markerHeight="8"
          refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" class="arrowhead-fill" />
  </marker>
</defs>
```

Then on each `<line>` / `<path>`: `marker-end="url(#<stem>-arrowhead)"`.

## Templates

Pick the closest match and customise. All templates render correctly out
of the box.

| Template | Pattern | Read example |
|---|---|---|
| `templates/stack.svg` | Vertical stack of boxes joined by arrows | `docs/ecosystem-intro.svg`, `docs/overview/architecture-layers.svg` |
| `templates/two-column.svg` | Two sub-panels side by side, connected by a dashed cross-section arrow | `docs/overview/libiio-architecture.svg`, `docs/overview/workflow-linux-noos.svg` |
| `templates/convergence.svg` | Two or more horizontal tracks converging into a single integration row at the bottom | `docs/overview/versioning-tracks.svg` |
| `templates/workflow.svg` | Vertically stacked layers with `Layer N` labels in the left margin | `docs/overview/workflow-fpga.svg`, `workflow-mcu.svg`, `workflow-rpi.svg`, `workflow-remote.svg`, `workflow-hil.svg` |

For more complex layouts (e.g. multiple sub-panels with internal arrows
and side-notes like `docs/overview/dataflow-ad4080.svg`), start from the
closest template and grow it — these patterns compose.

## DataX scope band (optional)

When the diagram covers more than just DataX components — i.e. the user's
application above and / or physical signal-chain hardware below — wrap
the DataX-scoped subset in a blue band with a rotated label, matching
the official ADI DataX architecture diagram:

```xml
<!-- Place BEFORE the boxes it wraps so it sits behind them -->
<rect x="<x>" y="<y>" width="<w>" height="<h>" rx="10"
      class="adi-datax-band"/>
<text x="<x+26>" y="<y+h/2>"
      class="adi-datax-label" text-anchor="middle"
      transform="rotate(-90 <x+26> <y+h/2>)">ADI DataX™</text>
```

Examples in the repo: `docs/ecosystem-intro.svg`,
`docs/overview/architecture-layers.svg`,
`docs/overview/libiio-architecture.svg`.

## Embedding the SVG in an .rst page

This skill does not edit `.rst` files. After writing the SVG, tell the
caller exactly what to paste:

```rst
.. svg:: <relative-or-absolute-path>.svg
   :align: center

   Short caption that names what the diagram shows.
```

Use `.. svg::`, **not** `.. figure::` or `.. image::`. The `.. svg::`
directive (defined in the `adi_doctools` Sphinx extension) inlines the
SVG as raw HTML so the page CSS reaches it and class-based theming
works. `.. figure::` would emit a separate `<img>` tag isolated from
page CSS, and would re-introduce the dark-mode white-background bug.

## Rebuild gotcha

The `.. svg::` directive `open()`s the SVG file directly and does **not**
register it as a Sphinx dependency. That means editing only the `.svg`
file does not trigger an `adoc serve` rebuild. Three ways to force the
rebuild after SVG-only edits, in order of preference:

- **Run `make svg-watch` in a second terminal** alongside `adoc serve`.
  It polls every 0.5 s and `touch`es the including `.rst` whenever any
  `.svg` under `docs/` changes. Set-and-forget for the whole editing
  session; no per-edit action needed. (Source:
  `docs/svg-watch.py`.)
- `touch` the including `.rst` file by hand. Fine for a one-off edit.
- `(cd docs && make clean && make html)` for a from-scratch build —
  use when CSS or env-cache state has also drifted.

Mention `make svg-watch` to the caller in the final hand-off so they
aren't confused when the live server seems to be ignoring their changes.

## Filename conventions

- Lowercase, kebab-case (`hdl-shared-usage.svg`, `release-tracks.svg`).
- Descriptive of the diagram's content, not its position
  (`device-bringup.svg`, not `figure3.svg`).
- Co-locate with the page that embeds it — a diagram referenced by
  `docs/overview/architecture.rst` lives in `docs/overview/`. The
  `.. svg::` argument can then be a bare filename rather than a long
  relative path.
- `.github/scripts/case.py` runs in CI and fails the build on uppercase
  filenames, so always lowercase the file before saving.

## Worked example

> User: "Add a diagram for the new ad7191 evaluation flow on the
> components page — three layers: ADC at the bottom, no-OS firmware in
> the middle, host application on top, with the no-OS layer marked as
> DataX scope."

1. Pick template: `templates/stack.svg` (vertical 3-box stack — closest
   to the request; could also start from `templates/workflow.svg` if
   layer labels are wanted in the margin).
2. Filename: `ad7191-eval-flow.svg`.
3. Save under `docs/overview/` (co-located with `components.rst`).
4. Customise: change box count from 4 to 3, swap titles
   ("AD7191" / "no-OS firmware" / "Host application"), set fills to
   `--adi-fill-hw` / `--adi-fill-hdl` / `--adi-fill-app`, rename the
   marker id to `ad7191-eval-flow-arrowhead`, adjust the viewBox height
   accordingly.
5. Wrap the no-OS firmware box in a `.adi-datax-band` rect (placed
   behind it in source order) with a rotated `ADI DataX™` label.
6. Hand off to the caller with the `.. svg:: ad7191-eval-flow.svg` snippet
   and the rebuild reminder.

## Bundled resources

- `templates/stack.svg` — vertical stack, 4 boxes with arrows + dots.
- `templates/two-column.svg` — two side-by-side sub-panels with a dashed
  cross-section arrow.
- `templates/convergence.svg` — multi-track convergence into one
  integration row.
- `templates/workflow.svg` — layered workflow with `Layer N` margin
  labels and an inline software-stack box.
- `references/css-classes.md` — full table of every CSS variable and
  helper class with notes on when to use each.

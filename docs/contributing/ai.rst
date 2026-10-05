AI Usage
========

For information on Analog Devices Inc. stance on AI usage, please see
:adi:`Responsible AI @ ADI <en/who-we-are/legal-and-risk-oversight/responsible-ai.html>`.

AI tools are most useful when they are connected to the same sources of truth
and validation paths that engineers already use: documentation, command-line
tools, tests, builds, hardware interfaces, and code review. This page describes
how ADI exposes that context to coding assistants and what a coding harness
adds on top of a language model.

Tooling for AI-assisted work
----------------------------

A large language model can explain, draft, and connect ideas quickly, but it is
not a substitute for project knowledge or validation. The value comes from
placing the model in a workflow where it can inspect a code base, call the
right tools, read the documentation, and report verified results.

We utilize two complementary mechanisms to achieve this:

- **MCP Servers** exposes tools and data through the Model Context Protocol.
  By coupling context with assertion, they allow the system to dynamically
  steer theagent toward optimal tool usage on the fly.
- **Skills** package task-specific instructions and tool inventories as text
  files. They teach the agent how to utilize tools and execute tasks without
  forcing tight coupling or rigid hooks.

A foundational design choice is our CLI-first stance: every tool available to
the MCP is also accessible via the CLI. This ensures that frequent tasks can be
automated programmatically and sustainably.

MCP servers and skills
~~~~~~~~~~~~~~~~~~~~~~

Our set of MCPs and Skills include:

- :external+doctools:ref:`doctools MCP <mcp>`:
  Searches ADI public documentation under
  https://analogdevicesinc.github.io and https://wiki.analog.com.

- :external+pyadi-iio:doc:`pyadi-iio MCP <mcp/index>`:
  Interacts with hardware at runtime. It exposes tools for device discovery,
  connection management, property configuration, data capture, and signal
  generation across supported device classes.

- :external+pyadi-dt:doc:`pyadi-dt MCP <mcp_server>`:
  Exposes device tree generation, linting, and inspection tools.

- :external+pyadi-jif:doc:`pyadi-jif MCP <mcp_server>`:
  Provides a programmatic interface to pyadi-jif, including JESD mode queries
  and system-level solving.

- :external+genalyzer:doc:`genalyzer MCP <mcp/index>`:
  Exposes spectral and code-density analysis tools. Tools cover all five
  genalyzer analysis domains — Fourier, histogram, DNL, INL, and time-domain
  waveform — plus generators and a quantizer for end-to-end
  simulate-and-verify workflows.

- :git+scopy:`Scopy skills <tools/scopy_dev_plugin/skills/scopy-tools-inventory/SKILL.md>`:
  Catalogs Scopy development tools such as the package generator, test tools,
  CI scripts, format and license checks, and development plugin commands.

We believe documentation is part of the code base and that assistants should
have access to it just like users have.

Besides using the :external+doctools:ref:`doctools MCP <mcp>`, public
documentation sources can be fetched directly, for example, the source for this
page is :git+system-level:`raw+docs/contributing/ai.rst`. Each rendered page
also provides a ``Copy content`` button that copies the page as Markdown, which
uses :git+doctools:`adi_doctools/theme/harmonic/scripts/html2md.js`; the MCP
uses :git+doctools:`adi_doctools/cli/aux_html2md.py` to convert with Python.

The coding harness
------------------

A coding harness is the software layer that wraps a LLM. It interfaces the
model, manages context usage and compaction, summarizes tools in the context,
and employs observability and recovery strategies.

To ensure  quality, we build the coding harness to be:

- **Honest**: the agent describes the validation steps it took.
- **Accurate**: tools to verify implementations and claims.
- **Useful**: fixes are delivered as patches that a developer can inspect and apply.

.. figure:: images/agentic-loop.svg
   :width: 800px
   :class: no-background

During a session, the harness can inject context, steer tool use, and employ
multiple models with different roles. Since we collect the collateral generated
by the run, including tool output and the agent session, the result can be
reviewed. If something goes wrong, the interaction can be traced back to the
step that introduced the issue.

Examples of coding harnesses are `pi.dev <https://pi.dev>`__,
`OpenCode <https://opencode.ai>`__, `Claude Code <https://claude.com/product/claude-code>`__,
and `OpenAI codex <https://openai.com/codex/>`__.

Jagged frontier and context
~~~~~~~~~~~~~~~~~~~~~~~~~~~

LLMs are prediction models with attention: Attention constructs weighted graphs
between tokens for every single forward pass. At scale, enables cognitive-like
behaviour emerges. However, models are incredible at creating perfectly
coherent narratives, which may be factually incorrect.

LLMs perform well on tasks within the jagged technology frontier, the uneven
boundary where the model excels at. A study shows that subjects using AI
completed 12.2% more tasks and finished 25.1% faster on tasks inside the model
capabilities frontier, but were 19% less likely to produce correct solutions on
complex tasks
(`Dell'Acqua et al., 2023 <https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf>`__).

Another study shows that performance also degrades over long sessions: frontier
models corrupt roughly 25% of document content by the end of ~20-iteration
workflows, with an extra 3–6% loss per tool call at 2–5× the token cost.
Non-compliance accounts for only ~3% of failures; the dominant causes are tool
misuse and mistake propagation between rounds
(`Laban, 2026 <https://arxiv.org/pdf/2604.15597>`__ pre-print).

To mitigate this nature of the model, we ensure the quality of the context and
tools available for the model, with careful analysis of sessions.

Pull request reviewer
---------------------

The pull request reviewer is an AI-assisted reviewer integrated into CI/CD. It
uses the tooling present in each workflow to provide contextual feedback on
pull requests: builds, static analysis, style validation, checks, and any other
project-specific tool that is meaningful for the code base.

It supports models from multiple vendors, cloud-hosted or self-hosted. The tool
does not approve or merge code; final decisions remain with our reviewers, and
there is always a human-in-the-loop. It enables resolving repetitive review
work early and leave humans with a smaller, better-described problems.

How it works
~~~~~~~~~~~~

On dispatch, the agent runs in a read-only environment, compiles the code base,
and validates issues and fixes against the actual build output. It then posts
annotated feedback as a GitHub Summary with downloadable git patches and the
agent session.

.. figure:: images/llm-run.svg

   LLM run example.

Usage
~~~~~

Access is available to any user with write access to the ``analogdevicesinc``
GitHub organization. For third-party pull requests, an ADI developer can
request a review on your behalf.

The workflow is included in each repository.

.. tip::

   Adding the ``llm review`` label on the pull request also triggers the llm
   review.

Go to
``github.com/analogdevicesinc/<repository>/actions/workflows/llm.yml``
(for example, :git+system-level:`actions/workflows/llm.yml <actions/workflows/llm.yml+>`
for this repository), click ``Run workflow``, and enter the pull request number,
branch, or Git SHA to review.

.. svg:: images/llm-dispatch.svg

   How to dispatch a LLM run.

Optional inputs include additional prompt instructions and model size selection.
The default prompt is defined in ``.github/workflows/llm.yml`` of each
repository, for example :git+system-level:`.github/workflows/llm.yml`.
The LLM front-end used is `pi.dev <https://pi.dev/>`__.

Once finished, the GitHub Summary contains the review, and the run artifacts
include git patches with suggested changes and a session file to continue
locally. An example run is available
:git+system-level:`here <actions/runs/24085972371+>`.

You can download and apply all patches in one go with
:git+doctools:`apply-patches.sh <ci/scripts/apply-patches.sh>`:

.. shell::

   $ apply-patches --repo=system-level 123456789

One liner to install:

.. shell::

   $ curl -fSsL \
     "https://raw.githubusercontent.com/analogdevicesinc/doctools/refs/heads/main/ci/scripts/apply-patches.sh" \
       -o ~/.local/bin/apply-patches.sh && \
     grep -q "/apply-patches.sh" ~/.bashrc || echo "source ~/.local/bin/apply-patches.sh" >> $_ ; . $_

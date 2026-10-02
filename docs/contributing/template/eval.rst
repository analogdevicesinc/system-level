Evaluation Boards
=================

Evaluation boards pages compile all content related to an evaluation board,
from the hardware overview, features, kit contents, hardware, user guides,
developer guides, and source code.

A top-level template is available at
:git-system-level:`docs/solutions/reference-designs/template/_index.rst`
(:ref:`rendered <template eval>`).
Please pay attention to the comments only visible on the source code,
and remove them as you follow the template.

Base page structure
-------------------

Evaluation boards pages are divided into five main sections:

* Overview
* User Guide
* Developer Overview
* Developer Guide
* Help and Support

The evaluation board begins with an overview of the board, similar to the first
paragraph at :adi:`analog.com </>`.

The Overview section provides key points about the evaluation board to help the
user understand it and choose the ideal solution (baremetal or Linux?, hard core
or FPGA-based?, etc.).

Then, cover key features, evaluation board kit contents, required equipment,
hardware overview (all generic to all carriers).

The "User Guide" section contains guides aimed at users, including those without
deep technical knowledge. Start with the most plug-and-play solution,
gradually diving deeper into technical aspects.
If something is too technical, save it for the "Developer Overview" or
"Developer Guide" sections.

The "Developer Overview" section should provide all technical details that a
developer may want to know and summarize and link all source code and
documentation available.
It's essential to leverage the :external+doctools:ref:`role git` and
:external+doctools:ref:`in-org-ref`.
Avoid using full URL paths, as they make consistency checks difficult.

Similar to the "User Guide" section, the "Developer Guide" section contains
guides but aimed at developers! Here is where you can really dive deep into the
details and complex parts.
However, make sure not to duplicate content already present on other pages,
especially external ones.
For example, the no-OS drivers' source repository already contains a page
explaining the driver details.
These developer guides should focus on intricate details of using the evaluation
board with the solutions.

Finally, the last section "Help and Support" contains generic information and
links, but you can still add help/support information related to your particular
evaluation board.

Simplify the base structure
---------------------------

Some evaluation boards are simpler than others, and may not require splitting
content into subpages.

If the evaluation board in question does not contain or need a developer guide,
then the "Developer Guides" section can be removed, and the "Developer Overview"
renamed simply to "Developers" with pointers to the source code.

Additionally, if there is only one carrier and user guide, the user guide can be
integrated into the main page, replacing the carrier-agnostic paragraphs with
the carrier-specific details.

An example of this structure is :ref:`eval-adxl355-pmdz`.
A more complex example is :ref:`eval-ad4052-ardz`.

Structure Rationale
-------------------

This structure aims at minimizing content repetition, clearly defining the
boundaries between "Plug&Play" solutions and highly-technical developer resources,
and ensuring consistent linking to the source code and related documentation.

It also enables generating custom documentations with only the pertinent content
for the evaluation board, such as using Doctools'
:external+doctools:ref:`custom-doc` with the following YAML file:

.. code:: yaml

   project: "EVAL-AD4052-ARDZ"
   description: "Evaluating the AD4050/AD4052 Compact, Low Power, 12-Bit/16-Bit, 2 MSPS Easy Drive SAR ADCs"

   include:
     - system-level/eval/user-guide/adc/ad4052-ardz
     - system-level/linux/drivers/iio-adc/ad4052
     - hdl/projects/ad4052_ardz
     - no-OS/drivers/ad405x.rst
     - no-OS/projects/ad405x.rst

   entry-point:
     - caption:
       files:
         - system-level/eval/user-guide/adc/ad4052-ardz/index.rst
     - caption: HDL Design
       files:
         - hdl/projects/ad4052_ardz/index.rst
     - caption: Linux IIO Driver
       files:
         - system-level/linux/drivers/iio-adc/ad4052/index.rst
     - caption: no-OS Driver&Project
       files:
         - no-OS/projects/ad405x.rst
         - no-OS/drivers/ad405x.rst

Produces a concise and resourceful user guide.

:orphan:

ADSP SoM and Carrier Board Templates
================================================================================

This directory contains the templates for the ADSP system-on-module (SoM)
reference designs. Each reference design is one combination of a SoM and a
carrier board, for example the EV-SC846-SOM on the EV-SOMCRR2-EZKIT. A SoM can
be used on several carrier boards and a carrier board can host several SoMs, so
the content of each board is kept in one data file and shared by all its
combinations.

Overview
--------------------------------------------------------------------------------

.. code-block:: text

   reference-designs/
   ├── template/adsp/
   │   ├── boards/                    # One data file per board
   │   │   ├── ev-sc846-som.yaml
   │   │   └── ev-somcrr2-ezkit.yaml
   │   ├── images/                    # Board pictures, shared by all pages
   │   ├── index.rst.jinja            # Combination templates
   │   ├── prerequisites.rst.jinja
   │   ├── quickstart.rst.jinja
   │   ├── user-guide.rst.jinja
   │   ├── board-overview.rst.jinja   # Board templates
   │   ├── documents.rst.jinja
   │   ├── som-hardware.rst.jinja
   │   ├── som-setup.rst.jinja
   │   ├── carrier-hardware.rst.jinja
   │   └── carrier-setup.rst.jinja
   └── ev-sc846-som-ev-somcrr2-ezkit/ # One directory per combination
       ├── combination.yaml
       ├── index.rst
       ├── prerequisites.rst
       ├── quickstart.rst
       └── user-guide.rst

The pages of a combination only include the combination templates, with the
data from ``combination.yaml``:

.. code-block:: rst

   .. include-template:: ../template/adsp/index.rst.jinja
      :file: combination.yaml

The combination templates include the board templates, with the data from
``boards/<som>.yaml`` and ``boards/<carrier>.yaml``. The ``include-template``
directive takes the data of a single file, so every board template only uses
the data of one board.

Board identifiers are the lowercase board names, as used in the analog.com
product page URLs. The templates derive the board names, with ``upper``, and
the product page URLs from them.

Adding a combination
--------------------------------------------------------------------------------

#. If the SoM or the carrier board is new, add its data file to ``boards/`` and
   its pictures to ``images/``. Use an existing file of the same board type as
   a starting point.
#. Create the directory ``<som>-<carrier>/``, with a ``combination.yaml`` and
   the four pages ``index.rst``, ``prerequisites.rst``, ``quickstart.rst`` and
   ``user-guide.rst``. Copy them from an existing combination; the pages are
   identical for all combinations.

The reference designs index lists the new directory automatically.

Combination variables
--------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Variable
     - Type
     - Description
   * - ``som``
     - string
     - Identifier of the SoM, the name of its file in ``boards/``
   * - ``carrier``
     - string
     - Identifier of the carrier board, the name of its file in ``boards/``
   * - ``processor``
     - string
     - Processor on the SoM, as in its analog.com product page URL (e.g.,
       ``ADSP-SC846``)
   * - ``openocd_interface``
     - string
     - OpenOCD interface configuration of the debug agent of the carrier board
   * - ``openocd_target``
     - string
     - OpenOCD target configuration of the processor
   * - ``release``
     - string
     - Name of the Linux release archive, see :ref:`adsp setup`
   * - ``dtb``
     - string
     - Linux device tree of the combination

The labels of the pages are ``<som> <carrier>``, followed by
``prerequisites``, ``quickstart``, ``user-guide`` or ``help-and-support``.

Board variables
--------------------------------------------------------------------------------

Common to SoMs and carrier boards:

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Variable
     - Type
     - Description
   * - ``id``
     - string
     - Identifier of the board, the same as the file name
   * - ``description``
     - RST
     - Overview paragraph, with a link to the product page
   * - ``features``
     - list
     - Features of the board
   * - ``images``
     - list
     - Pictures in ``images/``, each with ``file``, ``alt``, ``caption`` and
       ``width``
   * - ``manual``
     - string
     - Path of the board manual on analog.com, the complete user guide of the
       board
   * - ``documents``
     - list
     - (Optional) Links for the "Helpful documents" section, for example data
       sheets, hardware reference manuals and anomaly lists
   * - ``schematic``
     - string
     - Path of the schematic on analog.com
   * - ``bom_ref``
     - string
     - Label of the bill of materials in :ref:`adsp boms`
   * - ``hardware_sections``
     - list
     - (Optional) Additional user guide sections, each with ``title`` and an
       RST ``body``. Only describe what is needed to set up the boards; the
       manual covers the rest.

SoMs only:

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Variable
     - Type
     - Description
   * - ``power``
     - mapping
     - Power input jumper: ``jumper``, its setting for ``standalone`` and
       ``carrier`` use, and the ``standalone_input``
   * - ``boot``
     - mapping
     - Boot mode ``switch``, its ``jtag_position`` and ``flash_position``, and
       the list of ``modes`` as ``[position, mode]``
   * - ``jtag_voltage``
     - string
     - JTAG voltage of the processor
   * - ``uart``
     - string
     - Connector of the serial console

Carrier boards only:

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Variable
     - Type
     - Description
   * - ``power_input``, ``power_supply``
     - string
     - Power connector and supply voltage
   * - ``slots``
     - list
     - SoM connectors, each with ``name`` and ``ethernet`` port
   * - ``recommended_slot``, ``recommended_slot_reason``
     - string
     - SoM connector used by the quick start, and why
   * - ``debug_agent``
     - mapping
     - Debug agent ``switch``, the table ``columns``, the settings to
       ``enable`` and ``disable`` it, the ``enable_text`` for the quick start,
       and an optional ``note``
   * - ``jtag_routing``
     - mapping
     - JTAG routing ``switches`` and the ``routes``, each with ``route``,
       ``settings`` and, for a single SoM, its ``slot``

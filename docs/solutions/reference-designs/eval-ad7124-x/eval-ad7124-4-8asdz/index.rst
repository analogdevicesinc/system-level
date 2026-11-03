.. _eval-ad7124-4-8asdz_index:

EVAL-AD7124-4ASDZ / EVAL-AD7124-8ASDZ User Guide
===============================================================================

.. toctree::
   :hidden:

   hardware

The :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` and :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>` are full-featured
evaluation boards for the :adi:`AD7124-4` and :adi:`AD7124-8`, low power, low
noise, completely integrated analog front ends for high precision measurement
applications. Both boards share the same PCB design.

- The :adi:`AD7124-4` provides 4 differential or 7
  single-ended/pseudo-differential inputs.
- The :adi:`AD7124-8` provides 8 differential or 15
  single-ended/pseudo-differential inputs (additional inputs on connector J4).

The evaluation boards connect to the :adi:`SDP-B` controller
board via the 120-pin SDP connector. Power is provided through USB from the PC,
with on-board regulators generating all required supply rails.

.. figure:: ../images/eval-ad7124-asdz-top.webp
   :alt: Photo of the EVAL-AD7124-8-ASDZ evaluation board (top view)
   :align: center
   :width: 600

   EVAL-AD7124-8ASDZ Top view

.. figure:: ../images/eval-ad7124-asdz-bottom.webp
   :alt: Photo of the EVAL-AD7124-8-ASDZ evaluation board (bottom view)
   :align: center
   :width: 600

   EVAL-AD7124-8ASDZ Bottom view

Features
-------------------------------------------------------------------------------

- Full-featured evaluation board for the :adi:`AD7124-4` / :adi:`AD7124-8`
- On-board 2.5 V ADR4525 precision voltage reference
- PC control with :adi:`SDP-B`
- PC software for control and data analysis (time domain and frequency domain)
- Compatible with AD7124 Eval+ Software, IIO Scope, Python, and MATLAB
- Arduino, PMOD, and SDP-120 pin connectors for flexible interfacing
- Standalone SPI breakout mode via link settings

Related Documents
-------------------------------------------------------------------------------

- :adi:`AD7124-4 Data Sheet <AD7124-4>`
- :adi:`AD7124-8 Data Sheet <AD7124-8>`
- :adi:`EVAL-AD7124-4ASDZ Product Page <EVAL-AD7124-4ASDZ>`
- :adi:`EVAL-AD7124-8ASDZ Product Page <EVAL-AD7124-8ASDZ>`

Required Software
-------------------------------------------------------------------------------

- AD7124 Eval+ Software (included on CD or :download:`downloadable <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`)

Quick Start Guide
-------------------------------------------------------------------------------

Equipment required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` or :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>` evaluation board
- :adi:`SDP-B` controller board
- USB cable
- DC signal source
- PC running Windows with a USB 2.0 port

Getting started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   The evaluation software and drivers must be installed **before** connecting
   the evaluation board and controller board to the USB port of the PC, to
   ensure the system is correctly recognized.

#. With the :adi:`SDP-B` disconnected from the PC, install the AD7124 Eval+
   Software. Restart the PC after installation.
#. Connect the :adi:`SDP-B` to the evaluation board via the 120-pin SDP
   connector (J3).
#. Screw the two boards together using the plastic screw and washer set
   included in the evaluation board kit.
#. Connect the :adi:`SDP-B` to the PC using a USB cable.
#. From the Start menu, navigate to **Programs > Analog Devices > AD7124
   Eval+** to launch the software.
#. Select **EVAL-AD7124-4ASDZ** or **EVAL-AD7124-8ASDZ** from the interface
   selection dialog.

See the :ref:`SDP-B quickstart guide <eval-ad7124-x quickstart sdp_b>` for
detailed software installation and operation instructions.

Software Resources
-------------------------------------------------------------------------------

- :git-no-OS:`AD7124 no-OS driver <drivers/adc/ad7124>`
- :external+linux:ref:`ad7124` (Linux driver)

Design and Integration Files
-------------------------------------------------------------------------------

Schematics, layout files, and bill of materials are available on the
:adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124-4ASDZ>` product page.

.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7192

.. _ad7192:

AD7192 Evaluation Board User Guide
==================================

The EVAL-AD7192ASDZ evaluation kit features the AD7192 which is 4.8 kHz ultralow
noise 24-bit sigma-delta (Σ-Δ) ADCs.The on-chip low noise gain stage means that
signals of small amplitude can interface directly to the ADC.The internal clock
option provides a compact solution for low BW requirements.

The AD7192 ACE Plugin fully configures the AD7192 device register functionality
and provides dc time domain analysis in the form of waveform graphs, histograms,
and associated noise analysis for ADC performance evaluation.

Full specifications on the AD7192 are available in the product data sheet, which
should be consulted in conjunction with this user guide when working with the
evaluation board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7192blockdiag.png
   :width: 600px

Features
--------

- Full featured evaluation board for the AD7192
- PC control in conjunction with the system demonstration platform
  (EVAL-SDP-CB1Z/EVAL-SDP-CK1Z)
- PC software for control and data analysis (time and frequency domain)

Related Documents
-----------------

- :adi:`AD7192 Data Sheet <media/en/technical-documentation/data-sheets/ad7192.pdf>`

Required Software
-----------------

- :adi:`ACE Software <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7192asdz.html#eb-documentation>`
- :adi:`AD7192 ACE Plugin <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7192asdz.html#eb-documentation>`

Quick Start Guide
=================

The following steps highlight the process to begin using the evaluation board.

Equipment Required
------------------

#. :adi:`EVAL-AD7192ASDZ evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7192.html>`
#. PC running Windows with a USB2.0 port and software installed.
#. Controller Board

::

   - Option A: [[adi>en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html

\|EVAL-SDP-CK1Z]] and a USB-C cable

::

   - Option B: [[adi>en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-b.html

\|EVAL-SDP-CB1Z]] and a Micro-USB cable

Getting started
~~~~~~~~~~~~~~~

.. warning::

   Ensure the SDP board is not connected to the USB port of the PC

#. Install the
   :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`

- :dokuwiki:`Ace Plugin Install guide available here </resources/eval/user-guides/ad7192/softwareguide#ace_plugin_install_guide>`

#. If
   :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`
   is already installed, update the Plugins to download AD719x Plugin.

#. Connect the EVAL-AD7192ASDZ to the controller board

   #. **Option A:** Connect the EVAL-AD7192ASDZ to the EVAL-SDP-CK1Z

 Using the 120 pin connector

*  Screw the two boards together using the plastic screw-washer set included in
   the evaluation board kit to ensure that the boards are connected firmly
   together.

 Using the Arduino Connectors

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/sdp_connect.png

 **Option B:** Connect the EVAL-AD7192ASDZ to the EVAL-SDP-CB1Z

#. Using the 120 pin connector

   * Screw the two boards together using the plastic screw-washer set included
     in the evaluation board kit to ensure that the boards are connected firmly
     together.

#. If using Windows® XP, it may be needed to search for the controller board
   drivers. Choose to automatically search for the drivers for the controller
   board if prompted by the operating system.

#. Launch the ACE plugin from the **Analog Devices** subfolder in the
   **Programs** Menu.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ace_plugin_open.png
      :width: 300px

#. The
   :dokuwiki:`Low Noise Test Demo </resources/eval/user-guides/ad7192/softwareguide#low_noise_test_demo>`
   is a useful demo mode of the Ace Plugin software to ensure that the
   Evaluation board is communicating correctly with the Ace Plugin software.

Hardware Guide
--------------

:dokuwiki:`Visit the hardware guide chapter here </resources/eval/user-guides/ad7192/hardwareguide>`
**Contents of the Hardware guide:**

#. :dokuwiki:`Set-up Procedures </resources/eval/user-guides/ad7192/hardwareguide#set-up_procedures>`
#. :dokuwiki:`Block Diagram </resources/eval/user-guides/ad7192/hardwareguide#block_diagram>`
#. :dokuwiki:`Hardware Link Options </resources/eval/user-guides/ad7192/hardwareguide#hardware_link_options>`
#. :dokuwiki:`On Board Connections </resources/eval/user-guides/ad7192/hardwareguide#on_board_connections>`
#. :dokuwiki:`Power Supplies </resources/eval/user-guides/ad7192/hardwareguide#power_supplies>`
#. :dokuwiki:`Serial Interface </resources/eval/user-guides/ad7192/hardwareguide#serial_interface>`
#. :dokuwiki:`Reference Options </resources/eval/user-guides/ad7192/hardwareguide#reference_options>`
#. :dokuwiki:`GPIOs </resources/eval/user-guides/ad7192/hardwareguide#gpios>`
#. :dokuwiki:`Schematics </resources/eval/user-guides/ad7192/hardwareguide#schematics>`
#. :dokuwiki:`Bill of Materials </resources/eval/user-guides/ad7192/hardwareguide#bill_of_materials>`

Software Guide
--------------

:dokuwiki:`Visit the software guide chapter here </resources/eval/user-guides/AD7192/softwareguide>`

**Contents of the Hardware guide:**

- :dokuwiki:`Ace Plugin </resources/eval/user-guides/AD7192/softwareguide#ace_plugin>`
- :dokuwiki:`Ace Plugin Install <resources/eval/user-guides/AD7192/softwareguide#ace_plugin_install_guide>`
- :dokuwiki:`Ace Plugin Operation <resources/eval/user-guides/AD7192/softwareguide#ace_software_operation>`
- :dokuwiki:`Ace Plugin Demo Modes <resources/eval/user-guides/AD7192/softwareguide#AD7192_demo_modes>`
- :dokuwiki:`Low Noise Test Demo <resources/eval/user-guides/AD7192/softwareguide/demo_modes#low_noise_test_demo>`
- Weigh Scale Demo
- :dokuwiki:`Virtual Eval Guide <resources/eval/user-guides/ad7192/softwareguide#virtual_eval_guide>`
- :dokuwiki:`AD7192 Firmware </resources/tools-software/product-support-software/ad719x_mbed_iio_application>`


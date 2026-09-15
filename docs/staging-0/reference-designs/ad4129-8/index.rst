.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad4129-8

.. _ad4129-8:

AD4129-8 Evaluation Board User Guide
====================================

The
:adi:`EVAL-AD4129-8WARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-overview>`
evaluation kit features the AD4129-8 16-bit, ultra-low power, low noise
analog-to-digital converter (ADC).

The
:adi:`EVAL-AD4129-8WARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-overview>`
board connects to the USB port of the PC by connecting to the EVAL-SDP-CK1Z
motherboard. A 5V USB supply via the PC is regulated to 3.3 V to supply the
AD4129-8 and support all necessary components.

The
:adi:`AD4129-8 ACE Plugin <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-relatedsoftware>`
fully configures the AD4129-8 device register functionality and provides dc time
domain analysis in the form of waveform graphs, histograms, and associated noise
analysis for ADC performance evaluation.

The
:adi:`EVAL-AD4129-8WARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-overview>`
is an evaluation board that allows the user to evaluate the features of the ADC.
The user PC software executable controls the AD4129-8 over the USB through the
:adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
System Demonstration Platform (SDP) board.

Full specifications on the :adi:`AD4129-8 <en/products/ad4129-8.html>` are
available in the product data sheet, which should be consulted in conjunction
with this user guide when working with the evaluation board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4129-8wardz_block_diagram_adr391.png
   :width: 600px

Features
--------

- Full featured evaluation board for the AD4129-8
- PC control in conjunction with Analog Devices, Inc. System
- Demonstration Platform
  (:adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`)
- PC software for control and data analysis (time domain)
- Standalone capability

Equipment Needed
----------------

-
  :adi:`EVAL-AD4129-8WARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-overview>`
  evaluation board
-
  :adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
  System Demonstration Platform
- DC signal source
- USB cable
- PC running Windows with USB 2.0 port

Related Documents
-----------------

- :adi:`AD4129-8 Data Sheet <media/en/technical-documentation/data-sheets/ad4129-8.pdf>`

Required Software
-----------------

- :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
- :adi:`AD4129-8 ACE Plugin <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4129-8.html#eb-relatedsoftware>`

Quick Start Guide
=================

To begin using the evaluation board, do the following:

#. With the SDP-K1 board disconnected from the USB port of the PC, install the
   ACE software (can be downloaded online). Restart the PC after the software
   installation is complete. (For complete software installation instructions,
   see the Evaluation Software section.)
#. Connect the SDP-K1 board to the EVAL-AD4129-8WARDZ board.

::

   {{:resources:eval:user-guides:ad4130_new_eval_board_with_sdp_not_conencted_2.jpg?400|}}  {{:resources:eval:user-guides:ad4130_new_eval_board_with_sdp_conencted.jpg?400| *{{:resources:wechat_image_20210401114013.jpg?300|}}

#. Connect the SDP-K1 board to the PC using the supplied USB cable. Choose to
   automatically search for the drivers for the SDP-K1 board if prompted by the
   operating system.

::

   *{{:resources:eval:user-guides:20220308_110921.jpg?400|}}

#. From the Programs menu, go to the Analog Devices subfolder, and click ACE to
   launch the AD4129-8 ACE Plugin (see the Launching the Software section).

::

   *{{:resources:screenshot_2021-04-01_123406.png?400|}}

Hardware Guide
==============

Visit the hardware guide chapter
`here <http://wiki.analog.com/resources/eval/user-guides/ad4129-8/hardwareguide>`__
**Contents of the Hardware guide**:

#. :dokuwiki:`Set-up Procedures </resources/eval/user-guides/ad4129-8/hardwareguide#set-up_procedures>`
#. :dokuwiki:`Block Diagram </resources/eval/user-guides/ad4129-8/hardwareguide#block_diagram>`
#. :dokuwiki:`Hardware Link Options </resources/eval/user-guides/ad4129-8/hardwareguide#hardware_link_options>`
#. :dokuwiki:`On Board Connections </resources/eval/user-guides/ad4129-8/hardwareguide#on_board_connections>`
#. :dokuwiki:`Power Supplies </resources/eval/user-guides/ad4129-8/hardwareguide#power_supplies>`
#. :dokuwiki:`Serial Interface </resources/eval/user-guides/ad4129-8/hardwareguide#serial_interface>`
#. :dokuwiki:`Reference Options </resources/eval/user-guides/ad4129-8/hardwareguide#reference_options>`
#. :dokuwiki:`Schematics </resources/eval/user-guides/ad4129-8/hardwareguide#schematics>`
#. :dokuwiki:`Bill of Materials </resources/eval/user-guides/ad4129-8/hardwareguide#bill_of_materials>`

Software Guide
==============

Visit the software guide chapter
`here <http://wiki.analog.com/resources/eval/user-guides/ad4129-8/softwareguide>`__
**Contents of the Software guide**:

- :dokuwiki:`Ace Plugin </resources/eval/user-guides/ad4129-8/softwareprocedures#ace_plugin>`
- :dokuwiki:`Ace Plugin Install <resources/eval/user-guides/ad4129-8/softwareprocedures#ace_plugin_install_guide>`
- :dokuwiki:`Ace Plugin Operation <resources/eval/user-guides/ad4129-8/softwareprocedures#ace_software_operation>`
- :dokuwiki:`Visit the demo mode section here <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes>`
- :dokuwiki:`Noise Test Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#noise_test_demo>`
- :dokuwiki:`2 Wire RTD Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#wire_rtd_demo>`
- :dokuwiki:`3 Wire RTD Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#wire_rtd_demo1>`
- :dokuwiki:`4 Wire RTD Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#wire_rtd_demo2>`
- :dokuwiki:`Thermocouple Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#thermocouple_demo>`
- :dokuwiki:`Thermistor Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#thermistor_demo>`
- :dokuwiki:`4 Wire Bridge Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#wire_bridge_demo>`
- :dokuwiki:`6 Wire Bridge Demo <resources/eval/user-guides/AD4129-8/softwareprocedures/demo_modes#wire_bridge_demo1>`
- :dokuwiki:`Active Functional Model Guide <resources/eval/user-guides/ad4129-8/softwareprocedures/afm>`
- :dokuwiki:`AD4129 Firmware </resources/eval/user-guides/ad4129/mbed_iio_app>`

FIFO
====

Quick Start Demonstration
-------------------------

To acquire data from the EVAL-AD4129-8WARDZ without using the FIFO the
int_pin_sel bitfield in the io_control_1 register need to be set to ``11``.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130_8_int_pin_sel.png

Configuring the AD4129-8 FIFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. When using the FIFO on the AD4129-8 the int_pin_sel bitfield in the
   io_control_1 register need to be set to ``00``.
#. Expand the fifo_ctrl register in the AD4129-8 Memory Map.
#. The default value for the watermark bitfield is ``0x00`` which equates to 256
   conversions.

-

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4129_8_fifo_watermark_yoda_description.png
    :width: 600px

#. The fifo_mode bitfield sets which config the FIFO is setup for.

-

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4129_8_fifo_mode_yoda_description.png
    :width: 600px

#. The FIFO will start gathering conversions as soon as the Apply Changes button
   clicked in the AD4129-8 Memory Map Tab.
#. Go the Analysis tab and select the Run Continuous button.

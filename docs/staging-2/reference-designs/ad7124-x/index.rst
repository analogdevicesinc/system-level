.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7124-x

.. _ad7124-x:

AD7124-X User Guide
===================

The EVAL-AD7124-xASDZ evaluation kit features the AD7124-4/AD7124-X 24-bit, low
power, low noise analog-to-digital converter (ADC). A 5 V external supply is
regulated to 3.3 V to supply the AD7124-X and support all necessary components.
The EVAL-AD7124-xASDZ board connects to the USB port of the PC by connection to
the EVAL-SDP-CB1Z motherboard. The EVAL-AD7124-xASDZ software fully configures
the AD7124-X device register functionality and provides dc time domain analysis
in the form of waveform graphs, histograms, and associated noise analysis for
ADC performance evaluation. The EVAL-AD7124-xASDZ is an evaluation board that is
designed to allow the user to evaluate the features of the ADC. The user PC
software executable controls the AD7124-X over the USB through the system
demonstration platform board (EVAL-SDP-CB1Z).

The AD7124-X is a low power, low noise, complete analog front end for high
precision measurement applications. It contains a low noise, 24-bit Σ-Δ ADC. It
can be configured to have four differential inputs or seven single-ended or
pseudo-differential inputs. The on-chip low noise instrumentation amplifier
means that signals of small amplitude can be interfaced directly to the ADC.
Other on-chip features include a low drift 2.5 V reference, excitation currents,
reference buffers, multiple filter options and many diagnostic features.
Complete specifications for the AD7124-X are provided in the product data sheet
and should be consulted in conjunction with this user guide when using the
evaluation board. Full details about the EVAL-SDP-CB1Z are available on the
Analog Devices, Inc., website.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/AD7124-X_functional_block_diagram.png
   :width: 600px

Features
--------

- Full featured evaluation board for the AD7124-X
- PC control in conjunction with the system demonstration platform
  (EVAL-SDP-CB1Z)
- PC software for control and data analysis (time domain)
- Standalone capability

Documents Needed
~~~~~~~~~~~~~~~~

- :adi:`AD7124 Data Sheet <media/en/technical-documentation/data-sheets/AD7124-X.pdf>`

Required Software
~~~~~~~~~~~~~~~~~

-
  :adi:`AD7124 Evaluation Software <media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`
  (:dokuwiki:`Install guide </resources/eval/user-guides/ad7124/software#install_guide>`)(:dokuwiki:`Eval+ Description </resources/eval/user-guides/ad7124/software#eval_software_windows>`)

Equipment Needed
~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7124-XASDZ evaluation board <en/products/AD7124-X.html>`
-
  :adi:`EVAL-SDP-CB1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-b.html>`
  or
  :adi:`EVAL-SDP-CK1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
- USB cable
- PC running Windows with USB 2.0 port

Quick Start Guide
-----------------

To begin using the evaluation board, please do the following

#. With the controller board **disconnected** from the USB port of the PC,
   install the AD7124-X evaluation board software from the link provided above
   (or alternatively,
   :adi:`here <media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`).
   The PC must be restarted after the software installation is complete.
   Step-by-step walkthrough of the install process available here. Full install
   guide available in the
   :dokuwiki:`Install guide </resources/eval/user-guides/ad7124/software#install_guide>`
#. If using the EVAL-SDP-CB1Z board or the SDP-K1 with the 120pin connection:

- Screw the two boards together using the plastic screw-washer set included in
  the evaluation board kit to ensure that the boards are connected firmly
  together.

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/quick_start.jpg
    :width: 600px

#. If using the Arduino connector on the SDP-K1, connect as shown in the image
   below: (**:red:`Currently not supported by EVAL+, use SDP-B`**)

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_baord_sdp-k1.jpg
      :width: 400px

#. Connect the controller board to the PC using the supplied USB cable. If you
   are using Windows® XP, you may need to search for the EVAL-SDP drivers.
   Choose to automatically search for the drivers for the EVAL-SDP board if
   prompted by the operating system.

#. Launch the EVAL-AD7124-xASDZ software from the **Analog Devices** subfolder
   in the **Programs** menu.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/program_menu.png
      :width: 600px

#. If the AD7124 evaluation system is not connected to the USB port via the
   SDP-B when the software is launched, a connectivity error displays (see
   below). Connect the evaluation board to the USB port of the PC, wait a few
   seconds, click **Refresh**, and then follow the on-screen instructions.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/install_2.png
      :width: 250px

#. Once the evaluation system has been connected to the PC and **Refresh** has
   been clicked, the dialog box will update as shown.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/install_3.png
      :width: 250px

#. Click select on the dialog box and you will then be at the Eval+ homescreen.

A detailed **description of the various Eval+ windows** can be found
:dokuwiki:`here </resources/eval/user-guides/ad7124/software#eval_software_windows>`.
The
:dokuwiki:`Noise Test Demo </resources/eval/user-guides/ad7124/software/demo_modes#noise_test_demo>`
is a quick example to ensure that the boards and software have been set up
correctly.

Hardware Guide
--------------

:dokuwiki:`Visit the hardware guide chapter here <ad7124-x/hardware_guide>`
**Contents of the Hardware guide:**

::

   - [[resources:eval:user-guides:ad7124-x:hardware_guide#device_description|Description]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#set-up_procedures|Set Up Procedures]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#block_diagram|Block Diagram]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#hardware_link_options|Hardware Link Options]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#on_board_connectors|On Board Connecters]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#power_supplies|Power Supplies]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#serial_interface|Serial Interface]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#reference_options|Reference Options]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#schematics|Schematics]]
   - [[resources:eval:user-guides:ad7124-x:hardware_guide#bill_of_materials|Bill of Materials]]

Software Guide
--------------

:dokuwiki:`Visit the software guide chapter here <ad7124-x/software>` **Contents
of the Software guide:**

#. :dokuwiki:`Evaluation+ Software </resources/eval/user-guides/ad7124-x/software#eval_software>`

::

   - [[resources:eval:user-guides:ad7124-x:software#install_guide|Install Guide]]
   - [[resources:eval:user-guides:ad7124-x:software#eval_software_windows|Evaluation+ Windows]]
   - [[resources:eval:user-guides:ad7124-x:software#ad7124-x_eval_demo_modes|Evaluation+ Demo Modes]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#noise_test_demo|Noise Test Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#wire_rtd_demo|2 Wire RTD Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#wire_rtd_demo1|3 Wire RTD Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#wire_rtd_demo2|4 Wire RTD Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#thermocouple_demo|Thermocouple Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#thermistor_demo|Thermistor Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#wire_bridge_demo|4 Wire Bridge Demo]]
        - [[resources:eval:user-guides:ad7124-x:software:demo_modes#wire_bridge_demo1|6 Wire Bridge Demo]]
 - [[resources:eval:user-guides:ad7124-x:software#virtual_eval_guide|Virtual
   Eval]]

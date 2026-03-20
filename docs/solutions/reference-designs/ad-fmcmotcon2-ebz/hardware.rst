Motor Control Hardware
======================

Hardware solutions
------------------

:doc:`AD-FMCMOTCON2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/controller_board>` - Controller board

|AD-FMCMOTCON2-EBZ|

-  Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors
-  Digital board for interfacing with the low and high voltage drive boards
-  FMC signals voltage adaptation interface for seamless operation on all FMC voltage levels
-  Fully isolated digital control and feedback signals

   -  2 isolated GPOs
   -  2 isolated GPIs
   -  18 isolated drive signals – can drive 2 bridges with 4 legs simultaneously
   -  6 high speed ADC digital interfaces (data + clock)

-  Isolated Xilinx XADC interface
-  2 x Gbit Ethernet PHYs for high speed industrial communication - RGMII mode
-  Single ended Hall + Differential Hall + Encoder + Resolver interfaces

   -  2 x single ended HALL, 2 x differential HALL, 2 x encoder interfaces – this allows 2 motors to be driven simultaneously

-  Digital sensors interfaces

   -  EnDat
   -  BISS Interface

:doc:`AD-DRVLV2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/lv_board>` - Low voltage drive board

|AD-DRVLV2-EBZ|

-  Connects to the Controller board and has a power stage that can drive motors up to 48V and 20A.
-  Drives 2 motors simultaneously
-  High frequency drive stage implemented with ADI isolated gate drivers
-  Supported motor types

   -  BLDC
   -  PMSM
   -  Brushed DC
   -  Stepper (bipolar / unipolar)

-  Integrated over current protection
-  Reverse voltage protection
-  Current and Voltage measurement using isolated ADCs

   -  Current measurement on 2 phases for 2 motors
   -  DC Link Voltage measurement

-  BEMF zero cross detection for sensorless control of PMSM or BLDC motors
-  Separate voltage supplies for the 2 motors so that the motors don’t influence
   each other

:doc:`AD-DYNO2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/dyno>` - Dynamometer Drive System

|AD-DYNO2-EBZ|

-  Two BLDC motors connected in a dyno setup
-  Electronically adjustable load – the load value is set using the onboard buttons + LCD
-  Programmable step and ramp load changes
-  Measurement and display of load motor phase currents
-  Measurement and display of load motor speed
-  External control and monitoring interface

Downloads
---------

.. admonition:: Download
   :class: download

   **AD-FMCMOTCON2-EBZ**


   -  `Schematics <resources/ad-fmcmotcon2-ebz_schematics.pdf>`_
   -  `Bill of Materials <resources/ad-fmcmotcon2-ebz_bom.zip>`_
   -  `Allegro Board File <resources/ad-fmcmotcon2-ebz_layout.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ (You need 16.5 or higher).

   **AD-DRVLV2-EBZ**

   -  `Schematics <resources/ad-drvlv2-ebz_schematics.pdf>`_
   -  `Bill of Materials <resources/ad-drvlv2-ebz_bom.zip>`_
   -  `Allegro Board File <resources/ad-drvlv2-ebz_layout.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ (You need 16.5 or higher).


Where to Buy
------------

.. container:: round box

   :adi:`FMCMOTCON2 Evaluation Kit <design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html>`

.. |AD-FMCMOTCON2-EBZ| image:: images/mc2_ctrl_single.jpg
   :width: 300
.. |AD-DRVLV2-EBZ| image:: images/mc2_lv_single.jpg
   :width: 300
.. |AD-DYNO2-EBZ| image:: images/mc2_dyno_single.jpg
   :width: 300

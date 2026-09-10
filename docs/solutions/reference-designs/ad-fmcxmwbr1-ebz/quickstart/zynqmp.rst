.. _fmcxmwbr1 quickstart zynqmp:

ADRV9009-ZU11EG
===============================================================================

This guide provides instructions on how to set up and test the
:adi:`AD-FMCXMWBR1-EBZ` on the :adi:`ADRV9009-ZU11EG RF-SOM <ADRV9009-ZU11EG>`
with the :adi:`ADRV2CRR-FMC` carrier.

Overview
-------------------------------------------------------------------------------

The production testing of :adi:`AD-FMCXMWBR1-EBZ` (DUT) is automated. The test
procedure runs on :adi:`ADRV9009-ZU11EG` RF-SOM.

Creating an SD test card
-------------------------------------------------------------------------------

Write the latest available SD card image to a spare card and prepare the card
to boot into Linux.

.. admonition:: Download
   :class: download

   **Release February 2022**

   -  `AD-FMCXMWBR1-EBZ test image
      <https://swdownloads.analog.com/cse/prod_test_rel/fmcbridge_test/adrv9009zu11eg_fmcbridge_prod_test_2022.img.xz>`_

.. tip::

   To write an image on an SD card you can follow the instructions
   :external+kuiper:doc:`here <index>`.

Required hardware
-------------------------------------------------------------------------------

#. :adi:`ADRV2CRR-FMC` carrier board
#. :adi:`ADRV9009-ZU11EG RF-SOM <ADRV9009-ZU11EG>` with heat plate and heat
   sink fitted
#. `TE150A1251F01
   <https://www.digikey.com/en/products/detail/sl-power-electronics-manufacture-of-condor-ault-brands/TE150A1251F01/9856910>`_
   power supply (or similar)
#. SD card with testing procedure
#. Power rails cable (custom, available in the :adi:`AD-FMCXMWBR1-EBZ` kit)
#. `FFSD-20-D-12.00-01-N
   <https://www.digikey.com/en/products/detail/samtec-inc/FFSD-20-D-12-00-01-N/1106590>`_
   ribbon cable (available in the :adi:`AD-FMCXMWBR1-EBZ` kit)
#. AD-FMCBRIDGE1A TEST BOARD
#. QR code scanner: QUICKSCAN QD2430 Datalogic
#. USB 3.0 4-Port Hub: Targus ACH154
#. Keyboard
#. Ethernet cable for network connection
#. USB Adapter: USB Type C Plug, USB Type A Receptacle
#. Display port monitor and cable

Required setup
-------------------------------------------------------------------------------

-  First, the :adi:`ADRV9009-ZU11EG` setup should be built. Please refer to the
   `ADRV9009-ZU11EG Quick Start Guide
   <https://analogdevicesinc.github.io/system-level/pull/208/solutions/reference-designs/adrv9009-zu11eg/quickstart/quick-start-guide/>`_.
-  :adi:`ADRV2CRR-FMC` should be powered with the TE150A1251F01 power supply and
   connected to a network with the ethernet cable.
-  The screen is connected to :adi:`ADRV2CRR-FMC` through a display
   port cable. If there is no image shown on the screen at the first
   boot, please refer to the `guide
   <https://developer.analog.com/docs/hdl/user_guide/build_boot_bin.html>`_.
-  Connect the USB OTG adapter and plug the USB Port Hub. In the
   Port Hub will be connected the keyboard and the QR code scanner.
-  Plug the :adi:`AD-FMCXMWBR1-EBZ` into the FMC connector of the
   :adi:`ADRV2CRR-FMC`.

.. image:: ../images/picture2.png
   :alt: :adi:`AD-FMCXMWBR1-EBZ` test setup on carrier
   :align: center

.. important::

   Make sure that the potentiometers R19, R2, R20 are adjusted to maximum.
   (After the last turn a click sound can be heard.)

   .. image:: ../images/pot_adjustment.jpg

.. important::

   Before testing, please make sure that P5, P6, P8, P39, P40, P50, P51 have
   jumpers connecting pin 1 and pin 2.

-  Use the cables to connect the :adi:`AD-FMCXMWBR1-EBZ` to the TEST BOARD.

.. image:: ../images/fmcxmw_testsetup.jpg
   :align: center
   :width: 600

Test process
-------------------------------------------------------------------------------

.. important::

   Make sure that the full setup is connected when powering up or rebooting the
   system.

After the connections are done as explained in the "Required setup" section,
power up by switching S12 of :adi:`ADRV2CRR-FMC` to on position.
When booting, it is mandatory to have the full setup, with the
:adi:`AD-FMCXMWBR1-EBZ` board connected.
This way, the devices on the test board will be probed correctly at startup. The
test instructions will prompt on the screen and the testing should be done using
the following steps:

-  Select the appropriate command from the list. To start the test press 1 on
   the keyboard then press enter.

.. image:: ../images/1_test_procedure.png
   :align: center
   :width: 500

-  Test procedure will start, then you will be asked to scan the QR/Barcode on
   the board.

.. image:: ../images/2_test_procedure.png
   :align: center
   :width: 500

-  The program will start, the tests are performed automatically and will show
   the message PASSED/FAILED at the end of the procedure.

.. image:: ../images/3_test_procedure.png
   :align: center
   :width: 400

.. image:: ../images/4_test_procedure.png
   :align: center
   :width: 300

-  To test another board, select option (2) to power off the setup, before
   using the physical switch and disconnecting :adi:`AD-FMCXMWBR1-EBZ`.

.. image:: ../images/5_test_procedure.png
   :align: center
   :width: 500

Schematics and CAD Files
-------------------------------------------------------------------------------
..
   .. admonition:: Download
      :class: download

      -  `AD-FMCXMWBR1-EBZ test board Schematics
         <../resources/fmc_bridge_testbrd_update.pdf>`_
      -  `AD-FMCXMWBR1-EBZ test board CAD files
         <../resources/test_board_ad-fmcxmwbr1.7z>`_
..

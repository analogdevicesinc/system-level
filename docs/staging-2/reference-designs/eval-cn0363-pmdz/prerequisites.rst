.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cn0363-pmdz/prerequisites

.. _eval-cn0363-pmdz prerequisites:

EVAL-CN0363-PMDZ Hardware Setup
===============================

The :adi:`CN0363` HDL reference design and software are designed to operate with
the following hardware and FPGA development system:

- `ZED Board <http://zedboard.org/product/zedboard>`__, Rev C or later
- USB Keyboard/Mouse
- HDMI Monitor (Full HD)
- :adi:`CN0363` hardware: EVAL-CN0363-PMDZ
- Two vials: one filled with water and one filled with the sample liquid under
  test
- Formatted and partitioned 8GB SD card supplied with EVAL-CN0363-PMDZ board
- Ethernet connection for updating SD card

The equipment should be connected as shown below, make sure that all power is
off before starting to make the connections.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/cn0363_setup.png
   :width: 500px

#. PMOD JA connector of the ZED board connected to the PMOD connector on the
   EVAL-CN0363-PMDZ
#. USB mouse and keyboard connected to the ZED board (J13)
#. 12 V power supply connected to the ZED board (J20)
#. 3.3V VADJ
#. Ethernet cable with internet connection connected to the ZED board (only
   required for software updates)
#. HDMI monitor connected to the ZED board (J9)
#. SD card inserted into the ZED board (J12)
#. 6V to 12V power supply connected to the EVAL-CN0363-PMDZ

.. figure:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_test_setup.png
   :width: 300px

.. tip::

   **Note !!!** that the Jumpers and Switches must be set as shown in the
   picture above. (Click on the picture to enlarge)

Boot (JP7-JP11) and MIO0 (JP6) jumpers are set to SD card mode. To use USB
peripheral devices with ZedBoard, install jumpers JP2 and JP3. The FMC interface
spans over two PL I/O banks, banks 34 and 35. To meet the FMC spec, these banks
are powered from an adjustable voltage set by jumper, J18. Selectable voltages
include 1.8V and 2.5V (currently set).

For more detailed information on the ZedBoard jumper settings, check out the
*ZedBoard Hardware User Guide*, available on the
`ZedBoard doc page <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard>`__,
the *Jumper Settings* chapter.

More Information
----------------

See the :adi:`CN0363` documentation.

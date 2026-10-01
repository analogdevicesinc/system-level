.. _hmcad15xx user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Analog Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`HMCAD1520-EBZ<HMCAD1520-EBZ>` / :adi:`HMCAD1511-EBZ<HMCAD1511-EBZ>` 
evaluation board has four input channels that supports single-ended to 
differential conversion with the use of a balun. By default, all input channels
1-4 (SMAs J3, J5, J6 and J7) are balun-coupled. Alternatively, input channel 1
(SMAs J3 and J4) can be configured to differential to differential conversion,
and input channel 2 (SMA J5) can be configured to single-ended to differential 
conversion using the onboard :adi:`LTC6419<LTC6419>` high-speed differential 
ADC driver.

Refer to the table below for the optional amplifier configuration.

+---------------------------------+------------------------------------------+---------------------------------+------------------------------+------------------------------+
| **Analog input channel number** | **Default Input Driver, AC/DC coupling** | **Signal type on Input/Output** |            **Install**       |          **Uninstall**       |
+=================================+==========================================+=================================+==============================+==============================+
|                1                |    LTC6419, DC coupling, Unity Gain      | Differential/Differential       | R41, R42, R44, R45, R60, R61 | C51, C52, R23, R24, R56, R57 |
+---------------------------------+------------------------------------------+---------------------------------+------------------------------+------------------------------+
|                2                |    LTC6419, DC coupling, Unity Gain      |    Single-Ended/Differential    |         R46, R58, R59        |    C53, R54, R55, R23, R24   |
+---------------------------------+------------------------------------------+---------------------------------+------------------------------+------------------------------+

Analog Input Vcm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

the :adi:`HMCAD1511<HMCAD1511>` / :adi:`HMCAD1520<HMCAD1520>` supplies the 
common mode voltage at half-supply (0.9V) for all analog input channels. No 
external supply is needed for the input Vcm.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

.. warning::
  The recommended VADJ value for each FPGA carrier can be found in the 
  corresponding README.md file :git-hdl:`here <projects/hmcad1520_ebz>`.

Both the :adi:`HMCAD1520` and :adi:`HMCAD1511` are being supplied by
:adi:`ADM7154` with 1.8V. The board can be modified to bypass the LDO so the
:adi:`HMCAD1520` and :adi:`HMCAD1511` are directly supplied by the
:adi:`LTM8078` DC-DC regulator. To do this, change components C3 to 100uF, R6
to 200k, and install a ferrite bead to R9. Also, uninstall R8 and R10.

The supply rails for other components on the board (crystal, amplifier, etc)
are isolated to the :adi:`HMCAD1520` and :adi:`HMCAD1511` supply rail. Refer to
the board schematics for more info.

Clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The :adi:`HMCAD1520-EBZ<HMCAD1520-EBZ>` evaluation board uses an external 1GHz 
clock source on SMA J1 as default.

The :adi:`HMCAD1511-EBZ<HMCAD1511-EBZ>` evaluation board has an on-board 1GHz 
crystal for clocking the :adi:`HMCAD1511<HMCAD1511>`. The user can also 
configure the board to use an external clock source.

Refer to the table below for alternative clock configuration.

+-------------------------+-------------+---------------+
| **Clock Configuration** | **Install** | **Uninstall** | 
+=========================+=============+===============+
| Onboard                 |     R13     |      R12      |
+-------------------------+-------------+---------------+
| External                |     R12     |      R13      |
+-------------------------+-------------+---------------+

Schematic, PCB Layout, Bill of Materials and other Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :download:`HMCAD15xx Schematic <resources/hmcad1520_schematic.pdf>`
- :download:`HMCAD1520 <resources/hmcad1520_doc.pdf>` Datasheet
- :download:`PCB Layout <resources/hmcad15xx_pcb_layout.pdf>`
- :download:`Bill of Materials <resources/hmcad1520_bom.xls>`
- :download:`Gerber Files <resources/hmcad15xx_gerber.zip>`
- :download:`HMCAD15xx Interleaving Spurs Calculator <resources/hmcad15xx_interleaving_spur_calculator_rev1.xlsx>`

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy to example that can be used with it is:

- :ref:`iio-oscilloscope`
- :external+scopy:doc:`Scopy <index>`

Results
-------------------------------------------------------------------------------

For testing we used an input signal with a frequency of 200kHz and an amplitude 
of 1V.

.. image:: ./images/scopy_sig_gen.png
    :width: 600

First we need to Select Debugger -> iio:device2: axi_adc_hmcad15xx and for each 
voltage go to input_select and select the port on which you want that channel
to listen to

.. image:: ./images/hmcad1520_debugger.png
    :width: 600

.. include-template:: ../common/using-scopy.rst.jinja

     scopy_show_data_capture: true
     scopy_show_time_domain: true
     scopy_time_domain_image: ./images/scopy_capture.png

- In the above figure we are using a Single Channel configuration.

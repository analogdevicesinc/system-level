Evaluating the ADF4377 Microware Wideband Synthesizer with Integrated VCO
=========================================================================

The :adi:`EV-ADF4377SD1Z` evaluates the performance of the
:adi:`ADF4377` frequency synthesizer with an integrated voltage controlled
oscillator (VCO) for phase-locked loops (PLLs).

The evaluation board contains the :adi:`ADF4377` frequency synthesizer with
an integrated VCO, a USB interface, power supply connectors, and subminiature
Version A (SMA) connectors.

This board requires an :adi:`SDP-S` board (not supplied with the kit). The
:adi:`SDP-S` allows software programming of the :adi:`EV-ADF4377SD1Z` board
with :adi:`ACE` software.

Supported Carriers
------------------

-  `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Required Hardware
-----------------

-  :adi:`EV-ADF4377SD1Z` board & Power supply
-  :adi:`SDP-I-FMC <EVAL-SDP-I-FMC>` Interposer
-  ZedBoard

Required Software
-----------------

-  Xilinx SDK / Xilinx Vitis.
-  A UART terminal (Tera Term/PuTTY/Hyperterminal), Baud rate 115200.

Build Application
-----------------

In order to build the application and generate the .elf file, please follow
the :external+no-OS:doc:`no-OS build guide <build_guide>`.

Source files for the application can be found in the `Source code`_ section.

Run Application
---------------

Start a UART terminal (set to 115200 baud rate), and program the device and run
the elf file. An output example of the application is provided below:

::

   ADF4377 Successfully initialized!
   Output Frequency Locked!

Source code
-----------

-  :git-no-OS:`ADF4377 Application <projects/adf4377_sdz>`


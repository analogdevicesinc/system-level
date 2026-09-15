.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035/performance

.. _adrv9361-z7035 performance:

ADRV9361-Z7035 - Performance
============================

Error Vector Magnitude (EVM)
----------------------------

This section reports the EVM results for ADRV9361-Z7035 SDR 2X2 SOM. The general
test setup is shown below. In this test, the block labeled ``ADI Hardware
System`` represents the AD9361 on the SOM; the FPGA/SoC is the Zynq Z-7035 SoC
on the SOM.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/iio_object.png
   :width: 600px

IIO System Object

Test Parameters
~~~~~~~~~~~~~~~

#. LTE10 (64-QAM) waveform (I & Q) generated from the MathWorks LTE System
   Toolbox.
#. This dataset is sent to the AD9361 via the Analog Devices IIO System Object
   in MATLAB and transmitted through the AD9361 TX signal chain, at various RF
   frequencies.
#. The AD9361 TX is connected to the AD9361 RX with U.FL-to-U.FL loopback cables
   on the SOM.
#. The AD9361 RX signal chain captures the AD9361 LTE 10 transmitted signal, and
   sends samples back to the IIO system object.
#. The IIO System object sends the received I & Q waveforms to the LTE toolbox,
   where analysis is done.
#. This analysis (EVM) is captured and stored, and the RF is changed, and the
   test continues.
#. The tests were performed from 70MHz – 6 GHz in 100MHz steps.
#. This test is nominal – test done at room temperature, in lab settings.

Results
~~~~~~~

All EVM measurements were under ~2.5%. This works out to about -32dB for the
accumulation of RX and TX.

The AD9361 datasheet specs are ~ −37.782 dB for TX and −37.462 dB for RX (or
about 1.4% each). It is an RMS sum, so we would expect about 1.86% (-34.6dB)
based on the datasheet.

The datasheet uses narrowband baluns, and derives some gain from this. Since
this test is using the wideband baluns on ADRV9361−Z7035 SDR 2X2, that gain is
not seen. Therefore we consider the SOM to perform close enough to the AD9361
datasheet, with a difference of 0.6%.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/evm.png
   :width: 800px

Environmental
-------------

Information regarding environmental and mechanical testing is listed here.
Emissions, Sinusoidal vibration, random vibration, shock, temperature etc. The
ADRV9x63x RF SOM family is tested against various military (https://mil-std.org)
and Information Technology Standards (NIST) using external vendors with the
appropriate equipment. All details and results of such are maintained in the
test reports below.

Emissions and Immunity
~~~~~~~~~~~~~~~~~~~~~~

- :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/analog_devices_picozed_sdr_emc_emissions_and_immunity_ce_mark_test_report_rev_1_0.pdf`

- This report contains tests results for:

  - EN 55022:2010 unwanted emissions
  - EN 55024:2010 immunity

Shock and Vibration
~~~~~~~~~~~~~~~~~~~

- The
  :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/1510-107n_analog_devices_report.pdf`
  contains the results for MIL-STD-202G testing:
- Method 201A:

  - Sinusoidal Vibration
  - Sine Sweep: 10-55-10Hz Traversed in 1 minute.
  - Amplitude: 0.03in (0.06in max total excursion).
  - The motion is applied for a period of 2 hours in each of 3 mutually
    perpendicular directions.

- Method 214A:

  - Random Vibration
  - Frequency Range: 50-2000Hz
  - Amplitude: 5.35g rms
  - Duration: 1.5 hours/Axis
  - 3 mutually perpendicular directions.

- Method 213B:

  - Shock
  - Pulse Shape: Half-Sine.
  - Amplitude: 20g half-sine.
  - 11 msec N
  - 3 shocks positive, 3 shocks negative in 3 mutually perpendicular directions.
    (Total of 18 shocks)

- Tests are performed with unit electrically operating.

Temperature
~~~~~~~~~~~

The report listed above
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/1510-107n_analog_devices_report.pdf`
also contains the results of MIL-STD-810G testing.

The ADRV9361-Z7035 SDR 2X2 is rated for operation in the industrial temperature
range (-40 to 85°C). Please take care to respect the individual device maximum
die temperatures over your operating range with your specific design running on
the SOM.

All devices on the SOM are rated for this temperature range, with the exception
of the Micro SD card cage, which is rated for operation from -25°C to +85°C;
with storage over the full range listed in the table. The SOM has been validated
to work reliably over the full industrial temp range.

Both the Zynq SoC and the AD9361 have the ability to measure and report their
internal die temperature using their built-in data converters. These can be used
to monitor the real-time temperature of these devices and, when necessary, start
a fan wired to the carrier. In addition, for further heat dissipation, a heat
sink may be attached directly to the package of the Zynq SoC on the SOM itself.

Zynq Heat Sink
^^^^^^^^^^^^^^

Selecting heat sinks for Xilinx All-Programmable FPGAs, 3G ICs, and SoCs depends
upon many variables including chip size, device utilization, the ambient
environment, and other criteria. Avnet and CTS® have created technical aids to
ease this process of heat sink identification.

ADRV9361-Z7035 SDR 2X2 uses the Zynq XC7Z035-2LI device in the FBG676 package.
The package outline measures 27 x 27 mm. See Xilinx UG865 for information on
package size, thermal resistance, and recommendations for safely attaching heat
sinks.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/heatsinks.png
   :width: 400px

.. imported from https://wiki.analog.com/resources/eval/ad9082

.. _ad9081 evaluating-using-ace:

Evaluating MxFE™ using ACE
===============================================================================

This user guide describes additional modes and features available in the
:adi:`EVAL-AD9082` / :adi:`EVAL-AD9081` / :adi:`EVAL-AD9986` / :adi:`EVAL-AD9988`.
This guide explains the hardware and software setup needed to setup the
:adi:`AD9082`, :adi:`AD9081`, :adi:`AD9986` or :adi:`AD9988` in the
specified mode, as well as how a user can use the supplied hardware with
:adi:`ADS9-V2EBZ` and software (:adi:`ACE`) to setup the RF transceiver device
in a mode that is not explained in the
:adi:`Evaluation Board User Guide <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>`.

Required documents
-------------------------------------------------------------------------------

- Product datasheets:

   - :adi:`AD9081`
   - :adi:`AD9988`
   - :adi:`AD9082`
   - :adi:`AD9986`
   - :adi:`AD9177`
   - :adi:`AD9207`
   - :adi:`AD9209`

- :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
- :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>`

MxFE evaluation board hardware summary
-------------------------------------------------------------------------------

The table below shows the various evaluation boards and their details.

.. list-table::
   :header-rows: 1

   - - EVB Part #
     - Devices supported
     - Power delivery
     - Analog front end balun
     - Clock input balun
     - On-board crystal oscillator frequency
   - - :adi:`AD9081-FMCA-EBZ <EVAL-AD9081>`
     - :adi:`AD9081` / :adi:`AD9209` / :adi:`AD9177`
     - via FMC connector: uModule and LDO
     - BALH-0009SMG
     - SMP + BAL-0416
     - 100MHz
   - - :adi:`AD9082-FMCA-EBZ <EVAL-AD9082>`
     - :adi:`AD9082` / :adi:`AD9207` / :adi:`AD9177`
     - via FMC connector: uModule and LDO
     - BALH-0009SMG
     - SMP + BAL-0416
     - 100MHz
   - - :adi:`AD9988-FMCB-EBZ <EVAL-AD9988>`
     - :adi:`AD9988`
     - External 12V using ADP5056 and LDO
     - TCM1-83X / LDB184G6
     - SMA + NCR2-123+
     - 122.88MHz
   - - :adi:`AD9986-FMCB-EBZ <EVAL-AD9986>`
     - :adi:`AD9986`
     - External 12V using ADP5056 and LDO
     - TCM1-83X / LDB184G6
     - SMA + NCR2-123+
     - 122.88MHz

Installation of the Heat Sink with Integrated Fan
-------------------------------------------------------------------------------

A heat sink with integrated fan is shipped with the evaluation board for active
cooling of the IC device. Note the power consumption of the IC device is
dependent on its operation mode with some configurations consuming up to 13 W
where the IC die temperature can approach or exceed its maximum specified
operating range of 120 °C. For this reason, it is recommended that this heat
sink shown in Figure 1 is installed before the evaluation process begins.

.. image:: ../images/ad9081_fansink1.png
   :alt: Heat Sink with Fan
   :align: center

The installation steps are as follows:

- Remove blue frame clip that is attached to assembly by lifting metal tab
  free from this frame clip (using small tweezer or metal pick). This frame
  clip is not essential for attachment of the heat sink to the IC device (while
  noting that the FMCB-EBZ variant does not accept this frame clip due to
  passive components within its keep out region).
- Remove the thin plastic tape to expose the adhesive surface

.. image:: ../images/ad9081_fansink2.png
   :alt: Removing the plastic tape
   :align: center

- Carefully position and center the heat sink on top of the IC package such
  that it also remains clear of the RF baluns.
- Once positioned correctly, press down on the heat sinks top side for 10
  seconds to secure it to the IC package.
- Connect the power supply cable

The fan should start spinning once power is applied to the evaluation board.
In the unlikely event that it does not spin, it has been found that the two
screws used to secure the fan to the heatsink are too tight such that the fan
blades cannot spin freely. Loosening the screws using a standard Phillips
screwdriver often releases the fan blade allowing it to spin freely.

.. image:: ../images/ad9081_fansink3.png
   :alt: FanSink™ assembled on the Evaluation Board
   :align: center

Additional information on this product called fanSink™ from Advanced Thermal
Solutions can be found on the vendor's website.

Setting up MxFE™ in a Narrowband mode
-------------------------------------------------------------------------------

The following instructions allow the user to setup the MxFE chip in a single
band 250 MSPS I/Q data rate setup with direct RF sampling. The device is setup
as shown below:

.. image:: ../images/ad9081_narrowband_setup.png
   :alt: Setup block diagram of AD9081
   :align: center

The evaluation board is setup to use the on-board HMC7044 and on-chip PLL to
provide the DAC and ADC clocks. The HMC7044 also provides the clocks for the
FPGA to setup the SERDES link correctly. Refer to the Evaluation board user
guide (UG-1829) for more information on the hardware setup.

Configuring the device in ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open ACE and open the AD9081 plugin.

.. image:: ../images/ad9081_1_start.png
   :alt: ACE Start page with AD9081 plugin

Double click on the AD9081 block to open the chip view.

.. image:: ../images/ad9081_2_board_view.png
   :alt: Open the Chip View

Configure the device Chip View's Quick Configuration section as shown in the
figures below. The steps are numbered in sequence.

.. image:: ../images/ad9081_3_chip_setup1.png
   :alt: Quick configuration steps 1-5
   :align: left

.. image:: ../images/ad9081_4_chip_setup2.png
   :alt: Quick configuration steps 7-8
   :align: right
   
.. image:: ../images/ad9081_5_chip_setup3.png
   :alt: Quick configuration steps 9-10
   :align: left

.. image:: ../images/ad9081_6_chip_setup4.png
   :alt: Quick configuration steps 11-12
   :align: right

.. image:: ../images/ad9081_7_apply.png
   :alt: Apply button
   :align: right

Allow a few seconds for ACE and the ADS9v2 hardware to setup the AD9081. When
the chip is configured correctly, the chip view will show a status readout as
shown below.

.. image:: ../images/ad9081_8_chip_view_after_apply.png
   :alt: Chip readouts after apply

Obtaining an FFT from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on "Proceed to Analysis" button to capture an FFT from the ADC. A no
input FFT is shown below.

.. image:: ../images/ad9081_9_analysis_view.png
   :alt: FFT output with no input signal

Clicking on the "Update JESD Status" button in the chip view will output the
FPGA's JESD204B link status. It will also readout the MxFE chip's junction
temperature by polling the on-chip TMU

.. image:: ../images/ad9081_10_chip_view_after_fftanalysis_view.png
   :alt: FPGA JESD204 status and MxFE junction temperature readout

Connect a signal generator to any of the ADC inputs. Set the frequency to a
3.207GHz CW tone. The NCO is tuned to 3.2GHz. Set the amplitude to 5dBm for
example. This will need to be adjusted based on cable and other RF losses. In
the figure below, the signal generator output was set to 9.9dBm to get to
~-1.2dBFS fundamental power.

.. image:: ../images/ad9081_11_st_fft_onchippll_3p207ghz_9p9dbm.png
   :alt: Single Tone FFT with a CW tone at 3.207GHz

Setting up DPG Lite to generate a tone out of the DAC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open DPGDownloader Lite. Select a Single Tone waveform.

.. image:: ../images/ad9081_12_dpgl_setup1.png
   :alt: Selecting a Single Tone in DPG Lite
   :width: 200

Configure the DPG Lite GUI as shown below. The steps necessary for the setup
are enumerated.

.. image:: ../images/ad9081_13_dpgl_setup2.png
   :alt: DPG Lite Setup for Single Tone

After enabling the DAC output by pressing the "Play" button in DPG Lite, use a
SMA cable to connect DAC0 output to ADC3 input on the AD9081-FMCA-EBZ.
Capture an FFT in ACE.

.. image:: ../images/ad9081_14_st_fft_3p201ghz_dac0_loop_adc3_0dbfs.png
   :alt: DAC0 to ADC3 External Loopback

Below is a screenshot of the ADC FFT with simultaneous capture of all four
channels. ADC1 is sampling the signal generator output. ADC3 is sampling the
DAC0 output.

.. image:: ../images/ad9081_15_two_channel_outputs.png
   :alt: Two channel outputs

Setting up MxFE™ in a Wideband mode
-------------------------------------------------------------------------------

The following instructions allow the user to setup the MxFE chip in a single
band 1000MSPS I/Q data rate setup with direct RF sampling. The majority of the
instructions are similar to the Narrowband use case. The device is setup as
shown below:

.. image:: ../images/ad9081_wideband_setup_for_wiki.png
   :alt: Setup block diagram of AD9081
   :align: center

Configuring the device in ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only showing the Quick configuration section with the appropriate inputs to
setup the AD9081 in wideband mode.

.. image:: ../images/ad9081_1_jesd204_setup.png
   :alt: AD9081 JESD204 quick config setup 1
   :align: left

.. image:: ../images/ad9081_2_clock_config1.png
   :alt: AD9081 JESD204 quick config setup 2
   :align: right

.. image:: ../images/ad9081_3_clock_config2.png
   :alt: AD9081 JESD204 quick config setup 3
   :align: center

.. image:: ../images/ad9081_7_apply.png
   :alt: Apply button
   :align: center

Allow a few seconds for ACE and the ADS9v2 hardware to setup the AD9081.

Setting up DPG Lite to generate a tone out of the DAC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setup DPG Lite for single tone as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/4_dpgl_setup.png
   :alt: Selecting a Single Tone in DPG Lite

Obtaining an FFT from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect a signal generator to any of the ADC inputs. Set the frequency to a
3.207GHz CW tone.

Click on "Proceed to Analysis" button to capture an FFT from the ADC.

|FFT output|

Setting up AD9081/AD9988 in a 4T4R Dual-Band setup
-------------------------------------------------------------------------------

The AD9081/AD9988 and AD9082/AD9986 have flexible digital signal processing
(DSP) that allows it to act as a 4T4R (4 transmit and 4 receive) transceiver for
multiband radios. Below is an example showing the AD9081/AD9988 in a multiband
setup, where the device processes LTE bands 1 and 4. The band details are shown
below

+----------+-----------------+--------------+------------------+--------------------+
| **Band** | **Duplex Mode** | **f\ (MHz)** | **Uplink (MHz)** | **Downlink (MHz)** |
+==========+=================+==============+==================+====================+
| 1        | FDD             | 2100         | 1920 - 1980      | 2110 - 2170        |
+----------+-----------------+--------------+------------------+--------------------+
| 4        | FDD             | 1700         | 1710 - 1785      | 1805 - 1880        |
+----------+-----------------+--------------+------------------+--------------------+

For optimal performance of the AD9081/AD9988 in a direct RF conversion mode, it is essential to have a good frequency plan. In this example, a DAC sample rate (*f*\ :sub:`DAC`) of 4.9152GHz and an ADC sample rate (*f*\ :sub:`ADC`) of 2.4576GHz. The frequency plan of the receive path (ADC) is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/multiband_frequency_plan.png
   :alt: Receive (ADC) frequency plan with Bands 1 and 4
   :width: 400

To support the dual band operation, the AD9081/AD9988 will need to be configured
as shown below. Please note that the AD9081-FMCA-EBZ and AD9988-FMCB-EBZ have
different standard crystal oscillators. The AD9988-FMCA-EBZ has an on-board
122.88MHz crystal, and therefore can be configured using ACE, on-board HMC7044,
and on-chip PLL. For the example below, the AD9081-FMCA-EBZ was modified to use
a direct external clock, bypassing the HMC7044 and on-chip PLL. Refer to the
Evaluation Board User Guide (UG-1829) for more details.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/mxfe_setup_for_multiband.png
   :alt: AD9081 / AD9988 Multiband setup details

ACE setup details for dual-band transceiver operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps below to configure AD9081/AD9988 in the ACE GUI. The Quick configuration setup summary is shown in the screenshots below. Please note that in this example, a direct external clock was used. Please refer to :adi:`UG-1829 <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>` for details on how to run the evaluation board using an external clock source.

|image8|\ |image9| |image10|\ |image11|

Below is an FFT of the ADC sampling a 1.7325GHZ CW tone

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/1p7325ghz.png
   :alt: ADC sampled output of 1.7325GHz CW tone

and the ADC sampling a 1.95GHZ CW tone

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/1p95ghz.png
   :alt: ADC sampled output of 1.95GHz CW tone

Setting up transmitter in DPG Lite dual-band operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the spectrum of the DAC output two tones representing the center
frequencies of the two bands.

|DAC outputs showing the center frequencies of the two bands|

A Note on ADC performance
-------------------------------------------------------------------------------

The AD9081/AD9988/AD9082/AD9986 are highly integrated direct RF transceivers. Hence, the performance of the ADC may vary based on the device setup. For example, if the AD9082-FMCA-EBZ was setup to run in a transceiver mode (with DACs ON), and receive only mode (ADC only), there will be a noticeable difference in the ADC's noise performance. See below: |2.7GHz -1dBFS tone with AD9082 configured as a transceiver|\

|2.7GHz -1dBFS tone with AD9082 configured in Rx only mode|

AD9081/82 Programmable Filter (PFILT)
-------------------------------------------------------------------------------

This section of the user guide talks about how to run the MATLAB code for the
BPF compensation filter design and use the coefficients generated from it to
load the PFILT on AD9082-FMCA-EBZ board using ACE plug-in. The same technique
can be applied to the other evaluation boards listed above, as well. In this
document we are considering that you have a working set up of the
AD9082-FMCA-EBZ with following instructions from UG-1829 as listed under the
Documents needed section. Please refer to UG-1829 for hardware needed, how to
load ACE software and the required plug-in for using the AD9082-FMCA-EBZ.

**Where to start PFILT design – to equalize the response using the PFILT. How to download the MATLAB model for PFILT?** For documentation on the MATLAB support refer to this Wiki page: `Hsx Toolbox <https://wiki.analog.com/resources/tools-software/hsx-toolbox>`_ Please download the entire toolbox with the link off the main README: :git-HighSpeedConverterToolbox:`README.md` Then all the helper functions are on path. You can download the toolbox directly within MATLAB through Addon Explorer or grab the source from GitHub. This is documented here: https://wiki.analog.com/resources/tools-software/hsx-toolbox. This MATLAB support is provided through ADI's High Speed Converter Toolbox. Click on this link below on GitHub `HighSpeedConverterToolbox <https://github.com/analogdevicesinc/HighSpeedConverterToolbox>`_ and use the green button code as shown below to download the Compensation Filter folder under hsx_examples/mxfe_sim/

|HighSpeedConverterToolBox under GitHub| Figure 2: HighSpeedConverterToolBox under GitHub

Under the Compensation Filter Folder you should see the following:

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure3.png
   :alt: Compensation Filter Folder view under HighSpeedConverterToolBox
   :align: center

::

   Figure 3: Compensation Filter Folder view under HighSpeedConverterToolBox

This document uses the MxFEADCCompensationFilterDesign_BPF.m MATLAB code.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure4.png
   :alt: BPF MATLAB code view under MATLAB
   :align: center

::

   Figure 4: BPF MATLAB code view under MATLAB

You can either use the Run on the Editor Tab.Or Run individual sections on the
Editor Tab.

The MATLAB code uses the input response of the ADC in the file
“MXFE_ADC_Response” When you run the MATLAB code for the BPF you will get this
output response below, which we are interested in. We define the Pass Band and
the 2 Stop Bands for this ADC response. We then generate the target response
similar to the red trace in the figure. This is the filter that is generated. It
is the one in red which is the magnitude compensation filter. The composite
response is the one in yellow. This is for 192 tap BPF filter per channel.

|BPF Compensation Filter Response| Figure 5: BPF Compensation Filter Response

This is the output response that we try to replicate on the bench measurements
using the AD9082-FMCB-EBZ. The MATLAB code also generated this figure below
which defines the target response for the 2 Stop bands and Pass bands.

|Target Responses for the BPF Compensation Filter design| Figure 6: Target Responses for the BPF Compensation Filter design

When you type on the command window, “xt”, you will get the coefficient values
as shown below: It generates coefficients to load into PFIR on MxFE using the HW
 AD9082-FMCB-EBZ. The coefficient format generated in MATLAB is in decimal
format.

It needs to be converted to 2's complement and then to Hex Format prior to
loading it to the PFILT on AD9082-FMC-EBZ hardware using ACE plug-in

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure7.png
   :alt: Coefficient values in Decimal format generated from the MATLAB code for the BPF
   :align: center

::

   Figure 7: Coefficient values in Decimal format generated from the MATLAB code for the BPF

The coefficient /taps are generated from MATLAB. These are in decimal format.
Prior to loading into ACE, these need to be converted to 2's complement first
and then to Hex format. Example of how the coefficient file looks like after
converting into Hex. It is a text file and below is an excerpt from a
coefficient file for a bandpass, 192 tap filter.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure8.png
   :alt: Excerpt from a Coefficient file for PFILT loading
   :align: center

::

   Figure 8: Excerpt from a Coefficient file for PFILT loading

In this document we are considering that you have a working set up of the
AD9082-FMCB-EBZ with following instructions from UG-1829 as listed under the
Documents needed section. Once you have a working set up of the AD9082-FMCB-EBZ,
please use the last ADC Full Bandwidth condition shown under Table 2 of Page 11
of the UG-1829.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure9.png
   :align: center

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure9r.png
   :alt: Board View of selected Full Bandwidth ADC Use Case
   :align: center

::

   Figure 9: Board View of selected Full Bandwidth ADC Use Case

You can check the FFT response of the signal without PFILT:

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure10.png
   :alt: FFT of the signal @0.5GHz to ADC input, without PFILT
   :align: center

::

   Figure 10: FFT of the signal @0.5GHz to ADC input, without PFILT

**How to load the generated coefficients by MATLAB code in the ACE Tool?** 1.Design Band pass filter in MATLAB PFILT tool to equalize the ADC input: For a 192 tap single real mode PFILT: Use the following settings under Quick Configuration tool in Chip view for AD9082 board. You get to the chip view by click on the highlighted box in green in the figure below

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure11.png
   :alt: AD9082 Board view under ACE Plug-in
   :align: center

::

   Figure 11: AD9082 Board view under ACE Plug-in

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure12.png
   :alt: AD9082 Chip view under ACE Plug-in
   :align: center

::

   Figure 12: AD9082 Chip view under ACE Plug-in

**Configuring the Programmable Filter in ACE: 1.Click the programmable filter block in chip as highlighted in the picture below.**

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure13.png
   :alt: Programmable Filter Configuration Pop-up Window
   :align: center

::

   Figure 13: Programmable Filter Configuration Pop-up Window

2.The settings shown in the Programmable filter configuration shows for AD9082
TxFE. As, TxFE only has two ADCs. If it AD9081, under PFILT Quad mode selection
we need to choose PFilter Quad mode. We have selected Real N Tap Filter for
PFILT I mode and PFILT Q Mode is disabled.

3.Depending on whether, PFilter I Mode or PFilter Q Mode is selected, then the
PFILTER Coefficient Load select should be Real I Load or Real Q load.

4.Under Analysis window, Channel 0 is I data, Channel 1 is Q data.

5.Under select the PFilter coefficient file, load the coefficient file. The
coefficients needs to be in Hex Format when we upload them in ACE. So we convert
the coefficients generated from MATLAB from Decimal  2's complement Hex Format
before loading into ACE.

6.Once the coefficient file is loaded, click the Configure Filter Block under
the chip view. Please note that it takes several seconds to complete loading the
coefficients into the PFILT block.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure14.png
   :alt: Configure PFilter
   :align: center

::

   Figure 14: Configure PFilter

7.Now proceed to Analysis by click at the “Proceed to Analysis” button at the
bottom of the chip view page.

8.Below is the FFT plot at sampling frequency of 3Gsps and input to the ADC is
0.5GHz.

Showing Channel 0 which I Mode.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure15.png
   :alt: FFT plot at sampling frequency of 3Gsps
   :align: center

::

   Figure 15: FFT plot at sampling frequency of 3Gsps

This FFT plot correlates to the MATLAB compensation filter response shown in
Figure 5.

If you select the Channel 1 which is Q channel and as Q mode is disabled for the
selected 192 tap single real PFilter configuration. So no signal seen on the FFT
plot below.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure16.png
   :alt: FFT plot Channel 1 which is Q channel with Q mode Disabled under PFILT Configuration Tool
   :align: center

::

   Figure 16: FFT plot Channel 1 which is Q channel with Q mode Disabled under PFILT Configuration Tool

9.Under the configuration window for PFILT, if you select the PFILT Q mode and
disable the PFILT I mode. Then the FFT plot for Channel 1 will be showing the
signal transmission as below:

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure17.png
   :alt: FFT plot Channel 1 which is Q channel with Q mode Enabled under PFILT Configuration Tool.
   :align: center

::

   Figure 17: FFT plot Channel 1 which is Q channel with Q mode Enabled under PFILT Configuration Tool.

Troubleshooting Tips
-------------------------------------------------------------------------------

\*\* Evaluation Board is not Functioning Properly \*\*

- Ensure that the evaluation board is properly seated in the FMC connector
- After ACE has programmed the FPGA, power is provided to the evaluation board.
   Ensure that the LEDs that denote power is ok, are all lit. See image below.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/ceboard_power_rail_led.jpg
   :alt: LEDs denoting power to the various rails on the evaluation board
   :width: 200

- Ensure that the eRPC server has made a successful connection to the
   evaluation board. If the Chip Info reads back a successful UID, this means
   that the connection is successful. Otherwise, the UID will read 0x0 (see
   Figure 11). If this is the case, power cycle the board, and restart all
   software.

\*\* ACE is slow to capture data and setup the board \*\*

- Ensure that the USB connection between :adi:`ADS9-V2EBZ` board and the PC is done through a USB3.0 cable.
- Connect the cable to a USB3.0 supported port on the PC
- Restart all software and hardware

\*\* Unable to capture data after device is setup \*\*

In some instances, the user may be unable to capture data from the FPGA. This is
characterized by no capture via ACE, or a “configure channel failed” error in
ACE. In either case, only four of the six LEDs on the FPGA board will be lit
(see figure below).

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/ads9v2_unsuccessful_capture.jpg
   :alt: LED status on ADS9-v2EBZ following an unsuccessful data capture
   :width: 200

If this happens, and the setup is using an external direct clock to the chip,
ensure that the instrumentation is setup as explained in the evaluation board
user guide UG-1829. Ensure the correct clock and refclock frequencies are set.
Check the connections to the board to make sure they are snug. If the problem
persists, open DPG Lite and download a tone. After this step, a successful data
capture will show all the LEDs lit. See figure below.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/ads9v2_successful_capture.jpg
   :alt: LED status on ADS9-v2EBZ following a successful data capture
   :width: 200

\*\* HMC7044 Configuration Error \*\*

When operating with the on-board clocking and on-chip PLL mode, the user can get
a “HMC7044 Configuration Error” in the ACE setup.

.. image:: https://wiki.analog.com/_media/resources/eval/mxfe/hmc7044_config_error.png
   :alt: HMC7044 Configuration Error (REFCLK value cannot be supported using a 100MHz Crystal Oscillator)
   :width: 200

If this happens, ensure the correct modes are selected to setup the chip. Please
note that not all modes that are listed in the UG-1578, device user guide, are
supported by the evaluation board hardware using the on-board HMC7044 clock and
on-chip PLL. This is because the HMC7044 derives the reference from a 100MHz
crystal oscillator if using the FMCA version, or 122.88MHz crystal oscillator if
using the FMCB version of the evaluation board.

If this use case is required, the best approach is to switch to using the direct
external clock. This bypasses the HMC7044 setup and the user is not limited to
the setup options provided only by the combination of on-board crystal
oscillator and the HMC7044 setup.

\*\* ACE Does Not Auto-Detect the Hardware \*\*

After powering up the :adi:`ADS9-V2EBZ` FPGA board and starting ACE, the hardware will
be auto-detected and the plugin icon should appear in the GUI as shown at the
top of the "Configuring the device in ACE" section. In the unusual case that the
hardware is not detected and the plugin icon does not appear, try a different
USB3 cable before going to the trouble of reinstalling the plugin, or
reinstalling the whole ACE package.

Automating ACE with MATLAB
-------------------------------------------------------------------------------

User Guide: `ad9xxx_matlab_user_guide.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad9xxx_matlab_user_guide.pdf>`_

Code: `ad9xxx_matlab_code.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad9xxx_matlab_code.zip>`_

.. |FFT output| image:: https://wiki.analog.com/_media/resources/eval/mxfe/5_fft_output.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/mxfe/11.png
   :width: 200
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/mxfe/21.png
   :width: 200
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/mxfe/31.png
   :width: 200
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/mxfe/41.png
   :width: 200
.. |DAC outputs showing the center frequencies of the two bands| image:: https://wiki.analog.com/_media/resources/eval/mxfe/dac_output_dualband.png
.. |2.7GHz -1dBFS tone with AD9082 configured as a transceiver| image:: https://wiki.analog.com/_media/resources/eval/mxfe/ad9082_2p7ghz_adconlyfft.png
   :width: 600
.. |2.7GHz -1dBFS tone with AD9082 configured in Rx only mode| image:: https://wiki.analog.com/_media/resources/eval/mxfe/ad9082_2p7ghz_trxmodefft.png
   :width: 600
.. |HighSpeedConverterToolBox under GitHub| image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure2.png
.. |BPF Compensation Filter Response| image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure5.png
.. |Target Responses for the BPF Compensation Filter design| image:: https://wiki.analog.com/_media/resources/eval/mxfe/figure6.png

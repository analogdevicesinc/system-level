.. imported from: https://wiki.analog.com/resources/eval/user-guides/mykonos/software/filters

.. _mykonos software filters:

MATLAB Profile Generator for AD9371
===================================

The AD9371 Filter Design Wizard is used to design the transmitter and receiver
FIR filters for the AD9371 product family. It can also be used with the AD9375
device. This tool creates filters which equalize the desired passband, taking
into account the signal transfer functions through the entire analog and digital
signal path in the AD9371 transceiver. The tool also generates ADC profiles and
custom clock settings that can be used with the Transceiver Evaluation Software
to evaluate system performance. Any custom configuration of sampling rates and
bandwidths must use this tool to create a profile that can be used by in a
customer system or with the evaluation kit. The Filter Wizard is available as
MATLAB source code, a MATLAB app, and as a stand-alone executable.

With this wizard, users can perform the following tasks:

- Design the programmable FIR filters, get the filter coefficients and save them
  to a file, which can be directly loaded into the hardware.
- Examine the independent response of each filter, and the composite response of
  all the filters in a channel, including both digital and analog filters.
- Generate custom clock settings that can be used to evaluate performance of
  using different device clock inputs and sample rates.

Revision List, Change Log, Known Limitations
--------------------------------------------

See Release Notes Document
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/ad9371_filter_wizard_release_notes_v1.10.rtf`

Use MATLAB App
--------------

There are three ways you can use the AD9371 Filter Wizard:

- Executable : the executable includes the exe which allows the wizard to run as
  a separate application without requiring the MATLAB program to be running. The
  program provides a GUI that allows users to define the input parameters,
  generate filters, view the output results, and save all output parameters for
  their own use or use in the ADI EVB GUI software. To run this as a stand alone
  application, the MATLAB runtime engine needs to be installed (see link below).
  The runtime engine can take more than a minute to start up the first time it
  is run, so please be patient while it initializes.

The MATLAB runtime engine can be downloaded from the following link:
:mw:`products/compiler/mcr.html <products/compiler/mcr.html>`

- MATLAB App : the app runs as an application within MATLAB. Use of the app
  requires MATLAB to be running with valid licenses for the Control System
  Toolbox as well as MATLAB itself. The GUI and flexibility are identical to the
  executable, but running as an app in MATLAB allows the user to write
  additional code to post-process the data files created by the wizard.
- MATLAB source code (function) : These are MATLAB functions which users can
  launch from the MATLAB command window by properly defining the input
  parameters. Used this way, users have more control of the internal design
  process.

The executable is available here:
:ez:`rf/wide-band-rf-transceivers/design-support-ad9371/w/documents/18048/ad9371-75-filter-wizard-setup-file-faq <rf/wide-band-rf-transceivers/design-support-ad9371/w/documents/18048/ad9371-75-filter-wizard-setup-file-faq>`

The source code is available here:
:ez:`rf/wide-band-rf-transceivers/design-support-ad9371/m/file-uploads/2924 <rf/wide-band-rf-transceivers/design-support-ad9371/m/file-uploads/2924>`

This section elaborates on the first two options, the executable and the App,
and addresses both identically since the input and output functionality is the
same.

Using the MATLAB App and Exe
----------------------------

This section describes the user interface of the AD9371 Filter Wizard.

The first screen visible after starting the Wizard includes an Instruction
screen in the center with the input parameters on the left side and is shown in
the picture below:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/welcome_page.jpg

Please read through the short text on the Instruction tab before using the
wizard. Note also the links at the bottom, one of which takes you back to this
Wiki page and the other takes you to the ADI Engineer Zone forum. Any questions
about the Wizard will be addressed in this forum.

The Instructions page is one of several tabs in the GUI. The other tabs are used
to display filter responses for each channel type after clicking on ``Generate
Profiles`` as described below.

It"s important to understand that while the AD9371 has separate transmitter,
receiver, observation receiver, and sniffer receiver signal paths, all of their
digital filters and data converters receive their clocks from a common clocking
system, referred to as the Clock PLL (and dividers). Even though the input
fields show user configurable sampling rates for each of the different sections,
there are rules that must be followed in order to generate a configuration that
the AD9371 can use. Some examples of invalid configurations that illustrate the
following rules are shown further down this page.

The complete set of rules used by the GUI is also listed further down this Wiki
page.

#. The Tx Input Sample Rate must be the same as the ORx Output Sample Rate as
   internal and external AD9371 calibrations require these rates to be the same
#. The ORx Output Sample Rate must be a power of 2 multiple of the Rx Output
   Rate to satisfy JESD204B requirements
#. The Tx Synthesis (total) bandwidth must be less than 82% of the Tx sample
   rate
#. The ORx RF BW must be greater than 33% and less than 82% of the ORx sample
   rate
#. The Rx RF BW must be greater than 33% and less than 82% of the Rx sample rate

The ``Tx Input Sample Rate`` is the data rate of the ``I`` and ``Q`` samples.
This is the data rate output from the baseband processor to the AD9371. These
samples are serialized and sent across the JESD204B interface. Once deserialized
by the AD9371, the data rate input to the filtering blocks in the AD9371 is this
same ``Tx Input Sample Rate``.

**Tx Profile** Section Tx Total RF BW and the Tx Primary Signal BW. The Tx Total
RF BW in MHz is the total bandwidth used primarily by PA linerization algorithms
such as digital predistortion. It is also referred to in user guides and the
Wizard error messages as the ``synthesis`` bandwidth. It is expected that
signals outside of the ``Primary Signal BW`` but inside the ``Total RF BW`` will
be lower in level than the primary signals levels. As an example, a desired
signal may occupy 18 MHz of bandwidth and an FPGA predistortion algorithm may
linearize five times beyond that signal to reduce undesired emissions. The
primary BW would then be 18 MHz and the total BW would be 90 MHz.

The ``Pass Band Weight`` and ``Stop Band Weight`` are configurable. These values
are used to create a ratio. If the ratio is ``1``, then equal weighting is given
to achieving low passband ripple and high stopband attenuation. The Wizard will
use all FIR taps it has available to achieve this. Typical ripple values are
less than 0.5 dB and typical attenuation values are greater than 50 dB. A
specific configuration may make it difficult to generate a FIR filter with both
expected ripple and attenuation performance. It may also be desirable to have
better attenuation than the program generates by default. Changing the ratio of
weights alters the emphasis the Wizard places on meeting its objectives. For
example, changing the ratio by setting the Stop Band Weight to ``100`` will
sacrifice some passband ripple but improve the stop band attenuation. It is
difficult to quantify a ratio that always results in the same amount of emphasis
and de-emphasis. If the Wizard can easily achieve good ripple and attenuation as
mentioned above, then a ratio of 10:1 can make a significant difference in the
results. If the change in filter performance is not large enough, increase the
ratio. The values are real numbers so setting the weights to 1:10 (passband to
stopband) is the same as setting them to 0.1:1.

Next is the **ORx Profile** section. The ORx signal path input is intended to be
used with PA linearization algorithms as mentioned above. While the main receive
path (see below) is intended just for the desired signal, the ORx path was
designed for use with PA linearization algorithms. It can support a wider
bandwidth than the main Rx path because it is feeding back the desired signal
plus the spectral regrowth to the baseband processor. The spectral regrowth is
usually at least 2 times and occasionally as much as five times the bandwidth of
the desired signal received by the main receive path.

The sample rate is the output data rate sent to the JESD204B serializer.

The RF BW is the complex bandwidth used by the ORx signal path.

Weighting is described in the Tx section.

The **Rx Profile** section is next. Sample rate, bandwidth, and weighting are
described in previous sections.

The **SnRx Profile** section allows for configuration of the sniffer receiver
signal path. The maximum bandwidth of this path is 20 MHz and the maximum
sampling rate is 30.72 MSPS. Otherwise, the user-configurable fields are as
described in previous sections.

The defaults populated at startup will generate valid FIR filters if the user
merely presses the ``Generate Profiles`` button. The window to the right will
show the resulting composite response for the entire signal path as well as
responses for the various blocks within the chip.

An example of the Tx response using the default profile at startup is shown
below with the maximum ripple called out at the top left of the graph:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/tx.jpg

The same for the default Rx configuration is shown here:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/rx.jpg

An example of changing the Rx main signal path weighting to have a stop band
weight of 100 results in the following response:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/rx_sbw100.jpg

If the Tx Total (or Synthesis) bandwidth is larger than 82% of the Tx sample
rate, then the Wizard will indicate this with red text at the bottom of the
Wizard as well as a pop up window as shown below:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/tx_error_oor.jpg
   :width: 300px

As mentioned above, if the Tx sample rate and the ORx sample rates are not the
same, the AD9371 calibrations will not function properly. The Wizard will not
let such a profile be generated and will indicate this with red error text at
the bottom of the Wizard as well as a pop up window as seen here:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mykonos/software/tx_error_samplerate.jpg
   :width: 300px

When you click on the ``Output Profile to Files`` button, wizard generates four
files as described below

#. <file_name>.txt - Used for configuring AD9371 in GUI and script generation
#. <file_name>_AD9528.txt – Used for configuring AD9528 using TES GUI only, it
   will be generated if box is checked against ``Write AD9528 settings to File``
   option.
#. <file_name>_orxadc.txt – Used by GUI for plotting ORX ADC STF response only
#. <file_name>_rxadc.txt - Used by GUI for plotting RX ADC STF response only

AD9371 Filter Wizard Rules
--------------------------

- Tx Rules

  - 30 MSPS < = Tx Input Sample Rate < = 320 MSPS
  - 10 MHz < = Tx Primary Signal BW < = 100 MHz
  - 20 MHz < = Tx RF (Synthesis) BW < = 240 MHz
  - Tx Primary Signal BW < = Tx RF (Synthesis) BW

::

   *Tx Primary Signal BW < 0.33* Tx Input Sample Rate
   *Tx Synthesis BW < 0.82* Tx Input Sample Rate
   * 370 MHz < = DAC Clock Rate <= 640 MHz
   * Tx FIR number of coefficient options: 16, 32, 48, 64, 80 (max number may be less than 80 due for high sample rates)
   * Tx Input Sample Rate = ORx Output Sample Rate
   * Tx FIR decimation options: 1, 2, 4 (NOTE: 4 not currently supported by Wizard; to be added in future release)
 * Rx Rules
   * 20 MSPS < = Rx Output Sample Rate < = 200 MSPS
   * 8 MHz < = Rx Signal BW < = 100 MHz
   *Rx Signal BW > = 0.4* Rx Output Sample Rate
   *Rx Signal BW < = 0.82* Rx Output Sample Rate
   * 800 MHz < = ADC Clock Rate < = 1600 MHz when using the "decimate-by-five"
     stage after the ADC
   * 800 MHz < = ADC Clock Rate < = 1280 MHz when using the "decimate-by-four"
     stages after the ADC (currently not supported)
   * Rx ADC clock rate must equal the ORx ADC clock rate which implies that the
     Rx and ORx sampling rates must be related by a power of 2 at a minimum and,
     depending on the filters which can be enabled and bypassed, possibly even
     more tightly contrained
   * Rx FIR number of coefficients: 24, 48, 72 (maximum may be less than 72 for
     higher sampling rates)
   * Rx FIR decimation options: 1, 2, 4
 * ORx Rules
   * 8 MHz < = ORx Signal BW < = 240 MHz
   * 20 MSPS < = ORx Output Sample Rate < = 320 MSPS
   *ORx Signal BW > = 0.4* ORx Output Sample Rate
   *ORx Signal BW < = 0.82* ORx Output Sample Rate
   * 800 MHz < = ADC Clock Rate < = 1600 MHz when using the "decimate-by-five"
     stage after the ADC
   * 800 MHz < = ADC Clock Rate < = 1280 MHz when using the "decimate-by-four"
     stages after the ADC (currently not supported)
   * ORx FIR number of coefficients: 24, 48, 72 (maximum may be less than 72 for
     higher sampling rates)
   * ORx FIR decimation options: 1, 2, 4
   * Tx Input Sample Rate = ORx Output Sample Rate

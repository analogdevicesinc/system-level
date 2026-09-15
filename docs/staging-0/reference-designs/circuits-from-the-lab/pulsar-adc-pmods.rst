.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods

.. _circuits-from-the-lab pulsar-adc-pmods:

PulSAR ADC PMODs
================

These low power ADCs offer very high performance from 14-bits up to 18-bits with
throughputs ranging from 100 kSPS to 1.3 MSPS. The boards are designed to
demonstrate the ADC"s performance and to provide an easy digital interface for a
variety of system applications. A full description of these products is
available in their respective data sheets and should be consulted when utilizing
the boards. To purchase hardware, please visit our
:adi:`website. <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/PulsarPMODs.html>`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pulsar_pmod.jpg
   :width: 500px

The products which have PMOD boards associated with them can be found in the
table below.

.. list-table::
   :header-rows: 1

   * - Products
     - Resolution
     - ADC Throughput\*
     - Input Stage
     - Driver Amplifier
     - PMOD Part Number
   * - :adi:`AD7942`
     - 14-Bit
     - 250 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7942-PMDZ`
   * - :adi:`AD7946`
     - 14-Bit
     - 500 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7946-PMDZ`
   * - :adi:`AD7988-1`
     - 16-Bit
     - 100 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7988-1-PMDZ`
   * - :adi:`AD7685`
     - 16-Bit
     - 250 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7685-PMDZ`
   * - :adi:`AD7687`
     - 16-Bit
     - 250 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7687-PMDZ`
   * - :adi:`AD7686`
     - 16-Bit
     - 500 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7686-PMDZ`
   * - :adi:`AD7688`
     - 16-Bit
     - 500 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7688-PMDZ`
   * - :adi:`AD7693`
     - 16-Bit
     - 500 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7693-PMDZ`
   * - :adi:`AD7988-5`
     - 16-Bit
     - 500 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7988-5-PMDZ`
   * - :adi:`AD7980`
     - 16-Bit
     - 1000 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7980-PMDZ`
   * - :adi:`AD7983`
     - 16-Bit
     - 1333 kSPS
     - Unipolar, Single-Ended Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7983-PMDZ`
   * - :adi:`AD7690`
     - 18-Bit
     - 400 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7690-PMDZ`
   * - :adi:`AD7691`
     - 18-Bit
     - 250 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7691-PMDZ`
   * - :adi:`AD7982`
     - 18-Bit
     - 1000 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7982-PMDZ`
   * - :adi:`AD7984`
     - 18-Bit
     - 1333 kSPS
     - Unipolar, Differential Input
     - :adi:`ADA4841`
     - :adi:`EVAL-AD7984-PMDZ`

.. note::

   * The throughput of your PulSAR ADC will be limited to the SPI bus speed of
     your platform. For example, if you are using the SDP platform the max bus
     rate on the SPI is 30 MHz.

Hardware Setup
--------------

The PMOD board is small in size with dimensions approximately 1 inch in width by
3 inches in length. There are a few areas of the hardware I"d like to point out
for you, in order to use the board.

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

Typically, when using a PMOD board the power for the module comes directly from
the host board it is connected to. The power is generally capable of providing
up to 100 mA at 3.3V, and for complete power specifications please
`click here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`__.

In the case of the high precision, successive approximation ADC"s architecture,
it was required to provide low noise external power supplies to obtain datasheet
results. The ADC"s are driven by precision amplifiers which are also optimized
for noise and power. In order to enable those amplifiers to provide zero and
full scale inputs to the ADC, power supplies above and below the ADC input range
were needed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pmod_power_supplies.png
   :width: 500px

With all these factors combined, the board was designed using external power
supplies of -2.5V, GND (of course), and 7.5V. These supplies provide the power
for the entire PMOD board, so even though power is coming in through the PMOD
connector, it"s not actually powering the components on the board.

Input Connectors
~~~~~~~~~~~~~~~~

For the input signals coming into the PMOD board, SMB connectors were chosen to
help minimize the noise at the input. There are two (2) SMB connectors per
board, and thats because there are both positive(+) and negative(-) inputs to
each converter. This will provide the user with the cleanest input signal
possible, and fully utilize the resolution and speed of the converters.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/vin.png
   :width: 500px

Each of the converters also has a combination of single-ended inputs,
differential inputs, or pseudo-differential inputs. So in order to determine the
input style of your converter it is imperative to look at the datasheet of the
device you are using. The datasheet of any device should always be followed
before using it in an application or on a board.

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

The PMOD interface is a series of standardized digital interfaces for various
digital communication protocols such as SPI, I2C, and UART. These interface
types were standardized by Digilent, which is now a division of National
Instruments. Complete details on the PMOD specification can be found
`here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`__.

The specific interface used for the PulSAR PMOD boards is the extended SPI. In
general ADI has adopted the extended SPI connector for all PMOD devices which
have an SPI interface. It provides flexibility to add interrupts, general
purpose I/O, resets, and other important digitally controlled functions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pmod_pinout.png
   :width: 700px

Above is the connection to each of the PulSAR PMOD boards to the SPI PMOD
connector. Each of the PulSAR PMOD boards is hardware configured in a 3-wire
mode with no busy indicator. This configuration can be better explained in the
datasheet if you desire to learn more. This basically means that the only
signals that go between the converter and the processor are the CNV (similar to
a chip select in this mode), SCLK (serial Clock), and MISO (serial data out).
There are no registers internal to the PulSAR ADC"s, so there is no need for a
data input line, the data just streams out using the CNVST pin.

Getting Started
---------------

Using any of the PulSAR ADC PMOD boards is very simple. To get started
evaluating the ADCs, you are going to need the following equipment:

-
  :adi:`EVAL-AD7xxx-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/PulsarPMODs.html>`
  PMOD board (whichever version you are interested in)
-
  :adi:`EVAL-SDP-CB1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SDP-B.html>`
  (If you order this from the website it also includes the Mini USB Cable)
-
  :adi:`SDP-PMD-IB1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL_SDP-PMOD.html>`
  (If you order this from the website it also includes the EVAL-CFTL-6V-PWRZ)
- :adi:`EVAL-CFTL-6V-PWRZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CFTL-6V-PWRZ.html>`
- PC with Windows (.NET 3.5 or higher)
- Mini USB Cable

Evaluation
~~~~~~~~~~

Evaluating the PulSAR ADC PMOD boards is very simple. Using the required
equipment, follow these simple steps to get the evaluation working. Please make
sure you completely unplug all the boards before beginning.

#. Plug in the Mini USB cable from a USB port on your PC, to the **J1** of the
   EVAL-SDP-CB1Z.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/sdp_usb.jpg
      :width: 400px

- Make sure that the computer installs the device drivers, and that you can see
  the *ADI Development Tools* in your computer"s device manager.

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/device_manager.png
    :width: 500px

#. Ensure that you remove the shunt which is located at **JP1** of the
   SDP-PMD-IB1Z

#. Next take the EVAL-SDP-CB1Z board and connect **CON A** up to **J4** of the
   SDP-PMD-IB1Z interposer board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/sdp_usb_interposer.jpg
      :width: 500px

#. Connect the EVAL-CFTL-6V-PWRZ to **J1** barrel jack of the SDP-PMD-IB1Z, and
   **WAIT 10 SECONDS** before continuing

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/sdp_usb_interposer_power.jpg
      :width: 500px

#. Take the PulSAR ADC PMOD board you are using and connect it to **J3** of the
   SDP-PMD-IB1Z interposer board. This should finish the hardware setup.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/sdp_evaluation_combo.jpg
      :width: 700px

#. With the power source turn **OFF**, connect your external power supplies
   (-2.5V, GND, and 7.5V) to the terminal block of your EVAL-AD7xxx-PMDZ board.
#. Turn **ON** your external power supplies (-2.5V, GND, and 7.5V) connected in
   the previous step.

#. Place the shunt across **JP1** of the SDP-PMD-IB1Z, according to the
   silkscreen so that you will have 3.3V going to the PMOD connector.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/sdp_usb_interposer_power_jumper.jpg
      :width: 500px

#. Check again in the device manager to make sure the *ADI Development Tools*
   are still displaying. If yes, then you"ll be able to proceed onto the
   evaluation software section. If you don"t see ADI Development Tools, than you
   will have to start the hardware evaluation procedure over at step 1.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/device_manager.png
      :width: 500px

#. Connect your SMB cable from your signal source to the Vin+ and Vin-
   connectors of the EVAL-AD7xxx-PMDZ board.

Labview Software Application (GUI explained)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PulSAR ADC PMOD boards have a special version of software needed to run the evaluation, so please install this version of the software. .. admonition:: Download

   :dokuwiki:`PulSAR ADC PMOD Evaluation Software <ftp://ftp.analog.com/pub/cftl/EVAL-ADXXXX-PMDZ/1.0.0/>`

Once you download and install the software, you"ll be able to launch the
application and communicate with the hardware setup. When you open up the
application the front screen will look like the following:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/software_panel_numbered.png
   :width: 700px

The following is the description of how to use the user panel:

#. Select Supply Voltage

- The user must select either the 5.0V or 2.5V selection from the menu, that
  corresponds with the ADC supply voltage (VDD) of the PulSAR ADC PMOD they are
  using. This choice will limit the selections you can make under the *Select
  ADC* section.

#. Select ADC

- Please select the part number of the PulSAR ADC you are using. If your
  converter selection appears to be ``grayed out``, please go back to step one
  and make sure you have the correct supply voltage selected.

#. Sampling Frequency

- The user can set the desired sampling frequency, however the user cannot go
  beyond the max sampling frequency of the converter (shown just below in the
  panel). Units are entered in Hz , so you must type out all significant digits.
  (For example - 250 kHz must be typed out as ``250000``)

#. Number of Samples

- This drop down tells the software how many samples you want to take. Those
  samples will be used to make the waveform, histogram, and FFT displays and
  calculations.

#. Acquire Data

- Hit this button once, and the software will gather the data, run the
  calculations, and display the results on the various tabs. (Waveform,
  Histogram, FFT)

#. Data Capture Displays

   #. Waveform - Time domain representation of the data
   #. Histogram - Bin representation of the data
   #. FFT - Frequency domain representation of the data

The following screen shot is an example of using the AD7980 ADC, and looking at
the frequency domain to view a 10kHz input sine wave. This tab provided several
frequency domain calculations such as SINAD, THD, SNR.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/software_fft_10khz.png
   :width: 700px

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project

   :adi:`EVAL-AD7685-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7685-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7686-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7686-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7687-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7687-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7688-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7688-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7690-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7690-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7691-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7691-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7693-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7693-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7946-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7946-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7980-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7980-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7982-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7982-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7983-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7983-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7984-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7984-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7988-1-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7988-1-pmdz-designsupport.zip>`

   :adi:`EVAL-AD7988-5-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7988-5-pmdz-designsupport.zip>`

Change Log
----------

Rev 0 to Rev A

- Changed CAD tools from PADS to Allegro, so the reference designators have
  changed
- Replaced C9 and C10(Rev 0) and put in R5 and R7(Rev A)
- Added R16 and R17(Rev A) to be able to use more operating modes of the ADC
  (for example, daisy-chain mode)
- Removed U5 (ADG1401 on Rev 0) and connected the 5V reference directly to the
  ADC (U3 Rev 0)
- Removed U8 (ADP7104-3.3 on Rev 0) and connected the VIO pin of the ADC to VCC
  (J4 Rev 0)
- Separated out the AGND plane and DGND plane

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware. Register below to receive
   all these great benefits and more!

- :reg:`EVAL-AD7942-PMDZ <EVAL-AD7942-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7946-PMDZ <EVAL-AD7946-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7988-1-PMDZ <EVAL-AD7988-1-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7685-PMDZ <EVAL-AD7685-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7687-PMDZ <EVAL-AD7687-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7691-PMDZ <EVAL-AD7691-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7686-PMDZ <EVAL-AD7686-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7688-PMDZ <EVAL-AD7688-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7693-PMDZ <EVAL-AD7693-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7988-5-PMDZ <EVAL-AD7988-5-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7980-PMDZ <EVAL-AD7980-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7983-PMDZ <EVAL-AD7983-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7690-PMDZ <EVAL-AD7690-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7982-PMDZ <EVAL-AD7982-PMDZ?&v=RevA>`
- :reg:`EVAL-AD7984-PMDZ <EVAL-AD7984-PMDZ?&v=RevA>`

*End of Document*

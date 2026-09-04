.. _adalm-mmsc:

ADALM-MMSC
==========

Mixed-Mode Signal Chain Active Learning Module

Overview
--------

.. figure:: adalm-mmsc_angle.png
   :align: left
   :width: 800 px

   ADALM-MMSC Board

The :adi:`Analog Devices Active Learning Module-Mixed-Mode Signal Chain (ADALM-MMSC) <ADALM-MMSC>`
is an educational board designed to facilitate hands-on exploration of
fundamental signal chain concepts.

The core of the circuit is the :adi:`AD4080`, a 40 MSPS oversampling 
SAR analog-to-digital converter (ADC) with a configurable digital filter 
and internal data capture memory (single-port FIFO).

The board includes a highly configurable 2nd order analog filter with
adjustable cutoff frequencies, input attenuation, and filter gain.

An onboard selectable clock source provides sample rates from 5 MSPS to
40 MSPS. A :adi:`MAX32666FTHR` microcontroller runs an IIO server 
over a serial backend, allowing the use of standard tools such as Scopy, 
IIO Oscilloscope, Pyadi-iio, and ADI's MATLAB precision toolbox.

The Libiio library provides language bindings for C, C#, MATLAB®, Python,
and other languages.

Concepts demonstrated include:

- Digital filtering
- Analog vs. digital anti-alias filtering
- Properties of different digital filters
- Noise analysis
- Reference noise

Features
++++++++

- Multiple input connections
   - 100-mil posts compatible with the :adi:`ADALM2000`
   - SMA connections for benchtop signal generators
   - 1/8-inch stereo audio jack for connection to sound cards and other audio
     sources
- Selectable input attenuator
   - 3:5 attenuation allows ±5V input swing
   - 3:50, 3:500 attenuation settings allow testing with low-amplitude signals for dynamic
     range measurements
- Configurable Sallen-Key filter with low-noise amplifier
   - Cutoff frequencies between 200 kHz and 8 MHz
   - Gains of unity, 2, and 5 for exploring noise optimization
- Onboard fully-differential amplifier
   - Accepts arbitrary input signals
   - Input and output test connections for monitoring all critical points
- Onboard low-noise reference
   - Flagship LTC6655 for optimal performance
   - "Reference Corruption" input allows noise and interfering tones to be
     introduced and their effects observed
- Selectable conversion rates from 5 MSPS to 40 MSPS allow observation of
  aliasing and ADC noise density vs. sample rate

Applications
++++++++++++

- Mixed signal and digital signal processing experiments, workshops, 
  and lab exercises
- Precision data acquisition

System Architecture
+++++++++++++++++++

.. figure:: adalm-mmsc_block_diagram.png

   ADALM-MMSC Simplified Block Diagram

Package Contents
++++++++++++++++

.. admonition:: Errata
   :class: warning

   The first production build has three errors:

   - P7 pins are too short for ADALM2000 fly wires

     - Resolution: Use P29, P30 for experiments that probe the AD4080 inputs

   - C2 and C3 should not be installed. Most experiments will work but there is
     overshoot in the step response and a peak around 2 MHz in the frequency
     response.

     - Resolution: Remove C2 and C3. They are easily accessible using two
       soldering irons or tweezer-style rework iron.

   - R28 should be 249 ohms, not 249k. Only affects gain = 5 selection.

     - Resolution: Install 249 ohm, 1% tolerance, 0603 on top of 249 k. The 249k
       resistor will have negligible ~0.1% impact on gain.

   .. image:: first_prod_run_rework.png
      :width: 400px
      :align: center

The ADALM-MMSC kit includes the following boards and accessories:

.. figure:: package_contents.png
   :width: 500 px

   ADALM-MMSC Kit Contents

- (A.) 1x :adi:`ADALM-MMSC` Board
- (B.) 1x Pre-programmed :adi:`MAX32666FTHR` board
- (C.) 1x USB-A to Micro-USB cable
- (D.) 1x :adi:`MAX32625PICO` with 10-pin ribbon cable for SWD connection (for future firmware upgrades)

----

Components and Connections
--------------------------

.. figure:: primary_side.png

   ADALM-MMSC Primary Side

.. figure:: secondary_side.png

   ADALM-MMSC Secondary Side

.. csv-table:: Jumper Configurations
   :file: jumper_configurations.csv
   :widths: 5, 25, 60
   :header-rows: 1

.. csv-table:: Connection Descriptions
   :file: connections.csv
   :widths: 5, 25, 60
   :header-rows: 1

----
   
Quick Start
-----------

There are numerous combinations of signal sources, signal analyzers, and
software that can be used with the ADALM-MMSC. The most straightforward
approach to get up and running and establish baseline functionality is to use
the :adi:`ADALM2000` with Scopy. Scopy is a general-purpose IIO-based utility
with instrument-specific control panels for various hardware, including
the :adi:`ADALM2000`.


**Equipment Needed**

- 1x ADALM-MMSC Board (as Device Under Test)
- Windows, Mac, or Linux host computer with an available USB port
- Signal generator such as the :ref:`ADALM2000<m2k>` or similar
  Alternative signal sources include:

   - Generators in the audio range work well
   - A PC sound card with Audacity is another option

Hardware Setup
--------------

The hardware setup uses the :adi:`ADALM2000` (M2K) as the primary signal source
for the system, as shown in the image below. In this configuration, the M2K's
waveform generator outputs are connected to the designated input pins on the
ADALM-MMSC board, allowing the board to receive and process test signals. 

.. figure:: adalm-mmsc_hardware_setup.png

   ADALM2000 (M2K) to ADALM-MMSC Hardware Setup
   
1. Connect the two black GND wires from the ADALM2000 to the 
   lower two posts of P17 (Pins 3 and 4).
2. Connect the solid yellow W1 wire from the ADALM2000 to P17 Pin 1.
3. Connect the striped yellow W2 wire from the ADALM2000 to P17 Pin 2.
4. Connect both the ADALM2000 and the ADALM‑MMSC to the host computer 
   using two micro‑USB cables.
5. Set P10 to the lower position (DIR) and P12 to the upper position (DIR).
   This configuration bypasses the Sallen‑Key filter and applies the inputs 
   directly to the fully differential amplifier.

Software Setup
--------------

**Requirement:**

.. admonition:: Download

   **Scopy:** :git-scopy:`latest version <releases/latest+>`
   (:external+scopy:ref:`user guide <user_guide>`)

1. Connect the **ADALM‑MMSC** to the host computer using a
   **USB‑A to USB‑Micro** cable, then open the **Scopy** GUI.

2. If you are using the :adi:`ADALM2000`, connect the instrument and allow
   the calibration process to complete.

3. From the Scopy home screen, add the ADALM‑MMSC connection by clicking
   the ``+`` button, as shown in the figure below.

   .. figure:: scopy_add_device.png

      Adding the ADALM‑MMSC in Scopy

4. Click the ``Scan`` button and select the ADALM‑MMSC serial port.
   More than one serial port may be listed, depending on the devices
   connected to the host machine.

   .. figure:: scopy_scan.png

      Scanning for the ADALM‑MMSC Serial Port

5. Click ``Verify``, then click ``Add Device``.

   .. figure:: scopy_verify.png

      Verifying the ADALM‑MMSC Connection

6. From the Scopy home screen, click ``Connect``.

   .. figure:: scopy_connect.png

      Connecting to the ADALM‑MMSC in Scopy

7. Once connected, Scopy is ready to acquire data from the ADALM-MMSC.

   a. Open the **ADC Time** panel.
   b. Set the buffer size to **4096** (maximum is **16384**, limited by the
      AD4080 FIFO depth).
   c. Click ``Start``.

8. The figure below shows the ADC output when the signal generator is
   configured as follows:

   - Channel 1: **1 Vpp**, **500 kHz** sine wave
   - Channel 2: **1 Vpp**, **50 kHz** sawtooth

   .. figure:: scopy_adc_time.png

      ADC Time Domain Capture in Scopy

9. Refer to the supporting lab exercises and workshop materials for
   additional experiments.

Firmware Upgrades
+++++++++++++++++

1. Access the ADALM‑MMSC firmware source from the no‑OS repository:

   :git-no-OS:`ADALM‑MMSC firmware (no‑OS) <projects/adalm-mmsc>`.

2. Download the pre‑built firmware binaries from the no‑OS releases page:

   :git-no-OS:`ADALM‑MMSC releases <releases/latest+>`

   The firmware package is provided as ``adalm-mmsc.zip``.

3. Use the included **MAX32625PICO** board to upgrade the firmware.

4. Follow the instructions in the MAX32625PICO firmware images repository
   to load the MAX32666FTHR‑specific binary:

   :git-max32625pico-firmware-images:`MAX32625PICO firmware images <+>`

5. Connect the 10‑pin ribbon cable between the **MAX32625PICO** and the
   **MAX32666FTHR** board.

6. Drag and drop the file
   ``adalm-mmsc_maxim_iio_example_max32665.hex`` into the
   **DAPLink** drive (typically ``D:\`` or ``E:\`` on Windows).

7. Wait for the DAPLink drive to automatically eject, indicating that the
   firmware upgrade has completed successfully.

----

Resources
---------

Design & Integration Files
++++++++++++++++++++++++++

.. admonition:: Download

   :adi:`ADALM-MMSC Design & Integration Files <media/en/reference-design-documentation/design-integration-files/adalm-mmsc-designsupport.zip>`

    * Schematic
    * PCB Layout
    * Bill of Materials
    * Allegro Project

.. admonition:: Schematic Errata

   The value of **R44** is **499 Ohms** (not 1.33K as shown in the schematic)

Helpful Links
++++++++++++++

- :adi:`AD4080 Product Page <AD4080>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADM1085 Product Page <ADM1085>`
- :adi:`LT1468 Product Page <LT1468>`
- :adi:`LT3042 Product Page <LT3042>`
- :adi:`LT3093 Product Page <LT3093>`
- :adi:`LT3471 Product Page <LT3471>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`MAX38912 Product Page <MAX38912>`
- :adi:`ADALM2000 Product Page <ADALM2000>`
- :external+scopy:ref:`user_guide`

Support
++++++++

For questions and more information, please visit the
:ez:`EngineerZone Support Community </>`.

.. _interposer:

AD717X-2 FMC-SDP Interposer & Evaluation Board / Xilinx KC705 Reference Design
===============================================================================

.. warning::

   This page is provided for reference only. The Xilinx KC705 is obsolete
   hardware. The design described here is no longer actively maintained.

Supported Devices
-------------------------------------------------------------------------------

- :adi:`AD7175-2`
- :adi:`AD7176-2`

Evaluation Boards
-------------------------------------------------------------------------------

- :adi:`EVAL-AD7175-2SDZ`
- :adi:`EVAL-AD7176-2SDZ <en/products/ad7176-2.html>`

Overview
-------------------------------------------------------------------------------

This document presents the steps to setup an environment for using the
:adi:`EVAL-AD7176-2SDZ <AD7176-2>` evaluation board together with the
Xilinx KC705 FPGA board and the Xilinx Embedded Development Kit (EDK).
Below is presented a picture of the EVAL-AD7176-2SDZ Evaluation Board with
the Xilinx KC705 board.

.. image:: images/ad7176_2.jpg
   :width: 400
   :alt: EVAL-AD7176-2SDZ and Xilinx KC705 board


The **EVAL-AD7176-2SDZ** evaluation board is a member of a growing number of
boards available for the **SDP**. It was designed to help customers evaluate
performance or quickly prototype new **AD7176-2** circuits and reduce design
time.

The :adi:`AD7176-2` is a fast settling, highly accurate, high resolution,
multiplexed Σ-Δ analog-to-digital converter (ADC) for low band-width input
signals. Its inputs can be configured as two fully differential or four pseudo
differential inputs via the integrated crosspoint multiplexer. An integrated
precision, 2.5 V, low drift (2 ppm/°C), band gap internal reference (with an
output reference buffer) adds functionality and reduces the external component
count. The maximum channel scan data rate is 50 kSPS (with a settling time of
20 μs), resulting in fully settled data of 17 noise free bits. User-selectable
output data rates range from 5 SPS to 250 kSPS. The resolution increases at
lower speeds. The AD7176-2 offers three key digital filters. The fast settling
filter maximizes the channel scan rate. The Sinc3 filter maximizes the
resolution for single-channel, low speed applications. For 50 Hz and 60 Hz
environments, the AD7176-2 specific filter minimizes the settling times or
maximizes the rejection of the line frequency. These enhanced filters enable
simultaneous 50 Hz and 60 Hz rejection with a 27 SPS output data rate (with
a settling time of 36 ms).

Getting Started
-------------------------------------------------------------------------------

The first objective is to ensure that you have all of the items needed and to
install the software tools so that you are ready to create and run the
evaluation project.

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `AMD KC705 FPGA board <https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/ek-k7-kc705-g.html>`_
- FMC-SDP adapter board
- **EVAL-AD7175-2SDZ** / **EVAL-AD7176-2SDZ** evaluation board

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Xilinx ISE 14.3
- A UART terminal (ex. TeraTerm / Hyperterminal).

Run the Demonstration Project
-------------------------------------------------------------------------------

Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   Before connecting the ADI evaluation board to the Xilinx KC705 make sure
   that the VADJ_FPGA voltage of the KC705 is set to 3.3V. For more details
   on how to change the setting for VADJ_FPGA visit the AMD KC705 product
   page.

- Use the FMC-SDP interposer to connect the ADI evaluation board to the
  Xilinx KC705 board on the FMC LPC connector.
- Connect the JTAG and UART cables to the KC705 and power up the FPGA board.
- Start IMPACT, and double click "*Boundary Scan*". Right click and select
  *Initialize Chain*. The program should recognize the Kintex 7 device (see
  screenshot below).

.. image:: images/impact_config.png
   :width: 300

- Program the KC705 FPGA using the "*Bit/download.bit*" file from the
  reference design.
- Power the ADI evaluation board.
- Start a UART terminal and set the baud rate to 115200 bps.

At this point everything is set up and it is possible to start the evaluation
of the ADI hardware. To capture data from the ADC run the *data_capture.bat*
script located in the *DataCapture* folder of the reference design.
Every time the script is run a new batch of 8192 samples are read from the ADC
at the ADC's maximum sampling rate and saved into the *Acquisition.csv* file
located in the same folder as the data capture script. The data_capture.tcl
file can be modified for different configuration words to be programmed on the
AD7176-2. On the UART terminal messages will be displayed to show the status
of the program running on the FPGA as shown in the picture below.

.. image:: images/teraterm_adc.png
   :width: 400

If the resulting csv file is opened with Microsoft Excel, the data will be
displayed on a different number of columns, each column corresponding to a
channel.

.. tip::

   The first time the data capture script is run it is possible that an error
   will occur while the script is trying to connect to the system. Just run the
   script again and the error shouldn't appear anymore.

More information
-------------------------------------------------------------------------------

- :adi:`AD7176-2 Product Info <AD7176-2>` - pricing, samples, datasheet
- EVAL-AD7176-2SDZ evaluation board user guide is included on the CD as part
  of the Evaluation Board Kit
- `AMD KC705 FPGA board <https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/ek-k7-kc705-g.html>`_

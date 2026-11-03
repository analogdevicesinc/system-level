.. _eval_ad7606x prerequisites:

Prerequisites
===============================================================================

The required hardware and software depend on the evaluation path you choose.

Hardware Prerequisites
-------------------------------------------------------------------------------

**Evaluation Platform (choose one)**:

#. **IIO Ecosystem** (recommended):

   - :adi:`EVAL-AD7606B-FMCZ`, :adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>`, or equivalent
     evaluation board
   - :adi:`SDP-K1 System Demonstration Platform`

#. **FPGA-Based Evaluation**:

   - :adi:`EVAL-AD7606` evaluation board (EVAL-AD7605-4SDZ, EVAL-AD7606SDZ,
     etc.)
   - :adi:`EVAL-CED Converter Evaluation and Development (CED) Board`
   - Terasic USB Blaster for FPGA programming

#. **ACE Software Automation**:

   - :adi:`SDP-H1 Controller board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`
     with 12 V DC wall adapter
   - :adi:`EVAL-AD7606C-18` or equivalent evaluation board

#. **Linux / no-OS FPGA Development** (ZedBoard):

   - :adi:`EVAL-AD7606B-FMCZ` or :adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>` FMC evaluation
     board
   - AMD Xilinx `ZedBoard
     <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     Rev C or later, with 12 V power supply
   - SD card with at least 16 GB of memory (Linux path only)

**Cables**:

- USB cable (Type A to Mini-B or Micro-B, depending on controller board)
- SMB cables for analog signal inputs

Software Prerequisites
-------------------------------------------------------------------------------

**IIO Ecosystem**:

- :git-precision-converters-firmware:`precision-converters-firmware <.>`
  (Mbed firmware for SDP-K1)
- `Libiio <https://github.com/analogdevicesinc/libiio/releases>`_
- `IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_

**FPGA-Based Evaluation**:

- `Quartus II Web Edition <https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html>`_
  v11.0
- `Nios II EDS <https://community.altera.com/kb/knowledge-base/how-can-i-install-nios-ii-embedded-design-suite-legacy-tools/342234>`_ v11.0

**ACE Automation**:

- :adi:`ACE software
  <en/design-center/evaluation-hardware-and-software/ace-software.html>`
- AD7606B or AD7606C ACE plugin (downloadable within ACE)
- MATLAB or Python environment

**Linux / no-OS FPGA Development**:

- AMD Xilinx Vivado and Vitis (no-OS path)
- :external+kuiper:doc:`Kuiper Linux <index>` SD card image (Linux path)
- A UART terminal (Putty/Tera Term/Minicom, etc.) at 115200 baud (8N1)

**Optional — Python scripting**:

- Python 3.9+
- :git-pyadi-iio:`pyadi-iio <.>`

Next Steps
-------------------------------------------------------------------------------

Choose the evaluation path that best suits your needs:

- :ref:`IIO Ecosystem Quick Start <ad7606_mbed_iio_application>`
- :ref:`ZedBoard Quick Start <ad7606x quickstart zed>`
- :ref:`FPGA Prototyping with CED1Z <ad7606_ced1z_fpga>`
- :ref:`ACE Automated Testing <ad7606c_remotecontrol>`

.. note::

   If you encounter issues during setup, refer to the evaluation board user
   guide or consult the :ref:`Help and Support <help-and-support>` page.

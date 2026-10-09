.. collection:: EVAL-AD9434
   :subtitle: The EVAL-AD9434 is an evaluation board for the AD9434, single 12-bit ADC
   :image: images/eval_ad9434_fmc.png
   :label: eval user-guide

   system-level:
     - User guide <.>

   hdl:
     - HDL Project (ad9434_fmc) <projects/ad9434_fmc/index>

   no-OS:
     - no-OS Driver (ad9434) <drivers/adc/ad9434>

.. _ad9434:

EVAL-AD9434-FMC
===============================================================================

The :adi:`EVAL-AD9434` is an evaluation board for the :adi:`AD9434`, single
12-bit ADC. This reference design provides all the support circuitry to
operate devices in their various modes and configurations. It is designed to
interface directly with the :adi:`EVAL-SDP-H1` data capture card, allowing users
to download captured data for analysis. The Visual Analog software package,
which is used to interface with the device's hardware, allows users to download
captured data for analysis with a user-friendly graphical interface. The SPI
controller software package is also compatible with this hardware and allows the
user to access the SPI programmable features of the :adi:`AD9434`. The :adi:`EVAL-AD9434`
evaluation board is also supported on `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
and :xilinx:`ZC706` using ADI's HDL infrastructure.

The :adi:`AD9434` is a 12-bit monolithic sampling analog-to-digital converter
(ADC) optimized for high performance, low power, and ease of use. The part
operates at up to a 500 MSPS conversion rate and is optimized for outstanding
dynamic performance in wideband carrier and broadband systems. All necessary
functions, including a sample-and-hold and voltage reference, are included on
the chip to provide a complete signal conversion solution. This reference design
includes a data capture interface and the external DDR-DRAM interface for sample
storage. It allows programming the device and monitoring its internal status
registers. The board also provides other options to drive the clock and analog
inputs of the ADC.

Features:

- Full-featured evaluation board for the AD9434
- SPI interface for setup and control
- External, on-board oscillator, or AD9517 clocking option
- Balun/transformer or amplifier input drive option
- LDO regulator or switching power supply options
- VisualAnalog® and SPI controller software interfaces

Applications:

- Wireless and wired broadband communications
- Cable reverse path
- Communications test equipment
- Radar and satellite subsystems
- Power amplifier linearization

.. image:: images/eval_ad9434_fmc.png
   :align: center
   :width: 400

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9434`, we recommend using the :adi:`EVAL-AD9434`
evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad9434 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`ad9434 prerequisites` - what you need to get started with the setup
   #. :ref:`ad9434 quickstart`:

      #. Using the :ref:`ZC706/Zynq-7000 SoC <ad9434 quickstart zc706>`
      #. Using the :ref:`ZedBoard/Zynq-7000 SoC <ad9434 quickstart zedboard>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9434

   - :ref:`ad9434 block-diagram`

     - :adi:`AD9434 product page <AD9434>`

   - Resources for designing a custom AD9434-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. :external+hdl:ref:`ad9434_fmc` which you must use in your FPGA.

   - :adi:`AD9434 data sheet <media/en/technical-documentation/data-sheets/ad9434.pdf>`
#. :ref:`ad9434 evaluation-guide-sdph1`
#. :ref:`Help and Support <help-and-support>`

.. toctree::
   :hidden:
   :glob:

   user-guide
   prerequisites
   quickstart/index
   evaluation-guide-sdph1

.. _ad9434 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad9434_block_diagram.png
   :align: center
   :width: 700

Warning
-------------------------------------------------------------------------------

.. esd-warning::
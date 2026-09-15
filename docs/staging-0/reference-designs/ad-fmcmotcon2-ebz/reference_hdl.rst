.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon2-ebz/reference_hdl

.. _ad-fmcmotcon2-ebz reference_hdl:

Xilinx HDL Reference Design
===========================

The Reference design is based on the
`ZedBoard <http://zedboard.org/product/zedboard>`__. It has the complete
infrastructure for Linux support.

Reference Design
----------------

The reference design contains HDL blocks for interfacing with the various
components of the motor control hardware:

- Current Monitor - Implements the communication with the AD7401 sigma delta
  modulators present on the AD-FMCMOTCON2-EBZ and also the SINC3 filters for
  demodulating the 1-bit digital stream provided by these parts. This HDL block
  exposes a set of registers that can be accessed through the AXI Lite
  interface. A FIFO interface connected to a DMA controller allows the block to
  stream real time data to the application layer. An ADC PACK IP is used so that
  1, 2 or all channels can stream data at a time.
- Controller - Implements the interface to the IP control blocks in the system.
  A FIFO interface connected to a DMA controller allows the block to stream real
  time data to the application layer. It implements a basic six point drive of
  the motor. An ADC PACK block is used so that 1, 2, 4 or all channels can
  stream data at a time.
- Speed Detector - Implements the algorithm for converting Hall, BEMF and
  Encoder signals into speed and position data. This HDL block exposes a set of
  registers that can be accessed through the AXI Lite interface. A FIFO
  interface connected to a DMA controller allows the block to stream real time
  data to the application layer.
- GMII to RGMII - Converts the GMII interface from the two Ethernet cores from
  the PS7 block to RGMII interface that is available on the FMC Controller
  Board. The IP allows for the RX pins to be on different I/O Banks.
- I2C - There are two I2C interfaces connected to the FMC board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/motorcontrolrev2.jpg
   :width: 800px

Vivado Design Generation
------------------------

In order to build the project you need to follow the instructions from
:dokuwiki:`ADI Reference Designs HDL User Guide </resources/fpga/docs/hdl>`

Downloads
---------

.. admonition:: Download

   - :git-hdl:`Vivado ADI Libraries <library>`
   - :git-hdl:`Vivado Motor Control 2 Reference Design <projects/motcon2_fmc>`

Setting up Linux
----------------

.. note::

   For instructions on how to setup linux on the ZED board, please follow instructions at: :dokuwiki:`Linux on Zynq Quick Start Guide </resources/eval/user-guides/ad-fmcmotcon2-ebz/quickstart/zynq>`

Support
-------

.. note::

   - Questions? :ez:`Ask Help & Support <community/fpga>`.

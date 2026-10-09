.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0540

.. _eval-cn0540-ardz:

EVAL-CN0540-ARDZ
===============================================================================

24-Bit Data Acquisition System for IEPE Sensors.

.. image:: ../images/ad7768-1.png
    :align: left
    :width: 150

Overview
-------------------------------------------------------------------------------

Monitoring the health of machinery can help predict changes in a machine's
condition. There are many methods of tracking a machine's condition, but
vibration analysis is the most commonly used one. By tracking the vibration
analysis data over time, one can determine when a fault or failure is going to
occur, along with the source of the fault. Knowing the condition of a certain
machine will help not only increase efficiency and productivity, but create a
safer working environment.

The reference design shown below, shows a high resolution, wide-bandwidth,
high dynamic range, Integrated Electronics Piezoelectric (IEPE) compatible
interface data acquisition system (DAQ) for interfacing with Integrated Circuit
Piezo (ICP)/IEPE piezo vibration sensors. Most solutions which interface with
piezo sensors in the market are AC coupled, lacking DC and sub-hertz
measurement capability. This reference design is a DC coupled solution in which
DC and sub-hertz precision are achieved.

By looking at the complete data set from the vibration sensor in the frequency
domain (DC – 50 kHz), the type and source of a machine fault can be better
predicted using the; position, amplitude and number of harmonics found in the
FFT spectrum.

The data acquisition board incorporates a precision 24-bit, 1024kSPS
Sigma-delta ADC AD7768-1 and a 16-bit voltage output DAC LTC2606. Used as the
ADC driver is a high linearity FDA ADA4945-1 and a 200mA programmable
2-terminal current source LT3092. Analog input protection is provided by the
switch ADG5421F. The data acquisition board is an Arduino compatible form
factor, and can be interfaced and powered directly from most Arduino compatible
development boards.

This user guide will discuss how to use an Arduino compatible
micro-controller board and evaluation software to configure and collect
vibration data from the :adi:`EVAL-CN0540-ARDZ Shield` (**CN0540 Board**).

.. image:: ../images/cn0540_top.png
   :align: center
   :width: 500

.. image:: ../images/cn0540_bottom.png
   :align: center
   :width: 500

Features:

- Data acquisition solution fully characterized over -25°C to 85°C.
- Throughput of 1024kSPS.
- DC coupled for greater precision.
- Powered and interfaced directly through an Arduino compatible development board.

.. toctree::
   :hidden:

   user-guide
   prerequisites
   iio-oscilloscope
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of Contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`eval-cn0540-ardz user-guide` - what you need to know about the
      evaluation board
   #. :ref:`eval-cn0540-ardz prerequisites` - what you need to get started
      with the setup
   #. :ref:`eval-cn0540-ardz iio-oscilloscope-plugin` - what you need to get
      started with using IIO-Oscilloscope
   #. :ref:`eval-cn0540-ardz quickstart`:

      #. Using the :ref:`CoraZ7-07s/ Zynq‑7000 SoC <eval-cn0540-ardz quickstart coraz7s>`
      #. Using the :ref:`DE10-Nano/ Cyclone V SoC <eval-cn0540-ardz quickstart de10nano>`

#. Use the board to better understand the :adi:`EVAL-CN0540-ARDZ`

      #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`
      #. :external+kuiper:ref:`package-management`

   #. Linux Applications

      #. :ref:`EVAL-CN0540-ARDZ Plugin <eval-cn0540-ardz iio-oscilloscope-plugin>`
      #. :doc:`FRU EEPROM Utility </software/fru_dump>`

#. Design with the EVAL-CN0540-ARDZ

   #. :ref:`eval-cn0540-ardz block-diagram`

      #. :adi:`AD7768-1 Product Page <AD7768-1>`
      #. :adi:`CN0540 Circuit Note Page <CN0540>`

   #. Design a custom EVAL-CN0540-ARDZ based platform

      #. HDL software

         #. :git-hdl:`CN0540 HDL Reference Design <projects/cn0540>` which you must use in your FPGA.

      #. Linux software

        #. :git-linux:`CN0540 Linux driver source code <main:drivers/iio/adc/ad7768-1.c>`
        #. :git-linux:`CN0540/ CoraZ7S Linux device tree <main:arch/arm/boot/dts/xilinx/zynq-coraz7s-cn0540.dts>`
        #. :git-linux:`CN0540/ DE-10Nano Linux device tree <main:arch/arm/boot/dts/intel/socfpga/socfpga_cyclone5_de10_nano_cn0540.dts>`

      #. More information

         #. :external+hdl:ref:`spi_engine`

.. _eval-cn0540-ardz block-diagram:

Simplified functional block diagram
-------------------------------------------------------------------------------

.. image:: ../images/cn0540_revb_functional_block_diagram.png
   :align: center
   :width: 800

More Information and Useful Links
-------------------------------------------------------------------------------

 - :adi:`ADA4945-1 Product Page <ADA4945-1>`
 - :adi:`LT3092 Product Page <LT3092>`
 - :adi:`LTC2606 Product Page <LTC2606>`
 - :adi:`ADG5421F Product Page <ADG5421F>`

Software Projects and Platforms
-------------------------------------------------------------------------------

- :ref:`CN0540 + DE10-Nano FPGA <eval-cn0540-ardz quickstart de10nano>`
- :ref:`CN0540 + Cora Z7s FPGA <eval-cn0540-ardz quickstart coraz7s>`
- :ref:`CN0540 + SDP-K1 <eval-cn0540-ardz quickstart sdp-k1>`
- :ref:`CN0540 + STM Discovery Kit <eval-cn0540-ardz quickstart stm-discovery>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

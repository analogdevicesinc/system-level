.. _eval-ad463x-fmcz:

EVAL-AD4630-16/24FMCZ / EVAL-AD4030-24FMCZ
===============================================================================

.. image:: images/ad4630_24_chip.png
   :align: left
   :width: 150

.. image:: images/ad4030_24_chip.png
   :align: left
   :width: 150

.. clear-content::

Overview
-------------------------------------------------------------------------------

The EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ and EVAL-AD4630-16FMCZ evaluation
boards enable quick and easy evaluation of the AD4X3X family of 24-bit and
16-bit precision successive approximation register (SAR) analog-to-digital
converters (ADCs).
The :adi:`AD4630-24 <en/products/AD4630-24.html>` and
:adi:`AD4630-16 <en/products/AD4630-16.html>` are 2 MSPS per channel, low power,
dual channel 24-bit or 16-bit SAR ADCs while the
:adi:`AD4030-24 <en/products/AD4030-24.html>` is a single channel 24-bit
precision SAR ADC that supports up to 2 MSPS per channel. The evaluation boards
demonstrate the performance of either the AD4630-24, AD4030-24 or AD4630-16 and
provide a configurable analog front end (AFE) for a variety of system
applications.

Features:

-  2 MSPS per channel, 24-bit or 16-bit resolution with no missing codes
-  Guaranteed maximum +/-0.9 ppm INL
-  Low noise performance
-  On-board voltage reference, clock source, and ADC drivers
-  Versatile analog signal conditioning circuitry
-  Flexi-SPI serial interface with multiple SDO lanes
   (1, 2, or 4 per channel)
-  Optional DDR data clocking
-  On-chip sample averaging (power of 2, up to 65536 samples)
-  FMC-LPC system board connector
-  ACE PC software for configuration and data analysis (time and frequency
   domain)
-  Compatible with other off-the-shelf controller boards

Applications:

-  Automatic test equipment (ATE)
-  Precision data acquisition systems
-  Power quality analysis and grid monitoring
-  Vibration analysis and condition monitoring
-  Medical and scientific instrumentation
-  Industrial process control

Evaluation boards available:

-  :adi:`EVAL-AD4630-24FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-24.html>`
-  :adi:`EVAL-AD4630-16FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-16.html>`
-  :adi:`EVAL-AD4030-24FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4030-24.html>`

.. figure:: images/eval_ad4030_24_top.jpg
   :align: center
   :width: 400

   EVAL-AD4030-24FMCZ. Rev A/B

.. figure:: images/eval_ad4630_16_top.jpg
   :align: center
   :width: 400

   EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ. Rev C

.. figure:: images/cb_ad464030_24fmcz_top_evaluation_board.jpg
   :align: center
   :width: 400

   EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ. Rev E

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`Prerequisites <eval-ad463x-prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guide <eval-ad463x-quickstart>`:

      #. Using the :ref:`ZedBoard <eval-ad463x-quickstart-zedboard>`

   #. Configure an SD Card with
      :ref:`kuiper`

#. Design with the AD4630/AD4030

   - :ref:`eval-ad463x-block-diagram`

     - :adi:`AD4630-24 Product Page <en/products/AD4630-24.html>`
     - :adi:`AD4630-16 Product Page <en/products/AD4630-16.html>`
     - :adi:`AD4030-24 Product Page <en/products/AD4030-24.html>`

   - :ref:`eval-ad463x-user-guide`

   - Resources for designing a custom AD4630/AD4030-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:doc:`AD463x Linux Driver <drivers/iio-adc/ad463x>`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. :external+hdl:ref:`HDL reference design <ad4630_fmc>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad463x-block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/ad4030_24_block_diagram.png
   :align: center
   :width: 800

   AD4030-24 Block Diagram

.. figure:: images/ad4630_16_block_diagram.png
   :align: center
   :width: 800

   AD4630-16 Block Diagram

.. figure:: images/ad4630_24_block_diagram.png
   :align: center
   :width: 800

   AD4630-24 Block Diagram

ADI articles
-------------------------------------------------------------------------------

About precision SAR ADCs and the AD4630 family:

#. :adi:`Achieve 7.5 Digits Accuracy in Instrumentation Apps (Part 2) <en/resources/technical-articles/achieve-7-pt-5-digits-accuracy-instrumentation-apps-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Technical support for the evaluation board hardware and software can be obtained
by posting a question to ADI's
:ez:`EngineerZone <data_converters/precision_adcs>` technical support community
for precision ADCs.

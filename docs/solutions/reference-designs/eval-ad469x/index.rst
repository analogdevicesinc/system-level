.. _eval-ad469x:

EVAL-AD469x
===============================================================================

   .. image:: images/ad4692.png
      :align: left
      :width: 150

   .. clear-content::

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4696FMCZ` and :adi:`EVAL-AD4692-ARDZ` evaluation boards enable
quick and easy evaluation of the performance and features of the AD469x family
of devices.

The :adi:`AD4695`/:adi:`AD4696` are compact, 16-channel, 16-bit, 1 MSPS,
multiplexed successive approximation register (SAR) analog-to-digital converter
(ADC) that enable high performance data acquisition of multiple signals in a
small form factor. The :adi:`AD4697`/:adi:`AD4698` are pin-compatible 8-channel
variants.

The :adi:`AD4692`/:adi:`AD4691` are compact, high accuracy, 16-bit Easy Drive
successive approximation register (SAR) ADCs optimized for high-density
multichannel precision data acquisition solutions. The
:adi:`AD4693`/:adi:`AD4694` are pin-compatible 8-channel variants.

Features:

- 16-bit resolution
- Up to 1 MSPS throughput rate
- 16 channels (AD4691/AD4692/AD4695/AD4696) or
  8 channels (AD4693/AD4694/AD4697/AD4698)
- On-board reference circuitry
- ACE plugin available for device configuration and performance evaluation
- SPI-compatible serial interface
- FMC and Arduino form factor evaluation boards

Applications:

- Optical networking
- Wireless infrastructure
- Industrial automation

.. grid::
   :widths: 50% 50%

   .. figure:: images/ad4692_top.jpg
      :width: 300

      EVAL-AD4692ARDZ
   .. figure:: images/ad4696_top.jpg
      :width: 300

      EVAL-AD4696FMCZ

.. toctree::
   :hidden:

   user-guide
   ltspice-guide
   ltspice-transient-sims
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

   #. :ref:`Prerequisites <eval-ad469x-prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guide <eval-ad469x-quickstart>`:

      #. Using the :ref:`ZedBoard <eval-ad469x-quickstart-zedboard>`
      #. Using the :ref:`CoraZ7-07S <eval-ad469x-quickstart-coraz7s>`
      #. Using the :ref:`DE10-Nano <eval-ad469x-quickstart-de10nano>`

   #. Configure an SD Card with :external+kuiper:doc:`index`

#. Design with the AD469x

   - :ref:`eval-ad469x-block-diagram`

   - :ref:`eval-ad469x-user-guide`

   - :ref:`eval-ad469x-ltspice-guide`

     - :ref:`eval-ad469x-ltspice-transient-sims`

   - Resources for designing a custom AD469x-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:doc:`AD4695 IIO ADC driver
             <drivers/iio-adc/ad4695>`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. :external+hdl:ref:`HDL reference design <ad469x_evb>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad469x-block-diagram:

Simplified functional block diagram
-------------------------------------------------------------------------------

.. figure:: images/ad4692_block_diagram.jpeg
   :align: center
   :width: 800

   EVAL-AD4692-ARDZ Block Diagram

.. figure:: images/ad4696_block_diagram.png
   :align: center
   :width: 800

   EVAL-AD4696FMCZ Block Diagram

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD4691 Product Page <AD4691>`
- :adi:`AD4692 Product Page <AD4692>`
- :adi:`AD4693 Product Page <AD4693>`
- :adi:`AD4694 Product Page <AD4694>`
- :adi:`AD4695 Product Page <AD4695>`
- :adi:`AD4696 Product Page <AD4696>`
- :adi:`AD4697 Product Page <AD4697>`
- :adi:`AD4698 Product Page <AD4698>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Technical support for the evaluation board hardware and software can be
obtained by posting a question to ADI's
:ez:`EngineerZone <data_converters/precision_adcs>` technical support community
for precision ADCs.

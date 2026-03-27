.. imported from: https://wiki.analog.com/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/hw

.. _ad9081 mxfe-frontend hw:

2-24 GHz reference design hardware prototyping
===============================================================================

This page details the prototype hardware that ADI developed to prove out and
prototype this reference design. The hardware is composed of 2 main
platforms:

#. 2 to 24 GHz RX Engineering Platform
#. 2 to 24 GHz TX Engineering Platform

Each platform is composed of 4 primary pieces of hardware:

#. X-Microwave RF Signal Chain
   (`X-Microwave Reference Design Kits <https://xmicrowave.com/reference-design-kits/>`__)
#. AD9082 Evaluation Board (:adi:`AD9082-FMCA-EBZ <EVAL-AD9082>`)
#. ZCU102 Evaluation Board
   (:xilinx:`EK-U1-ZCU102-G <products/boards-and-kits/ek-u1-zcu102-g.html>`)
#. ADI's X-Microwave Bridge Board (:adi:`AD-FMCXMWBR1-EBZ`)

Additional hardware is also needed, such as cables, test equipment and power
supplies.

With these 4 key pieces of hardware, the full signal chain (including the
digitizer) can be evaluated for functionality and performance. Additionally,
all control of the signal chain is conducted from a central location (FPGA on
the ZCU102), which allows for coordinated control system prototyping.

Below is a diagram showing how these pieces fit together to complete the
prototyping system.

.. figure:: ../images/ad9081_2to24_prototypingplatformhw.png
   :align: center

   Prototyping platform hardware

Once the hardware is connected as pictured above, the pinouts for the XMW
bridge board can be distributed to the components in the signal chain to
interface with the hardware platform. The following block diagram shows the
receiver signal chain with LO circuits and XMW bridge board pinouts connected:

.. figure:: ../images/ad9081_2to24_updatedrxcontrol.png
   :align: center

   Receiver signal chain with XMW bridge board pinouts

The following block diagram shows the transmit signal chain with LO circuits
and XMW bridge board pinouts connected:

.. figure:: ../images/ad9081_2to24_updatedtxcontrol.png
   :align: center

   Transmit signal chain with XMW bridge board pinouts

.. important::

   This hardware is currently in development. We expect to have results of
   our prototyping posted soon.

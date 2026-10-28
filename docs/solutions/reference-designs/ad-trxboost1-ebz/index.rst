.. _ad-trxboost1-ebz:

AD-TRXBOOST1-EBZ
===============================================================================

Overview
-------------------------------------------------------------------------------

The :adi:`AD-TRXBOOST1-EBZ` is an add on board for the
:adi:`FMCOMMS2/3/4/5 <AD-FMCOMMS2-EBZ>` boards which contain the
:adi:`AD9361`. While the complete chip level design package can be found on the
ADI product pages of this RF transceiver, information on the card, and how to
use it and the design package that surrounds it, can be found here.

The purpose of the AD-TRXBOOST1-EBZ is to add a pre-amp to the TX output and
an LNA to the RX input of the AD9361.

The AD-TRXBOOST1-EBZ module is comprised of the ADL5610 which is an 18dB RF
fixed gain block that can operate between 30MHz and 6 GHz with a low noise
figure of 2.2dB, the ADL5521 which is a 20dB LNA that can operate between
400MHz and 4GHz with a low noise figure of 0.8dB, along with the ADP2370
switch regulator and two ADP7104 LDOs.

For additional information or to purchase the AD-TRXBOOST1-EBZ, visit:
:adi:`AD-TRXBOOST1-EBZ`.

Features:

-  Includes schematics, layout, BOM, Gerber files
-  Powered from single Keyed connector that matches the header on the
   FMCOMMS2/3/4 series.
-  Provides one channel TX and one channel RX boost.

Applications:

-  Electronic test and measurement equipment
-  General-purpose software radios
-  Radar systems
-  Ultra wideband satellite receivers
-  Signals intelligence (SIGINT)
-  Point to point communication systems
-  DOCSIS 3.0 CMTS and HFC networks
-  Multiple input/multiple output (MIMO) radios
-  Automated test equipment

.. figure:: images/trxboost1_-_top.jpg
   :align: center
   :width: 500

.. toctree::
   :hidden:

   ad-trxboost1-ebz
   characterization
   practical
   quickstart
   testing

Table of contents
-------------------------------------------------------------------------------

#. Use the board as an add-on to the
   :ref:`AD-FMCOMMS2/3/4/5 <fmcomms2>` platform

   #. :ref:`Quick Start Guide <ad-trxboost1-ebz quickstart>`
   #. :ref:`Characterization <ad-trxboost1-ebz characterization>`
   #. :ref:`Production Testing <ad-trxboost1-ebz testing>`
   #. :ref:`Practical Guide <ad-trxboost1-ebz practical>` to using the
      :adi:`AD-TRXBOOST1-EBZ` with the :adi:`AD-FMCOMMS3-EBZ`

#. :ref:`ad-trxboost1-ebz block-diagram`

#. :ref:`Help and Support <ad-trxboost1-ebz help-and-support>`

.. _ad-trxboost1-ebz block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/rx_path.png
   :align: center
   :width: 400

.. figure:: images/tx_path.png
   :align: center
   :width: 400

.. _ad-trxboost1-ebz help-and-support:

Help and support
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on the
`EngineerZone Support Community <https://ez.analog.com/>`_, but before that,
please make sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _fmcomms4 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do
an initial system setup for the :adi:`EVAL-AD-FMCOMMS4` boards on various FPGA
development boards. They will discuss how to program the bitstream, run a no-OS
program or boot a Linux distribution.

.. toctree::

   On ZCU102 <zcu102>
   On KCU105 <kcu105>
   On ZC706 <zc706>
   On ZC702 <zc702>
   On ZED <zed>

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCOMMS4-EBZ is, by definition a "FPGA mezzanine card" (FMC), that
means it needs a carrier to plug into. The supported carriers can be found
:ref:`here <fmcomms2/3/4 carriers>`.

Supported environments
-------------------------------------------------------------------------------

The supported environments can be found
:ref:`here <fmcomms2/3/4 supported-env>`.

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the AD-FMCOMMS4-EBZ board connects to the LPC connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few
typical setups are shown below.

ZC702 + FMCOMMS4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Early versions of the ZC702 carriers need to work around `AR# 51438, PG signal
does not assert by default <https://www.xilinx.com/support/answers/51438.html>`_
errata.

.. image:: ../images/fmcomms4_zc702_linux.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms4 quickstart zc702>`.

ZC706 + FMCOMMS4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms4_zc706_linux.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms4 quickstart zc706>`.

ZED + FMCOMMS4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms4_zed_linux.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms4 quickstart zed>`.

ZCU102 + FMCOMMS4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms4_zcu102_linux.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms4 quickstart zcu102>`.

KCU105 + FMCOMMS4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms4_kcu105.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms4 quickstart kcu105>`.

.. _ad9694 quickstart:

Quickstart
===============================================================================

The quick start guides provide simple step-by-step instructions on how to do an
initial system setup for the :adi:`AD9694-500EBZ <EVAL-AD9694>` board using various evaluation
platforms.

.. toctree::
   :maxdepth: 1

   On ZCU102 <zcu102>
   ADS7-V2EBZ (Windows) <ads7-v2>

.. _ad9694 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`AD9694-500EBZ <EVAL-AD9694>` is an FMC card; it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Platform
     - Connector
     - Notes
   * - :xilinx:`ZCU102`
     - FMC HPC1
     - FPGA carrier, Kuiper Linux

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Platform
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On the ZCU102, the :adi:`AD9694-500EBZ <EVAL-AD9694>` connects to the **FMC HPC1** connector.
The carrier setup requires power, UART (115200 baud), Ethernet (Linux), and SMA
cables for analog inputs and clock sources.

ZCU102 + AD9694-500EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9694_zcu102_setup.png
   :width: 800

Go to :ref:`the ZCU102 quickstart guide <ad9694 quickstart zcu102>`.

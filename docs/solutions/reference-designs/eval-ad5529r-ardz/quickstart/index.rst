.. _eval-ad5529r-ardz quickstart:

Quickstart
==========

This section provides step-by-step guides to get the EVAL-AD5529R-ARDZ
evaluation board running on supported carrier platforms.

.. _eval-ad5529r-ardz carriers:

Supported Carriers
------------------

.. list-table:: Hardware Compatibility
   :header-rows: 1
   :widths: 30 25 25 20

   * - Carrier Board
     - Connector
     - Interface
     - Status
   * - `Cora Z7-07S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`_
     - Arduino Shield
     - Arduino headers
     - Supported

.. _eval-ad5529r-ardz environments:

Supported Environments
----------------------

.. list-table:: Software Environment Support
   :header-rows: 1
   :widths: 30 20 50

   * - Environment
     - Status
     - Notes
   * - HDL
     - Supported
     - SPI Engine + DMA + PWM architecture
   * - Linux
     - Supported
     - IIO driver via Kuiper Linux
   * - No-OS
     - Planned
     - Bare-metal driver in development

Hardware Setup
--------------

.. TODO:: Add hardware setup photo (cora-z7-setup.png)

.. code-block:: rst

   .. figure:: ../images/cora-z7-setup.png
      :align: center
      :width: 700

      EVAL-AD5529R-ARDZ Connected to Cora Z7-07S

1. Connect the EVAL-AD5529R-ARDZ to the Cora Z7 Arduino headers
2. Insert a prepared MicroSD card (see :ref:`eval-ad5529r-ardz quickstart cora-z7`)
3. Connect the Micro-USB cable for UART console
4. Power on the Cora Z7

.. toctree::
   :glob:
   :maxdepth: 1

   *

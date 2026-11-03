.. _eval-ad7124-x quickstart:

Quickstart
===============================================================================

The following quick start guides provide step-by-step instructions for setting
up and using the AD7124 evaluation boards with their compatible carrier
platforms.

.. toctree::
   :titlesonly:

   EVAL-ADICUP3029 (with EVAL-AD7124-8-PMDZ) <adicup3029>
   SDP-B / Eval+ Software (with SDZ and ASDZ boards) <sdp_b>
   Nucleo-L476RG (with SDZ boards) <nucleo_l476rg>
   SDP-K1 / Mbed (with ASDZ boards) <sdp_k1>

.. _ad7124x carriers:

Supported Carriers
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 25 15

   * - Evaluation Board
     - Controller Board
     - Connection
     - Interface
   * - :adi:`EVAL-AD7124-8-PMDZ`
     - :adi:`EVAL-ADICUP3029`
     - Pmod connector
     - SPI
   * - :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>`
     - :adi:`SDP-B`
     - 120-pin SDP connector
     - SPI
   * - :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>`
     - `Nucleo-L476RG <https://www.st.com/en/evaluation-tools/nucleo-l476rg.html>`_
     - :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`
     - SPI
   * - :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>`
     - :adi:`SDP-B`
     - 120-pin SDP connector
     - SPI
   * - :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>`
     - `Nucleo-L476RG <https://www.st.com/en/evaluation-tools/nucleo-l476rg.html>`_
     - :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`
     - SPI
   * - :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>`
     - :adi:`SDP-B`
     - 120-pin SDP connector
     - SPI
   * - :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>`
     - :adi:`EVAL-SDP-CK1Z <SDP-K1>`
     - Arduino connectors
     - SPI
   * - :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>`
     - :adi:`SDP-B`
     - 120-pin SDP connector
     - SPI
   * - :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>`
     - :adi:`EVAL-SDP-CK1Z <SDP-K1>`
     - Arduino connectors
     - SPI

Supported Environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 25 20 20

   * - Controller Board
     - No-OS / Bare Metal
     - Mbed
     - STM32 HAL
   * - :adi:`EVAL-ADICUP3029`
     - :green:`Yes`
     -
     -
   * - :adi:`SDP-B`
     - :green:`Yes` (Eval+ Software)
     -
     -
   * - Nucleo-L476RG
     -
     -
     - :green:`Yes`
   * - :adi:`SDP-K1`
     -
     - :green:`Yes`
     -

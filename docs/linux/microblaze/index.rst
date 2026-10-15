.. _microblaze:

MicroBlaze
==========

Pre-built MicroBlaze Linux images (FPGA bitstream + kernel) for Analog Devices
FPGA carrier and FMC card combinations, and how to load them onto hardware.

To build the images yourself instead of using the pre-built ones, see
:ref:`linux-kernel microblaze`.

Latest release (2026_r1)
------------------------

:Build timestamp: ``2026_09_18 - 2026_r1``
:Packaged archive: ``microblaze_images_2026_r1.zip`` (one folder per design)
:Artifacts: Official download link to be added.

The release is built from the following components:

.. list-table::
   :header-rows: 1
   :widths: 20 35 35 25

   * - Component
     - Repository
     - Branch / tag
     - Commit
   * - Bitstream (``system_top.bit``)
     - `analogdevicesinc/hdl <https://github.com/analogdevicesinc/hdl>`__
     - `2026.1.0 <https://github.com/analogdevicesinc/hdl/releases/tag/2026.1.0>`__
     - `b62abef <https://github.com/analogdevicesinc/hdl/commit/b62abeff22d613d08e1aeb7f94850ab6a6576a74>`__
   * - Linux kernel (``simpleImage.strip``)
     - `analogdevicesinc/linux <https://github.com/analogdevicesinc/linux>`__
     - `xlnx/release/v6.12.y-2026r1 <https://github.com/analogdevicesinc/linux/tree/xlnx/release/v6.12.y-2026r1>`__ `xlnx_2026.1.0 <https://github.com/analogdevicesinc/linux/releases/tag/xlnx_2026.1.0>`__
     - `b47bbbe <https://github.com/analogdevicesinc/linux/commit/b47bbbe8ca7bc582c96251fa30d86e55de363f68>`__
   * - Root filesystem
     - `analogdevicesinc/buildroot <https://github.com/analogdevicesinc/buildroot>`__
     - `master <https://github.com/analogdevicesinc/buildroot/tree/master>`__
     - `0a81b12 <https://github.com/analogdevicesinc/buildroot/commit/0a81b12ba0b99749b28fc6473a6d60b672cc5f7b>`__

Supported FPGA carriers and FMC cards
-------------------------------------

20 images across 2 carriers. Each download is the design's folder inside
``microblaze_images_2026_r1.zip``.

.. list-table::
   :header-rows: 1
   :widths: 25 45 30

   * - FPGA carrier
     - FMC card
     - Download folder
   * - KCU105
     - ADRV9371X
     - ``kcu105_adrv9371x/``
   * - KCU105
     - FMCDAQ2
     - ``kcu105_fmcdaq2/``
   * - KCU105
     - FMCDAQ3
     - ``kcu105_fmcdaq3/``
   * - KCU105
     - FMCOMMS2-3
     - ``kcu105_fmcomms2-3/``
   * - KCU105
     - FMCOMMS4
     - ``kcu105_fmcomms4/``
   * - VCU118
     - AD9081 (204B tx17/rx18)
     - ``vcu118_ad9081/``
   * - VCU118
     - AD9081 (204B tx9/rx10, default)
     - ``vcu118_ad9081_m8_l4/``
   * - VCU118
     - AD9081 (default + Corundum 100G)
     - ``vcu118_ad9081_m8_l4_corundum/``
   * - VCU118
     - AD9081 (204C tx10/rx11, 16.5 Gbps)
     - ``vcu118_ad9081_204c_txmode_10_rxmode_11/``
   * - VCU118
     - AD9081 (204C tx10/rx11, 24.75 Gbps)
     - ``vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps/``
   * - VCU118
     - AD9081 (204C tx23/rx25, 16.5 Gbps)
     - ``vcu118_ad9081_204c_txmode_23_rxmode_25/``
   * - VCU118
     - AD9081 (204C tx23/rx25, 24.75 Gbps)
     - ``vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps/``
   * - VCU118
     - AD9081 (204C tx24/rx26, 24.75 Gbps)
     - ``vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps/``
   * - VCU118
     - AD9082
     - ``vcu118_ad9082/``
   * - VCU118
     - AD9084 (204C M4 L8 NP16, 4x4)
     - ``vcu118_ad9084_204C_M4_L8_NP16_20p0_4x4/``
   * - VCU118
     - ADRV9025
     - ``vcu118_adrv9025/``
   * - VCU118
     - ADRV9025 (JESD204C)
     - ``vcu118_adrv9025_jesd204c/``
   * - VCU118
     - ADRV9025 (NLS)
     - ``vcu118_adrv9025_nls/``
   * - VCU118
     - Dual AD9208
     - ``vcu118_dual_ad9208/``
   * - VCU118
     - FMCDAQ3
     - ``vcu118_fmcdaq3/``

.. note::

   **Changed in 2026_r1:** the ``KC705`` and ``VC707`` carriers are deprecated
   and removed from the HDL build matrix. ``ad_quadmxfe1_ebz`` (quad MxFE on
   VCU118) is temporarily excluded (Vivado 2024.2 update) and will return once
   fixed.

Archive contents
----------------

Each ``<carrier>_<fmc>/`` folder contains:

- ``system_top.bit`` — FPGA bitstream (from the HDL project)
- ``simpleImage.strip`` — MicroBlaze Linux kernel with the design's device tree
  embedded
- ``run.tcl`` — ``xsdb``/``xsct`` script that programs the FPGA and boots the
  kernel

Loading the image
-----------------

Use the AMD Xilinx toolchain (**2025.1**) — ``xsdb``/``xsct`` from Vivado/Vitis.
Run the commands from inside the design's own folder, as the scripts reference
``system_top.bit`` and ``simpleImage.strip`` by their plain names.

Method 1: run.tcl (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ source /path/to/Xilinx/2025.1/Vivado/settings64.sh
         $ cd <carrier>_<fmc>/
         $ xsdb run.tcl

   .. tab-item:: Windows

      .. shell:: ps1

         $ cd <carrier>_<fmc>
         $ c:/Xilinx/Vivado_Lab/2025.1/bin/xsdb.bat run.tcl

``run.tcl`` automates the full sequence:

.. mermaid::

   flowchart LR
       subgraph ATT["Attach"]
           A["connect<br/>attach to the JTAG hw_server"]
       end
       subgraph PRG["Program FPGA"]
           B["fpga -f system_top.bit<br/>program the FPGA<br/>with the bitstream"]
       end
       subgraph BOOT["Boot kernel"]
           direction TB
           C["select the<br/>MicroBlaze target"]
           D["dow simpleImage.strip<br/>load the Linux image<br/>into memory"]
           E["con<br/>start execution"]
           C --> D --> E
       end
       subgraph DET["Detach"]
           F["disconnect<br/>detach from the hw_server"]
       end

       A --> B --> C
       E --> F

       classDef session fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#263238
       classDef program fill:#e1f5ff,stroke:#01579b,stroke-width:2px,color:#013a63
       classDef load fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px,color:#10331a
       classDef run fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#5a2d00

       class A,C,F session
       class B program
       class D load
       class E run

Method 2: xsdb / xsct (manual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start ``xsdb`` and run the same steps manually:

::

   xsdb> connect
   xsdb> fpga -f system_top.bit
   xsdb> targets                 ;# list targets
   xsdb> target 3                ;# select the MicroBlaze #0 target
   xsdb> dow simpleImage.strip
   xsdb> con
   xsdb> disconnect

Method 3: xmd (legacy)
~~~~~~~~~~~~~~~~~~~~~~~~

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.strip
   xmd> run

Console access
--------------

Connect a terminal to the board's USB UART port:

- **Baud:** 115200, 8 data bits, no parity, 1 stop bit (8N1)

Default user accounts:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - User
     - Password
   * - ``root``
     - ``analog``
   * - ``analog``
     - ``analog``

Boards with an LCD display the DHCP-assigned IP address for remote access (SSH,
libiio). A displayed ``192.168.2.2`` means DHCP failed — check the subnet.

References
----------

- :ref:`Build the MicroBlaze Linux kernel from source <linux-kernel microblaze>`
- `ADI HDL documentation <https://analogdevicesinc.github.io/hdl/>`__
- `Reference wiki page (2023_R2) <https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/microblaze_loading>`__
- `HDL 2026.1.0 release notes <https://github.com/analogdevicesinc/hdl/releases/tag/2026.1.0>`__

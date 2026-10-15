.. _microblaze:

MicroBlaze
==========

Pre-built MicroBlaze Linux images — each a bootable Linux kernel, device tree,
and root filesystem — plus the matching FPGA bitstream, for ADI
evaluation boards on AMD Xilinx FPGA platforms, and how to load them onto hardware.

To build the images yourself instead of using the pre-built ones, see
:ref:`linux-kernel microblaze`.

Latest release (2026_r1)
------------------------

:Packaged archive: `microblaze_images_2026_r1.zip <https://packages.analog.com/public/raw/versions/2026_r1/microblaze_images_2026_r1.zip>`__ (per-design folders; multi-variant designs grouped)

The release is built from the following components:

.. list-table::
   :header-rows: 1
   :widths: 20 35 35

   * - Component
     - Repository
     - Tag
   * - Bitstream
     - `analogdevicesinc/hdl <https://github.com/analogdevicesinc/hdl>`__
     - `2026.1.0 <https://github.com/analogdevicesinc/hdl/releases/tag/2026.1.0>`__
   * - Linux kernel
     - `analogdevicesinc/linux <https://github.com/analogdevicesinc/linux>`__
     - `xlnx_2026.1.0 <https://github.com/analogdevicesinc/linux/releases/tag/xlnx_2026.1.0>`__
   * - Root filesystem
     - `analogdevicesinc/buildroot <https://github.com/analogdevicesinc/buildroot>`__
     - `2026.1.0 <https://github.com/analogdevicesinc/buildroot/releases/tag/2026.1.0>`__

Supported platforms and evaluation boards
-----------------------------------------

20 images across 2 AMD Xilinx FPGA platforms. Each download is the design's folder inside
``microblaze_images_2026_r1.zip``. Designs built in several variants (AD9081
and ADRV9025) are grouped under a shared folder, one subfolder per variant; the
paths below are relative to the archive root.

.. list-table::
   :header-rows: 1
   :widths: 12 20 38 30

   * - Platform
     - Evaluation board
     - Build parameters
     - Download folder
   * - KCU105
     - ADRV9371X
     - default
     - ``kcu105_adrv9371x/``
   * - KCU105
     - FMCDAQ2
     - default
     - ``kcu105_fmcdaq2/``
   * - KCU105
     - FMCDAQ3
     - default
     - ``kcu105_fmcdaq3/``
   * - KCU105
     - FMCOMMS2-3
     - default
     - ``kcu105_fmcomms2-3/``
   * - KCU105
     - FMCOMMS4
     - default
     - ``kcu105_fmcomms4/``
   * - VCU118
     - AD9081
     - default
     - ``vcu118_ad9081/vcu118_ad9081/``
   * - VCU118
     - AD9081
     - M8, L4
     - ``vcu118_ad9081/vcu118_ad9081_m8_l4/``
   * - VCU118
     - AD9081
     - M8, L4, Corundum 100G
     - ``vcu118_ad9081/vcu118_ad9081_m8_l4_corundum/``
   * - VCU118
     - AD9081
     - JESD204C, TX mode 10, RX mode 11
     - ``vcu118_ad9081/vcu118_ad9081_204c_txmode_10_rxmode_11/``
   * - VCU118
     - AD9081
     - JESD204C, TX mode 10, RX mode 11, 24.75 Gb/s lane rate
     - ``vcu118_ad9081/vcu118_ad9081_204c_txmode_10_rxmode_11_lr_24_75Gbps/``
   * - VCU118
     - AD9081
     - JESD204C, TX mode 23, RX mode 25
     - ``vcu118_ad9081/vcu118_ad9081_204c_txmode_23_rxmode_25/``
   * - VCU118
     - AD9081
     - JESD204C, TX mode 23, RX mode 25, 24.75 Gb/s lane rate
     - ``vcu118_ad9081/vcu118_ad9081_204c_txmode_23_rxmode_25_lr_24_75Gbps/``
   * - VCU118
     - AD9081
     - JESD204C, TX mode 24, RX mode 26, 24.75 Gb/s lane rate
     - ``vcu118_ad9081/vcu118_ad9081_204c_txmode_24_rxmode_26_lr_24_75Gbps/``
   * - VCU118
     - AD9082
     - default
     - ``vcu118_ad9082/``
   * - VCU118
     - AD9208
     - dual
     - ``vcu118_ad9082/vcu118_ad9208_dual/``  
   * - VCU118
     - AD9084
     - JESD204C, M4 L8 NP16, 20.0 Gb/s, 4×4
     - ``vcu118_ad9084_204C_M4_L8_NP16_20p0_4x4/``
   * - VCU118
     - ADRV9025
     - default
     - ``vcu118_adrv9025/vcu118_adrv9025/``
   * - VCU118
     - ADRV9025
     - JESD204C
     - ``vcu118_adrv9025/vcu118_adrv9025_jesd204c/``
   * - VCU118
     - ADRV9025
     - NLS
     - ``vcu118_adrv9025/vcu118_adrv9025_nls/``
   * - VCU118
     - FMCDAQ3
     - default
     - ``vcu118_fmcdaq3/``

.. note::

   **Changed in 2026_r1:** the ``KC705`` and ``VC707`` platforms are no longer
   supported. Quad MxFE on VCU118 is not included in this
   release.

Archive contents
----------------

At the archive root are three text files alongside the design folders:

- ``README.txt`` — release notes and usage summary
- ``LICENSE.txt`` — license terms
- ``SOURCES.txt`` — source repositories and tags the images were built from

Single-variant designs sit directly at the archive root. Designs built in
several variants are grouped under a shared folder named after the base design,
with one subfolder per variant (the base variant repeats the group name). The
download table above gives the exact path for each.

Every leaf design folder contains:

- ``system_top.bit`` — FPGA bitstream (from the HDL project)
- ``simpleImage.strip`` — the bootable MicroBlaze Linux image: kernel, device
  tree, and root filesystem
- ``run.tcl`` — ``xsdb``/``xsct`` script that programs the FPGA and boots the
  image

Loading the image
-----------------

The ``xsdb``/``xsct`` commands come from AMD Vitis (**2025.1**); sourcing
``Vitis/settings64.sh`` is enough, so Vivado is not required (sourcing
``Vivado/settings64.sh`` also works, as it sets up Vitis as well). Run the
commands from inside the design's own (leaf) folder, as the scripts reference
``system_top.bit`` and ``simpleImage.strip`` by their plain names. For a grouped
design the leaf folder is nested one level under the group folder, e.g.
``vcu118_ad9081/vcu118_ad9081_m8_l4/``.

Method 1: run.tcl (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ source /path/to/Xilinx/2025.1/Vitis/settings64.sh
         $ cd <design>/
         $ xsdb run.tcl

   .. tab-item:: Windows

      .. shell:: ps1

         $ cd <design>
         $ c:/Xilinx/Vivado_Lab/2025.1/bin/xsdb.bat run.tcl

``run.tcl`` runs the same sequence as the manual steps in Method 2 below:
connect, program the FPGA, select the MicroBlaze target, download the image,
run, and disconnect.

Method 2: xsdb / xsct (manual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start ``xsdb`` and run the same steps manually. Run ``targets`` first and note
the MicroBlaze target index for your design — it is not the same for every
design:

::

   xsdb> connect
   xsdb> fpga -f system_top.bit
   xsdb> targets                 ;# list targets
   xsdb> target <n>              ;# select the MicroBlaze target
   xsdb> dow simpleImage.strip
   xsdb> con
   xsdb> disconnect

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


References
----------

- :ref:`Build the MicroBlaze Linux kernel from source <linux-kernel microblaze>`
- `ADI HDL documentation <https://analogdevicesinc.github.io/hdl/>`__
- `HDL 2026.1.0 release notes <https://github.com/analogdevicesinc/hdl/releases/tag/2026.1.0>`__
- `Buildroot 2026.1.0 release notes <https://github.com/analogdevicesinc/buildroot/releases/tag/2026.1.0>`__

.. _linux-kernel microblaze:

Build MicroBlaze Linux kernel
=============================

On the development host
-----------------------

This guide provides some step-by-step instructions on how to build a Microblaze
Linux Kernel image for the FMC board connected to a:

* :xilinx:`KC705`
* :xilinx:`KCU105`
* :xilinx:`VC707`
* :xilinx:`VCU118`
* :xilinx:`VCU128`

The :git-linux:`main:/` contains the Linux Kernel flavor from Analog Devices Inc.
:download:`mb_rootfs <https://dev.azure.com/AnalogDevices/OpenSource/_build/results?buildId=63451&view=artifacts&pathAsName=false&type=publishedArtifacts>`
contains the files system to be used.
As the compiler, the Microblaze GNU Tools are included on both
:xilinx:`AMD Vivado <en/products/software/adaptive-socs-and-fpgas/vivado.html>` and
:xilinx:`AMD Vitis <en/products/software/adaptive-socs-and-fpgas/vivado.html>`, as well
as the ``xsdb`` tool for booting.

After ensuring all tools are installed, clone the :git-linux:`main:/`

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

The ``depth`` and ``no-single-branch`` options are included to speed up the
cloning by fetching only near the head of each branch/release, you may remove
them to fetch all history, but bear in mind it will go from around 800 MB to
around 3.4GB and growing.

Checkout the Release branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Use the latest release, if not required otherwise!

The release branches have the format ``<Year>_R[1|2]``, starting from ``2014_R2``.

.. shell::

   $git checkout origin/2026_R1 -b 2026_R1
    Branch 2026_R1 set up to track remote branch 2026_R1 from origin.
    Switched to a new branch '2026_R1'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Microblaze GNU Toolchain included in AMD Vivado/Xilinx is the recommended
compiler.

/data/opt/Xilinx/Vitis/$XVERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/

.. shell::

   $XVERSION=2026.1
   $GCC_MICROBLAZE=$PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/
   $export ARCH=microblaze
   $export CROSS_COMPILE="$GCC_MICROBLAZE/microblazeel-xilinx-linux-gnu-"

.. important::

   Find the path to the Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.
   Alternatively, you can replace Vitis with Vivado.

Compile the kernel
~~~~~~~~~~~~~~~~~~

Prepare the configuration. For AD9084 and AD9088, use:

.. shell::

   ~/linux
   $make adi_mb_apollo_defconfig
    #
    # configuration written to .config
    #

For other devices, use:

.. shell::

   ~/linux
   $make adi_mb_defconfig
    #
    # configuration written to .config
    #

Download the `mb_rootfs <https://dev.azure.com/AnalogDevices/OpenSource/_build/results?buildId=63451&view=artifacts&pathAsName=false&type=publishedArtifacts>`__
from the published artifacts and place it in the root of the kernel tree (*~/linux*).


The result of building the kernel is an elf file in *arch/microblaze/boot* named
`simpleImage.<dts-file>` based on the dts specified.

The build process for the kernel searches in the *arch/microblaze/boot/dts*
directory for a specified device tree file and then builds the device tree into
the kernel image.

The following command shows the general format for the build target name. Note
that the *<dts-file>* does not include the file extension *.dts*.

.. shell::

   ~/linux
   $make simpleImage.<dts-file>

.. tip::

   You can generate a :ref:`generic simpleImage and overwrite the dtb <linux-kernel microblaze dtb-hack>`
   instead.

To see what device-trees for the different FPGA carrier and FMC module combination exist type:

.. shell::

   ~/linux
   $ls -l arch/microblaze/boot/dts

So, for example, for *vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dts*:

.. shell::

   ~/linux
   $make simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
      SYNC    include/config/auto.conf.cmd
      CC      scripts/mod/empty.o
      CC      scripts/mod/devicetable-offsets.s
      MKELF   scripts/mod/elfconfig.h
      HOSTCC  scripts/mod/modpost.o
      HOSTCC  scripts/mod/sumversion.o
      HOSTCC  scripts/mod/file2alias.o

    [ --snip-- ]

      AR      init/built-in.a
      LD      vmlinux.o
      MODPOST vmlinux.symvers
      MODINFO modules.builtin.modinfo
      GEN     modules.builtin
      LD      .tmp_vmlinux.kallsyms1
      KSYMS   .tmp_vmlinux.kallsyms1.S
      AS      .tmp_vmlinux.kallsyms1.S
      LD      .tmp_vmlinux.kallsyms2
      KSYMS   .tmp_vmlinux.kallsyms2.S
      AS      .tmp_vmlinux.kallsyms2.S
      LD      vmlinux
      SORTTAB vmlinux
      SYSMAP  System.map
      OBJCOPY arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
      SHIPPED arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.unstrip
      STRIP   vmlinux arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip
      UIMAGE  arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.ub
    Image Name:   Linux-5.10.0-97916-g513446e488c3
    Created:      Tue Jan 18 12:07:35 2022
    Image Type:   MicroBlaze Linux Kernel Image (uncompressed)
    Data Size:    18398124 Bytes = 17966.92 KiB = 17.55 MiB
    Load Address: 80000000
    Entry Point:  80000000
    Kernel: arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1 is ready  (#3678)

The STRIP image (*.strip*) found under *arch/microblaze/boot* is the ELF image
to load via the debugger.

.. _linux-kernel microblaze dtb-hack:

Patch a DTB to a simpleImage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Microblaze embeds the device tree into the simpleImage, but if you need to
generate a batch of images with the same kernel, you can create an "empty"
devicetree, build the simpleImage:

.. shell::

   /path/to/linux
   $ printf "/dts-v1/;\n\n/ { };\n" > arch/microblaze/boot/dts/generic.dts
   $ make simpleImage.generic

Locate the embedded empty DTB slot using a helper script:

.. code-block:: python
   :caption: find_empty_dtb.py

   import struct, sys

   # 'Empty' DTB struct block: FDT_BEGIN_NODE, '', FDT_END_NODE, FDT_END
   EMPTY_STRUCT = bytes.fromhex('00000001000000000000000200000009')
   DTB_MAGIC = 0xd00dfeed
   OFF_DT_STRUCT = 56

   with open(sys.argv[1], 'rb') as f:
       data = f.read()

   pos = 0
   while True:
       pos = data.find(EMPTY_STRUCT, pos)
       if pos == -1:
           break
       dtb_start = pos - OFF_DT_STRUCT
       if dtb_start < 0:
           pos += 1
           continue
       magic = struct.unpack('>I', data[dtb_start:dtb_start+4])[0]
       if magic != DTB_MAGIC:
           pos += 1
           continue
       if struct.unpack('>I', data[dtb_start+8:dtb_start+12])[0] != OFF_DT_STRUCT:
           pos += 1
           continue
       dtb_size = struct.unpack('>I', data[dtb_start+4:dtb_start+8])[0]
       dtb_end = dtb_start + dtb_size
       boundary = dtb_end
       while boundary < len(data) and data[boundary] == 0:
           boundary += 1
       print(f'{dtb_start} {dtb_size} {boundary} {boundary - dtb_start}')
       sys.exit(0)

   sys.exit(1)

Then build the target DTB, zero the slot, and write the new DTB in place:

.. shell::
   :no-path:

   $ image=arch/microblaze/boot/simpleImage.generic.strip
   $ dtb=vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dtb
   $ read dtb_start dtb_size dtb_boundary dtb_available < <(python3 find_empty_dtb.py "$image")
   $ make $dtb
   # Copy generic image and patch the copy
   $ dtb_length=$((dtb_boundary - dtb_start))
   $ image_out="$(dirname $image)/simpleImage.${dtb%.dtb}.strip"
   $ cp "$image" "$image_out"
   $ dd if=/dev/zero \
       of="$image_out" \
       bs=1 seek=$dtb_start conv=notrunc count=$dtb_length
    68152 bytes (68 kB, 67 KiB) copied, 0.0198292 s, 3.4 MB/s
   $ dd if="arch/microblaze/boot/dts/$dtb" \
        of="$image_out" \
        bs=1 seek=$dtb_start conv=notrunc
    31787 bytes (32 kB, 31 KiB) copied, 0.0111866 s, 2.8 MB/s

.. _linux-kernel microblaze boot:

Boot on FPGA MicroBlaze
~~~~~~~~~~~~~~~~~~~~~~~

One method to load the kernel onto the already built and running FPGA which has
the MicroBlaze processor is to use ``xsdb``/``xsct`` or ``xmd`` from the AMD
Xilinx Vivado/Vitis toolset to download the build *.strip* file.

Go to the folder containing the *.strip* and *system_top.bit* file, to flash the
bitstream and download the Image.

.. note::

   The **system_top.bit** is obtained from the HDL project.
   Learn how to :external+hdl:ref:`build_hdl`, but instead of using the generated
   **\*.sdk/system_top.xsa**, use the **\*.runs/impl_1/system_top.bit**.

With ``xsdb``/``xsct``:


.. tab-set::

   .. tab-item:: Linux

      .. shell:: sh

         $ source /path/to/Xilinx/2026.1/Vivado/settings64.sh
         $ xsdb

   .. tab-item:: Windows

      .. shell:: ps1

         $ c:/Xilinx/Vivado_Lab/2026.1/bin/xsdb.bat

Then use the commands to program the FPGA:

::

   xsdb> connect
   xsdb> fpga -f system_top.bit
   xsdb> targets
     1  xcku040
        2  MicroBlaze Debug Module at USER2
           3  MicroBlaze #0 (Running)
   xsdb> targets 3
   xsdb> dow simpleImage.kcu105_fmcdaq2.strip
   xsdb> con
   xsdb> disconnect

To automate, the same commands can be added to a *.tcl* script and run with ``xsdb run.tcl``.
In this case, make sure you add an ``after 5000`` command between ``targets 3`` and ``dow...``,
to allow enough time for the MIG to calibrate.

With ``xmd``:

::

   xmd> fpga -f system_top.bit
   xmd> connect mb mdm
   xmd> dow simpleImage.vc707_fmcomms2-3.strip
   xmd> run

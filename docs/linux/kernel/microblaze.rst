.. _linux-kernel microblaze:

Build MicroBlaze Linux kernel
=============================

On the development host
-----------------------

This guide provides some step-by-step instructions on how to build a MicroBlaze
Linux Kernel image for the FMC board connected to a:

* :xilinx:`KC705`
* :xilinx:`KCU105`
* :xilinx:`VC707`
* :xilinx:`VCU118`
* :xilinx:`VCU128`

The :git-linux:`main:/` contains the Linux Kernel flavor from Analog Devices Inc.
:download:`mb_rootfs <https://artprodcus3.artifacts.visualstudio.com/Adb5ce8ff-2df6-4e7b-a491-7c0f5e26801a/02a28b00-b3c8-4fdf-af9c-c2460499147f/_apis/artifact/cGlwZWxpbmVhcnRpZmFjdDovL0FuYWxvZ0RldmljZXMvcHJvamVjdElkLzAyYTI4YjAwLWIzYzgtNGZkZi1hZjljLWMyNDYwNDk5MTQ3Zi9idWlsZElkLzYzNDUxL2FydGlmYWN0TmFtZS9tYl9yb290ZnM1/content?format=zip>`
contains the files system to be used.
As the compiler, the MicroBlaze GNU Tools are included on both
:xilinx:`AMD Vivado <en/products/software/adaptive-socs-and-fpgas/vivado.html>` and
:xilinx:`AMD Vitis <en/products/software/adaptive-socs-and-fpgas/vivado.html>`, as well
as the ``xsdb`` tool for booting.

After ensuring all tools are installed, clone the :git-linux:`main:/`

.. shell::

   $ git clone https://github.com/analogdevicesinc/linux.git \
                --no-single-branch --depth=10 \
                -- linux

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

   $ git checkout origin/2026_R1 -b 2026_R1
     Branch 2026_R1 set up to track remote branch 2026_R1 from origin.
     Switched to a new branch '2026_R1'

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MicroBlaze GNU Toolchain included in AMD Vivado/Xilinx is the recommended
compiler.

/data/opt/Xilinx/Vitis/$XVERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/

.. shell::

   $ XVERSION=2026.1
   $ GCC_MICROBLAZE=$PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/microblaze/linux_toolchain/lin64_le/bin/
   $ export ARCH=microblaze
   $ export CROSS_COMPILE="$GCC_MICROBLAZE/microblazeel-xilinx-linux-gnu-"

.. important::

   Find the path to the AMD Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.
   Alternatively, you can replace Vitis with Vivado.

Compile the kernel
~~~~~~~~~~~~~~~~~~

Prepare the configuration. For AD9084 and AD9088, use:

.. shell::

   ~/linux
   $ make adi_mb_apollo_defconfig
    #
    # configuration written to .config
    #

For other devices, use:

.. shell::

   ~/linux
   $ make adi_mb_defconfig
    #
    # configuration written to .config
    #

Download the `mb_rootfs <https://artprodcus3.artifacts.visualstudio.com/Adb5ce8ff-2df6-4e7b-a491-7c0f5e26801a/02a28b00-b3c8-4fdf-af9c-c2460499147f/_apis/artifact/cGlwZWxpbmVhcnRpZmFjdDovL0FuYWxvZ0RldmljZXMvcHJvamVjdElkLzAyYTI4YjAwLWIzYzgtNGZkZi1hZjljLWMyNDYwNDk5MTQ3Zi9idWlsZElkLzYzNDUxL2FydGlmYWN0TmFtZS9tYl9yb290ZnM1/content?format=zip>`__
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
   $ make simpleImage.<dts-file>

.. tip::

   You can generate a :ref:`generic simpleImage and overwrite the dtb <linux-kernel microblaze dtb-hack>`
   instead.

To see what device-trees for the different FPGA carrier and FMC module combination exist type:

.. shell::

   ~/linux
   $ ls -l arch/microblaze/boot/dts

So, for example, for *vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dts*:

.. shell::

   ~/linux
   $ make simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
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

MicroBlaze embeds the device tree into the simpleImage, but if you need to
generate a batch of images with the same kernel, you can create an "empty"
devicetree, build the simpleImage:

.. shell::

   ~/linux
   $ printf "/dts-v1/;\n\n/ { };\n" > arch/microblaze/boot/dts/generic.dts
   $ make simpleImage.generic
   $ rm arch/microblaze/boot/dts/generic.dts

Locate the embedded DTB slot using a helper script (also in :git+linux:`ci:ci/lib.sh`):

.. code-block:: python
   :caption: find_empty_dtb.py

   import struct
   import sys

   # 'Empty' DTB structure block: FDT_BEGIN_NODE, '', FDT_END_NODE, FDT_END
   EMPTY_STRUCT = bytes.fromhex('00000001000000000000000200000009')
   DTB_MAGIC = 0xd00dfeed
   OFF_DT_STRUCT = 56

   image = sys.argv[1]
   with open(image, 'rb') as f:
       data = f.read()

   def elf_section(name):
       # Returns the file offset and size of the named ELF section
       if data[:4] != b'\x7fELF':
           sys.exit(f'{image}: not an ELF file')
       end = '<' if data[5] == 1 else '>'
       if data[4] == 1:
           shoff, = struct.unpack_from(end + 'I', data, 32)
           shentsize, shnum, shstrndx = struct.unpack_from(end + 'HHH', data, 46)
           sh = end + 'IIIIII'
       else:
           shoff, = struct.unpack_from(end + 'Q', data, 40)
           shentsize, shnum, shstrndx = struct.unpack_from(end + 'HHH', data, 58)
           sh = end + 'IIQQQQ'
       headers = [struct.unpack_from(sh, data, shoff + i * shentsize)
                  for i in range(shnum)]
       strtab = headers[shstrndx][4]
       for sh_name, _, _, _, offset, size in headers:
           if data[strtab + sh_name:data.index(b'\0', strtab + sh_name)] == name:
               return offset, size
       sys.exit(f'{image}: no {name.decode()} section')

   start, slot_size = elf_section(b'__fdt_blob')
   magic, size, off_dt_struct = struct.unpack_from('>III', data, start)
   struct_block = data[start + OFF_DT_STRUCT:start + OFF_DT_STRUCT + len(EMPTY_STRUCT)]
   if (magic != DTB_MAGIC or off_dt_struct != OFF_DT_STRUCT or
           struct_block != EMPTY_STRUCT):
       sys.exit(f'{image}: __fdt_blob does not hold an empty DTB')

   print(start, size, slot_size)

And the following script, which copies the image, clears the slot, and writes
the DTB in it, after checking that the DTB is valid and fits in the slot:

.. code-block:: sh
   :caption: patch_dtb.sh

   #!/bin/sh
   # Usage: patch_dtb.sh <simpleImage.generic.strip> <dtb> <output image>
   set -e
   image=$1
   dtb=$2
   out=$3

   slot=$(python3 "$(dirname "$0")/find_empty_dtb.py" "$image")
   set -- $slot
   start=$1
   slot_size=$3

   magic=$(od -An -tx1 -N4 "$dtb" | tr -d ' \n')
   if [ "$magic" != d00dfeed ]; then
       echo "$dtb: not a DTB" >&2
       exit 1
   fi
   size=$(stat -c %s "$dtb")
   if [ "$size" -gt "$slot_size" ]; then
       echo "$dtb: $size bytes, larger than the $slot_size bytes slot" >&2
       exit 1
   fi

   cp "$image" "$out"
   dd if=/dev/zero of="$out" bs=1 seek="$start" count="$slot_size" \
      conv=notrunc status=none
   dd if="$dtb" of="$out" bs=1 seek="$start" conv=notrunc status=none
   echo "$out: $size bytes DTB at offset $start"

Then build the DTB and patch it into a copy of the image, for example for
*vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.dts*:

.. shell::

   ~/linux
   $ dts=vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1
   $ make $dts.dtb
   $ sh patch_dtb.sh arch/microblaze/boot/simpleImage.generic.strip \
       arch/microblaze/boot/dts/$dts.dtb \
       arch/microblaze/boot/simpleImage.$dts.strip
     arch/microblaze/boot/simpleImage.vcu118_quad_ad9081_204c_txmode_23_rxmode_25_onchip_pll_revc_nz1.strip: 31807 bytes DTB at offset 9118368

To patch several devicetrees, repeat the last two steps for each one:

.. shell::

   ~/linux
   $ for dts in vcu118_quad_ad9084_revB vcu118_quad_ad9084_26p4_revB ; do \
        make $dts.dtb
        sh patch_dtb.sh arch/microblaze/boot/simpleImage.generic.strip \
           arch/microblaze/boot/dts/$dts.dtb \
           arch/microblaze/boot/simpleImage.$dts.strip ; \
     done

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

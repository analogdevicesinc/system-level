.. _linux-kernel zynqmp:

Build ZynqMP / MPSoC Linux kernel and devicetree
================================================

Using a script
--------------

We provide
:git-wiki-scripts:`a script <raw+linux/build_zynqmp_kernel_image.sh>`
that does automates the build for Zynq using the Linaro toolchain.

.. attention::

   This script differs from the one for Zynq.

The script takes up to 3 parameters, but if left blank, it uses defaults:

#. **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this,
   if you want to use an already cloned kernel repo
#. **<devicetree_file>** - which device tree should be exported/copied from the
   build. Default is ``xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb`` for
   ZynqMP
#. **<path_to_other_toolchain>** - in case you have your own preferred toolchain
   (other than Linaro's or AMD Xilinx's) you can use override it with this 3rd paramameter

The script will:

* Clone the ADI kernel tree
* Download the Linaro GCC toolchain (if no other is specified)
* Build the ADI kernel tree
* Export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line, with defaults:

.. shell::

   $wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynqmp_kernel_image.sh && \
   $       chmod +x build_zynqmp_kernel_image.sh && \
   $       ./build_zynqmp_kernel_image.sh


Building with Petalinux
-----------------------

Please see here: :ref:`linux-kernel petalinux`.

On the development host
-----------------------

Make sure you have ``u-boot-tools`` installed, to have the ``mkimage`` utility
available. You can install it via your distro's package manager.

Then

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

or do a git pull in a existing cloned repository.

The ``depth`` and ``no-single-branch`` options are included to speed up the
cloning by fetching only near the head of each branch/release, you may remove
them to fetch all history, but bear in mind it will go from around 800MB to
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

Add aarch64-linux-gnu-gcc to PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the AMD Xilinx toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   $source $PATH_TO_XILINX/Vitis/$VITIS_VERSION/settings64.sh
   $which aarch64-linux-gnu-gcc
    $PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/aarch64/lin/aarch64-linux/bin/aarch64-linux-gnu-gcc

.. important::

   Find the path to the AMD Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.

.. shell::

   $export ARCH=arm64
   $export CROSS_COMPILE="aarch64-linux-gnu-"

Using the Arm GNU Toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Arm GNU Toolchain can be used to compile the kernel.
Download the ``aarch64-none-linux-gnu`` tarball for your host from the
`Arm GNU Toolchain downloads <https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>`__
page. Always use the latest release just in case.

Extract the downloaded tarball and set the environment variables:

.. shell::

   $export ARCH=arm64
   $export CROSS_COMPILE=$(pwd)/<extracted-toolchain-dir>/bin/aarch64-none-linux-gnu-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the
kernel tree.

.. shell::

   $make adi_zynqmp_defconfig
    #
    # configuration written to .config
    #

Build the kernel via 'make'. This is the same for all Xlinx ZYNQMP MPSoC FPGAs.

.. shell::

   $make -j5 Image UIMAGE_LOADADDR=0x8000
      CHK     include/config/kernel.release
      CHK     include/generated/uapi/linux/version.h
      HOSTCC  scripts/basic/fixdep
      HOSTCC  scripts/basic/bin2c

    [ -- snip --]

      CC      init/version.o
      LD      init/built-in.o
      KSYM    .tmp_kallsyms1.o
      KSYM    .tmp_kallsyms2.o
      LD      vmlinux
      SORTEX  vmlinux
      SYSMAP  System.map
      OBJCOPY arch/arm64/boot/Image

Build the devicetree FCMOMMS2/3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card

.. list-table::
   :header-rows: 1

   - - device tree
     - board
     - chip
   - - zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dts
     - :xilinx:`ZCU102` **Rev. 1.0**
     - | :ref:`fmcomms2` or
       | :ref:`ad-fmcomms3-ebz hardware-guide` board
   - - zynqmp-zcu102-rev10-ad9364-fmcomms4.dts
     - :xilinx:`ZCU102` **Rev. 1.0**
     - | :ref:`fmcomms4` board
   - - zynqmp-zcu102-revB-ad9361-fmcomms2-3.dts
     - :xilinx:`ZCU102` Rev.B
     - | :ref:`fmcomms2` or
       | :ref:`ad-fmcomms3-ebz hardware-guide` board
   - - zynqmp-zcu102-revB-ad9364-fmcomms4.dts
     - :xilinx:`ZCU102` Rev.B
     - | :ref:`fmcomms4` board

The device tree **zynqmp-zcu102-revA.dts** can also be used for any ZCU102 FPGA
that uses an SD card for boot up. Building the device tree uses 'make' by
turning the .dts file to a .dtb. The command is simply 'make' plus the device
tree name with a .dtb file extension.

.. shell::

   $make xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb
    DTC     arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **uImage** and
**<device_tree_name>.dtb**. Refer to the code below to find their respective
output directories. Take note that the device tree file needs to be renamed to
**devicetree.dtb**.
See :external+kuiper:doc:`index` for more information in configuring the
SD card with Kuiper.

.. shell::

   $cp arch/arm64/boot/Image /media/michael/BOOT/
   $cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-revB-ad9361-fmcomms2-3.dtb /media/michael/BOOT/system.dtb

Common Issues
-------------

This sections goes through common issues related to the Linux Kernel on the
ZynqMP.

.. _zynqmp displayport-no-picture:

DisplayPort - no picture?
~~~~~~~~~~~~~~~~~~~~~~~~~

The default configuration for most of the projects is to use the HDMI output,
and that is what the configuration is set up for.

For DisplayPort projects, you may need to add a custom ``xorg.conf`` file.

.. code:: bash

   printf 'Section "Device"
     Identifier "myfb"
     Driver "fbdev"
     Option "fbdev" "/dev/fb0"
   EndSection' > /etc/X11/xorg.conf

After following that, the board should be rebooted.

You can find a list with tested monitors
:xilinx:`here <support/answers/68671.html>`.
Resolution or image problems may appear if there is used a monitor that was not
tested.



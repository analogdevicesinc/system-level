.. _linux-kernel zynq:

Build Zynq Linux kernel and devicetree
======================================

Using a script
--------------

We provide
:git-wiki-scripts:`a script <raw+linux/build_zynq_kernel_image.sh>`
that does automates the build for Zynq using the Linaro toolchain.

The script takes up to 3 parameters, but if left blank, it uses defaults:

#. **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this,
   if you want to use an already cloned kernel repo
#. **<devicetree_file>** - which device tree should be exported/copied from the
   build. Default is ``zynq-zc702-adv7511-ad9361-fmcomms2-3.dtb`` for Zynq
#. **<path_to_other_toolchain>** - in case you have your own preferred toolchain
   (other than Linaro's or Xilinx's) you can use override it with this 3rd param

The script will:

* Clone the ADI kernel tree
* Download the Linaro GCC toolchain (if no other is specified)
* Build the ADI kernel tree
* Export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line, with defaults:

.. shell::

   $wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_zynq_kernel_image.sh && \
   $chmod +x build_zynq_kernel_image.sh && \
   $./build_zynq_kernel_image.sh

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

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few toolchains that can be used. The AMD Xilinx toolchain is
recommended, but the Linaro toolchain can also be used.

Other toolchains/compilers for ARM may work as well, but the ones described here
have been tested and found to work.

Using the AMD Xilinx toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   - - Release names and Branches
     - Required Vivado/Vitis versions
   - - 2014_R2
     - Vivado 2014.2
   - - 2015_R2
     - Vivado 2015.2
   - - 2016_R1
     - Vivado 2015.4.2
   - - 2016_R2
     - Vivado 2016.2
   - - 2017_R1
     - Vivado 2016.4
   - - 2018_R1
     - Vivado 2017.4
   - - 2018_R2
     - Vivado 2018.2
   - - 2019_R1
     - Vivado 2018.3
   - - 2019_R2
     - Vivado 2019.1
   - - 2021_R1
     - Vivado 2021.1
   - - 2021_R2
     - Vivado 2021.2
   - - 2022_R2
     - Vivado 2022.2
   - - 2023_R2
     - Vivado 2023.2
   - - 2026_R1
     - Vivado 2026.1

.. shell::

   $source $PATH_TO_XILINX/Vitis/$VITIS_VERSION/settings64.sh
   $which which arm-linux-gnueabihf-gcc
    $PATH_TO_XILINX/Vitis/$VITIS_VERSION/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin/arm-linux-gnueabihf-gcc

.. important::

   Find the path to the Xilinx installation folder, and then use
   it to replace this string: **$PATH_TO_XILINX** that is written above.
   Same goes for the **$VITIS_VERSION**, where you choose the Vitis version.

.. shell::

   $export ARCH=arm
   $export CROSS_COMPILE="arm-linux-gnueabihf-"

Using the Arm GNU Toolchain
^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, the Arm GNU Toolchain can be used to compile the kernel.
Download the ``arm-none-linux-gnueabihf`` tarball for your host from the
`Arm GNU Toolchain downloads <https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>`__
page. Always use the latest release just in case.

Extract the downloaded tarball and set the environment variables:

.. shell::

   $export ARCH=arm
   $export CROSS_COMPILE=$(pwd)/<extracted-toolchain-dir>/bin/arm-none-linux-gnueabihf-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

Inside the repository, generate the configuration file before building the
kernel tree.
The command shown below is generic and is not project specific.
As long as the board is a ZYNQ FPGA, use the configuration below.

.. shell::

   $make zynq_xcomm_adv7511_defconfig
    #
    # configuration written to .config
    #

Build the kernel
~~~~~~~~~~~~~~~~

Build the kernel via 'make'. This is the same for all AMD Xilinx ZYNQ FPGAs.

.. shell::

   $make -j5 UIMAGE_LOADADDR=0x8000 uImage
    scripts/kconfig/conf --silentoldconfig Kconfig
      CHK     include/config/kernel.release
      CHK     include/generated/uapi/linux/version.h
      UPD     include/config/kernel.release
      CHK     include/generated/utsrelease.h

    [ -- snip --]

      AS      arch/arm/boot/compressed/bswapsdi2.o
      AS      arch/arm/boot/compressed/piggy.gzip.o
      LD      arch/arm/boot/compressed/vmlinux
      OBJCOPY arch/arm/boot/zImage
      Kernel: arch/arm/boot/zImage is ready
      UIMAGE  arch/arm/boot/uImage
    Image Name:   Linux-3.17.0-126697-g611e217-dir
    Created:      Fri Nov 28 10:20:40 2014
    Image Type:   ARM Linux Kernel Image (uncompressed)
    Data Size:    3195872 Bytes = 3120.97 kB = 3.05 MB
    Load Address: 00008000
    Entry Point:  00008000

Build the devicetree FCMOMMS2/3/4/5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card

.. list-table::
   :header-rows: 1

   - - device tree
     - board
     - chip
   - - zynq-adrv9361-z7035-bob
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-bob-cmos
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-packrf
     - :adi:`ADRV-PACKRF`
     - | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-fmc
     - :adi:`ADRV1CRR-FMC`
     - | :adi:`ADV7511` (on-board) and the
       | :adi:`ADRV9361`
   - - zynq-adrv9361-z7035-fmc-rfcard-tdd
     - :adi:`ADRV1CRR-FMC`
     - | :adi:`ADV7511` (on-board), the
       | :adi:`ADRV9361` and the
       | :adi:`AD-PZSDR2400TDD-EB`
   - - zynq-adrv9364-z7020-bob
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9364`
   - - zynq-adrv9364-z7020-bob-cmos
     - :adi:`ADRV1CRR-BOB`
     - | :adi:`ADRV9364`
   - - zynq-adrv9364-z7020-packrf
     - :adi:`ADRV-PACKRF`
     - | :adi:`ADRV9364`
   - - zynq-coraz7s
     - `Cora Z7`_
     - |
   - - zynq-mini-itx-adv7511
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board)
   - - zynq-mini-itx-adv7511-ad9361-fmcomms2-3
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board)
       | :ref:`fmcomms2`
       | :ref:`ad-fmcomms3-ebz hardware-guide`
   - - zynq-mini-itx-adv7511-ad9364-fmcomms4
     - `Mini-ITX`_
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms4` board
   - - zynq-zc702-adv7511
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board)
   - - zynq-zc702-adv7511-ad9361-fmcomms2-3
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms2` or
       | :ref:`ad-fmcomms3-ebz hardware-guide` board
   - - zynq-zc702-adv7511-ad9361-fmcomms5
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad-fmcomms5-ebz`
   - - zynq-zc702-adv7511-ad9364-fmcomms4
     - :xilinx:`ZC702`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms4` board
   - - zynq-zc706-adv7511
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board)
   - - zynq-zc706-adv7511-ad6676-fmc
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`eval-ad6676 eval` board
   - - zynq-zc706-adv7511-ad9265-fmc-125ebz
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`eval_ad9265` board
   - - zynq-zc706-adv7511-ad9361-fmcomms2-3
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms2` or
       | :ref:`ad-fmcomms3-ebz hardware-guide` board
   - - zynq-zc706-adv7511-ad9361-fmcomms5
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad-fmcomms5-ebz` board
   - - zynq-zc706-adv7511-ad9361-fmcomms5-ext-lo-adf5355
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad-fmcomms5-ebz` board
   - - zynq-zc706-adv7511-ad9364-fmcomms4
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms4` board
   - - zynq-zc706-adv7511-ad9434-fmc-500ebz
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad9434` board
   - - zynq-zc706-adv7511-ad9625-fmcadc2
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad_fmcadc2_ebz eval` board
   - - zynq-zc706-adv7511-ad9739a-fmc
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :adi:`EVAL-AD9739A`
   - - zynq-zc706-adv7511-adrv9371
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`adrv9371x block diagram` board
   - - zynq-zc706-adv7511-adrv9375
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`adrv9371x block diagram` board
   - - zynq-zc706-adv7511-fmcadc4
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad_fmcadc4_ebz eval` board
   - - zynq-zc706-adv7511-fmcdaq2
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad-fmcdaq2-ebz hardware` board
   - - zynq-zc706-adv7511-fmcdaq3
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`AD-FMCDAQ3-EBZ <ad_fmcdaq3_ebz>` board
   - - zynq-zc706-adv7511-fmcjesdadc1
     - :xilinx:`ZC706`
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad_fmcjesdadc1_ebz eval` board
   - - zynq-zc706-imageon
     - :xilinx:`ZC706`
     - | FMC-IMAGEON
   - - zynq-zed-adv7511
     - `Zed Board <http://zedboard.org/product/zedboard>`__
     - :adi:`ADV7511` (on-board)
   - - zynq-zed-adv7511-ad9361-fmcomms2-3
     - `Zed Board <http://zedboard.org/product/zedboard>`__
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms2` or
       | :ref:`ad-fmcomms3-ebz hardware-guide` board
   - - zynq-zed-adv7511-ad9364-fmcomms4
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`fmcomms4` board
   - - zynq-zed-adv7511-ad9467-fmc-250ebz
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`ad9467_fmc_250ebz` board
   - - zynq-zed-adv7511-cn0363
     - `ZedBoard`_
     - | :adi:`ADV7511` (on-board) and the
       | :ref:`eval-cn0363-pmdz` board
   - - zynq-zed-imageon
     - `ZedBoard`_
     - | FMC-IMAGEON

.. _ZedBoard: https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard
.. _Mini-ITX: https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/mini-itx
.. _Cora Z7: https://digilent.com/reference/programmable-logic/cora-z7/start

Building the device tree uses 'make' by turning the .dts file to a .dtb. The
command is simply 'make' plus the device tree name with a .dtb file extension.

.. shell::

   $make zynq-zc702-adv7511-ad9361.dtb
    DTC     arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output files for building the kernel and device tree are **uImage** and
**<device_tree_name>.dtb**. Refer to the code below to find their respective
output directories. Take note that the device tree file needs to be renamed to
**devicetree.dtb**.
See :external+kuiper:doc:`index` for more information in configuring the
SD card with Kuiper.

.. shell::

   $cp arch/arm/boot/uImage /media/BOOT/uImage
   $cp arch/arm/boot/dts/zynq-zc702-adv7511-ad9361.dtb  /media/BOOT/devicetree.dtb

On the target platform (devicetrees)
------------------------------------

To modify devicetrees on the target platform:

#. Make sure the boot partition is mounted. On new images, this can be done by
   right-clicking the boot icon on the desktop and selecting the "Mount Volume"
   option. The partition will then be mounted at */media/analog/boot*.

#. Convert the compiled devicetree related to the target back into an editable
   format.

   .. shell::

      $cd /media/analog/boot/zynq-zc702-adv7511
      $dtc -I dtb -O dts -o devicetree.dts devicetree.dtb


#. Modify the devicetree.dts file as required.

#. Recompile the devicetree file. Note that this will overwrite the original dtb
   file, copy or rename the original file if you want to keep it before running
   this step.

   .. shell::

      $cd /media/analog/boot/zynq-zc702-adv7511
      $dtc -I dts -O dtb -o devicetree.dtb devicetree.dts


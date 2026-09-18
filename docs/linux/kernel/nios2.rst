.. imported from: https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/nios2

.. _linux-kernel nios2:

Nios2 Linux on Altera FPGA Development Boards
==============================================

.. warning::

   Support for the A10GX carrier is discontinued and will not be supported in
   future releases. The last supported HDL release is **hdl_2021_r1**.

Pre-built images
----------------

Pre-built Linux images are available for the following hardware configurations:

.. list-table::
   :header-rows: 1

   * - Carrier
     - FMC Card
   * - `Arria 10 GX <https://www.altera.com/products/devkit/po-3017/arria-10-gx-fpga-development-kit>`_
     - :adi:`EVAL-ADRV9008-9009`, :adi:`ADRV9371`, :adi:`EVAL-AD-FMCDAQ2-EBZ`,
       :adi:`EVAL-AD-FMCDAQ3-EBZ`
   * - `Arria V GT <https://www.altera.com/products/devkit/po-3017/arria-v-gt-fpga-development-kit>`_
     - :adi:`AD-FMCJESDADC1-EBZ`

..
   Download the pre-built image for you setup:

   A10GX carrier:
   - ADRV9009 + A10GX (2019_R2): https://swdownloads.analog.com/cse/nios2/2019_r2/adrv9009_a10gx.zip
   - ADRV9371x + A10GX (2019_R2): https://swdownloads.analog.com/cse/nios2/2019_r2/adrv9371x_a10gx.zip
   - FMCDAQ2 + A10GX (2019_R2): https://swdownloads.analog.com/cse/nios2/2019_r2/daq2_a10gx.zip
   - FMCDAQ2 + A10GX (2018_R1): daq2_a10gx_2018_r1.zip
   - FMCDAQ2 + A10GX (2016_R1): a10gx_daq2_2016_r1.zip
   - FMCDAQ3 + A10GX (2016_R1): a10gx_daq3_2016_r1.zip
   - FMCDAQ2 + A10GX (2015_R2): a10gx_daq2_2015_r2.zip
   - FMCDAQ2 + A10GX (2015_R1): a10gx_daq2_2015_r1.zip

   A5GT carrier:
   - FMCJESDADC1 + A5GT (2015_R2): a5gt_fmcjesdadc1_2015_r2.zip
   - FMCJESDADC1 + A5GT (2015_R1): a5gt_fmcjesdadc1_2015_r1.zip

   Master/latest images:
   - https://swdownloads.analog.com/cse/nios2/master/latest_nios2_images.tar.gz

On Windows with Quartus II installed, run the provided ``program.bat`` script to
program the board. This will flash the FPGA bitfile and Linux ELF image, then
launch a Nios2 terminal displaying the Linux console output.

IIO Oscilloscope remote
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install :ref:`IIO Oscilloscope <iio-oscilloscope>` on a host PC and connect
remotely to the target platform:

#. Open **Settings > Connect**
#. Select **Manual** and enter the URI: ``ip:<board-ip>``
#. Press **Refresh** then **Connect**

To determine the board IP, log in on the Nios2 terminal with user ``root`` and
password ``analog``, then run ``ifconfig``.

Building Linux
--------------

Using a script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::

   $wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/main/linux/build_nios2_kernel_image.sh && \
   $chmod +x build_nios2_kernel_image.sh && \
   $./build_nios2_kernel_image.sh

The script will:

- Clone the ADI kernel repository
- Download the Nios2 GCC toolchain
- Compile the kernel
- Export the zImage and device tree files

Step-by-step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the ADI Linux kernel:

.. shell::

   $git clone https://github.com/analogdevicesinc/linux.git \
   $            --no-single-branch --depth=10 \
   $            -- linux

Checkout the release branch:

.. shell::

   ~/linux
   $git checkout origin/2021_R1 -b 2021_R1

Download the root filesystem:

.. shell::

   ~/linux
   $wget https://swdownloads.analog.com/cse/nios2/rootfs/rootfs.cpio.gz

Set up the cross-compile environment:

.. shell::

   $export ARCH=nios2
   $export CROSS_COMPILE=/path/to/nios2-toolchain/bin/nios2-linux-gnu-

.. important::

   Replace ``/path/to/nios2-toolchain`` with the actual path to your Nios2
   GNU toolchain installation.

Configure and build:

.. shell::

   ~/linux
   $make adi_nios2_defconfig

Copy the appropriate device tree for your hardware:

.. list-table::
   :header-rows: 1

   * - Carrier + FMC
     - Device Tree
   * - A10GX + DAQ2
     - ``a10gx_daq2.dts``
   * - A10GX + DAQ3
     - ``a10gx_daq3.dts``
   * - A5GT + FMCJESDADC1
     - ``a5gt_fmcjesdadc1.dts``

Build the kernel:

.. shell::

   ~/linux
   $make zImage

.. _linux-kernel zynq-hdmi:

Embedded ARM and AD9361/AD9364
===============================================================================

The image for the AD9361/AD9364 based boards can be found, and created by
following the directions :external+kuiper:doc:`here <index>`.

After that is complete, and running, you should see the IIO scope, which will be
described :ref:`here <iio-oscilloscope>`

ZC706
-------------------------------------------------------------------------------

The default slot for the AD9361 based boards is the LPC FMC slot, as shown:

.. image:: images/fmcomm2_zc706photo2.jpg
   :width: 600

Linux with HDMI video output on the ZED, ZC702 and ZC706 boards
-------------------------------------------------------------------------------

Supported devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`ADV7511`
- :adi:`FMCOMMS-1 <ad-fmcomms1-ebz>`
- :adi:`FMCOMMS-2 <ad-fmcomms2-ebz>`
- :adi:`FMCOMMS-3 <ad-fmcomms3-ebz>`
- :adi:`FMCOMMS-4 <ad-fmcomms4-ebz>`
- :adi:`FMCOMMS-5 <ad-fmcomms5-ebz>` (ZC702, ZC706 only)
- :adi:`AD-FMCADC2-EBZ <ad-fmcadc2-ebz>` (ZC706 only)
- :adi:`AD-FMCDAQ2-EBZ <ad-fmcdaq2-ebz>` (ZC706 only)
- :adi:`EVAL-FMCDAQ3-EBZ` (ZC706 only)
- :adi:`AD-FMCJESDADC1-EBZ <ad-fmcjesdadc1-ebz>` (ZC706 only)

Supported carriers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `ZC702 <https://www.xilinx.com/ZC702>`__
- `ZC706 <https://www.xilinx.com/ZC706>`__
- `Zed Board <http://zedboard.org/content/overview>`_
  (not for :adi:`FMCOMMS-5 <ad-fmcomms5-ebz>`)

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/adv7511.png
   :width: 400

Preparing the SD-card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To boot the system on the ZED, ZC702 or ZC706 board you'll need a SD memory
card. The SD card should have at least 4 GB of storage and it is recommended to
use a card with speed-grade 6 or higher to achieve optimal file transfer
performance.

The SD card needs to be partitioned with two partitions. The first one should be
about 40MB in size and the second one should take up the remaining space. For
optimal performance make sure that the partitions are 4MB aligned. The first
partition needs to be formatted with a FAT filesystem. It will hold the
bootloader, devicetree and kernel images. The second partition needs to be
formatted with a ext4 filesystem. It will store the systems root filesystem.

.. image:: images/linux-zynq-gparted-sdcard.png
   :width: 600

Obtain the HDL reference design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ZYNQ does not have a on-chip graphics or audio core, instead the FPGA is
used to generate the necessary signals to deliver the video and audio streams to
the ADV7511. Analog Devices provides a reference HDL design which contain
support for generating the necessary video and audio as well as support for
interfacing with the AD-FMCOMMS1-EBZ.

The HDL reference designs can be downloaded from their respective wiki page:

- :external+hdl:ref:`ADV7511 XILINX KC705, VC707, ZC702 AND ZED REFERENCE DESIGN <adv7511>`
- :dokuwiki:`AD-FMCOMMS1-EBZ REFERENCE DESIGN <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`
- :external+hdl:ref:`AD-FMCOMMS2-EBZ DESIGN <fmcomms2>`

.. hint::

   The AD-FMCOMMS1-EBZ reference designs for the ZED, ZC702 and ZC706 include
   support for the ADV7511. So you only need one of the reference designs
   depending on whether you want support for the AD-FMCOMMS1-EBZ or not.

You can either use the provided reference designs to build your own system.bit
or use a pre-build system.bit file. The system.bit will be required in the next
step.

Build the boot image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To complete this step you need to have a u-boot image for the Zynq platform.
Please refer to the `Xilinx wiki
<https://xilinx-wiki.atlassian.net/wiki/spaces/A/overview>`_ on how to build
such an image.

The bootloader can be build with Xilinx SDK. In order to do so it is necessary
to first export the HDL design from the Xilinx Platform Studio to the SDK, this
is done by clicking the "Export to SDK" button in the Platform Studio GUI.

Export project to SDK:

.. image:: images/linux-zynq-export-xps.png
   :width: 600

Once the project has been exported create a new FSBL project in the SDK. To do
this right-click on the newly exported hardware platform specification in left
"Project Explorer" panel and select "New > Project" from the popup menu. Select
"Xilinx - Application Project" on first dialog page. On the second dialog page
choose a name for the project (zynq_fsbl for example) and on the third page
select "Zynq FSBL" template.

.. image:: images/linux-zynq-xsdk-fsbl1.png
   :width: 400

.. image:: images/linux-zynq-xsdk-fsbl2.png
   :width: 400

.. image:: images/linux-zynq-xsdk-fsbl3.png
   :width: 400

The project should build automatically. If not a manual build can be started by
right clicking the newly created project in the left "Project Explorer" panel
and selecting "Build Project" from the popup menu. After the project has been
build it is time to generate the boot image. This is done by right clicking on
the project in the left "Project Explorer" pane and selecting "Create Boot
Image". This will open up the bootgen wizard. The bootgen wizard needs three
files:

- The freshly build zynq_fsbl.elf binary
- The system.bit bitstream
- The u-boot.elf binary

Add these files to partitions list in the dialog, then select an output folder.

.. image:: images/linux-zynq-bootgen.png
   :width: 400

Clicking "Create Image" will now generate in the chosen location a new boot
image for the target platform. The output \*.bin file should be named "BOOT.BIN"
and needs to be saved on the first partition of the SD-card.

Alternative method of building the Zynq boot image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The boot image BOOT.BIN is build using the bootgen tool which requires several
input files.

Instructions on how to build the Hardware Description File (HDF) handover file
can be found here:

- :external+hdl:ref:`Building HDL <build_hdl>`

All further steps are lengthy explained in the :external+hdl:ref:`Build the boot
image BOOT.BIN <build_boot_bin>` guide and on the `Xilinx Wiki Page
<http://www.wiki.xilinx.com>`_

- `Build u-boot <http://www.wiki.xilinx.com/Build+U-Boot>`_

  - Make sure you checkout the proper git tag matching your Vivado Version
    (xilinx-v2018.2, xilinx-v2017.4, ...)

- `Build FSBL <http://www.wiki.xilinx.com/Build+FSBL>`_
- `Build PMU Frimware <http://www.wiki.xilinx.com/Build+PMU+Firmware>`_
- `Build Arm Trusted Firmware (ATF) <http://www.wiki.xilinx.com/Build+Arm+Trusted+Firmware+%28ATF%29>`_
- `Build BOOT image <http://www.wiki.xilinx.com/Prepare+Boot+Image>`_

Use script to build BOOT.BIN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For ease of use we provide a bash shell script which allows building BOOT.BIN
from system_top.hdf, u-boot.elf and either bl31.elf or a path to the Arm Trusted
Firmware repository

Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The script can be downloaded from here:

- `build_zynqmp_boot_bin.sh <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynqmp_boot_bin/build_zynqmp_boot_bin.sh>`_

.. tip::

   **NOTE: After downloading the script you need to make it executable**

   .. code-block:: bash

      $ chmod +x build_zynqmp_boot_bin.sh

Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   usage: build_zynqmp_boot_bin.sh system_top.xsa u-boot.elf (download | bl31.elf | <path-to-arm-trusted-firmware-source>) [output-archive]

- Path to ``system_top.xsa`` and ``u-boot.elf`` are required parameters.
- The 3rd argument must either be ``download`` (which will git clone the ATF
  repository), ``bl31.elf`` or the file system ``path`` to the Arm Trusted
  Firmware source code repository
- An optionally 4th ``name`` parameter can be given to tar.gz the output
  directory. (``name``.tar.gz)
- Build output is located in a local directory named: output_boot_bin.
- This script requires Xilinx Vitis and bootgen in the PATH.

  - A simple way is to source vivado settings[32|64].sh for Linux:

  .. code-block:: bash

     $ source /opt/Xilinx/Vivado/202x.x/settings64.sh

  - When using **cygwin**, you can add the following in the ~/.bashrc
    configuration file:

  .. code-block:: bash

     export PATH=$PATH:/cygdrive/c/Xilinx/Vivado/202x.x/bin
     export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/bin
     export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin

.. tip::

   **NOTE: u-boot.elf**

   For those who don't want to build u-boot themselves.
   The **u-boot.elf** can be extracted from the project folder on the
   :external+kuiper:doc:`SD Card image <index>`, **bootgen_sysfiles.tgz**

Build and install the kernel image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The prerequistes for following these instructions are to have:

   - mkimage from your distribution (normally ``apt-get install u-boot-tools``)
   - C compiler from the Xilinx SDK

.. note::

   The most stable kernel source tree containing support for the ZED, ZC702 and
   ZC706 plus **AD-FMCOMMS1-EBZ** can be found at :git-linux:`2016_R1
   <2016_R1:>`. For the
   **AD-FMCOMMS2-EBZ** use also the :git-linux:`2016_R1
   <2016_R1:>` branch.

Download and build the kernel image:

.. code-block:: console

   > git clone https://github.com/analogdevicesinc/linux.git
   Cloning into 'linux'...
   remote: Counting objects: 2550298, done.
   remote: Compressing objects: 100% (466978/466978), done.
   remote: Total 2550298 (delta 2118600), reused 2483072 (delta 2058083)
   Receiving objects: 100% (2550298/2550298), 727.70 MiB | 353 KiB/s, done.
   Resolving deltas: 100% (2118600/2118600), done.
   Checking out files: 38170/38170), done.
   > cd linux
   > # For AD-FMCOMMS2-EBZ use
   > # git checkout master
   > export ARCH=arm
   > export CROSS_COMPILE=/path/to/your/arm/cross-compiler
   > # e.g. export CROSS_COMPILE=/opt/CodeSourcery/Sourcery_G++_Lite/bin/arm-xilinxa9-linux-gnueabi-
   > make zynq_xcomm_adv7511_defconfig
   #
   # configuration written to .config
   #
   > make uImage LOADADDR=0x00008000
     ...
     OBJCOPY arch/arm/boot/uImage
     Kernel: arch/arm/boot/uImage is ready

.. note::

   The same kernel image is used for all HDL reference design.

The next step is to build the devicetree for your target platform. While the
kernel is the same for all target boards the devicetree file differs as it
describes the board specifics.

.. important::

   The devicetree must match the HDL reference design that is used. It is not
   possible to use a adv7511 only devicetree for a AD-FMCOMMS1-EBZ reference
   HDL design, even if the AD-FMCOMMS1-EBZ is not connected to the FMC slot.

To build the devicetree from the devicetree file run
``make name-dts-replaced-by-dtb``

Build the devicetree for ZED with HDMI video out and XCOMM:

.. code-block:: console

   > make zynq-zed-adv7511-xcomm.dtb
     DTC     arch/arm/boot/zynq-zed-adv7511-xcomm.dtb
   DTC: dts->dtb  on file "arch/arm/boot/dts/zynq-zed-adv7511-xcomm.dts"

The last step is to copy both the kernel and the devicetree files to the first
partition of the SD card. It is important to rename the devicetree file to
devicetree.dtb

Copy kernel and device tree to SD card:

.. code-block:: console

   > cp arch/arm/boot/uImage /media/BOOT/uImage
   > cp arch/arm/boot/zynq-zed-adv7511-xcomm.dtb /media/BOOT/devicetree.dtb

uEnv.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default environment that is used by the u-boot bootloader instructions the
kernel to use a ramfs disk for its root filesystem. In order to boot from the SD
card it is necessary to overwrite the default environment. This can be done by
placing a file called uEnv.txt in the BOOT partition of the SD card. This file
will be read by u-boot and is used to replace the default environment.

**uEnv.txt for using SD card rootfs**

.. code-block::

   uenvcmd=run adi_sdboot
   adi_sdboot=echo Copying Linux from SD to RAM... && fatload mmc 0 0x3000000 ${kernel_image} && fatload mmc 0 0x2A00000 ${devicetree_image} && if fatload mmc 0 0x2000000 ${ramdisk_image}; then bootm 0x3000000 0x2000000 0x2A00000; else bootm 0x3000000 - 0x2A00000; fi
   bootargs=console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait

Install the root file system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will use a `Linaro Ubuntu ARM <http://linaro.org>`_ rootfs as
it provides a good out of the box experience. The latest version can be found on
the `Linaro Download page <http://www.linaro.org/downloads/>`_. In this example
we will use the 12.11 release.

The first step is to download the
`archive containing the root filesystem <https://releases.linaro.org/archive/12.12/ubuntu/vexpress/linaro-precise-ubuntu-desktop-20121124-560.tar.gz>`_.

Download Linaro Ubuntu ARM rootfs:

.. code-block:: console

   > wget http://releases.linaro.org/archive/12.12/ubuntu/vexpress/linaro-precise-ubuntu-desktop-20121124-560.tar.gz

The next step is to extract the root filesystem from the archive to the SD card.
It is important to preserve the file permission and owner settings, otherwise
the system will be unable to boot. Since some of the files have root permissions
it is necessary to run the extraction process as root.

Extract the root filesystem onto the SD card:

.. code-block:: console

   > sudo tar --strip-components=3 -C /media/rootfs -xzpf linaro-precise-ubuntu-desktop-20121124-560.tar.gz binary/boot/filesystem.dir
   > ls /media/rootfs/
   bin/  boot/  dev/  etc/  home/  lib/  lost+found/  media/  mnt/ opt/
   proc/  root/  run/  sbin/  selinux/  srv/  sys/  tmp/  usr/  var/

Testing the system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once all of the previous tasks have been completed it is time to test the
system. To do this insert the SD-card into the board and power-up the board.
After a few seconds the blue "DONE" LED should light up. This means that the
bitstream has been loaded and the system will now start to boot. It is also
possible to connect to the serial console by using the on-board UART-to-USB
bridge, this allows to monitor the boot process and view debug messages.

After another few seconds the monitor connected to the system will turn on and
display the `Linux mascot <https://en.wikipedia.org/wiki/Tux>`_ in the top left
corner, after that the Ubuntu Desktop system will appear on the screen. The
system is now ready to be used.

Post-installation tweaks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the system has been installed it is time to do some post-installation
tweaks to the system. None of them is required to get a basic working system,
but they improve the overall video and audio experience quite a bit.

Enable xf86-video-modesetting Xorg driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The xf86-video-modesetting driver is a driver which has been written to take
advantage of the new Kernel Mode Setting (KMS) API of the DRM layer. This allows
to switch between different screen resolutions at runtime (using the Xservers
xrandr interface) and adds plug-and-play support for monitors.

Unfortunately the current Linaro Ubuntu distribution does not contain a package
for xf86-video-modesetting driver. So it becomes necessary to manually download
and build it. Open up a terminal on the target system and run the following
commands.

Download and install xf86-video-modesetting:

.. code-block:: console

   > sudo apt-get install xserver-xorg-dev libdrm-dev xutils-dev
   > wget http://xorg.freedesktop.org/archive/individual/driver/xf86-video-modesetting-0.9.0.tar.bz2
   > tar -xjf xf86-video-modesetting-0.9.0.tar.bz2
   > cd xf86-video-modesetting-0.9.0
   > ./configure --prefix=/usr
   > make
   > sudo make install

To enable the modesetting driver the create /etc/X11/xorg.conf and add
following lines:

Enable the modesetting driver:

.. code-block::

     Section "Device"
       Identifier "ADV7511 HDMI"
       Driver "modesetting"
     EndSection

Fixing issues with pulse audio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PulseAudio is the audio daemon used by default on the Linaro Ubuntu
installation. Unfortunately PulseAudio's 'glitch-free' algorithm seems to cause
audio glitches on this particular platform. To get seamless audio experience it
is necessary to disable the glitch-free feature. To disable the 'glitch-free'
feature of pulse audio open up a terminal on the target system an run the
following commands.

Disable pulse audio 'glitch-free' feature:

.. code-block:: console

   > sed -i 's,load-module module-udev-detect.*,load-module module-udev-detect tsched=0,' /etc/pulse/default.pa

More information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :dokuwiki:`AD-FMCOMMS1-EBZ Reference Design <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`
- :ref:`AD-FMCOMMS2-EBZ User Guide <fmcomms2>`
- :ref:`AD-FMCOMMS3-EBZ User Guide <ad-fmcomms3-ebz>`
- :dokuwiki:`AD-FMCOMMS4-EBZ User Guide <resources/eval/user-guides/ad-fmcomms4-ebz>`
- :dokuwiki:`AD-FMCOMMS5-EBZ User Guide <resources/eval/user-guides/ad-fmcomms5-ebz>`
- :dokuwiki:`AD-FMCDAQ2-EBZ User Guide <resources/eval/user-guides/ad-fmcdaq2-ebz>`
- :dokuwiki:`AD-FMCADC2-EBZ User Guide <resources/eval/user-guides/ad-fmcadc2-ebz>`
- :ref:`ADI IIO Oscilloscope <iio-oscilloscope>`
- :external+linux:doc:`ADV7511 HDMI transmitter Linux Driver <drivers/drm/adv7511>`
- :external+linux:doc:`AXI HDMI HDL Linux Driver <drivers/drm/hdl-axi-hdmi>`
- :external+linux:doc:`HDL AXI SPIDF Linux Driver <drivers/sound/hdl-axi-spidf>`
- :external+linux:doc:`HDL AXI I2S Linux Driver <drivers/sound/hdl-axi-i2s>`
- :external+linux:doc:`AD9523-1: Low Jitter Clock Generator <drivers/iio-pll/ad9523>`
- :external+linux:doc:`ADF4351: Wideband Synthesizer with Integrated VCO <drivers/iio-pll/adf4350>`
- :external+linux:doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers <drivers/iio-amplifiers/ad8366>`
- :external+linux:doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual ADC <drivers/iio-adc/axi-adc-hdl>`
- :external+linux:doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+ DAC <drivers/iio-dds/axi-dac-dds-hdl>`
- :external+linux:doc:`AD9361 RF Agile Transceiver Linux device driver <drivers/iio-transceiver/ad9361>`

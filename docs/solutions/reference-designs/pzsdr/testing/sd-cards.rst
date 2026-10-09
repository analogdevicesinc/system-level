.. _pzsdr testing sd-cards:

Creating ADRV9361 RF SOM production testing SD cards
===============================================================================

SOM2
-------------------------------------------------------------------------------

The code for all the various pieces required to create testing SD cards can be
found on GitHub:

.. admonition:: Download
   :class: download

   **U-Boot:**

   -  U-Boot test branch: :git-u-boot-xlnx:`tree/pzsdr-test`
   -  U-Boot QSPI booting branch: :git-u-boot-xlnx:`tree/qspiboot`

   A version of U-Boot built from the test branch will run through the tests
   assuming a properly formatted SD card, while the QSPI branch is for
   flashing to the device.

   **No-OS:**

   -  HDL dev branch: https://github.com/analogdevicesinc/hdl/tree/dev/projects/pzsdr/ccbrk
   -  Loopback test: :git-no-OS:`projects/capi_selftest/boards/loopback`

   Xilinx SDK 2015.2 is currently required to build both of these projects.

In order to create an SD card for testing, the various test binaries, U-Boot
versions, and other files must be built and placed in the correct location in
the boot partition of the standard SD card image. See the following hierarchy
of test and flash related files on an SD card's boot partition mounted at
``/media/BOOT``:

.. code-block:: none

   /media/BOOT
   ├── BOOT.BIN
   ├── devicetree.dtb
   ├── flash
   │   ├── BOOT.BIN
   │   ├── system.bit
   │   └── uramdisk.image.gz
   ├── ad9361.elf
   ├── loopback.elf
   └── uImage

FPGA bitstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The bitstream is already available on the SD card in the
``bootgen_sysfiles.tgz`` file located in the related platform directory on
the BOOT partition. This assumes the SD card's BOOT partition is already
mounted at ``/media/BOOT``.

.. code-block:: bash

   mkdir -p ~/zynq-picozed-sdr2/bootgen
   cd /media/BOOT/zynq-picozed-sdr-bob
   tar -xvf bootgen_sysfiles.tgz -C ~/zynq-picozed-sdr2/bootgen
   mkdir -p /media/BOOT/flash
   cp ~/zynq-picozed-sdr2/bootgen/system.bit /media/BOOT/flash/

Now build a different bitstream used for various test features:

.. code-block:: bash

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/hdl
   cd hdl/projects/pzsdr/ccbrk
   git checkout dev
   make pzsdr.ccbrk

Symlink the created bitstream into the unpacked bootgen directory:

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/bootgen
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.runs/impl_1/system_top.bit

Creating the main U-Boot test binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/u-boot-xlnx
   cd u-boot-xlnx
   git checkout pzsdr-test
   export CROSS_COMPILE=arm-xilinx-eabi-
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)

Create the BOOT.BIN file. The default bif file has a few file name mismatches —
the bitstream name mismatch is already corrected (symlinked above). Fix the
FSBL name:

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/bootgen
   mv zynq_fsbl_0.elf fsbl.elf
   cp ~/zynq-picozed-sdr2/u-boot-xlnx/u-boot ./u-boot-picozed.elf
   bootgen -image zynq.bif -w -o BOOT.BIN
   cp BOOT.BIN /media/BOOT/

Creating the QSPI U-Boot binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes you have already cloned the U-Boot repository in the previous
step.

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/u-boot-xlnx
   git clean -fxd
   git checkout qspiboot
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)
   cp u-boot ~/zynq-picozed-sdr2/bootgen/u-boot-picozed-qspi.elf

Create a new bif file at ``~/zynq-picozed-sdr2/bootgen/zynq-qspi.bif``:

.. code-block:: none

   the_ROM_image:
   {
   [bootloader]./fsbl.elf
   ./u-boot-picozed-qspi.elf
   }

This removes the FPGA bitstream from the generated BOOT.BIN (it will be
flashed separately) and points to the newly generated U-Boot ELF file.

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/bootgen
   bootgen -image zynq-qspi.bif -w -o BOOT.BIN
   cp BOOT.BIN /media/BOOT/flash/

Creating the no-OS test ELFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/no-OS
   cd no-OS/pzsdr/ccbrk/loopback
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.sdk/system_top.hdf
   make
   cp sdk/loopback/Release/loopback.elf /media/BOOT

.. note::

   The ``ad9361`` and Linux/device tree sections for SOM2, and the full SOM1
   section, are TODO.

SOM1
-------------------------------------------------------------------------------

.. note::

   SOM1 instructions are TODO.

FMC Carrier
-------------------------------------------------------------------------------

The code for all the various pieces required to create testing SD cards can be
found on GitHub:

.. admonition:: Download
   :class: download

   **U-Boot:**

   -  U-Boot test branch: :git-u-boot-xlnx:`tree/pzsdr-ccfmc-test`

   **No-OS:**

   -  Tests for various loopback modules (PMOD, camera, FMC, SFP+) run at
      the U-Boot level: :git-no-OS:`projects/capi_selftest/boards/loopback`
   -  HDL dev branch: https://github.com/analogdevicesinc/hdl/tree/dev/projects/pzsdr/ccfmc

   **Test script:**

   -  Bash script to automate the various interface tests:
      :git-board-tests:`picozed-sdr2-fmc/runtests.sh`
   -  The remaining files used by the tests:
      :git-board-tests:`picozed-sdr2-fmc`

First, write the latest available SD card image from
`kuiper-linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
to a spare card and prepare it to boot into Linux as detailed on that page.

FPGA bitstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   mkdir -p ~/zynq-picozed-sdr2/bootgen
   cd /media/BOOT/zynq-picozed-sdr-bob
   tar -xvf bootgen_sysfiles.tgz -C ~/zynq-picozed-sdr2/bootgen

Build a loopback-enabled bitstream:

.. code-block:: bash

   mkdir -p ~/zynq-picozed-sdr2
   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/hdl
   cd hdl/projects/pzsdr/ccfmc
   git checkout dev
   make pzsdr.ccfmc

Symlink the created bitstream:

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/bootgen
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.runs/impl_1/system_top.bit

Creating the main U-Boot test binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/u-boot-xlnx
   cd u-boot-xlnx
   git checkout pzsdr-ccfmc-test
   export CROSS_COMPILE=arm-xilinx-eabi-
   make zynq_picozed_sdr2_defconfig
   make -j$(nproc)

.. code-block:: bash

   cd ~/zynq-picozed-sdr2/bootgen
   mv zynq_fsbl_0.elf fsbl.elf
   cp ~/zynq-picozed-sdr2/u-boot-xlnx/u-boot ./u-boot-picozed.elf
   bootgen -image zynq.bif -w -o BOOT.BIN
   cp BOOT.BIN /media/BOOT/

Creating the no-OS test ELFs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~/zynq-picozed-sdr2
   git clone https://github.com/analogdevicesinc/no-OS
   cd no-OS/pzsdr/ccfmc/loopback
   ln -s ~/zynq-picozed-sdr2/hdl/projects/pzsdr/ccbrk/ccbrk_pzsdr.sdk/system_top.hdf
   make
   cp sdk/loopback/Release/loopback.elf /media/BOOT

Linux test scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the board testing repository into the analog user's home directory,
then set it to run automatically on boot:

.. code-block:: bash

   git clone https://github.com/analogdevicesinc/board-tests
   rm -f /home/analog/.config/autostart/*
   cat << EOF > /home/analog/.config/autostart/picozed-sdr2-fmc-tests.desktop
   [Desktop Entry]
   Exec=sudo /home/analog/board-tests/picozed-sdr2-fmc/runtests.sh
   Terminal=True
   Type=Application
   Name=PicoZed SDR2 FMC tests
   GenericName=PicoZed SDR2 FMC tests
   EOF
   chmod +x /home/analog/.config/autostart/picozed-sdr2-fmc-tests.desktop

The SD card will now automatically launch the test script in a terminal window
on startup.

Breakout Board
-------------------------------------------------------------------------------

ADI image changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Mount the boot partition:

   .. code-block:: bash

      mount /dev/mmcblk0p1 /media/boot/

#. Decompile the device tree:

   .. code-block:: bash

      dtc -I dtb -O dts -o /media/boot/devicetree.dts /media/boot/devicetree.dtb

#. Remove all ``gpio_keys`` mappings from the device tree
   (``vim /media/boot/devicetree.dts``):

   .. code-block:: none

      gpio_keys {
          compatible = "gpio-keys";
          #address-cells = <0x1>;
          #size-cells = <0x0>;
          autorepeat;

          pb0 { label = "Left"; linux,code = <0x69>; gpios = <0x6 0x36 0x0>; };
          pb1 { label = "Right"; linux,code = <0x6a>; gpios = <0x6 0x37 0x0>; };
          pb2 { label = "Up"; linux,code = <0x67>; gpios = <0x6 0x38 0x0>; };
          pb3 { label = "Down"; linux,code = <0x6c>; gpios = <0x6 0x39 0x0>; };
          sw0 { label = "SW0"; linux,input-type = <0x5>; linux,code = <0x0>; gpios = <0x6 0x3e 0x0>; };
          sw1 { label = "SW1"; linux,input-type = <0x5>; linux,code = <0x1>; gpios = <0x6 0x3f 0x0>; };
          sw2 { label = "SW2"; linux,input-type = <0x5>; linux,code = <0x2>; gpios = <0x6 0x40 0x0>; };
          sw3 { label = "SW3"; linux,input-type = <0x5>; linux,code = <0x3>; gpios = <0x6 0x41 0x0>; };
      };

#. Recompile the device tree:

   .. code-block:: bash

      dtc -I dts -O dtb -o /media/boot/devicetree.dtb /media/boot/devicetree.dts

#. Copy ``runtests.sh`` to ``/root`` and make it executable:

   .. code-block:: bash

      chmod +x runtests.sh

#. Add a call to ``/root/runtests.sh`` in ``/etc/rc.local``.

Raspberry Pi image changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Configure
   `Adafruit PiTFT 2.2" HAT Mini Kit <https://www.adafruit.com/product/2315>`_
   (320×240 2.2" TFT, No Touch).
#. Add ``breakout_board_test.py`` and ``reboot_poweroff.py`` to ``/home/pi/``.
#. Add the following line to the end of ``.bashrc``:

   .. code-block:: bash

      python /home/pi/breakout_board_test.py & python /home/pi/reboot_poweroff.py &

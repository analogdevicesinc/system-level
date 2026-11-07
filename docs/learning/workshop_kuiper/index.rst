.. collection:: Customizing ADI Kuiper Linux
   :subtitle: Build and customize ADI Kuiper Linux images.
   :label: workshop

   Learn to configure Kuiper 2 images and interact with ADI hardware.

   system-level:
     - .
     - learning/workshops_embedded_linux/index
     - learning/converter_connectivity_tutorial/index

Customizing ADI Kuiper Linux
============================

Introduction
------------

This workshop is designed to explore the ADI Kuiper Linux distribution and teach
you how to customize it for your specific needs. ADI Kuiper Linux is an
open-source Linux distribution created by Analog Devices for product evaluation
boards and reference designs. Through hands-on activities, you'll learn to build
custom Kuiper 2 images, configure boot files for different carrier boards, and
interact with ADI hardware using IIO tools.

Slide Deck and Booklet
----------------------

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

.. admonition:: Download

   :download:`Customizing ADI Kuiper Linux Slide Deck <ftc_2025_kuiper.pdf>`

A complete booklet of the hands-on activity is also provided, as a companion to
following the tutorial yourself:

.. admonition:: Download

   :download:`Customizing ADI Kuiper Linux Booklet <ftc_2025_kuiper_booklet.pdf>`

Theory
------

- Introduction to ADI Kuiper Linux
- What Does Kuiper Include
- Unlocking the Power of Kuiper 2

  - Key Features
  - Stages Anatomy
  - Build Flow
  - Configuration File
  - Supported Versions
  - Extra Scripts

Introduction to ADI Kuiper Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI Kuiper Linux is an open-source Linux distribution for Analog Devices. It
serves as the primary distribution for product evaluation boards and reference
designs.

- It includes pre-built boot files, device drivers and a variety of development
  utilities
- Supports over 140 FPGA-based projects and over 30 Raspberry Pi-based designs
- The first release was published at the beginning of 2021

What Does Kuiper Include
~~~~~~~~~~~~~~~~~~~~~~~~

*Boot Files*

- More than 1,300 Linux device drivers for Analog Devices products
- Pre-built boot files for over 140 FPGA-based projects and over 30 RPi-based
  designs
- Supported platforms include:

  - AMD/Xilinx: Zynq, Zynq MP, Versal
  - Intel FPGA: Cyclone5, Arria10, Stratix10
  - Raspberry Pi: 2, 3, 4, 5

*Libraries and Applications*

A variety of development utilities, software libraries and examples for
different projects:

- LibIIO - Linux Industrial I/O library
- IIO Oscilloscope - Signal visualization tool
- PyADI-IIO - Python for ADI Industrial I/O Devices
- ADI-LIBM2k - Interface library for the ADALM2000
- GNU Radio - The free and open software radio ecosystem
- Scopy - Multi-functional software tool

Unlocking the Power of Kuiper 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Key Features*

- Kuiper 2 is a **Debian based** distribution
- Contains a **configuration file**, where every setting can be done without
  modifying the source code
- Supported architectures are **armhf** (32 bits) and **arm64** (64 bits)
- Analog Devices **libraries can be added individually**, making the image
  completely customizable for each project
- Supports installation of **different versions of boot files** for Xilinx and
  Intel carriers and Raspberry Pi platforms
- Can **configure the image at build time for a specific hardware setup**,
  preparing the image to be transferred on an SD card and booted on a board,
  without the need to manually copy boot files
- Supports running a **custom script** at build time, to cover even more custom
  settings that are not standard in the config file
- Supports **exporting the source files** of all the packages used in the
  Kuiper 2 image at build time

*Stages Anatomy*

The kuiper repository structure includes:

- **ci/** - Support for automatic builds in GitHub Actions
- **docs/** - Support for GitHub Documentation
- **stages/** - Build stages organized in numbered directories:

  - 01.bootstrap
  - 02.set-locale-and-timezone
  - 03.system-tweaks
  - 04.configure-desktop-env
  - 05.adi-tools
  - 06.boot-partition
  - 07.extra-tweaks
  - 08.export-stage

- **build-docker.sh** - Shell script used to automate the process of preparing
  the Docker environment
- **config** - Set of variables that control tool installation
- **kuiper-stages.sh** - Shell script used to build the Kuiper 2 image

The stages approach adds logical clarity, modularity, simplifies maintenance
and simplifies customization.

*Build Flow*

The build process follows this flow:

1. Source files are stored on GitHub
2. Pull requests and pushes trigger GitHub Actions
3. The build starts and runs through each stage (stage 1 through stage 8)
4. The config file provides settings to the stages directory
5. Docker is used to execute the build
6. The ADI Package Repository is used during the build
7. The resulting ADI-KUIPER-LINUX image is exported
8. ADI boot files (from Jenkins/Azure Pipelines) are added to complete the image

*Configuration File*

The configuration file controls various aspects of the build:

- **Target architecture** - armhf or arm64
- **Debian version** - The base Debian release
- **Boot files** - Release version or source of installation (SW Downloads or
  ADI repository)
- **ADI library or tool** - cmake arguments (if the case), github branch or tag
- **Extra script** - Custom scripts to run during build
- **Export sources** - Whether to export package sources
- **Prepare boot files in the boot partition** - board and carrier settings

*Supported Versions*

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Version
     - Variable in config file
     - Stage/substage
   * - Basic image
     - No variable
     - 01.bootstrap, 02.set-locale-and-timezone, 03.system-tweaks,
       05.adi-tools/14.write-git-logs, 06.boot-partition,
       08.export-stage/01.extend-rootfs, 08.export-stage/03.generate-license,
       08.export-stage/04.export-image
   * - With desktop environment
     - CONFIG_DESKTOP
     - 04.configure-desktop-env
   * - With ADI tool
     - CONFIG_[ADI tool], CONFIG_[ADI tool]_CMAKE_ARGS, BRANCH_[ADI tool]
     - 05.adi-tools/xx.install-[ADI tool]
   * - With exported sources
     - EXPORT_SOURCES
     - 08.export-stage/02.export-sources
   * - With custom script
     - EXTRA_SCRIPT
     - 07.extra-tweaks/01.extra-scripts
   * - With boot partition ready for a specific hardware setup
     - ADI_EVAL_BOARD, CARRIER
     - 08.export-stage/04.export-image

*Extra Scripts*

Kuiper allows you to run additional scripts during the build process to
customize the resulting image. This feature enables advanced customization
beyond the standard configuration options.

To use extra scripts:

1. **Add the script** - Place your script file inside the kuiper/stages
   directory
2. **Make it executable** - Make sure your script is executable:
   ``chmod +x your-script.sh``
3. **Add the path** - Set EXTRA_SCRIPT in the config file to your script's
   path, relative to kuiper directory

Hands-on activity
-----------------

By the end of this workshop, you will learn:

* How to build a custom Kuiper 2 image using kuiper
* How to prepare SD cards for different carrier boards
* How to explore IIO devices and connect to target boards
* How to build and load kernel modules
* How to use GNU Radio with Jupiter SDR
* How to monitor temperature sensors locally and remotely using libiio

Pre-requisites
~~~~~~~~~~~~~~

**Common Linux commands:**

* **cd**: used to change the current working directory in Linux and other
  Unix-like operating systems
* **ls**: lists files and directories within the file system, and shows
  detailed information about them
* **cat**: displays the contents of one or multiple text files
* **echo**: prints out its arguments as standard output; use ``>`` or ``>>``
  with the *echo* command to print the output to a file instead of displaying
  it in the terminal
* **mv**: moves a file from one location to another, rename a file with or
  without moving it

Workshop Preparation
~~~~~~~~~~~~~~~~~~~~

This workshop requires four SD cards with pre-configured Kuiper images:

- One for the **Raspberry Pi 5** (development workstation)
- One for the **CoraZ7S** (target board)
- One for the **Jupiter SDR** (target board)
- One for the **Raspberry Pi 4** (target board)

Preparing the Raspberry Pi 5 SD Card
++++++++++++++++++++++++++++++++++++

1. Download the `Raspberry Pi 5 Kuiper image
   <https://swdownloads.analog.com/cse/kuiper/kuiperv2.0.0/FTC25/ftc25_pi5_image.zip>`__.

2. Unzip the downloaded file to extract the image.

3. Write the image to an SD card by following the
   :external+kuiper:ref:`Writing the Image to an SD Card
   <use-kuiper-image>` guide.

Preparing the CoraZ7S SD Card
+++++++++++++++++++++++++++++

1. Download the `CoraZ7S Kuiper image
   <https://swdownloads.analog.com/cse/kuiper/kuiperv2.0.0/FTC25/ftc25_cora_image.zip>`__.

2. Unzip the downloaded file to extract the image.

3. Write the image to an SD card by following the
   :external+kuiper:ref:`Writing the Image to an SD Card
   <use-kuiper-image>` guide.

Preparing the Jupiter SD Card
+++++++++++++++++++++++++++++

1. Download the `Jupiter Kuiper image
   <https://swdownloads.analog.com/cse/kuiper/kuiperv2.0.0/FTC25/ftc25_jupiter_image.zip>`__.

2. Unzip the downloaded file to extract the image.

3. Write the image to an SD card by following the
   :external+kuiper:ref:`Writing the Image to an SD Card
   <use-kuiper-image>` guide.

Preparing the Raspberry Pi 4 SD Card
++++++++++++++++++++++++++++++++++++

1. Download the `Raspberry Pi 4 Kuiper image
   <https://swdownloads.analog.com/cse/kuiper/kuiperv2.0.0/FTC25/ftc25_pi4_image.zip>`__.

2. Unzip the downloaded file to extract the image.

3. Write the image to an SD card by following the
   :external+kuiper:ref:`Writing the Image to an SD Card
   <use-kuiper-image>` guide.

----

Make sure the Raspberry Pi 5 in front of you is booted and is connected to the
monitor, mouse, keyboard and WiFi.

The booklet and the .ppt presentation can also be found in the Kuiper image on
Raspberry Pi 5 on the desktop named "booklet.pdf" and "powerpoint.pdf".

.. note::

   Before disconnecting a board from the power cable, run the following command
   in the terminal connected to that image:

   .. code-block:: bash

      sudo poweroff

Build a Custom Kuiper 2 Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this exercise you will learn how to build a Kuiper 2 image that runs a
custom script.

1. Open a terminal, clone the kuiper repository, move inside it and
   start Visual Studio Code:

   .. code-block:: bash

      git clone https://github.com/analogdevicesinc/kuiper
      cd kuiper
      code .

2. Modify the *config* file in the project as follows:

   .. list-table:: Config file modifications
      :header-rows: 1
      :widths: 20 40 40

      * - Line in config
        - Old string
        - Modified string
      * - Line 8
        - TARGET_ARCHITECTURE=armhf
        - TARGET_ARCHITECTURE=arm64
      * - Line 23
        - CONFIG_DESKTOP=n
        - CONFIG_DESKTOP=y
      * - Line 30
        - CONFIG_LIBIIO=n
        - CONFIG_LIBIIO=y
      * - Line 226
        - EXTRA_SCRIPT=
        - EXTRA_SCRIPT=stages/07.extra-tweaks/01.extra-scripts/examples/extra-script-example.sh

   Make sure you saved the file.

3. Create a new file at the location
   *stages/07.extra-tweaks/01.extra-scripts/examples/* named *custom-file.txt*
   and write to it "Hello FTC25" (or anything you want). You can do that by
   right-clicking on *examples* folder and pressing *Add new file*.

4. Open the file *extra-script-example.sh* from location
   *stages/07.extra-tweaks/01.extra-scripts/examples/* and add the following
   line at the end of the file:

   .. code-block:: bash

      cp stages/07.extra-tweaks/01.extra-scripts/examples/custom-file.txt /home/analog

   Make sure to save the files. You can close now Visual Studio Code.

5. In the terminal you have opened start the build by running:

   .. code-block:: bash

      sudo bash build-docker.sh

   Password: *analog*

   **Congratulations! You started your first Kuiper 2 custom build!**

   **Do not close the terminal until the build is finished. For any other
   command you will need to open a new terminal.**

CoraZ7S Exercises
~~~~~~~~~~~~~~~~~

For this workshop you will get: a CoraZ7S board, an ethernet cable, a USB
cable, and an ADXL355 pmod.

Prepare SD card
+++++++++++++++

The first thing you must do is prepare the SD Card with CoraZ7s boot files.

1. Make sure the adapter is connected through USB to the workstation (RPi5).

2. Insert the SD Card you received with the CoraZ7s board into the SD slot on
   the adapter.

3. Run the following command to see the storage devices connected to the
   workstation (typically /dev/sda):

   .. code-block:: bash

      lsblk

   Identify the SD card (verify its size and mountpoint).

4. Run the following command to list the available project boot files on the
   SD Card.

   .. code-block:: bash

      sudo configure-setup.sh -b /media/root/BOOT --help

   Make sure you see the adxl355/coraz7s pair among the eval_board/carrier
   pairs. If missing, it's possible you somehow got a wrong SD card.

   Now let's run the script to prepare the boot files for our CoraZ7s carrier.

   .. code-block:: bash

      sudo configure-setup.sh -b /media/root/BOOT adxl355 coraz7s

   If successful you should see the following:

   .. code-block:: text

      '/media/analog/BOOT/zynq-common/uImage' -> '/media/analog/BOOT/uImage'
      '/media/analog/BOOT/ zynq-coraz7s-adxl355/BOOT.BIN' -> '/media/analog/BOOT/BOOT.BIN'
      '/media/analog/BOOT/ zynq-coraz7s-adxl355/devicetree.dtb' -> '/media/analog/BOOT/devicetree.dtb'
      '/media/analog/BOOT/ zynq-coraz7s-adxl355//uEnv.txt' -> '/media/analog/BOOT/uEnv.txt'
      Successfully prepared boot partition for running project adxl355 on coraz7s.

5. **SAFELY** unmount the SD card partitions (BOOT and rootfs) by right
   clicking each one and selecting unmount. The password is *analog*.

6. Extract the SD Card from the adapter.

Now the SD Card is prepared for CoraZ7s!

Hardware Setup
++++++++++++++

1. Insert the SD card prepared in the SD port of CoraZ7s.

2. Connect the ADXL355 to the JA port of the CoraZ7s.

3. Connect the UART port of the CoraZ7s to a USB port of your Raspberry Pi 5
   using the USB cable received.

4. Connect the Ethernet port of the CoraZ7s to the Ethernet port of your
   Raspberry Pi 5.

By now, your CoraZ7s board should be up and running. It may take a few seconds
for it to boot.

Exercise 1: CoraZ7s Environment Exploration
+++++++++++++++++++++++++++++++++++++++++++

1. On your Raspberry Pi 5, search for *Terminal* and open it.

2. Write the following command to discover the available IIO devices:

   .. code-block:: bash

      iio_info -s

   Look for the IP address correspondent to *ftc25-cora* machine. You will need
   it for the next steps. To find it easier you can search by the hostname of
   the carrier:

   .. code-block:: bash

      iio_info -s | grep ftc25-cora

   The output should look like this:

   .. code-block:: text

      0: 169.254.35.68 (xadc) [ip:ftc25-cora.local]

3. Write the following command to connect via ssh to the CoraZ7s (replace the
   IP address in the command with the address of your board):

   .. code-block:: bash

      ssh -X analog@169.254.35.68

   The password is *analog*.

   At this point you should see this in your terminal:

   .. code-block:: text

      analog@ftc25-pi5:~$ ssh root@169.254.35.68
      root@169.254.35.68's password:
      Linux analog 6.1.70-35308-ge2e62cc28c80 #1525 SMP Fri Aug 15 07:04:44 EEST 2025
      armhf

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Fri Oct 24 19:11:04 2025 from 169.254.35.68
      root@ftc25-cora:~#

   You are now connected to the CoraZ7s. Every command you run from this point
   forward will be executed on the CoraZ7s, not your workstation.

Exercise 2: Build a kernel object for ADXL355 driver
++++++++++++++++++++++++++++++++++++++++++++++++++++

This exercise will demonstrate how to create a kernel object for an existing
driver and load it in such a way that the system recognizes it as part of the
kernel. By running the command *iio_info* in the terminal you will see in the
output that there is no *adxl355* device found.

1. Move to the ftc25-cora folder:

   .. code-block:: bash

      cd ftc25-cora

2. Create a Makefile:

   .. code-block:: bash

      sudo touch Makefile

3. Open the Makefile with a file editor of your choice (nano, Vim, Code):

   .. code-block:: bash

      sudo nano Makefile

4. Write to the Makefile the following lines and then save and exit the file
   with CTRL+S, then CTRL+X:

   .. code-block:: makefile

      obj-m := adxl355_spi.o

      all:
      	make -C /usr/src/linux-headers-6.1.0/ M=$(shell pwd) modules

      clean:
      	make -C /usr/src/linux-headers-6.1.0/ M=$(shell pwd) modules

   Make sure to keep the indentation (use tabs, not spaces).

5. Run *make* to build the kernel object:

   .. code-block:: bash

      sudo make

6. Load the new kernel object:

   .. code-block:: bash

      sudo insmod adxl355_spi.ko

7. Check again with *iio_info* to see readings from the accelerometer.

   .. code-block:: bash

      iio_info

Exercise 3: Play a Snake game with the accelerometer
++++++++++++++++++++++++++++++++++++++++++++++++++++

Using the accelerometer module, you will have the chance to play a little oldie
but goldie SNAKE game.

1. Run the game controls in the background:

   .. code-block:: bash

      python3 game.py &

2. Start the Snake game:

   .. code-block:: bash

      /usr/games/nsnake

Move the accelerometer board around and observe the output. Be careful not to
disconnect the wires. Have fun!

Extra: Control a LED (Optional)
+++++++++++++++++++++++++++++++

Turn on an LED and make it blink with a heartbeat rhythm.

1. Switch to *root* user for this exercise:

   .. code-block:: bash

      su

   Password: *analog*

2. Move to the LEDs directory using the command below:

   .. code-block:: bash

      cd /sys/class/leds

3. Here you can see 6 directories corresponding to the 3 colors of each RGB
   LED on the board:

   .. code-block:: bash

      ls

   Each one of them contains the following attributes:

   .. list-table:: LED attributes
      :header-rows: 1
      :widths: 30 70

      * - Attribute
        - Description
      * - brightness
        - stores the status of the LED; possible values: 0, 1
      * - trigger
        - changes the status of the LED
      * - max_brightness
        - indicates the max brightness value that can be written to brightness
          attribute
      * - device
        - a symbolic link pointing to the parent device of the LED

   The important features of the *trigger* function are:

   .. list-table:: Trigger options
      :header-rows: 1
      :widths: 20 80

      * - Trigger
        - Description
      * - none
        - the default state where no specific trigger is set for the LED
      * - timer
        - this trigger causes the LED to blink at a specified rate set in
          *delay_on* and *delay_off* attributes
      * - oneshot
        - turns the LED on for a short period and then turns it off; the period
          is set in *oneshot*
      * - heartbeat
        - causes the LED to blink in a pattern that mimics a heartbeat
      * - cpu
        - links the LED activity to CPU activity

   The *delay_on* and *delay_off* attributes are active when the timer features
   is enabled, and it will appear in the LED folder.

4. Turn on the RED color of the first LED by setting the corresponding
   *brightness* to 1:

   .. code-block:: bash

      echo 1 >> led0_red/brightness

5. Make the red color of the first led blink in heartbeat mode:

   .. code-block:: bash

      echo heartbeat >> led0_red/trigger

6. Now run a script that executes a series of commands that change the LEDs
   colors:

   .. code-block:: bash

      leds.sh

**After you finish the exercises on CoraZ7s, please make sure to run "sudo
poweroff" in the terminal connected to the target board.**

Jupiter SDR Exercises
~~~~~~~~~~~~~~~~~~~~~

You received a Jupiter board with an SD Card, a power cable, one loopback cable
and 2 antennas.

Prepare SD card
+++++++++++++++

The first thing you must do is prepare the SD Card with Jupiter SDR boot files.

1. Make sure the adapter is connected through USB to the workstation (RPi5).

2. Insert the SD Card you received with the Jupiter SDR board into the SD slot
   on the adapter.

3. Run the following command to see the storage devices connected to the
   workstation (typically /dev/sda):

   .. code-block:: bash

      lsblk

   Identify the SD card (verify its size and mountpoint).

4. Run the following command to list the available project boot files on the
   SD Card.

   .. code-block:: bash

      sudo configure-setup.sh -b /media/root/BOOT --help

   Make sure you see the jupiter_srd/jupiter_sdr pair among the
   eval_board/carrier pairs. If missing, it's possible you somehow got a wrong
   SD card.

   Now let's run the script to prepare the boot files for our Jupiter SDR
   carrier.

   .. code-block:: bash

      sudo configure-setup.sh -b /media/root/BOOT jupiter_sdr jupiter_sdr

   If successful you should see the following:

   .. code-block:: text

      '/media/analog/BOOT/zynqmp-common/Image' -> '/media/analog/BOOT/Image'
      '/media/analog/BOOT/zynqmp-jupiter-sdr/BOOT.BIN' -> '/media/analog/BOOT/BOOT.BIN'
      '/media/analog/BOOT/zynqmp-jupiter-sdr/boot.scr' -> '/media/analog/BOOT/boot.scr'
      '/media/analog/BOOT/zynqmp-jupiter-sdr/system.dtb' -> '/media/analog/BOOT/system.dtb'
      '/media/analog/BOOT/zynqmp-common/uEnv.txt' -> '/media/analog/BOOT/uEnv.txt'
      Successfully prepared boot partition for running project jupiter_sdr on jupiter_sdr.

5. **SAFELY** unmount the SD card partitions (BOOT and rootfs) by right
   clicking each one and selecting unmount. The password is *analog*.

6. Extract the SD Card from the adapter.

Now the SD Card is prepared for Jupiter SDR!

Hardware Setup
++++++++++++++

1. Insert the SD card prepared in the SD port of Jupiter SDR.

2. Connect the Ethernet port of the Jupiter SDR to the Ethernet port of your
   Raspberry Pi 5.

3. Connect the loopback cable to the Jupiter SDR to A TX1 and A RX1.

4. Connect the power cable you received to the power port of the Jupiter SDR.

5. Make sure to press the power button.

By now, your Jupiter SDR board should be up and running. It may take a few
seconds for it to boot.

Exercise 1: Jupiter SDR Environment Exploration
+++++++++++++++++++++++++++++++++++++++++++++++

1. On your Raspberry Pi 5, search for *Terminal* and open it.

2. Write the following command to discover the available IIO devices:

   .. code-block:: bash

      iio_info -s

   Look for the IP address correspondent to *ftc25-jupiter* machine. You will
   need it for the next steps. To find it easier you can search by the hostname
   of the carrier:

   .. code-block:: bash

      iio_info -s | grep ftc25-jupiter

   The output should look like this:

   .. code-block:: text

      0: 169.254.35.68
      (ltc2945,tps6598x_source_psy_0_0038,tps6598x_source_psy_0_003f,xilinx-ams,adrv9002-
      phy,axi-adrv9002-rx-lpc,axi-adrv9002-rx2-lpc,axi-adrv9002-tx-lpc,axi-adrv9002-tx2-
      lpc) [ip:ftc25-jupiter.local]

3. Connect to the Jupiter SDR board as the **root** user using one of the
   following commands. Make sure to replace the IP address with the actual
   address of the board.

   .. code-block:: bash

      ssh root@169.254.35.68

   The password is *analog*.

   At this point you should see something like this in your terminal:

   .. code-block:: text

      analog@ftc25-pi5:~$ ssh root@169.254.35.68
      root@169.254.35.68's password:
      Linux analog 6.1.70-35308-ge2e62cc28c80 #1525 SMP Fri Aug 15 07:04:44 EEST 2025
      aarch64

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      Last login: Fri Oct 24 19:11:04 2025 from 169.254.35.68
      root@ftc25-jupiter:~#

   You are now connected to Jupiter SDR. Every command you run from this point
   forward will be executed on the Jupiter SDR, not your workstation.

Exercise 2: Jupiter Configuration
+++++++++++++++++++++++++++++++++

1. You should be connected as the **root** user to Jupiter by the end of the
   previous exercise.

2. Write the Jupiter profile to configure the driver used to control the board
   to prepare for the following exercises:

   .. code-block:: bash

      cat /home/analog/ftc25-jupiter/jupiter_1_92MHz_profile.json > /sys/bus/iio/devices/iio:device1/profile_config

Now you have the hardware and driver parts ready for the GNU Radio exercises!

Exercise 3: Loopback Complex Sinewave
+++++++++++++++++++++++++++++++++++++

1. Open GNU Radio Companion, the application used for the following exercises.
   Go to Applications > Development > GNU Radio Companion.

2. Open the exercise_3.grc file from */home/analog/ftc25-pi5/jupiter* folder.

3. Double-click on the Variable Config block and fill the placeholder IP
   variable with the actual IP address of the Jupiter board. If you forgot it,
   you could simply use the ``iio_info -s`` command again.

4. Click the play button. It may take a few seconds for the visualization to
   open.

5. You should see the transmitted samples and received samples visualization,
   along with the transmitted spectrum and received spectrum.

Congrats! You have a loopback transmission of a complex sinewave using your
Jupiter board.

**Bonus:** You can try setting different frequencies using the slider at the
top.

Extra: Doppler Effect (Optional)
++++++++++++++++++++++++++++++++

Connect the antennas to the Jupiter SDR to A TX1 and A RX1 (replacing the
loopback cable).

1. Open the *extra.grc* file from *ftc25-pi5/jupiter* folder on desktop and
   fill in the board IP address. This is very similar to what was done in the
   previous exercise.

2. Press play and have fun with the Doppler effect visualization.

**After you finish the exercises on Jupiter SDR, please make sure to run "sudo
poweroff" in the terminal connected to the target board.**

Raspberry Pi 4 Exercises
~~~~~~~~~~~~~~~~~~~~~~~~

You received a Raspberry Pi 4 board, an SD Card and a power cable.

For this exercise, there is no need to configure the boot files for the board,
since Kuiper runs on Raspberry Pi boards by default.

Prepare SD Card
+++++++++++++++

No SD card preparation is needed for Raspberry Pi 4.

Hardware Setup
++++++++++++++

1. Make sure the Raspberry Pi 4 has an SD card in the SD port.

2. Connect the power cable you received to the power port of the Raspberry Pi 4.

3. Connect the ethernet cable you received to the ethernet port of the
   Raspberry Pi 4.

By now, your Raspberry Pi 4 board should be up and running. It may take a few
seconds for it to boot.

Exercise 1: Raspberry Pi 4 Environment Exploration
++++++++++++++++++++++++++++++++++++++++++++++++++

1. On your Raspberry Pi 5, search for *Terminal* and open it.

2. Write the following command to discover the available IIO devices:

   .. code-block:: bash

      iio_info -s

   Look for the IP address correspondent to *ftc25-pi4* machine. You will need
   it for the next steps. To find it more easily you can search by the hostname
   of the carrier:

   .. code-block:: bash

      iio_info -s | grep ftc25-pi4

   The output should look like this:

   .. code-block:: text

      0: 169.254.35.68 (cpu_termal,rpi_volt) [ip:ftc25-pi4.local]

   Make sure you remember the IP address corresponding to the Raspberry Pi 4
   board.

Exercise 2: Monitor Workstation Temperature
+++++++++++++++++++++++++++++++++++++++++++

1. Start the temperature monitoring python script:

   .. code-block:: bash

      python3 ftc25-pi5/pi4/monitor_temperature.py

   You should see now a thermometer that monitors the internal temperature of
   your RPi5 Workstation. Take your time to understand what is being displayed.

2. Open a new terminal instance like you did in the first step of Exercise 1.

3. In this new terminal use the following script to stress the CPU of the RPi5
   and raise its temperature:

   .. code-block:: bash

      python3 ftc25-pi5/pi4/stress.py

   This script will stop by itself when a critical (>80 degrees Celsius)
   temperature is reached.

4. Go back to the initial terminal where the monitor_temperature.py script and
   observe the effect.

5. Press CTRL+C to stop the monitoring application.

Exercise 3: Monitor Remotely RPi4 Temperature
+++++++++++++++++++++++++++++++++++++++++++++

1. Using one of the active terminals, open the monitor_temperature.py script
   in VS Code:

   .. code-block:: bash

      code ftc25-pi5/pi4/monitor_temperature.py

2. Search for the following section:

   .. code-block:: python

      #===================================================================
      # EXERCISE: Change this ONE line for remote monitoring!
      #===================================================================
      # For LOCAL monitoring (RPi5 monitors itself):
      #     ctx = iio.Context()
      #
      # For REMOTE monitoring (RPi5 monitors RPi4 at 169.254.35.68):
      #     ctx = iio.Context("ip:169.254.35.68")
      #===================================================================

      # Change the line below
      ctx = iio.Context()

      #===================================================================

   Right now, the highlighted line of code uses the default local context,
   meaning the temperature sensor it monitors is the one on your Raspberry Pi 5
   Workstation.

3. Replace ``ctx = iio.Context()`` with the following, making sure you use the
   actual IP address of your Raspberry Pi 4 target board, the one you
   discovered in Exercise 1. If you forgot it you can simply use the
   ``iio_info -s`` command once again.

   .. code-block:: python

      ctx = iio.Context("ip:169.254.35.68")

4. Make sure you save the file and then close the VS Code editor.

5. In one of the active terminals start the monitoring script once again:

   .. code-block:: bash

      python3 ftc25-pi5/pi4/monitor_temperature.py

   Now the digital thermometer is monitoring remotely the temperature sensor on
   Raspberry Pi 4.

6. Press CTRL+C to stop the monitoring application.

Extra: Optional Challenge
+++++++++++++++++++++++++

1. Using one of the active terminals, start the monitor_temperature.py script:

   .. code-block:: bash

      python3 ftc25-pi5/pi4/monitor_temperature.py

   Let it run.

2. Using another terminal, copy the stress.py script to RPi4 using scp. Make
   sure you replace the IP address below with the actual IP address of the
   target board.

   .. code-block:: bash

      scp ftc25-pi5/pi4/stress.py analog@169.254.35.68:/home/analog

3. Connect to the target board using ssh. Don't forget to replace the IP
   address.

   .. code-block:: bash

      ssh analog@169.254.35.68

4. Start the stress script on the target board:

   .. code-block:: bash

      python3 stress.py

5. Observe the effects on the digital thermometer running in the first
   terminal.

6. Press CTRL+C to stop the monitoring application.

**After you finish the exercises on Raspberry Pi 4, please make sure to run
"sudo poweroff" in a terminal connected to the target board.**

Raspberry Pi 5 Networking Exercise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this exercise you will communicate with other participants via a
lightweight publish/subscribe protocol called MQTT.

1. Open a terminal and run the following command to listen to a port where all
   participants will write messages:

   .. code-block:: bash

      mosquitto_sub -h test.mosquitto.org -t "ftc25-kuiper"

2. Open a new terminal and write the following command to send messages to the
   port everyone listens to:

   .. code-block:: bash

      mosquitto_pub -h test.mosquitto.org -t "ftc25-kuiper" -m "Hello from Pi $HOSTNAME"

Boot your Custom Kuiper 2 Image on RPi5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this exercise you will write on an SD card the Kuiper 2 image you just built
and will boot it on the Raspberry Pi 5 in front of you.

1. Power-off the carrier board in front of you (CoraZ7s, Raspberry Pi 4 or
   Jupiter SDR), take the SD card from it and connect it to the Raspberry Pi 5.

2. Open a terminal in kuiper/kuiper-volume folder, unarchive and copy
   the Kuiper image on the SD card. Use lsblk command to check the partition.
   As you saw earlier, the SD card from the adapter is mounted at SDA.

   .. code-block:: bash

      lsblk
      sudo unzip image_2025-11-10-ADI-Kuiper-Linux-arm64.zip
      sudo dd if=image_2025-11-10-ADI-Kuiper-Linux-arm64.img of=/dev/sda bs=1M status=progress conv=fsync

3. After the image is copied successfully, **SAFELY** unmount the SD card
   partitions (BOOT and rootfs) by right clicking each one and selecting
   unmount. The password is *analog*.

4. Extract the recently written SD card from the adapter.

5. Power off the Raspberry Pi 5 and disconnect it from the power cable, take
   out the SD card from it and replace it with the recently written card, and
   then connect back the Pi board to power.

6. Look after the file you copied with the extra script and check what it
   contains.

**Congratulations! You booted your first Kuiper 2 custom image!**

Takeaways
---------

* **ADI Kuiper Linux simplifies embedded development**: The distribution
  provides pre-built boot files, device drivers, and development utilities for
  Analog Devices products.

* **Kuiper 2 is highly customizable**: The configuration file allows you to
  control every aspect of the build without modifying source code, from
  architecture selection to custom scripts.

* **Stages-based build system**: The modular stages approach adds logical
  clarity and simplifies both maintenance and customization.

* **IIO enables seamless device communication**: Using libiio and tools like
  iio_info, you can discover and interact with ADI devices both locally and
  remotely over the network.

* **Support for multiple platforms**: Kuiper supports Xilinx/AMD FPGAs, Intel
  FPGAs, and Raspberry Pi boards, making it versatile for various evaluation
  and development scenarios.

* **Open source advantage**: With BSD-3-Clause licensing, ADI Kuiper Linux
  code can be freely used, modified, and integrated into projects.

Resources
---------

**Kuiper**

:external+kuiper:doc:`index`

:git-kuiper:`kuiper Repository </>`

**Hardware**

`Digilent Cora Z7 Reference Manual <https://digilent.com/reference/programmable-logic/cora-z7/reference-manual>`_

:adi:`Jupiter SDR Product Page <AD-JUPITER-EBZ>`

:adi:`EVAL-ADXL355-PMDZ Product Page <EVAL-ADXL355-PMDZ>`

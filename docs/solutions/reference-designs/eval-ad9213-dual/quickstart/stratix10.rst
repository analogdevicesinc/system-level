.. _eval-ad9213-dual quickstart stratix10:

Intel Stratix 10 SX Quick start
===============================================================================

.. figure:: ../images/stratix10_board.jpeg
   :alt: Stratix 10 SX SoC board
   :width: 800

   Stratix 10 SX SoC board

.. esd-warning::

This guide provides instructions on how to bring up the :adi:`AD9213-DUAL-EBZ`
on  in Synchronized 10G Mode or Interleaved 20G Mode to enable data capture and
visualization in :ref:`iio-oscilloscope` and 
:adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`.
The AD9213 Manual Calibration and Interleaving Guide provides extra detail.

Required equipment and hardware
-------------------------------------------------------------------------------

- :adi:`AD9213-DUAL-EBZ Evaluation Board`
- `Intel Stratix 10 SX SoC Development Kit <https://docs.altera.com/r/docs/683303/current/stratix-10-sx-soc-development-kit-user-guide/overview>`__
- RF Power Splitter for splitting the test tone to apply two equal signals
  to each of the two ADCs
- Phase matched coaxial cables to connect the power splitter to the ADC
  input board connectors
- RF Balun for single-ended-to-differential conversion of the 500 MHz
  reference clock
- Coax cables for the 500 MHz reference clock connections
- Signal generators:

  - Analog signal source: frequency and power requirements depend on the
    tests to be performed; a bandpass filter is often used for single tone
    tests
  - 500 MHz Reference Clock source: should have very low phase noise and be
    capable of supplying a 5 dBm, 500 MHz clock signal

- PC running Windows with at least 2 USB ports and an Ethernet port, with:

  - One mini-USB cable
  - One micro-USB cable
  - One Ethernet cable

Helpful documents
-------------------------------------------------------------------------------

- :adi:`AD9213 Datasheet <en/products/ad9213.html>`
- `Intel Stratix 10 SX SoC Development Kit User Guide <https://docs.altera.com/r/docs/683303/current/stratix-10-sx-soc-development-kit-user-guide/overview>`_

Required software
-------------------------------------------------------------------------------

- :intel:`Intel Quartus Prime Programmer 19.3 <content/www/us/en/software-kit/661657/intel-quartus-prime-pro-edition-design-software-version-19-3-for-windows.html>`
- :ref:`iio-oscilloscope`
- :adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`

  - VisualAnalog Canvas for AD9213-DUAL-EBZ (supplied by ADI)
  - :git-libiio:`/` (for IIO Client block in provided VisualAnalog Canvas)
  - :dokuwiki:`IIO Plugin for VisualAnalog <_media/resources/tools-software/linux-software/libiio/clients/va_iiopluginsetup.zip>`

ADI software deliverables
-------------------------------------------------------------------------------

- :dokuwiki:`Dual-AD9213-EBZ <_media/resources/eval/dual_ad9213_ebz.zip>`

The link above contains the following:

- FPGA binary for the Stratix 10 SX SoC
- SD Card images containing IIO libraries and a system initialization
  sequence
- Example scripts for Synchronization and Interleaving
- PDF Documents: Software License, Quickstart Guide, Manual Calibration
  Guide
- VisualAnalog (software from analog.com) Canvases for viewing FFTs
- Serial terminal of your choice to connect to the board via UART

Setup and connection
-------------------------------------------------------------------------------

Perform all connections with power and signal generators OFF, connecting the
boards as shown in the typical setup figure above.

.. figure:: ../images/ad9213_dualbrd_plus_stratix10_image_two_power_adapters.jpeg
   :alt: Image of Intel Stratix 10 SX SoC board with AD9213-DUAL-EBZ
         connected via FMC+
   :align: center

   AD9213-DUAL-EBZ and Intel Stratix 10 SX Board - Setup

.. figure:: ../images/ad9213_dualbrd_plus_stratix10_diagram_two_power_adapters.jpeg
   :alt: Diagram of Intel Stratix 10 SX SoC board with AD9213-DUAL-EBZ
         connected via FMC+
   :align: center

   AD9213-DUAL-EBZ and Intel Stratix 10 SX Board - Typical Setup

Board switch configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the switches on the Stratix 10 SX SoC FPGA board as follows:

.. figure:: ../images/stratix10_board_switches.jpeg
    :alt: Switches on the Stratix 10 SX SoC board

    Switches on the Stratix 10 SX SoC board  

**SW1**

.. list-table::
   :header-rows: 1

   * - S10
     - M10B
     - FMCA
     - FMCB
     - PCIE
     - MSTR0
     - MSTR1
     - MSTR2
   * - OFF
     - ON
     - ON
     - ON
     - ON
     - ON
     - ON
     - ON

**SW2 - MSEL**

Configure SW2 according to the desired boot mode:

.. list-table::
   :header-rows: 1

   * - Switch Bit
     - 1 (MSEL0)
     - 2 (MSEL1)
     - 3 (MSEL2)
     - 4 (Not Used)
   * - JTAG Mode
     - ON
     - ON
     - ON
     - OFF
   * - QSPI Mode
     - ON
     - OFF
     - OFF
     - OFF

**SW3 - USR_DIPSW_FPGA**

.. list-table::
   :header-rows: 1

   * - PIN1
     - PIN2
     - PIN3
     - PIN4
   * - OFF
     - OFF
     - OFF
     - OFF

**SW4**

.. list-table::
   :header-rows: 1

   * - I2C FLAG
     - DC_POWER CTRL
     - FACTORY LOAD
     - SECURITY MODE
   * - ON
     - OFF
     - OFF
     - ON

SD card preparation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the ADI Linux Image (``image_2021-07-28-ADI-Kuiper-full.zip``)
   available under :git-kuiper:`releases+`.
#. Program a blank SD card (at least 16 GB) with the downloaded image using
   the instructions in :external+kuiper:ref:`use-kuiper-image`.

   .. note::

      Once the image is programmed, eject the SD card and re-insert it. The
      SD card will already include a few folders in its BOOT partition; those
      can be ignored for this setup.

#. For the SD card to boot correctly, place the
   ``socfpga_stratix10_socdk.dtb`` and the ``u-boot.itb`` files provided in
   the SD card folder into the top-level directory (``BOOT D:``). In
   addition to this, also place one of the ``Image`` files based on use
   case:

   - From the **Dual 10G Image** folder - for Synchronized 10G Mode
   - From the **Single 20G Image** folder - for Interleaved 20G Mode

#. Replace the SD card on the Stratix 10 SX SoC board with the SD card you
   just programmed.

Power-up and signal generators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power up the boards and configure the signal generators:

- Start with low test signal power (about 0 dBm); this can be adjusted
  later as desired.
- For the reference clock signal, set the generator power to 5 dBm.

UART connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the Micro-USB port of the Stratix 10 SX SoC board to the host PC.
Use a serial terminal application of choice (PuTTY, Tera Term, etc) to open
the corresponding COM port with the following settings: **115200 baud, 8N1**.

Programming the board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Start Quartus Prime Programmer 19.3. The software should auto-detect the
   Stratix 10H SoC Evaluation Board in the **Hardware Setup** section at
   the top. If it does not appear automatically, select it manually.

#. Once the board has been detected, click **Add File**.

   .. figure:: ../images/ad9213dual_quickstart_fig5_quartus_setup.jpeg
      :alt: Quartus Prime Programmer Hardware Setup dialog showing the
            detected Stratix 10 board
      :width: 600

      Setting up the Quartus Programmer to program the FPGA image

#. Navigate to the location of the ADI-provided FPGA program
   (``ad9213_dual_ebz_s10soc_hps_20_4.sof``), select the file, and click
   **Open**.

   .. note::

      It will take a few seconds for the file to be added and the FPGA
      device to appear on screen.

#. Click **Start** and wait for the programmer to complete.

   .. note::

      Programming the FPGA also triggers the Linux boot on the HPS. The
      COM console provides updates on the progress of the boot.

   .. figure:: ../images/ad9213dual_quickstart_fig6_using_quartus_programmer.jpeg
      :alt: Quartus Prime Programmer showing programming progress for the
            AD9213-DUAL-EBZ FPGA image
      :width: 600

      Using the Quartus Programmer to program the FPGA image

#. The COM console will display a verbose running of the
   initialization scripts, at the end of which the setup will be ready.

   .. figure:: ../images/ad9213dual_quickstart_fig7_com_console_process_initialization.jpeg
      :alt: COM console showing the completed boot process and
            initialization output
      :width: 600

      COM console once the boot process and initialization are
      complete

#. Obtain the board IP address by running ``ifconfig`` in the console.

   .. figure:: ../images/ad9213dual_quickstart_fig8_using_ifconfig_for_stratix10_ip_address.jpeg
      :alt: COM console showing ifconfig output with the Stratix 10 board
            Ethernet IP address
      :width: 600

      Using ifconfig to obtain the IP address of the Stratix 10
      SX SoC board Ethernet connection

SSH connection (Interleaved 20G Mode only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Interleaved 20G Mode, open an SSH connection to the board to run SPI
scripts. Use your terminal application with the following settings:

- **Connection Type**: SSH
- **Host Name**: IP address of the Stratix 10 board, obtained in the
  previous step
- **Port**: ``22``

.. figure:: ../images/ad9213dual_quickstart_fig9_opening_ssh_connection.jpeg
   :alt: Configuration dialog with SSH connection settings for the
         Stratix 10 SX SoC board
   :width: 600

   Opening an SSH connection to the Stratix 10 SX SoC board

Login credentials:

- **Login**: ``root``
- **Password**: ``analog``

.. figure:: ../images/ad9213dual_quickstart_fig10_ssh_login_successful.jpeg
   :alt: SSH session after login showing access to board components
         via SPI
   :width: 600

   Connection after login ready to access the components on
   the board via SPI

An example script for SPI reads and writes can be provided on request.

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Go to the **Connect** tab, select **Manual**, enter the IP address of
   the board prefaced by ``ip:`` in the URL input box, and click
   **Refresh**.

   .. figure:: ../images/ad9213dual_quickstart_fig11_setup_iio_scope.jpeg
      :alt: IIO Oscilloscope connection dialog with manual IP entry
      :width: 600

      Setting up a connection to IIO Oscilloscope

#. Once you click Refresh, all the IIO devices on the AD9213-DUAL-EBZ —
   including the two AD9213s and the other clock chips — will show up.
   Click **Connect**. On subsequent connections with the same setup,
   IIO Oscilloscope will auto-detect the configuration automatically.

   .. figure:: ../images/ad9213dual_quickstart_fig12_iio_ready_to_connect.jpeg
      :alt: IIO Oscilloscope showing all devices on the evaluation board
            ready to connect
      :width: 600

      All devices on the evaluation board ready to connect to
      IIO Oscilloscope

#. After connecting, an SPI Controller window and a Plotting window will
   open.

#. The SPI Controller window allows reading and writing individual registers
   for any device on the board. This is optional — the automatic startup
   configuration has already run on boot.

   .. figure:: ../images/ad9213dual_quickstart_fig13_read_write_spi_registers.jpeg
      :alt: IIO Oscilloscope Controller view showing SPI register read/write
            interface
      :width: 600

      Using the IIO Oscilloscope Controller view to read and
      write SPI

#. Use the Plotting window to capture data from one AD9213 at a time or
   from both simultaneously. The selection of the AD9213 and the number of
   samples can be made using the panels on the left. The tool allows both
   time domain and frequency domain captures.

   .. note::

      In Interleaved 20G Mode, voltage 0 (channel 0) represents data from
      both ``ad9213_0`` and ``ad9213_1`` as a combined waveform or FFT.

   .. figure:: ../images/ad9213dual_quickstart_fig14_plot_separate_domain_outputs.jpeg
      :alt: IIO Oscilloscope Plotting view showing separate time domain
            outputs from each AD9213
      :width: 1000

      Using the IIO Oscilloscope Plotting view to plot separate
      time domain outputs from each AD9213 (Ain = 136 MHz @ 5 dBm)

For more detailed frequency domain analysis, use a VisualAnalog Canvas as
described in the next section.

VisualAnalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One-time IIO installations before running VisualAnalog (only needed if the
ADI-provided VisualAnalog Canvas will be used):

#. Install :git-libiio:`/` (needed to use the IIO Client block in VisualAnalog)
#. Install the :dokuwiki:`IIO Plugin for VisualAnalog <_media/resources/tools-software/linux-software/libiio/clients/va_iiopluginsetup.zip>`

**Synchronized 10G Mode**

#. Go to the **Existing** tab and browse to the location of the
   ``Dual9213_IIOScope_FFT.vac`` canvas. Select the canvas and click
   **Open**.

   .. figure:: ../images/ad9213dual_quickstart_fig15_open_visualanalog_canvas.jpeg
      :alt: VisualAnalog canvas selection dialog for the dual AD9213
            Synchronized 10G Mode
      :width: 600

      Opening the VisualAnalog Canvas to plot FFTs for the dual
      AD9213s (Synchronized 10G Mode)

#. Once the canvas is open, open the settings for the IIO Client module.
   Enter the IP address for the Stratix 10 SX SoC board, the sampling
   frequency, the sample size per AD9213, and enable both AD9213s. Click
   **OK**.

   .. figure:: ../images/ad9213dual_quickstart_fig16_setup_va_for_dualad9213.jpeg
      :alt: VisualAnalog IIO Client module settings for Synchronized 10G
            capture
      :width: 800

      Setting up the VisualAnalog Canvas for capture for the
      dual AD9213s (Synchronized 10G Mode)

#. The canvas is now ready to capture FFTs for each of the AD9213s. Click
   **Play** to capture. In addition to the FFT plot and its analysis, the
   canvas also displays sample data for each AD9213.

   .. figure:: ../images/ad9213dual_quickstart_fig17_va_fft_capture_data_analysis.jpeg
      :alt: VisualAnalog canvas showing FFT capture, analysis, and sample
            data for AD9213_0
      :width: 800

      VisualAnalog canvas FFT capture, analysis and sample data
      for AD9213_0 (150.3 MHz @ 14.90 dBm)

**Interleaved 20G Mode**

#. Go to the **Existing** tab and browse to the location of the
   ``Dual9213_Interleaved20G_FFT.vac`` canvas. Select the canvas and click
   **Open**.
#. Once the canvas is open, open the settings for the IIO Client module.
   Enter the IP address for the Stratix 10 SX SoC board, set the sampling
   frequency to ``20000``, the sample size to ``65536``, and enable the
   datapath (shows up at Channel 0, but contains a sample interleaved
   stream of data from both AD9213s). Click **OK**.

   .. note::

      Before you are ready to capture, the two AD9213s need to be gain and
      timing aligned and the sample clock to one AD9213 needs to be
      inverted with respect to the other.

#. Use the instructions in the AD9213 Manual Calibration and Interleaving
   Guide to run the example scripts in the SSH connection environment you
   opened to the board to align and interleave.
#. The canvas is now ready to capture an FFT. Click **Play** to capture.
#. In addition to the FFT plot and its analysis, the canvas also displays
   sample data.

Building from source
-------------------------------------------------------------------------------

This section describes how to build all software components from source for
the Intel Stratix 10 SX SoC platform.

Get toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and configure the AArch64 cross-compilation toolchain:

.. shell::
   :user: analog

   ~
   $mkdir tools
   $cd tools
   $wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/10.3-2021.07/binrel/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu.tar.xz
   $tar xvf gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu.tar.xz
   $export CROSS_COMPILE=/home/analog/tools/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu-
   $export ARCH=arm64
   $cd ~

Build Linux kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: analog

   ~
   $git clone https://github.com/analogdevicesinc/linux
   $cd linux
   $git checkout altera_adxcvr_master
   $make adi_stratix10_defconfig
   $make Image
   $make altera/socfpga_stratix10_socdk_ad9213_dual.dtb
   $cp arch/arm64/boot/Image /media/analog/BOOT/
   $cp arch/arm64/boot/dts/altera/socfpga_stratix10_socdk_ad9213_dual.dtb \
   $  /media/analog/BOOT/socfpga_stratix10_socdk.dtb
   $cd ~

Build ARM Trusted Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: analog

   ~
   $git clone https://github.com/altera-opensource/arm-trusted-firmware
   $cd arm-trusted-firmware
   $git checkout rel_socfpga_v2.6.0_22.07.02_pr
   $make bl31 PLAT=stratix10 DEPRECATED=1
   $cd ~

Build U-Boot and copy u-boot.itb to SD card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: analog

   ~
   $git clone https://github.com/altera-opensource/u-boot-socfpga
   $cd u-boot-socfpga
   $git checkout rel_socfpga_v2022.01_22.11.02_pr
   $ln -sf ../arm-trusted-firmware/build/stratix10/release/bl31.bin .
   $sed -i \
   $  's/earlycon panic=-1/earlycon panic=-1 console=ttyS0,115200 root=\/dev\/mmcblk0p2 rw rootwait/g' \
   $  configs/socfpga_stratix10_defconfig
   $sed -i '/^CONFIG_NAND_BOOT=y/d' configs/socfpga_stratix10_defconfig
   $sed -i '/^CONFIG_SPL_NAND_SUPPORT=y/d' configs/socfpga_stratix10_defconfig
   $sed -i '/^CONFIG_CMD_UBI=y/d' configs/socfpga_stratix10_defconfig
   $echo 'CONFIG_USE_BOOTCOMMAND=y' >> configs/socfpga_stratix10_defconfig
   $echo 'CONFIG_BOOTCOMMAND="bridge enable 0xf; setenv ethaddr 00:15:17:ab:cd:ef; load mmc 0:1 ${kernel_addr_r} Image; load mmc 0:1 ${fdt_addr_r} socfpga_stratix10_socdk.dtb; booti ${kernel_addr_r} - ${fdt_addr_r}"' \
   $  >> configs/socfpga_stratix10_defconfig
   $make socfpga_stratix10_defconfig
   $sed -i \
   $  '/4GB/,/0x80000000>;/creg = <0 0x00000000 0 0x80000000>;' \
   $  arch/arm/dts/socfpga_stratix10_socdk.dts
   $make
   $cp u-boot.itb /media/analog/BOOT/
   $cd ~

Generate .sof and .jic files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: analog

   ~
   $git clone https://github.com/analogdevicesinc/hdl
   $cd hdl/projects/ad9213_dual_ebz/s10soc
   $make
    Building ad9213_dual_ebz_s10soc [/home/analog/hdl/projects/ad9213_dual_ebz/s10soc/ad9213_dual_ebz_s10soc_quartus.log] ... OK
   $quartus_pfg -c ad9213_dual_ebz_s10soc.sof \
   $  -o hps_path=../../../../u-boot-socfpga/spl/u-boot-spl-dtb.hex \
   $  ad9213_dual_ebz_s10soc_hps.sof
   $quartus_pfg -c ad9213_dual_ebz_s10soc_hps.sof \
   $  ad9213_dual_ebz_s10soc_hps.jic \
   $  -o device=MT25QU02G \
   $  -o flash_loader=1SX280HU2F50E1VGAS

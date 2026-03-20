Frequency Hopping Example Design
================================

This article will explain an example design that utilizes the frequency hopping
features of the AD9361 transceiver through the use of its built-in fastlock
profiles under external pin control. Since this example focuses on features that
are generally used in tightly time-constrained applications, the design will be
done primarily built around logic for the FPGA fabric and software control
interfaces. The following topics will be discussed:

-  AD9361 fastlock for fast frequency hopping
-  Creating a custom reference design for MathWorks HDL Coder
-  Control logic for fastlock
-  IIO driver implementation
-  MATLAB example using the deployed controller and IIO driver

AD9361 Fastlock for Fast Frequency Hopping
------------------------------------------

The AD9361 transceiver has a massive LO tuning range from 70 MHz to 6 GHz in
roughly ~4 Hz steps. Allowing for support of many different applications for the
transceiver. However, move the LO across this range has strict requirements,
specifically for the internal VCXO driving the RX or TX paths. Whenever an LO
change of 100 MHz is required from a calibrated frequency, the VCXO must be
first moved and re-calibrated. This is automatically performed by the driver,
and monitoring the PLL lock settings will show the TX or RX PLL unlocking during
this frequency change and re-calibration phase. During this process, a series of
values are written into the VCXO calibration registers that are unique for that
LO frequency. The during of the re-calibration can vary depending on the divider
ratio used to generate the LO in question. This will normally range from X to Y.
During this phase data receiver or transmitted is invalid, and only will become
valid once the related PLL is locked.

In order to increase this LO transition rate, it is possible to save these
calibrations on-chip for future need LO switches. These extra registers are
called fastlock registers or fastlock profiles, and a maximum of 8 are provided
on-chip. If more are needed, calibration information can be pulled off-chip then
loaded from the baseband processor in the future. When using these fastlock
profiles, a user can simply recall a fastlock profile from the desired register
set and the LO will move to the frequency associated with that profile and the
LO will lock-in with ~15-25us depending on configuration and LO frequency. The
selection of profiles can be done over SPI, or more commonly, over direct
external pins provided at the CTRL_IN interfaces of the transceiver. The pin
control interface will be used in this design since it is the fastest and most
deterministic.

Fastlock Controller IP
----------------------

.. image:: ../images/hoppingdiagram.png
   :align: center
   :width: 800

.. container:: centeralign

   \ *Frequency Hopper Controller Reference Design Interfaces*\

For this design, an HDL Coder workflow will be used to both generate the
additional controlling IP, but also to stitch the generated IP into a custom
reference design. The diagram above outlines the connections of the Hop
Controller which is responsible for selecting specific fastlock profiles, as
well as managing receive DMA to only capture data during the dwell period after
the AD9361 has transitioned between frequencies.

The custom HDL reference design will be adapted from the standard design
provided for the ADRV9361-Z7035 RF-SOM with FMC carrier board. From the original
design, two main changes are made to support this frequency hopping use case.
These changes are:

-  Modify the CTRL_OUT connections in the reference design to allow connection to a custom IP core. By default, the CTRL_OUT pins are connected directly to the Zynq's ARM GPIO controller.
-  Modify the CTRL_IN connections to be exposed as standalone ports, similarly
   to what is done for the CTRL_OUT pins. By default, these pins go directly
   back to the ARM as well.

These are accomplished by modifying two files. The main system wrapper
(system_top.v) to unbundle the desired ports:

::

     output  [ 3:0]  gpio_ctl,
     input   [ 7:0]  gpio_status,

     output          spi_csn,
     output          spi_clk,
     output          spi_mosi,
     input spi_miso);
   ...
     ad_iobuf #(.DATA_WIDTH(2)) i_iobuf_ad9361 (
       .dio_t ({gpio_t[46:45]}),
       .dio_i ({gpio_o[46:45]}),
       .dio_o ({gpio_i[46:45]}),
       .dio_p ({ gpio_resetb,        // 46:46
                      gpio_sync })); // 45:45
   ...
       .up_txnrx (gpio_o[48]),
       .gpio_en_agc (gpio_en_agc),
       .gpio_status (gpio_status),
       .gpio_ctl (gpio_ctl));

and the main Tcl file used to build the project itself (system_bd.tcl):

::

   ad_ip_parameter axi_ad9361 CONFIG.ADC_INIT_DELAY 29

   # Add external pin for EN_AGC
   create_bd_port -dir O gpio_en_agc

   # Add external pins for CTRL_IN
   create_bd_port -from 0 -to 7 -dir I gpio_status

   # Add external pins for CTRL_OUT
   create_bd_port -from 0 -to 3 -dir O gpio_ctl

Back in MATLAB, a new interface definition file set is created. This simply requires modifying the :git-TransceiverToolbox:`trx_examples/targeting/frequency-hopping/%2BAnalogDevicesDemo/%2Badrv9361z7035/%2Bccfmc_lvds_hop/%2Brxtx/add_rx_tx_io.m` file, which is responsible for defining possible interfaces of generated IP. To separate this design as well, separate targets were made for this design with a specific namespace. MATLAB performs namespace separation using plus folders which you will find in the :git-TransceiverToolbox:`trx_examples/targeting/frequency-hopping` folder of the ADI BSP.

::

   tcollins@winston:/tmp/TransceiverToolbox$ ls -A trx_examples/targeting/frequency-hopping/ |grep -v /$
   adi_build.tcl
   +AnalogDevicesDemo                  <--- MATLAB API to reference design
   build_kernel.sh
   ccfmc_lvds_hop                      <--- Verilog and tcl for reference design
   devicetree.dtb
   devicetree.dts
   fastlock.m
   FrequencyHopper.m
   frequency_hopping.slx
   hdlcoder_board_customization.m      <--- Registration for HDL Workflow Advisor
   hdlworkflow.m
   hopper.patch
   hop_result.bmp

Control Logic For Fastlock
--------------------------

The Hop Controller has two main modes, hop enabled and hop disabled. In the hop
disabled mode, the controller will use the current index last provided by the
internal state machine. If the HOPPER_MANUAL_PROFILE_ENABLE register is set, the
profile used will be based on the HOPPER_MANUAL_PROFILE register.

In hopping mode, when the HOPPER_MANUAL_PROFILE_ENABLE register is not set, the
controller will rotate through profiles 0-7 in order. When 7 is reached the
internal counter rolls back to start at 0 again. It will remain at the profile
for 20+N samples where N is the value provided in the HOPPER_DWELL_SAMPLES
register.

Register map:

+------------------------------+----------+---------+------------------------------------------------------------------------------------------+
| Name                         | Register | Range   | Purpose                                                                                  |
+==============================+==========+=========+==========================================================================================+
| HOPPER_DWELL_SAMPLES         | 0x100    | 32 bits | Number of samples to remain a profile index when HOPPER_ENABLE_HOPPING is set            |
+------------------------------+----------+---------+------------------------------------------------------------------------------------------+
| HOPPER_ENABLE_HOPPING        | 0x104    | 1 bit   | Enables automatic profile rotation                                                       |
+------------------------------+----------+---------+------------------------------------------------------------------------------------------+
| HOPPER_FORCE_OUT_ENABLE      | 0x108    | 1 bit   | Latches DMA enables high when set                                                        |
+------------------------------+----------+---------+------------------------------------------------------------------------------------------+
| HOPPER_MANUAL_PROFILE        | 0x120    | 3 bit   | Index of profile to select. Only applicable when HOPPER_MANUAL_PROFILE_ENABLE is set     |
+------------------------------+----------+---------+------------------------------------------------------------------------------------------+
| HOPPER_MANUAL_PROFILE_ENABLE | 0x124    | 1 bit   | Select profile index based on HOPPER_MANUAL_PROFILE instead of internal controller state |
+------------------------------+----------+---------+------------------------------------------------------------------------------------------+

Fastlock Controller IIO Driver
------------------------------

To provide configuration to the Hop Controller IP an IIO driver was implemented, which must be built into the Linux kernel on the target platform. The source of this driver is provided as a :git-TransceiverToolbox:`patch <trx_examples/targeting/frequency-hopping/hopper.patch>` to the ADI kernel. The Hop Controller IIO driver is a platform driver and can currently only be instantiated via devicetree.

Required devicetree properties:

-  compatible: Should always be “adi,axi-hopper-1.00”
-  reg: Base address and register area size. This parameter expects a register
   range.

Example

::

   axi-hopper@43c00000 {
           compatible = "adi,axi-hopper-1.00";
           reg = <0x43c00000 0xffff>;
   };

Device Attributes
~~~~~~~~~~~~~~~~~

Each and every IIO device, typically a hardware chip, has a device folder under
/sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under
every one of these directory folders reside a set of files, depending on the
characteristics and features of the hardware device in question. These files are
consistently generalized and documented in the IIO ABI documentation. In order
to determine which IIO deviceX corresponds to which hardware device, the user
can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the
sequence in which the iio device drivers are loaded/registered is constant, the
numbering is constant and may be known in advance.

::

   root@analog:/sys/bus/iio/devices/iio:device5# ls -l
   total 0
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 dev
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 dwell_samples
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 forced_enable
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 hopping_enable
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 manual_profile_enable
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 manual_profile_indx
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 name
   lrwxrwxrwx 1 root root    0 Jan  1 00:03 of_node -> ../../../../../firmware/devicetree/base/fpga-axi@0/axi-hopper@43c00000
   drwxrwxrwx 2 root root    0 Jan  1 00:00 power
   lrwxrwxrwx 1 root root    0 Jan  1 00:03 subsystem -> ../../../../../bus/iio
   -rw-rw-rw- 1 root root 4096 Jan  1 00:00 uevent

Using the IIO tools we can see the **axi-hopper** device in the IIO device list.

::

   root@analog:~# iio_attr -a -d
   Using auto-detected IIO context at URI "local:"
   IIO context has 7 devices:
       iio:device3: ad9517-3, found 0 device attributes
       iio:device1: ad9361-phy, found 18 device attributes
       iio:device6: cf-ad9361-lpc, found 0 device attributes
       iio:device4: cf-ad9361-dds-core-lpc, found 0 device attributes
       iio:device2: xadc, found 1 device attributes
       iio:device0: ad7291, found 0 device attributes
       iio:device5: axi-hopper, found 5 device attributes

MATLAB Example
--------------

Since there is an IIO driver for the Hop Controller it can be controlled remotely from MATLAB. A system object called :git-TransceiverToolbox:`FrequencyHopper <trx_examples/targeting/frequency-hopping/FrequencyHopper.m>` was created using the IIO binding provided in the `ADI BSP <https://wiki.analog.com/resources/eval/user-guides/matlab_bsp>`_ to access the IIO driver. The :git-TransceiverToolbox:`example <trx_examples/targeting/frequency-hopping/fastlock.m>` provided in the BSP will load profiles for 8 LO frequencies 1 MHz apart so they the receiver can view the entire hopping range. Next, the Hop Controller is configured and hopping is initiated. The script will show a frequency versus time plot similar to below.

.. image:: ../images/hop_result.png
   :align: center
   :width: 600

Running the Demo
~~~~~~~~~~~~~~~~

.. tip::

   \ `Demo Video <https://vimeo.com/337844457>`_\

Requirements:

-  `Analog Devices Transceiver Toolbox <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
-  Xilinx Vivado
-  :adi:`ADRV9361-Z7035 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV9361-Z7035.html>` with :adi:`FMC Carrier <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html#eb-overview>`

To build and run the demo:

-  Create a `standard ADI SD card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_ (Release 2018_R1+ depending on MATLAB version)
-  Build the BOOT.BIN for the design from MATLAB using the provided :git-TransceiverToolbox:`hdlworkflow <trx_examples/targeting/frequency-hopping/hdlworkflow.m>` script. This is provided with the Transceiver Toolbox install and can be accessed by running in the MATLAB command prompt: ``a=which('frequency-hopping/hdlworkflow.m');cd(a(1:end-13))``
-  Build the kernel with the necessary driver patch. A :git-TransceiverToolbox:`script <trx_examples/targeting/frequency-hopping/build_kernel.sh>` is provided to accomplish this patched build. Note that this will require a Linux machine or VM since building kernels is not practical on Windows.
-  Place the generate BOOT.BIN, uImage, and provided :git-TransceiverToolbox:`trx_examples/targeting/frequency-hopping/devicetree.dtb` onto the BOOT partition of the SD card.

Now the ADRV9361-Z7035 can be booted from the built SD card, the :git-TransceiverToolbox:`trx_examples/targeting/frequency-hopping/fastlock.m` example can be run from MATLAB. Note you may need to update the URI at the top of the example to reflect the IP address of your ADRV9361-Z7035.

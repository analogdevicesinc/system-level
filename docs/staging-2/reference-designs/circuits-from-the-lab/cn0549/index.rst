.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0549

.. _circuits-from-the-lab cn0549:

CN0549 User Guide
=================

CbM requires capturing full bandwidth data to ensure that all harmonics,
aliasing, and other mechanical interactions in both the time and frequency
domain are accounted for. This data collection requires a high performance
sensor and data acquisition (DAQ) system that can provide high fidelity,
real-time data into a data analysis tool or application.

Using established tools like MATLAB® or newer Python-based tools like
Tensorflow, analyzing the data, profiling the machinery, and creating algorithms
for smart decision making is greatly simplified.

Vibration sensing has traditionally dominated most CbM applications because of
the availability of sensors, and the science behind the analysis is better
understood. The integrated electronic piezoelectric (IEPE) standard is a popular
signaling interface standard for high end microelectronic mechanical systems
(MEMS) and piezo sensors that are prevalent in the industry today.

:adi:`CN0549` helps to address these gaps by providing a complete system from
sensor to algorithm development.

Required Materials
------------------

Hardware:

#. :adi:`EVAL-CN0532-EBZ <en/design-center/reference-designs/circuits-from-the-lab/CN0532.html>`
#. :adi:`EVAL-CN0540-ARDZ <en/design-center/reference-designs/circuits-from-the-lab/CN0540.html>`
#. :adi:`EVAL-XLMOUNT1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-xlmount1.html>`
#. Cabling the CN0532 to the CN0540

   #. :digikey:`1m Shielded male to male SMA cable <135101-02-M1.00>` or
   #. Twisted pair set of wires cut to the desired length

#. `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__
#. `Class 10 16GB SD Card <https://www.amazon.com/gp/product/B073K14CVB/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1>`__
#. `USB OTG <https://www.amazon.com/Rankie-Female-Adapter-Convertor-3-Pack/dp/B00YOX4JU6/ref=sr_1_19?dchild=1&keywords=usb+otg+adapter&qid=1590089326&sr=8-19>`__
   (micro USB to USB Type A female USB 2.0 Compatible)
#. Wireless Keyboard and mouse with USB Dongle
#. Male to male HDMI Cable

.. note::

   This page will focus on using the DE10-Nano board, but it is also possible to
   create the CN0549 setup connected to a CoraZ7-07s FPGA platform. For more
   information on how to use the CoraZ7-07s platform please
   :dokuwiki:`click here </resources/eval/user-guides/circuits-from-the-lab/cn0540/coraz7s>`.

Software:

#. `ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/cn0540.tar.gz>`__

Setting up and Configuring the SD Card
--------------------------------------

To prepare the SD-card for the DE10-Nano board:

- `ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/cn0540.tar.gz>`__
- Validate, Format, and Flash the SD Card
- :dokuwiki:` Format and flash the SD Card using Windows </resources/tools-software/linux-software/zynq_images/windows_hosts>`
- :dokuwiki:` Format and flash the SD Card using Linux </resources/tools-software/linux-software/zynq_images/linux_hosts>`

Putting together the CN0549
---------------------------

#. Take out the CN0532 sensor from its packaging, it will look like this.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0532_hw.jpg
      :width: 400px

#. Cut the end of an SMA cable at one end, and solder the center tap to the ACC
   pad and the outside shield to the GND pad.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0532_soldered2.jpg
      :width: 400px

#. Using the EVAL-XLMOUNT1, mount the CN0532 to the side of the cube using the
   screws provided. It doesn"t matter which side you mount, because you will
   likely need to change the orientation at the customer.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0532_xlmount1_attached.jpg
      :width: 400px

#. Take out the DE10-Nano, it will look like this.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/de10-nano_hw.jpg
      :width: 400px

#. Make sure that the FPGA Configuration Mode Switch is set at the following
   positions.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/de10-nano_fpga_switch_matrix.png
      :width: 400px

#. Insert the programmed micro SD Card into the slot provided on the bottom of
   the DE10-Nano board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/de10-nano_sdcard_insert.jpg
      :width: 400px

#. Make sure you push the SD card all the way into the slot, as its spring
   loaded and isn"t inserted until it clicks all the way in.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/de10-nano_sdcard_connected.jpg
      :width: 400px

#. Take of the CN0540 data acquisition(DAQ) board, it will look like this.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0540_hw.jpg
      :width: 400px

#. Orient the CN0540 DAQ board so that the SMA connector is on the same end as
   the Ethernet jack of the DE10-Nano.

#. Find the Arduino header pins on the CN0540 and line them up with the mating
   Arduino connectors found on the DE10-Nano.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0540_de10_angled_lineup.jpg
      :width: 400px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0540_de10_stacked_lineup.jpg
      :width: 400px

#. Once both rows of pins are lined up, push the CN0540 DAQ board down into the
   DE10-Nano so that the boards fit snuggly together.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/cn0540_de10_stacked.jpg
      :width: 400px

    Note, the CN0540 will make solid contact with the DE10-Nano even with the
    plexiglass installed, so there is no need to remove that before connecting
    the two boards together.

#. Connect the SMA cable from the CN0532 sensor board to the SMA connector on
   the CN0540 DAQ board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_sma_insert.jpg
      :width: 400px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_sma_connected.jpg
      :width: 325px

#. Next its time to connect the peripherals up to the DE10-Nano

#. Connect up the USB On the GO(OTG) cable using the micro USB port on the
   DE10-Nano.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_otg_connected.jpg
      :width: 400px

#. Place the wireless keyboard/mouse dongle into the end of the USB OTG cable.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_otg_connected_dongle.jpg
      :width: 400px

#. Place one end of the HDMI cable into the HDMI connector on the DE10-Nano.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_hdmi_insert.jpg
      :width: 400px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_hdmi_connected.jpg
      :width: 400px

#. Connect the 5V power supply to the power jack provided on the DE10-Nano.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_power_insert.jpg
      :width: 330px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0549/daq_power_connected.jpg
      :width: 400px

Booting
-------

Now that you have everything plugged into the DE10-Nano and the CN0540 boards,
its time to boot the system.

.. important::

   Make sure that your HDMI cable is connected into your HDMI monitor before
   applying power to the DE10-Nano board

#. Plug the DC power supply into your power outlet.
#. You"ll notice that the several LEDs turn on, and after about 5-10 seconds the
   ``User LED`` on the DE10-Nano near the Ethernet jack will turn on (it should
   be solid orange).
#. This indicates that software image has booted up properly.
#. You should see the ADI Kuiper Linux image home screen up on your HDMI
   monitor, after the DE10-Nano has booted
#. Use your USB wireless mouse, move to the ``start button`` on the home screen,
   navigate down to ``Other``.
#. Find and open the IIO-Oscilloscope application.
#. You will be prompted for a password, type in **analog** and press <Enter>

Using the System with IIO Oscilloscope
--------------------------------------

Now its time to start communicating with the CN0540 so you can start streaming
data. When you first open IIO-Oscilloscope you"ll see two windows.

#. CN0540 Plugin / DMM / DEBUG Window
#. IIO Capture Window

CN0540 IIO-Oscilloscope Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CN0540 IIO Plugin automatically configures the CN0540, so it is ready to use
as soon as you run the application. Calibration of the sensor is also
automatically performed so that a user can start using the capture window to
collect and analyze data. No other configuration is required for the
application.

If you want to re-calibrate the system, shut the system down, or modify
individual registers of the devices on the CN0540 that can also be done either
using the CN0540 Plugin or using the DEBUG panel to write/read specific
registers. This is optional and typically application specific.

Below is a picture of what the CN0540 IIO Plugin looks like.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_cn0540_plugin_controls.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_cn0540_plugin_block_diagram.png
   :width: 400px

User interface
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Section
     - User Control
     - Description
     - Value
   * - Power Control
     - SW_FF
     - Checks the current status of the ADG5421"s FF Pin
     - Low(normal)
       High(over voltage)
   * -
     - Shutdown
     - Shutdowns power from the AD7768-1
     - Disabled(Power On)
       Enabled(Power down)
   * - ADC Driver Settings
     - FDA Status
     - ADA4945 Operational Status
     - Checked(Enable)
       Un-Checked(Disabled)
   * -
     - FDA Mode
     - ADA4945 Power Mode
     - Checked(Full Power)
       Un-Checked(Low Power)
   * - Sensor Calibrations
     - Calibration Result
     - The Calibration is set for a 10V calibration
     - 10.0V
   * -
     - Input Voltage(mV)
     - Calibrated AD7768-1 Input voltage offset
     - ~ 0.0V
   * -
     - Shift Voltage(mV)
     - Calibrated LTC2606 Level Shifting Voltage
     - ~ 0.0V
   * -
     - Sensor Voltage(mV)
     - Calibrated Sensor Input voltage
     - ~ 10.0V
   * - Voltage Monitor
     - Vin+ (mV)
     - Input voltage coming from the sensor
     -
   * -
     - Vgpoi2 (mV)
     - Not Used
     - N/A
   * -
     - Vgpoi3 (mV)
     - Not Used
     - N/A
   * -
     - Vcom (mV)
     - ADA4945 Common Mode input voltage
     - ~2.5 V
   * -
     - Vfda+ (mV)
     - AD7768-1 Ain+ input voltage
     -
   * -
     - Vfda- (mV)
     - AD7768-1 Ain- input voltage
     -

IIO Capture Window
~~~~~~~~~~~~~~~~~~

For CbM applications, most customers are typically interested in the frequency
domain plots. To obtain a FFT plot, do the following:

#. Use the drop down menu labeled ``Plot Type`` and select ``Frequency Domain``.
#. Set the number of samples to 16384
#. Set the averaging to 3

You should see a nice plot like this when connected to the CN0532 sensor.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_capture_cn0532.png
   :width: 500px

Additional Information and Useful Links
---------------------------------------

- :adi:`CN0532 Circuit Note Page <CN0532>`
- :adi:`CN0532 Design Support Package <CN0532-DesignSupport>`
- :adi:`CN0540 Circuit Note Page <CN0540>`
- :adi:`CN0540 Design Support Package <CN0540-DesignSupport>`
- :adi:`EVAL-XLMOUNT1 Mounting Block <EVAL-XLMOUNT1>`

Reference Demos & Software Examples
-----------------------------------

Data Science Examples
~~~~~~~~~~~~~~~~~~~~~

- :dokuwiki:`Streaming CbM Data directly into MATLAB </resources/eval/user-guides/circuits-from-the-lab/cn0549/matlab_example>`
- :dokuwiki:`Streaming CbM Data directly into Python Tools </resources/eval/user-guides/circuits-from-the-lab/cn0549/python_example>`

Alternate Data Acquisition Setups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :dokuwiki:`Using the CN0540 with the CoraZ7-07s </resources/eval/user-guides/circuits-from-the-lab/cn0540/coraz7s>`
- :dokuwiki:`Using the CN0540 with a networked DE10-Nano </resources/eval/user-guides/circuits-from-the-lab/cn0540/de10-nano>`

Standalone Demo Kit
~~~~~~~~~~~~~~~~~~~

- :dokuwiki:`Building a CN0549 Pelican Kit </resources/eval/user-guides/circuits-from-the-lab/cn0549/pelican_kit>`



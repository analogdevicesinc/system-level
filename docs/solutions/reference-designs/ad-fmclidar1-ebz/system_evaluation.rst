Setting up the system
================================================================================

.. warning::

   Support for the ad_fmclidar_ebz is discontinued on all supported carriers:
   Arria10 SOC, ZC706 and ZCU102. ad_fmclidar_ebz will not be supported in
   future releases, last release image in which pre-build files can be found is
   2021_r1. (check the
   :external+kuiper:doc:`Kuiper <index>`
   to see all available Kuiper Linux releases).

.. image:: images/lidar_system_1.jpg
   :alt: Complete system assembled including additional optics and FPGA board
   :width: 400

To get the system up and running follow the steps below:

- Connect the DAQ board to the FMC HPC connector on the FPGA carrier board
- Connect the ribbon cables between the DAQ board and the Laser and AFE boards.
  The DAQ board has labels on the silkscreen next to the AFE and Laser board
  connectors indicating which board these correspond to
- Connect the SMA cables between the DAQ and the AFE board. It is recommended
  to match the TIA outputs with the ADC inputs using the labeling on the SMA
  connectors so that they have the same letter (A, B, C, D). Make sure that the
  P (positive) and N (negative) are matched between the boards.
- It is is also possible to use one of the ADC channels to sample the laser
  dive signal by connecting the SMA outputs of the Laser board to one of the
  ADC channels

.. image:: images/lidar_lens.jpg
   :alt: Lens mount
   :align: right
   :width: 100

- Insert the lens into the 1.5" lens tube (the longer one) with the spherical
  surface pointing outwards. The tube comes with a retaining ring that is used
  to set the position of the lens inside the tube. Position the lens such that
  top of the spherical surface is aligned with the edge of the tube. Use the
  retaining ring provided in the box to lock the lens in place.
- It is recommended to use the 1" tube provided in the box to limit the field
  of view of the system by screwing it on the 1.5" tube in front of the lens.
- Connect the external 12V power supply that comes with the kit to the Laser
  board
- The SD card that comes with the kit contains the Linux files for multiple
  projects. Before it can be used all the files from the
  BOOT/zynq-zc706-adv7511-fmclidar1 must be copied onto the root of the SD
  card
- Plug the SD card that comes with the kit in the FPGA carrier board
- Connect to the FPGA board a HDMI monitor and a USB keyboard and mouse
- Power up the FPGA board
- After the FPGA board boots power the laser board by pressing the S1 switch
- After the FPGA boots the
  :ref:`IIO Oscilloscope <iio-oscilloscope>`
  will start allowing to configure the system, capture and visualize data from
  it

.. note::

   - See the :external+kuiper:doc:`Kuiper Linux instructions <index>` on how to
     burn the Linux image on the SD card. This might be useful if the SD card is
     corrupted or a new image needs to be written to the SD card.
   - The SD card in the box might not have the latest software release. It is
     recommended to update the software when using the system for the first time
     by following the
     :external+kuiper:doc:`Kuiper Linux instructions <index>`
   - To prevent the SD from getting corrupted at system power down it is
     recommended to run this command to safely power down the system:
     *sudo shutdown -h now*

Running the evaluation software
================================================================================

The IIO Oscilloscope enables viewing the raw data acquired on all the ADC
channels as well as controlling some hardware settings through the LIDAR plugin.
It uses the
:ref:`libiio library <libiio>`
to talk to the system and the functionality of the controls in the LIDAR plugin
is implemented by reading and writing different attributes of the Linux drivers
in the system. The source code of the plugin, showing how to access the
available attributes, can be found
:git-iio-oscilloscope:`here <plugins/lidar.c>`.

IIO Oscilloscope data capture window
--------------------------------------------------------------------------------

.. image:: images/liadr_iio_scope_plot.png
   :alt: LIDAR IIO Oscilloscope
   :align: right
   :width: 400

The main window of the IIO Osciloscope allows setting the length of the data
captures and selecting the ADC channels that will be displayed on the plot. The
length of the data capture must be always set to a multiple of 256 to match the
internal data bus length, otherwise the plot will either hang or display
incorrect data.

There are 5 channels under the axi-ad9094-hpc device, 4 of them (voltage0 to
voltage3) corresponding to the physical data channels of the AD9094 and the 5th
one (voltage4) showing the mux selections of the 4 TIAs on the AFE board. The
mux selections channel is encoded on 8 bits with 2 bits for each TIA showing the
actual bit values for the CHSEL0 and CHSEL1 TIA inputs. This channel is always
selected. If it's interfering with the display of the other data channels it can
always be multiplied with 0 using the Math function of the IIO oscilloscope.

.. image:: images/lidar_voltage4_format.png
   :width: 400

IIO Oscilloscope LIDAR plugin
--------------------------------------------------------------------------------

.. image:: images/liadr_iio_scope_plugin.png
   :align: right
   :width: 350

Sequencer Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A TIA channel sequencer implemented in the LIDAR HDL design that controls the
mux selection independently for all the TIAs. The sequencer's operation can be
controller from the LIDAR plugin using the options in the *Sequencer Settings*
section. The sequencer can run in **auto** mode, meaning that it will change the
mux selection at every data capture based on the sequence specified in the
*Auto Config* section, which defines what the mux selection is for all the TIAs
for 4 consecutive data captures. The length of the data capture is specified in
the IIO Oscilloscope main window and a data capture is always triggered by the
start of a laser pulse so that the start of the data is aligned with the
transmitted laser pulse, which is time 0 for time of flight measurement.

In **manual** mode the 4 *Manual Channel* controls correspond to the 4 TIAs on
the AFE board, starting with U2 on the left and continuing with U3, U4, U5 to
the right. The values are in the range 0:3 and control the setting of the CHSEL0
and CHSEL1 pins of the TIAs.

The *Pulse delay* setting controls the delay between the time the TIA channel is
changed a new laser pulse is generated. This delay is required to account for
the time needed by the TIA to settle after the channel change.

Laser Pulse Generator Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HDL design contains a pulse generator that precisely controls the timing of
the laser pulses. The generator must be enabled before the data capture is
started because the captures are triggered by the laser pulses. There are 2
parameters that can be controlled for the laser pulses - the frequency and the
width, which actually define the total optical power of the system.

.. important::

   The system was certified for Eye Safety Class 1 with 20ns pulse width and
   50KHz laser settings. When operating the system above these settings eye
   safety class 1 is no longer guaranteed and laser safety glasses (e.g
   `LG2 laser safety glasses <https://www.thorlabs.com/thorproduct.cfm?partnumber=LG2>`_)
   must be worn all the time. It is recommended to wear laser safety glasses all
   the time irrespective of the laser setting to avoid any dangerous situations
   that might arise when modifying the software.

AFE Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The APD on the AFE board needs a negative bias voltage in the range 120V to 200V
to work. This determines the sensitivity of the APD and is set through the
*APD Bias* control.

The TIA output signal has an offset that can be compensated via the *Tilt*
control. This helps bring the signal close to 0 and maximize the ADC range.

.. note::

   See the :doc:`AFE board wiki page <hardware_afe>` for a complete description
   of the signal chain.

Monitoring the status of the JESD Link
--------------------------------------------------------------------------------

At system startup, besides the IIO Oscilloscope, the
:ref:`JESD 204B Eye Scan <software jesd-eye-scan>`
app starts to allow monitoring the status of the JESD204B link to the AD9094 on
the DAQ board.

Make some actual distance measurements
================================================================================

:git-pyadi-iio:`examples/lidar.py` is a standalone GUI application developed on
top of Analog Devices'
:git-pyadi-iio:`pyadi-iio library </>`.

Besides displaying the received signals, lidar.py can be used configure all the
relevant board parameters, including the Pulse Width, APD Bias, Tilt Voltage,
Sequencer Settings and the parameters used to generate the reference signal.
This reference signal is then used to approximate and display the distance to
the first object the LIDAR laser is pointed at. All these parameters, signals
and measurements are displayed and can be configured in real time.

.. image:: images/lidarpy_gui_screenshot.png

For the distance measurement, a correlation method is used. The LIDAR board has
a reference signal which can be connected to one of the output channels, but
this example does not use that approach. Instead, we try to approximate this
reference signal by taking a single square pulse signal with the width equal to
the pulse width specified in the Laser Settings of the GUI section. A FIR filter
is then applied to this square pulse signal to obtain a reference signal
approximation, which is plotted along with the received signals. The Filter
Length and the Filter Cutoff Frequency can be modified in real time via the
GUI's interface to improve the accuracy of the measurement. Modifying the Filter
Length, while potentially improving the correlation method accuracy, will also
shift the generated signal, so the Distance Offset will also have to be manually
adjusted. You can play with all these parameters and see what works best for
you.

Each displayed distance measurement is a mean value of the last 10 measurements
to smooth out the variations in the received signals as much as possible. Each
change to the GUI parameters only takes effect after Config Board is pressed. A
snapshot of all the current received signals can be saved in a CSV file format.

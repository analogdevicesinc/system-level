.. _pluto users quick_start:

PlutoSDR Quick Start
====================

Most people don't read instructions, and just want get things going. This is
the minimum to get things going, and a few common trouble shooting tips along
the way.

1. Install the drivers
----------------------

Install the drivers for your operating system:

* :ref:`Windows <pluto-m2k drivers windows>`
* :ref:`Linux <pluto-m2k drivers linux>`
* :ref:`MAC <pluto-m2k drivers osx>`

2. Plug the device in to USB, and check things are working
-----------------------------------------------------------

After installing the drivers for your platform, plug in the ADALM-PLUTO via
USB and verify that it's working properly. Follow the platform-specific
verification steps from the driver installation pages above.

3. Install Scopy for your host
-------------------------------

Download and install :external+scopy:doc:`Scopy <index>`
for your host.

4. IIO Oscilloscope vs Scopy 2.0
----------------------------------

:external+scopy:doc:`Scopy 2.0 <index>` is the modern
replacement for the legacy
:dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`
application. Both tools provide similar functionality for configuring and
testing PlutoSDR, but Scopy 2.0 offers a more polished interface and
additional features.

AD936X plugin comparison
~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO:: verify this intersphinx target against the live scopy inventory

The :external+scopy:doc:`AD936X plugin <plugins/ad936x/ad936x>`
in both tools allows you to configure the transceiver's receive and transmit
chains. Scopy 2.0 provides a cleaner layout with the same controls.

.. list-table::
   :widths: 50 50

   * - **IIO Oscilloscope**
     - **Scopy 2.0**
   * - .. image:: images/iio_vs_scopy/iio_osc_ad936x_plugin.png
          :width: 22em
     - .. image:: images/iio_vs_scopy/scopy_ad936x_plugin.png
          :width: 22em

Register map comparison
~~~~~~~~~~~~~~~~~~~~~~~

Both tools provide access to the device register map for advanced debugging.
Scopy 2.0 offers a more comprehensive view with register descriptions and
bit-level details.

.. list-table::
   :widths: 50 50

   * - **IIO Oscilloscope**
     - **Scopy 2.0**
   * - .. image:: images/iio_vs_scopy/iio_osc_reg_map.png
          :width: 22em
     - .. image:: images/iio_vs_scopy/scopy_reg_map.png
          :width: 22em

5. Testing PlutoSDR with Scopy 2.0
-----------------------------------

This section walks you through a basic loopback test to verify your PlutoSDR
is working correctly using Scopy 2.0.

Open Scopy
~~~~~~~~~~

Launch Scopy on your host. If your PlutoSDR is connected via USB, it should
appear automatically as an AD936X device.

.. figure:: images/quick_start_pluto/open_scopy.png
   :width: 45em

Connect to the device
~~~~~~~~~~~~~~~~~~~~~

Click the **+** button to add a new device. In the IIO tab, enter
``ip:pluto.local`` in the URI field and click **Verify** to connect.

.. figure:: images/quick_start_pluto/connect_device_to_scopy.png
   :width: 45em

Configure the transceiver
~~~~~~~~~~~~~~~~~~~~~~~~~

Once connected, open the **AD936X** plugin. Here you can configure the receive
and transmit chain parameters including RF bandwidth, sampling rate, LO
frequency, and gain settings.

.. figure:: images/quick_start_pluto/modify_frequency_val_scopy.png
   :width: 45em

Set up the DAC for signal generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the **DAC** section. Set the MODE to **DDS** and configure TX1 to
use **One CW Tone**. Set the desired frequency, scale (amplitude in dB), and
phase for your test tone.

.. figure:: images/quick_start_pluto/dds_mode_scopy.png
   :width: 45em

View the signal in the time domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **ADC - Time** to view the captured signal in the time domain. Click
**Start** to begin acquisition. You should see a sine wave corresponding to
your DDS tone.

.. figure:: images/quick_start_pluto/adc_time_scopy.png
   :width: 45em

View the signal in the frequency domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **ADC - Frequency** to view the FFT of the captured signal. You should
see a clear peak at your configured DDS frequency.

.. figure:: images/quick_start_pluto/adc_frequency_scopy.png
   :width: 45em

Enable markers for analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable **MARKER** in the right panel to identify peak frequencies and their
power levels. The markers will display frequency and amplitude information
at the bottom of the screen.

.. figure:: images/quick_start_pluto/enable_markers_scopy.png
   :width: 45em

Use Genalyzer for detailed analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable **Genalyzer analysis** in the right panel to compute detailed signal
quality metrics including SNR, SINAD, SFDR, and other parameters.

.. figure:: images/quick_start_pluto/genalyzer_scopy.png
   :width: 45em

Experiment with TX attenuation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return to the **AD936X** plugin and adjust the TX attenuation to see how it
affects the received signal level. The images below show the TX attenuation
control and the resulting change in signal amplitude.

.. figure:: images/quick_start_pluto/tx_attenuation_scopy.png
   :width: 45em

.. figure:: images/quick_start_pluto/tx_att_db_scopy.png
   :width: 15em

6. Connect to your favorite SDR framework, and do interesting things
---------------------------------------------------------------------

Connect the ADALM-PLUTO to your preferred SDR framework:

* :mw:`MATLAB and Simulink <hardware-support/adalm-pluto-radio.html>`
* :ref:`GNU Radio <software gnuradio>`
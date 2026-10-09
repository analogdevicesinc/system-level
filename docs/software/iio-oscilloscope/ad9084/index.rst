.. _ad9084 iio-oscilloscope:

AD9084
======

Capture Window
--------------

Main receivers are handled by the axi-ad9081-rx-hpc IIO device,
The number of channels depend on the JESD mode (M) parameter and
can vary from case to case. When using complex IQ,
two channels index by _i and _q from a receiver.

Screenshots
+++++++++++

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: ad9084_osc_time.png

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: ad9084_osc_fft.png

.. image:: ad9084_osc_tone_fft.png

.. _ad9084 iio-oscilloscope-plugin:

Plugin
------

The AD9084 plugin works with the IIO Oscilloscope. You should always use the
latest version if possible. Changing any field will immediately write changes
which have been made to the AD9084 settings to the hardware, and then read it
back to make sure the setting is valid. If you want to set something that the GUI
changes to a different number, that either means that GUI is rounding (sorry),
or the hardware (either the AD9084 or the FPGA fabric) does not support
that mode/precision.

If you want to play with /sys/bus/iio/devices/…. and manipulate the devices behind
the back of the GUI, it's still possible to see the settings by clicking the
Reload Settings button at the bottom of the GUI.

The AD9084 view is divided in three sections:

  - Receive Chain
  - Transmit Chain
  - FPGA Settings

.. image:: ad9084_osc_plugin.png

Receive Chain
+++++++++++++

.. image:: ad9084_osc_plugin_rx.png

- ADC Rate(MHz): Displays the ADC Sample Rate. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#adc_rate>`
- ADC Nyquist Zone Control: Selects the Nyquist Zone. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#adc_nyquist_zone_control>`
- RX Main NCO Frequency Control: Controls the Main NCO. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#main_data_path>`
- RX Main NCO Phase Control: Controls the Main NCO Phase. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#main_data_path1>`
- RX Channel NCO Frequency Control: Controls the Channel NCO Frequency. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#channel_data_path>`
- RX Channel NCO Phase Control: Controls the Channel NCO Phase. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#channel_data_path1>`

Transmit Chain
++++++++++++++

.. image:: ad9084_osc_plugin_tx.png

- DAC Rate(MHz): Displays the DAC Sample Rate. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#dac_rate>`
- TX Main NCO Frequency Control: Controls the Main NCO Frequency. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#main_data_path>`
- TX Main NCO Phase Control: Controls the Main NCO Phase. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#main_data_path1>`
- TX Channel NCO Frequency Control: Controls the Channel. NCO Frequency :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#channel_data_path>`
- TX Channel NCO Phase Control: Controls the Channel NCO Phase. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#channel_data_path1>`
- TX NCO Channel Digital Gain: Controls the Channel NCO digital gain. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#tx_nco_channel_digital_gain>`
- TX NCO Test Tone Modes: Controls the Test Tone generation. :dokuwiki:`Read More <resources/tools-software/linux-drivers/iio-mxfe/ad9081#tx_nco_test_tone_modes>`

FPGA Settings
+++++++++++++

Transmit/DDS
~~~~~~~~~~~~

The plugin provides several options on how the transmitted data is generated.

It is possible to either use the built-in two tone **Direct Digital Synthesizer (DDS)**
to transmit a bi-tonal signal on channels I and Q of the DAC.
Or it is possible to use the **Direct Memory Access (DMA)** facility to transmit
custom data that you have stored in a file.

This can be achieved by selecting one of the following options listed by the **DDS Mode**:

One CW Tone
~~~~~~~~~~~

In **One CW Tone** mode one continuous wave (CW) tone will be outputted.
The plugin displays the controls to set the Frequency, Amplitude and Phase
for just one tone and makes sure that the amplitude of the other tone is set to 0.
The resulting signal will be outputted on the Channel I of the DAC and the exact
same signal but with a difference in phase of 90 degrees will be outputted
on the Channel Q of the DAC.

.. image:: one_cw_tone.png

Two CW Tone
~~~~~~~~~~~

In **Two CW Tone** mode two continuous wave (CW) tones will be outputted.
The plugin displays the controls to set the frequencies F1 and F2,
amplitudes A1 and A2, phases P1 and P2 for the two tones. The resulting
signal will be outputted on the Channel I of the DAC and the exact same
signal but with a difference in phase of 90 degrees will be outputted
on the Channel Q of the DAC.

.. image:: two_cw_tones.png

Independent I/Q Control
~~~~~~~~~~~~~~~~~~~~~~~

In **Independent I/Q Control** the plugin displays the controls to set the frequencies,
amplitudes and phases for the two tones that will be outputted on channel
I and additionally it allows for the two tones that will be outputted on
channel Q of the DAC to be configured independently.

.. image:: iq_independent.png

.. note::

   The bi-tonal signal (T) is defined as the sum of two tones:

   .. math::
      T(t) = A1 * sin(2 * p * F1 * t + P1) + A2 * sin(2 * p * F2 * t + P2)

   where:

   - A --- Amplitude
   - F --- Frequency
   - P --- Phase

DAC Buffer Output
~~~~~~~~~~~~~~~~~

The file selector under the File Selection section is used to locate and choose
the desired data file. Under the DAC Channels section the enabled channels will
be used to transmit the data stored in the file. To finalize the process,
a click on the Load button is required.

.. important::

   - There are two types of files than can be loaded: .txt or .mat.
     The IIO-Oscilloscope comes with several data files that can be used.
     If you want to create your own data files please take a look at the
     :doc:`Basic IQ Data Files </solutions/reference-designs/fmcomms2/common/basic_iq_datafiles>`
     documentation first.
   - Due to hardware limitation only specific combinations of enabled channels are possible.
     You can enable a total of 1, 2, 4, etc. channels. If 1 channel is enabled then it can be
     any of them. If two channels are enabled then channels 0, 1 or channels 2, 3 can be
     enabled and so on.

Disable
~~~~~~~

In this mode both DDS and DMA are disabled causing the DAC channels to stop transmitting any data.

.. note::

  - Upon pressing the **Reload Settings** button the values will be reloaded with the corresponding driver values.
    Useful in scenarios where the diver values get changed outside this plugin and a refresh on plugin's values
    is needed.

  - Some plugin values will be rounded to the nearest value supported by the hardware.
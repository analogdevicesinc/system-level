Active Function Model (AFM)
===========================

This page provides a step by step guide to launching and using ADI's new Active
Function Model Tool. The AFM simulates crucial part performance characteristics
within seconds. Configure operating conditions such as operation modes and
sensor biasing/excitation, as well as device features like gain or FIFO.
Performance characteristics include noise, histogram, resolution, power
consumption, timing diagrams, response plots, and more.

Tools and Analysis Window
-------------------------

There are a number of software tools and analysis windows available as part of
the AD4130-8 ACE software window. These tools can be access via the System
Explorer window:

|image1|

\*\* How to access different software tools and timing diagrams:\*\*

The AD4130-8 Sequencer Timer is accessed via the ACE software package:

a. Access the Ace AD4130 Software Plugin as detailed in the :doc:`AD4130-8 User Guide </solutions/reference-designs/ad4130-8/ad4130-8>`

a. Click on the "Tools" on the left hand side. An accordion menu will appear.

b. Select "System Explorer" within this "Tools" menu. A System Explorer window
   will appear on the right hand side.

c. Click on "AD4130-8 Board" and a number of Models will appear.

d. Select "AD4130-8 Sequencer Timing Diagram" for example.

|image2|

--------------

Memory Map
----------

The memory map window allows the user to program and view the parts at a
register level or at a bit level.

-  The main method of writing all changes is to click on "Apply Changes" (1)
-  The register contents can be edited (or read) in as a hex word (2) or at a bit level (3).
-  The user can alternate between a register view and a bitfield view (4).

--------------

.. image:: ../images/mem_map.png
   :align: center

For more details on the register, select the register(1). A pop up will show up
in the bottom of the screen (2). For more detail on the bitfield select the info
bottom to the left of the bitfield (3).

.. image:: ../images/ad4130_8_register_detail.png
   :align: left

--------------

Sequencer Timing Diagram
------------------------

**The AD4130 ACE Program includes a number of integrated software tools to assist in understanding device functionality.**

**1. What is the Sequencer Timing Diagram?**

The Sequencer timing diagram is one of a number of software tools integrated
into our ACE software. The Sequencer Timing Diagram and the FIFO Timing Diagram
have been developed to assist users of the AD4130 in understanding the timing
around sigma delta ADCs of this type. The Sequencer Timing Diagram updates based
on the timing settings selected by the user.

**2. How does the user access the Sequencer Timing Diagram?**

The AD4130 Sequencer Timer is accessed via the ACE software package:

a. Access the Ace AD4130 Software Plugin as detailed in the :doc:`AD4130-8 User Guide </solutions/reference-designs/ad4130-8/ad4130-8>`

a. Click on the "Tools" on the left hand side. An accordion menu will appear.

b. Select "System Explorer" within this "Tools" menu. A System Explorer window
   will appear on the right hand side.

c. Click on "AD4130 Board" and a number of Models will appear.

d. Select "AD4130 Sequencer Timing Diagram"

|image3|

**3. Why is a Sequencer Timing Diagram necessary?**

There a number of configurable timing parameters on the AD4130 that dictate
timing around the AD4130. The diagrams generate with this tool allow us to see
when the part is converting, on which particular channel and when the user needs
to read back the data.

**4. Where are the configurable settings located and how does the user update the diagram?**

The ADC settings are located in the accordion menu on the left hand side within
the "Sequencer Timing Diagram Tab" The user can modify the the settings on the
AD4130 and update the diagram by clicking on the Run button.

`timing_fsm.mp4 <../images/timing_fsm.mp4>`_

**5. What are the main settings that will impact the timing?**

.. important::

   We recommend that the user reads the datasheet before experimenting with
   Sequencer Timing Diagram software functionality

**5a. Enabling ADC Channels** The AD4130 has an on-chip multiplexer allowing a number of channels to be converted upon in a single sequence of conversions. There are 16 channels that can be configured by the user. The analog input signals that are applied to the AIN+ and AIN- for the channel can be selected as well as the setup. The settings that are applied to these channels are refer to as setups.

.. image:: ../images/channel1.png
   :align: center
   :width: 800

**5b. Configuring ADC Setups** The AD4130 allows for up to 8 different setup configurations that can be applied to the channels. The reference, reference buffer and PGA Gain setting will not impact the timing diagram. Within the Setups register contain the settings that have the biggest impact on timing. These are:

-  Sync Filter Setting - Experiment between the different Sync filters available on the AD4130. See how it impacts the 1st sample on a new channel.
-  FS - This value relates dictated our Sample Rate of our ADC. The timing diagram should allow the user to see how often they can read from the ADC.
-  Settle - This is the allows us to increase the settling time displayed in grey at the start of each conversion.
-  Repeat - This repeats a conversion on a single channel.

.. tip::

   Why not experiment with the tool? You could try to compare the timing (output
   data rate) of repeated signal channel conversions versus single conversions
   sequenced on a number of different channels. That first sample on a new
   channel needs to considered right!!!

**5c. ADC Modes**

The AD4130 has a number of modes of operation that can be accessed via the
Model:

-  Continuous Conversion
-  Single Conversion
-  Duty Cycling
-  Single Sequence, Idle by /SYNC
-  Single Sequence, Standby by /SYNC

**6. How does the user calculate the data throughput rate ?**

**Digital Filter Latency**

When more than one channel is enabled the link between the datasheet ODR and the
data throughput rate is complex. This is due to latency of the digital filter
when switching channels. The time needed for the digital filters to settle
depends on the sync filter type. In general the higher the filter order the
lower the noise but the downside is the number of conversion cycles needed for
the filter to settle. The first conversion of Sync3 filter will take 3
conversion cycles until the digital equivalent to the analog input is reached.
The first conversion of a Sync 4 filter will take 4 conversion cycles until the
digital equivalent of the analog input voltage is reached. There is also the
user programable t_settle time that takes into account the mux switching.

|image4|

**How to Calculate our Throughput Rate**

Taking an example where all the channels in our system are configured with the
same settling value, filter settings and configured to complete only 1
conversion ( no repeat conversion) we can use the information available in our
model or in the datasheet to calculate our effective output data rate:

.. note::

   
   Example 1: All channels configured with the same configuration and no repeat
   conversions on any channel.
   
   -  *Filter Type = Sync 3*
   -  *FS = 1*
   -  *SETTLE_n = 1*
   -  // Number of Channels Enabled = 3 or 5//
   

We calculate our output data rate based on the datasheet tables to be 2400/FS
for a Sync 3 filter this makes our single channel output data rate to be.

*Single channel settled ODR (Hz) = 2400*

.. important::

   Calculating your Throughput rate is not as simple as taking your Settled
   Channel ODR(Hz) and dividing by the number of channels enabled because of the
   digital filter latency described above.

When we enable more than one channel the initial settling needs to be taken into
account and based on our SETTLE_n in this example SETTLE_n = 1 making number of
MCLK cycles before the conversion begins after switching channels equal to:

*t\ SETTLE (MCLKs) = 32*

There is always a fixed digital post processing time of 28 MCLK cycles that
impacts when the data can be read back on the first conversion which can be
discounted when calculating our throughput rate due to the time overlap with the
settling time as seen in the figure below:

*DPP time (MCLKs) = 28*

The first conversion on each channel needs to take into account the filter
latency. The number of MCLK cycles this takes depends on the filter type. For a
Sync3 filter it is 3 times the settled channel conversion time. For a Sync 4
filter it is 4 times the settled conversion time. The latency is due to the
settling of the digital filter.

.. note::

   Solving Example 1:

   
   t\ :sub:`1ST_CNV_IDEAL` + t\ :sub:`SETTLE` (MCLKS) = *((3 x 32 x 1) + 32) = 128*
   
   where MCLK(sec) = 1/76.8kHz
   
   *1/76800 x (128) = 600 SPS*
   
   If we were converting on only one channel our 1st conversion ODR would be:
   
   *f\ 1CNV_ODR\ (SPS) = 600 SPS*
   
   In order to calculate our effective output data rate we divide our f\ :sub:`1CNV_ODR`\ 1conv_odr by the number of channels we are converting on to get our effective output data rate.
   
   with 3 channels enabled:
   
   *Throughput rate = 600/3 = 200 SPS*
   
   with 5 channels enabled:
   
   *Throughput rate = 600/5 = 120 SPS*

How to Calculate the Throughput Rate using the Timing Tool

The sequencer timing diagram in continuous conversion mode or duty cycling mode
allows us to calculate our throughput rate.

.. note::

   The /RDY falling edge to /RDY falling edge time between subsequent conversions = t\ :sub:`1ST_CNV_IDEAL` + t\ :sub:`SETTLE`

.. image:: ../images/falling_edge_to_falling_edge.png
   :align: center

If we use the timing tool (two sequences shown each with 3 conversions per sequence shown) we see exactly what is happening. We can tell the rate of the conversion on a per channel basis or the throughput rate. |image5|

|image6|

.. note::

   Solving Example 1:

   
   Using the information displayed:
   
   t\ :sub:`1ST_CNV_IDEAL` + t\ :sub:`SETTLE` = 1.67ms
   
   1/1.67ms = 600ms
   
   We divide this by the number of channels we have: 600SPS/3 = 200SPS
   
   Throughput rate (SPS) = 200SPS

**How to Calculate the Throughput Rate using the Timing Tool through multiple channels with different configurations**

We can calculate the throughput rate using the timing tool using. We take the sum of the /RDY falling edge to /RDY falling edge times between subsequent conversions. (t\ :sub:`1ST_CNV_ODR` in the AD4696-8 datasheet) telling us how often the channel is being sampled. The length of time the conversion is taking place will vary depending on the filter selection as well as oversampling and decimation (FS value) settings but the overall throughput rate is dictated by the total time it takes for all conversions enabled in the sequence.

In all of the examples we are excluding Repeat conversions but when we enable
repeat conversions, the timing tool allow us to see exactly what happens
visually.

.. note::

   Example 2: 3 channels configured with independent configurations and no
   repeat conversions on any channel.

   
   -  Channel 0 - We want to gather a conversion as fast as possible.
   -  Ain0 -Ain 1
   -  *Filter Type = Sync 3*
   -  *FS = 1*
   -  *SETTLE_n = 1*
   -  // Number of Channels Enabled = 3 or 5//
   
   -  Channel 1 - We want to achieve 50 Hz rejection. (Set the cut off freq. of our filter to FS=48)
   -  Ain2- Ain3
   -  *Filter Type = Sync 3*
   -  *FS = 48*
   -  *SETTLE_n = 1*
   -  // Number of Channels Enabled = 3 or 5//
   
   -  Channel 2 - We want to achieve 50 Hz rejection(Set the cut off freq. of our filter to FS=48) and Lower Noise (Sync 4)
   -  Ain 3 - Ain4
   -  *Filter Type = Sync 3*
   -  *FS = 1*
   -  *SETTLE_n = 1*
   -  // Number of Channels Enabled = 3 or 5//

   |image7|

.. note::

   
   Solving Example 2:
   
   1/ (60.859ms + 80.417ms + 1.244ms) = 7 SPS
   
   Throughput Rate = 7SPS
   

--------------

FIFO Timing Diagram
-------------------

**7. How does the user calculate the amount of time I have to readback FIFO while converting?**

The AD4130 includes an on-board FIFO allowing users to minimize the time when
their microcontroller is actively reading from the part. The ‘Watermark’ mode is
first in mode where data is gathered until a number of samples (a watermark) is
reached. The user can continually convert or use in the FIFO in conjunction with
/SYNC to kick off conversions. The FIFO when continuously converting needs to be
emptied when the interrupt signal goes high. The user has a pre-defined period
of time to read back data from the FIFO. The FIFO readback window is a function
of the users SCLK frequency. The tool allows the user to vary the SCLK frequency
or use a gated clock to inform the user when designing their system that, they
need to reduce their watermark level.

.. image:: ../images/fifo.png
   :align: center
   :width: 2000

The maximum clock frequency when reading the AD4130 is 5MHz but if the user is
using a gated clock with delays in between writes, watermark level may need to
be reduced to avoid missed conversions. While continuously converting the user
does not read the data completely from the FIFO. There maybe be the case where
the user is not reading the FIFO quickly enough. If the user attempts to convert
while the FIFO is being read, conversions may be ignored if the DOUT is being
read. If you continues to read back after this time is exceeded while attempting
conversions, the conversions will be discarded. This is because the FIFO is
still being read when a new conversion is attempting to take place. The
conversion will be lost.

.. image:: ../images/events_window_revb.png
   :align: center
   :width: 1100

The events window can be opened to display errors. It is accessed under 'Tools'.

The user can select their SCLK Frequency as well as any gating that might delay
the clock.

The user can also select their watermark value.

The AD4130 FIFO Timing Diagram Tool will display an error if the clock speed is
too slow to read back the data in the calculated readback time.

.. tip::

   The tool will recommend for the user to reduce the watermark level to avoid
   missed conversions

\*\* 8. When in duty cycle mode, how can the user calculate the throughput
rate?*\*

We can calculate the throughput rate using the timing tool using. We take the
sum of the /RDY falling edge to /RDY falling edge times between subsequent
conversions. Another option would be to take the sum of the active and standby
time. This info tells us how often the channel is being sampled. The length of
time the conversion is taking place will vary depending on the duty cycle ration
(1:4 or 1:16), the filter selection as well as oversampling and decimation (FS
value) settings.

.. image:: ../images/duty_cycling_wiki_plot_zoomed.png
   :align: center
   :width: 1100

--------------

Power Calculator
----------------

The power calculator allows the user calculate the average power based on the
user settings chosen.

It allows the user to choose a supply voltage (1) as well as a battery type (2)
where the tool calculated the time it would take to drain the batter when
operating the AD4130-8 using the register settings and configuration chosen by
the user.

|image8|

The average power is based on the user settings chosen. The breakdown of this power is also displayed in the `Timing Diagram <https://wiki.analog.com/resources/eval/user-guides/ad4130/seq_timing_diagram>`_. This allows the user to enable duty cycling and observe the changes in Idd with respect to time.

|image9|

--------------

Analysis Window
---------------

The Analysis Window is used for making measurements using a physical hardware.
An AD4130-8 Evaluation board is needed to capture data. Data is captured by
clicking on 'Run Once' or 'Run Continuously'.

The **Histogram** or **Waveform** sections (3) display the results of the noise analysis or the waveform for the selected analysis channel, including both noise and resolution measurements.

|screenshot_2021-04-09_122534.png|

-  The data graph (1) shows each successive sample of the ADC output. Zoom in on the data in the graphusing the scroll wheel on your mouse or by selecting the magnifying glass.
-  The **Result** section (2) shows the analysis of the channel selected.
-  The **Samples** numeric control sets the number of samples gathered per batch. This control is unrelated to the ADC mode. You can capture a defined sample set or continuously gather batches of samples. In both cases, the number of samples set in the **Samples**\ (4) numeric input dictates the number of samples.
-  Click the Run Once button (2) to start gathering ADC results. Click the **Run Continuously** button (2) to start gathering ADC results continuously. Results appear in the waveform graph (1).
-  Click the **Codes** drop-down menu (5) to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls is fixed. When selecting **Fixed**, the axis ranges can be programmed; however, these ranges do not automatically adjust after each batch of samples.

--------------

Noise(Simulation Analysis) Window
---------------------------------

Labeled "AD4130 Noise" in the system explorer, this window behaves similar to the Analysis window but the results are simulated and not measured. This allows the user to compare simulated to measured results. The buttons used to control are detailed in: `Analysis Window <https://wiki.analog.com/resources/eval/user-guides/ad4130/analysiswindow>`_

.. image:: ../images/demo_noise.png
   :align: center

--------------

Frequency Response Window
-------------------------

This window allows the user to observe the response of the internal filter based
on their filter register settings (including FS value).

.. image:: ../images/filter.png
   :align: center

-  Filter cut off calculated in the results section
-  The notch in is also displayed on the waveform screen.
-  There is to manually check the rejection at user defined rejection frequecies F1 and F2.
-  The MCLK frequency can also be varied in also to observe the impact of
   oscillator error on rejection.

--------------

Step Response Window
--------------------

This window simulates the step response associated with the analog input ideal
step. This shows the input voltage step and settling time associated with the
digital filter chosen. Click 'Run' to simulate the step response based on the
register settings selected.

.. image:: ../images/step.png
   :align: center

:doc:`Previous Page: Software Guide </solutions/reference-designs/ad4130-8/softwareguide>`

:doc:`Return to Homepage </solutions/reference-designs/ad4130-8/ad4130-8>`

.. |image1| image:: ../images/accessing_ad4130_analysis_window_and_tools.png
.. |image2| image:: ../images/system_explorer_pane.png
   :width: 800

.. |image3| image:: ../images/system_explorer_pane.png
   :width: 800

.. |image4| image:: ../images/first_conversion_on_a_new_channel_diagram.png
   :width: 800

.. |image5| image:: ../images/2_cycles_sync_3_same_setup_3_channels_enabled.png
   :width: 1100

.. |image6| image:: ../images/2_cycles_sync_3_same_setup_3_channels_enabled_zoomed.png
   :width: 1100

.. |image7| image:: ../images/example_2d.png
   :width: 1100

.. |image8| image:: ../images/power.png
.. |image9| image:: ../images/idd_timing_window.png
.. |screenshot_2021-04-09_122534.png| image:: ../images/screenshot_2021-04-09_122534.png

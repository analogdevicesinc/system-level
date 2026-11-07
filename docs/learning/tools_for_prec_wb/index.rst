.. collection:: Tools for Precision Wideband Mixed Signal System Design
   :subtitle: Tools for precision wideband mixed-signal applications.
   :label: tutorial

   Explore signal generation, data acquisition, and frequency-domain analysis.

   system-level:
     - .
     - learning/tools_for_ls/index
     - learning/sw_infrastructure/index
     - tools/m2k/index

Tools for Precision Wideband Mixed Signal System Design
===============================================================================

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

The goal of this tutorial is to equip the reader with a collection of
hardware and software tools for developing precision wideband
mixed-signal applications.
**Content Guide:** This tutorial includes complete written
instructions, a video guide, and a slide deck that can be used for
delivering as a hands-on workshop.
What exactly does "Precision Wideband" mean?

The "precision" part means that DC parameters such as offset, gain
error, linearity, and temperature drift are also important.

The "wideband" part means that **unlike** "low speed"
applications, timing, or jitter, of individual samples with respect to
previous and future samples **IS** critical. The application involves
extracting information from arrays of samples that are correlated with
each other in some way. AC performance metrics such as signal to noise
ratio and total harmonic distortion extracted from a Fourier transform
of the data **will** be considered. Even if the end application does
not involve sine waves, these metrics are almost always a useful
indicator of performance.


An important point is that sample jitter is important for the "wideband"
aspects of these applications. If you are measuring signal to noise ratio,
the Signal to Noise ratio (SNR) can be no greater than:

:math:`SNR <= -20 * log(2*pi*f\_{IN}*t\_{j})`

Where:
:math:`f_{IN}` is the analog input frequency in Hz
:math:`t_{j}` is the RMS jitter in seconds RMS

In this tutorial, we will be generating excitation waveforms,
digitizing time-domain signals, performing Fast Fourier Transforms
(FFTs), extracting features from the frequency domain, and calculating
measurement parameters. We **will** be measuring AC Signal to Noise
Ratio (SNR), Total Harmonic Distortion (THD), measuring steps,
wiggles, and other situations where precise timing is required.
Throughout the exercises we'll be writing simple Python code to
capture and analyze data, using the industry standard Industrial I/O
(IIO) framework to interact with the ADC, and the popular NumPy and
Matplotlib Python libraries. Thus this exercise also serves as a
mini-tutorial on Python.

Materials
~~~~~~~~~~~~~~~~~~~

-  Raspberry Pi 4; 2G, 4G, or 8G version, OR Raspberry Pi 400 (the
   keyboard one).
-  5V USB-C wall adapter for Raspberry Pi
-  Colorimeter Setup. This is not in production (yet), but full gerbers
   are provided. The pull request is in review,
   `HERE <https://github.com/analogdevicesinc/education_tools/pull/48>`__
-  Optical absorbance demonstration material such as:

   -  Optical filters such as `Roscolux Selector Pack <https://www.mcmaster.com/7769T9/>`__
   -  `API pH test and adjust kit <https://www.apifishcare.com/product/ph-test-adjuster-kit>`__

-  16GB (or larger) Class 10 (or faster) micro-SD card, with
   :ref:`kuiper` installed.
-  User interface setup (choose one):

   -  HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
   -  Host Windows/Linux/Mac computer on same network as Raspberry Pi

-  :adi:`ADALM2000`
-  Clone or download zip of the Python code for this tutorial from:
   `Python Code for the Hardware and Software Tools for Precision Wideband Instrumentation Workshop <https://github.com/cristina-suteu/ftc23-hstpwi/>`__

This probably isn't necessary as of Kuiper 2022r2, but just in case
you want to update pyadi-iio or have the examples in your home
directory, run these commands in a terminal:

.. shell::

   $git clone https://github.com/analogdevicesinc/pyadi-iio.git
   $cd pyadi-iio
   $sudo pip install .

Background
~~~~~~~~~~

This tutorial builds on the concepts covered in:
Introduction to the basic concepts of writing software to talk to
external devices:
`Converter Connectivity Tutorial </university/labs/software/iio_intro_toolbox>`__
This tutorial that starts to deal with analyzing time series data:
`Precision ADC Tutorial </university/labs/software/precision_adc_toolbox>`__
And this workshop in which we actually build a simple test instrument:
`Tools for Low Speed Mixed Signal System Design </university/labs/software/tools_for_low_speed_mix-sig_systems>`__

Slide Deck and Video
~~~~~~~~~~~~~~~~~~~~

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

A complete video run-through is also provided, either as a companion
to following the tutorial yourself, or to practice before presenting
as a hands-on workshop:

.. todo::

   Video and Slide Deck

Preparation - a few resources for learning Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Stack Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Introducing an exciting new product that we'll apply our skills to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Booting the system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Post-boot housekeeping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configuring the System (and rebooting!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Command Line Tools (Hello, Colorimeter and AD4630-24!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pyadi-iio And examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next Steps: Other languages (C++, C#, MATLAB, etc.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Wrapup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Additional References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

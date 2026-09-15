.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms11-ebz

.. _ad-fmcomms11-ebz:

AD-FMCOMMS11-EBZ User Guide
===========================

The AD-FMComms11-EBZ board is a system platform board for communication
infrastructure applications that demonstrates the Direct to RF (DRF) transmitter
and observation receiver architecture. Using high sample rate RFDAC(s) and
RFADC(s), a number of components in previous generation transmitters can be
eliminated, such as mixers, modulators, IF amplifiers and filters. The objective
being to bring the ADC or DAC as close to the antenna as possible, leading to
possibly more cost effective and efficient communications solution. It is
composed of multi-GSps RF ADC :adi:`AD9625` and DAC :adi:`AD9162`, Cheetah and
Barium respectively. The transmit path contains a balun, low pass filter, gain
block and variable attenuation to produce an output appropriate for a power
amplifier module. Along the observation path, the PA output is coupled back into
the board through a variable attenuator, a balun and finally the ADC. Clock
management is taken care of on board; all the necessary clocks are generated
from a reference. Power management is present as well. We will provide typical
performance data for the entire range (70 MHz – 6 GHz) which is supported by the
platform. This is primarily for system investigation and bring up of various
waveforms from a software team before their custom hardware is complete, where
they want to see waveforms, but are not concerned about the last 1dB or 1% EVM
of performance.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/fmcomms11_image.png
   :width: 600px

Table of Contents
-----------------

#. :dokuwiki:`Introduction <ad-fmcomms11-ebz/introduction>`
#. :dokuwiki:`FMCOMMS11 Hardware <ad-fmcomms11-ebz/hardware>`: This provides a
   brief description of the AD-FMCOMMS11-EBZ board by itself, and is a good
   reference for those who want to understand a little more about the board. If
   you just want to use the board, you can skip this section, and come back to
   it when you want to incorporate one of the devices into your product.

   #. :dokuwiki:`Hardware <ad-fmcomms11-ebz/hardware>` (including
      :dokuwiki:`schematics </ad-fmcomms11-ebz/hardware#downloads>`)

      #. :dokuwiki:`Functional Overview & Specifications <ad-fmcomms11-ebz/hardware/functional_overview>`
      #. :dokuwiki:`Characteristics & Performance <ad-fmcomms11-ebz/hardware/card_specification>`
      #. :dokuwiki:`Configuration options <ad-fmcomms11-ebz/hardware/configuration_options>`
      #. :dokuwiki:`FCC or CE certification <ad-fmcomms11-ebz/certification>`

   #. :dokuwiki:`Production Testing Process <ad-fmcomms11-ebz/testing>`

#. Use the AD-FMCOMMS11-EBZ Board to better understand the :adi:`AD9625` and
   :adi:`AD9162`

   #. :dokuwiki:`What you need to get started <ad-fmcomms11-ebz/prerequisites>`
   #. :dokuwiki:`Quick-Start Guides <ad-fmcomms11-ebz/quickstart>`

      #. :dokuwiki:`Linux on ZC706 <ad-fmcomms11-ebz/quickstart/zynq>`
      #. :dokuwiki:`Configure a pre-existing SD-Card </resources/tools-software/linux-software/zynq_images#preparing_the_image>`
      #. :dokuwiki:`Update the old card you received with your hardware </resources/tools-software/linux-software/zynq_images#staying_up_to_date>`

   #. Linux Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`

         #. :dokuwiki:`FMCOMMS11 Control in the IIO Scope Plugin <resources/tools-software/linux-software/fmcomms11_plugin>`

   #. :dokuwiki:`HDL reference design <ad-fmcomms11-ebz/reference_hdl>`

#. Design with the FMCOMMS11"s AD9625 and AD9162

   #. Understanding the FMCOMMS11

      #. :adi:`AD9162 Product page <AD9162>`
      #. :adi:`AD9625 Product page <AD9625>`

#. :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`

ADI Articles
------------

- Four Quick Steps to Production: Using Model-Based Design for Software-Defined
  Radio
- :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
- :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
- :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
- :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

ADI Videos
----------

- :adi:`Silent Switcher µModule Regulators Powering GSPS Sampling ADC <en/products/ad9625.html#product-recommendations>`

MathWorks Webinars
------------------

- :mw:`Modelling and Simulating Analog Devices" RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

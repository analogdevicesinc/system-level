.. imported from: https://wiki.analog.com/resources/eval/user-guides/pwm-generator

.. _pwm-generator:

PWM-Generator System Overview
=============================

(this page is under construction) The PWM-Generator Add-On for EVAL boards
simplifies setup and testing by providing all PWM signals required to stimulate
3-phase B6 inverter topologies. The Generator is based on an STM32L432KCU6
Nucleo32 development board and is fully controlled via USB from a host running a
Windows 10 OS. A small GUI application on the host controls all functions of the
PWM-Generator.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-overview-1.jpg

Output Signals & Pin-Out
========================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-sig-pin.jpg

Proposed Level Shifter Interposer Board
---------------------------------------

In cases where Eval-Boards expect 5V logic (TTL) input signals, level-shifting
from 3.3V logic of the PWM Generator is required. This could be achieved by a
level-shifter interposing board. In order to facilitate usage and minimize
p.c.b. real estate, such a level-shifter board could also accommodate the
PWM-Generator in a piggy-back fashion.

A GENPRES (generator present) signal is provided to the host eval board which
can be modified by the host in order to disable the PWM-Generator"s outputs.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-interposer-1.jpg

Physical Dimensions for EVAL-Board Integration
----------------------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-mech.jpg

Setup Guide
-----------

a. Prerequisites

Required Hardware:

#. STM32L432 :digikey:``NUCLEO32`` evaluation board,
   `NUCLEO-L432KC <NUCLEO-L432KC>`
#. Computer running Windows 10

Required Software:

#. STM32CubeProgrammer for programming the STM32L432 with the PWM Generator
   firmware, https://www.st.com/en/development-tools/stm32cubeprog.html
#. ADI PWM Generator Software, this contains the PWM Generator Control software,
   as well as the PWM Generator firmware.
   https://webcontent.corpnt.analog.com/SSDAdmin/ApprovedSecureContent.aspx

b. Installation:

#. First, install the ADI PWM generator software. This will also copy the
   firmware for the STM32L432 NUCLEO on your computer, which will then be
   transferred to the NUCLEO in a later step. Do not start the application yet.
   The installation directory is C:\\Analog
   Devices\\SoftwareModules\\PwmGenerator-Rel1.0.0

#. Install the STM32CubeProgrammer. Connect the STM32L432 NUCLEO board to your
   computer. The red LED on the NUCLEO board will light up. Open the
   STM32CubeProgrammer app:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-cube-1.jpg

On the right hand pane, make sure that the connection type is set to ST-LINK, then click ``Connect``. The log window should report a successful connection as ``Data read successfully`` (the data displayed in the data window may be different). Note that the NUCLEO LED is flashing in red/green.\ .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-cube-2.jpg

3. Install the PWM generator firmware on the NUCLEO board: click on the ``Open
   file`` tab and open the firmware ``adi_pwm_gen.hex`` in C:\\Analog
   Devices\\SoftwareModules\\PwmGenerator-Rel1.0.0\\firmware\\bin.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-cube-3.jpg

Now, click on the ``Download`` button to download the firmware onto the NUCLEO.
Click OK to confirm the completion of the download process. Your STM32L432
NUCLEO is now ready to run as a PWM generator. Close the STM32CubeProgrammer.

Using the PWM Generator
-----------------------

1. Start the PWM generator software (PGS) pwm_gen_gui.exe in

C:\\Analog Devices\\SoftwareModules\\PwmGenerator-Rel1.0.0\\host\\bin

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/adi-pwm-generator-1.jpg

2.Select the correct COM port in the drop-down list. The PGS will immediately
connect to the NUCLEO board:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/adi-pwm-generator-2.jpg

3.Now you can set the PWM parameters according to your requirements:

- PWM Frequency: Carrier frequency ouf the PWM outputs (1kHz .. 250 kHz)
- PWM Deadtime: Deadtime of signal transitions between associated high-side and
  low-side PWM outputs.
- Modulation Frequency: Modulation frequency applies to all six output channels.
  A modulation frequency of 0 Hz allows for static testing at a fixed
  (``frozen``) modulation depth, set by
- Modulation Amplitude: Sets the peak modulation depth on all PWM channels. A
  modulation of 0 sets all PWM outputs to fixed 50 % duty cycle, a modulation
  amplitude of 1 sets the PWM outputs vary between 100 % and 0% duty cycle
  according to the Modulation Frequency setting.
- Modulation type: Lets you choose from either pure sine modulation or sine +
  3rd harmonic modulation (actually, a space modulation pattern is implemented).
  Oscillograms show typical PWM-generator waveforms after 1kOhm / 100 nF
  low-pass filter on each output.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-sig-1.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pwm-generator/pwm-generator-sig-2.jpg
   :width: 400px

Finally, click on ``Apply`` to send the changes to the PWM generator, which will
then take immediate effect. You can then ``Save`` and ``Load`` these settings
for later use.

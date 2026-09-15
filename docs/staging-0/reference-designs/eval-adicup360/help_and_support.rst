.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/help_and_support

.. _eval-adicup360 help_and_support:

Help and Support
================

Do you need help or have general support questions, than I hope this page helps
you resolve those.

This page has a quickstart troubleshooting approach that goes over some very
general questions and common pitfalls, but if you have a specific issue which
requires more information or detail please contact us through EngineerZone or
Email. (links can be found further down on the page where to direct specific
questions)

What to do When Things Go Wrong
-------------------------------

There are many things that can go wrong with an ecosystem this complex, but if
you are having issues getting the board or software working, here are a few
simple things you can try before contacting Analog Devices.

#. Check the Power

- Do you have the USB cable plugged in? What about the DC power jack?

#. Program the ADICUP360

- Sometimes a flashed program doesn"t run properly or can make it difficult to
  run the debugger.
- The first thing to try in this case, is to
  :dokuwiki:`drag and drop </resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers#daplink_drive>`
  a known good .BIN program into flash.(something with quick visible indicators
  works best, for example a blink program)
- If drag and drop is not working, it may be necessary to erase the flash. To do
  so:
- Download and install the CrossCore Serial Flash Programmer from here:
  :adi:`en/design-center/processors-and-dsp/evaluation-and-development-software/crosscore-serial-flash-programmer.html#dsp-overview`.
- Make sure that the USB cable is plugged into the USER USB(P13)
- Ensure the switch matrix is set up like this: S1=0, S2=1, S3=0, S4=1
- Power cycle the ADICUP360 board while holding down the boot switch (S6)
- Select the mbed serial COM port in the CrossCore Serial Flash Programmer, and
  erase the flash.
- Then try
  :dokuwiki:`dragging and dropping <resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers#daplink_drive>`
  a working .BIN file into flash (again a blink program will
  verify the fix fastest)
- Not receiving/transmitting data to the UART
- Make sure that the switch matrix (S1,S2,S3,S4) are set correctly for which set
  of UART pins you want to use and that your USB cable is plugged into the USER
  USB(P13).
- I'm trying to program/debug, but I'm getting errors.
- Make sure that you are plugged into the DEBUG USB(P14) when trying to
  program/debug your program.  This is the only USB that connects to the
  ADuCM360.
- Check the drives attached to your computer, do you see a mass storage device
  called Mbed or Maintenance ?  If you see the Maintenance drive and your USB is
  plugged in, then likely the ADICUP360 isn't being powered.  Try power cycling
  the USB cable, you may have just hit the "Boot" or "RESET" button during power
  up by accident.

This is just a brief self-help guide to troubleshooting common issues. If you
have other questions that need answering please direct those requests to the
locations outlined below.

Hardware, Software, and Documentation Questions
-----------------------------------------------

If you have any questions regarding the **base platform**, any of the
**shields/pmods** or are experiencing any problems using the **software** or
issues following any of the **documentation** feel free to ask us a question.

- :ez:`ADuCM360 support community <community/analog-microcontrollers/aduc-cortex-m3>`
  for questions about:

  - ADICUP360 hardware
  - ADuCM360 silicon
  - ADICUP360 software
  - ADICUP360 documentation

- :ez:`Reference Design support community <community/circuits_from_the_lab>` for
  questions about:

  - Add on Arduino shields from Analog Devices
  - Add on PMODs from Analog Devices
  - Add on Arduino shield or PMOD documentation

When asking a question please take the time to give a detailed description of
your problem. If you are experiencing a problem please state the steps you have
executed, the result you expected you would get and the result you actually got.
By doing so you enable us to provide you precise and detailed answers in a
timely manner.

.. tip::

   Before asking questions please take the time to check if somebody else
   already asked the same question. You might just find your question already
   answered.

CrossCore Embedded Studio questions
-----------------------------------

If you have questions regarding the tools used with the EVAL-ADICUP360, either
post a question or send an email.

- :ez:`CrossCore Embedded Studio support community <community/dsp/software-and-development-tools/cces>`
  for questions about:

  - Download/Install issues
  - Build, debug, run, issues
  - Other tools related issues

- The CrossCore Embedded Studio team can also be emailed using the address
  below:

  - :dokuwiki:`processor.tools.support@analog.com </mailto/processor.tools.support@analog.com>`

ADuCM360-IDE questions (Deprecated)
-----------------------------------

.. note::

   This Interactive Development Environment(IDE) is being **phased out** as of
   **October 30th 2017**. We are moving the EVAL-ADICUP360 tools support over
   to CrossCore Embedded Studios(CCES). You should consider migrating to CCES
   at your earliest convenience. We will be **removing support** for the
   ADuCM360-IDE tools **April 30th 2018**. Here is a link to download the
   :dokuwiki:`CrossCore tools. </resources/eval/user-guides/eval-adicup360/tools/cces_setup_guide#crosscore_embedded_studio_download_packages>`

Questions about the Analog Devices Eclipse IDE should be asked at the
:ez:`ADuCM Eclipse IDE support community <community/analog-microcontrollers/aducm-eclipse-ide>`.

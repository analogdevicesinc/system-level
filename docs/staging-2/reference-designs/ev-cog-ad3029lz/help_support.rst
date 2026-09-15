.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029lz/help_support

.. _ev-cog-ad3029lz help_support:

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

**Check the Power**

- Do you have the USB cable plugged in? if yes, then check switch (S7) in USB
  position
- If you are using batteries, is the switch (S7) in the ``BATT`` position

  - Try replacing your batteries, and see if the board powers up.

**Program the EV-COG-AD3029LZ**

- Sometimes a flashed program doesn"t run properly or can make it difficult to
  run the debugger.
- The first thing to try in this case, is to
  :dokuwiki:`drag and drop </resources/eval/user-guides/ev-cog-ad3029lz/tools/hardware_usb>`
  a known good .HEX or .BIN program into flash.(something with quick visible
  indicators works best)
- If drag and drop is not working, it may be necessary to erase the flash. To do
  so:

  - Download and install the CrossCore Serial Flash Programmer from here:
    :adi:`en/design-center/processors-and-dsp/evaluation-and-development-software/crosscore-serial-flash-programmer.html#dsp-overview`.
  - Make sure that the USB is connected and on UART header (P8) 1 & 2 and 7 & 8 are shorted.
  - Power cycle the EV-COG-AD3029LZ board while holding down the boot switch.
  - Select the mbed serial COM port in the CrossCore Serial Flash Programmer, and
    erase the flash.
  - Then try :dokuwiki:`drag and drop <resources/eval/user-guides/ev-cog-ad3029lz/tools/hardware_usb>`
    a .HEX or .BIN file into flash
  - If the mass erase didn't work, and you are trying to drag and drop a large
    .BIN file on EV-COG-AD3029LZ hardware, it's possible that the mbed interface
    file needs to be updated to support your application.

- Please visit the
  :dokuwiki:`Driver Installation for On-board Debugger (CMSIS DAP) <resources/eval/user-guides/ev-cog-ad3029lz/tools/hardware_usb>`
  page in order to put the board in update mode.
- Once you are in "maintenance mode" you should drag and drop the latest
  interface file onto your maintenance drive.  That file can be downloaded at
  the bottom of
  :dokuwiki:`Driver Installation for On-board Debugger (CMSIS DAP) <resources/eval/user-guides/ev-cog-ad3029lz/tools/hardware_usb>`.

- Not receiving/transmitting data to the UART

  * Make sure that the UART header (P8) is positioned in the correct
    destination to transmit/receive UART data.
  * JH6 is shorted.

This is just a brief self-help guide to troubleshooting common issues. If you
have other questions that need answering please direct those requests to the
locations outlined below.

Hardware, Software, and Documentation Questions
-----------------------------------------------

If you have any questions regarding the **EV-COG-AD3029LZ**, any of the
**shields/pmods** or are experiencing any problems using the **software** or
issues following any of the **documentation** feel free to ask us a question.

-
  :ez:`ADuCM3029 support community <community/analog-microcontrollers/aducm302x>`
  for questions about:
- EV-COG-AD3029LZ hardware
- ADuCM3029 silicon
- EV-COG-AD3029LZ software
- EV-COG-AD3029LZ documentation

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

If you have questions regarding the tools and tool chain that is used with the
EV-COG-AD3029LZ, either post a question or send an email.

-
  :ez:`CrossCore Embedded Studio support community <community/dsp/software-and-development-tools/cces>`
  for questions about:

  - Download/Install issues
  - Build, debug, run, issues
  - Other tools related issues

- The CrossCore Embedded Studio team can also be emailed using the address
  below:

  - :dokuwiki:`processor.tools.support@analog.com </mailto/processor.tools.support@analog.com>`



:dokuwiki:`Back </resources/eval/user-guides/ev-cog-ad3029lz>`

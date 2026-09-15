.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/tools/ccsfp_unlock_adicup360

.. _eval-adicup360 tools ccsfp_unlock_adicup360:

Unlocking a ``Bricked`` ADICUP360
=================================

Problem Statement
-----------------

Occasionally when you are debugging a new program or loading a pre-built .BIN
file using the ADICUP360, the board can get stuck and becomes unusable(commonly
known as ``bricked``). This can happen because the code is in an endless loop,
hard fault occurs, or other mistakes that make it so the board becomes
unresponsive.

The good thing is there is a way to recover your hardware from this condition!

How to Recover the ADICUP360
----------------------------

#. Download and install
   :adi:`CM3WSD UART Programmer <media/en/evaluation-boards-kits/evaluation-software/CM3WSD.zip>`
#. Plug in the micro USB cable into P13 of the EVAL-ADICUP360 board
#. Setup the switches on the ADICUP360 board as follows:

   #. S1=0 , S2=1 , S3=0 , S4=1

#. Plug the other end of the USB cable into the computers USB port
#. Open up the CM3WSD UART Programmer tool
#. Change the parameters of the utility to the following settings:(see image
   below)

   #. ``Serial Port`` = COM X (USB Serial Port)
   #. ``Baudrate`` = 9600

::

   - "Flash Action" = Mass Erase\\ {{ :resources:eval:user-guides:eval-adicup360:tools:cm3wsd_setup.png?400 |}}

#. On the EVAL-ADICUP360 board, hold down the ``**BOOT**`` button
#. On the EVAL-ADICUP360 board press and release the ``**RESET**`` button, but
   continue holding the ``**BOOT**`` button
#. Go back to the CM3WSD UART Programmer application and hit the ``**Start**``
   button

#. Allow the program to finish erasing the memory, and once its complete your
   EVAL-ADICUP360 will be ready for use once again.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/tools/cm3wsd_success.png
      :width: 400px

*End of Document*

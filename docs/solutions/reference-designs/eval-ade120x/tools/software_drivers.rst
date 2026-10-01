How to Use ADE120x Software Drivers
===================================

The software drivers for the ADE120x products were written using the MBED
platform. MBED is an open source, online development environment that supports a
large array of controller boards with ARM core processors. The SDP-K1 is a
controller board developed by ADI and is designed to be used to develop drivers
and example programs for ADI evaluation boards.

The MBED code was written to run on the EVAL-SDP-K1 evaluation board connected
to the EVAL-ADE1202EBZ evaluation boards. Note, EVAL-SDP-K1 needs to be
purchased separately.

Note, the EVAL-SDP-K1 needs to be purchased separately

For further details refer to `this link <https://confluence.analog.com/display/MBED/Mbed%3A+Instructions+for+Users+and+Customers>`_

Getting Started
---------------

-  To use the EVAL-SDP-K1 with the MBED online compiler a user account must
   be set up first. To set up an account navigate to
   `MBED <https://www.mbed.com/en/>`_
-  Follow `this link <https://wiki.analog.com/resources/tools-software/mbed>`_
   for instructions on setting up the SDP-K1 within the MBED environment.
-  The ADE1202 example application can be found `here <https://os.mbed.com/teams/AnalogDevices/code/EVAL-ADE120x/>`_
-  To get started click on the Import Into Compiler button

.. image:: ../images/ade120x_mbed.png
   :align: center
   :width: 400

-  Once imported into the compiler the screen should look like the following:

   |image1|

   On the left hand side is the Program Workspace and will display any
   programs you have imported into the workspace.
-  Double click on the main.cpp file to open the main program code.

.. |image1| image:: ../images/mbed_workspace.png
   :width: 400

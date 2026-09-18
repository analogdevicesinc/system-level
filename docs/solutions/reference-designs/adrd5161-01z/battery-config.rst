ADRD5161-01Z Battery Configuration
==================================


Description
-----------

The fuel-gauge chip MAX17320 has the configuration data stored in a non-volatile memory, which has a limited number of writes. Because of this, we recommend using
the configuration that is already loaded on the chip, which is compatible with for 3 series, 2 parallel Panasonic NCR18650GA Li-ion batteries.
In order to obtain compatibility with other battery packs, MAX17320's non-volatile memory needs to be updated to reflect the characteristics of the new batteries.
The following sections describe this process. 
NOTE: We strongly suggest using the recommended configuration. 


Hardware Requirements
---------------------

* ADRD5161-01Z board
* I2C FTDI Programmer with SWD Header
* User desired battery pack


Software Requirements
---------------------

* MAX17320 Wizard - available on analog.com

Install Tools
--------------

- Download and install the  MAX17320 Evaluation GUI available on analog.com. 

Hardware Setup
--------------

In order to ensure communication between the computer, which is running the Configuration Wizard, and the fuel-gauge chip on the board,
the solder jumpers highlighted in the image below must be switched from: JP4-5-6 : 3-2 -> 1-2. 
NOTE: After configuring MAX17320, these jumpers must go back to their initial positions , to communicate with the MCU.


.. image:: res/jumpers.png


After configuring the jumpers, the I2C adaptor board needs to be connected to the SWD hearder, that is located close to the on-board display, 
highlighted with red, below. 

.. image:: res/i2cswd.png


Finally, you need to have your battery pack connected, so the chip and GUI can draw proper measurements. 

Software Setup
--------------

After installing the MAX17320 Evaluation software, follow along the process as shown in the images below. 

.. image:: res/1.png

.. image:: res/2.png

.. image:: res/3.png

.. image:: res/4.png

.. image:: res/5.png

.. image:: res/6.png

.. image:: res/7.png

.. image:: res/8.png

.. image:: res/9.png

.. image:: res/10.png

.. image:: res/11.png

.. image:: res/12.png

.. image:: res/13.png

.. image:: res/14.png
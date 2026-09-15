.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0537

.. _eval-adicup3029 reference_designs demo_cn0537:

Smoke Detector Demo (w/ EVAL-CN0537-ADRZ)
=========================================

The **ADuCM3029_demo_cn0537** project provides a solution to implement a smoke
detector with the capability to pass **UL-217 specification**, using the
**EVAL-CN0537-ARDZ** and the **EVAL-ADICUP3029**. The Arduino shield uses a
**ADPD188BI** to control the LEDs and photodiodes, a temperature sensor for
compensation, heater resistors to correct condensation and an SD card adapter to
log operation data when not attended by a user terminal. The program can be
controlled using a **UART** **CLI**.

General Description/Overview
----------------------------

The **ADuCM_demo_cn0537** project uses **EVAL-CN0537-ARDZ** and
**EVAL-ADICUP3029** to provide an **UL-217 compliant** solution to smoke
detection. The application gives user access to the **ADPD188BI** registers and
other software defined application parameters to get smoke data at the desired
rate and use it to calculate the **Power Transfer Ratio (PTR)** that directly
correlates to the amount of smoke in the chamber. The alarm algorithm then takes
the **PTR measurement** and measures it against a calculated baseline to
determine if the alarm should trigger or not.

The application has two main stages:

#. Initialization
#. Main process

In the initialization process the software modules and part drivers are
instantiated and set to initial values.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0537_initialization.png

The application initializes the **CLI** process on top of the **UART core** and
then sets up the **ADPD188BI** for smoke detection measurements. The program
then reads calibration data from the part and uses them to set up the **PTR
measurements**. After the **PTR measurements** are ready the application
initializes the algorithm. This process may take a few seconds to complete. The
application finishes initialization by setting up **temperature compensation**
and real time clock counter. The main process is then started in **idle mode**.

The main process has two modes of operation: **idle** and **streaming**. In **idle mode** the serial **CLI** may be used to alter functionality parameters like **ADPD188BI** registers and output data rate. The **CLI** can also be used to set up **SD card logging** by creating a file on it. .. note::

   Note that for the log to be complete, the file opened on the card must also be closed for the data to be saved.

Using the **"stream"** command the process switches to **streaming mode** where
smoke data is taken out at the set sampling rate. After **temperature
compensation** and **PTR calculation**, data is fed to the algorithm to
determine the alarm state. If the alarm is triggered the buzzer is activated and
the alarm can only be reset by pressing the button on the shield or calling the
**"reset_alarm"** command on the **CLI**. If working parameters need to be
adjusted, it is recommended to return to **idle mode** by calling the **"idle"**
command and adjusting as necessary and then return to the **stream mode**.

In **streaming mode**, if the serial terminal is connected, the application will
display **temperature compensated** code values or **PTR values** at users"
choice, timestamped. The **timestamp** is in seconds relative to the start of
the application. The alarm state is also displayed on the terminal while
streaming.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-CN0537-ARDZ
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

::

   * {{ :resources:eval:user-guides:eval-adicup3029:reference_designs:aducm3029_demo_cn0537_hex.zip | Smoke Detector Demo Software for UL-217 Standard (.hex file and copyrights) }}

::

   * {{
     :resources:eval:user-guides:eval-adicup3029:reference_designs:aducm3029_demo_cn0537_en14604.zip | Smoke Detector Demo Software for EN-14604 Standard (.hex file and copyrights) }}

Setting up the Hardware
-----------------------

#. Set up the **EVAL-CN0537-ARDZ** as shown in the
   :dokuwiki:`Hardware User Guide </resources/eval/user-guides/circuits-from-the-lab/cn0537#connectors_and_jumper_configurations>`.

#. Connect **EVAL-CN0537-ARDZ** board to the **EVAL-ADICUP3029**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0537_arduino.jpg

#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0537_system_pc.jpg

Programming the Firmware
------------------------

This application software is used with the ADICUP3029 to demonstrate the
capabilities of the CN0537 evaluation board. To upload the CN0537 software to
the ADICUP3029, connect both boards together through the Arduino form factor
connectors (P1 to P4 on the CN0537) and plug them to a computer through USB.

Upon connection, the hardware should appear as a DAPLINK drive on the computer.
Drag and drop the ADuCM3029_demo_cn0537.hex file to the DAPLINK drive to program
the ADICUP3029.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0537/cn0537_uploading_hex_file.png
   :width: 600px

.. admonition:: Download

   Available .hex files for CN0537:

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/aducm3029_demo_cn0537_hex.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/aducm3029_demo_cn0537_en14604.zip`

Outputting Data
---------------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-serial-terminal-setup
   :end-before: .. end-serial-terminal-setup

Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the
list of commands and their short versions. Below is the short command list:

.. list-table::
   :header-rows: 1

   * - Function
     - Command
     - Description
     - Example
   * - Application commands
     -
     -
     -
   * -
     - *h*
     - Display available commands.
     -
   * -
     - *s*
     - Put the device in GO mode and stream data from the device to the
       terminal.
       <*no*> = number of samples to be displayed. If not specified stream indefinitely. After the selected number of samples have been streamed the device will still sample, but not output data.
     -
   * -
     - *i*
     - Stop the stream.
       <*opt*> = 1 to put the program in idle mode, 0 to keep the program in streaming mode, but stop streaming.
     -
   * -
     - *ms*
     - Set the output mode.
       <*opt*> = "CODE" to stream data in codes; "PTR" to stream PTR data.
     -
   * -
     - *os*
     - Set output data rate. <*odr*> = new sample rate.
     - os 2.45 = set sample rate to 2.45 samples per second.
   * -
     - *og*
     - Get current output data rate.
     -
   * -
     - *ra*
     - Stop the alarm if triggered.
     -
   * -
     - *n*
     - Insert a note into the stream and also the SD card log if started.
     - n Note 1 = print "Note 1" on th terminal stream and SD card log if
       started.
   * -
     - *ar*
     - Redo initialization of the algorithm. Useful if conditions changed significantly since start of the program.
     -
   * -
     - *hc*
     - Heater resistors control.
       <*opt*> = 1 to turn heater resistors on; 0 to turn the heater resistors off.
     -
   * - SD card commands
     -
     -
     -
   * -
     - *fo*
     - Open a file on the SD card. If the file does not exist it is created.
       If the file exists and has information the new information will be
       appended.
       <*name*> = name of the file to be opened.
     - fo file1 = a file named "file1.txt" is opened on the card.
   * -
     - *fc*
     - Close the last file open on the SD card. This also saves the latest content to memory.
     -
   * - Device commands
     -
     -
     -
   * -
     - *rr*
     - Read device register.
       <*addr*> = address of the register to be read in hexadecimal.
     - rr a = read register 0xA
   * -
     - *rw*
     - Write device register.
       <*addr*> = address of the register to be read in hexadecimal.
       <*val*> = value to be written to the register in hexadecimal.
     - rw a 12c = write 0x12C to register 0xA
   * -
     - *rd*
     - Read and display all device registers in one command.
     -

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0537_putty_update.png

UL-217 Testing Results
----------------------

Using both the EVAL-CN0537-ARDZ and the EVAL-CN0537-ALGO (now referred as
ADSW-SMOKEALGO-PRODLIC), the setup was tested at a certified testing facility
(Intertek) and passed all the smoke sensor aspects of the UL-217 8th Ed.
standards. You can view the entire report here.

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0357/intertek_test_report_on_eval-cn0537-algo.pdf`



.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis16227-pc-eval

.. _inertial-mems imu adis16227-pc-eval:

ADIS16227 EVALUATION ON A PERSONAL COMPUTER
===========================================

The
:dokuwiki:`Vibration Evaluation Program </resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>`
enables PC-based evaluation of the :adi:`ADIS16227CMLZ <ADIS16227>`, using the
following hardware:
:adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`
breakout board and :adi:`EVAL-ADIS` evaluation system. Please the following
picture for an example of how to use these two devices together for this
purpose.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-eval-adis-setup.png
   :width: 300px

PART NUMBERS TO ORDER
=====================

:adi:`Click here to start the online ordering process <en/mems-sensors/mems-accelerometers/adis16227/products/product.html#product-samples>`
for the following two parts, or contact your ADI distributor to place the order.

:adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`

:adi:`EVAL-ADISZ <EVAL-ADIS>`

SOFTWARE TO DOWNLOAD
====================

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram.rst

   :start-after: .. start-vibration-evaluation-program-download
   :end-before: .. end-vibration-evaluation-program-download

PC SYSTEM REQUIREMENTS
======================

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram.rst

   :start-after: .. start-pc-system-requirements
   :end-before: .. end-pc-system-requirements

ADIS16227/PCBZ CONTENTS & SETUP
===============================

The
:adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`
kit comes with the following materials: (1) ADIS16227CMLZ, (1) interface PCB,
(10) M2x0.4x6mm machine screws and (1)10-32 x 3/8`` flat socket head screw.

Installing the :adi:`ADIS16227CMLZ <ADIS16227>` onto the interface PCB requires
two simple steps:

**Step #1**

Secure the :adi:`ADIS16227CMLZ <ADIS16227>` to the interface board, using the
10-32 x 3/8`` flat socket head machine screw.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-mnt-with-10-32-screw.png
   :width: 300px

**Step #2**

Insert the :adi:`ADIS16227CMLZ's <ADIS16227>` flex connector into the mating
connector on the interface board, then close the clasp to secure the connection.
For more details on this process, please
:ez:`click here to see a video demonstration <docs/DOC-2672>`

EVAL-ADISZ SETUP
================

Use the following two steps to configure the :adi:`EVAL-ADISZ <EVAL-ADIS>` for
use with the :adi:`ADIS16227/PCBZ <ADIS16227>`:

**Step #1**

Connect J1 on the :adi:`EVAL-ADISZ <EVAL-ADIS>` to J1 on the
:adi:`ADIS16227/PCBZ <ADIS16227>`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-j1-cable.png
   :width: 300px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-eval-adis-setup.png
   :width: 300px

NOTE: The ribbon cable in this example is not included with the :adi:`EVAL-ADIS`
or :adi:`ADIS16227/PCBZ <ADIS16227>`. For more information on where to acquire
these types of cables,
:ez:`Click here <mems/w/documents/4496/faq-adis16228-pcbz-breakout-board-cables>`.

**Step #2**

Set JP1 to +3.3V

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-jp1-setting-02.jpg
   :width: 300px

USB DRIVER INSTALLATION
=======================

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram.rst

   :start-after: .. start-usb-driver-installation
   :end-before: .. end-usb-driver-installation

VIBRATION EVALUATION PROGRAM OVERVIEW
=====================================

This section provides a basic description of the functions in the Vibration
Evaluation Software package. For a list of
:dokuwiki:`ADIS16227-specific tutorials <#adis16227_evaluation_tutorials>` that
provided detailed, step-by-step instructions for the most common
:adi:`ADIS16227` evaluation functions, please
:dokuwiki:`click here <#adis16227_evaluation_tutorials>`.

LAUNCH SOFTWARE
===============

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram.rst

   :start-after: .. start-launch-software
   :end-before: .. end-launch-software

Device Selection
----------------

Click on **Device**, located on the left hand side of the Menu bar, at the top
of the **Main Screen**, to select the appropriate DUT (Device Under Test). In
this example, the :adi:`ADIS16227` is in use. Note that some of the Menu bar
options appear in a lighter gray color, to indicate that they are not associated
with a particular device. For example, all of the **Network** options presently
only apply to the :adi:`ADIS16229` at this time, so they will appear in the
lighter gray color when either :adi:`ADIS16227` or [adi>adsi16228|ADIS16228]]
options are in use.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_deviceselection_01.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-select.png
   :width: 600px

Register Access
---------------

The **Register Access** option on the **Menu Bar** provides direct read and
write access to all of the user-accessible registers in DUT.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_registeraccess_01.png
   :width: 600px

Register Access Window Appearance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example of the **Register Access** window that illustrates the
:adi:`ADIS16228`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_01.png
   :width: 600px

Reading Register Contents
~~~~~~~~~~~~~~~~~~~~~~~~~

Select a specific register to read the contents.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-registers.png
   :width: 600px

Writing Data to Registers
~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following two steps to write a value to the register. 1. Enter the hex
code for the register.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-reg-new-hex-value.png
   :width: 600px

2. Click on **Write**

NOTE: Clicking on **Write** causes the Vibration Evaluation Program to write to
both upper and lower bytes

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-reg-write.png
   :width: 600px

Single-Command Options
~~~~~~~~~~~~~~~~~~~~~~

The vibration sensor products often come with registers that support ``Global
Commands.`` While these commands are associated with specific bits, located in
user-accessible registers, the right side of the **Register Access** Window
provides access to them through a drop down menu that offers each related
register and a series of **Write** buttons.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-glob-comm-button.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-glob-cmd-writes.png
   :width: 600px

Network
-------

Coming soon…..

Alarms
------

The **Alarm > Alarm Settings** option on the **Menu Bar** provides a more
convenient method for configuring the Spectral Alarm functions. This provides a
more convenient method for tuning this function, in comparison with the
single-register access method associated with **Register Access** window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-start.png
   :width: 600px

Selecting **Alarms > Alarm Settings** will cause the following window to open:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_01.png
   :width: 600px

Select boxes in the matrix and enter values that are associated with the
magnitude of the output data and FFT bin numbers.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_02.png
   :width: 600px

Click on **Write to DUT** to update all registers that are associated with these
entries.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_03.png
   :width: 600px

Close this window, then go back in. The values will not appear automatically.
Click on **Read from DUT** to make sure the settings are still in place.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_04.png
   :width: 600px

The **Alarms > Alarm Status Form** option provides a convenient monitor for the
conditions. The dashes will change to green (no alarm), yellow (``warning``
alarm, associated with Level 1) or red (``critical`` alarm, associated with
Level 2), depending on the conditions, after a data capture event completes.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_statusform_01.png
   :width: 400px

Data Capture
------------

The **Data Capture** window provides user inputs for file location, base file
name and for resetting the file count.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-data-cap.png
   :width: 500px

When this function is active (See the
:dokuwiki:`Enable Data Capture checkbox </resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram#enable_data_capture>`,
located in the **Main Screen**), each trigger will cause the creation of a new
file that contains the FFT result and FFT Header information. Notice the
increments in the file count, after three clicks on the **Start** button.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-datalog-file.png
   :width: 600px

This counter is also in the **Data Capture Window**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-data-file-cnt.png
   :width: 500px

Tools
-----

The **Tools** option in the **Menu Bar** offers two options: **USB** and
**SPI**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-tools-menu.png
   :width: 600px

Use the **USB** option to manually connect or disconnect to the USB port on the
:adi:`EVAL-ADIS`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_01.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_02.png
   :width: 400px

Use the **SPI** option to adjust the timing in between the :adi:`EVAL-ADIS` and
the DUT. this should not be required for normal operation but the ``typical``
settings are offered in the following picture:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-spi-utilities.png
   :width: 400px

Demo
----

Visit the
:dokuwiki:`ADIS16229 Vibration Demo Wiki Guide <resources/eval/user-guides/inertial-mems/imu/vibrationdemo>`
for more details on this function.

About
-----

This option offers the revision and some codes that might be useful when seeking
technical support.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-version-1-2.png
   :width: 400px

Data Collection Mode
--------------------

The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic
modes of data collection: manual time domain, manual FFT, automatic FFT and
automatic time domain. Inside of these products, these modes are typically
related to the settings in the REC_CTRL1 register. The **Main Screen** offers a
drop-down selection menu for these modes, along with a **Start** button to begin
operation. At this time, only use the **Manual FFT** or **Manual Time Domain**
modes in the **Main Screen**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-man-fft.png
   :width: 600px

Waveform Display
----------------

The **Waveform Display** enables quick access to sensor data.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px

KEY PROGRAM FEATURES
====================

The follow sections provide a basic description of each function inside of the
Vibration Evaluation Program.

:dokuwiki:`Click here to access a list of ADIS16228 Tutorials with the Vibration Evaluation Program <[/resources/eval/user-guides/inertial-mems/imu/adis16228-pc-eval#adis16228_evaluation_tutorials>`

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram.rst

   :start-after: .. start-program-features
   :end-before: .. end-program-features

ADIS16227 EVALUATION TUTORIALS
==============================

For specific, step-by-step instructions for evaluating the :adi:`ADIS16227`,
click on the following tutorials. Please note that this is under construction.
These tutorials will update often. For specific tutorial requests, please post
them in the :ez:`MEMS Community, inside of the Engineer Zone <community/mems>`.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-regaccess_01.pdf`

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_singlesrx_01.pdf`

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_foursrx_01.pdf`

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_singlesrx_alarms_01.pdf`

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_multisrx_alarms.pdf`

**Future Tutorials**

ADIS16228 FFT Records Demo, using Data Capture

Manual FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Manual FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

Periodic FFT Mode, Single Sample Rate

Periodic FFT Mode, Single Sample Rate, with Alarms

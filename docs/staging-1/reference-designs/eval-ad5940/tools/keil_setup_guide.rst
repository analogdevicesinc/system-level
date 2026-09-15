.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad5940/tools/keil_setup_guide

.. _eval-ad5940 tools keil_setup_guide:

How to setup and use Keil IDE
=============================

The AD5940 SDK provides support for Keil IDE to develop firmware. Keil provides
an evaluation licence that is free but limits the code size to 32 kB. Currently,
none of the evaluation examples in the AD5940 development pack exceed this.

How to Download Keil
--------------------

To download Keil IDE click on the following link
https://www.keil.com/demo/eval/arm.htm

This will open up a form which must be filled out to download the software.
Click Submit when complete to begin the download process. Once the software has
downloaded an evaluation licence is required. Keil offers two different
evaluation licences, time limited and size limited. Choose the size limited
licence. This limits the allowable code size to 32kB. All the AD5940 example
projects are within this limitation.

The latest versions of Keil use the ARM compiler v6, but the example code still
uses v5, and refuses to compile under v6. Therefore, you will also need to
download the legacy compiler, and install it at the correct location (not the
default location), as shown in
https://developer.arm.com/documentation/ka005073/latest

How to edit and run example code in Keil
----------------------------------------

To edit and run example code in Keil follow these steps:

#. Download the AD5940 SDK from the the GitLab repository:

.. admonition:: Download

   `AD5940 SDK Source Code <https://github.com/analogdevicesinc/ad5940-examples>`__

*(*\ **Hint:** *Also download the included submodule in examples/ad5940lib. This
can be done with the git bash in one step by executing: ``git clone
–recurse-submodules :git-ad5940-examples.git`` (without the double quotes))*

#. Navigate to the **examples->AD5940_ADC->ADICUP3029**
#. Double click on ADICUP3029.uvprojx file to open the project in Keil [The
   package at https::`/github.com/analogdevicesinc/ad5940-examples+` doesn"t
   contain ADICUP3029.uvprojx in **examples->AD5940_ADC->ADICUP3029** or other
   folders]
#. The project structure is shown in the left hand side of the screen. It is
   divided into 4 sub sections:

- AD5940Lib - This contains the AD5940.c source file which has all the AD5940
  library functions. This file is common to all examples. The ADICUP3029Port.c
  file is located here also and contains port functions for the ADuCM3029
  microcontroller.
- Application - This sub section contains the application code and main.c file.
- CMSIS - This contains the arm CMSIS math library.

- Device - This folder contains the startup code for the ADuCM3029
  micrcontroller. These files should not be modified.

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/keil_adc.png
    :width: 600px

#. Double click on AD5940_ADCPolling.c to open the file in the editor.
#. Modify code as required.
#. To compile and build the project go to **Project->Rebuild all target files**.
   It may take a couple of seconds to fully compile all the source code.
#. If you see build errors like "Fatal Error[Pe1696]: cannot open source file
   ``adi_cycle_counting_config.h``", you need to add/adjust include paths:

- Click Menu > Project > Options > C/C++ Compiler > Preprocessor > Additional
  include directories (click on the three dots on the right)
- Click on "<Click to add>"
- Find the file on your computer and add it, e.g. navigate to (and then select):
  "C:\\ad5940-examples\\examples\\AD5940_BATImpedance\\ADICUP3029\\RTE\\Device\\ADuCM3029" (adjust the path depending on where you stored the example folder, which example project you use and which include file is missing)
- Click OK twice, then Menu > Project > Clean
- Click Menu > Project > Rebuild All

#. To download the code to the evaluation boards first ensure the boards are
   connected to the PC or laptop. Then click on the red icon in the toolbar to
   download the source code and begin the debugging session.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/keil_debug.png
      :width: 600px

#. To set breakpoints click to the left of the line of code. A red dot will
   appear as in below screenshot.

#. To begin executing press the ``Run`` button which is highlighted in below
   screenshot.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/keil_debugger.png
      :width: 600px

#. Hint: If downloading the code didn"t work because of an error like this:
   "Failed to load flash loader:
   C:/Users/YourUsername/IAR-CMSIS-Packs/AnalogDevices/ADUCM302x_DFP/3.2.0/\\ARM\\config\\flashloader\\AnalogDevices\\FlashADUCM3029.flash":

- Try this method instead:
  https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/tools/adicup3029_hw_drivers#daplink_drive
- If your board doesn"t start after this, give flashing/debugging using the
  steps described above another try - sometimes it works again.

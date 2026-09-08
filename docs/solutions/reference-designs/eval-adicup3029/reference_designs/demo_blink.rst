Blink LED Demo
==============

The **ADuCM3029_Blink** is a Blink LED demo project for the **EVAL-ADICUP3029** base board which is created using the Analog Devices Cross Core Embedded Studio.

General Description/Overview
----------------------------

The **ADuCM3029_Blink** project uses :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adicup3029.html>` which is an Ultra Low Power, Arduino compatible ARM Cortex M3 based platform. The platform support various sensor shields.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)

Setting up the Hardware
-----------------------

No specific hardware setup required for this demo

Configuring the Software
------------------------

No specific configuration required for this demo

Outputting Data
---------------

This example blinks the DS3 (green) and DS4 (red) LEDs on the EVAL-ADICUP3029 board. The example blinks the two LEDs in a binary count pattern. The test runs for a fixed number of iterations before exits. **All Done** message is printed on to console once program exits.

Obtaining the Source Code
-------------------------

The source code and include files of the **ADuCM3029_Blink** demo can be found here:

.. admonition:: Download
   :class: download

   :git-no-OS:`no-OS/tree/master/projects/aducm_blinky_example <projects/aducm_blinky_example>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

*End of Document*

ADuCM302x Device Family Pack (DFP)
==================================

General Description/Overview
----------------------------

The ADuCM302x Device Family Pack (DFP) provides access to all the necessary on-chip peripheral drivers for both the :adi:`ADuCM3029` and the :adi:`ADuCM3027` devices. This software layer is the foundation layer needed when writing applications using this microprocessor family. When combined with the ADICUP3029 software pack as well as the Sensors software pack, there are many great Internet of Things(IoT) applications and demos that can be replicated using the ADICUP3029 development platform.

The following on-chip drivers are provided as part of the ADuCM302x Device
Family Pack:

-  spi

.. image:: ../images/software_packs_aducm302x_device_block_diagram.png
   :align: right
   :width: 600

-  i2c
-  uart
-  sport
-  beep
-  wdt
-  gpio
-  rtc
-  dma
-  cryto
-  adc
-  tmr

For detailed information regarding the ADuCM302x DFP, please see our complete
ADuCM302x software user guide.

.. hint::

   `ADuCM302x DFP Release Notes <http://download.analog.com/tools/EZBoards/CM302x/Releases/Release_3.2.0/ADuCM302x_DFP_3.2.0_Release_Notes.pdf>`_

.. important::

   You MUST have this software package installed on your laptop or PC in order
   to compile, debug, and run the applications for the ADICUP3029 platform.

Downloading the ADuCM302x Software Pack
---------------------------------------

The software pack can be installed directly by the tool chain's CMSIS pack
manager. Optionally, you may download and then use the CMSIS pack manager's
manual installation to install the pack.

-  Downloaded via the tool chain's CMSIS pack manager

   -  It is **recommended** to download the ADuCM302x software pack through from the tool chain's CMSIS pack manager. That way, all the files, directories structure, and project structure for the various applications is properly saved and accessed. For a detailed description on how to download the ADuCM302x software pack through CrossCore Embedded Studio please see our :doc:`CrossCore Embedded Studio Quickstart User Guide </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`.

-  Downloaded to local directory

   -  However if you do decide to download the ADuCM302x software pack to your
      PC/laptop directly, please use the link below to download the pack file
      from Keil's website. You will then need to "import" the pack file using
      your tool chain's CMSIS pack manager's import feature. Note that all
      software packs can be downloaded from Keil's website.

.. admonition:: Download
   :class: download

   `ADuCM302x DFP 3.2.0 <http://download.analog.com/tools/EZBoards/CM302x/Releases/AnalogDevices.ADuCM302x_DFP.3.2.0.pack>`_

*End of Document*

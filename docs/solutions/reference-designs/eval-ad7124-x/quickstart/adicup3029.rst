.. _eval-ad7124-x quickstart adicup3029:

EVAL-ADICUP3029 Quick Start
===============================================================================

.. esd-warning::

This guide describes how to use the :adi:`EVAL-AD7124-8-PMDZ` Pmod board with
the :adi:`EVAL-ADICUP3029` development platform using the
**ADuCM3029_demo_ad7124_8PMDZ** demo project.

The demo provides a CLI-based interface to control the :adi:`AD7124-8` ADC,
showcasing the flexibility of the AD7124 in choosing inputs, filters, and
different ranges for the available 16 channels.

General description
-------------------------------------------------------------------------------

The initial configuration engages all inputs in a mix of differential and
single-ended channels:

- Channels 0--7: AIN0/AIN1, AIN2/AIN3, ..., AIN14/AIN15 (differential)
- Channels 8--15: AIN0/AGND, AIN1/AGND, ..., AIN7/AGND (single-ended)

By default only channel 0 is active, but this can be adjusted using the
CLI commands described below. All channels initially use configuration
register 0 (sinc4 filter, widest PGA range, maximum sample rate).

Prerequisites
-------------------------------------------------------------------------------

See :ref:`eval-ad7124-x prerequisites` for the full list.

**Hardware:**

- :adi:`EVAL-AD7124-8-PMDZ`
- :adi:`EVAL-ADICUP3029`
- Micro USB to USB cable
- PC or laptop with a USB port

**Software:**

- :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ demo application <master:projects/ADuCM3029_demo_ad7124_8PMDZ>`
- CrossCore Embedded Studio (2.9.1 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Serial terminal program (e.g., PuTTY, Tera Term)

Setting up the hardware
-------------------------------------------------------------------------------

#. Connect the :adi:`EVAL-AD7124-8-PMDZ` board to the Pmod connector on the
   :adi:`EVAL-ADICUP3029`.

   .. figure:: ../images/ad7124_pmod_unplug.jpg
      :alt: EVAL-AD7124-8-PMDZ and EVAL-ADICUP3029 before connection
      :align: center
      :width: 500

      EVAL-AD7124-8-PMDZ and EVAL-ADICUP3029 before connection

#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer. The final setup should look similar to the picture
   below.

   .. figure:: ../images/ad7124_pmod_plug.jpg
      :alt: EVAL-AD7124-8-PMDZ connected to EVAL-ADICUP3029
      :align: center
      :width: 500

      EVAL-AD7124-8-PMDZ connected to EVAL-ADICUP3029

Serial terminal setup
-------------------------------------------------------------------------------

A serial terminal is used to interact with the demo firmware over USB. The
default serial settings are:

- **Baud rate:** 115200
- **Data bits:** 8
- **Parity:** None
- **Stop bits:** 1
- **Flow control:** None

Example setup using PuTTY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Plug in the EVAL-ADICUP3029 using a micro-USB cable.
#. Wait for the device driver to install on your PC.
#. Open Device Manager and find the assigned COM port.

   .. figure:: ../images/device_manager.png
      :alt: Windows Device Manager showing COM port
      :align: center
      :width: 400

      Windows Device Manager showing COM port

#. Open PuTTY and configure the serial settings:

   .. figure:: ../images/putty_serial_config.png
      :alt: PuTTY serial configuration
      :align: center
      :width: 400

      PuTTY serial configuration

#. Under the Terminal category, enable **Implicit CR in every LF** and
   **Implicit LF in every CR**. Enable local echo and line editing.

   .. figure:: ../images/putty_terminal_options.png
      :alt: PuTTY terminal options
      :align: center
      :width: 600

      PuTTY terminal options

#. Click **Open** to start the terminal session.

Available commands
-------------------------------------------------------------------------------

Type **help** or **h** after the initial calibration sequence to display the
list of available commands.

.. csv-table:: Available Commands
   :file: ../files/available-commands.csv

.. figure:: ../images/ad71248pmdz_terminal_sample.png
   :alt: Terminal output sample showing AD7124-8 PMDZ demo
   :align: center
   :width: 600

   Terminal output sample

Obtaining the software
-------------------------------------------------------------------------------

There are two ways to program the EVAL-ADICUP3029:

#. **Drag and drop** the prebuilt .Hex file to the DAPLINK USB drive (easiest
   method for quick evaluation)
#. **Build from source** using CrossCore Embedded Studio (allows customization)

.. admonition:: Download

   Prebuilt AD7124-8 Pmod Hex File:

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ.hex <releases/download/Latest/ADuCM3029_demo_ad7124_8PMDZ.hex+>`

   Complete AD7124-8 Pmod Source Files:

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ Source Code <projects/ADuCM3029_demo_ad7124_8PMDZ>`

How to use the tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The official tool for use with the EVAL-ADICUP3029 is CrossCore Embedded
Studio. For more information on downloading the tools and a quick start guide,
see the
:doc:`Tools Overview page </solutions/reference-designs/eval-adicup3029/tools>`.

For importing existing projects, see
:doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`.

For configuring debug sessions, see
:doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`.

Project structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application contains the platform drivers with sources in
**platform_source** and headers in **platform_include**. In the **src** root
directory there is the AD7124 driver as found on GitHub, but with a custom
initialization vector in the **ad7124_regs** module.

.. figure:: ../images/ad7124pmdz_file_structure.png
   :alt: AD7124 PMDZ project file structure
   :align: center
   :width: 300

   AD7124 PMDZ project file structure

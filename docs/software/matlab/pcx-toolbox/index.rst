Precision Toolbox
===============================================================================

.. note::

   This section only gives an overview on the Precision Toolbox, for all
   details, see
   :external+PrecisionToolbox:doc:`the dedicated doc <index>`.

Analog Devices Precision Toolbox For MATLAB and Simulink is a set of tools to
model, interface, and target with ADI precision devices within MATLAB and
Simulink. These are combined into a single Toolbox which contains a set of Board
Support Packages (BSP). The list of supported converters is provided :ref:`below
<pcx-toolbox supported boards>`.

Quick Start with Toolbox
-------------------------------------------------------------------------------

The current stable Toolbox can be downloaded from the :git-PrecisionToolbox:`releases+`.
Download the latest .mltbx file then open that file within MATLAB. Opening the
file will automatically install the Toolbox, adding the necessary components to
your MATLAB path. The "Analog Devices, Inc. Precision Toolbox" will appear in
your :mw:`Add-Ons Explorer <help/matlab/matlab_env/manage-your-add-ons.html>`
within MATLAB.

.. admonition:: Download
   :class: download

   :git-PrecisionToolbox:`Analog Devices Inc, Precision Toolbox Release Page <releases+>`.

To interface and stream data with hardware will require installation of
:ref:`libiio` and one of two Hardware Support Packages from MathWorks. The
libiio library can be obtained from the :git-libiio:`/`.

Libiio Installers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   Stable releases are available at :git-libiio:`releases+`.

These support packages provide the necessary libIIO MATLAB bindings used by
ADI's system objects. Starting in R2024a, the functionality of Communications
Toolbox Support Package for Xilinx Zynq-Based Radio is included in SoC Blockset
Support Package for AMD Devices.

.. admonition:: Download

   | For releases after R2024a:
   | :mw:`SoC Blockset Support Package for AMD FPGA and SoC Devices <matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`
   | For Releases R2023b and before, either:
   | :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <matlabcentral/fileexchange/48491-communications-toolbox-support-package-for-xilinx-zynq-based-radio>`
   | :mw:`Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <help/supportpkg/plutoradio/index.html>`

.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They
   are not used.
   See :external+kuiper:doc:`Kuiper documentation <index>` for the FPGA
   carrier board SD card images.

Toolbox Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on your needs, different toolboxes will be required. For basic data
streaming into MATLAB or Simulink only the following MathWorks toolboxes are
required:

-  :mw:`Communications Toolbox <products/communications/>`
-  :mw:`DSP System Toolbox <products/dsp-system/>`
-  :mw:`Signal Processing Toolbox <products/signal/>`
-  :mw:`SoC Blockset <products/soc.html>`
-  :mw:`SoC Blockset Support Package for AMD FPGA and SoC Devices (FREE) <matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`

For HDL code generation the following are required:

-  :mw:`HDL-Coder <products/hdl-coder>`
-  :mw:`Xilinx Zynq Support from HDL Coder (FREE) <hardware-support/zynq-hdl-coder>`

Building the Toolbox Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The toolbox can only be built under Linux or with Cygwin on a Windows platform.
Conveniently, the entire process is automated with a Makefile located in the
CI/scripts folder of the repository. The following is required on the system
before the build process can be run:

-  A supported MATLAB version installed in the default location
   (/usr/local/MATLAB)
-  Packages: git zip unzip tar make wget sed

.. warning::

   You should only manually build the toolbox if you require a custom branch or
   no toolbox installer is available

First clone the repo and move into it:

.. shell::

   git clone https://github.com/analogdevicesinc/PrecisionToolbox.git
   cd PrecisionToolbox

To build the toolbox run the following:

.. shell::

   make -C CI/scripts build

To create an installable tlbx file run:

.. shell::

   make -C CI/scripts gen_tlbx

Device Control and Data Streaming
-------------------------------------------------------------------------------

Device interfaces which provide control and data streaming are implemented with
MATLAB System Objects and Simulink Blocks. These System Objects can be accessed
under the "adi" namespace in MATLAB and are followed by their part number or
board name and finally Tx or Rx:

.. code-block:: matlab

   adi.<Part or Board Name>.<Tx or Rx>

To get a list of currently available objects with the BSP installed simply run:

.. code-block:: matlab

   help adi

To get more information on a given object run:

.. code-block:: matlab

   help adi.<Part or Board Name>

or

.. code-block:: matlab

   doc adi.<Part or Board Name>

Common Attributes
~~~~~~~~~~~~~~~~~

There are some common attributes that need to be set for system objects and parts.

-  ``uri`` Context address of IIO device.

   -  IP with usage ''bf.uri = 'ip:192.168.2.1' ''

Extending Interfaces
~~~~~~~~~~~~~~~~~~~~

If a driver attribute or setting is not available in the standard objects it can
be easily extended to cover more IIO attributes. See this
:ref:`guide <matlab bsp-extend>`.

Examples
-------------------------------------------------------------------------------

Examples for streaming data and targeting FPGAs are listed within the Toolbox
documentation itself. To view run the following with MATLAB:

.. code-block:: matlab

   doc adi

They can also be viewed on GitHub:

  -  :git-PrecisionToolbox:`Examples <examples>`

.. _pcx-toolbox supported boards:

Supported Boards
-------------------------------------------------------------------------------
The following have device-specific implementations in MATLAB and Simulink. If a
device has an IIO driver, MATLAB support is possible, but a device-specific
MATLAB or Simulink interface may not exist yet.

.. list-table:: Supported Parts
   :header-rows: 1
   :widths: 20 20 20 15 25

   * - Evaluation Card
     - Controller Board
     - Streaming Support
     - Targeting
     - Variants and Minimum Supported Release
   * - AD7380
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7381
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7383
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7384
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7386
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7387
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7388
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7380-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7381-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7383-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7386-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7387-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7388-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - ADAQ4370-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - ADAQ4380-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7768
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7768-1
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4030-24
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4630-16
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4630-24
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - ADAQ4224
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4858
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD2S1210
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4000
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4001
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4002
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4003
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4004
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4005
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4006
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4007
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4008
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4010
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4011
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4020
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4021
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD4022
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD5760
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD5780
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD5781
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD5790
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD5791
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7124-4
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD7124-8
     - Zedboard
     - Yes
     - No
     - ADI (2021b)
   * - AD3530r
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4050
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4052
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4060
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4062
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4170
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD7190
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD7192
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD7193
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD7194
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD7195
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD4190
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD5592r
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD5593r
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD5710r
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)
   * - AD5706r
     - SDP-K1
     - Yes
     - No
     - ADI (2021b)

Further Reading
-------------------------------------------------------------------------------

For more information, check out the
:external+PrecisionToolbox:doc:`dedicated documentation <index>`
which contains useful information such as:

  - :external+PrecisionToolbox:doc:`common/installation`
  - :external+PrecisionToolbox:doc:`common/data_streaming`
  - :external+PrecisionToolbox:doc:`common/limitations`
  - :external+PrecisionToolbox:doc:`reference_api/index`

Help & Support
-------------------------------------------------------------------------------

Questions? :ez:`Ask Help & Support <linux-software-drivers>`.

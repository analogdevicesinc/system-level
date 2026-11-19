RF Microwave Toolbox
===============================================================================

.. note::

   This section only gives an overview on the RF Microwave Toolbox, for all
   details, see
   `the dedicated doc <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/>`_.

Analog Devices RF Microwave Toolbox For MATLAB and Simulink is a set of tools to
model, interface, and target with ADI RF devices within MATLAB and Simulink.
These are combined into a single Toolbox which contains a set of Board Support
Packages (BSP). The list of supported boards is provided
:ref:`below <rf-microwave-toolbox supported boards>`.

Quick Start with Toolbox
-------------------------------------------------------------------------------

The current stable Toolbox can be downloaded from the
:git-RFMicrowaveToolbox:`releases+`. Download the latest mltbx file then open
that file within MATLAB. Opening the file will automatically install the
Toolbox, adding the necessary components to your MATLAB path. The "Analog
Devices, Inc. RF Microwave Toolbox" will appear in your `Add-Ons Explorer
<https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`_
within MATLAB.

.. admonition:: Download
   :class: download

   :git-RFMicrowaveToolbox:`Analog Devices Inc, RF Microwave Toolbox Release Page <releases+>`.

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

The toolbox can only be built under Linux or with Cygwin on a Windows platform. Conveniently, the entire process is automated with a Makefile located in the CI/scripts folder of the repository. The following is required on the system before the build process can be run:

-  A supported MATLAB version installed in the default location (/usr/local/MATLAB)
-  A supported Vivado version installed in the default location (/opt/Xilinx)
-  Packages: git zip unzip tar make wget sed

.. warning::

   You should only manually build the toolbox if you require a custom branch or
   no toolbox installer is available


First clone the repo and move into it:

.. shell::

   git clone https://github.com/analogdevicesinc/RFMicrowaveToolbox.git
   cd RFMicrowaveToolbox

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

For example, to instantiate a Stingray object to control the X-Band Development
Platform it can be created as follows:

.. code-block:: matlab

   bf = adi.Stingray;

The Stingray Evaluation board contains an ADXUD1AEBZ,
:adi:`ADF4371` and :adi:`ltc2314-14`.
Therefore, it uses the objects corresponding to these devices along with
ADAR100x, a generic :adi:`ADAR1000` superclass under the hood. Similarly, ADALM-PHASER
class is also derived from low level objects based on their parts.

For example usage of certain objects, it can be useful to inspect their related
test code which exercises instantiations in different configurations. The available
code is available in the GitHub repo folder
:git-RFMicrowaveToolbox:`here <test>`, where object tests have the naming
convention <Object>Tests.m.

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

   -  :git-RFMicrowaveToolbox:`Examples <rfm_examples>`

.. _rf-microwave-toolbox supported boards:

Supported Boards
-------------------------------------------------------------------------------

The following have device-specific implementations in MATLAB and Simulink. If a
device has an IIO driver, MATLAB support is possible, but a device-specific
MATLAB or Simulink interface may not exist yet.

.. list-table:: Supported Parts
   :header-rows: 1
   :widths: 20 20 20 15 25

   * - Evaluation Card
     - FPGA Board
     - Streaming Support
     - Targeting
     - Variants and Minimum Supported Release
   * - ADALM-PHASER
     - NA
     - Yes
     - No
     - ADI (2021b)
   * - Stingray
     - ZCU102
     - Yes
     - No
     - ADI (2021b)

Further Reading
-------------------------------------------------------------------------------

For more information, check out the
`dedicated documentation <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/>`__
which contains useful information such as:

   - `Installation <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/install/>`_
   - `Data Streaming <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/streaming/>`_
   - `Reference API <https://analogdevicesinc.github.io/RFMicrowaveToolbox/main/sysobjects/adi.Stingray/>`_

Help & Support
-------------------------------------------------------------------------------

Questions? :ez:`Ask Help & Support <sw-interface-tools>`.

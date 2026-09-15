.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp

.. _ad-fmcomms2-ebz software matlab_bsp:

Analog Devices BSP for MathWorks HDL Workflow Advisor
=====================================================

.. warning::

   MATLAB and Simulink support have been migrated to the new ADI Toolboxes. This
   page is kept for legacy reasons. Please migrate to the new
   :dokuwiki:`Transceiver Toolbox </resources/tools-software/transceiver-toolbox>`

The Analog Devices BSP for MathWorks HDL Workflow Advisor is a collection of
board definitions and reference designs that provide to the MathWorks HDL
Workflow Advisor support to:

- Generate IP blocks compatible with Analog Devices HDL reference designs for
  various Analog Devices platforms
- Automatically insert the generated IPs into the Analog Devices Vivado HDL
  reference designs

The Analog Devices BSP is based on the
:mw:`MathWorks Board and Reference Design Registration System <help/hdlcoder/ug/board-and-reference-design-system.html>`.

Supported platforms
-------------------

- :dokuwiki:`PicoZed SDR <resources/eval/user-guides/picozed_sdr>`
- :adi:`AD-FMComms2-EBZ`
- :adi:`AD-FMComms3-EBZ`
- :adi:`AD-FMComms5-EBZ`

Functionality
-------------

The
:mw:`MathWorks HDL Workflow Advisor <help/hdlcoder/examples/getting-started-with-hardware-software-codesign-workflow-for-xilinx-zynq-platform.html>`
enables users to automatically generate HDL code from a Simulink model. The user
can choose from a selection of several different Target Workflows, including
``ASIC/FPGA``, ``FPGA-In-The-Loop``, and ``IP Core Generation``. Target Platform
selections include Xilinx Evaluation Boards and Altera Evaluation Boards as well
as other custom evaluation boards.

The Analog Devices BSP for HDL Workflow Advisor extends the set of Target
Workflows for IP Core Generation with the Analog Devices boards listed in the
*Supported Platforms* section. The BSP consists of a set of board definitions
that specify all the characteristics needed by the HDL Workflow Advisor to be
able to incorporate a board in the code generation flow, as well as a set of
Xilinx Vivado reference designs that are used by the Workflow Advisor to
automatically insert the generated IPs into the Vivado designs. All the Analog
Devices Vivado HDL reference designs have inside a "donut hole" to accommodate
custom IPs. Each design exposes a set of interface signals to which the IP can
connect to. All these signals are specified in the board definition and are
available in the Workflow Advisor GUI to connect to the generated IP"s ports.

When running the Workflow Advisor the first step if to select the Target
Platform. The figure below shows some of the available Analog Devices target
platforms.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/adi_bsps.png
   :width: 600px

The next step is to configure the interfaces between the IP and the reference
design. Each target platform has a set of interface signals that are accessible
in the *Target Platform Interfaces* drop down boxes form step 1.2 (Set Target
Interface) of the HDL Workflow Advisor. The figure below shows an example of how
to configure the target interface for a specific model.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/board_interface.png
   :width: 600px

All the Analog Devices AD9361 based SDR platforms have the same interface
signals and they are dependent on the type of flow that is selected – receive
(Rx) or transmit (Tx). The table below describes the interface signals for the
AD9361 based SDR platforms.

Receive flow (Rx)
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Signal name
     - Width
     - Description
   * - IP Data 0 OUT
     - 16
     - Custom IP data output signal. This signal is connected to a DMA channel
       in the ADI reference design.
   * - IP Data 1 OUT
     - 16
     - Custom IP data output signal. This signal is connected to a DMA channel
       in the ADI reference design.
   * - IP Data 2 OUT
     - 16
     - Custom IP data output signal. This signal is connected to a DMA channel
       in the ADI reference design.
   * - IP Data 3 OUT
     - 16
     - Custom IP data output signal. This signal is connected to a DMA channel
       in the ADI reference design.
   * - IP Data Valid OUT
     - 1
     - Data valid signal from the custom IP. Used to signal to the rest of the
       design that the IP data out channels have valid data. The duration must
       be 1 clock cycle.
   * - AD9361 ADC Data I0
     - 16
     - AD9361 ADC I0 channel data.
   * - AD9361 ADC Data Q0
     - 16
     - AD9361 ADC Q0 channel data.
   * - AD9361 ADC Data I1
     - 16
     - AD9361 ADC I1 channel data.
   * - AD9361 ADC Data Q1
     - 16
     - AD9361 ADC Q1 channel data.

Transmit flow (Tx)
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Interface signal name
     - Width
     - Description
   * - IP Data 0 IN
     - 16
     - Custom IP data input signal. This signal is connected to a DMA channel in
       the ADI reference design.
   * - IP Data 1 IN
     - 16
     - Custom IP data input signal. This signal is connected to a DMA channel in
       the ADI reference design.
   * - IP Data 2 IN
     - 16
     - Custom IP data input signal. This signal is connected to a DMA channel in
       the ADI reference design.
   * - IP Data 3 IN
     - 16
     - Custom IP data input signal. This signal is connected to a DMA channel in
       the ADI reference design.
   * - IP Load Tx Data OUT
     - 1
     - Custom IP output signal used to notify the design that the IP is ready to
       receive new input data. The duration must be 1 clock cycle.
   * - AD9361 DAC Data I0
     - 16
     - AD9361 DAC I0 channel data. To be used as input into the custom IP.
   * - AD9361 DAC Data Q0
     - 16
     - AD9361 DAC I0 channel data. To be used as input into the custom IP.
   * - AD9361 DAC Data I1
     - 16
     - AD9361 DAC I0 channel data. To be used as input into the custom IP.
   * - AD9361 DAC Data Q1
     - 16
     - AD9361 DAC I0 channel data. To be used as input into the custom IP.

The custom IP always runs at the sample clock and must be able to process /
generate a sample every clock cycle.

Once the target interface has been defined, make sure to select the ``Target
Language`` as Verilog (defaults to VHDL) in Step 3.1.1 of the HDL Workflow
Advisor. All the other settings of steps 2 and 3 of the HDL Workflow Advisor can
be left in their default state and the project generation process can be started
by running step 4.1 (Create Project). The result of this step is a Vivado
project which has the custom IP core integrated into the Analog Devices HDL
reference design. The bistream for the design can be generated either by running
step 4.4 (Create bistream) or by compiling the generated Vivado Project directly
in Vivado. The project can be found in the *hdl_prj/vivado_ip_project* folder.

MATLAB External mode support
----------------------------

The BSP also enables external mode support for the supported Analog Devices
boards. This enables the Simulink models used for IP core generation to be ran
in External mode and talk to the target hardware running the Analog Devices
Linux distribution.

These are the steps to configure external mode support for Analog Devices
platforms:

#. Use the **AnalogDevices.util.SDUpdater** tool to write to an SD card
   containing the latest ADI Linux image the device tree and uImage files for
   external mode support. To write the new files select the drive which
   corresponds to the SD card, select the appropriate board and just click on
   the *Write SD* button.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/sdupdater.png
      :width: 400px

#. Open the model"s **Configuration Parameters** window by pressing *CTRL-E* in
   the external mode model window.

#. In the **Hardware implementation** settings set the *Hardware Board* to *ZYNQ
   SDR* and the *IP address* to the IP address of the target hardware. The
   Analog Devices platforms are configured by default to get dynamic IP
   addresses. To find the address of your board just type *ifconfig* in a Linux
   terminal on your board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/zynq_sdr_option.png
      :width: 600px

#. In the **Code Generation** settings set the toolchain to *Linaro Toolchain
   4.8*.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/code_generation.png
      :width: 600px

Once all these steps are done the model can be ran in external mode by selecting
the "External" option in the model"s toolbar menu and pressing the **Play**
button.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/external_mode.png
   :width: 600px

Download & Installation
-----------------------

The Analog Devices BSP requires the following dependencies that must be
installed beforehand.

.. admonition:: Download

   :mw:`MathWorks HDL Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40447-hdl-coder-support-package-for-xilinx-zynq-7000-platform>`

   :mw:`Embedded Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40448-embedded-coder-support-package-for-xilinx-zynq-7000-platform>`

The Analog Devices BSP can be downloaded from the Analog Devices github using
the link below.

.. admonition:: Download

   :git-MathWorks_tools:`Analog Devices BSP for MathWorks HDL Workflow Advisor <hdl_wa_bsp+>`

.. important::

   Be sure to use the 2017b branch. ADI is moving towards a new installation
   standard which is used by the master branch.

To install the Analog Devices BSP set the Matlab current folder to the
*/vendor/AnalogDevices* folder found in the location where the BSP was
downloaded and run **AnalogDevices.install** in the MATLAB command window. After
the installation process is complete run **ver** in the MATLAB command window to
list all the installed packages. If the installation was succesfull the *HDL
Coder BSP: Analog Devices Inc, Version 1.01, (R2015b)* should appear in the
packages list.

To uninstall the Analog Devices BSP set the Matlab current folder to the
*/vendor* folder found in the location where the BSP was downloaded and run
**AnalogDevices.uninstall** in the MATLAB command window.

Further Reading
---------------

:adi:`Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio - Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Help & Support
--------------

.. note::

   - Questions?
     :dokuwiki:`Ask Help & Support </resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

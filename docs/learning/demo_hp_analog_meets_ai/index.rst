.. collection:: High-Performance Analog Meets AI
   :subtitle: Data extraction for AI training and inference.
   :image: demo_block_diagram.svg
   :label: demo

   Explore a multi-channel RF modulation recognition workflow.

   system-level:
     - .

DEMO High-Performance Analog Meets AI
===============================================================================

Extracting data from high-performance, high-data-rate analog signal chains for
AI model training and real-time inference presents significant challenges due to
the complexity of interfaces, processing, and integration requirements. Analog
Devices addresses these challenges by providing a comprehensive, open-source
data extraction and integration software stack, which ensures seamless
connectivity between advanced signal chains and high-performance compute
platforms.

Resources
-------------------------------------------------------------------------------

- HDL branch:       :git-hdl:`adrv9009_qsfp_10G <adrv9009_qsfp_10G:>`
- Linux branch:     :git-linux:`adr9009zu11eg_100MHZ_qsfp <adr9009zu11eg_100MHZ_qsfp:>`
- Corundum branch:  `corundum <https://github.com/ucsdsysnet/corundum.git>`__
- PyADI-IIO branch: :git-pyadi-iio:`jupiter_modulation <jupiter_modulation:>`

Block diagram
-------------------------------------------------------------------------------

.. figure:: demo_block_diagram.svg
   :align: center
   :width: 900

Demo description
-------------------------------------------------------------------------------

This demo illustrates an AI-based multi-channel RF modulation scheme recognition
workflow for signal intelligence applications. Four AD-JUPITER-EBZ systems are
used to generate RF signals with different modulation schemes across a total of
eight channels. The signals are then digitized by two ADRV9009-ZU11EG SoMs,
which stream the raw IQ data to a host PC via 10Gb Ethernet links. The AI model,
derived from a MathWorks reference design, is deployed on the NVIDIA GPU hosted
in the PC. The NVIDIA Holoscan AI infrastructure manages the efficient transfer
of data from the network interfaces into GPU memory, where the AI model is
executed. By combining ADI’s high-performance data extraction infrastructure
with MathWorks development tools and NVIDIA deployment frameworks, the system
enables efficient AI application development and real-time execution for
advanced signal intelligence tasks.

.. figure:: demo_description.svg
   :align: center
   :width: 600

System Capabilities
-------------------------------------------------------------------------------

The system demonstrates an advanced, end-to-end data extraction and AI-based
signal processing workflow designed for high-performance signal intelligence
applications. It combines Analog Devices’ high-speed RF hardware and data
infrastructure with third-party AI frameworks to deliver real-time modulation
recognition and efficient AI model development.

Key capabilities include:

#. High-Performance Data Extraction

   * Supports real-time acquisition of high-bandwidth RF data from multi-channel
     signal chains.
   * Seamlessly bridges physical interfaces, FPGA-based logic, and low-level
     software drivers to enable reliable data transfer from ADI RF front ends to
     edge processors.
   * Flexible connectivity options, including Ethernet, PCIe, USB, and UART,
     allow integration with a wide range of compute platforms.

#. Real-Time AI Modulation Recognition

   * Demonstrates multi-channel RF modulation scheme classification using AI
     models deployed on NVIDIA GPUs.
   * The NVIDIA Holoscan AI infrastructure ensures efficient data movement
     between network interfaces and GPU memory, supporting low-latency
     inference.

#. Multi-Channel & Multi-Device Synchronization

   * Incorporates multiple AD-JUPITER-EBZ boards and ADRV9009-ZU11EG SoMs to
     generate and digitize RF signals across eight channels.
   * Provides accurate clock distribution and synchronization through
     AD-SYNCHRONA14-EBZ, ensuring deterministic latency and coherent signal
     processing across multiple systems.

#. Seamless Data Integration Stack

   * Enables flexible partitioning of data flow between edge and host compute
     devices, improving scalability and system optimization.
   * Utilizes an open-source ADI software stack that simplifies the setup of
     data collection pipelines for AI model training and real-time inference.

#. Integration with Industry-Standard AI Frameworks

   * Compatible with MathWorks reference designs for AI model generation,
     MATLAB-based workflows, NVIDIA Holoscan, and ROS2.
   * Bridges data science workflows with embedded environments to enable
     real-world dataset generation, model optimization, and deployment.

#. End-to-End AI Development Ecosystem

   * ADI’s AI Fusion tools within CodeFusion Studio™ enable model optimization,
     deployment, and real-time performance analysis.
   * Supports rapid development cycles by providing actionable insights and
     performance metrics for system tuning.

Required Hardware
-------------------------------------------------------------------------------

The following hardware components are required to set up and run the
multi-channel RF modulation recognition demo:

.. list-table::
   :widths: 15 30 5 15
   :header-rows: 1

   * - Component
     - Role
     - Quantity
     - Notes
   * - :dokuwiki:`Jupiter SDR <resources/eval/user-guides/jupiter-sdr>`
     - Versatile 2 x RxTx software-defined-radio platform based on ADRV9002 and
       Xilinx Zynq UltraScale+ MPSoC. Generates RF signals with configurable
       modulation schemes.
     - 4
     - Used to generate 8-channel RF input for AI recognition.
   * - :dokuwiki:`ADRV9009-ZU11EG RF-SOM
       <resources/eval/user-guides/adrv9009-zu11eg>`
     - RF System-on-Module with dual ADRV9009 wideband transceivers. Performs
       high-speed digitization and streaming of IQ data to the host.
     - 2
     - Provides synchronized multi-channel data acquisition.
   * - :dokuwiki:`AD-SYNCHRONA14-EBZ
       <resources/eval/user-guides/ad-synchrona14-ebz>`
     - Clock synchronization and distribution board based on AD9545 and HMC7044.
       Ensures accurate multi-channel phase alignment.
     - 1
     - Synchronizes all RF signal paths and data capture timing.
   * - NVIDIA IGX Orin platform
     - High-performance computing system with NVIDIA GPU acceleration. Runs
       Holoscan AI infrastructure and the AI modulation recognition model.
     - 1
     - Requires 10Gb Ethernet connectivity.
   * - SMA Cables
     - RF connection between the SDR transmit and receive channels.
     - 8
     - High-quality coaxial cables recommended for minimal signal loss.
   * - 100G QSFP28 Active Optical Cable
     - Provides high-speed data connection between the RF-SOM and the host
       compute platform.
     - 1
     - Supports low-latency, high-bandwidth Ethernet link.
   * - Network switch with at least 4 PoE ports
     - Provides Ethernet connectivity and power delivery to connected devices.
     - 1
     - Use a managed switch compatible with 10GbE interfaces.

SD Card Configuration
-------------------------------------------------------------------------------

- For the Jupiter SDR platform, the boot files are generated using the Using
  Kuiper Image:

  :external+kuiper:ref:`Writing the Image to an SD Card
  <use-kuiper-image>`

- For the ADRV9009-ZU11EG, begin by checking out the HDL branch, then navigate
  to the **adrv2crr_fmc** directory.

Run the following command to enable Corundum support and build the design:
**make CORUNDUM=1** Once the build process is complete, generate the necessary
boot files: boot.bin, device tree, and uImage by following the steps:

- BOOT.BIN: :external+hdl:ref:`Build the boot image BOOT.BIN <build_boot_bin>`
- Devicetree: :dokuwiki:`Building the Zynq Linux kernel and devicetrees from
  source <resources/tools-software/linux-build/generic/zynq?s%5b%5d=devicetree>`

Capture in Data Using Scopy2.0
-------------------------------------------------------------------------------

Captured RF Signal in Time Domain

.. figure:: capture_time.jpg
   :align: center
   :width: 900

Captured RF Signal in Frequency Domain

.. figure:: capture_frequency.jpg
   :align: center
   :width: 900

AI Modulation Detection Applications
-------------------------------------------------------------------------------

.. toctree::
   :caption: The following applications are available:
   :maxdepth: 1

   software/index

.. _software jesd-eye-scan:

JESD204 Eye Scan
===============================================================================

About
--------------------------------------------------------------------------------

Validating JESD204B serial links becomes increasingly difficult at higher data
rates. The quality of the line cannot be determined by measuring the far-end eye
opening at the receiver pins with readily available lab equipment. Traditional
oscilloscopes suitable for JESD204B testing require 16-32 GHz bandwidth and cost
over $150,000.

Xilinx 7-Series FPGA GTP transceivers include integrated signal integrity
blocks with PLL, TX pre-emphasis, RX AGC, RX linear equalization, RX clock data
recovery, and adaptation. The 2-D Eye Scan feature provides an "on-chip scope"
to visualize post-equalization signal quality.

A separate sampler adjusts horizontally (time) and vertically (amplitude) in
parallel with the normal CDR sampler, enabling error counting and BER
calculation across offset settings.

The utility interfaces with the JESD204 Interface Framework through the
following driver components:

- :external+linux:ref:`axi_jesd204_tx`
- :external+linux:ref:`axi_jesd204_rx`
- :external+linux:ref:`axi_adxcvr`

Source code is available at :git-jesd-eye-scan-gtk:`GitHub <>`.

BERT testing
--------------------------------------------------------------------------------

The following table shows testing duration vs. BERT rates for a 5.0 Gbps link:

.. list-table::
   :header-rows: 1

   * - BERT Rate
     - Bits
     - Duration
   * - 10\ :sup:`-8`
     - 10\ :sup:`8`
     - 20 ms
   * - 10\ :sup:`-10`
     - 10\ :sup:`10`
     - 2 seconds
   * - 10\ :sup:`-12`
     - 10\ :sup:`12`
     - 3.33 minutes
   * - 10\ :sup:`-17`
     - 10\ :sup:`17`
     - ~8 months

With 8,192 pixels (64 x 128 offsets), capturing 10\ :sup:`-8` BERT requires
2.7 minutes; 10\ :sup:`-17` would take 5,400+ years.

Mask
--------------------------------------------------------------------------------

The JESD204B specification defines receive keep-out masks based on channel baud
rate. The vertical axis in the 2-D statistical eye diagram is in "codes", not
millivolts, since measurements occur post-equalization within the FPGA.

Installation
--------------------------------------------------------------------------------

Debian/Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   apt-get update
   apt-get install -y git build-essential gnuplot libgtk-3-dev libncurses-dev

CentOS/RedHat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   yum update
   yum -y groupinstall 'Development Tools'
   yum -y install git ncurses-devel gtk3-devel gnuplot

Usage
--------------------------------------------------------------------------------

.. code-block::

   Usage: jesd_eye_scan [-p PATH]
       -p     Allows setting a different directory root. Default is /.
              This is useful when running the tool remote

Local execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::

   $jesd_eye_scan &

Remote execution (X11 forwarding)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::

   $ssh -X root@<board-ip> jesd_eye_scan

Remote execution (SSHFS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   mkdir /home/user/mnt
   sudo sshfs -o direct_io,sync_read,allow_other \
       -o StrictHostKeyChecking=no root@<board-ip>:/ /home/user/mnt
   LC_ALL=c jesd_eye_scan -p /home/user/mnt

.. note::

   The ``LC_ALL=c`` prefix is important when running remotely, because the
   locale on the client system can influence the format of the data.

Output
--------------------------------------------------------------------------------

The tool displays three main windows:

#. **Main Window** — Overall eye diagram visualization
#. **Status Information** — System and link metrics
#. **Lane Information** — Per-lane statistics

The eye opening numbers show error-free regions in Unit Intervals (time domain)
and codes (voltage scale). Heat map colors represent error density at each
point.

Requirements
--------------------------------------------------------------------------------

- JESD204B converter
- :xilinx:`ZC706` or :xilinx:`ZCU102` (local execution), or :xilinx:`KC705`,
  :xilinx:`KCU105` (remote execution)
- ADI Linux image on SD Card or ADI kernel with Microblaze RFS

Tweaking
--------------------------------------------------------------------------------

Converter-side adjustments available:

- JESD204B pre-emphasis
- JESD204B CML differential output drive level

These modifications trade off eye opening, power consumption, and potential EMI
emissions.

References
--------------------------------------------------------------------------------

- :xilinx:`Serial Link Signal Integrity Analysis <support/documents/white-papers/wp428-Serial-Link-Signal-Integrity.pdf>`
- :xilinx:`Eye Scan with MicroBlaze Processor MCS <support/documents/application-notes/xapp743-eye-scan-with-microblaze.pdf>`
- :xilinx:`7 Series FPGAs GTX/GTH Transceivers User Guide <support/documents/user-guides/ug476_7Series_Transceivers.pdf>`
- :adi:`The JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`

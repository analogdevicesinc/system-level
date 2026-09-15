.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9009/reference_hdl

.. _adrv9009 reference_hdl:

ADRV9009 HDL Reference Design
=============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page
   is outdated and the new one can be found at
   https://analogdevicesinc.github.io/hdl/projects/adrv9009/index.html

Functional Overview
-------------------

The HDL reference design is an embedded system built around a processor core
either ARM, NIOS-II or Microblaze. A functional block diagram of the system is
shown below. The device digital interface is handled by the transceiver IP
followed by the JESD204B and device specific cores. The JESD204B lanes are
shared among the 4 transmit, 2 receive and 2 observation/sniffer receive data
paths by the same set of transceivers within the IP. The cores are programmable
through an AXI-lite interface. The delineated data is then passed on to
independent DMA cores for the transmit, receive and observation/sniffer paths.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/adrv9009.svg

Digital Interface
-----------------

The digital interface consists of 4 transmit, 2 receive and 2
observation/sniffer lanes running up to 9.8Gbps. The transceivers then interface
to the cores at 128bits@245MHz in the transmit and 64bits@245MHz for the receive
channels. The sniffer/observation rates depend on the mode selected. The data is
sent or received based on the configuration (programmable) from separate
transmit and receive chains.

DAC Interface
-------------

The DAC data may be sourced from an internal data generator (DDS or pattern) or
from the external DDR via DMA. The internal DDS phase and frequency are
programmable. DAC UNPACK IP (util_upack) allows transfering data from the DMA to
a reduced number of channels, at a higher rate.

ADC Interface
-------------

The ADC data is sent to the DDR via DMA. The ADC PACK IP (util_cpack) allows
capturing only part of the channels.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI
signals are controlled by a separate AXI based SPI core.

Download
--------

The HDL repository, list of supported carriers and the list of required IP cores
can be found here:

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-adrv9008/9
   :end-before: .. end-adrv9008/9

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-help-support
   :end-before: .. end-help-support

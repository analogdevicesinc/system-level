.. _pzsdr carriers packrf:

ADRV-PackRF
===========

PackRF is a pair of software defined radios designed using the `ADRV9361-Z7035 <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom>`_ system on module (SOM). The SOM is based on the\ :adi:`AD9361 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/wideband-transceivers-ic/ad9361.html>` RF Transceiver and the Xilinx Zynq®-7000 All Programmable (AP) SoC.

See the :adi:`Analog Devices Product Home Page <en/design-center/reference-designs/circuits-from-the-lab/cn0412.html#rd-overview>` for information on price and options to purchase the system.

The purpose of the radio is to provide an RF platform to software developers, system architects, and product developers who want a single platform which operates over a wide tuning range (70 MHz – 6 GHz). PackRF accelerates development from initial evaluation to field deployment.

The radio is contained inside a blue aluminum enclosure with access to
connections for power, ethernet, USB, OLED, audio and micro SD card. Antenna’s
connect to SMA’s on the second face plate (not shown here) for TX, RX,
monitoring and GPS I/O’s. Silkscreen on the radio contains various part numbers
and links to additional material.

.. image:: ../images/pelican_case.jpg
   :alt: PackRF
   :align: center
   :width: 600

Portable Radio Reference Design
-------------------------------

The radios are referred to as 'Portable Radio Reference Design'. Each one is a combination of `ADRV9361-Z7035 <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom>`_ PCB, carrier card, metal enclosure and additional, smaller items (adapter PCBs, cables, connectors etc). The system is fully contained inside of a 159.99mm x 78.00mm x 43.00mm (6.3" x 3.071" x 1.69") aluminum metal enclosure. Card guides on the inside of the case provide a secure shelf for the PCB's. Production units will be a blue metal etched with silkscreen providing part numbers, links to documentation and more.

.. image:: ../images/production_build.png
   :alt: 1 Portable Radio Unit
   :align: center
   :width: 600

Included with the radio module is a complete single carrier modem reference
design. The modem is designed as a constantly transmitting frequency division
duplexing (FDD) system with a single transmit channel (uplink) and single
receive channel (downlink), enabling a single bidirectional point-to-point link
between two nodes. A complete wireless video link can be demonstrated with the
webcams provided in this kit between disjoint nodes.

Radio Hardware
~~~~~~~~~~~~~~

A list of Design files is located in the :ref:`Hardware <pzsdr carriers packrf hardware>` section. These include pdf's of the schematics, gerber files, board file in native format, bill of materials and more.

Radio Design Features
~~~~~~~~~~~~~~~~~~~~~

-  Hot-swappable Input Power
-  Battery Backup
-  Charge Maintenance
-  OLED and Navigation Scroll Wheel
-  Custom Designed Menu

Follow this link for more detailed information on :ref:`design features <pzsdr carriers portable-radio-reference-design features>` regarding the power supply design, mechanical considerations, battery maintenance system logic and more.

Portable Radio Software and HDL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software for the ADRV-PACKRF is provided by Analog Devices as an open source reference design that can be used in various applications. The system source code consists of several components, which are used together to control onboard devices and provide connectivity to external tools for development. Follow this link for more information on the :ref:`System Software Architecture <pzsdr carriers packrf system-software-architecture>`

Radio GUI
~~~~~~~~~

Portable Radio Application Use Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This :ref:`example use case <pzsdr carriers packrf example-use-case>` allows the user to perform a simple experiment with the datalink and USB webcams.

-  Default
-  Modem

Radio Assembly
~~~~~~~~~~~~~~

Save yourself a headache and do not disassemble the radio.

Assembly of the Portable Radio Reference Design is almost as complicated as some of the hardware and software. It occupies a significant amount of time and will cause headaches, finger aches and potential damage to the device. A detailed list of instructions is provided in case you are assembling or opening a radio. Have a look at the :ref:`assembly instructions <pzsdr carriers portable-radio-reference-design assembly-instructions>` before beginning.

The Gallery
~~~~~~~~~~~

There is also a :ref:`picture gallery <pzsdr carriers portable-radio-reference-design gallery>` to document the travels and adventures of the radio.

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/ADRV-PACKRF?&v=RevE>`_ to receive all these great benefits and more!

*End of Document*

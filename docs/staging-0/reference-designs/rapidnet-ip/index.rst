.. imported from: https://wiki.analog.com/resources/eval/user-guides/rapidnet-ip

.. _rapidnet-ip:

RapidNet IP Wireless Networking Protocol Solution
=================================================

:adi:`RapidNet-IP` protocol is a long range sub-GHz wireless networking solution
that addresses industrial and commercial applications where reliability,
robustness, scalability, and battery life are critical. Applications such as
electronic shelf label (ESL), smart lock, and smart infrastructure can be
realized by RapidNet IP.

RapidNet IP is a complete point-to-multipoint wireless networking solution
operating in sub-GHz worldwide regional bands. RapidNet IP protocol uses
star-repeater network topology, enables longer range communication with faster
message transmit times.

RapidNet IP leverages the market proven :adi:`ADF7023` radio transceiver and
lowest power ULP processors (:adi:`ADuCM3029` or :adi:`ADuCM4050`).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/1.png
   :width: 600px

Features and Specification
--------------------------

- Efficient low power network

*  Low power IEEE802.15.4g/e wireless network with time synchronized channel hopping (TSCH)—no collisions and no lengthy receive waits
* Lowest power consumption per node with star and extended star network topology configuration.
* Reliable end-to-end communications with acknowledgements
* Long range

  * Typical range of 500 m (2 hop and confguration setting dependent)

* Data rate and frequency

  * High throughput (4 pks/sec at 1 kB per packet)
  * Fast network join time (for example, 256 motes in 47 sec)
  * Low latency—minimum of 5 sec network loop cycle
  * ISM frequency band support (433,868,915,920 MHz)
  * Multiple data rate support (37.5 kbps to 300 kbps)
  * On-demand bandwidth allocation (for example, up to 1 MB per node/1 hr)

* Supported modes:

  * Master mode (on-chip applications)
  * Slave mode (application coprocessor)

* Current consumption:

  * Active: <10 µA ave. (3 updates of 1 kB packets/day case)
  * Sleep: <1.5 µA

* FCC and ARIB STD T108 regulation test feature support integrated
* Supports OTA (over-the-air) update
* Reliable scheduling of alert messages from any or all motes
* Sample software available for Linux® or :adi:`ADuCM4050` -based gateways with
  various backhaul connectivity options

Software Package
----------------

Below are the pre-requisites for RapidNet IP for Developing application or
running in-build demo. Please follow procedure on how to install IAR and DFP
packs on
:dokuwiki:`Prerequisites for RapidNet IP </resources/eval/user-guides/rapidnet-ip/sw>`
wiki page.

#. IAR 8.22.2
#. ADuCM3029 DFP 3.2.0
#. EV-COG-AD3029LZ BSP 3.1.0
#. RapidNet IP Binary installer 1.1.0 - for running the in-built demo
#. RapidNet IP Source installer 1.1.0 - for developing applications

RapidNet IP offers below Software Package.

Binary Installer
~~~~~~~~~~~~~~~~

#. This software pack contains only binary files, tools and document required to
   run the RapidNet IP application.
#. :adi:`Click here <en/products/landing-pages/001/rapidnet-ip-protocol.html>`
   to download the binary installer.

Source Installer
~~~~~~~~~~~~~~~~

- This software pack contains source code to develop application on RapidNet IP Protocol.
- Follow these steps to download "RapidNet IP" source package

  - Click www.analog.com/SRF to go to Analog devices software request form, to request the source installer.
  - Fill required details.
  - Under 'Target Hardware', select 'Ultra Low Power Microcontroller'
  - Under 'Software requested' section, check 'RapidNet IP'.
  - Click 'SUBMIT' button available at the bottom of the page.
  - You will receive an e-mail notification with a download link.

RapidNet IP Module
------------------

User can buy RapidNet IP modules from third party vendors. Contact ADI for more
information about this.

Module Connection diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/rf_module_block_doagram.png
   :width: 500px

Castellation leads pinout
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/castellations-1.png
   :width: 500px

RapidNet IP Development Kits
----------------------------

Below are the different kits available for evaluating RapidNet IP Network
Protocol.

#. **EV-RAPID-ESL-900JZ** - RapidNet IP ESL Evaluation kit with TELEC
   Certification specific for Japan.
#. **EV-RAPID-ESL-900Z** - RapidNet IP ESL Evaluation Kit for all the regions
   except Japan.
#. **EV-RAPID-NODE-900Z** - Electronic Shelf Labelling (ESL) node which should
   be ordered only if more nodes are required during the evaluation of
   EV-RAPID-ESL-900JZ/EV-RAPID-ESL-900Z.
#. **EV-RAPID-KIT-900Z** - RapidNet IP Sensor Application Kit

Below are the kit contents. Please click on the individual link to know more
about the particular board.

#. **EV-RAPID-ESL-900JZ/EV-RAPID-ESL-900Z** - RapidNet IP Electronic Shelf
   Labelling (ESL) Kit

- :dokuwiki:`EV-COG-AD3029LZ </resources/eval/user-guides/ev-cog-ad3029lz>` -
  development platform for Analog Devices Ultra Low Power Microcontroller
  :adi:`ADuCM3029`
- :dokuwiki:`EV-DNG-RFMOD-9001Z </resources/eval/user-guides/ev-dng-rfmod-9001z>`
  - USB Dongle which acts as Border Router for RapidNet IP Network (902-958MHz)
- :dokuwiki:`EV-COG-ADF7023-9Z </resources/eval/user-guides/ev-cog-adf7023-9z>`
  - :adi:`ADF7023-J` Connectivity Cog (902-958MHz)
- :dokuwiki:`EV-GEAR-EINK1Z </resources/eval/user-guides/ev-gear-eink1z>` - Cog
  Ecosystem Gear with E-Paper Display from E-INK.

#. **EV-RAPID-NODE-900Z** - RapidNet IP Electronic Shelf Labelling (ESL) Kit

- :dokuwiki:`EV-COG-AD3029LZ </resources/eval/user-guides/ev-cog-ad3029lz>` -
  development platform for Analog Devices Ultra Low Power Microcontroller
  :adi:`ADuCM3029`
- :dokuwiki:`EV-COG-ADF7023-9Z </resources/eval/user-guides/ev-cog-adf7023-9z>`
  - :adi:`ADF7023-J` Connectivity Cog (902-958MHz)
- :dokuwiki:`EV-GEAR-EINK1Z </resources/eval/user-guides/ev-gear-eink1z>` - Cog
  Ecosystem Gear with E-Paper Display from E-INK.

#. **EV-RAPID-KIT-900Z** - RapidNet IP Sensor Application Kit

- :dokuwiki:`EV-COG-AD3029LZ </resources/eval/user-guides/ev-cog-ad3029lz>` -
  development platform for Analog Devices Ultra Low Power Microcontroller
  :adi:`ADuCM3029`
- :dokuwiki:`EV-DNG-RFMOD-9001Z </resources/eval/user-guides/ev-dng-rfmod-9001z>`
  - USB Dongle which acts as Border Router for RapidNet IP Network (902-958MHz)

Additional Resources
--------------------

- :dokuwiki:`RapidNet IP Slave Mode Userguide </resources/eval/user-guides/rapidnet-ip/slave-mode>`
- :dokuwiki:`RapidNet IP Repeater Userguide </resources/eval/user-guides/rapidnet-ip/repeater-mode>`
- :dokuwiki:`RapidNet IP DeviceServer Userguide </resources/eval/user-guides/rapidnet-ip/deviceserver-userguide>`

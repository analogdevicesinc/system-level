.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-pzsdr2400tdd-eb

.. _ad-pzsdr2400tdd-eb:

AD-PZSDR2400TDD-EB User Guide
=============================

The :adi:`AD-PZSDR2400TDD-EB` is affectionately dubbed the first "RF personality
card". It plugs into the ADRV1CRR-FMC
:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html`
carrier card. 35mm U.FL coaxial cables connect the card to the ADRV9361-Z7035
:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV9361-Z7035.html#eb-overview`
providing access to the transmit and receive inputs of the :adi:`AD9361`.
Information on the card, how to use it, the design package that surrounds it,
and the software which can make it work, can be found here.

The purpose of the :adi:`AD-PZSDR2400TDD-EB` is to provide the user with a
tunable path to condition the transmit or receive signals of the :adi:`AD9361`.
Selection of TX or RX path is achieved by the 200MHz to 2.7GHz SPDT switch
:adi:`HMC546LP2` controlled by the FPGA and accompanying software. The transmit
path consists of a 2.4GHz filter, half watt driver amplifier :adi:`ADL5324` and
2 watt power amplifier :adi:`HMC921`. The receive path consists of the same
2.4GHz filter as well as a low loss LNA :adi:`HMC669`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pzsdr2400tdd-ebz/pcb_top.jpg
   :width: 600px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:dokuwiki:`ask <ad-pzsdr2400tdd-eb/help_and_support>`.

#. :dokuwiki:`Introduction <ad-pzsdr2400tdd-eb/introduction>`
#. :dokuwiki:`Hardware <ad-pzsdr2400tdd-eb/hardware>`: This provides a brief
   description of the board by itself, and is a good reference for those who
   want to understand a little more about the board. If you just want to use the
   board, you can skip this section, and come back to it when you want to
   incorporate the AD9361 into your product.

   #. :dokuwiki:`Hardware <ad-pzsdr2400tdd-eb/hardware>` (including
      :dokuwiki:`schematics </ad-pzsdr2400tdd-eb/hardware#downloads>`)

      #. :dokuwiki:`Functional Overview & Specifications <ad-pzsdr2400tdd-eb/hardware/functional_overview>`
      #. :dokuwiki:`Configuration options <ad-pzsdr2400tdd-eb/hardware/configuration_options>`
      #. :dokuwiki:`Characteristics and Performance <ad-pzsdr2400tdd-eb/hardware/characteristics_and_performance>`
      #. :dokuwiki:`Layout Considerations <ad-pzsdr2400tdd-eb/hardware/Layout_Considerations>`
      #. :dokuwiki:`FCC or CE certification <ad-pzsdr2400tdd-eb/hardware/fcc or ce certification>`

   #. :dokuwiki:`Software <ad-pzsdr2400tdd-eb/software>`

#. :dokuwiki:`Help and Support <ad-pzsdr2400TDD-eb/help_and_support>`

.. todo:: .. figure: analogTV>4840956066001

Warning
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

AD-PZSDR2400TDD-EB User Guide
=============================

The :adi:`AD-PZSDR2400TDD-EB` is affectionately dubbed the first
'RF personality card'. It plugs into the ADRV1CRR-FMC
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

.. figure:: images/pcb_top.jpg
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB board top view.

.. toctree::

   Introduction <introduction>
   Hardware <hardware>
   Functional Overview <hardware/functional_overview>
   Configuration Options <hardware/configuration_options>
   Characteristics and Performance <hardware/characteristics_and_performance>
   Layout Considerations <hardware/layout_considerations>
   FCC or CE Certification <hardware/fcc_or_ce_certification>
   Software <software>
   Help and Support <help_and_support>

For HDL reference documentation on the AD9361 TDD mode support, see
:external+hdl:doc:`library/axi_ad9361/tdd_support`.

Warning
-------

.. esd-warning::

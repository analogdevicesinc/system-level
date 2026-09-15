.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/hardware

.. _adrv936x_rfsom hardware:

ADRV936x RF SOM Hardware
""""""""""""""""""""""""

Whether you want to understand the changes between revisions, or just understand
how to probe the PCB, this is where all the information should be.

ADRV936x - Mechanical
=====================

The ADRV9361-Z7035 SDR 2X2 SOM uses a 20 layer PCB that measures 2.440`` x
3.937`` (62 mm x 100 mm). The 62mm x 100mm form factor is compatible with the
DP10062 ``Sick of Beige v1.0`` specification from dangerousprototypes.com.

Connectors
----------

The MicroHeaders used on ADRV9361-Z7035 are FCI 0.8mm BergStak®100-position Dual
Row, BTB Vertical Receptacles (61082-101400LF). These receptacles mate with any
of the FCI 0.8mm BergStak® 100-position Dual Row BTB Vertical Plugs
(61083-10x400LF) to provide variable stack heights of 5mm, 6mm, 7mm or 8mm. The
SOM uses the FCI ``receptacle`` while carrier cards use the ``plug``. Both
receptacle and plug include a PCB locator peg that can be used to design
precisely mated SOM and carrier layouts.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/locator.png
   :width: 600px

More information about these connectors can be found
`here <http://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/61082.pdf>`__.

Dimensions
----------

The physical dimensions of the connectors, mounting holes and PCB is common
between the ADRV9361-Z7035 and the ADRV9364-Z7020.

.. admonition:: Download

   The Footprint is common between the two parts:

   :dokuwiki:`Mounting holes and physical dimensions </resources/eval/user-guides/adrv936x_rfsom/08_038702d_conn_dim.pdf>`

   - Carrier Card Connector Dimensions:

   :dokuwiki:`Connector Dimensions </resources/eval/user-guides/adrv936x_rfsom/carrier_connector_locations.jpg>`

   - ADRV9361-Z7035 Step file:
     :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035.step.zip`

 A STEP-File is a widely used data exchange form of ISO 10303 which can
 represent 3D objects in Computer-aided design (CAD) and related information.

Pinout
------

.. admonition:: Download

   The connector pinouts are a superset:

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035_pinout_jx_1-4_.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_pinout_jx_1-4_.pdf`

ADRV9361-Z7035 Hardware
=======================

Revision F
----------

This is the current shipping version.

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9361-z7035/02-038702-01-f2.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9361-z7035/05-038702-01-f2.7z`

- Changes from Rev E to Rev F:

  - The schematic did not change. We only made an adjustment to the layout.
  - The RF traces were modified to improve the insertion loss and the return
    loss as well as the EVM.

    - This resulted in some layout changes for discrete capacitors

  - On the SOM the revision is shown as ``F2`` on the PCB artwork
  - The reset button moved position

Revision E
----------

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035_reve.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/05_038702-e.xlsx`

Revision C (First publicly available revision)
----------------------------------------------

This is the first publicly available revision.

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035.pdf`

Why do a Rev D?
~~~~~~~~~~~~~~~

- Improved the power structure and increased the 0.95V current from 2A to 6A
- Added a
  `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`__
  option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
- Improved the layout to accommodate the power changes.

ADRV9364-Z7020 Hardware
=======================

Revision D
----------

This is the current shipping version.

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revd-1.pdf`

   ::

        *There was a small typo in the rev D0 of the schematics (below), the net named ''*_EN_AGC'', was tied to the ''ENABLE'' pin, and the net called ''*_ENABLE'' was tied to the ''EN_AGC'' pin. This is fixed/updated in this schematic. copper/layout does not change, only the designation on the wire (for clarity).

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revd.pdf`

   ::

        * This has the notation error described above.

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/05-041351-01-d3.xlsx`

Revision C
----------

This is the first publicly available revision.

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revc.pdf`

Why do a Rev D?
~~~~~~~~~~~~~~~

- Improved the power structure and increased the 1V current from 2A to 4A

  - Improved the layout to accommodate the power changes.

- Added a
  `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`__
  option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
- Improved the RF traces to have better insertion loss and return loss.

Carrier Support
===============

The ADRV9361-Z7035 supports all features on the
:adi:`ADRV1CRR-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`
carrier board. The ADRV9364-Z7020 supports a subset of features because the Zynq
Z7020 has fewer available user I/Os. For the ADRV9364-Z7020 it is recommended to
use the
:adi:`ADRV1CRR-BOB <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-BOB.html>`
carrier.

Support
=======

Please refer to :ez:`EngineerZone <community/fpga>` with questions on
hardware/schematics/or using the ADRV936x RF SOMs.

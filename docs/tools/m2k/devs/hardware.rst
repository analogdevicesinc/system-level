.. _m2k hardware:

ADALM2000 Hardware
==================

Whether you want to understand the changes between revisions, or just
understand how to probe the PCB, this is where all the information should be.

Connectors
----------

The :adi:`ADALM2000`` includes a button (S1 on the PCB), and two USB
connectors.

.. image:: ../images/button_connectors.jpg
   :align: center
   :width: 400px

.. image:: ../images/zoom_conn.jpg
   :align: center
   :width: 400px

The button can be defined by software, it is normally held on with a paper clip
or thumb tack during power on to put the device into a recovery mode. It can be
re-purposed to do other things.

The first USB connector (the middle one) is the USB OTG connector (can be the
USB HOST connector (cabled to a USB peripheral), or the USB peripheral
connector (cabled to a USB Host)).

The second USB connector (the one on the side) is for power only when running
in Host mode.

Removing the case
-----------------

The plastic case comes off quite easily, with the removal of two black
`Phillips screws <https://en.wikipedia.org/wiki/List_of_screw_drives#Phillips>`__
on the bottom of the case. The production version may be different. It will for
sure be :dokuwiki:`CE and FCC certified <university/tools/m2k/common/regulatory_compliance>`.
(already passed)

Removing the screws will allow you to take the top off the case, and expose the
PCB.

.. grid::
   :widths: 50% 50%

   .. image:: ../images/removing_the_case.jpg
      :width: 400px

   .. image:: ../images/exposed_pcb.jpg
      :width: 400px

If you want to remove the PCB, and place it on the table, we recommend that you
attach `Cylindrical Bumpers <https://www.digikey.com/en/products/detail/3m/SJ5076/570288?s=N4IgTCBcDaIMwFkCMBWAbABjSgtAOQBEQBdAXyA>`__
(also known as feet), on the PCB to protect the components on the bottom of the
PCB. These are not included in the design, and must be purchased separately (as
we don't expect too many people wanting to do this).

Mating connectors
-----------------

It's likely that you might want to make a board that mates directly to the
:adi:`ADALM2000`- check out these connectors. There are listed here as a
convenience.

  +---------------------------+-------------------------+-------------------------------------------------+
  | Manufacture               | Part Number             | Possible providers                              |
  +===========================+=========================+=================================================+
  | Sullins Connector         | PPPC152LJBN-RC          | `Digikey <https://www.digikey.com/en/products/  |
  | Solutions                 |                         | detail/PPPC152LJBN-RC>`__                       |
  +---------------------------+-------------------------+-------------------------------------------------+
  | Samtec                    | `SSQ-115-02-T-D-RA      | `Digikey <https://www.digikey.com/en/products/  |
  |                           | <https://www.samtec.com/| detail/SAM1224-15-ND>`__,                       |
  |                           | products/ssq-115-02-t-d-| `Mouser <https://www.mouser.com/ProductDetail/  |
  |                           | ra>`__                  | Samtec/SSQ-115-02-T-D-RA?qs=rU5fayqh%252BE2UN30x|
  |                           |                         | yNQdAQ%3D%3D>`__                                |
  +---------------------------+-------------------------+-------------------------------------------------+

Revision D
----------

.. admonition:: Downloads
   :class: note

   * :dokuwiki:`Rev D Schematics <_media/university/tools/m2k/devs/02_042233d_top_updated_sch.pdf>`
   * :dokuwiki:`Rev D Gerbers <_media/university/tools/m2k/devs/09-042233-01d.zip>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__)
   * :dokuwiki:`Rev D Bill of materials <_media/university/tools/m2k/devs/05-042233-01-d2-adalm2000_d_bom.xlsx>`
   * :dokuwiki:`Rev D Allegro Board File <_media/university/tools/m2k/devs/adalm2000_brd_revd.7z>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer
     <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__
     to view.
   * :dokuwiki:`Rev D Cadence project <_media/university/tools/m2k/devs/20_042233e_compress.zip>`
   * :dokuwiki:`Rev D 3D model (Case, bare PCB, connectors) <_media/university/tools/m2k/devs/m2k_with_case.zip>`

Revision C
----------

.. admonition:: Downloads
   :class: note

   * :dokuwiki:`Rev C Schematics <_media/university/tools/m2k/devs/adalm2000_revc_schematic.pdf>`
   * :dokuwiki:`Rev C Gerbers <_media/university/tools/m2k/devs/09-042233-01c.zip>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__)
   * :dokuwiki:`Rev C Bill of materials <_media/university/tools/m2k/devs/05-042233-01-cadalm2000-revc-bom.xlsx>`
   * :dokuwiki:`Rev C Allegro BoardFile <_media/university/tools/m2k/devs/08_042233c-revc-brd.7z>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer
     <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__
     to view.
   * :dokuwiki:`Rev C Cadence project <_media/university/tools/m2k/devs/20-042233-01c.zip>`

Revision B
----------

.. admonition:: Downloads
   :class: note

   * :dokuwiki:`Rev B Schematics <_media/university/tools/m2k/devs/adalm2000_revb_schematic.pdf>`
   * :dokuwiki:`Rev B Gerbers <_media/university/tools/m2k/devs/09-042233-01b.zip>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__)
   * :dokuwiki:`Rev B Bill of materials <_media/university/tools/m2k/devs/05-042233-01-b_adalm2000_b_bom.xlsx>`
   * :dokuwiki:`Rev B Allegro Board File <_media/university/tools/m2k/devs/08_042233brevb_brd.7z>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer
     <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__
     to view.
   * :dokuwiki:`Rev B Cadence Project <_media/university/tools/m2k/devs/20-042233-01b.zip>`

Why do a Rev C?
~~~~~~~~~~~~~~~

- A voltage divider should be added TX calibration path
- Two 10 uF capacitors need to be added at USB power inputs.
- The negative rail of the AD8066 should have a power down and for this is
  needed a -5V LDO.
- ADP198 in the positive power supplies analog stage can be removed.
- The analog power sequence has to be improved.
- The 2.4 Ohm resistor at output of User power supply needs to be replaced with
  4.7Ohm.
- The user power supplies should have individual power down and a 6V protection
  Zenner diode at the output.

Revision A
----------

.. admonition:: Downloads
   :class: note

   * :dokuwiki:`Rev A Schematics <_media/university/tools/m2k/devs/adalm2000_reva_schematic.pdf>`
   * :dokuwiki:`Rev A Gerbers <_media/university/tools/m2k/devs/09-042233-01a.zip>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__)
   * :dokuwiki:`Rev A Bill of materials <_media/university/tools/m2k/devs/042233a_adalm2000_a_bom.xlsx>`
   * :dokuwiki:`Rev A Allegro Board File <_media/university/tools/m2k/devs/08_042233areva_brd.7z>`
     (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer
     <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__
     to view.
   * :dokuwiki:`Rev A Cadence project <_media/university/tools/m2k/devs/20-042233-01a.zip>`

Why do a Rev B?
~~~~~~~~~~~~~~~

- Because of heating on the board the supply for the scope input buffers is
  reduced. The buffers are supplied on rev B at -3V3 and 3V8 (obtained with an
  LDO from Vin).
- The digital and analog 1V8 rails are merged but the footprint of the LDO for
  1V8_A is kept in case there will be too much noise.
- For lower power consumption the ADC divers are replaced with ADA4940-2ACPZ.
- To remove the back powering of the analog section the DACs controlled by I2C
  are powered from the digital supplies.
- The user power supplies could use an amplifier that provides low power,
  smaller noise and larger bandwidth, such as ADA4805.
- The AWG protection and the power supplies monitor can be removed.
- The input choke needs to be replaced with a version with a higher current
  rating for a lower impedance at high frequencies.

Images
------

Click to get the full size image.

.. image:: ../images/m2k.jpg
   :align: center
   :width: 500px

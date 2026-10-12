.. _pzsdr carriers portable-radio-reference-design assembly-instructions:

Portable Radio Reference Design — Assembly Instructions
===============================================================================

These are the assembly instructions for the radio.

Stage 1 — Partial Assembly
===============================================================================

Belly Plate
-------------------------------------------------------------------------------

OLED Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Cut a strip of electric tape to place over the exposed vias found on the
   OLED PCB.

   .. image:: ../../images/oled_with_tape.jpg
      :width: 300

#. Place the OLED into the rectangular opening.
#. Place 4× M2.5 × 4mm screws through the belly plate and OLED. Apply
   Loctite. Attach 4× M2.5 nuts and tighten. Cut off the ends of the screw
   if it extends beyond the nut.
#. Insert a
   `20-position FMC cable <https://www.digikey.com/WM11498-ND>`_ into the
   OLED connector with the exposed copper facing away from the PCB. Close the
   black bracket to secure the cable.
#. Apply hot glue to the connector and part of the cable so it cannot be
   accidentally removed.

   .. warning::

      Be careful removing this glue — too much force can damage the OLED
      connector.

#. Bend the cable backwards so it sticks out past the end of the belly plate.

   .. image:: ../../images/oled_connected_to_belly_plate.jpg
      :width: 600

Nav Switch Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Place 4× M2.5 × 8mm screws through the belly plate. Apply Loctite 242.
#. Place 4×
   `908-135 <https://www.digikey.com/908-135-ND>`_
   standoffs onto the screws.
#. Place the Nav Switch PCB into the circular opening with the connector
   closer to the middle of the belly plate. Attach 4× M2.5 nuts and tighten.

   .. grid::
      :widths: 50 50

      .. figure:: ../../images/nav_close.jpg

         Nav switch close-up

      .. figure:: ../../images/nav_switch.jpg

         Nav switch installed

#. Insert the ribbon cable into the connector on the Nav Switch so it extends
   towards the battery. Bend the cable towards the red line and pull it out to
   the left side. Apply hot glue to the connector and a fraction of the cable
   to secure everything.

   .. note::

      There is a clearance constraint between this cable header and a component
      on the bottom of the PCB. Glue must be restricted to below the top of the
      cable header when plugged into the Nav Switch PCB.

   .. image:: ../../images/belly_plate_with_battery_on_side.jpg

Battery Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Battery CU-J479-V6: Molex 51065-0300 <https://www.batteryspace.com/Custom-Polymer-Li-Ion-battery-3.7V-3200mAh-11.8-Wh-with-Thermistor.aspx>`_

#. Clean the area between the two PCBs with a dry cloth.
#. Cut a 1–1.25 inch piece of double-sided tape, peel off the cover, and
   place firmly between the PCBs.
#. Place the battery firmly onto the tape with the yellow and white labels
   facing away from the belly plate.

   .. image:: ../../images/belly_plate_inside.jpg

Preparing the ADRV936x PCB
-------------------------------------------------------------------------------

Heatsink Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Heatsink <https://www.digikey.com/345-1146-ND>`_

#. Apply a circle of thermal grease to the protruding portion of the Xilinx
   FPGA and spread the paste around.

   .. image:: ../../images/grease_fpga.jpg
      :width: 400

#. Carefully place the heatsink making sure the plastic frame snaps into place.

   .. warning::

      Be careful of C108. The plastic of the heatsink frame can catch on this
      component and damage it if too much force is applied.

   .. grid::
      :widths: 50 50

      .. figure:: ../../images/c108.jpg
         :width: 400

         C108 component to avoid

      .. figure:: ../../images/heatsink_image.jpg
         :width: 400

         Heatsink installed

Boot Switch Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PCB must boot using the micro SD card connector on the carrier board.
Using tweezers or a small screwdriver, move switch S1 into the **SDC**
position (text on either side of the switch indicates the correct orientation).

.. image:: ../../images/microsd_card_position.jpg
   :width: 400

Connecting the PCBs
-------------------------------------------------------------------------------

#. Line up the ADRV936x PCB connectors with those on the carrier card. The
   boards will only mate in one orientation — rotate 180° if it does not fit.
   Do not force the connection; little force is required when properly aligned.

   .. image:: ../../images/aligning_the_cards.jpg
      :width: 400

#. The image below shows the cards before being pressed together. Notice the
   gaps at the edges of the connectors.

   .. image:: ../../images/card_aligned_not_connected.jpg
      :width: 600

#. The following image shows the cards properly mated.

   .. image:: ../../images/card_aligned_connected.jpg
      :width: 600

#. Make sure to press all four corners to ensure a solid connection.

Connecting the RF cables
-------------------------------------------------------------------------------

Connecting 12 U.FL-to-SMA cables to the pair of PCBs and face plate of the
box is a challenging but critical step. Take care to make the correct
connections and route the cables carefully.

-  Fasten all cables to the face plate THEN connect them to the PCBs. Hold
   the connector in place when tightening the nut to avoid damaging the face
   plate.
-  Each cable connects to a specific connector on the PCB. Firmly connect one
   cable before moving on to the next.
-  All TX cables go through the hole in the PCB closest to them.
-  None of the RX cables go through the PCB holes.
-  GPS cables go through both holes.

.. image:: ../../images/u.fl_cables_connected_to_face_plate.jpg
   :width: 600

.. image:: ../../images/feeding_tx_cables_through_holes_2_.jpg
   :width: 600

Securing the RF Cables
-------------------------------------------------------------------------------

A 3D-printed cable brace holds all connectors and cables in place, protecting
the delicate U.FL connectors from movement or accidental damage.

#. Make sure each U.FL connector is perpendicular to the edge of the board.
#. Gently place the brace down on top of the cables and PCB, aligning the
   holes of the brace with the holes of the PCB.

   .. grid::
      :widths: 33 33 33

      .. figure:: ../../images/cable_brace_-_bottom.png
         :width: 600

         Bottom of cable brace (3D model)

      .. figure:: ../../images/cable_brace_final.jpg
         :width: 600

         Bottom of cable brace (photo)

      .. figure:: ../../images/secure_rf_cable.jpg
         :width: 600

         Cable brace fitted on PCB

Securing the PCBs
-------------------------------------------------------------------------------

#. Place 4×
   `5mm nylon spacers <https://www.digikey.com/R40-6710594>`_
   between the PCBs, aligned with the corner holes of the SOM PCB.
#. Insert 2×
   `#6-32 metal screws <https://www.digikey.com/PMS 632 0075 PH>`_
   on the cable brace side. Apply Loctite 242. Secure with
   `metal hex nuts <https://www.digikey.com/HNSS 632>`_.
   Do not over-tighten.
#. Insert 2×
   `#6-32 nylon screws <https://www.digikey.com/NY PMS 632 0050 PH>`_
   in the other two mounting holes. Apply Loctite 242. Secure with
   `nylon hex nuts <https://www.digikey.com/H620-ND>`_.
   Do not over-tighten.

.. image:: ../../images/som_carrier.jpg
   :width: 600

Once these steps are complete, begin the radio
:ref:`Partial Assembly Test <pzsdr carriers packrf testing>`.

Stage 2 — Full Assembly
===============================================================================

Body Plate
-------------------------------------------------------------------------------

IMU Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the IMU to the adapter PCB, making sure to properly align the
   header with the receptacle.
#. Plug the ribbon cable into the adapter PCB.
#. Insert screws into the body plate. Place the IMU into the screws with the
   adapter PCB away from the case.
#. Add Loctite to the screws. Add nuts and tighten according to the
   `ADIS16460 instructions <https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis16imu4-pcb>`_
   (a torque wrench is required).

   .. image:: ../../images/case_and_imu.jpg
      :width: 600

#. Apply hot glue to the connector.

Cutting a Slot for the JTAG Adapter Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This procedure needs to be performed on only half of the boxes.

Using a table saw, cut a 1.25" opening down the second shelf. This allows the
JTAG Adapter cable to protrude from the case. The JTAG adapter cable will be
added AFTER the PCBs are inserted.

.. image:: ../../images/case_saw_cut_for_jtag.jpg
   :width: 600

Inserting the PCBs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Lay both units on the table.

   .. image:: ../../images/inserting_pcb_s_1.jpg
      :width: 600

#. Gently pull the face plate and cables above the PCB.

   .. image:: ../../images/inserting_pcb_s_2.jpg
      :width: 600

#. All cables must protrude past the edge of the PCB so they do not get stuck
   between the PCB and the case.

   .. image:: ../../images/inserting_pcb_s_3.jpg
      :width: 600

#. There should be 4 empty rows on the side of the case, with the PCB slotting
   into the 5th row from the bottom.

   .. image:: ../../images/shelf_position.jpg
      :width: 400

#. Keep the cables and face plate from being caught between the side of the
   box and the PCB.

   .. image:: ../../images/inserting_pcb_s_4.jpg
      :width: 600

#. The FPGA is intended to make contact with the metal case. Flex the case
   slightly if needed for the FPGA to fit.

   .. image:: ../../images/inserting_pcb_s_5.jpg
      :width: 600

#. Make sure none of the U.FL-to-SMA cables are caught between the plastic
   and the IMU adapter PCB.

   .. image:: ../../images/inserting_pcb_s_6.jpg
      :width: 600

#. Using tweezers, connect the JTAG Adapter Cable so it protrudes from the
   opening cut into the box. Apply hot glue to the cable so it does not come
   loose.

Inserting the Belly Plate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Flip the unit over so the flat surface is down. The belly plate slides into
   the outermost slot.

   .. image:: ../../images/inserting_belly_plate_1.jpg
      :width: 600

#. Keep the OLED cable, battery cable, and navigation switch cable from
   catching on anything. A small screwdriver or tweezers will help with
   manipulating the cables.

   .. image:: ../../images/handy_tools.jpg
      :width: 600

#. Make sure the OLED connector on the carrier card is open (plastic frame
   pulled gently away from the connector).

   .. image:: ../../images/oled_connector_open.jpg
      :width: 600

#. Insert the cable into the connector and close the black plastic to secure
   it.

   .. image:: ../../images/oled_cable_secured.jpg
      :width: 600

#. Add hot glue to the connector and cable so any force is applied to the glue
   and not the connector itself.
#. Connect the battery cable to the battery plug.

   .. image:: ../../images/battery_and_oled_connected_2.jpg
      :width: 600

#. Slide the belly plate so it is flush with either end of the box.

Connecting the IMU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Using tweezers or pliers, grab the IMU cable and gently push it into the
   connector.

   .. image:: ../../images/imu_cable_connected.jpg
      :width: 600

#. Apply hot glue to the cable and connector so it cannot be disconnected
   unintentionally. Let the glue dry for a minute.

   .. image:: ../../images/glueing_imu.jpg
      :width: 600

Face Plate
-------------------------------------------------------------------------------

#. Make sure the button faces the same direction as the beveled screw holes on
   the face plate.

   .. image:: ../../images/face_plate_with_power_switch.jpg
      :width: 600

#. Add hex nut and tighten slightly.
#. Add the male pin header to the Power Switch Adapter PCB protruding TOWARD
   the face plate. Solder the pins.
#. Add the Power Switch Adapter PCB to the power switch. Solder the four pins.

   .. image:: ../../images/pcb_buton.jpg
      :width: 400

#. Attach the Power Switch Cable to the header.
#. Position the Power Switch Adapter PCB parallel to the bottom of the face
   plate. Position the hex nut parallel to the bottom of the face plate.
   Tighten the hex nut and apply Loctite.
#. Add hot glue to the connector on the Adapter PCB so the cable cannot be
   disconnected. Let the glue dry for a minute.

Connecting the Power Switch and Navigation Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Slide the belly plate away to access the Power Switch Connector (P9) and
   Navigation Switch Connector (P11).

   .. image:: ../../images/connecting_power_switch_cable_and_navigation_switch_cable.jpg
      :width: 400

#. Connect the power switch cable to P9. Apply hot glue to the connector.

   .. note::

      Make sure no glue goes outside the white line in the silkscreen — this
      will make the PCB difficult to slide in and out.

#. Connect the navigation cable to P11.
#. Slide the case back to its starting position. Apply hot glue to the
   connector so it cannot be easily removed.

Adding the plastic frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Position the plastic frame so one of the short sides of the face plate goes
   through the opening.

   .. image:: ../../images/first_step_in_applying_plastic_frame.jpg
      :width: 600

#. Gently push the face plate through the plastic frame.

   .. image:: ../../images/second_step_in_applying_plastic_frame.jpg
      :width: 600

#. Push the plastic frame flush to the case.

Securing the face plates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SMA Face Plate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ensure U.FL cables are not pinched or resting in any damaging condition.
   Make sure no U.FL cables are caught between the edge of the PCB and the
   face plate as you press it flush to the end of the case.

   .. image:: ../../images/closing_the_face_plate.jpg
      :width: 600

#. Insert screws and secure. Do not over-tighten — this risks stripping the
   threads.

Ethernet Face Plate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Make sure the connectors fit properly into the holes — they should be flush
   with no force required to align.

   .. image:: ../../images/ethernet_face_plate.jpg
      :width: 600

#. Insert screws and secure.

Adding Face Plate Labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two labels need to be added to the SMAs to match the text shown below (future
builds will have silkscreen etched with the correct labels).

.. image:: ../../images/labels_for_face_plate.jpg
   :width: 400

Once these steps are complete, begin the radio
:ref:`Full Assembly Test <pzsdr carriers packrf testing>`.

PackRF — Final Assembly
===============================================================================

#. Place one finished radio in each slot (only one radio should have the JTAG
   adapter cable hanging out of the side).
#. Place one TPE-115GI POE injector in each slot.
#. Place 20 RF antennas in the slot.
#. Place the remaining items into the large open rectangle on the left (fold
   and press air out of plastic packaging so everything fits):

   -  2× Micro SD cards
   -  2× USB OTG cables
   -  2× GPS antennas
   -  2× Ethernet cables
   -  2× Car adapters
   -  2× DC wall warts
   -  2× Webcams (de-boxed)
   -  1× JTAG adapter
   -  2× USB cables

.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test

.. _circuits-from-the-lab cn0566 assy_prod_test:

CN0566 Assembly and Production Test
===================================

Assembly and Production Test Procedure for ADALM-PHASER (CN0566).

.. video:: https://www.youtube.com/watch?v=WR1DHfraLf8

Assembly
--------

1. Install the u.fl cables as shown. Ensure that the connector is aligned before
   seating, and use a flat surface to press, such as an unused pencil eraser:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/u_fl_cables.jpg
      :width: 400px

2. Install the 40-pin M-F extender on the reverse side of the board. Place the
   board on stiff antistatic foam while doing this, and use a steady, even
   pressure.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/Rpi_riser.jpg
      :width: 400px

3. Install a 22 mm M-F standoff and 12 mm M-F standoff as shown below. The
   threads from the 22 mm standoff enter from the reverse side of the board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/standoff_stackup.png
      :width: 400px

4. Install the camera mount using two 3 mm pan head screws as shown. Do not
   over-tighten.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/camera_mount.jpg
      :width: 400px

5. Install the four tall standoffs from the top side of the board, at the four corners.

   .. note::

      Photo of four corner standoffs, so the Pi can be assembled easily.

6. Prepare the ADALM-Pluto:

   - Remove the board from the enclosure, leaving the SMA panel intact
   - Solder the 14-pin header as noted.
   
   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/pluto_prep.jpg
      :width: 400px

7. Mount the ADALM-Pluto from the top side of the board. Note that the threaded
   ends of the standoff will need to be flexed slightly. Secure with 4x M2.5
   nylon nuts.

8. Connect the U.FL cables to the ADALM-Pluto as shown:

#. The previously installed RX2 cable from the CN0566 board to Pluto RX2A
#. Snap the second cable onto the SMA to U.FL adapter.
#. Snap the other end of the second cable onto Pluto TX2A, then snake the
   adapter between the Pluto and CN0566, thread onto CN0566 TX_IN SMA.
#. Install a 90-degree SMA adapter onto CN0566 J1 as shown, facing downward.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/pluto_u_fls.jpg
      :width: 400px

9. Connect the 14-pin ribbon cable between CN0566 and Pluto as shown:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/ribbon_cable_installation.jpg
      :width: 400px

#. Mount the Raspberry Pi from the reverse side of the board. Use 4x M2.5 x 4
   mm pan head screws to secure.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/rpi_mounting.jpg
      :width: 400px

Test
----

Place the Vivaldi antenna / Selfie-Stick directly above the assembly as shown.
The antenna should aim directly down at the center of the array:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/assy_prod_test/test_front_view.jpg
   :width: 400px

Plug a micro HDMI to HDMI cable into the Raspberry Pi HDMI connector closest to
the USB-C power input.

Insert a pre-prepared SD card into the Raspberry Pi. (See below for preparation
instructions.)

Plug a keyboard into one of the remaining USB ports on the Raspberry Pi (A mouse
is optional.)

Connect a 3 Amp USB-C power adapter to the power input on the CN0566. The
Raspberry Pi will boot.

Create an SD card by following the instructions here:
:dokuwiki:`quickstart </resources/eval/user-guides/circuits-from-the-lab/cn0566/quickstart>`

Type the following command:

::

   cd ~/pyadi-iio/examples/phaser
   python3 phaser_prod_tst.py

Then press enter. The test script will automatically run and print pass / fail
results.

Example test results (taken from a random board on May 24, 2025). Your results
may differ a bit.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/example_test_results.png
   :width: 600px

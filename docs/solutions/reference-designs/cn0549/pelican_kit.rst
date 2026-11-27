CN0549 CbM Pelican Kit
======================

This page describes how to create a standalone CN0549 CbM kit that
can travel with you anywhere. The following steps assume that you have
already completed the instructions for assembling the CN0549 system. If
you have not configured the hardware or software, please visit the
:doc:`CN0549 User Guide </solutions/reference-designs/cn0549/cn0549>`
before continuing with this kit.

Required Materials
------------------

Hardware:

-  :adi:`EVAL-CN0532-EBZ`
-  :adi:`EVAL-CN0540-ARDZ`
-  :adi:`EVAL-XLMOUNT1`
-  Cabling the CN0532 to the CN0540

   -  `1m Shielded male to male SMA cable <https://www.digikey.com/135101-02-M1.00>`_ or
   -  Twisted pair set of wires cut to the desired length

-  `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
-  `Class 10 16GB SD Card <https://www.amazon.com/gp/product/B073K14CVB>`_
-  `USB OTG <https://www.amazon.com/Rankie-Female-Adapter-Convertor-3-Pack/dp/B00YOX4JU6>`_ (micro USB to USB Type A female USB 2.0 compatible)
-  `Pelican Case 1400 w/Foam <https://www.pelican.com/us/en/product/cases/protector/1400>`_
-  `10.1 Inch HDMI Display <https://www.amazon.com/gp/product/B076GZVCP2>`_
-  `HDMI cable (male to male) <https://www.monoprice.com/product?p_id=24187>`_ (2 ft length)
-  `USB Wireless Keyboard + Mouse <https://www.amazon.com/Wireless-Keyboard-Jelly-Comb-Portable/dp/B0756XFFJZ>`_ (must be less than 11.5 inches wide and 4.5 inches tall)

Software:

-  `ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/2021-02-18-ADI-Kuiper-CN0540.img.xz>`_

Creating a Pelican Kit
----------------------

The following sections describe how to integrate the CN0549 into a single Pelican case for easy use, transport, and shipping. 
These instructions assume that you have already completed the CN0549 hardware, software, and system setup. 
If you have not configured the hardware or software, please visit the :doc:`CN0549 User Guide </solutions/reference-designs/cn0549/cn0549>`.

Mount the HDMI Monitor
~~~~~~~~~~~~~~~~~~~~~~

Mount the HDMI monitor inside the Pelican 1400 case on the lid side. To do this, you must cut into the foam provided in the case.

-  Align the edge of the monitor with the left-hand side of the case as shown in the picture. This will leave about 2 inches of foam on the right-hand side.

.. image:: images/pelican_case_monitor_positioning.jpg
   :width: 400

-  Position the monitor approximately 1 inch from the top and 2 inches from the bottom edge of the foam.

|image1|

.. image:: images/pelican_case_monitor_foam_bottom_width.jpg
   :width: 400

-  Cut around the outline of the monitor using a very sharp knife.

.. image:: images/pelican_case_monitor_foam_cutting.jpg
   :align: center
   :width: 400

-  After cutting out the monitor opening, it should look like this.

.. image:: images/pelican_case_monitor_foam_outline.jpg
   :align: center
   :width: 400

-  After cutting the monitor placement, adhere it to the Pelican case lid. Cut 4 Velcro strips and place them on the back of the monitor as shown below. Do not cover venting holes or other important access points.

.. image:: images/pelican_case_monitor_velcro.jpg
   :align: center
   :width: 400

-  On the right-hand side, you will see the connector panel. Connect the HDMI cable and the DC barrel jack to the monitor.

|image2|

.. image:: images/monitor_input_power_connected.jpg
   :width: 410

-  Use the monitor to align the other side of the Velcro with the case. Remove the adhesive backing and insert the monitor into the Pelican case lid. Apply light pressure to ensure a stable connection, but not so much as to damage the screen.

|image3|

.. image:: images/cn0549_pelican_case_buildup_monitor.jpg
   :width: 400

Cutting the Foam
~~~~~~~~~~~~~~~~

All other items needed to run the demo must fit inside this Pelican case. There are several possible layouts, but the following steps describe an optimal arrangement.

Begin by preparing the foam. The Pelican case includes foam that is perforated into 0.5 inch squares. This allows you to customize the layout and fit the components in the case.

-  Lift the foam block from the main basin of the Pelican case and remove the thin, single piece of foam located at the bottom. Place it aside for later use.
-  When viewed from the top, the foam has an outer non-perforated layer and an inner perforated grid.
-  Remove all the foam pieces shown in blue using the grid pattern outlined below. Note that the outer edge is non-perforated.

|image4| |image5|

.. important::

   Remove the foam in 5 or 6 large sections. You will need this foam later as padding for the bottom of the case.

-  Create padding using the foam removed in the previous steps.
-  There are 3 different padding heights, divided by equipment section.

.. image:: images/pelican_case_foam_cutout_grid_map2.png
   :align: center
   :width: 400

-  Keyboard == No padding
-  HDMI and power cords == 1 inch of padding
-  DAQ, FPGA, sensor, mounting block, USB OTG, mouse == 1.5 inches of padding

-  After cutting the padding, reinsert it into the foam cutout. If you follow these steps correctly, your Pelican case should look like this.

.. image:: images/cn0549_pelican_case_buildup_keyboard2.jpg
   :align: center
   :width: 400

Equipping the Pelican ase
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Begin placing the required items into your Pelican case for standalone operation.
-  The keyboard should be the first item placed into the assigned foam slots.

.. image:: images/cn0549_pelican_case_buildup_keyboard3.jpg
   :align: center
   :width: 400

-  Next, connect the DE10-Nano to the CN0540, CN0532, mounting block, SMA cable, and USB OTG adapter, then place them in their assigned positions.

.. image:: images/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg2.jpg
   :align: center
   :width: 400

-  Coil the wires for the CN0532, mounting block, SMA cable, and USB OTG cable neatly so they fit into the correct position. Place the wireless mouse on top of these.
-  Attach the HDMI cable and the DC barrel jack to the DE10-Nano. Coil the cables so that everything fits into its assigned position.

.. image:: images/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg_mouse_hdmi_power1.jpg
   :align: center
   :width: 400

-  When everything is complete, the main basin of the Pelican case should look like this.

.. image:: images/cn0549_pelican_case_buildup_cn0540_cn0532_de10_otg_mouse_hdmi_power2.jpg
   :align: center
   :width: 400

-  The entire open CN0549 case should look similar to this.

.. image:: images/pelican_case_complete_open2.jpg
   :align: center
   :width: 400

-  Before closing the lid, add the protective foam to prevent damage to the HDMI monitor.

.. image:: images/pelican_case_complete_open_protected2.jpg
   :align: center
   :width: 400

-  You are now ready to close the case and transport your setup.

.. image:: images/cn0549_pelican_case_complete_closed.jpg
   :align: center
   :width: 400

*End of Document*

.. |image1| image:: images/pelican_case_monitor_foam_top_width.jpg
   :width: 280
.. |image2| image:: images/monitor_input_power_ports.jpg
   :width: 380
.. |image3| image:: images/pelican_case_velco.jpg
   :width: 400
.. |image4| image:: images/pelican_case_foam_cutout_grid2.png
   :width: 400
.. |image5| image:: images/pelican_case_foam_cutout_grid_legend2.png
   :width: 400

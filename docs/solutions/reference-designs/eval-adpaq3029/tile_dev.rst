.. _eval-adpaq3029 tile_dev:

EVAL-ADPAQ3029 - Tile (GUI) development (Obsolete)
==================================================

.. warning::

   This page is obsolete. The Moduware app has been discontinued and is no
   longer available on the Google Play Store, and the Moduware website is no
   longer reachable, so the steps below may no longer work. The closest
   available alternative is the
   `Moduware React Native prototype app <https://github.com/moduware/moduware-react-native-prototype>`__,
   which has not been tested with the EVAL-ADPAQ3029.

Application development for the Moduware platform consists of two primary parts:
Firmware and Web based GUI application.

Firmware
--------

The firmware for the application development can be created in CrossCore Embedded Studio as explained in the previous section. CrossCore Embedded studio works with C programming language to access the hardware of the Dev Module. Using the Dev Module files, the Module Development Kit (MDK) is able to act as a median between the hardware and Web based software. Running a continuous loop, the MDK checks for any events or interrupts and uploads the corresponding data to the API via ``np_api_upload``. After being uploaded, the data response can be pulled from the tile app.

GUI Application
---------------

Moduware Modpack Tiles are created through the web based application consisting
of:

-  ``driver.json``: register commands allowing the web based tile to communicate with the hardware registers (0x2700-0x27FF). Formatting of return data (0x2800+)
-  ``index.html``: User interface (ie: buttons, displays, etc.)
-  ``NexpaqHeader.js``: Event based functions allowing callbacks
-  ``Scripts.js``: Custom functions executed based on events ie: Button presses, returns from firmware package

Development
~~~~~~~~~~~

Please find the example source code for Tile development in :ref:`resources <eval-adpaq3029 resources>` page.

-  The files that make up the tile can be opened and edited in any text editor.
-  Begin by initializing any functions declared in the MDK_REGISTER_CMD in the .json file.
-  In the same .json file create the format for the data to be read.
-  In the index.html file, the user interface can be created. This is where all buttons, displays, and text is programmed.
-  Open up the scripts.js file located in the js folder.

   -  Event listeners using the variables declared in index.html i.e: document.addEventListener(‘click’, function(e))
   -  Event listeners can call other functions within scripts.js
   -  Functions called by an event listener can remain local or make a callback
      to the firmware to obtain data or change the state of the hardware

Deployment
~~~~~~~~~~

Installing Moduware App
^^^^^^^^^^^^^^^^^^^^^^^

-  Install the basic version of the Moduware app that could be downloaded from
   the website moduware.com/app. The app was also available on Google Play Store.
-  Once the application is installed, launch the application. The following GUI
   is displayed when the application is opened.

.. image:: images/tile2.png
   :align: center
   :width: 400

-  Click on ``FIND MODUWARE`` option to scan the devices available near you. Select the right device (the mini-dev board) and pair it.

.. image:: images/tile3.png
   :align: center
   :width: 400

-  Once the connection is established between phone and the gateway, the screen
   appears as shown in the image.

.. image:: images/tile4.png
   :align: center
   :width: 400

-  Since the Moduware phone backpack supports up to 6 slots to connect 6
   different modules, the application shows 6 tiles. Since there is no firmware
   in the module and no tile has been stored in the mobile device memory, a
   dummy tile is displayed on the screen.

.. note::

   Make sure you turn on bluetooth before scanning for devices

Installing Tile GUI
^^^^^^^^^^^^^^^^^^^

Once Tile development is complete and ready to test/run on smartphone:

-  Now, connect the smartphone to PC using USB in File transfer mode.
-  You should be able to see a new drive where files in Phone memory are visible.
-  Navigate to ``Moduware`` app directory and copy the whole tile source code directory to it.
-  If you could not find the ``Moduware`` directory, create a new one.
-  Make sure that the tile project files are within the folder named ``Moduware.tile.example-name``, where “name” is any project name.
-  Eject the smartphone drive and launch the moduware app again.
-  Connect the module/gateway as explained previously.
-  Now you should be able to see the new Tile GUI showing ``DevMod``.

.. image:: images/tile5.png
   :align: center
   :width: 400

.. note::

   Many a times, there may be a dummy tile being dispalyed on the ``Moduware`` app as seen in the image. In this case, just disconnect the power cable from the modules and connect them back again.\
.. image:: images/tile6.png
   :align: center
   :width: 400


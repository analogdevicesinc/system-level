.. _analog-attach:

Analog Attach
=============

.. note::

   This section only gives an overview on Analog Attach, for all details, see
   :external+analog-attach:doc:`the dedicated doc <index>`.

Analog Attach is a VS Code extension for creating and editing Device Tree
files (DTS) and Device Tree Overlay (DTSO) files with schema validation,
binding support, and remote deployment capabilities.

Get it from the `VS Code Marketplace <https://marketplace.visualstudio.com/items?itemName=AnalogDevices.analog-attach>`__,
the extension source code is available at :git-analog-attach:`/`.

Requirements
------------

Analog Attach requires:

#. A valid Linux kernel repository (for example, ``analogdevicesinc/linux``)
   configured in settings
#. C compiler (gcc) for precompiling dts/dtso files
#. Device Tree Compiler (dtc)
#. SSH for connecting to a device
#. sshpass for password authentication during deployment

Getting Started
---------------

.. tip::

   See :external+analog-attach:doc:`the installation guide <install/index>` for
   detailed setup instructions.

The extension provides two main views:

* **Plug and Play View** - A graphical editor for creating device tree overlays
  by selecting devices from a catalog
* **Tree Config View** - A tree-based editor for configuring device tree nodes
  with full validation support

Support
-------

Documentation
~~~~~~~~~~~~~

-  All Analog Attach documentation is available :external+analog-attach:doc:`here <index>`.

Other Useful Links
~~~~~~~~~~~~~~~~~~

-  :git-analog-attach:`Source </>`
-  `VS Code Marketplace <https://marketplace.visualstudio.com/items?itemName=AnalogDevices.analog-attach>`__

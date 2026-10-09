Streaming Data from the CN0549 into Python Tools
================================================

This page is going to discuss how to use the :adi:`CN0549` 
Machine Learning Enablement Platform for streaming high fidelity 
analog sensor data from a device under test (DUT) into Python-based 
data analysis tools such as Tensorflow and Keras. The goal is that 
once you have the data in these tools, you'll be able to create 
your own algorithms and train your system using your own data.

This page will outline how to get the data from the sensor all the way
to Python, using open source hardware and software from Analog Devices.
At the end of this page links will also be provided to specific examples
done in Tensorflow or Keras, where you can recreate each examples using
the training data and scripts provided.

Requirements
------------

.. important::

   This user guide page assumes that you have the complete CN0549 system put together.
   This includes both hardware and software setup. If you have not completed this step, 
   please refer back to the :doc:`CN0549 User Guide </solutions/reference-designs/cn0549/cn0549>` on how to get setup.

Hardware:

-  Ethernet Cable
-  Router or network connection
-  Mini USB to USB type A cable
-  PC or Laptop

Software:

-  `Download Python 3.6 or higher <https://www.python.org/downloads/>`_
-  `Download libiio <https://github.com/analogdevicesinc/libiio>`_
-  pyADI-iio

Preparing your PC/Laptop
~~~~~~~~~~~~~~~~~~~~~~~~

-  Install Python and Libiio onto your laptop.
-  Open up the Python command prompt (this may be different than your Windows CMD application).
-  Import libiio into Python by using the following command.
   
   .. code:: python
   
      pip install pylibiio

-  Install and import pyadi-iio into Python by using the following command.

   .. code:: python
   
      pip install pyadi-iio

System Setup
------------

-  Ensure your CN0549 System is connected together. If you need to setup the CN0549, 
   please refer back to the :doc:`user guide </solutions/reference-designs/cn0549/cn0549>`.

.. tip::
   
   The user guide shows the USB OTG connector and the HDMI cable installed, but
   those two steps will not be needed here since we are streaming data over the
   network into the laptop.

-  Connect the other end of the Ethernet cable into a router or other network
   connection. This will be the easiest way to stream and save the data.

.. note::

   If you don't have a network available and want to stream data directly 
   from the Ethernet port of the DE10-Nano to the Ethernet port of your PC 
   that is still possible, but requires some extra configuration. 
   Please see the :dokuwiki:`Network Configuration </resources/tools-software/linux-software/network-config>` 
   page for complete details.

-  Plug the mini USB cable into the UART connector of the DE10-Nano.
-  Plug in the USB cable (from the UART of DE10-Nano) into your PC's USB port.

   -  A driver for the board should automatically be detected and installed on your PC. 
      If this does not happen you may have to manually install that driver in order to continue. 
      Here is a link to the `UART Serial Driver <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>`_

-  Plug the power supply into the wall outlet and use the DC barrel jack to
   power up the CN0549 setup.

.. image:: images/cn0549_python_generic_sw_blk_dig.png
   :align: center
   :width: 1200

Finding your DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~

Before you can start gathering data, you first must locate the CN0549 system
setup on your network.

-  Set up a UART serial communication between your PC and the DE10-Nano board using the micro USB cable to USB type A
-  Using your device manager, locate the COM port assigned to the DE10-Nano board

.. image:: images/com_port.png
   :align: center
   :width: 600

-  Open Putty, Tera Term, or other serial terminal program and open a terminal between the COM port the DE10-Nano board by setting the Baud rate to **115200**, and pressing "Connect".
-  You'll now be prompted to provide a user name and password.

.. note::

   | Use the following credentials for Analog Devices Kuiper Linux
   
   | Username = analog 
   | Password = analog

   | Press the Enter key between each.

-  Type **ifconfig** into the terminal, hit "Enter"
-  That should echo back some information where you can pull out the inet
   address of eth0.

.. image:: images/serial_terminal_linux_ifconfig_inet.png
   :align: center
   :width: 600

Connecting to the CN0549 via Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With your system fully setup, it's now time to stream data directly into Python.

Data streaming and device control are provided through the python classes in 
`pyadi-iio <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_. 
Devices or sensors which connect through the CN0540, such as the CN0549, 
will share a common base class called :external+pyadi-iio:doc:`adi.cn0540 <devices/adi.cn0540>`. 
However, each specific sensor will have its own class that will contain documentation, methods, 
and properties specific to it. Therefore, end users should always use the python class associated with the sensor and not the CN0540.

Below is a basic example where we will talk to a CN0540 with CN0549 attached. This is done remotely from a host PC, 
but can be done locally on the board or through another backend. 
See the :external+pyadi-iio:doc:`pyadi-iio doc for more information <guides/connectivity>`. 
This example can be downloaded from :git-pyadi-iio:`GitHub directly <examples/cn0532_cn0540_basic.py>`.

.. code:: python

   # Import the module
   import adi
   # Define the URI we use to connect to the remote device
   uri = "ip:analog"
   # Connect to the device
   xl = adi.cn0532(uri)
   # Set number of samples to capture
   xl.rx_buffer_size = 2**12
   # Pull rx_buffer_size samples back from the device
   data = xl.rx()

The example above can be run from a command prompt of terminal as:

.. code:: bash

   python3 cn0532_cn0540_basic.py

or by loading into your favorite editor like Spyder, VSCode, or PyCharm. Once run the return object ``data`` will be a numpy array of 32-bit integers of shape ``(2^12,1)``. Numpy is a common type used in many numerical libraries.

For further details about pyadi-iio consult the :external+pyadi-iio:doc:`documentation on GitHub <index>`, or look at more examples in the :git-pyadi-iio:`examples folder <examples>`.

Machine Learning Examples
-------------------------

A key purpose of the CN0540 platform is to help aid in condition-based monitoring applications. 
A common tool used in that space is machine learning, where algorithms are trained for system identification, 
anomaly detection, or for other purposes. For those familiar with Tensorflow an example has been created 
to outline a machine identification problem, with datasets created from the CN0540+CN0549 mounted to a physical piece of hardware. 
This example is provided in the form of a `Jupyter Notebook <https://jupyter.org>`_, which is a common medium for sharing code and implementations.

-  :git-pyadi-iio:`Tensorflow Classification Example using an Oscillating Fan [Notebook <examples/cn0549/ml_fan_example.ipynb>`]
-  :git-pyadi-iio:`Tensorflow Classification Example using an Oscillating Fan [Python script] <examples/cn0549/ml_cn0532.py>`
-  :git-pyadi-iio:`Tensorflow Classification Example using an Oscillating Fan [Data collection script] <examples/cn0549/collect_data.py>`

*End of Document*

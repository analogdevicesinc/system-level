Enabling Flexible Data Acquisition Across Mixed Vendor Compute Platforms
================================================================================

ADI DataX™ unifies application portability across heterogeneous
compute environments, enabling reusable workflows for data acquisition and
processing. Developers can scale complexity as needed, from rapid prototyping to
advanced system refinement. The solution highlights modularity, consistency, and
efficiency in building multi‑vendor data pipelines. This approach significantly 
reduces integration overhead and accelerates product development.

Resources
--------------------------------------------------------------------------------
- Zephyr: :git-zephyr:`EVAL-CN0391-ARDZ <https://github.com/MaureenHelm/zephyr/tree/eval_cn0391_ardz>`
- no-OS: :git-noos:`EVAL-CN0391-ARDZ <https://github.com/analogdevicesinc/no-OS/tree/staging/eval-cn0391-ardz:>`
- Hardware: 
  
  - :adi:`AD-APARD32690-SL Rev. E <ad-apard32690-sl>`
  - :adi:`AD-APARDPFW-SL <ad-apardpfw-sl>`
  - :adi:`EVAL-ADIN1110 <eval-adin1110>`
  - :adi:`EVAL-CN0391-ARDZ <cn0391>`
  - :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>`

Block diagram
--------------------------------------------------------------------------------

.. figure:: demo_block_diagram.svg
   :align: center

   Block diagram of the demo setup.


Demo description
--------------------------------------------------------------------------------
This demo illustrates the flexibility of ADI DataX™ in enabling data acquisition
across mixed vendor compute platforms. The system integrates ADI's data 
acquisition hardware with a variety of compute platforms, including Zephyr RTOS 
and no-OS. The demo showcases the seamless connectivity and data flow between 
the hardware and software components, demonstrating how developers can easily 
build and deploy data acquisition workflows across different environments. By 
leveraging ADI DataX™, developers can focus on application development without 
worrying about the complexities of integration, enabling faster time-to-market 
for their products.

In this demo setup, the Raspberry Pi, running :adi:`Kuiper 2 <kuiper>`, serves
as the central aggregation unit, communicating with the ADI hardware components
to acquire data using the  :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>` via T1L
connections.

The :adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>` powers the :adi:`AD-APARDPFW-SL <ad-apardpfw-sl>`
which powers the :adi:`AD-APARD32690-SL <ad-apard32690-sl>` and forwards power 
to the :adi:`EVAL-ADIN1110 <eval-adin1110>`.

To demonstrate the flexibility of DataX™, the :adi:`AD-APARD32690-SL <ad-apard32690-sl>`
runs Zephyr RTOS, while the :adi:`EVAL-ADIN1110 <eval-adin1110>` runs no-OS. 
Both of the boards have an :adi:`EVAL-CN0391-ARDZ <cn0391>` connected to them, 
which is used to read the temperature using 4 thermocouples each.
The system can be interchanged, by simply compiling the Zephyr application for
the :adi:`EVAL-ADIN1110 <eval-adin1110>` and the no-OS application for the
:adi:`AD-APARD32690-SL <ad-apard32690-sl>`, demonstrating the ease of using
DataX™ in enabling data acquisition across mixed vendor compute platforms.


Required Hardware
--------------------------------------------------------------------------------

.. csv-table::
    :file: hardware_table.csv

Building steps
--------------------------------------------------------------------------------

Raspberry Pi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For detailed instructions on configuring the Raspberry Pi with the
:adi:`AD-RPI-T1LPSE-SL <ad-rpi-t1lpse-sl>`, please refer to the
:ref:`ad-rpi-t1lpse-sl` documentation:

- :ref:`software-setup` - Building and flashing the Micro-SD card
- :ref:`setting-up-static-ip` - Configuring a static IP address


Zephyr RTOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This project builds an Industrial I/O Daemon (iiod) with network support on the 
APARD32690 platform. It enables remote access to industrial I/O devices over the 
network using the Libiio v.1.0 library run on Zephyr RTOS.
The monitored device here is an ad7124 which exposes 4 virtual channels for 
reading the temperature from 4 different Type K thermocouples. 
The data can be visualized using Scopy, which connects to the iiod running on the 
APARD32690 board.

Setting Up the Zephyr Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to build the Zephyr application, you need to set up the Zephyr environment. 
Please follow the instructions on `Zephyr Getting Started Guide <https://docs.zephyrproject.org/latest/develop/getting_started/index.html>`_ to do so. 
Make sure to install all the required dependencies and initialize the Zephyr workspace before proceeding to the next steps. 

Getting Libiio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the latest version of Libiio into the Zephyr project by updating *west.yml*. 
Add the following lines under `remotes`:

.. code-block:: yaml

   manifest:
    - name: libiio
      url-base: https://github.com/analogdevicesinc

Add the following lines under `projects`:

.. code-block:: yaml

    - name: libiio                                                                                    
      path: modules/lib/libiio
      revision: main

Run this command to update the Zephyr project with the new manifest:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   ~/zephyrproject/zephyr
   $west update

You should now have Libiio in the Zephyr project under *modules/lib/libiio*.

Build and Run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To further emphasize the way ADI DataX™ allows software to efortlessly accomodate 
hardware changes, there are 2 possible setups for this Zephyr project. The only 
software and hardware difference between the two is the inclusion or exclusion of the 
AD-APARDPFW-SL shield from the build command and from the physical setup, as 
explained below:

 1) Both the AD-APARDPFW-SL shield and the EVAL-CN0391-ARDZ shield connected to the AD-APARD32690-SL board.
    AD-APARDPFW-SL powers the AD-APARD32690-SL and establishes the ethernet connection over SPI0.

      Build the application for this setup using the following command:

      .. shell::
         :user: analog
         :group: analog
         :show-user:

         ~/zephyrproject/zephyr   
         $west build -p always -b apard32690/max32690/m4 ../modules/lib/libiio/zephyr/samples/iiod/ -S iiod-network --shield eval_cn0391_ardz --shield ad_apardpfw_sl


 2) Only EVAL-CN0391-ARDZ shield connected to the AD-APARD32690-SL. 
    The AD-APARD32690-SL is externally powered through the USB and uses SPI4 to communicate via ethernet.

      Build the application:

      .. shell::
         :user: analog
         :group: analog
         :show-user:

         ~/zephyrproject/zephyr   
         $west build -p always -b apard32690/max32690/m4 ../modules/lib/libiio/zephyr/samples/iiod/ -S iiod-network --shield eval_cn0391_ardz

Then flash:

.. shell::
   :user: analog
   :group: analog
   :show-user:
   
   ~/zephyrproject/zephyr
   $west flash --runner openocd

.. Note::
   This flashing process requires the ADI distribution of OpenOCD to be installed. Details on how to 
   install it can be found on `ADI OpenOCD GitHub <https://github.com/analogdevicesinc/openocd#:~:text=%23%20Building%20OpenOCD%0A%0AThe,sudo%20make%20install>`_.

   If you have problems with the flashing process, please append the build command with 
   ``-DOPENOCD=<path_to_your_adi_openocd>`` and rebuild. You should see *<path_to_your_adi_openocd>* 
   in *./build/zephyr/runners.yaml*, under *config -> openocd*.

By connecting to the serial communication of the board (e.g.: ``minicom -D /dev/ttyACM0 -b 115200``) 
and resetting the AD-APARD32690-SL board, the following output should be observed for each configuration:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Configuration 1 (with AD-APARDPFW-SL)
     - Configuration 2 (without AD-APARDPFW-SL)
   * - .. code-block::

          Hello World! apard32690/max32690/m4
          [00:00:00.176,000] <inf> phy_adin: PHY 1 ID 283BCA1
          [00:00:00.178,000] <inf> phy_adin: PHY 1 2.4V mode supported
          [00:00:00.180,000] <inf> phy_adin: PHY 2 ID 283BCA1
          [00:00:00.182,000] <inf> phy_adin: PHY 2 2.4V mode supported
          *** Booting Zephyr OS build v4.3.0-5400-g0c770e917768 ***

     - .. code-block::

          Hello World! apard32690/max32690/m4
          [00:00:00.150,000] <inf> phy_adin: PHY 1 ID 283BCA1
          [00:00:00.152,000] <inf> phy_adin: PHY 1 2.4V mode supported
          *** Booting Zephyr OS build v4.3.0-5400-g0c770e917768 ***

no-OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project builds an Industrial I/O Daemon (iiod) with network support on the
EVAL-ADIN1110 platform. It enables remote access to industrial I/O devices over the
network using the Libiio v.0.x library run on no-OS environment.
The monitored device here is an :adi:`AD7124-8 <AD7124-8>` which exposes 4
virtual channels for reading the temperature from 4 different Type K 
thermocouples. The data can be visualized using Scopy, which connects to the 
iiod running on the EVAL-ADIN1110 board.

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ADIN1110_Hw_Config.png
   :align: center
   :width: 600 px

   EVAL-ADIN1110 hardware configuration

.. note::
   The EVAL-CN0391-ARDZ can be powered only through the USB port of the EVAL-ADIN1110
   board for this particular setup.

Setting Up the no-OS Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to build the no-OS application, you need to set up the no-OS environment.
Please follow the instructions on the :git-noos:`no-OS Build Guide <build_guides/build_guides:>`
to do so. Make sure to install all the required dependencies (GNU Make, ARM GCC
toolchain, and OpenOCD) before proceeding to the next steps.

Build and Run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After setting up the environment, build the application using the following command
from the no-OS root directory:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   ~/no-OS
   $make -j$(nproc) -C projects/eval-cn0391-ardz EXAMPLE=iio_lwip_example ADIN1110_STATIC_IP=y

Then flash:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   ~/no-OS
   $make -C projects/eval-cn0391-ardz run

The default static IP address is ``192.168.90.60``. You can override this by
specifying the following parameters during compilation:

- ``NO_OS_IP`` - The static IP address
- ``NO_OS_NETMASK`` - The network mask
- ``NO_OS_GATEWAY`` - The gateway address

For example:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   ~/no-OS
   $make -j$(nproc) -C projects/eval-cn0391-ardz EXAMPLE=iio_lwip_example ADIN1110_STATIC_IP=y NO_OS_IP=192.168.97.101 NO_OS_NETMASK=255.255.255.0 NO_OS_GATEWAY=192.168.97.1

You are now ready to connect to the board using Scopy and start acquiring data from
the thermocouples. To do this, follow the steps below:

   1) Open Scopy and enter the URI of the EVAL-ADIN1110 board (``ip:192.168.90.60``), then click **Verify**.
   2) Click **Add Device** with both *DataLogger* and *Debugger* selected.
   3) Then click **Connect**.
   4) Go to the **Data Logger** tab, select the channels you want to display and then click **Start** to start acquiring data from the thermocouples.

Scopy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You are now ready to connect to the board using Scopy and start acquiring data from the thermocouples.
To do this, follow the steps below, also explained in the video:

   1) Open Scopy and enter the URI of the APARD32690-SL board (``ip:192.168.97.100``), then click **Verify**. 
   2) Click **Add Device** with both *DataLogger* and *Debugger* selected.
   3) Then click **Connect**.
   4) Go to the **Data Logger** tab, select the channels you want to display and then click **Start** to start acquiring data from the thermocouples.

   .. figure:: scopy_connect.gif
      :align: center
      :width: 600 px

      Connecting to the boards using Scopy.

   .. note::
      Use ip:192.168.97.100 for AD-APARD32690-SL or ip:192.168.90.60 for EVAL-ADIN1110EBZ.
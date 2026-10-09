.. _eval-ad7616-sdz quickstart zedboard:

ZedBoard Quick Start Guide
===============================================================================

.. image:: ../../images/ZedBoard.png
   :width: 500

.. esd-warning::

This guide provides quick instructions on how to setup the
:adi:`EVAL-AD7616SDZ` on:

- :xilinx:`ZedBoard` using the :adi:`SPD-I-FMC` adapter

Using no-OS as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed:

- HDL boot file: ``system_top.xsa``
- no-OS project: :git-no-OS:`projects/ad7616-sdz`

Instructions on how to build the HDL boot file from source can be found here:

- :external+hdl:ref:`ad7616_sdz` build documentation.
  More HDL build details at :external+hdl:ref:`build_hdl`.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx Vivado and Vitis (downloading Vitis from
  `here <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_
  will include Vivado as well)
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud rate 115200 (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :xilinx:`ZedBoard` FPGA board and its power supply (12 V DC)
- :adi:`EVAL-AD7616SDZ` evaluation board and a 7 V to 9 V DC power supply (J7)
- :adi:`SDP-I-FMC` adapter board
- 2x Micro-USB cables, one for UART (J14) and one for JTAG (J17)

More details as to why you need these, can be found at
:ref:`eval-ad7616-sdz prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`EVAL-AD7616SDZ` to the :adi:`SPD-I-FMC` adapter

   .. image:: ../images/ad7616sdp.jpeg
      :width: 500

#. Plug the :adi:`SPD-I-FMC` into the FMC connector of the :xilinx:`ZedBoard`

   .. image:: ../images/zed_ad7616.jpeg
      :width: 500

#. Set the VADJ jumper on the ZedBoard to **3.3 V**

   .. image:: ../images/zed_jumper.jpeg
      :width: 500

   .. warning::

      Because of the :adi:`SPD-I-FMC`, the VADJ level on the ZedBoard must be 
      set to **3.3 V**.

#. Configure the EVAL-AD7616-SDZ resistors (on the back) as follows:

   .. list-table::
      :header-rows: 1

      * - Jumper/Solder link
        - Position
        - Description
      * - SL1
        - Unmounted
        - Channel Sequencer Enable
      * - SL2
        - Unmounted
        - RC Enable Input
      * - SL3
        - Unmounted
        - Selects 1 MISO mode
      * - SL4
        - Unmounted
        - Oversampling Ratio Selection OS2
      * - SL5
        - Mounted
        - If mounted, selects serial interface
      * - SL6
        - Unmounted
        - Oversampling Ratio Selection OS1
      * - SL7
        - Unmounted
        - Oversampling Ratio Selection OS0
      * - LK40
        - A
        - Onboard 5V power supply selected
      * - LK41
        - A
        - Onboard 3.3V power supply selected

   .. note::

      The configuration above selects the **serial** interface (SL5 mounted).
      To use the **parallel** interface instead, unmount SL5.

#. Connect Micro-USB cable to the UART connector (J14) on the ZedBoard and
   to your host PC
#. Connect Micro-USB cable to the JTAG connector (J17) on the ZedBoard and
   to your host PC
#. Connect the power supply to the :xilinx:`ZedBoard`

   .. image:: ../images/zed_connections.jpeg
      :width: 500

#. Connect a 7 V to 9 V DC power supply to the :adi:`EVAL-AD7616SDZ`
   power jack (J7)

   .. image:: ../images/zed_power.jpeg
      :width: 500

#. Ensure both boards share a common ground connection
#. Build the HDL project:

   #. Verify you have the correct version of Vivado installed. The supported
      version is listed on the :git-hdl:`HDL releases page <releases>`.
   #. Build the HDL project to generate the ``system_top.xsa`` file using the
      :external+hdl:ref:`build_hdl` guide.

      .. important::

         The make command varies based on the interface you want to use:

            - **Serial** interface:

            .. code-block:: bash

               $ make SER_PAR_N=1

            - **Parallel** interface:

            .. code-block:: bash

               $ make SER_PAR_N=0
 
#. Refer to the `AD7616 No-Os Example Project <https://analogdevicesinc.github.io/no-OS/projects/ad7616-sdz/#xilinx-platform>`_
   for instructions on how to build and run the no-OS project on the ZedBoard.
#. Turn on the power switch on the ZedBoard
#. Observe console output messages on your terminal (use the first ttyUSB or
   COM port registered)

.. Console output
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Add the console output from the no-OS AD7616 application running on
.. the ZedBoard.

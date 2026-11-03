.. _ad7606x quickstart zed:

ZedBoard Quick Start
================================================================================

.. image:: ../../images/ZedBoard.png
   :align: center
   :width: 600

.. esd-warning::

This guide provides step-by-step instructions on how to set up the
:adi:`EVAL-AD7606B-FMCZ` / :adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>` on:

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  The supported revision is C or higher.

Using no-OS as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed for the system to boot:

- HDL boot file: ``system_top.xsa``
- no-OS project: :git-no-os:`projects/ad7606x-fmc`

Instructions on how to build the boot files from source can be found here:

- :external+no-OS:doc:`projects/adc/ad7606x-fmc`. More no-OS build details
  at :external+no-OS:doc:`build_guide`.
- :external+hdl:ref:`ad7606x_fmc`. More HDL build details at
  :external+hdl:ref:`build_hdl`.

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx Vivado and Vitis (downloading Vitis from
  `here <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_
  will include Vivado as well)
- A UART terminal (Putty/Tera Term/Minicom, etc.), baud rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx `ZedBoard
  <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  Rev C or later, with 12 V power supply
- :adi:`EVAL-AD7606B-FMCZ` or :adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>` FMC evaluation
  board
- 2x Micro-USB cables (one for UART, one for JTAG)
- Signal generator capable of ±10 V or ±5 V output (to drive analog inputs)

More details as to why you need these can be found at
:ref:`eval_ad7606x prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/zed_ad7606_setup.jpeg
   :align: center
   :width: 800

Follow the steps in this order to avoid damaging the components:

#. Get the `ZedBoard
   <https://digilent.com/reference/programmable-logic/zedboard/start>`__.
#. Configure ZedBoard for JTAG boot by setting the BOOT mode switches
   (JP7–JP11) and MIO0 jumper (JP6) for JTAG mode. VADJ (JP18) should be set 
   to 2.5 V.

   .. image:: ../../images/zed_mio_jmp.jpeg
      :align: center
      :width: 400

   .. image:: ../../images/zed_vadj_jmp.jpeg
      :align: center
      :width: 400

#. Connect your signal generator to the analog inputs of the evaluation board
   using SMB cables (V1± through V8±, or V1± through V4± for the AD7606-4).
#. Plug the :adi:`EVAL-AD7606B-FMCZ` into the FMC LPC Connector (J1).

   .. image:: ../images/zed_ad7606.jpeg
      :align: center
      :width: 400

#. Connect the 12 V power supply to J20 — **do not power on yet**.
#. Connect the UART port (J14) to your PC via Micro-USB.
#. Connect the PROG port (J17) to your PC via Micro-USB (for JTAG).

   .. image:: ../../images/zed_pow_eth_uart_prog.jpeg
      :align: center
      :width: 400

#. Power on the board using the power switch.
#. In Vitis, program the FPGA with the generated ``system_top.xsa`` and
   run the no-OS application on the Zynq PS.
#. Observe output in your serial terminal at 115200 baud (8N1).

.. seealso::

   For more detailed information on ZedBoard jumper settings, check the
   *ZedBoard Hardware User Guide* (chapter "Configuration modes")
   `here <https://digilent.com/reference/_media/zedboard/zedboard_ug.pdf>`__.

.. TODO: uncomment when boot log is available
.. Console output
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..
.. The following is what is printed in the serial console after you have
.. connected to the proper ttyUSB or COM port:
..
.. .. collapsible:: Complete boot log
..
..    ::
..

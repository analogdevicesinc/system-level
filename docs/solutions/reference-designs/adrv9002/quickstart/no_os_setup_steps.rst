Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`EVAL-ADRV9002` FMC board to the
   FPGA carrier FMC socket.
#. Configure `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ for JTAG boot mode (mode MIO[5:2] jumpers in
   the position **0,0,0,0**).
#. Connect USB UART (Micro-USB) to your host PC (J14).
#. Connect USB JTAG (Micro-USB) to your host PC (J17).
#. Connect 12V power supply to barrel jack.
#. Turn on the power switch (SW8) on the FPGA board.
#. Build and run the project using the steps shown in
   :external+no-OS:doc:`here <projects/rf-transceiver/adrv9001>`.
#. Observe console output messages on your terminal (use the first ttyUSB or
   COM port registered).

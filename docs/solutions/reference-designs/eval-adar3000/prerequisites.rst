.. include-template:: ../template/prerequisites.rst.jinja

    prerequisites_ref: eval-adar3000 prerequisites
    carriers_ref: eval-adar3000 carriers
    additional_hardware:
      - ADAR3000/3001-EVALZ evaluation board
      - SDP-I-FMC interposer
      - Two bench power supplies: 1.2 V, 250 mA and 1.8 V, 20 mA
      - JTAG programmer (the ZCU102 on-board USB-JTAG, or an external
        probe), for no-OS
      - SD card with at least 16 GB of memory, for Linux
    additional_software:
      - AMD Xilinx Vivado and Vitis 2025.1
      - :external+kuiper:doc:`Kuiper <index>` SD card image, for Linux
      - :git-libiio:`libiio <releases+>` 1.0.0 or later, for the no-OS IIO
        example
      - UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

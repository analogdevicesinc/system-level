.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad5940/tools/porting_source_code

.. _eval-ad5940 tools porting_source_code:

How to port AD594x Firmware Examples to other Micro controller Families
=======================================================================

The AD594x example projects are written for the ADuCM3029 micro controller.
There are also examples written for the NUCLEO-F411RE board. The example
projects are designed to be easily ported to other micro controllers. This
document details the steps involved.

Source Code Structure
---------------------

This section describes the file structure for the firmware examples. The
following image is a capture from the AD5940_BIA example project opened in Keil
IDE.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/folder_structure.png
   :width: 300px

- AD5940Lib

  - *ad5940.c*

    - This is the main AD5940 library file and contains all library function. No
      modifications should be made to this file.

  - *ADICUP3029.c*

    - Contains specific functions for the ADuCM3029 microcontroller. The
      functions defined in this file will need to be modified according to the
      MCU. Descriptions of each function are outlined below.

- Application

  - *main.c*

    - This is the main file in the program that handles the MCU core
      initialization functions such as configuring Uart interface and MCU system
      clocks. This file needs to be re-written for a new MCU

  - *AD5940Main.c*

    - This file provides high level application control functions such as
      dealing with interrupts and transmitting data. This does not need to be
      modified when porting to a new MCU.

  - *BodyImpedance.c*

    - This file handles the core measurement sequences including sequencer
      configuration, reading data from the FIFO and processing the data. This
      file does not need to be modified when porting to a new MCU.

- CMSIS

* This is the CMSIS pack for the selected MCU. This CMSIS pack should be imported for the particular MCU and should not be edited
* Device

  * This folder has the startup file for the chosen MCU and should not be
    edited.

Porting Functions in ADICUP3029Port.c
-------------------------------------

The main port file between the MCU and AD5940 is the ADICUP3029Port.c file. The
following are the main functions and their purpose:

::

   *AD5940_ReadWriteNBytes(unsigned char*pSendBuffer,unsigned char *pRecvBuff,unsigned long length)
     * This function simply transmits N number of bytes to the AD5940 on the MOSI line and receives the response on the MISO line.
     *The function has 3 input parameters.* pSendBuffer is a pointer to the buffer used to store the data to be transmitted. * pRecvBuff is a pointer to the buffer used to store the results. length is the number of bytes in the buffer to be sent.
   * AD5940_CsClr(void)
     * This function simply drives the GPIO pin connected to the AD5940's CS pin low

- AD5940_CsSet(void)

  - This function sets the GPIO pin connected to the AD5940 CS pin high.

- AD5940_RstSet(void)

  - This function drives the GPIO connected to the AD5940 reset pin high.

- AD5940_RstClr(void)

  - This function drives the GPIO pin connected the AD5940 reset pin low to
    initiate a hardware reset

- AD5940_Delay10us(uint32_t time)

  - This function implements a wait period using the systick timer on the cortex
    core. This function will vary depending on MCU. Take care that this function
    is implemented correctly to ensure the AD5940 library functions correctly.

- AD5940_GetMCUIntFlag(void)

  - This function returns the status of the interrupt flag that is set in the
    external interrupt handler to indicate the AD5940 has generated an
    interrupt.

- AD5940_ClrMCUIntFlag(void)

  - This function clears the interrupt status flag.

::

   *AD5940_MCUResourceInit(void*pCfg)
     * This function initializes and configures the main peripherals for the functions defined above.
        - The GPIOs are configured accordingly for the SPI interface, Reset pin and external interrupt pin
        - The SPI is configured according to the AD5940 datasheet
        - The external interrupt source is enable in the NVIC on the cortex core
        - The CS pin and Reset pin are set high.
   * Ext_Int0_Handler()
   * The interrupt handler handles the interrupt to the MCU when the AD5940 INTC pin generates an interrupt to alert the MCU that data is ready. It sets the ucInterrupted flag to 1.

Porting Functions in main.c
---------------------------

The main.c file only implements 2 functions:

::

   *MCUPlatformInit(void*pCfg)
     * This function initializes the core clocks on the MCU
   * UrtCfg(int iBaud)
     * This function initializes the the Uart interface on the MCU to print results to the Uart.

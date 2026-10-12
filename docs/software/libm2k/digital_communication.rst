.. _libm2k digital_communication:

Digital communication
"""""""""""""""""""""

Libm2k includes bitbang implementations on a variety of protocols.

How to install it?
==================

Windows
-------

In the *Select Additional Tasks* window, select *Install libm2k tools* option.

How to build it?
================

Build and install libm2k. Instruction can be found
:ref:`here <libm2k>`. Make sure to enable tools option.

Enable tools on Linux or OSX
----------------------------

.. shell::

   ~/libm2k/build
   $cmake -DENABLE_TOOLS=ON ../

Enable tools on Windows
-----------------------

Check the *ENABLE_TOOLS* box in CMake GUI.

Protocols
=========

There is a common structure to use for all the protocols when trying to
communicate with other device using libm2k:

* initialize the protocol
* read/write packets
* free the resources allocated  by initialization

Initialization of any protocol can be split into:

* specific attributes initialization
* generic attributes initialization
* protocol descriptor initialization

The structure that stores all ADALM-2000 specific attributes can be found in the
extra header, while all generic attributes are found in the standard header. For
example SPI generic attributes are found in *libm2k/tools/spi.hpp*, while SPI
specific attributes of ADALM-2000 are found in *libm2k/tools/spi_extra.hpp*.

#. Instantiate and set all parameters of the init structure from the extra
   header (m2k_protocol_init).
#. Instantiate and set all parameters of the init structure from the standard
   header (protocol_init_param). This structure contains a parameter called
   extra. The value of this parameter is supposed to be a reference to the
   structure from the extra header.
#. Instantiate a protocol descriptor and then call the init function that will
   populate the descriptor with the information found in initial structures. Use
   this descriptor every time when a writing/reading operation is performed.

SPI
---

Initialization parameters:

* max_speed_hz - write/read frequency
* chip_select - index of any digital pin
* mode - spi mode
* extra:

  * clock - index of any digital pin
  * mosi - index of any digital pin
  * miso - index of any digital pin
  * bit_numbering - {LSB | MSB}
  * cs_polarity - {ACTIVE_LOW | ACTIVE_HIGH}

Functions:

* spi_init - initialize the SPI communication peripheral

  * desc - SPI descriptor
  * param - structure that contains the SPI parameters

* spi_write_and_read - write and read data to/from SPI

  * desc - SPI descriptor
  * data - buffer with the transmitted/received data
  * bytes_number - number of bytes to write/read

* spi_remove - free the resources allocated by spi_init

  * desc - SPI descriptor

Examples:

Include headers

.. code:: c++

   #include <libm2k/m2k.hpp>
   #include <libm2k/contextbuilder.hpp>
   #include <libm2k/tools/spi.hpp>
   #include <libm2k/tools/spi_extra.hpp>

Setup SPI

.. code:: c++

   libm2k::contexts::M2k context = libm2k::contexts::m2kOpen("ip:192.168.2.1");

   // first step of initialization
   m2k_spi_init m2KSpiInit;
   m2KSpiInit.clock = 1;
   m2KSpiInit.mosi = 2;
   m2KSpiInit.miso = 7;
   m2KSpiInit.bit_numbering = MSB;
   m2KSpiInit.context = context;

   // second step of initialization
   spi_init_param spiInitParam;
   spi_init_param.max_speed_hz = 1000000;
   spi_init_param.mode = SPI_MODE_3;
   spi_init_param.chip_select = 0;
   spi_init_param.extra = (void)&m2KSpiInit;

   // third step of initialization
   spi_desc desc = nullptr;
   spi_init(&desc, &spiInitParam);

Write data

.. code:: c++

   uint8_t data[2] = {0xAB, 0xFF};
   spi_write_and_read(desc, data, 2);

Remove the descriptor

.. code:: c++

   spi_remove(desc);
   libm2k::contexts::contextClose(context, true);

I²C
---

Initialization parameters:

* max_speed_hz - write/read frequency
* slave_address - 7/10 bit address
* extra:

  * scl - index of any digital pin
  * sda - index of any digital pin

Functions:

* i2c_init - initialize the I²C communication peripheral

  * desc - I²C descriptor
  * param - structure that contains the I²C parameters

* i2c_write - write data to a slave device

  * desc - I²C descriptor
  * data - buffer with the transmitted data
  * bytes_number - number of bytes to write
  * option - I²C transfer mode

    * 1 = 7 bit addressing
    * 3 = 7 bit addressing with repeated start
    * 4 = 10 bit addressing
    * 6 = 10 bit addressing with repeated start

* i2c_read - read data from a slave device

  * desc - I²C descriptor
  * data - buffer with the received data
  * bytes_number - number of bytes to read
  * option - I²C transfer mode

* i2c_remove - free the resources allocated by i2c_init

  * desc - I²C descriptor

Examples:

Include headers

.. code:: c++

   #include <libm2k/m2k.hpp>
   #include <libm2k/contextbuilder.hpp>
   #include <libm2k/tools/i2c.hpp>
   #include <libm2k/tools/i2c_extra.hpp>

Setup I²C

.. code:: c++

   libm2k::contexts::M2k context = libm2k::contexts::m2kOpen("ip:192.168.2.1");

   // first step of initialization
   m2k_i2c_init m2KI2CInit;
   m2KI2CInit.scl = 0;
   m2KI2CInit.sda = 1;
   m2KI2CInit.context = context;

   // second step of initialization
   i2c_init_param i2CInitParam;
   i2CInitParam.max_speed_hz = 100000;
   i2CInitParam.slave_address = 0x48;
   i2CInitParam.extra = (void)&m2KI2CInit;

   // third step of initialization
   i2c_desc desc = nullptr;
   i2c_init(&desc, &i2CInitParam);

Write and read the data

.. code:: c++

   uint8_t  data_write[] = {0x0B};
   uint8_t  data_read[] = {0};
   i2c_write(desc, data_write, sizeof(data_write), i2c_general_call | i2c_repeated_start);
   i2c_read(desc, data_read, sizeof(data_read), i2c_general_call);

Remove the descriptor

.. code:: c++

   i2c_remove(desc);
   libm2k::contexts::contextClose(context, true);

UART
----

Initialization parameters:

* baud_rate - write/read frequency
* device_id - index of any digital pin
* extra:

  * parity - {NO_PARITY | ODD | EVEN | MARK | SPACE}
  * bits_number - {5 | 6 | 7 | 8}
  * stop_bits - {ONE | ONE_AND_A_HALF | TWO}

Functions:

* uart_init - initialize the UART communication peripheral

  * desc - UART descriptor
  * param - structure that contains the UART parameters

* uart_write - write data to UART

  * desc - UART descriptor
  * data - buffer with the transmitted data
  * bytes_number - number of bytes to write

* uart_read - read data to UART

  * desc - UART descriptor
  * data - buffer with the received data
  * bytes_number - number of bytes to read

* uart_get_errors - check if UART errors occurred

  * desc - UART descriptor

* uart_remove - free the resources allocated by uart_init

  * desc - UART descriptor

Examples:

Include headers

.. code:: c++

   #include <libm2k/m2k.hpp>
   #include <libm2k/contextbuilder.hpp>
   #include <libm2k/tools/uart.hpp>
   #include <libm2k/tools/uart_extra.hpp>

Setup UART

.. code:: c++

   libm2k::contexts::M2k context = libm2k::contexts::m2kOpen("ip:192.168.2.1");

   // first step of initialization
   m2k_uart_init m2KUartInit;
   m2KUartInit.bits_number = 8;
   m2KUartInit.parity = NO_PARITY;
   m2KUartInit.stop_bits = ONE;
   m2KUartInit.context = context;

   // second step of initialization
   uart_init_param uartInitParam;
   uartInitParam.device_id = 0;
   uartInitParam.baud_rate = 9600;
   uartInitParam.extra = (void)&m2KUartInit;

   // third step of initialization
   uart_desc desc = nullptr;
   uart_init(&desc, &uartInitParam);

Write data

.. code:: c++

   uint8_t dataWrite[] = {'A', 'D', 'I'};
   uart_write(desc, dataWrite, sizeof(dataWrite));

Remove the descriptor

.. code:: c++

   uart_remove(desc);
   libm2k::contexts::contextClose(context, true);

Libm2k and no-OS drivers
========================

Analog Devices offers a variety of :git-no-OS:`No-OS drivers <drivers>`
for a variety peripherals in a hardware agnostic format.
These drivers can be interfaced with the libm2k
in order to use the M2K as a master to configure/use the peripheral.
Documentation for the drivers available at :external+no-OS:doc:`drivers_doc`.

In order to integrate libm2k with no-OS drivers some standard steps must be
followed:

* drivers inclusion
* libm2k headers inclusion
* writing the logic

  * C++ file
  * drivers included as external C

Including all required driver files in the project is the first step in
integrating libm2k with no-OS drivers.

The drivers will include some protocols, for example *"i2c.h"*. The afferent
header of libm2k, *libm2k/tool/i2c.hpp*, does not match with the header
included by the drivers (*"i2c.h"*). In order not to modify the drivers we are
going to create a header named after the protocol (*"i2c.h"*) in which the
libm2k header will be included. For example create the *"i2c.h"* header in which
you will include *libm2k/tools/i2c.hpp*.

Each file that will call libm2k methods should be a C++ file. The inclusion of
any driver in a C++ file has to be marked as an external C file inclusion.

Example:

AD5592r can be independently configured as DAC outputs, ADC inputs, digital
outputs, or digital inputs. In this example we are going to generate ascending
voltage values, communicating with the chip using SPI.

- Hardware configuration (ADALM-2000 <- -> AD5592r):

  - SCK: DIO_0 <- -> P4
  - MOSI: DIO_1 <- -> P2
  - MISO: DIO_2 <- -> P3
  - SS: DIO_3 <- -> P1
  - GND: GND <- -> P5
  - VLOGIC: V+ -> P6
  - Oscilloscope: 1+ <- I/O0

- Project structure:

  - ad5592r-base.h
  - ad5592r-base.c
  - ad5592r.h
  - ad5592r.c
  - delay.h
  - delay.c
  - spi.h
  - i2c.h
  - main.cpp

- Get all AD5592r drivers from
  :git-no-OS:`drivers/adc-dac/ad5592r`
- Get delay header from
  :git-no-OS:`include/no_os_delay.h`
- Implement mdelay function from delay.h

.. code:: c++

   #include "delay.h"
   #include <unistd.h>

   void mdelay(uint32_t msecs) {
       usleep(msecs * 1000);
   }

Create spi.h and i2c.h headers (we are not going to use I²C in this example,
but AD5592r drivers include I²C header). In each file include the afferent
header of libm2k.

.. code:: c++

   //spi.h
   #include <libm2k/tools/spi.hpp>

.. code:: c++

   //i2c.h
   #include <libm2k/tools/i2c.hpp>

Create main.cpp file:

.. code:: c++

   #include <libm2k/m2k.hpp>
   #include <libm2k/contextbuilder.hpp>
   #include <libm2k/analog/m2kpowersupply.hpp>
   #include <libm2k/analog/m2kanalogin.hpp>
   #include <libm2k/tools/spi_extra.hpp>

   extern "C" {
       #include "ad5592r.h"
   }
   extern struct ad5592r_rw_ops ad5592r_rw_ops; //default operations

   int main()
   {
       struct ad5592r_init_param init_param;
       init_param.int_ref = true; // use the internal reference

       struct ad5592r_dev device;
       device.ops = &ad5592r_rw_ops; //initialize the operations

       libm2k::contexts::M2k *context = libm2k::contexts::m2kOpen("ip:192.168.2.1");
       libm2k::analog::M2kPowerSupply *powerSupply = context->getPowerSupply();
       libm2k::analog::M2kAnalogIn *analogIn = context->getAnalogIn();

       std::cout << "Calibrating . . ." << std::endl;
       context->calibrateADC();

       powerSupply->enableChannel(0, true);
       powerSupply->pushChannel(0, 5); // power up the chip

       // first step of initialization
       m2k_spi_init m2KSpiInit; // m2k specific attributes of SPI
       m2KSpiInit.clock = 0;
       m2KSpiInit.mosi = 1;
       m2KSpiInit.miso = 2;
       m2KSpiInit.bit_numbering = MSB;
       m2KSpiInit.context = context;

       // second step of initialization
       spi_init_param spiInitParam; // generic attributes of SPI
       spiInitParam.max_speed_hz = 2500000;
       spiInitParam.mode = SPI_MODE_2;
       spiInitParam.chip_select = 3;
       spiInitParam.extra = (void*)&m2KSpiInit;

       // third step of initialization
       spi_init(&device.spi, &spiInitParam); // initialize SPI communication

       device.channel_modes[0] = CH_MODE_DAC; // set the first channel as a DAC
       device.num_channels = 1; // enable just the first channel
       ad5592r_init(&device, &init_param ); //initialize AD5592r

       for(int i = 0; i < 0xfff; i+=0x0f) {
           ad5592r_write_dac(&device, 0, i); // generate voltage
           std::cout << analogIn->getVoltage(0) << std::endl; //read voltage
       }

       libm2k::contexts::contextClose(context, true);
   }

Compile the project:

.. code:: c++

   gcc -c delay.c
   gcc -c ad5592r-base.c
   gcc -c ad5592r.c
   g++ -c main.cpp
   g++ -o example delay.o ad5592r-base.o ad5592r.o main.o -lm2k
   ./example

.. _datax-matlab-example:

Language Support: MATLAB
------------------------

.. note::

   This is a work in progress.

While the previous exercises used Python and pyadi-iio to communicate with
the AD5592r, the IIO framework is language-agnostic. Any language that can
call into the libiio C library (or use its command-line tools) can control the
hardware. In this section, we will recreate the NPN curve tracer example
in **MATLAB**, and instead of running on the Raspberry Pi, we will use the
**MAX32666FTHR** Feather board as a tinyiiod IIO server, connected to the
ADALM-LSMSPG over SPI and I2C, and controlled from a PC over USB serial.

.. note::

   This exercise demonstrates two key concepts: using MATLAB as an alternative
   to Python for IIO device control, and using a bare-metal microcontroller
   (MAX32666FTHR) as a portable alternative to the Raspberry Pi Linux host.

<<GanscaTudor, take it away!>>
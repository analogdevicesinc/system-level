.. _pluto users temp:

PlutoSDR Thermals
=================

There is a quick and easy script at
`github <https://github.com/analogdevicesinc/plutosdr_scripts/blob/master/pluto_temp.sh>`_
which allows you to print out temperature from a remote PC to either a USB
connected device, or one plugged in the network.

Example Usage
-------------

.. code:: console

   analog@analog:~$ ./pluto_temp.sh
   using uri -u usb:1.4.5
   pluto: 40.4 °C      zynq: 55.1 °C

For tracking temperatures, use the help option:

.. code:: console

   analog@analog:~$ ./pluto_temp.sh -h
   ./pluto_temp.sh [uri] [number loops] [delay in seconds]

Monitoring Example
------------------

.. code:: console

   analog@analog:~$ ./pluto_temp.sh usb:1.4.5 10 1
   using uri -u usb:1.4.5
   pluto: 40.4 °C      zynq: 55.4 °C
   pluto: 39.5 °C      zynq: 54.5 °C
   pluto: 40.4 °C      zynq: 54.8 °C
   pluto: 40.4 °C      zynq: 54.5 °C
   pluto: 40.4 °C      zynq: 55.4 °C
   pluto: 39.5 °C      zynq: 54.8 °C
   pluto: 40.4 °C      zynq: 55.0 °C
   pluto: 40.4 °C      zynq: 55.4 °C
   pluto: 40.4 °C      zynq: 54.4 °C
   pluto: 39.5 °C      zynq: 54.6 °C

Remote Execution
----------------

You can also copy it to the PlutoSDR (via scp), and run it directly.

.. code:: console

   root@pluto:~# uname -a
   Linux pluto 4.14.0-42540-g387d584 #301 SMP PREEMPT Wed Jul 3 15:06:53 CEST 2019 armv7l GNU/Linux
   root@pluto:~# ./pluto_temp.sh local: 10 1
   using uri -u local:
   pluto: -65.8 °C      zynq: 55.0 °C
   pluto: 40.4 °C      zynq: 54.6 °C
   pluto: 40.4 °C      zynq: 55.2 °C
   pluto: 39.5 °C      zynq: 54.8 °C
   pluto: 39.5 °C      zynq: 55.0 °C
   pluto: 39.5 °C      zynq: 55.0 °C
   pluto: 40.4 °C      zynq: 54.5 °C
   pluto: 40.4 °C      zynq: 54.6 °C
   pluto: 40.4 °C      zynq: 55.5 °C
   pluto: 40.4 °C      zynq: 55.6 °C

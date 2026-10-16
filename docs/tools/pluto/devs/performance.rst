.. _pluto devs performance:

ADALM-PLUTO Performance Metrics
===============================

Receiver
--------

.. TODO:: Add receiver performance metrics

Transmitter
-----------

.. TODO:: Add transmitter performance metrics

Data Throughput
---------------

Via IIOD USB backend
~~~~~~~~~~~~~~~~~~~~

.. code:: console

   $ iio_readdev -u usb:1.100.5 -b 100000 cf-ad9361-lpc | pv > /dev/null
   210GiB 1:19:51 [26,1MiB/s]

Via IIOD Network backend with RNDIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: console

   $ iio_readdev -n 192.168.2.1 -b 100000 cf-ad9361-lpc | pv > /dev/null
   203MiB 0:00:10 [20,4MiB/s]

Via local IIO device
~~~~~~~~~~~~~~~~~~~~

.. code:: console

   $ iio_readdev -u local: -b 100000 cf-ad9361-lpc | pv > /dev/null
   13.5GiB 0:02:09 [107MiB/s]

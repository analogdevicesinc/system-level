.. _pluto transceiver_transferring_data:

Controlling the transceiver and transferring data
=================================================

PlutoSDR runs `Linux <https://en.wikipedia.org/wiki/Linux>`__.
The :ref:`device drivers <pluto-m2k drivers>` allowing you to control the
transceiver and capture samples are therefore part of to the Linux Industrial IO
(IIO) framework. IIO is a kernel subsystem for analog to digital or digital to
analog converters and related hardware. IIO communicates with user space via
`sysfs <https://en.wikipedia.org/wiki/sysfs>`__ and a character devices. From a
plain user interaction point of view this is quite intuitive, since everything
is just a file. However when controlling the device from software, this can be
quite painful, since you simple want to call a function or method, instead of
doing string manipulation and file IO. LibIIO fills this gap, provides all sorts
of device abstraction and handles all kind of IIO internals. LibIIO is cross
platform and also provides different language bindings, so that you can control
IIO devices from C, C++, C# or Python.

If you’re not familiar with IIO, please start reading here:

-  :ref:`libiio`
-  :ref:`libiio internals`
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/ABI/testing>`__
-  `IIO Documentation <http://git.kernel.org/?p=linux/kernel/git/gregkh/staging.git;a=tree;f=drivers/staging/iio/Documentation;hb=refs/heads/staging-next>`__
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`__
-  `Video from FOSDEM of how IIO is used in SDR applications <http://ftp.heanet.ie/mirrors/fosdem-video/2015/devroom-software_defined_radio/iiosdr.mp4>`__

.. video:: https://www.youtube.com/watch?v=p_VntEwUe24

    LibIIO - A Library for Interfacing with Linux IIO Devices - Dan Nechita, Analog Devices Inc

Controlling the transceiver
---------------------------

The code snippet below is a minimalistic example without error checking. It
shows how to control the AD936x transceiver via a remote connection.

#. Create IIO IP Network context. Instead of ``ip:xxx.xxx.xxx.xxx`` it'll also
   accept ``usb:XX.XX.X``
#. Get the AD936x PHY device structure
#. Set the TX LO frequency (see :external+linux:ref:`ad9361`)
#. Set RX baseband rate

.. code-block:: c
   :linenos:

   #include <iio.h>

   int main (int argc, char **argv)
   {
       struct iio_context *ctx;
       struct iio_device *phy;

       ctx = iio_create_context_from_uri("ip:192.168.2.1");

       phy = iio_context_find_device(ctx, "ad9361-phy");

       iio_channel_attr_write_longlong(
           iio_device_find_channel(phy, "altvoltage0", true),
           "frequency",
           2400000000); /* RX LO frequency 2.4GHz */

       iio_channel_attr_write_longlong(
           iio_device_find_channel(phy, "voltage0", false),
           "sampling_frequency",
           5000000); /* RX baseband rate 5 MSPS */

       receive(ctx);

       iio_context_destroy(ctx);

       return 0;
   } 

Receiving data
--------------

#. Get the RX capture device structure
#. Get the IQ input channels
#. Enable I and Q channel
#. Create the RX buffer
#. Fill the buffer
#. Process samples

.. code-block:: c
   :linenos:

   int receive(struct iio_context *ctx)
   {
       struct iio_device *dev;
       struct iio_channel *rx0_i, *rx0_q;
       struct iio_buffer *rxbuf;

       dev = iio_context_find_device(ctx, "cf-ad9361-lpc");

       rx0_i = iio_device_find_channel(dev, "voltage0", 0);
       rx0_q = iio_device_find_channel(dev, "voltage1", 0);

       iio_channel_enable(rx0_i);
       iio_channel_enable(rx0_q);

       rxbuf = iio_device_create_buffer(dev, 4096, false);
       if (!rxbuf) {
           perror("Could not create RX buffer");
           shutdown();
       }

       while (true) {
           void *p_dat, *p_end, *t_dat;
           ptrdiff_t p_inc;

           iio_buffer_refill(rxbuf);

           p_inc = iio_buffer_step(rxbuf);
           p_end = iio_buffer_end(rxbuf);

           for (p_dat = iio_buffer_first(rxbuf, rx0_i); p_dat < p_end; p_dat += p_inc, t_dat += p_inc) {
               const int16_t i = ((int16_t*)p_dat)[0]; // Real (I)
               const int16_t q = ((int16_t*)p_dat)[1]; // Imag (Q)

               /* Process here */

           }
       }

       iio_buffer_destroy(rxbuf);

   }

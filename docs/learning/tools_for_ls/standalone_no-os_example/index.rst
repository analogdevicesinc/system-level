.. _datax-no-os-standalone:

Porting to a Fully Embedded System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This is a work in progress.


While the ultimate goal of the curve tracer is to have a local display, that's
another layer of both hardware and software development that we can defer a bit
longer with a little bit of creative thinking. Since there is a serial port
available, we can test out the logic by printing values to a terminal, formatted
as comma-separated variable (CSV) data for easy copy/paste into `LibreOffice
<https://www.libreoffice.org/>`__ or other spreadsheet for plotting. And for a
bit of `icing on the cake
<https://www.merriam-webster.com/dictionary/icing%20on%20the%20cake>`__ and
nostalgia, we can also make an ASCII-art plot!

Go back to the zip file from the no-OS release, and drag-and-drop the curve
tracer example HEX file into the DAPLINK drive. Press the RESET button on the
ADALM-LSMSPG and observe the output. The CSV data and ASCII-art plots will be
printed to the terminal as shown in the figures below.

.. code-block::
   :caption: ASCII-art NPN curve trace output

   === AD5592R (SPI) - NPN Curve Tracer (Ic vs Vc) ===
   Y-axis: Ic (0 to 7.16 mA)
   X-axis: Vc (0 to 2.45 V)

   +------------------------------------------------------------+
   |         ****** ***** ***** ***** ***** ***** ** *          |
   |        *                                                   |
   |       *                                                    |
   |      *                                                     |
   |                                                            |
   |      * ** ***** ***** ***** ***** ***** ***** ***** *      |
   |     * *                                                    |
   |      *                                                     |
   |     **                                                     |
   |     *                                                      |
   |    *   *** ***** ***** ***** ***** ***** ***** ***** **    |
   |     ***                                                    |
   |    *                                                       |
   |    **                                                      |
   |    **                                                      |
   |    *  ***** ***** ***** ***** ***** ***** ***** ***** ***  |
   |   *  *                                                     |
   |   ***                                                      |
   |****** **** ***** ***** ***** ***** ***** ***** ***** **** *|
   |                                                            |
   +------------------------------------------------------------+
   0.0       0.49       0.98       1.47       1.96       2.45 V

   ===== AD5592R Curve Trace Complete =====


Similarly, you will see an ASCII-art PNP curve trace similar to the figure below.

.. code-block::
   :caption: ASCII-art PNP curve trace output

   === AD5593R (I2C) - PNP Curve Tracer (Ic vs Vc) ===
   Y-axis: |Ic| (0 to 5.62 mA)
   X-axis: Vc (0 to 2.50 V)

   +------------------------------------------------------------+
   | ***** ****** ***** ****** ***** ****** ***** ****** *******|
   |                                                         *  |
   |                                                        **  |
   |                                                       **   |
   |  ** ****** ***** ****** ****** ***** ****** ***** **** *   |
   |                                                        *   |
   |                                                        *   |
   |                                                       *    |
   |                                                      * *   |
   |                                                            |
   |                                        ***** ******* *     |
   |      ***** ****** ****** ***** ****** *               *    |
   |                                                            |
   |                                                       *    |
   |                                                      *     |
   |                                                            |
   |                                                   ***      |
   |                                   * ** ****** ****         |
   |         ** ****** ****** ****** ** *                       |
   |         *                                                  |
   +------------------------------------------------------------+
   0.0       0.50       1.00       1.50       2.00       2.50 V

   ===== AD5593R Curve Trace Complete =====

At this point all of the math, algorithms, and overall operation of the curve
tracer are running in the embedded target, and we're able to verify everything
is operating properly and with full (analog) performance. The next step can be
to connect a local display, or enable a server for display on a remote screen
such as a tablet or mobile device.

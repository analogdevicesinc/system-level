.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation

.. _ad-fmcomms2-ebz interface_timing_validation:

Digital Interface Timing Verification
=====================================

The FMCOMMS[2345] boards featuring :adi:`AD9361` has a digital tuning feature
(programmable IO delay) and in most cases the FPGA features programmable IO
delay elements as well. The software tunes this interface for an optimal delay
setting ensuring that the interface works over part to part variations (AD9361
and the baseband/FPGA), voltage, temperature, interface speeds and across
different carrier boards (trace differences in PCB layout).

The tuning may be done either in FPGA, AD9361 or both (though not necessary).
The FPGA tuning may be the preferred option for you, as it can compensate for
the high fan-out clock buffers, however, since not all FPGA devices have this
option - in the ADI reference designs and software - we don"t use the FPGA, and
stick with the AD9361 tuning only.

In the ADI provided designs, the tuning algorithm works as follows (irrespective
of which delay element is tuned):

The receive chain is validated first. The AD9361 is programmed to generate a
`PRBS <https://en.wikipedia.org/wiki/Pseudorandom_binary_sequence>`__ (PN) BIST
pattern at the digital interface. A corresponding (and matched) sequence monitor
is implemented in the FPGA. The delay is sweeped from minimum to maximum
monitoring the status signals. More precisely the function first sweeps all data
delays (0..15) and then all clock delays (0..15). This happens at three
different interface rates. A low rate of 25MSPS and a higher rates of 40 and
61.44MSPS. All pass and fails are stored in a field, while the results of the
low and high rate are overlayed. The optimal delay is selected as the mid point
of the range where the monitor locks.

.. tip::

   **bist_timing_analysis** shown below only does a 2D pretty print of all Clock
   and Data delays combinations on RX at a given baseband rate.

   - ``o`` = PASS
   - ``.`` = FAIL

   After its done the REG6 content is restored and nothing is selected! If you
   want to re-trigger the digital interface tune algorithm please see below.

::

   root@analog:/sys/kernel/debug/iio/iio:device1# echo 1 > bist_timing_analysis
   root@analog:/sys/kernel/debug/iio/iio:device1# cat bist_timing_analysis
   CLK: 10000000 Hz 'o' = PASS
   DC0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:. . . . . . . . . . . . . . . .
   1:. . . . . . . . . . . . . . . .
   2:. . . . . . . . . . . . . . . .
   3:. . . . . . . . . . . . . . . .
   4:. . . . . . . . . . . . . . . .
   5:. . . . . . . . . . . . . . . .
   6:. . . . . . . . . . . . . . . .
   7:. . . . . . . . . . . . . . . .
   8:o . . . . . . . . . . . . . . .
   9:o o . . . . . . . . . . . . . .
   a:o o o . . . . . . . . . . . . .
   b:o o o o . . . . . . . . . . . .
   c:o o o o o . . . . . . . . . . .
   d:o o o o o o . . . . . . . . . .
   e:o o o o o o o . . . . . . . . .
   f:o o o o o o o o . . . . . . . .

   root@analog:/sys/kernel/debug/iio/iio:device1# echo 1 > bist_timing_analysis
   root@analog:/sys/kernel/debug/iio/iio:device1# cat bist_timing_analysis
   CLK: 60000000 Hz 'o' = PASS
   DC0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:. . . . . . o o o o o . . . . .
   1:. . . . . . . o o o o o . . . .
   2:. . . . . . . . o o o o o . . .
   3:. . . . . . . . . o o o o o . .
   4:. . . . . . . . . . o o o o o .
   5:. . . . . . . . . . . o o o o o
   6:. . . . . . . . . . . . o o o o
   7:. . . . . . . . . . . . . o o o
   8:. . . . . . . . . . . . . . o o
   9:o . . . . . . . . . . . . . . o
   a:o o . . . . . . . . . . . . . .
   b:o o o . . . . . . . . . . . . .
   c:o o o o . . . . . . . . . . . .
   d:o o o o o . . . . . . . . . . .
   e:. o o o o o . . . . . . . . . .
   f:. . o o o o o . . . . . . . . .

In the example above the clock delays are on the horizontal axis, while the data
delays are displayed on the vertical axis. The ``ad9361_dig_tune()`` function
overlays the two and would select a data delay of 11 (0xB).

The next step is to tune the transmit path. Since AD9361 has no such monitors in
the transmit path, it is set to be in digital loopback mode. Individual
(separate equations) PRBS patterns are sent from the FPGA in the transmit path
and are monitored in the receive path. The optimal delay is calculated the same
way as before.

The device is then set to it"s normal mode of operation. When enabling the FIR
filter blocks inside the AD9361, tests have been shown that the data/clock delay
slightly shifts. So in some cases when running with a high baseband sample rate
of 61.44MSPS the data/clock delays originally computed during driver
initialization don"t work anymore. For this reason we always rerun the interface
tuning algorithm whenever a filter is enabled at the target baseband rate. if
the FIR is disabled the original settings are restored.

Interface tuning upon FIR enable can be omitted by setting following device tree
attribute:

- adi,digital-interface-tune-fir-disable

In some cases the Digital Interface Timing Analysis and Verification is not
required. For example:

- on well understood custom board designs, where layout is fixed, and properly
  matched,
- where the interface runs at fewer (one) rates,
- where full temperature swings, or where I/O voltages are better controlled,
- in HALF DUPLEX mode, where the TX path tuning is not possible.

The TX tuning process or the entire Rx/Tx step can be skipped.

.. list-table::
   :header-rows: 1

   * - AD9361/4 Driver
     - Method
     - Values
   * - Linux
     - adi,digital-interface-tune-skip-mode (devicetree attribute)
     - 0, 1, 2
   * - No-OS
     - init_param->digital_interface_tune_skip_mode (Init Parameter)
     - 0, 1, 2

.. list-table::
   :header-rows: 1

   * - Skip Mode Value
     - Explanation
   * - 0
     - Perform RX and TX path tune
   * - 1
     - Perform RX and skip TX path tune, use default TX CLK/DATA delay values
   * - 2
     - Skip RX and TX path tune, use default RX/TX CLK/DATA delay values

Alternative way to configure the default RX/TX CLK/DATA delay values:

.. list-table::
   :header-rows: 1

   * - AD9361/4 Driver
     - Method
     - Values
   * - Linux
     - adi,delay-rx-data
     - 0..15
   * - Linux
     - adi,rx-data-clock-delay
     - 0..15
   * - Linux
     - adi,rx-data-delay
     - 0..15
   * - Linux
     - adi,tx-fb-clock-delay
     - 0..15
   * - No-OS
     - init_param->delay_rx_data
     - 0..15
   * - No-OS
     - init_param->rx_data_clock_delay
     - 0..15
   * - No-OS
     - init_param->rx_data_delay
     - 0..15
   * - No-OS
     - init_param->tx_fb_clock_delay
     - 0..15

Debugging
---------

When running into failures it"s beneficial to enable extended debugging
information. The code for the digital interface calibration features two
verboseness levels.

Enabling them requires a driver rebuild in some situations. There is also a
debugfs runtime API for it, however if the digital interface tune algorithm
fails initially the driver probe and initialization is aborted and thus no
device.

Additional debug information can be enabled by adding the BE_VERBOSE and
BE_MOREVERBOSE flags in the ad9361_post_setup() function.

::

   @@ -621,11 +621,11 @@ static int ad9361_post_setup(struct iio_dev *indio_dev)
           axiadc_write(st, ADI_REG_CHAN_CNTRL(i),
                    ADI_FORMAT_SIGNEXT | ADI_FORMAT_ENABLE |
                    ADI_ENABLE | ADI_IQCOR_ENB);
       }

   -   flags = 0;
   +   flags = BE_VERBOSE | BE_MOREVERBOSE;

       ret = ad9361_dig_tune(phy, (axiadc_read(st, ADI_REG_ID)) ?
           0 : 61440000, flags);
       if (ret < 0)
           goto error;

With these flags set you should observe following kernel/debugging messages

::

   [ --snip-- ]

   ad9361 spi32766.0: ad9361_probe : AD9361 Rev 2 successfully initialized

   [ --snip-- ]

   SAMPL CLK: 25000000 tuning: RX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:o o o o o o o o o # # # # o o o
   1:o o o o o o o o o o o # # # # o

   SAMPL CLK: 40000000 tuning: RX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:o o o o o o o o o # # # # o o o
   1:o o # # # # o o o o o # # # # o

   SAMPL CLK: 61440000 tuning: RX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # o o o o o # # # # o o o
   1:# o # # # # # # # # o # # # # #

   SAMPL CLK: 61440000 tuning: RX          <- Composite overlay of the above RX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # o o :red:`o` o o # # # # o o o      <- Algorithm selects RX Data Delay = 6
   1:# o # # # # # # # # o # # # # #

   SAMPL CLK: 25000000 tuning: TX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # # # # # # # # # # # # #
   1:# o o o o o o o o o o o o o # #

   SAMPL CLK: 40000000 tuning: TX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # # # # # # # # # # # # #
   1:# o o o o o o o o o o o # # # #

   SAMPL CLK: 61440000 tuning: TX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # # # # # # # # # # # # #
   1:# o o o o o o # # # # # # # # #

   SAMPL CLK: 61440000 tuning: TX          <- Composite Overlay of the above TX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # # # # # # # # # # # # #
   1:# o o o :red:`o` o o # # # # # # # # #      <- Algorithm selects TX Clock Delay = 4

   cf_axi_adc 79020000.cf-ad9361-lpc: ADI AIM (9.00.b) at 0x79020000 mapped to 0xf0358000, probed ADC AD9361 as MASTER

   [ --snip-- ]

digital_tune runtime API
~~~~~~~~~~~~~~~~~~~~~~~~

The digital_tune debugfs file takes two arguments.

The first one specifies whether the algorithm tunes on the current baseband rate
only (**0**) or whether it tunes on all three like it"s being done initially
(**1**).

The second argument is a bit mask flag which sets the verbosity level and
possibly other things as well. It"s recommended to only set the mask to **1** or
**3**.

.. code:: c

   enum dig_tune_flags {
       BE_VERBOSE = 1,
       BE_MOREVERBOSE = 2,
       DO_IDELAY = 4,
       DO_ODELAY = 8,
       SKIP_STORE_RESULT = 16,
       RESTORE_DEFAULT = 32,
   };

::

   //Current baseband rate only and be verbose//

   root@analog:/sys/kernel/debug/iio/iio:device1# dmesg -n7
   root@analog:/sys/kernel/debug/iio/iio:device1# echo 0 3 > digital_tune
   SAMPL CLK: 30720000 tuning: RX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:o o o o o o o o o o # # # # o o
   1:o o o o o o # # # # # o o o o o

   SAMPL CLK: 30720000 tuning: TX
     0:1:2:3:4:5:6:7:8:9:a:b:c:d:e:f:
   0:# # # # # # # # # # # # # # # #
   1:# o o o o o o o o o o o o o o o

As always - if you have any questions - feel free to ask in the
:ez:`support forums <community/fpga>`

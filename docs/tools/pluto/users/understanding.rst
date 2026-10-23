.. _pluto users understanding:

Basic internals of Pluto
=========================

.. figure:: images/understanding/pluto_simple_block_diagram.png
   :width: 200
   :align: right

The basic block diagram of the ADALM-PLUTO is pretty easy to understand. It has
two antennas, where the analog Radio Frequency (RF) energy goes in/out, and a
single USB connector, where digital data also goes in/out to a host system.
However, there is more going on that just RF to bits.

RF to bits is a difficult task that many have solved
`over the years <https://en.wikipedia.org/wiki/History_of_radio>`_. Starting as
a pure analog problem (and solution), people have been working on this for a
long time, and it's always interesting to better understand how long people have
been working on these types of problems.

* `James Clerk Maxwell <https://en.wikipedia.org/wiki/James_Clerk_Maxwell>`_
  published
  `A Treatise on Electricity and Magnetism <https://en.wikipedia.org/wiki/A_Treatise_on_Electricity_and_Magnetism>`_
  in 1873

* `Heinrich Rudolf Hertz <https://en.wikipedia.org/wiki/Heinrich_Hertz>`_ was
  transmitting and receiving EM waves, and published papers on them in 1887 and
  1890.

* `Guglielmo Marconi <https://en.wikipedia.org/wiki/Guglielmo_Marconi>`_
  developed the first apparatus for long distance radio communication during the
  summer of 1895, transmitting signals up to 2 miles (3.2 km) and over hills.

* `Reginald A. Fessenden <https://en.wikipedia.org/wiki/Reginald_Fessenden>`_
  became the first person to send audio (wireless telephony) by means of
  electromagnetic waves, transmitting over a distance of about 1.6 kilometers in
  December 1900, and six years later on Christmas Eve 1906 he became the first
  person to make a public radio broadcast.

* `Edwin Armstrong <https://en.wikipedia.org/wiki/Edwin_Howard_Armstrong>`_
  developed the
  `supersonic heterodyne <https://en.wikipedia.org/wiki/Superheterodyne_receiver>`_
  receiver as part of his work during WW I in 1918; and Wide-band
  `frequency modulation <https://en.wikipedia.org/wiki/Frequency_modulation>`_
  between 1928 and 1933.

.. figure:: images/understanding/prototype_armstrong_superheterodyne_receiver_1920.jpg
   :width: 300

* British researchers, trying to solve some superhet issues, developed the
  `homodyne <https://en.wikipedia.org/wiki/Direct-conversion_receiver>`_ in
  1932. The design was later renamed the synchrodyne, and is now sometimes
  referred to as direct conversion or zero-IF.

For nearly the last hundred years, radio design and architecture hasn't changed
that much. While many designers and engineers have made vast improvements in
devices (from tubes to transistors to integrated circuits), and implementations
(shielding, noise reduction, etc.), the fundamental architecture that radio
engineers work with is historic.

.. figure:: images/understanding/pluto_medium_block_diagram.png
   :width: 200
   :align: right

The radio inside the ADALM-PLUTO is the
:external+linux:ref:`AD9363 <ad9361>`, a high
performance, highly integrated RF agile transceiver, based on a direct
conversion receiver.

* The receive subsystem includes a low-noise amplifier (LNA), a direct
  conversion mixer, configurable analog filters, a high-speed analog to digital
  converter (ADC), digital decimation filters, and a 128-tap finite impulse
  response (FIR) filter to produce a 12-bit output signal at the appropriate
  sample rate. The receive chain is augmented with configurable automatic gain
  control (AGC) or manual gain control modes, dc offset correction, and
  quadrature correction. The resulting received I and Q signals are passed onto
  the digital baseband processor, in this case the AMD Xilinx Zynq SoC.

* The transmit subsystem also use a direct conversion architecture. Accepting
  12-bit I and Q samples from the baseband processor (in this case, the same
  AMD Xilinx Zynq SoC), it runs them through a 128-tap finite impulse response
  (FIR)
  filter, digital interpolation filters, a high speed digital to analog
  converter (DAC), an analog filter, the direct conversion mixers, and through a
  small power amplifier (PA) out to the antenna.

* Fully integrated phase-locked loops (PLLs) inside the AD9363 provide clocks
  and local oscillators for receive and transmit channels, and clocks for the
  ADC, DAC and output sample rate.

The
`AMD Xilinx Zynq All Programmable SoC <https://www.xilinx.com/products/silicon-devices/soc/zynq-7000.html>`_
(AP SoC) integrates the software programmability of an ARM-based processor with
the hardware programmability of an FPGA, enabling hardware acceleration while
integrating CPU, DSP, ASSP, and mixed signal functionality into a single device.
Such devices feature a single-core ARM Cortex™-A9 processor mated with 28nm
Artix®-7 based programmable logic, outfitted with commonly used hardened
peripherals (USB, SPI, etc.)
.. _pluto users name:

Why "Pluto"
===========

Just like `Pluto <https://en.wikipedia.org/wiki/Pluto>`_ (the celestial body)
is a `Dwarf Planet <https://en.wikipedia.org/wiki/Dwarf_planet>`_, the PlutoSDR
is an active learning module resembling a
`software defined radio <https://en.wikipedia.org/wiki/Software-defined_radio>`_,
but it lacks some performance/technical criteria for classification as such.
While it serves as a great learning tool for communications or SDR classes, the
PlutoSDR is not meant as a replacement for professional Software Defined Radios.
It was designed to provide RF/SDR functionality for students at an affordable
price point; as a result, there are limitations users should understand.

System Issues
-------------

Temperature Range
~~~~~~~~~~~~~~~~~

The PlutoSDR has been tested in the range "10°C to 40°C. While this is nominal
for classrooms world wide - it is not robust enough for units to be used in a
commercial setting." Devices inside typically specify 0°C to 70°C or −40°C to
+85°C. This limitation stems from system-level design, casing, and qualification
scope. Higher performance requires additional verification.

Digital Issues
~~~~~~~~~~~~~~

USB 2.0
^^^^^^^

`USB 2.0 <https://en.wikipedia.org/wiki/USB#USB_2.0>`_ operates at 480 Mb/s
half-duplex:

* At 100% utilization: 60 MB/s theoretical
* Protocol overhead (~10-15%): reduces to ~50 MB/s
* Control/interrupt/isochronous transfers (~10%): reduces to ~45 MB/s
* Half-duplex split: ~22.5 MB/s each direction
* 12-bit samples (2 bytes): ~11 MSPS theoretical

Actual PlutoSDR performance: 7.5 – 12 MSPS, roughly 65–100% of theoretical
rates. This depends heavily on USB host and concurrent traffic. Faster
interfaces (Gigabit/10G Ethernet, USB 3.0, PCIe) exist in commercial offerings.

The PlutoSDR includes 512 MB internal memory enabling burst mode operations.
Example: 128 MB (32 MSamples) at 30.72 MSPS (LTE20) stores 1.04166 seconds of
RF data—approximately 104 LTE frames—sufficient for educational decoders.

FPGA Size
^^^^^^^^^

The Xilinx Zynq 7010 FPGA is quite limited:

============  =====
Attribute     Size
============  =====
Logic Cells   28 K
Block RAM     2.1 Mb
DSP Slices    80
============  =====

.. figure:: images/name/pluto_utilization.jpg

The default design uses FPGA resources for:

* CMOS interface implementation
* I/Q rotation (optional)
* DDS (multi-tone transmit generation)
* 8x interpolation/decimation (enables sample rates as low as 65.104166 kSPS
  versus AD9363 minimum 520.833 kSPS)

Typical utilization includes: 40 DSP slices for additional
decimation/interpolation filters (20 each), 20 for optional DDS, 2 per channel
for optional 2×2 matrix multiply (IQ correction/phase rotation), and 1 per
channel for DC filtering. Users not requiring these features can disable them
for custom logic. Larger performance requirements necessitate upgrading to
larger `Zynq <https://www.xilinx.com//support/documentation/selection-guides/zynq-7000-product-selection-guide.pdf>`_
devices, impacting size and cost.

RF Issues
---------

Oscillator
~~~~~~~~~~

The PlutoSDR uses a Rakon RXO3225M 40.000 MHz oscillator
(Custom PN: `509336 <https://ez.analog.com/cfs-file/__key/telligent-evolution-components-attachments/00-323-00-00-00-03-22-63/attachment.pdf>`_)
meeting :adi:`AD9363` jitter requirements. Frequency
stability is ±25 ppm (voltage, temperature, drift plus initial accuracy).

While seemingly problematic, this is addressable through:

* Digital correction by programming XO frequency to measured values (Hz
  resolution), updating LO and sample rates accordingly
* Standard receiver frequency compensation algorithms—most systems accommodate
  transmitter/receiver frequency mismatches
* Loopback testing—offsets match between transmit/receive channels on a single
  device (random phase differences remain between LOs)

Alternative oscillators can overcome this limitation at potential cost impact.

Tuning Range
~~~~~~~~~~~~

The :adi:`AD9363` tuning range spans 325–3800 MHz
LO center frequencies—over one decade covering many interesting bands in the
`US <https://www.ntia.doc.gov/files/ntia/publications/january_2016_spectrum_wall_chart.pdf>`_,
`Europe <http://www.erodocdb.dk/docs/doc98/official/pdf/ERCRep025.pdf>`_,
`Australia <http://www.acma.gov.au/webwr/radcomm/frequency_planning/spectrum_plan/aust_rf_spectrum_plan.doc>`_,
and `Japan <http://www.tele.soumu.go.jp/e/adm/freq/search/share/plan.htm>`_.
However, this is narrower than the :adi:`AD9361` or :adi:`AD9364` which span
70–6000 MHz (nearly two decades).

Upgrading involves swapping to AD9364 or AD9361—pinouts are nearly identical but
cost increases. Some users report success
:ref:`telling the PlutoSDR <pluto users customizing>`
it contains an AD9364.

RF Shielding
~~~~~~~~~~~~

The PlutoSDR lacks internal RF shielding. Strong transmitters (e.g., cellphones)
placed nearby may degrade performance at any tuned frequency. Adding RF
shielding would impact cost and size.

RF Filtering
~~~~~~~~~~~~

There are no preselect or output filters. The AD9363 output directly feeds the
SMA connector; antenna input directly feeds the AD9363 pins.

The AD9363 RF transmitter outputs moderate 3rd harmonic distortion. At 3 GHz,
the 3rd harmonic (9 GHz) falls outside the balun range. At 500 MHz, the 3rd
harmonic (1500 MHz) remains within range—a 500 MHz transmission inadvertently
broadcasts at 1500 MHz as well.

Adding specific preselect/output filters complicates design based on desired
tuning range and antenna selection. (Antennas function as filters themselves.)

RF Performance
~~~~~~~~~~~~~~

The :adi:`AD9363` RF performance is adequate for many applications but does not
match higher-performance devices like the :adi:`AD9361`, :adi:`AD9364`, or
:adi:`AD9371` found in commercial SDR offerings.
The PlutoSDR exceeds performance of many same-class devices and datasheet
specifications in testing, but is not designed as the best possible SDR.
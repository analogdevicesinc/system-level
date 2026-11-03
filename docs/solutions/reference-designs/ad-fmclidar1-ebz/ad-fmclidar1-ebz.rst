.. _ad-fmclidar1-ebz user-guide:

User guide
================================================================================

.. image:: images/highlevel_blk_dig.png
   :align: center
   :width: 600

**DAQ Board**

- High speed data acquisition board containing the AD9094 quad channel ADC
  and clocking control for the full system. The FMC compliant connector
  interface means that this board can be connected to the users preferred
  FPGA development board. The Laser board and AFE board connect directly
  to this board.
- :doc:`DAQ Board Design Files and Description <hardware_daq>`

**Laser Board**

- The laser board is mated to the AFE board for mechanical mounting on an
  optional tripod stand. It is then connected electrically to the DAQ board
  using the cable provided.
- It contains 4 individual lasers with appropriate precision driver and
  power components for accurate firing of the lasers.
- To alter the laser Field-of-View custom Fast Axis Collimator optics are
  available from specialist optics suppliers.
- :doc:`Laser Board Design Files and Description <hardware_laser>`

**AFE Board**

- The AFE board contains a 16 channel APD from First Sensor and four ADI
  LTC6561 Quad channel TIA's with necessary power and timing signal chains.
  Custom optics can be fitted to the board using industry standard mounting
  adapters based on individual use cases.
- :doc:`AFE Board Design Files and Description <hardware_afe>`

.. note::

   For more information and how to buy the system please goto the
   :adi:`Analog Devices AD-FMCLIDAR1-EBZ Product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-FMCLIDAR1-EBZ.html>`

System setup & evaluation
--------------------------------------------------------------------------------

The development kit is delivered with an SD card containing the evaluation
software for the
:git-hdl:`supported FPGA carrier boards <hdl_2019_r1:projects/ad_fmclidar1_ebz>`
and a set of accessories required to put the system together and get it up
and running in no time.

.. image:: images/box_contents.jpg
   :alt: Box contents
   :align: right
   :width: 400

This is what you'll find in the development kit box:

- 8 x SMA cables to connect the AFE and Laser boards analog output signals
  to the DAQ board ADC inputs
- 2 x ribbon cables to connect the AFE and Laser boards digital signals
  to the DAQ board
- 12V @ 4A power supply for the Laser board and power cables
- `Plano-Convex Lens, Ø1", f = 25.4 mm, AR Coating: 650-1050 nm, P/N: LA1951-B-N-BK7 <https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1951-B>`_
- `SM1 Lens Tube, 1.50" Thread Depth, P/N: SM1L15 <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1L15>`_
- `SM1 Lens Tube, 1" Thread Depth, P/N: SM1L10 <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1L10>`_
- `Retaining Ring For stackable lens mount 0.08 thick, P/N: SM1RR <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1RR>`_
- SD card with the evaluation software for the supported FPGA carrier boards

The tripod shown in the system picture from the **Introduction** section is
not included but the specs can be found
`here <https://www.manfrotto.com/global/pixi-mini-tripod-black-mtpixi-b/>`_.

.. note::

   :doc:`Getting the system up and running <system_evaluation>`

Application Development
--------------------------------------------------------------------------------

.. image:: images/lidar_sw_fwrk.png
   :alt: SDK Architecture
   :align: right
   :width: 300

The Lidar Prototyping Platform software framework is common across all
hardware variants, developed with industry standard tools and interfaces.
The necessary parameters are exposed for customers to develop their own
proprietary solutions. Support is provided to cover a broad base of operating
systems used across different industry areas. There is a proven ADI JESD
framework available to reduce development complexity and time, and guarantees
deterministic transfer of data from the APD to the host processing system.

.. admonition:: Download
   :class: download

   :git-hdl:`Access the LiDAR Prototyping Platform software and get started <docs/projects/ad_fmclidar1_ebz>`

Laser Safety
--------------------------------------------------------------------------------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007
   for a Class 1 laser product. This device also complies with 21 CFR 1040.10
   and 1040.11 except for deviations pursuant to Laser Notice No. 50, dated
   June 24, 2007. Only use Software and Firmware updates that are specifically
   provided for this solution.

..
   `Laser Certification Report <resources/report_2223_fmclidar1_60825_classification.pdf>`_

   `Additional values tested <resources/fmclidar1_additional_testing.pdf>`_

Example
--------------------------------------------------------------------------------

As an example to prove out the overall system functionality a demo using
select optics was chosen to have the capability to detect an object of
approximately 1m x 1m in size at 60m range with 50% reflective characteristic.

- For the AFE Board a 1"(25.4mm) diameter lens, option from Thorlabs
  LA1951-B-N-BK7, was chosen (included in the box)
- For the laser board a custom Fast Axis Collimator optic was selected to
  narrow the vertical FoV from 30 degrees (natural dispersion of the laser)
  down to 1 degree to help achieve the 60m range. Mounting of these lenses
  requires a custom lens holder and also active lens alignment fitting during
  the manufacturing process. This was done at
  `FISBA <https://www.fisba.com/>`_, a worldwide leading supplier of
  customized optical components, systems and microsystems with locations
  across Europe and in the US.
- The lasers were driven at 50KHz with a pulse width of 20ns

..
   .. note::

      Application note:
      `Making distance measurements with the AD-FMCLIDAR1-EBZ <resources/lidar_measurement.pdf>`_

Videos & Articles
--------------------------------------------------------------------------------

- `YouTube: 776jK4yPvjI <https://www.youtube.com/watch?v=776jK4yPvjI>`_
- `YouTube: uOehjnhe7Zc <https://www.youtube.com/watch?v=uOehjnhe7Zc>`_
- `YouTube: 9-KRkB00VMQ <https://www.youtube.com/watch?v=9-KRkB00VMQ>`_

- :adi:`Open-Source LIDAR Prototyping Platform <analog-dialogue/articles/open-source-lidar-prototyping-platform>`

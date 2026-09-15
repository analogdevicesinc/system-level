.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ltpa-kit/hardware

.. _eval-ltpa-kit hardware:

EVAL-LTPA-KIT Hardware User Guide
=================================

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/kitangle.gif`
   :width: 600px

The EVAL-LTPA-KIT or LTpowerAnalyzer Kit is a low-cost, high performance,
compact laboratory tool for evaluating and characterizing power supply designs –
allowing measurements of frequency response, transient response, and output
impedance. Combined with the capabilities of the ADALM2000 Learning Module, it
offers high portability with its compact size.

The LTpowerAnalyzer Software offers a user-friendly interface with
documentations for ease of usage. It comes with four different current probes
for 1A, 10A, 50A, and 100A. Immediately kick-off using the kit with the
LT8642S-based demo board as the device under test (DUT).

--------------

Hardware Setup
--------------

Equipment Needed
~~~~~~~~~~~~~~~~

The EVAL-LTPA-KIT comes with the following boards and accessories:

- ► Base Board:

::

   *  LTpowerAnalyzer Base Board

- ► Current Probes:

::

   * 1A Current Probe
   * 10A Current Probe
   * 50A Current Probe
   * 100A Current Probe

- ► Interposer Boards:

::

   * Interface Connector Board A
   * Interface Connector Board B (5 pieces)
   * Interface Connector Board C

- ► LT8642A Demo Board (DUT)
- ► 2-Inch 16-Pin Ribbon Cable
- ► 8-Inch 14-Pin Ribbon Cable
- ► Connector Sockets (2 pieces)

The following list of equipment are not provided as part of the kit, but are
required for running the setup described in this guide.

- ► Laptop or PC running Windows 10
- ► :adi:`ADALM2000 active learning module`
- ► Digital power supply (12 V)

Bode Plot Measurement
~~~~~~~~~~~~~~~~~~~~~

The Bode Plot measurement scheme works by injecting a voltage signal to the
feedback network. As discussed in the
:dokuwiki:`eval-ltpa-kit #Components and Connection </resources/eval/user-guides/eval-ltpa-kit #Components and Connection>`
section, depending on the feedback network of the DUT, this may be done by
placing a series injection resistor.

The included DUT,\ **LT8642S Demo Board**, features a 16-pin male header for
easy interfacing with the LTpowerAnalyzer"s interposer board. The demo board may
be connected to the interface board of the LTpowerAnalyzer via a ribbon cable.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/dut_board.png
   :width: 600px

   LT8642S DUT Board

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/sample_ribbon_cable_connection_from_the_demo_board_to_the_ltpoweranalyzer.png
   :width: 300px

   Sample ribbon cable connection from the Demo Board to the LTpowerAnalyzer
   (via the Interface A Board)

However, other DUTs do not have a native support for these interfaces. Below is
an example illustrating how to set up the hardware DUT for gain and phase
measurements.

.. note::

   A DC1516A-B demo board, featuring the LTC3833EFE controller, was used to
   demonstrate simple hardware modifications to make a Bode Plot Measurement
   with any DUT without the native socket connectors.

\ **1. Identifying where to connect the injection signal**

Determine which connection type is appropriate for your circuit as described in
the Components and Connections overview. Consult the datasheet or schematic
diagram of the DUT.

This DC1516A-B Demo Board already has a 10 Ω injection resistor in series with
the feedback network as shown below:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/dc1516a-b_connection.png
   :width: 400px

.. note::

   **Kelvin Connection Guide for Bode Plot Measurements**

For this example, choose the kelvin connection setup with the transformer (T+ &
T-) and the signal inputs (OUT+ & IN+) terminal block pins connected to the
injection resistor R4. Connect the OUT-, IN-, and GND terminal block pins to the
GND of the demo board. Most boards require adding the injection resistor before
making the connections.

\ **2. Solder the wires to the DUT**

In this example, 28-gauge twisted pair wires (Red and Black), and a 26-gauge
solid core wire were used for the connections.

- Connect OUT+ and T+ together (Red Wire) to one of the terminals of the
  injection resistor.
- Connect IN+ and T- together (Black Wire) to the opposite terminal of the
  injection resistor.
- Connect all GND, OUT-, and IN- together to the ground plane of the DUT.

It is recommended to connect the OUT+ and T+ wires to the terminal connected
directly to the DUT"s voltage output plane (Vout). Recheck connections, and
ensure there are no shorts.

.. note::

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/bode_injection_connection.jpg
      :width: 300px

      OUT+, T+, IN+, T- Connection

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/bode_gnd_connection.jpg
      :width: 300px

      GND, OUT-, IN- Connection

\ **3. Prepare the system for measurements**

- Connect the LTpowerAnalyzer (LB3031A) main board to the ADALM2000 (M2k) or the
  Analog Discovery 2 USB scope.
- Connect the wires to the terminal block on the LTpowerAnalyzer main board and
  connect the demo board Vin inputs to a power supply.
- Connect the USB scope to the computer via the USB cable and launch the
  LTpowerAnalyzer software.
- Connect a current probe to the LTpowerAnalyzer main board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/bode_system_example.jpg
   :width: 600px

.. note::

   **Basic LTpowerAnalyzer System Setup for Bode Plots Only (No current probe
   attached yet)**

>>>

--------------

Transients and Impedance Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different methods of setting up a DUT for transients and impedance measurements:

Method 1: LT8642S DUT
^^^^^^^^^^^^^^^^^^^^^

The out-of-the box DUT, LT8642S, comes with a readily installed female socket
connector. This allows convenient changing of current probes, with no soldering
required

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/lt8642s_dut_connectors.png
   :width: 1000px

.. note::

   **LT8642S DUT Connectors**

>>

Method 2: Soldering Braid Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this method, the LB3058A current probe will be directly installed at the DUT
via soldering braids for a good mechanical connection.

This method improves electrical connection by reducing parasitics from affecting
the measurements and providing a good mechanical connection. However, its
biggest drawback is that the DUT is damaged due to the scraping of the solder
mask, thus making it challenging to swap current probes.

1. Scrape off the solder mask on the GND and VOUT planes, then add folded solder
   braid.

.. note::

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/soldermask.jpg
      :width: 300px

      Scrape off the Solder Mask

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/solderbraid.jpg
      :width: 300px

      90-degree Solder Braid

2. Solder in the LB3058A Current Source.

.. note::

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/currentprobeback.jpg
      :width: 300px

      Current Probe Front View

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/currentprobefront.jpg
      :width: 300px

      Current Probe Back View

3. Connect the Vout+ and Vout- wires to the terminal block and plug in the
   14-pin ribbon cable.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/currentprobewithconnection.jpg
   :width: 400px

.. note::

   **Completed Setup**

>>

Method 3: Socket Installation Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this method, a 60-position female connector or edge rate card socket will be
used for installing current probes to your DUT.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/60_position_female_connector.png
   :width: 200px

.. note::

   **60 Position Female Connector or Edge Rate Card Socket**

This method is similar to the soldering-braid method, requiring to scrape off
the solder mask on the board. However, it provides more flexibility in
installing and swapping out current probes.

1. Scrape off the solder mask on the GND and Vout Planes to expose the copper
   for connection. Ensure that the scrapped regions will be able to accommodate
   the length and required soldering space for the female socket connector.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/unscrapped_solder_mask_at_the_vout_and_gnd_planes_of_a_dut.png
   :width: 400px

.. note::

   **Before: Unscrapped solder mask at the VOUT and GND planes of a DUT
   (LTC3899EUF)**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/scrapped_solder_mask_at_the_vout_and_gnd_planes.png
   :width: 400px

.. note::

   **After: Scrapped solder mask at the VOUT and GND planes**

2. It is recommended to tin the exposed copper region for ease of soldering
   later.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/tinned_scrapped_region.png
   :width: 500px

.. note::

   **Tinned scrapped region**

3. Solder the female socket connector to the exposed copper.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/soldered_female_socket_connector.png
   :width: 500px

.. note::

   **Soldered female socket connector**

4. Ensure proper connection via a continuity check. Check for possible shorts as
   well.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-kit/complete_installed_female_socket_connector.png
   :width: 500px

.. note::

   **Complete installed female socket connector**

.. tip::

   The LTpowerAnalyzer Kit comes with an easy-to-use graphical user interface,
   designed to be used in conjunction with the hardware components.

   To access the installer and learn how to use the built-in tools, visit the
   :dokuwiki:`EVAL-LTPA-KIT Software User Guide </resources/eval/user-guides/eval-ltpa-kit/software>`

--------------

Resources
---------

- :adi:`LT1761 Product Page <LT1761>`
- :adi:`LT1964 Product Page <LT1964>`
- :adi:`ADG709 Product Page <ADG709>`
- :adi:`LTC6252 Product Page <LTC6252>`
- :adi:`ADA4891-2 Product Page <ADA4891-2>`
- :adi:`LTC6240 Product Page <LTC6240>`
- :adi:`ADA4807-1 Product Page <ADA4807-1>`
- :adi:`LT8642S Product Page <LT8642S>`

Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer
Zone.

.. note::

   :ez:`EngineerZone Support Community <reference-designs>`

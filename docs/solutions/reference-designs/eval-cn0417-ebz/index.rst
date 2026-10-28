.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0417

EVAL-CN0417-EBZ
===============

USB Powered 2.4 GHz RF Power Amplifier.

Overview
--------

The :adi:`CN0417` is a small USB-powered RF power amplifier optimized for
2400 MHz operation. The amplifier typically provides 20 dB of gain through its
RF band of operation, boosting signals for various communication protocols such
as ISM, MC-GSM, W-CDMA, TD-SCDMA, and LTE. It requires a 5V USB supply for
normal operation. The input and output, both populated with edge-mounted SMA
connectors, are DC blocked and matched to 50Ω for ease of use. More information
on this board can be found at
:dokuwiki:`PlutoSDR Amplifier </university/tools/pluto/users/amp>`.

The :adi:`ADL5606` is a broadband, two-stage, 1W RF driver amplifier
that operates over a frequency range of 1800 MHz to 2700 MHz. The device can be
used in a wide variety of wired and wireless communication protocols, including
ISM, MC-GSM, W-CDMA, TD-SCDMA, and LTE.

The :adi:`LTM8045` is an integrated switching DC/DC converter that
contains a current mode controller, power switching element, power coupled
inductor, power Schottky diode, and a modest amount of input and output
capacitance. It can be configured as a SEPIC or inverting converter by simply
grounding the appropriate output rail.

The EVAL-CN0417-EBZ board connects through SMA and is powered by the bus
voltage from the USB port.

.. figure:: block_diagram3.png

General Setup
-------------

Required Equipment
~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-CN0417-EBZ Board <CN0417>`
- RF Signal Source (like the :ref:`PlutoSDR <pluto>`)
- Micro-USB power adaptor or Micro-USB to USB cable

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: revb_blockd.jpg

- Terminal block **J1** is the SMA female connector for RF input, and would
  normally be connected to an SDR.
- Terminal block **J2** is the SMA male connector for RF output, and would
  normally be connected to an antenna
- Terminal block **P1** is the micro USB port to provide power to the board

Test setup
~~~~~~~~~~

.. figure:: 10-31-2018_10-51-55_am.png

#.  Plug in the micro-USB end of the micro-USB cable or power adapter to P1 of
    the :adi:`EVAL-CN0417-EBZ Board <CN0417>`
#.  Plug the other end of the cable into a power outlet or a PC USB port
    providing at least 500 mA.
#.  An LED light will turn on indicating the board is on and is in operation.
#.  Connect the RF output of the RF signal source to J1 of
    the :adi:`EVAL-CN0417-EBZ Board <CN0417>`
#.  Connect J2 of the :adi:`EVAL-CN0417-EBZ Board <CN0417>` to desired DUT or
    equipment needing the amplifier signal.

Running the System
~~~~~~~~~~~~~~~~~~

-   After completing the setup, the :adi:`EVAL-CN0417-EBZ Board <CN0417>`
    will automatically turn on and output the amplified version of the input.

Normal Operation
~~~~~~~~~~~~~~~~

.. figure:: cn0417.png

For normal operation, connect:

#.  Connect P1 (micro USB) connector of the :adi:`EVAL-CN0417-EBZ Board <CN0417>`
    into a PC USB port or 5V USB charger.
#.  An LED light will turn on indicating the board is on and is in operation.
#.  Connect the RF output of the :ref:`PlutoSDR <pluto>` to J1 of the
    :adi:`EVAL-CN0417-EBZ Board <CN0417>`.
#.  Connect J2 of the :adi:`EVAL-CN0417-EBZ Board <CN0417>` to an antenna
    (ensure the antenna can dissipate 1W).

.. warning::

    Connecting the :adi:`EVAL-CN0417-EBZ Board <CN0417>` directly to
    the Pluto SDR input (Rx) may exceed the absolute maximum ratings for the RF
    Input (which is +2.5 dBm). Doing this may permanently damage the PlutoSDR input.
    Never do this for any reason.

    .. figure:: pluto_setup_1.jpg

    We test the :adi:`EVAL-CN0417-EBZ Board <CN0417>` in this configuration, by
    ensuring the Tx attenuator is set to an attenuation of 30 dB or more. This
    ensures the gain of +20 dB from the :adi:`EVAL-CN0417-EBZ Board <CN0417>` will
    not exceed the maximum ratings for the RF Input.

    Never do this in normal operation.

Additional Resources
---------------------

- :adi:`CN0417 Circuit Note Page <CN0417>`
- :adi:`CN0417 Design Support Package <CN0417-DesignSupport>`
- :dokuwiki:`Test Results </university/tools/pluto/users/amp>`
- :adi:`ADL5606 Product Page <ADL5606>`
- :adi:`LTM8045 Product Page <LTM8045>`

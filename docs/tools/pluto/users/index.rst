.. _pluto users:

For End Users
=============

.. figure:: ../pluto_in_hand.png
   :width: 200
   :align: right

Everyone using Pluto should read these pages. They will demonstrate how to
interact with RF signals with MATLAB, Simulink, GNU Radio or custom C, C++, C#,
or Python code on a host (x86) or embedded (Raspberry Pi, Beaglebone,
96boards.org, etc.) platform over USB. As you can see, we have lots of examples
with MATLAB and Simulink, as we find that a very powerful environment, and a
path to a releasable radio (you can take your algorithms, and easily embed them
into a custom product).

Contents
--------

..
   Make sure all things are in ./users

Hardware
^^^^^^^^

- :ref:`Introduction to the Hardware <pluto users intro>`
- :ref:`What's with the name? <pluto users name>` *PlutoSDR?*
- :ref:`Understanding the Internals <pluto users understanding>`
- :ref:`How hot? <pluto users temp>`
- :ref:`How Far, How fast? <pluto users far_fast>`
- :ref:`RF Output <pluto users transmit>`
- :ref:`Phase Noise & Accuracy <pluto users phase_noise>`
- :ref:`RF Input <pluto users receive>`
- :ref:`Receiver Sensitivity <pluto users receiver_sensitivity>`
- :ref:`Dealing with Non-Quadrature signals <pluto users non_quad>`
- :ref:`Antennas <pluto users antennas>`
- :download:`Letter of Volatility <letter_of_volatility_pluto.pdf>`

Software
^^^^^^^^

- :ref:`Quick Start <pluto users quick_start>`
- Installing Device Drivers on:
  :ref:`Windows <pluto-m2k drivers windows>`,
  :ref:`Linux <pluto-m2k drivers linux>`,
  :ref:`MAC <pluto-m2k drivers osx>`
- :ref:`Upgrading Firmware <pluto users firmware>`
- :ref:`Calibrating <pluto users calibration>`
- :ref:`Customizing <pluto users customizing>`

Applications
^^^^^^^^^^^^

Once the drivers are configured and set up, you can interact with the
:adi:`ADALM-PLUTO` Active Learning Module from:

- `Scopy <https://analogdevicesinc.github.io/scopy/index.html>`__
- `gqrx <http://gqrx.dk/>`__, an open source software defined radio receiver
  (SDR) powered by the GNU Radio
- :mw:`Official support for MATLAB and Simulink <hardware-support/adalm-pluto-radio.html>`
- :dokuwiki:`MATLAB IIO Bindings <resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
- :ref:`GNU Radio <software gnuradio>`
- `SDRangel <https://github.com/f4exb/sdrangel>`__, an Open Source Qt5 /
  OpenGL 3.0+ SDR and signal analyzer frontend to various hardware.
- `SDR# <https://airspy.com/download/>`__. The PlutoSDR frontend for
  SDRsharp can be found here:
  `sdrsharp-plutosdr <https://github.com/Manawyrm/sdrsharp-plutosdr>`__
- `SoapySDR <https://github.com/pothosware/SoapySDR>`__. The Soapy SDR
  plugin for PlutoSDR can be found here:
  `SoapyPlutoSDR <https://github.com/jocover/SoapyPlutoSDR>`__
- `Access and control of PlutoSDR hardware using python bindings to libiio <https://github.com/radiosd/PlutoSdr>`__
- `Python Interfaces <https://analogdevicesinc.github.io/pyadi-iio/index.html>`__
- :ref:`C Examples <pluto transceiver_transferring_data>`

Resources
^^^^^^^^^

- :ref:`ASEE Papers <pluto users asee_papers>`

.. toctree::
   :hidden:
   :glob:

   *

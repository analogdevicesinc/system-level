.. _pluto users:

For End Users
=============

.. image:: ../pluto_in_hand.png
   :width: 200px
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

#. :dokuwiki:`Introduction to the Hardware <university/tools/pluto/users/intro>`

   #. :dokuwiki:`What's with the name? <university/tools/pluto/users/name>` *PlutoSDR?*
   #. :dokuwiki:`Understanding the Internals <university/tools/pluto/users/understanding>`
   #. :dokuwiki:`How hot? <university/tools/pluto/users/temp>`
   #. :dokuwiki:`How Far, How fast? <university/tools/pluto/users/far_fast>`

      #. :dokuwiki:`RF Output <university/tools/pluto/users/transmit>`

         #. :dokuwiki:`Phase Noise & Accuracy <university/tools/pluto/users/phase_noise>`

      #. :dokuwiki:`RF Input <university/tools/pluto/users/receive>`

         #. :dokuwiki:`Receiver Sensitivity <university/tools/pluto/users/receiver_sensitivity>`
         #. :dokuwiki:`Dealing with Non-Quadrature signals <university/tools/pluto/users/non_quad>`

   #. :dokuwiki:`Antennas <university/tools/pluto/users/antennas>`
   #. :dokuwiki:`Letter of Volatility <_media/university/tools/pluto/users/letter_of_volatility_pluto.pdf>`

#. :dokuwiki:`Quick Start <university/tools/pluto/users/quick_start>`
#. Intro to the Software. Installing Device Drivers on:

   #. :ref:`Windows <pluto-m2k drivers windows>`
   #. :ref:`Linux <pluto-m2k drivers linux>`
   #. :ref:`MAC <pluto-m2k drivers osx>`

#. Upgrading the the ADALM-PLUTO :dokuwiki:`Firmware <university/tools/pluto/users/firmware>` .
#. :dokuwiki:`Calibrating <university/tools/pluto/users/calibration>` the ADALM-PLUTO.
#. :dokuwiki:`Customizing <university/tools/pluto/users/customizing>` the ADALM-PLUTO.
#. Once the driver are configured and set up, you can interact with the
   :adi:`ADALM-PLUTO` Active Learning Module from:

   #. :ref:`iio-oscilloscope`
   #. `gqrx <http://gqrx.dk/>`__, an open source software defined radio receiver
      (SDR) powered by the GNU Radio
   #. :mw:`Official support for MATLAB and Simulink <hardware-support/adalm-pluto-radio.html>`
   #. :dokuwiki:`MATLAB IIO Bindings </resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
   #. :ref:`GNU Radio <software gnuradio>`
   #. `SDRangel <https://github.com/f4exb/sdrangel>`__, an Open Source Qt5 /
      OpenGL 3.0+ SDR and signal analyzer frontend to various hardware.
   #. `SDR# <https://airspy.com/download/>`__. The PlutoSDR frontend for
      SDRsharp can be found here:
      `sdrsharp-plutosdr <https://github.com/Manawyrm/sdrsharp-plutosdr>`__
   #. `SoapySDR <https://github.com/pothosware/SoapySDR>`__. The Soapy SDR
      plugin for PlutoSDR can be found here:
      `SoapyPlutoSDR <https://github.com/jocover/SoapyPlutoSDR>`__
   #. `Access and control of PlutoSDR hardware using python bindings to libiio <https://github.com/radiosd/PlutoSdr>`__
   #. :dokuwiki:`Python Interfaces </resources/tools-software/linux-software/pyadi-iio>`
   #. :dokuwiki:`C Examples </university/tools/pluto/controlling_the_transceiver_and_transferring_data>`

#. :dokuwiki:`/university/tools/pluto/Accessories </Accessories>`

.. toctree::
   :hidden:
   :glob:

   *

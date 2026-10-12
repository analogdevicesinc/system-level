.. _fmcomms11 user-guide:

User guide
===============================================================================

Top view
-------------------------------------------------------------------------------

.. image:: images/top_view_ic_component.jpg
   :align: center
   :width: 600

Bottom view
-------------------------------------------------------------------------------

.. image:: images/AD-COMMS11-EBZBOTTOM-evaluation-board.jpg
   :align: center
   :width: 600

Hardware guide
-------------------------------------------------------------------------------

For detailed hardware documentation, refer to:

- :doc:`hardware` - Board overview, PCB layers and dimensions
- :ref:`fmcomms11 functional-overview` - System block diagram and signal paths
- :ref:`fmcomms11 card-specification` - Transmitter and receiver characterization

Design files (schematic, PCB layout, bill of materials) are available
:ref:`here <fmcomms11 hardware-design-files>`.

Software guide
-------------------------------------------------------------------------------

The FMCOMMS11 evaluation board is supported with the
:git-libiio:`libiio library </>`. This library is cross-platform
(Windows, Linux, Mac) with language bindings for C, C#, Python, MATLAB,
and others.

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   iio_has_plugin: true
   iio_plugin_ref: fmcomms11-plugin

.. include-template:: ../common/using-scopy.rst.jinja

PyADI-IIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-pyadi-iio:`PyADI-IIO </>` is a Python abstraction module for ADI
hardware with IIO drivers. An FMCOMMS11 example can be found
:git-pyadi-iio:`here <examples/fmcomms11_example.py>`.

MATLAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
- `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_
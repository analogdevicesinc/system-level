.. imported from: https://wiki.analog.com/resources/eval/user-guides/industrial_wireless_cbm_evaluation_tool_3axis

.. _industrial_wireless_cbm_evaluation_tool_3axis:

Voyager 3, Wireless Condition Based Monitoring Platform
=======================================================

Overview
--------

This document will give a high level explanation of the function and setup of
Analog Devices" Condition Based Monitoring (CBM) evaluation software and
hardware. This includes a brief introduction to the software and how it is used
with the CBM hardware. It also includes a step-by-step guide on the
functionality of the CBM Graphical User Interface (GUI).

The function of the system is to provide an evaluation tool for a wireless
signal chain for MEMS-accelerometer based vibration monitoring. The hardware can
be directly attached to a motor or fixture via a stud.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fig1.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fig2.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fig3.png
   :width: 800px

   Figure 1. SmartMesh System Overview

The CBM hardware signal chain consists of a tri-axis ADXL356 accelerometer
mounted to the base of the module. The output of the ADXL356 is read into the
AD7685 ADC, and then processed by the ADuCM4050 low power microcontroller. Here
it is buffered, transformed to the frequency domain and streamed to the
SmartMesh IP mote. From the SmartMesh chip it is wirelessly streamed to the
SmartMesh IP Manager. The manager connects to a PC and visualization and saving
of the data can take place.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/hd_mote_with_txt.png
   :width: 400px

   Figure 2. CBM Mote Breakdown

--------------

Features
--------

Smartmesh
~~~~~~~~~

::

   *2.4 GHz multi-hop wireless mesh networking solution.
   *Automatic creation and maintenance of network, with 101 mote limit.
   *Scalability for networks to work in different configurations.
   *High data capacity with up to 7.2 kbps of payload data per node (in a 3 mote setup).

Mote
~~~~

::

   *Low-power motes (wireless nodes) with >10 year battery life, suitable for tough RF environments.
   *Small form factor packages.
   *3-axis acceleration data.

GUI
~~~

::

   *Supports real-time plotting of incoming data, tested for up to 3 motes
   *Options to update mote parameters on-the-fly.
   *Save incoming data to database.
   *Customise data plotting.
   *Available as both an executable or python file.

--------------

Getting Started
~~~~~~~~~~~~~~~

Equipment
^^^^^^^^^

- :adi:`SmartMesh IP Manager (DC2274A) </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/dc2274a-a.html#eb-overview>`
- EV-CBM-VOYAGER3-1Z Hardware Module (referred to as ``Mote``)
- JTAG Cable (only needed for firmware upgrade)
- Programming Board (Only needed for firmware upgrade)
- Clamp

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/hardware_v3-1z.png
   :width: 400px

   Figure 3. Mote, Manager, Programming Board and Clamp

Software Required
^^^^^^^^^^^^^^^^^

The software for this project is available as an executable, or as a python
file. The executable only works on windows, but requires no installation of
dependencies by the user, these are all packaged into the executable. If running
the python file, a number of dependencies must first be installed. Please
consult the CBM_setup guide for more detailed instructions on running the python
program.

Executable (Windows Only)
'''''''''''''''''''''''''

- CBM_app.exe

Python
''''''

- Python 2.7.15
- Pip for Python (latest version)
- Matplotlib (v2.2.3)
- PySerial (v3.5)
- Scipy (v1.2.2)
- Pandas (v0.23.3)
- openpyxl (v2.6.4)
- CBM_app.py (provided in software package)

::

   *[[https://github.com/analogdevicesinc/ev-cbm-voyager| ev-cbm-voyager GitHub]].

Quickstart
~~~~~~~~~~

- Plug the manager into any available USB port on your PC
- Place the 2xAA batteries in the mote.
- Download the available software below in the software installation section.
- Save the CBM_app executable anywhere on your PC and launch the program.
- A window should pop up, prompting you for the COM port of your manager. Search
  for the manager port number in your computers device manager, under PORTS(COM
  & LPT). The correct COM port is the last of four consecutive COM ports
- Click connect.
- When the Mote"s green LED starts blinking, data is plotted, with the default
  being time and fft plots.
- While the mote is stationary, double click the remove adc offset checkbox.
- Interact with the mote by shaking it, and observe the changes to the data
  plotted.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mote_v3-1z_remove_offset.png
   :width: 600px

   Figure 4. Initial Connection to Single Stationary Mote

--------------

Documentation
~~~~~~~~~~~~~

A setup guide has been created for the Wireless CBM tool which is available on
this wiki. This may be used if the quickstart provided here does not result in
successful operation of the program, or for more information about this program
and its setup.

::

   *{{ :resources:eval:user-guides:cbm_setup.pdf | CBM Setup Guide}}

::

   *{{ :resources:eval:user-guides:wcbm-01_firmware_guide.pdf | WCBM-01 Firmware
   Guide}}

::

   *{{ :resources:eval:user-guides:developers_firmware_guide.pdf | Developers Firmware Guide}}

::

   *{{
   :resources:eval:user-guides:condition_based_monitoring_statistical_functions.pdf | Statistical Functions Guide}}

--------------

Typical Measurements
~~~~~~~~~~~~~~~~~~~~

If you have the program running, with a mote connected, simply shake the mote in
any direction. This should update the plots with some meaningful vibration data.

This demo can be improved by using the mote in conjunction with a small
motorized device (e.g. electric fan). Simply place the mote as close to the
vibration source as possible and observe the results in the GUI.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/mote_v3-1z_time_series_output.png
   :width: 800px

   Figure 5. Typical GUI Output

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fft_markers.png
   :width: 600px

   Figure 6. Fourier Transform graph explained

--------------

Mounting Information
~~~~~~~~~~~~~~~~~~~~

The Voyager enclosure includes a ¼-28 threaded hole. To mount the mote, either a
mounting stud or a magnetic mount can be used. Magnetic mounts are typically
used in situations where the monitored equipment does not include a threaded
hole. Several different scenarios for mounting are discussed below, with
suggested parts for each scenario.

Mounting Studs
^^^^^^^^^^^^^^

#. If the monitored equipment includes a ¼-28 threaded hole, then a ¼-28 to ¼-28
   attach stud can be used. Example Parts:

- `CTC: MH108-1B; <https://www.ctconline.com/mounting_studs.aspx?prd=MH108-1B>`__
- `PCB Piezotronics 081B20; <https://www.pcb.com/products?m=081B20>`__

#. If the monitored equipment includes an M6 threaded hole, then a ¼-28 to M6
   attach stud can be used. Example Parts:

- `CTC: MH108-5B; <https://www.ctconline.com/mounting_studs.aspx?prd=MH108-5B>`__
- `https://www.pcb.com/products?m=M081B20PCB Piezotronics: M081B20 Metric mounting stud, ¼-28 to M6 x 0.75, BeCu w/shoulder <https://www.pcb.com/products?m=M081B20PCB Piezotronics: M081B20 Metric mounting stud, ¼-28 to M6 x 0.75, BeCu w/shoulder>`__

#. If the monitored equipment includes an M8 threaded hole, then a 1/4 -28 to M8
   attach stud can be used. Example Parts:

- `MH108-6B; <https://www.ctconline.com/mounting_studs.aspx?prd=MH108-6BCTC>`__

Magnetic Mounts
^^^^^^^^^^^^^^^

#. IFM and PCB Piezotronics provide magnetic mounts with M8 or ¼-28 vibration
   sensor attach. Example Parts:

- `IFM M8 attachment flat E30448; <https://www.ifm.com/ie/en/product/E30448?tab=details>`__
- Note: To use the IFM base then you also need a ¼-28 to M8 adaptor stud for the
  Voyager enclosure

#. PCB Piezotronics ¼-28. Example Parts:

- `PCB Piezotronics ¼-28, both flat and curved surface attachment <https://www.pcb.com/sensors-for-test-measurement/accelerometers/accessories/magnetic-mounting-bases>`__
- Note: The Piezotronics bases 080A54, 080A130/131/132 could be used directly
  with the Voyager enclosure concept, as they include a ¼-28 treaded hole.

—

LTspice Simulation
~~~~~~~~~~~~~~~~~~

Figure 7 can be used to simulate the frequency response of a MEMS circuit.
Figure 7 has two elements - firstly the response of the MEMS mechanical
structure estimated using the LAPLACE equation, and secondly the signal chain
op-amp filtering. Figure 8 presents the x-axis frequency response of the
ADXL356, in good agreement with the ADXL356 data sheet Figure 8. This model
assumes a nominal resonant frequency of 5500 Hz, a Q of 17, and the use of a
single-pole, low-pass filter that has a cutoff frequency of 1500 Hz. This model
does not include consideration of the manner in which the accelerometer is
coupled to the platform that it is monitoring.

The simulation model shows good agreement with the data sheet typical
performance, with resonant frequency of 5.5kHz. For AC analysis its best to use
a LAPLACE circuit in LTspice, but for transient analysis discrete components or
a simple voltage waveform input should be used for best simulation performance.
This is a good rule of thumb when extending the analysis to the rest of the
signal chain beyond the MEMS and op-amp. For example, Figure 9 shows an added
ADC on the op-amp output.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/voyager_image1.png
   :width: 900px

   Figure 7. LTspice Simulation circuit for ADXL356 MEMS Frequency Response

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/voyager_image2.png
   :width: 900px

   Figure 8. LTspice Frequency Response Simulation Output for ADXL356 (X-Axis)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/voyager_image3.png
   :width: 1000px

   Figure 8. Extending the analysis to the ADC)

LTSpice models are available here:

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/voyager.zip`

--------------

Further Reading
~~~~~~~~~~~~~~~

If you are a developer interested in contributing to this project, or looking at
the SmartMesh library in greater detail, more information is available at the
SmartMeshSDK space on
`Dustcloud <https://dustcloud.atlassian.net/wiki/spaces/SMSDK/overview>`__. This
gives links to a number of example programs which show the full capability of
the SmartMesh library, and links to the source code for the whole project
available on GitHub at
`SmartMesh GitHub <https://github.com/dustcloud/smartmeshsdk>`__.

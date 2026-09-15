.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x/fluorescence

.. _circuits-from-the-lab eval-adpd410x fluorescence:

EVAL-ADPD410X-ARDZ Fluorescence Measurement Demo
================================================

The :adi:`EVAL-ADPD410x-ARDZ` allows users to take advantage of the flexibility
of the :adi:`ADPD4100` and :adi:`ADPD4101` as multimodal sensor front ends to a
wide range of applications. One example of a specialized application is the
:adi:`CN0503`, a reference design for optical water quality measurement. This
demonstration shows how to perform fluorescence measurement using the
:adi:`EVAL-ADPD410x-ARDZ`, similarly to the
:dokuwiki:`CN0503 Fluorescence Measurement Demo </resources/eval/user-guides/circuits-from-the-lab/cn0503/fluorescence>`.

.. important::

   This demo uses a lot of the optical, mechanical, and photodiode and LED
   components from the :adi:`CN0503` kit. This demo is especially prepared to
   show the ability of the :adi:`EVAL-ADPD410x-ARDZ` board to perform the same
   measurements as the :adi:`CN0503`. For a less complex demo setup, refer to
   the Turbidity Demo.

General Description/Overview
----------------------------

One method of measuring the amount of substance in a sample is by using
fluorescent light. In this setup, a light is passed from a monochromatic source
through the sample, and then the fluorescence in the substance is measured using
a detector tuned to its wavelength. The intensity of the fluorescent light
compared to the intensity of the incident light will be proportional to the
amount of the fluorescent substance in the sample. An effective way of
performing this is by using the setup shown below.

Light is emitted from an LED at 365 nm wavelength. It then passes through a
beam-splitter, which directs some of the incident light to a reference
photodiode detector for sampling. Quinine in the sample fluoresces due to the
365 nm light and emits ~450 nm light. Another photodiode detector, sensitive to
blue light frequencies, is positioned at 90 degrees from the light path to
measure the intensity. This placement decreases the effects of the light emitted
from the source LED. Additionally, a monochromatic filter is placed in front of
the detector to further isolate the measurement.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/fluorescence_path.png
   :width: 600px

   Fluorescence Path

Demo Requirements
-----------------

The following is a list of items needed to replicate this demo.

- :adi:`EVAL-ADPD410x-ARDZ`
- :adi:`EVAL-ADICUP3029` with firmware (see Firmware Setup)
- Host computer with PyADI-IIO and relevant dependencies installed (See
  :dokuwiki:`EVAL-ADPD410X-ARDZ Python Example </resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x#python-and-pyadi-iio>`)
- 3D Printed Single Path Base () (Also orderable from
  `Shapeways <https://www.shapeways.com>`__)
- 3D Printed Cuvette Holder () (Also orderable from
  `Shapeways <https://www.shapeways.com>`__)
- `Type 1FLP Disposable Macro Cuvettes UV Plastic (Lightpath: 10mm) <https://www.fireflysci.com/disposable-fluorescence-cells/type-1flp-disposable-macro-cuvettes-lightpath-10 mm>`__
- `10 mm Dia. x 6.6 mm FL, Uncoated Molded Aspheric Condenser Lens <https://www.edmundoptics.com/p/10mm-dia-x-66mm-fl-uncoated-molded-aspheric-condenser-lens/30541/>`__
- `12.5 x 17.5 mm, 50R/50T, Plate Beamsplitter <https://www.edmundoptics.com/p/125-x-175mm-50r50t-plate-beamsplitter/5798/>`__
- `Fluorescence Filter (SCHOTT GG-475, 12.5 mm Dia., Longpass Filter) <https://www.edmundoptics.com/p/gg-475-125mm-dia-longpass-filter/11320/>`__

- Fluorescence Photodiode Board

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/img_20200428_165220.jpg
    :width: 100px

- Transmit Photodiode Board

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/img_20200428_165212.jpg
    :width: 100px

- 365 nm LED Board

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/img_20200501_130028.jpg
    :width: 100px

- Male-to-female jumper headers for connection
- ( Optional ) Prepared samples with known quinine concentration measurement

Setting up the EVAL-ADPD410X-ARDZ
---------------------------------

Configure the onboard jumper header and solder jumper connections, as shown
below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/fl_adpd410x_jumperconn.jpg
   :width: 400px

   ADPD410X Jumper Connections

.. list-table::
   :header-rows: 1

   * - **Header**
     - **Setting**
     - **Image**
     -
   * - P10
     - No connection
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/p10_empty.png
         :width: 200px

     -
   * - JP1
     - Shorted Pin 2 and Pin 3
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/jp1_5v.png
         :width: 200px

     -
   * - IOSEL
     - Shorted Pin 1 and 2
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/iosel_shunt.png
         :width: 200px

     -

Set the following :adi:`EVAL-ADICUP3029` switches according to their
configuration on the table below.

.. list-table::
   :header-rows: 1

   * - **Switch**
     - **Configuration**
   * - UART (S2)
     - USB
   * - POWER (S5)
     - WALL/USB

Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029` using the
headers, as shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/arduinoconnection.jpg
   :width: 400px

   Arduino Connection

Firmware Setup
--------------

Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro USB to USB cable.
Drag and drop the appropriate .hex file from the list below to the Daplink
Drive. (See
:dokuwiki:`eval-adpd410x#driver-/-firmware-setup </resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x#driver-/-firmware-setup>`)

.. admonition:: Download

   Pre-built hex files can be found here:

   - :git-EVAL-ADICUP3029:`EVAL-ADPD4100-ARDZ .Hex File (ADuCM3029_demo_adpd410x_spi_waterquality.hex) <releases/download/Latest/ADuCM3029_demo_adpd410x_spi_waterquality.hex+>`
   - :git-EVAL-ADICUP3029:`EVAL-ADPD4101-ARDZ .Hex File (ADuCM3029_demo_adpd410x_i2c_waterquality.hex) <releases/download/Latest/ADuCM3029_demo_adpd410x_i2c_waterquality.hex+>`

   The latest source code can be found here:

   - :git-EVAL-ADICUP3029:`EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_adpd410x <tree/master/projects/ADuCM3029_demo_adpd410x+>`

Optical Path Setup
------------------

The demo utilizes an optical path similar to the one used by :adi:`CN0503`,
but only for a single channel. The single path base and cuvette holder are
available as 3D-printable designs () and can also be ordered using Shapeways.

#. Assemble the cuvette holder. See
   :dokuwiki:`Assembling the Tower </resources/eval/user-guides/circuits-from-the-lab/cn0503#assembling_the_tower>`
   for instructions.
#. Insert the 365 nm LED Board to the base, as shown below.
#. Insert the Transmit Photodiode Board at the bottom of the base, as shown
   below. The Transmit Photodiode Board uses the same photodiode as the one used
   as reference in the :adi:`CN0503`.
#. Insert the Fluorescence Photodiode Board to the base, as shown below.
#. Insert the monochromatic or fluorescence filter to the slit in front of the
   Fluorescence Photodiode Board, as shown below.
#. Insert the cuvette with the quinine sample to measure.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/fluorescence_topviewpath.png
   :width: 400px

Hardware Connection
-------------------

Connect the 365 nm LED Board, Transmit Photodiode Board, and Fluorescence
Photodiode Board to the prototyping connectors of the :adi:`EVAL-ADPD410x-ARDZ`,
as shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/demo_connection.png
   :width: 600px

   Demo Connection

Software Setup
--------------

This demo uses a PyADI-IIO example script. See
:dokuwiki:`Software Setup </resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x#software_setup>`
for the complete installation instructions from libiio to pyadi-iio.

#. Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029`.
#. Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro-USB cable and
   note the serial port from the Device Manager as in
   :dokuwiki:`Connection </resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x#connection>`.
#. Open command prompt or terminal and navigate through the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
#. Run the example script using the command.
   ::

      ...\pyadi-iio\examples>python adpd410x_demo.py

#. The script will ask for a serial port. Input the noted serial port and press
   Enter. In cases when the board is not found, press the reset button (S1) on
   the :adi:`EVAL-ADPD410x-ARDZ` and input the noted serial port again.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/pyadiiio_example2_comport.png
      :width: 400px

#. When the board is detected, you will be asked to specify the demo application
   to use. Since this setup is only applicable for fluorescence measurements,
   enter 1.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/demo_selectapplication.png
      :width: 400px

#. A plot will appear showing the measured and computed quinine concentration.
   You have the option to save a copy of the displayed waveform at any point in
   time using the matplotlib controls at the top. Remove the cuvette and replace
   the quinine sample with a different concentration to observe the measurement
   change.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adpd410x/demo_fluorescenceresult.png
      :width: 400px

.. important::

   The demo script uses the same polynomial approximation used in
   :dokuwiki:`Computing Quinine Concentration </resources/eval/user-guides/circuits-from-the-lab/cn0503/fluorescence#computing_concentration>`.

Reference Links
---------------

- :dokuwiki:`Hardware User Guide </resources/eval/user-guides/circuits-from-the-lab/eval-adpd410x>`

.. _eval_adpd410x fluorescence_demo:

Fluorescence Measurement Demo
==============================

The :adi:`EVAL-ADPD410x-ARDZ` allows users to take advantage 
of the flexibility of the :adi:`ADPD4100` and :adi:`ADPD4101` as multimodal sensor front ends 
to a wide range of applications. One example of a specialized application is the :adi:`CN0503`, 
a reference design for optical water quality measurement. This demonstration shows how to perform 
fluorescence measurement using the :adi:`EVAL-ADPD410x-ARDZ`, 
similarly to the :ref:`CN0503 Fluorescence Measurement Demo <fluorescence-measurement>`.

.. important::

   This demo uses a lot of the optical, mechanical, and photodiode 
   and LED components from the :adi:`CN0503` kit. This demo is especially 
   prepared to show the ability of the :adi:`EVAL-ADPD410x-ARDZ` board to 
   perform the same measurements as the :adi:`CN0503`. For a less complex 
   demo setup, refer to the Turbidity Demo.

General Description/Overview
----------------------------

One method of measuring the amount of substance in a sample is by using
fluorescent light. In this setup, a light is passed from a monochromatic source
through the sample, and then the fluorescence in the substance is measured using
a detector tuned to its wavelength. The intensity of the fluorescent light
compared to the intensity of the incident light will be proportional to the
amount of the fluorescent substance in the sample. An effective way of
performing this is by using the setup shown below.

Light is emitted from an LED at 365 nm wavelength. It then passes through a beam-splitter, 
which directs some of the incident light to a reference photodiode detector for sampling. 
Quinine in the sample fluoresces due to the 365 nm light and emits ~450 nm light. 
Another photodiode detector, sensitive to blue light frequencies, is positioned at 90 degrees 
from the light path to measure the intensity. This placement decreases the effects of the 
light emitted from the source LED. Additionally, a monochromatic filter is placed 
in front of the detector to further isolate the measurement.

|image1|

Demo Requirements
-----------------

The following is a list of items needed to replicate this demo.

-  :adi:`EVAL-ADPD410x-ARDZ`
-  :adi:`EVAL-ADICUP3029` with firmware (see Firmware Setup)
-  Host computer with PyADI-IIO and relevant dependencies installed (See :doc:`EVAL-ADPD410X-ARDZ Python Example </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`)
-  3D Printed Single Path Base () (Also orderable from `Shapeways <https://www.shapeways.com>`_)
-  3D Printed Cuvette Holder () (Also orderable from `Shapeways <https://www.shapeways.com>`_)
-  `Type 1FLP Disposable Macro Cuvettes UV Plastic (Lightpath: 10mm) <https://www.fireflysci.com/disposable-fluorescence-cells/type-1flp-disposable-macro-cuvettes-lightpath-10 mm>`_
-  `10 mm Dia. x 6.6 mm FL, Uncoated Molded Aspheric Condenser Lens <https://www.edmundoptics.com/p/10mm-dia-x-66mm-fl-uncoated-molded-aspheric-condenser-lens/30541/>`_
-  `12.5 x 17.5 mm, 50R/50T, Plate Beamsplitter <https://www.edmundoptics.com/p/125-x-175mm-50r50t-plate-beamsplitter/5798/>`_
-  `Fluorescence Filter (SCHOTT GG-475, 12.5 mm Dia., Longpass Filter) <https://www.edmundoptics.com/p/gg-475-125mm-dia-longpass-filter/11320/>`_
-  Fluorescence Photodiode Board

      .. image:: images/img_20200428_165220.jpg
         :width: 100

-  Transmit Photodiode Board

      .. image:: images/img_20200428_165212.jpg
         :width: 100

-  365 nm LED Board

      .. image:: images/img_20200501_130028.jpg
         :width: 100

-  Male-to-female jumper headers for connection
-  (**Optional**) Prepared samples with known quinine concentration measurement

Setting up the EVAL-ADPD410X-ARDZ
---------------------------------

Configure the onboard jumper header and solder jumper connections, as shown below.

|image2|

========== ======================= =========
**Header** **Setting**             **Image**
========== ======================= =========
P10        No connection           |image3|
JP1        Shorted Pin 2 and Pin 3 |image4|
IOSEL      Shorted Pin 1 and 2     |image5|
========== ======================= =========

Set the following :adi:`EVAL-ADICUP3029` switches according to their configuration on the table below.

========== =====================
**Switch** **Configuration**
========== =====================
UART (S2)  USB
POWER (S5) WALL/USB
========== =====================

Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029` using the headers, as shown below.

|image6|

Firmware Setup
--------------

Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro USB to USB cable. Drag and drop the appropriate HEX file 
from the list below to the Daplink Drive. (See :doc:`Firmware Setup </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`)

.. admonition:: Download
   :class: download

   
   Pre-built HEX files can be found here:
   
   -  `EVAL-ADPD4100-ARDZ HEX File (ADuCM3029_demo_adpd410x_spi_waterquality.hex) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_adpd410x_spi_waterquality.hex>`_
   -  `EVAL-ADPD4101-ARDZ HEX File (ADuCM3029_demo_adpd410x_i2c_waterquality.hex) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_adpd410x_i2c_waterquality.hex>`_
   
   The latest source code can be found here:
   
   -  :git-EVAL-ADICUP3029:`EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_adpd410x <projects/ADuCM3029_demo_adpd410x>`
   

Optical Path Setup
------------------

The demo utilizes an optical path similar to the one used by :adi:`CN0503`, but only for a single channel. The single path base and cuvette holder are available as 3D-printable designs () and can also be ordered using Shapeways.

-  Assemble the cuvette holder. See :ref:`Assembling the Tower <eval-cn0503-ardz assembling-the-tower>` for instructions.
-  Insert the 365 nm LED Board to the base, as shown below.
-  Insert the Transmit Photodiode Board at the bottom of the base, as shown below. The Transmit Photodiode Board uses the same photodiode as the one used as reference in the :adi:`CN0503`.
-  Insert the Fluorescence Photodiode Board to the base, as shown below.
-  Insert the monochromatic or fluorescence filter to the slit in front of the Fluorescence Photodiode Board, as shown below.
-  Insert the cuvette with the quinine sample to measure.

.. image:: images/fluorescence_topviewpath.png
   :width: 400 px

Hardware Connection
-------------------

Connect the 365 nm LED Board, Transmit Photodiode Board, and Fluorescence Photodiode Board to the prototyping connectors of the :adi:`EVAL-ADPD410x-ARDZ`, as shown below.

|image7|

Software Setup
--------------

This demo uses a PyADI-IIO example script. See :doc:`Software Setup </solutions/reference-designs/eval-adpd410x/eval-adpd410x>` for the complete installation instructions from libiio to pyadi-iio.

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the :adi:`EVAL-ADICUP3029`.
-  Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro-USB cable and note the serial port from the Device Manager as in :doc:`Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Open command prompt or terminal and navigate through the examples folder inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example script using the command. ``...\pyadi-iio\examples>python adpd410x_demo.py``
-  The script will ask for a serial port. Input the noted serial port and press Enter. In cases when the board is not found, press the reset button (S1) on the :adi:`EVAL-ADPD410x-ARDZ` and input the noted serial port again.

      |image8|

-  When the board is detected, you will be asked to specify the demo application
   to use. Since this setup is only applicable for fluorescence measurements,
   enter 1.

      |image9|

-  A plot will appear showing the measured and computed quinine concentration.
   You have the option to save a copy of the displayed waveform at any point in
   time using the matplotlib controls at the top. Remove the cuvette and replace
   the quinine sample with a different concentration to observe the measurement
   change.

      |image10|

.. important::

   The demo script uses the same polynomial approximation used in :ref:`Computing Quinine Concentration <fluorescence-measurement>`.

Reference Links
---------------

-  :doc:`Hardware User Guide </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`

.. |image1| image:: images/fluorescence_path.png
   :width: 600
.. |image2| image:: images/fl_adpd410x_jumperconn.jpg
   :width: 400
.. |image3| image:: images/p10_empty.png
   :width: 200
.. |image4| image:: images/jp1_5v.png
   :width: 200
.. |image5| image:: images/iosel_shunt.png
   :width: 200
.. |image6| image:: images/arduinoconnection.jpg
   :width: 400
.. |image7| image:: images/demo_connection.png
   :width: 600
.. |image8| image:: images/pyadiiio_example2_comport.png
   :width: 400
.. |image9| image:: images/demo_selectapplication.png
   :width: 400
.. |image10| image:: images/demo_fluorescenceresult.png
   :width: 400

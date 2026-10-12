.. _eval_adsd3100_nxz flashing:

Flashing Image Instructions
===============================================================================

This guide provides instructions for flashing a microSD card image using
balenaEtcher on Windows systems.

Install balenaEtcher
-------------------------------------------------------------------------------

Download and install balenaEtcher from the official website:
https://www.balena.io/etcher/

The SD Card
-------------------------------------------------------------------------------

The NXP Platform requires a microSD card. You can connect it using:

- An SD card adapter (if your PC has an SD card slot)
- A USB hub with appropriate card reader capability

Flash Image onto SD Card
-------------------------------------------------------------------------------

Follow these steps to flash the image:

Step 1: Launch balenaEtcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the balenaEtcher application.

.. figure:: images/capture0.png
   :alt: balenaEtcher Launch
   :align: center
   :width: 600

   balenaEtcher Application

Step 2: Select Flash from File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click "Flash from file" and select the provided .img file.

.. figure:: images/capture1.png
   :alt: Select Image File
   :align: center
   :width: 600

   Select Image File

Step 3: Select Target
~~~~~~~~~~~~~~~~~~~~~

Select the target microSD card.

.. figure:: images/capture.png
   :alt: Select Target
   :align: center
   :width: 600

   Select Target SD Card

Step 4: Flash
~~~~~~~~~~~~~

Click "Flash!" to initiate the process.

.. figure:: images/capture3.png
   :alt: Flash Process
   :align: center
   :width: 600

   Flashing in Progress

Step 5: Verify
~~~~~~~~~~~~~~

Wait for the flash and verification to complete successfully.

.. figure:: images/capture4.png
   :alt: Flash Complete
   :align: center
   :width: 600

   Flash Complete

.. note::

   After flashing, safely eject the SD card and insert it into the
   EVAL-ADSD3100-NXZ module.

.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175-nxz/nvm

.. _eval-adtf3175-nxz nvm:

ADTF3175 NVM Contents
=====================

The module NVM follows the Serial Flash Discoverable Parameters (SFDP) standard.
The flash consists of a linked list.

NVM ChunkType
-------------

The table below shows the structures that will come with a calibrated ADTF3175
module.

.. list-table::

   * - **Chunk Type**
     - **Component**
     - **Descriptions**
   * - 0x3D
     - NVM Header
     - Must always start at address 0x0
   * - 0x01
     - CCB
     - Imager Calibration content
   * - 0x56
     - Imager Factory Firmware
     - Reserved space for Imager Factory Firmware
   * - 0x57
     - Imager Current Firmware
     - Reserved space for Imager Current Firmware
   * - 0x58
     - Imager Upgrade Firmware
     - Reserved space for Imager Upgrade Firmware
   * - 0x53
     - ADSD3500 Factory Firmware
     - Reserved space for ADSD3500 Factory Firmware
   * - 0x54
     - ADSD3500 Current Firmware
     - Reserved space for ADSD3500 Current Firmware
   * - 0x55
     - ADSD3500 Upgrade Firmware
     - Reserved space for ADSD3500 Upgrade Firmware
   * - 0x52
     - ADSD3500 Init Firmware
     - ADSD3500 boot up firmware
   * - 0x50
     - Capabilities Structure
     -
   * - 0x51
     - Debug Structure
     -

Chunk Type Details
~~~~~~~~~~~~~~~~~~

Each chunk type has a header with the following details. The header is typically
followed by chunk data + a 4 byte CRC.

.. list-table::

   * - chunkID
     - Signature for each header type, always 0xAD
   * - chunkType
     - ID for chunk type
   * - major version
     - Major version number
   * - minor version
     - Minor version number
   * - headerSizeBytes
     - Header Size, always 20
   * - chunkSizeBytes
     - Size of chunk data
   * - nextChunkHeader
     - Address of next chunk header
   * - chunkHeaderCRC
     - CRC of previous 16 bytes

NVM Header
^^^^^^^^^^

The NVM header always starts at address 0x0.

.. list-table::

   * - **Content**
     - **Size (bytes)**
     - **Value**
     - **Description**
   * - chunkID
     - 1
     - 0xAD
     -
   * - chunkType
     - 1
     - 0x3D
     -
   * - major version
     - 1
     - 0x##
     -
   * - minor version
     - 1
     - 0x##
     -
   * - headerSizeBytes
     - 4
     - 20
     -
   * - chunkSizeBytes
     - 4
     - 0x00
     - Always 0
   * - nextChunkHeader
     - 4
     - 0x14
     -
   * - chunkHeaderCRC
     - 4
     - CRC
     - CRC of previous 16 bytes

CCB
^^^

.. list-table::

   * - **Content**
     - **Size (bytes)**
     - **Value**
     - **Description**
   * - chunkID
     - 1
     - 0xAD
     -
   * - chunkType
     - 1
     - 0x01
     -
   * - major version
     - 1
     - 0x##
     -
   * - minor version
     - 1
     - 0x##
     -
   * - headerSizeBytes
     - 4
     - 20
     -
   * - chunkSizeBytes
     - 4
     - 0x##
     - Size of CCB
   * - nextChunkHeader
     - 4
     - 0x##
     - Location of next header
   * - chunkHeaderCRC
     - 4
     - CRC
     - CRC of previous 16 bytes
   * - CCB Data
     - chunkSizeBytes
     - DATA
     -
   * - CCB Data CRC
     - 4 bytes
     - CRC
     - CRC of CCB data

Imager Firmware
^^^^^^^^^^^^^^^

ADSD3500 Firmware
^^^^^^^^^^^^^^^^^

ADSD3500 Init Firmware
^^^^^^^^^^^^^^^^^^^^^^

Capabilities Structure
^^^^^^^^^^^^^^^^^^^^^^

Debug Structure
^^^^^^^^^^^^^^^

Modifying NVM
-------------

V4L2 Device Driver
==================

This documentation covers the V4L2 device driver for the ADSD3500 Time-of-Flight
(ToF) camera on the EVAL-ADTF3175D evaluation board. The driver source code is
maintained in the Analog Devices ToF repository.

Available Scripts
-----------------

The SD Card Image includes scripts located in ``~/Workspace/adsd3500_getframe``
that enable frame streaming without the SDK. These utilities use the
``v4l2-ctl`` command-line tool (pre-installed on the system) to capture frames
to a file named ``frame.bin``.

Key scripts include:

-  ``get_frame.sh`` - Basic single frame capture
-  ``get_frame_mp.sh`` - Mega-pixel mode streaming
-  ``get_frame_8.sh`` - 8-bit depth mode
-  ``get_frame_mp_ab.sh`` - Mega-pixel with AB frames

Control Parameters
------------------

The driver exposes several configurable controls accessible via ``v4l2-ctl``:

Phase/Depth Bits
   Range from 8-bits to 16-bits (selectable via menu values 2-6)

AB Frames
   Off or 8-bit to 16-bit options available

Confidence Data
   Disabled, 4-bit, or 8-bit modes

Additional Controls
   Operating mode selection, AB averaging toggle, and depth enable option

Usage Example
-------------

The ``get_frame_mp.sh`` script demonstrates command syntax: it configures
operating mode 10 (mega-pixel), sets 12-bit depth output, disables AB and
confidence frames, then streams frames at 1024×3072 resolution in BG12 pixel
format.

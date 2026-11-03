.. _eval-ad7124-x prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. One of the :adi:`AD7124-4` / :adi:`AD7124-8`-based evaluation boards:
   :adi:`EVAL-AD7124-8-PMDZ`, :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>`,
   :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>`, :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>`, or
   :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>`.

#. A carrier platform. Our recommended ones can be found
   :ref:`here<ad7124x carriers>`
#. A PC or laptop with a USB port.
#. Test equipment for generating analog input signals.
#. USB cable (for connecting the controller board to the PC).

Additional hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- For the :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` and :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>`
  (with :adi:`SDP-B` or Nucleo): 7--9 V DC power supply applied
  to J3 (bench top) or J5 (wall wart/DC plug).
- For the :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` and :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>`
  (with :adi:`SDP-B`): no external power supply required; the
  board is powered through the :adi:`SDP-B` via USB from the PC.
- Analog input test signals or sensors (RTDs, thermocouples, thermistors) as
  appropriate for your application.

Software prerequisites
-------------------------------------------------------------------------------

If using the EVAL-ADICUP3029 (with EVAL-AD7124-8-PMDZ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. CrossCore Embedded Studio (2.9.1 or higher)
#. ADuCM302x DFP (3.2.0 or higher)
#. ADICUP3029 BSP (1.1.0 or higher)
#. Serial terminal program (e.g., `PuTTY <https://www.putty.org/>`_,
   `Tera Term <https://ttssh2.osdn.jp/index.html.en>`_)

If using the SDP-B (with EVAL-AD7124-4SDZ, EVAL-AD7124-8SDZ,
EVAL-AD7124-4ASDZ, or EVAL-AD7124-8ASDZ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. AD7124 Eval+ Software (included on CD or :download:`downloadable <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`)
#. :adi:`SDP-B` board drivers (installed as part of the Eval+
   Software installation)

If using the Nucleo-L476RG (with EVAL-AD7124-4SDZ or EVAL-AD7124-8SDZ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. `STM32CubeIDE <https://www.st.com/en/development-tools/stm32cubeide.html>`_
#. `ad7124_stm32_example.zip <https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_example/ad7124_stm32_example.zip>`_
#. Serial terminal program (e.g., PuTTY)

.. note::

   Check the :ref:`quickstart guides <eval-ad7124-x quickstart>` for detailed
   setup instructions specific to each controller board.

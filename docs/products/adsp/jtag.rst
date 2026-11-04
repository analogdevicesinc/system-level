.. _adsp-jtag:

JTAG
""""

.. toctree::
   :hidden:
   :glob:

List of ADI JTAG debuggers

================= ================================================================================
JTAG version      Product Page
================= ================================================================================
ICE-1000          `EMULATORS`_
ICE-1500          `EMULATORS`_
ICE-2000          `EMULATORS`_
Debug Agent       usually comes on carrier boards like `EV-SOMCRR-EZLITE`_ and `EV-SOMCRR-EZKITE`_
================= ================================================================================

All of the debuggers above support OpenOCD 

Supported ADSP-SCxxx products by ICE debugger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ==================== ==============
JTAG version Voltage level switch Voltage Levels
============ ==================== ==============
ICE-1000     manual               1.8/3.3V
ICE-1500     manual               1.8/3.3V
ICE-2000     automatic            1.8/3.3V
Debug Agent  manual               1.8/3.3V
============ ==================== ==============

ICE JTAG ADSP Products Voltage levels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

============ ============= ==========================
ADSP Product Voltage Level Supported ICE
============ ============= ==========================
ADSP-SC573   3.3V          1000/1500/2000/Debug Agent
ADSP-SC589   3.3V          1000/1500/2000/Debug Agent
ADSP-SC594   3.3V          1000/1500/2000/Debug Agent
ADSP-SC598   3.3V          1000/1500/2000/Debug Agent
ADSP-SC846   1.8V          1000/1500/Debug Agent
============ ============= ==========================

.. _EV-SOMCRR-EZLITE: https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezlite.html
.. _EV-SOMCRR-EZKITE: https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ev-somcrr-ezkit.html
.. _EMULATORS: https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html
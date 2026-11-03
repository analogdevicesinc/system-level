.. _ad9084 prerequisites:

Prerequisites
===============================================================================


What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

#. The :adi:`EVAL-AD9084 <AD9084-FMCA-EBZ>` evaluation card.
#. A carrier platform. ADI does not offer these boards for sale or loan, getting
   one yourself is normal part of development or evaluation of the AD9084.

    - :ref:`See the supported carriers <ad9084 carriers>`.
    - The carrier may require one or more `FMC+ riser cards <https://www.samtec.com/kits/optics-fpga/fmcp-extender/>`__.

#. Analysis | Control | Evaluation (ACE) software with the AD9084 plugin installed.

    - :adi:`Download ACE software <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
    - :ref:`Apollo Profile Generator <ad9084 profile-generator>`

#. Some way to interact with the platform,

   - for the FPGA only solutions, this includes:

     - LAN cable (Ethernet)
     - Host PC (Windows or Linux)
     - Micro-USB or USB-C cables
     - SD Card with at least 16 GB of memory

#. Internet connection (without proxies makes things much easier) to update the
   scripts/binaries on the SD Card that came with the ADI FMC Card. (Firewalls
   are OK, proxies make things a pain).
#. RF Test equipment.

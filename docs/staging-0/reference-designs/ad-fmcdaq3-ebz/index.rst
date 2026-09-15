.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz

.. _ad-fmcdaq3-ebz:

AD-FMCDAQ3-EBZ User Guide
=========================

The
:adi:`AD-FMCDAQ3-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-FMCDAQ3-EBZ.html#eb-overview>`
is an FMC board for the high speed DAC :adi:`AD9152` & ADC :adi:`AD9680`. While
the complete chip level design package can be found on the ADI product pages of
these converters, information on the card, and how to use it, the design package
that surrounds it, and the software which can make it work, can be found here.

The purpose of the
:adi:`AD-FMCDAQ3-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-FMCDAQ3-EBZ.html#eb-overview>`
is a data acquisition platform that connects the analog world using FMC to the
FPGA.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcdaq3_top_new.png
   :width: 400px

#. :dokuwiki:`Introduction <ad-fmcdaq3-ebz/introduction>`
#. :dokuwiki:`Quick Start Guides <ad-fmcdaq3-ebz/quickstart>`

   #. :dokuwiki:`Linux on ZC706 <ad-fmcdaq3-ebz/quickstart/zynq>`
   #. :dokuwiki:`Linux on ZCU102 <ad-fmcdaq3-ebz/quickstart/zcu102>`
   #. :dokuwiki:`Linux on KCU105 <ad-fmcdaq3-ebz/quickstart/kcu105>`
   #. :dokuwiki:`Linux on VCU118 <ad-fmcdaq3-ebz/quickstart/vcu118>`
   #. :dokuwiki:`Linux on A10GX <ad-fmcdaq3-ebz/quickstart/a10gx>`

#. :dokuwiki:`Hardware <ad-fmcdaq3-ebz/hardware>` (including
   :dokuwiki:`schematics </ad-fmcdaq3-ebz/hardware#downloads>`)

   #. :dokuwiki:`Functional Overview & Specifications <ad-fmcdaq3-ebz/hardware/functional_overview>`

#. :dokuwiki:`Reference HDL Design <ad-fmcdaq3-ebz/reference_hdl>`
#. :dokuwiki:`Software <ad-fmcdaq3-ebz/software>`

   #. :dokuwiki:`No-OS drivers <ad-fmcdaq3-ebz/software/baremetal>`
   #. :dokuwiki:`Linux <ad-fmcdaq3-ebz/software/linux>`

      #. :dokuwiki:`ZC706, ... <ad-fmcdaq2-ebz/software/linux/zynq>`
      #. :dokuwiki:`A10GX (Nios2) </resources/tools-software/linux-drivers/platforms/nios2>`
      #. :dokuwiki:`Applications <ad-fmcdaq2-ebz/software/linux/applications>`

         #. :dokuwiki:`FMCDAQ3 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcdaq2_plugin>`

#. :dokuwiki:`Production Testing Process <ad-fmcdaq3-ebz/testing>`
#. :dokuwiki:`Help and Support <ad-fmcdaq3-ebz/help_and_support>`

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

.. _adsp linux-support:

Linux support
-------------

ADI supports running Linux on all ADSP SoCs with Cortex-A5 and A55 cores.
That includes the following repositories. New features are tracked in the
`ADSP Github Project <https://github.com/orgs/analogdevicesinc/projects/20/views/1>`__
and coordinated with the community during weekly public office hours at 17:00 CET
on Thursdays using a
`Jitsi meeting <https://meet.jit.si/AnalogDevicesIncDigitalSignalProcessingOfficeHours>`__.

To set up new ADSP evaluation boards see :ref:`Getting Started <adsp setup>`.

Upstream forks
^^^^^^^^^^^^^^

The ADSP Linux team maintains branches based on upstream releases (see
:external+linux:ref:`mainline`).

Changes made to support ADI hardware is upstreamed as quickly as possible.
Until those changes have been accepted upstream, they are maintained in the
following ADI forks.

Release versions include the upstream version and a ADI specific release number
(e.g.  ``1``, ``2``, ...). Current development branches are found by looking
for the the Commits link with the newest version and at least one Release.

- Deprecated :git-lnxdsp-linux:`+`:
    - v4.19
      :git-lnxdsp-linux:`Commits <commits/release/yocto-1.0.0+>`
    - v5.4.183
      :git-lnxdsp-linux:`Commits <commits/release/yocto-2.1.0+>`
    - v5.15.78
      :git-lnxdsp-linux:`Commits <commits/release/yocto-3.1.0+>`
- :git-linux:`+`:
    - v6.12.0:
      :git-linux:`Commits <commits/adsp-6.12.0-y+>`
      :git-linux:`Release 1 <releases/tag/adsp-6.12.0-1+>`
      :git-linux:`Release 2 <releases/tag/6.12.0-2+>`
      :git-linux:`Release 3 <releases/tag/6.12.0-3+>`
      :git-linux:`Release 4 <releases/tag/6.12.0-4+>`
      :git-linux:`Release 5 <releases/tag/6.12.0-5+>`
    - v6.12.89:
      :git-linux:`Commits <commits/adsp-6.12.89-y+>`
      :git-linux:`Release 1 <releases/tag/6.12.89-1+>`
    - v6.18.31:
      :git-linux:`Commits <commits/adsp-6.18.31-y+>`
      :git-linux:`Release 1 <releases/tag/6.18.31-1+>`
      :git-linux:`Release 2 <releases/tag/6.18.31-2+>`
      :git-linux:`Release 3 <releases/tag/6.18.31-3+>`

..
    - v6.12.38:
      :git-linux:`Commits <commits/adsp-6.12.38-y+>`
    - v6.12.65:
      :git-linux:`Commits <commits/adsp-6.12.65-y+>`

- :git-u-boot:`+`
    - v2025.07:
      :git-u-boot:`Commits <commits/adi-u-boot-2025.07.y+>`
      :git-u-boot:`Release 1 <releases/tag/v2025.07-1+>`
    - v2025.10:
      :git-u-boot:`Commits <commits/adi-u-boot-2025.10.y+>`
      :git-u-boot:`Release 1 <releases/tag/v2025.10-1+>`
      :git-u-boot:`Release 2 <releases/tag/v2025.10-2+>`
      :git-u-boot:`Release 3 <releases/tag/v2025.10-3+>`
      :git-u-boot:`Release 4 <releases/tag/v2025.10-4+>`
      :git-u-boot:`Release 5 <releases/tag/v2025.10-5+>`
    - v2026.01:
      :git-u-boot:`Commits <commits/adi-u-boot-2026.01.y+>`
- :git-buildroot:`+`
    - v2025.02 (LTS):
      :git-buildroot:`Commits <commits/adi-2025.02-y+>`
    - v2025.05:
      :git-buildroot:`Commits <commits/adi-2025.05.x+>`
      :git-buildroot:`Release 1 <releases/tag/2025.05-1+>`
      :git-buildroot:`Release 2 <releases/tag/2025.05-2+>`
    - v2026.02:
      :git-buildroot:`Commits <commits/adi-2026.02-y+>`
      :git-buildroot:`Release 1 <releases/tag/2026.02-1+>`
      :git-buildroot:`Release 2 <releases/tag/2026.02-2+>`
      :git-buildroot:`Release 3 <releases/tag/2026.02-3+>`
      :git-buildroot:`Release 4 <releases/tag/2026.02-4+>`
    - v2027.02 (LTS):
- :git-trusted-firmware-a:`+`
- :git-optee_os:`+`
- :git-openocd:`+`
    - :git-openocd:`0.12.0-1.0.0 <releases/tag/0.12.0-1.0.0+>`
      :git-openocd:`0.12.0-1.1.1 <releases/tag/0.12.0-1.1.1+>`
      :git-openocd:`0.12.0-1.1.2 <releases/tag/0.12.0-1.1.2+>`
      :git-openocd:`0.12.0-1.2.0 <releases/tag/0.12.0-1.2.0+>`
      :git-openocd:`0.12.0-1.3.0 <releases/tag/0.12.0-1.3.0+>`
      :git-openocd:`0.12.0-1.3.1 <releases/tag/0.12.0-1.3.1+>`
      :git-openocd:`0.12.0-1.4.0 <releases/tag/0.12.0-1.4.0+>`

ADI repositories
^^^^^^^^^^^^^^^^

For Yocto support see :ref:`adsp linux-support yocto` below.

- :git-adsp-ldr:`+`
    - :git-adsp-ldr:`v1.0.0 <releases/tag/v1.0.0+>`
      :git-adsp-ldr:`v1.0.1 <releases/tag/v1.0.1+>`
      :git-adsp-ldr:`v1.0.2 <releases/tag/v1.0.2+>`
      :git-adsp-ldr:`v1.0.3 <releases/tag/v1.0.3+>`
- :git-lnxdsp-repo-manifest:`+`
- :git-br2-external:`+`
    - v2025.05:
      :git-br2-external:`Release 0.1.0 <releases/tag/2025.05-0.1.0+>`
      :git-br2-external:`Release 0.2.0 <releases/tag/2025.05-0.2.0+>`
    - v2026.02:
      :git-br2-external:`Release 0.1.0 <releases/tag/2026.02-0.1.0+>`
      :git-br2-external:`Release 0.2.0 <releases/tag/2026.02-0.2.0+>`
      :git-br2-external:`Release 0.2.0 <releases/tag/2026.02-1.0.0+>`
- :git-rpmsg-examples:`+`
    - :git-rpmsg-examples:`v1.0.0 <releases/tag/v1.0.0+>`
- :git-rpmsg-utils:`+`
    - :git-rpmsg-utils:`v1.0.0 <releases/tag/v1.0.0+>`

.. _adsp linux-support yocto:

Yocto
~~~~~

:git-lnxdsp-adi-meta:`+`
  - Kirkstone:
    :git-lnxdsp-adi-meta:`Release v3.0.0 <releases/tag/3.0.0-rel+>`
    :git-lnxdsp-adi-meta:`Release v3.1.0 <releases/tag/3.1.0-rel+>`
    :git-lnxdsp-adi-meta:`Release v3.1.1 <releases/tag/3.1.1-rel+>`
    :git-lnxdsp-adi-meta:`Release v3.1.2 <releases/tag/3.1.2-rel+>`
  - Scarthgap:
    :git-lnxdsp-adi-meta:`Release v5.0.0 <releases/tag/5.0.0-rel+>`
    :git-lnxdsp-adi-meta:`Release v5.0.1 <releases/tag/5.0.1-rel+>`
    :git-lnxdsp-adi-meta:`Release v5.1.0 <releases/tag/5.1.0-rel+>`

For every official Yocto release, Poky defines the oldest and newest default supported
kernel versions. Newer versions of the kernel may be supported with recipe 
modifications or a separate recipe. The meta-adi layer defines it own linux
kernel recipe with its own version.

.. list-table::
   :header-rows: 1

   * - Release
     - ADSP Yocto Release
     - Oldest kernel
     - Newest kernel (Poky)
     - Newest kernel (ADSP)
   * - v3.0.0
     - Kirkstone (4.0)
     - 3.2.0, 3.14 (aarch64)
     - 5.15
     - 5.15
   * - v3.1.0
     - Kirkstone (4.0)
     - 3.2.0, 3.14 (aarch64)
     - 5.15
     - 5.15
   * - v3.1.1
     - Kirkstone (4.0)
     - 3.2.0, 3.14 (aarch64)
     - 5.15
     - 5.15
   * - v3.1.2
     - Kirkstone (4.0)
     - 3.2.0, 3.14 (aarch64)
     - 5.15
     - 5.15
   * - v5.0.0
     - Scarthgap (5.0)
     - 5.15
     - 6.6
     - 6.12
   * - v5.0.1
     - Scarthgap (5.0)
     - 5.15
     - 6.6
     - 6.12
   * - v5.1.0
     - Scarthgap (5.0)
     - 5.15
     - 6.6
     - 6.18
   * - v6.0.0 (In Development)
     - Wrynose (6.0)
     - 5.15
     - 6.18
     - 6.18

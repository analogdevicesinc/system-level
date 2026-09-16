.. _overview_versioning_support:

Versioning and Support
===============================================================================

This page explains how versioning works across `ADI DataX™
<https://developer.analog.com/solutions/adi-datax>`__, which component
versions work together, where to find support, and how to stay up-to-date
with new releases.

.. contents:: Contents
   :local:
   :depth: 2

Understanding ADI DataX Versioning
-------------------------------------------------------------------------------

ADI DataX consists of multiple independently-versioned components that must
work together. Understanding the versioning strategy for each component helps
you select compatible versions and plan upgrades.

Component Versioning Strategies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Across the different ADI source code repositories, there will be a concept of a release. This primarily relates to a a cross component release where components are built and tested together to ensure compatibility. This is done through a single Linux distribution (Kuiper Linux) that bundles specific versions of each component. no-OS releases follow this same cadence but are tested separately since they run in different environments.

The Kuiper Linux distribution release name is primarily tied to the version of AMD tools (Vivado), which the HDL release is also tied to. This is due to the historical supported hardware platforms that have been supported by ADI since 2014. Therefore, a release with the name ``2023_r2`` indicates that it is tied to AMD Vivado 2023.2 and Vitis 2023.2. The HDL, Linux, and no-OS repositories will all create release tags and branches with similar names.

Outside of HDL, Linux, and no-OS, other components such as libiio and pyadi-iio have their own independent versioning strategies that are not tied to the Kuiper Linux or HDL release names. However, for each Kuiper Linux release, specific versions of libiio and pyadi-iio are bundled and tested together to ensure compatibility. These are documented in the Kuiper Linux release notes.

.. svg:: versioning-tracks.svg
   :align: center

   Three release tracks across ADI DataX and how they converge in a Kuiper
   Linux release. Track A shares a single name across HDL, Linux, and no-OS;
   Track B versions independently; Kuiper pins one tested combination of all
   of them.

.. note::

   In 2026, new release naming will be more generic to denote the year and not
   be as strictly tied to a version of AMD tools.

HDL
^^^

Tags ``YYYY_rN`` (e.g. ``hdl_2024_r2``), bi-annual, with LTS branches and a
``main`` development branch. The release name pairs with the AMD Vivado /
Vitis version the bitstream targets. Release notes:
:git-hdl:`GitHub Releases <releases+>`,
:external+hdl:ref:`releases user guide <releases>`.

Linux Kernel Drivers
^^^^^^^^^^^^^^^^^^^^

Tracks upstream Linux versions plus ADI patches (e.g. ``6.1.75-adi``); LTS
kernels (5.15, 6.1, 6.6) are recommended for production. Drivers are
upstreamed to mainline when stable. Release notes:
:git-linux:`GitHub Releases <releases+>`,
:external+linux:ref:`releases user guide <getting_started>`.

libiio
^^^^^^

Semantic versioning, ``vMAJOR.MINOR`` (e.g. ``v0.26``), 2–3 releases per
year. Minor versions add features and stay backwards-compatible; major
bumps may break API. Release notes:
:git-libiio:`GitHub Releases <releases+>`.

no-OS
^^^^^

``YYYY_rN`` tags synchronized with HDL releases (quarterly cadence).
Release notes: :git-no-OS:`GitHub Releases <releases+>`.

pyadi-iio
^^^^^^^^^

Python semver, ``vMAJOR.MINOR.PATCH`` (e.g. ``v0.0.17``); published to
PyPI on a monthly-to-quarterly cadence; backwards-compatible within a
minor version. Release notes:
:git-pyadi-iio:`GitHub Releases <releases+>`.

Kuiper Linux
^^^^^^^^^^^^

``YYYY_rN`` releases (e.g. ``2024_r1``), bi-annual. Debian-based; bundles
a tested combination of ADI's Linux kernel, libiio, pyadi-iio, Scopy,
IIO Oscilloscope, and other tools. The exact bundled versions are
documented in each release's notes. Release notes:
:git-adi-kuiper-gen:`GitHub Releases <releases+>`.

Version Compatibility Matrix
-------------------------------------------------------------------------------

The following table shows tested and recommended version combinations:

.. list-table:: Recommended Version Combinations
   :header-rows: 1
   :widths: 14 15 10 12 15 12 12 24

   * - Supported Tools
     - HDL
     - Linux Kernel
     - libiio
     - pyadi-iio
     - Kuiper Linux
     - no-OS
     - Notes
   * - Vivado 2025.1
     - main
     - main
     - libiio-v0
     - main
     - main
     - main
     - **Bleeding Edge** - Not fully tested, may have issues
   * - Vivado 2023.2
     - hdl_2023_r2
     - 6.1.70
     - v0.26
     - v0.0.19
     - 2023_r2
     - 2023_r2
     - **Latest Stable** - Recommended for new projects
   * - Vivado 2022.2
     - 2022_r2
     - 5.15.x-adi
     - v0.24
     - v0.0.15
     - 2022_r2
     - 2022_r2
     - Previous Release - Mature, conservative


Compatibility Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Forward Compatibility:**

- **libiio:** Generally backward compatible; newer versions work with older contexts
- **pyadi-iio:** Requires compatible libiio version (usually latest or previous release)
- **Linux drivers:** Mainline drivers work across kernel versions (devicetree may differ)
- **HDL:** IP cores are forward compatible within same Vivado/Quartus major version

**Breaking Changes:**

Major version bumps (e.g., libiio v0.x → v1.0) may introduce API changes. Check
release notes before upgrading production systems.

**Mixing Versions:**

You can generally mix versions across the network boundary:

- Old libiio client can access new server (via ``ip:`` backend)
- New libiio client can access old devices
- pyadi-iio works with multiple libiio versions

**FPGA + Linux:**

HDL and Linux kernel versions must match for:

- Devicetree bindings (new devices)
- AXI IP core addresses
- Driver compatibility with HDL features

Use the same release tag (e.g., ``2023_r2`` and ``hdl_2023_r2``) to ensure compatibility.

Checking Installed Versions
-------------------------------------------------------------------------------

The quickest way to capture every component version on a running system is the
``check_versions.sh`` helper script (output covers the Linux kernel, libiio,
pyadi-iio, Kuiper Linux, and any local HDL or no-OS clones). Include its
output when filing an issue or asking for help.

Release Cadence
-------------------------------------------------------------------------------

Each component publishes its own release notes; rather than tracking a printed
schedule, watch the corresponding GitHub repository for "Releases only"
notifications:

- HDL: :git-hdl:`releases <releases+>` — bi-annual, named ``YYYY_rN`` and
  paired with the AMD Vivado version of the same year.
- Linux kernel: :git-linux:`releases <releases+>` — tracks upstream LTS
  with ADI patches.
- no-OS: :git-no-OS:`releases <releases+>` — quarterly, synchronized with
  HDL.
- libiio: :git-libiio:`releases <releases+>` — semver, 2–3 releases per
  year.
- pyadi-iio: :git-pyadi-iio:`releases <releases+>` — published to PyPI on
  a monthly-to-quarterly cadence.
- Kuiper Linux: :git-adi-kuiper-gen:`releases <releases+>` — annual; pins
  one tested combination of every component above.

Critical fixes are backported to the current release branch only; older
release branches do not receive new features or updates. When asking for
support, name the release you're on (e.g. ``Kuiper Linux 2023_r2`` /
``HDL hdl_2023_r2``) so a maintainer can match what you're seeing.

Before upgrading a production system, read the relevant release notes,
upgrade HDL and the Linux kernel together when their tags match
(devicetree bindings and AXI addresses are the load-bearing pair), and
verify in a non-production environment first.

Support Channels
-------------------------------------------------------------------------------

- `EngineerZone <https://ez.analog.com/>`_ — ADI's monitored support forum;
  fastest response for general questions. Search first, then post with
  hardware details, component versions, and error messages.
- `ADI Wiki <https://wiki.analog.com/>`_ — driver pages, application notes,
  hardware setup guides, known issues and workarounds.
- GitHub issues per repo for bug reports and feature requests:
  `hdl <https://github.com/analogdevicesinc/hdl/issues>`_,
  `linux <https://github.com/analogdevicesinc/linux/issues>`_,
  `libiio <https://github.com/analogdevicesinc/libiio/issues>`_,
  `no-OS <https://github.com/analogdevicesinc/no-OS/issues>`_,
  `pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio/issues>`_.
- For customers with a support contract: contact ADI technical support via
  your regional sales representative.

When you file something, include the hardware (device part number,
evaluation board, carrier board), component versions
(``check_versions.sh`` output), the complete error message (text, not a
screenshot), the kernel log (``dmesg | grep -i 'ad\|iio'``), and a minimal
reproducible example.

Contributing
-------------------------------------------------------------------------------

ADI DataX is open source. Contributions go through GitHub: fork, branch, and
submit a pull request. Each repository carries its own ``CONTRIBUTING.md``
with code-style, commit-message, and sign-off requirements (Developer
Certificate of Origin sign-off is required across the board).

Upgrade procedures live in each component's own docs because they differ
substantially (rebuild + reflash MCU firmware vs. rebuild + reprogram FPGA
bitstream vs. ``apt upgrade`` packages):

- HDL: :external+hdl:ref:`releases user guide <releases>`
- Linux kernel: :doc:`/linux/kernel/index`
- no-OS: :external+no-OS:doc:`index`
- libiio: :ref:`libiio`
- pyadi-iio: :external+pyadi-iio:doc:`index`
- Kuiper Linux: :doc:`/linux/kuiper/index`

Deprecated features get at least two releases of advance notice (announced
in release notes, with a runtime warning where the API permits) before
removal, and a documented migration path to the replacement.

See Also
-------------------------------------------------------------------------------

- :doc:`architecture` — full-stack architecture
- :doc:`components` — per-component documentation
- :doc:`workflows` — concrete end-to-end scenarios

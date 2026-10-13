.. _overview_versioning_support:

Versioning and Support
===============================================================================

This page explains how versioning works across the ADI ecosystem, which component
versions work together, where to find support, and how to stay up-to-date with
new releases.

.. contents:: Contents
   :local:
   :depth: 2

Understanding Ecosystem Versioning
-------------------------------------------------------------------------------

The ADI ecosystem consists of multiple independently-versioned components that
must work together. Understanding the versioning strategy for each component
helps you select compatible versions and plan upgrades.

Component Versioning Strategies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Across the different ADI source code repositories, there will be a concept of a release. This primarily relates to a a cross component release where components are built and tested together to ensure compatibility. This is done through a single Linux distribution (Kuiper Linux) that bundles specific versions of each component. no-OS releases follow this same cadence but are tested separately since they run in different environments.

The Kuiper Linux distribution release name is primarily tied to the version of AMD tools (Vivado), which the HDL release is also tied to. This is due to the historical supported hardware platforms that have been supported by ADI since 2014. Therefore, a release with the name ``2023_r2`` indicates that it is tied to AMD Vivado 2023.2 and Vitis 2023.2. The HDL, Linux, and no-OS repositories will all create release tags and branches with similar names.

Outside of HDL, Linux, and no-OS, other components such as libiio and pyadi-iio have their own independent versioning strategies that are not tied to the Kuiper Linux or HDL release names. However, for each Kuiper Linux release, specific versions of libiio and pyadi-iio are bundled and tested together to ensure compatibility. These are documented in the Kuiper Linux release notes.

.. note::

   In 2026, new release naming will be more generic to denote the year and not
   be as strictly tied to a version of AMD tools.

HDL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** ``YYYY_rN`` (e.g., ``hdl_2024_r2``)

**Strategy:**

- Bi-annual releases
- Git tags for each release
- Branches for Long-Term Support (LTS) versions
- ``main`` branch tracks latest development

**What Changes:**

- New device support
- IP core updates (JESD204, SPI Engine, DMA)
- Bug fixes and performance improvements
- Vivado/Quartus version requirements

**Finding Version:**

.. code-block:: bash

   cd hdl
   git describe --tags
   # e.g., hdl_2024_r2

**Release Notes:**

| :git-hdl:`GitHub Releases <releases+>`
| :external+hdl:ref:`Releases user guide <releases>`

Linux Kernel Drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** Mainline kernel version + ADI patches (e.g., ``6.1.75-adi``)

**Strategy:**

- Tracks upstream Linux kernel releases
- ADI patches applied on top for new features
- Drivers upstreamed to mainline when stable
- LTS kernels (5.15, 6.1, 6.6) recommended for production
- ``main`` branch uses AMD/Xilinx as upstream base. See Linux README for details.

**What Changes:**

- New drivers
- Devicetree bindings
- Bug fixes and optimizations
- Documentation updates

**Finding Version:**

.. code-block:: bash

   uname -r
   # e.g., 6.1.75-adi-xilinx-v2024.1

**Release Notes:**

| :git-linux:`GitHub Releases <releases+>`
| :external+linux:ref:`Releases user guide <getting_started>`

libiio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** ``vMAJOR.MINOR`` (e.g., ``v0.26``)

**Strategy:**

- Semantic versioning approaching v1.0
- Minor versions add features, maintain backward compatibility
- ``main`` branch for development
- Tagged releases on GitHub

**What Changes:**

- New backends (e.g., serial backend added in v0.21)
- Performance improvements
- API additions (rarely breaking changes)
- Bug fixes

**Finding Version:**

.. code-block:: bash

   iio_info --version
   # Libiio version: 0.26 (git tag: a0eca0d)

.. code-block:: python

   import iio
   print(iio.version)
   # ('0', '26', 'a0eca0d')

**Release Notes:** :git-libiio:`GitHub Releases <releases+>`

no-OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** ``YYYY_rN`` (synchronized with HDL releases)

**Strategy:**

- Quarterly releases aligned with HDL
- Tagged releases on GitHub
- ``main`` branch for development
- Platform HAL updates

**What Changes:**

- New device drivers
- Platform support (new MCUs)
- TinyIIO server updates
- Build system improvements

**Finding Version:**

Check firmware build logs or ``git describe --tags`` in source tree.

**Release Notes:** :git-no-OS:`GitHub Releases <releases+>`

pyadi-iio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** ``vMAJOR.MINOR.PATCH`` (e.g., ``v0.0.17``)

**Strategy:**

- Python semantic versioning
- Published to PyPI (``pip install pyadi-iio``)
- Frequent releases (monthly to quarterly)
- Backward compatible within minor versions

**What Changes:**

- New device classes
- API additions
- Bug fixes
- libiio dependency updates

**Finding Version:**

.. code-block:: bash

   pip show pyadi-iio
   # Version: 0.0.17

.. code-block:: python

   import adi
   print(adi.__version__)
   # '0.0.17'

**Release Notes:** :git-pyadi-iio:`GitHub Releases <releases+>`

Kuiper Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version Format:** ``YYYY_rN`` (e.g., ``2024_r1``)

**Strategy:**

- Bi-annual releases (r1, r2)
- Debian-based, tracks Debian stable
- Bundles specific versions of ADI tools
- Rolling updates via ``apt`` between releases

**What's Included:**

- Base: Debian 12 (Bookworm) or 11 (Bullseye)
- Kernel: ADI-patched Linux (e.g., 6.1.x)
- libiio: Specific version (e.g., 0.26)
- pyadi-iio: Specific version (e.g., 0.0.17)
- Scopy: Latest stable
- Tools: IIO Oscilloscope, GNU Radio, development tools

**Finding Version:**

.. code-block:: bash

   cat /etc/issue
   # Analog Devices Kuiper Linux 2024_r1

**Release Notes:** :git-adi-kuiper-gen:`GitHub Releases <releases+>`

Version Compatibility Matrix
-------------------------------------------------------------------------------

The following table shows tested and recommended version combinations:

.. list-table:: Recommended Version Combinations
   :header-rows: 1
   :widths: 12 15 10 12 15 12 24

   * - HDL
     - Linux Kernel
     - libiio
     - pyadi-iio
     - Kuiper Linux
     - no-OS
     - Notes
   * - **2024_r2**
     - 6.1.75-adi
     - v0.26
     - v0.0.17
     - 2024_r1
     - 2024_r2
     - **Latest Stable** - Recommended for new projects
   * - **2024_r1**
     - 6.1.54-adi
     - v0.25
     - v0.0.16
     - 2023_r2
     - 2024_r1
     - **LTS** - Production use, well-tested
   * - **2023_r2**
     - 5.15.x-adi
     - v0.24
     - v0.0.15
     - 2023_r2
     - 2023_r2
     - Previous LTS - Mature, conservative
   * - **main**
     - 6.6.x-adi
     - main
     - main
     - N/A
     - main
     - **Development** - Bleeding edge, may have issues

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

Use the same release tag (e.g., both ``2024_r1``) to ensure compatibility.

Checking Installed Versions
-------------------------------------------------------------------------------

Quick Version Check Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run this on your Linux system to see all installed ADI component versions:

.. code-block:: bash

   #!/bin/bash
   echo "=== ADI Ecosystem Version Check ==="
   echo ""

   echo "Linux Kernel:"
   uname -r

   echo ""
   echo "libiio:"
   iio_info --version 2>&1 | grep "version:"

   echo ""
   echo "pyadi-iio:"
   python3 -c "import adi; print('v' + adi.__version__)" 2>/dev/null || echo "Not installed"

   echo ""
   echo "Kuiper Linux:"
   cat /etc/issue 2>/dev/null | grep Kuiper || echo "Not Kuiper Linux"

   echo ""
   echo "HDL (if cloned):"
   cd ~/hdl 2>/dev/null && git describe --tags 2>/dev/null || echo "HDL not found"

   echo ""
   echo "no-OS (if cloned):"
   cd ~/no-OS 2>/dev/null && git describe --tags 2>/dev/null || echo "no-OS not found"

Save as ``check_versions.sh`` and run with ``bash check_versions.sh``.

Release Cadence and Planning
-------------------------------------------------------------------------------

Typical Release Schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   This is a placeholder schedule, actual dates may vary.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Component
     - Frequency
     - Typical Timing
   * - **HDL**
     - Quarterly
     - February (r1), May (r2), August (r3), November (r4)
   * - **Linux Kernel**
     - Continuous
     - Follows upstream LTS, ADI patches as needed
   * - **libiio**
     - As Needed
     - 2-3 times per year, or when major features ready
   * - **no-OS**
     - Quarterly
     - Synchronized with HDL releases
   * - **pyadi-iio**
     - Monthly-Quarterly
     - As new device support or features are added
   * - **Kuiper Linux**
     - Annual
     - Usually Q1 (r1) and Q3 (r2)
   * - **Scopy**
     - Quarterly-Biannual
     - Independent release cycle

Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Critical fixes may be backported to the current release branch. Older releases will not receive new features or updates. It is advised to request support for the latest stable release, as fixes are added there first. As newer releases become available, older release support is phased out and will have limited assistance.

When asking for support, please specify which release you are using (e.g., Kuiper Linux 2024_r1, HDL 2024_r2, libiio v0.26) to get the most accurate help. If you are using development branches (``main``), be aware that these may have bugs and are not guaranteed stable.

**When to Use Latest:**

- New projects in development
- Need latest device support
- Active development, frequent updates acceptable
- Prototyping and evaluation

Staying Updated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Subscribe to Announcements:**

- Watch GitHub repositories (analogdevicesinc/hdl, /linux, /libiio, /no-OS, /pyadi-iio)
- Enable "Releases only" notifications
- Join EngineerZone forums for announcements

**Check for Updates:**

.. code-block:: bash

   # Update package lists (Debian/Ubuntu/Kuiper)
   sudo apt update
   sudo apt list --upgradable | grep -E 'libiio|adi'

   # Update Python packages
   pip list --outdated | grep pyadi-iio

   # Update from GitHub
   cd ~/hdl && git fetch && git log HEAD..origin/main --oneline

**Upgrade Strategy:**

1. **Read release notes first** - Check for breaking changes
2. **Test in non-production environment**
3. **Backup configurations** (devicetree, application code)
4. **Upgrade dependencies together** (e.g., HDL + kernel in sync)
5. **Verify functionality** before deploying

Support Channels
-------------------------------------------------------------------------------

Getting Help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**EngineerZone Forums:**

https://ez.analog.com/

ADI's official support forum, monitored by engineers:

- Search existing discussions
- Post questions with hardware details, software versions, error messages
- Fastest response for general questions

**GitHub Issues:**

Report bugs and request features on specific repositories:

- `HDL Issues <https://github.com/analogdevicesinc/hdl/issues>`_
- `Linux Issues <https://github.com/analogdevicesinc/linux/issues>`_
- `libiio Issues <https://github.com/analogdevicesinc/libiio/issues>`_
- `no-OS Issues <https://github.com/analogdevicesinc/no-OS/issues>`_
- `pyadi-iio Issues <https://github.com/analogdevicesinc/pyadi-iio/issues>`_

Include:

- Component versions (``check_versions.sh`` output)
- Hardware platform
- Complete error messages
- Minimal reproducible example

**ADI Wiki:**

https://wiki.analog.com/

Comprehensive documentation:

- Driver pages with detailed documentation
- Application notes
- Hardware setup guides
- Known issues and workarounds

**Product Pages:**

Datasheets, evaluation board user guides, design files on analog.com:

- Technical specifications
- Reference schematics
- Characterization data

**Technical Support:**

For customers with support contracts, contact ADI technical support directly
through your regional sales representative or via the ADI website.

**Community Resources:**

- **GNU Radio Mailing List:** For SDR-related questions
- **Raspberry Pi Forums:** For RPi hardware questions
- **Stack Overflow:** Tag with ``analog-devices``, ``iio``, ``pyadi-iio``

What to Include When Asking for Help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Essential Information:**

1. **Hardware:**

   - Device part number (e.g., AD9081, AD4080)
   - Evaluation board (e.g., AD9081-FMCA-EBZ)
   - Carrier board (e.g., ZCU102, Nucleo-H563ZI, Raspberry Pi 4)

2. **Software Versions:**

   - Run ``check_versions.sh`` and include output
   - Specify if using Kuiper Linux or custom build

3. **Error Details:**

   - Complete error messages (not screenshots of text)
   - Kernel logs: ``dmesg | grep -i ad\|iio``
   - Application output with debug enabled

4. **What You've Tried:**

   - Steps to reproduce
   - Troubleshooting already attempted
   - Related forum/GitHub threads searched

5. **Expected vs. Actual:**

   - What you expected to happen
   - What actually happened

**Good Example:**

   *"I'm using AD4080 with STM32 Nucleo-H563ZI running no-OS 2023_r2 firmware.
   When I try to connect via serial from my Ubuntu 22.04 host with libiio 0.26,
   I get 'Error: no device found'. Output of check_versions.sh attached.
   iio_info -u local: works on the host (finds CPU temp sensor). The STM32
   appears as /dev/ttyACM0 and I can see serial output in minicom. I tried
   increasing baud rate to 460800 with same result. Related GitHub issue #123
   mentions similar problem but solution didn't work for me."*

**Bad Example:**

   *"My ADC doesn't work. Help!"*

Contributing to the Ecosystem
-------------------------------------------------------------------------------

The ADI ecosystem is open source and welcomes community contributions.

How to Contribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Code Contributions:**

1. Fork the repository on GitHub
2. Create a feature branch (``git checkout -b feature/my-feature``)
3. Make changes following project coding style
4. Test thoroughly on target hardware
5. Submit a Pull Request with detailed description

**Documentation Contributions:**

- Fix typos or unclear explanations
- Add examples or tutorials
- Translate documentation
- Update outdated information

**Bug Reports:**

High-quality bug reports are valuable contributions:

- Detailed reproduction steps
- Minimal test case
- System information (versions, hardware)
- Logs and error messages

**Hardware Testing:**

- Test pre-release versions on your hardware
- Report compatibility issues
- Validate fixes before release

**Sharing Knowledge:**

- Answer questions on EngineerZone
- Write blog posts or tutorials
- Present at conferences
- Share example applications

Contribution Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each repository has a ``CONTRIBUTING.md`` file with specific guidelines. General
principles:

- **Code Style:** Follow existing style (HDL: Verilog standards; Python: PEP8)
- **Commit Messages:** Clear, concise, imperative mood ("Add feature" not "Added feature")
- **Testing:** Ensure changes don't break existing functionality
- **Documentation:** Update docs to match code changes
- **Sign-off:** Include ``Signed-off-by:`` in commits (Developer Certificate of Origin)

Migration Guides
-------------------------------------------------------------------------------

Upgrading Between Releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**HDL Upgrades:**

When upgrading HDL versions:

1. Check :external+hdl:doc:`release notes <user_guide/releases>` for breaking changes
2. Update Vivado/Quartus to required version (check project README)
3. Rebuild project (``make clean && make``)
4. Update devicetree if using new features
5. Recompile Linux kernel if devicetree changed
6. Test boot and device enumeration

**Linux Kernel Upgrades:**

1. Review `kernel changelog <https://analogdevicesinc.github.io/linux/getting_started.html>`_
2. Update devicetree for new bindings
3. Recompile kernel and modules
4. Update userspace tools (libiio) if needed
5. Test IIO device functionality

**libiio Upgrades:**

Usually straightforward:

.. code-block:: bash

   sudo apt update && sudo apt upgrade libiio-utils python3-libiio

Or build from source:

.. code-block:: bash

   git clone https://github.com/analogdevicesinc/libiio
   cd libiio
   git checkout v0.26  # or latest tag
   mkdir build && cd build
   cmake .. && make && sudo make install

**pyadi-iio Upgrades:**

.. code-block:: bash

   pip install --upgrade pyadi-iio

Check for API changes in :git-pyadi-iio:`release notes <releases+>`.

**no-OS Upgrades:**

Firmware upgrades require rebuilding and reflashing:

1. Pull latest tag: ``git checkout 2024_r2``
2. Update project if needed (check project README for changes)
3. Rebuild: ``mkdir build && cd build && cmake .. && make``
4. Flash new binary to microcontroller
5. Verify IIO device enumeration from host

Deprecation Policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Advance Notice: Deprecated features announced in release notes
- Transition Period: Minimum 2 releases before removal
- Migration Path: Alternative solution provided
- Warnings: Deprecated APIs emit warnings before removal

See Also
-------------------------------------------------------------------------------

**Next Steps:**

- :doc:`architecture` - Understanding the full stack
- :doc:`components` - Component-specific documentation
- :doc:`workflows` - Practical examples with version requirements

**Support:**

- :ez:`/`
- :dokuwiki:`Wiki </>`
- `GitHub Organization <https://github.com/analogdevicesinc/>`_

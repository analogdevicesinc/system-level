.. _packaging:

Packaging at ADI
""""""""""""""""

ADI has a large portfolio of analog and digital components. That hardware is
enabled by a complex software ecosystem. To provide internal users and
customers a better experience we are evaluating how to provide a consistent
approach for packaging.

Distribution packaging
======================

Packaging for distributions (e.g. Debian, Ubuntu, and Fedora) provides numerous
advantages:

- Convenient for users to find and install the software
- Updates with the rest of the system software while containers and language
  specific package managers are often never updated
- Supports creating users, changing permissions, installing systemd service
  files and udev rules

There are two recommended approaches, either use fpm with packages.analog.com
or upstream packages.

Software projects
=================

- Linux kernel distribution packages
- ADSP LDR
- ADI fork of OpenOCD
- Upstream Labgrid
- IIO-Oscilliscope
- Boot loaders to support ADI perihperals and FPGA fabric on Xilinx evaluation
  boards
- ...

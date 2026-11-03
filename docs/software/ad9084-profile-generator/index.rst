.. _ad9084 profile-generator:

AD9084 (Apollo) Profile Generator
=================================

The Apollo plugin comes bundled with the ACE software and can be downloaded
from :adi:`here <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`.

.. image:: apollo_plugin_main_window.png

Apollo Profile Generator
------------------------

The Apollo profile generator is a tool that allows you to create profiles
with different configurations for the AD9084 device. The profiles are then
programmed into the device to configure it to work in a specific way.

.. image:: apollo_profile_generator.png

The profile generator allows you to configure various parameters of the AD9084:

- The JESD parameters
- ADC / DAC clock frequencies
- Interpolation / Decimation factors

.. important::

   The JESD parameters configured in the profile have to match the ones used to build
   the AD9084 HDL design.

.. note::

   By pressing the ``Save`` button, the profile generator will generate 3 files inside the
   ``User Library`` folder:

   - A ``.json`` file containing all the profile settings
   - A ``_summary.json`` file containing a brief summary of the profile settings
   - A ``.bin`` file containing the profile settings in binary format which will be
     loaded on the AD9084

Using the generated profile
---------------------------

The :adi:`AD9084` driver will look for the profile in the default location
``linux/lib/firmware/`` in order to program it to the board.

.. important::

   The driver reads the ``adi,device-profile-fw-name`` property from the device tree
   and will search for the corresponding ``.bin`` file.

.. note::

   The following commands assume that the profile has been generated and saved
   with the ``new_profile.bin`` name.

After generating the profile, copy the ``.bin`` file to the ``linux/lib/firmware`` location:

.. shell:: bash
   :show-user:

   $cp <path_to_profile>/new_profile.bin linux/lib/firmware/

Update the defconfig to include the generated profile
+++++++++++++++++++++++++++++++++++++++++++++++++++++

For Virtex UltraScale+ carriers (:xilinx:`VCU118`/:xilinx:`VCU128`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update the ``arch/microblaze/configs/adi_mb_defconfig`` file to include
the generated ``.bin`` under the ``CONFIG_EXTRA_FIRMWARE`` option:

.. shell:: bash
   :show-user:

   $cd linux
   $sed -i 's/^CONFIG_EXTRA_FIRMWARE="/&new_profile.bin /' arch/arch/microblaze/configs/adi_mb_defconfig

   $cat arch/arch/microblaze/configs/adi_mb_defconfig | grep 'CONFIG_EXTRA_FIRMWARE='
    CONFIG_EXTRA_FIRMWARE="new_profile.bin APOLLO_FW_CPU1_B.bin <...>"

You can then follow the :ref:`Linux kernel build flow <ad9084_ebz microblaze linux>`
to build the kernel and boot it on the board.

For Versal carriers (:xilinx:`VCK190`/:xilinx:`VPK180`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update the ``arch/arm64/configs/adi_versal_defconfig`` file to include
the generated ``.bin`` under the ``CONFIG_EXTRA_FIRMWARE`` option:

.. shell:: bash
  :show-user:

  $cd linux
  $sed -i 's/^CONFIG_EXTRA_FIRMWARE="/&new_profile.bin /' arch/arm64/configs/adi_versal_defconfig

  $cat arch/arm64/configs/adi_versal_defconfig | grep 'CONFIG_EXTRA_FIRMWARE='
  CONFIG_EXTRA_FIRMWARE="new_profile.bin APOLLO_FW_CPU1_B.bin <...>"

You can then follow the :ref:`Linux kernel build flow <ad9084 versal linux>`
to build the kernel and boot it on the board.

For Intel Agilex 7 I-Series (`FM87 <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1305>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update the ``arch/arm64/configs/adi_zynqmp_defconfig`` file to include
the generated ``.bin`` under the ``CONFIG_EXTRA_FIRMWARE`` option:

.. shell:: bash
  :show-user:

  $cd linux
  $sed -i 's/^CONFIG_EXTRA_FIRMWARE="/&new_profile.bin /' arch/arm64/configs/adi_zynqmp_defconfig

  $cat arch/arm64/configs/adi_zynqmp_defconfig | grep 'CONFIG_EXTRA_FIRMWARE='
  CONFIG_EXTRA_FIRMWARE="new_profile.bin APOLLO_FW_CPU1_B.bin <...>"

You can then follow the :ref:`Linux kernel build flow <ad9084 agilex linux>`
to build the kernel and boot it on the board.

.. important::

   The ``adi,device-profile-fw-name`` property must also be updated
   in the device tree to match the name of the newly generated profile.

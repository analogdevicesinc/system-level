.. _adsp-system-protection:

System Protection Features
==========================

The ADSP-SC5xx processors include two important hardware protection
units that help secure and protect system resources from unintended access or modification.

.. note::
   This documentation applies to all SHARC Connect processors (SC57x, SC58x, SC59x).
   The core concepts are the same across all families. Refer to your processor's Hardware
   Reference Manual for family-specific details.

Overview
--------

The system protection features consist of:

- **System Protection Unit (SPU)** - Protects peripheral registers from
  unauthorized writes
- **System Memory Protection Unit (SMPU)** - Protects memory regions from
  unauthorized read/write access

These protection mechanisms work together to create a secure and reliable system by
preventing accidental or malicious access to critical system resources.

.. note::
   A known hardware anomaly (20000003) affects SPU and SMPU on SC5xx silicon in all revisions.
   Non-secure reads or writes to the upper half (address offset + 0x800 to + 0xFFF)
   of each SPU/SMPU instance may be erroneously blocked. As workaround, the documentation suggests
   avoiding accessing these ranges from non-secure masters.

When to Use These Features
--------------------------

Use the system protection features when you need to:

- Prevent unintended configuration changes to critical peripherals
- Implement security boundaries between secure and non-secure software
- Protect sensitive memory regions from unauthorized access
- Create multiple protection zones with different access rights
- Debug system integration issues by detecting unauthorized accesses

Common Use Cases
----------------

- Lock down clock, power, and boot configuration registers after system
  initialization to prevent accidental reconfiguration that could
  destabilize the system.
- Configure SPU and SMPU to enforce ARM TrustZone security boundaries,
  ensuring secure firmware has exclusive access to sensitive peripherals and
  memory regions.
- In multi-core systems, use protection units to isolate each core's
  resources and prevent interferences.
- Enable protection violations to generate interrupts that help identify
  unauthorized access attempts during development and integration.

.. toctree::
   :maxdepth: 2

   spu
   smpu

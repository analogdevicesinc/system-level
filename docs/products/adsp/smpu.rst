.. _adsp-smpu:

System Memory Protection Unit (SMPU)
====================================

The System Memory Protection Unit (SMPU) provides flexible protection of memory
regions against unauthorized read or write access. Think of it as a security
checkpoint for memory. This peripheral examines every memory transaction and
decides whether to allow or block it.

.. note::
   This guide applies to all ADSP-SC5xx processors. While the SMPU
   functionality is consistent across processor families, the specific details vary:

   - Number and location of SMPU instances
   - System ID assignments for bus requesters
   - Number of available protection regions

What Does the SMPU Do?
-------------------------

The SMPU protects specific memory regions from unauthorized read or write
transactions by specific cores and DMA requesters. We can configure:

- Which memory regions to protect
- Whether to protect reads, writes, or both
- Which bus requesters are allowed to access each region
- Whether secure or non-secure transactions are permitted

Key Features
---------------

- **Multiple SMPU Instances** - Each processor family has multiple SMPU
  instances protecting different memory paths; the number and configuration
  varies by family.
- **Multiple Protection Regions** - Each SMPU instance can monitor up to 8
  memory regions simultaneously, each with its own size and protection
  settings.
- **Flexible Region Sizes** - Memory regions can range from 4 KB to 4 GB,
  with alignment requirements based on the region size.
- **ID-Based Protection** - Each bus requester has a unique ID; the SMPU can
  allow or block access based on these IDs.
- **Security Integration** - The SMPU works with Arm TrustZone to enforce
  security boundaries:

  - Block non-secure accesses to secure memory
  - Allow secure masters to access both secure and non-secure memory
  - Per-region security configuration

Multiple SMPU Instances
~~~~~~~~~~~~~~~~~~~~~~~

Make sure you're configuring the right SMPU instance for the memory path you want
to protect; L2 memory has multiple SMPU instances. An example from SC59x is given below.

ADSP-SC59x SMPU Instances
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Instance
     - Location
     - What It Protects
   * - SMPU-CL2_0
     - L2 Core Port 0
     - L2 SRAM Banks 0-3, Boot ROM0
   * - SMPU-DL2_0
     - L2 DMA Port 0
     - L2 SRAM Banks 0-7, Boot ROM0-2
   * - SMPU-CL2_1
     - L2 Core Port 1
     - L2 SRAM Banks 4-7, Boot ROM1-2
   * - SMPU-DL2_1
     - L2 DMA Port 1
     - L2 SRAM Banks 0-7, Boot ROM0-2
   * - SMPU-CL2_2
     - L2 Core Port 2
     - L2 SRAM Banks 0-7, Boot ROM0-2
   * - SMPU-DMC0
     - DDR Controller
     - External DDR3 memory
   * - SMPU-SPI2
     - SPI/OSPI Flash
     - External flash memory
   * - SMPU-OTP
     - OTP Memory
     - One-time programmable memory

For SC57x and SC58x, see the SMPU instance tables in the respective
:adi:`SC57x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/adsp-sc57x-2157x_hwr.pdf>` and
:adi:`SC58x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf>`.

How It Works
---------------

The SMPU examines every memory transaction in this order:

1. Address Check - Does it fall within a protected region?
2. Operation Check - Is it a read or write?
3. Bus Requester ID check - Which bus requester is making the request?
4. Security Level Check - Is it a secure or non-secure transaction?
5. Decide - Pass the transaction, or return an error

A SMPU sits between bus requesters and memory.

Basic Configuration
----------------------

Protecting a Memory Region
~~~~~~~~~~~~~~~~~~~~~~~~~~

To protect a memory region, we need to configure several registers.

First, we should define the region to protect. This can be done by setting the
base address and size in ``SMPU_RADDR[n]`` and ``SMPU_RCTL[n]``.

Second, we need to configure the protection itself. After deciding whether we allow
read/write or both, we may set ``RPROTEN`` and ``WPROTEN``.

After that we need to specify which IDs we are going to allow. For this, we need to
understand how ID specification works. By using ``RIDA0`` / ``RIDB0`` and ``RIDMSKA0`` /
``RIDMSKB0``, we can set which bus requester IDs can bypass the protection.

As we can understand from register names, SMPU uses two "protection units" (A and B) for
ID matching. Each unit performs a masked comparison with the incoming transaction ID. The
operation is basically having a logical AND operation with IDs and masks. There is also a
register to invert the result of this match, allowing us to decide which IDs are NOT allowed.

Bus Requester IDs
-----------------

As described above, each bus requester has a unique ID that the SMPU uses to control access.

**Example SC59x Bus Requester IDs (partial list)**

The table below is a partial SC59x example; it does not list every bus requester
(for example, the Arm cores are omitted). See the applicable
:adi:`SC592/SC594 Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/adsp-2159x-sc591-592-594-hrm.pdf>`
or :adi:`SC595/SC596/SC598 Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/adsp-sc595-sc596-sc598-hrm.pdf>`
for the complete table.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Master
     - ID (binary)
     - Description
   * - SHARC+ 0 Data Port
     - ``0xxxx00001001``
     - Core 0 data accesses
   * - SHARC+ 0 Instruction
     - ``0000001000111``
     - Core 0 instruction fetches
   * - SHARC+ 1 Data Port
     - ``0xxxx00011001``
     - Core 1 data accesses
   * - SHARC+ 1 Instruction
     - ``0000001010111``
     - Core 1 instruction fetches

Note: ``x`` means the bit can be 0 or 1 (use mask to match groups)

For SC57x and SC58x, see the System Controller IDs table in the respective
:adi:`SC57x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/adsp-sc57x-2157x_hwr.pdf>` and
:adi:`SC58x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf>`.

Memory Region Sizes
----------------------

SMPU allows us to set region size between 4KB and 4GB. Each size has an address alignment requirement.
If the address is not properly aligned, the SMPU will mask the lower bits. It may end up with
potentially protecting a different region than intended. Some of the valid region sizes and their
alignment requirements can be seen below.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Size
     - SIZE Value
     - Address Alignment
   * - 4 KB
     - 0
     - Multiple of 4 KB (``0xXXXXX000``)
   * - 8 KB
     - 1
     - Specific values only (``0``, ``0x2000``, ``0x4000``, etc.)
   * - 1 MB
     - 8
     - Multiple of 1 MB (``0xXXX00000``)
   * - 2 MB
     - 9
     - Specific values only
   * - 4 MB
     - 10
     - Multiple of 4 MB (``0xXXX00000``)
   * - 8 MB - 4 GB
     - 11-20
     - See Hardware Reference Manual for details.

Configuring Security
-----------------------

Global Security Settings
~~~~~~~~~~~~~~~~~~~~~~~~

Here, secure and non-secure refer to the corresponding Arm TrustZone transaction
states. We can control whether these transactions are allowed by writing to the
``SMPU_SECURECTL`` register. As default, only secure transactions are allowed. To
also support non-secure transactions, we can set ``WNSEN`` and ``RNSEN`` bits.

Per-Region Security
~~~~~~~~~~~~~~~~~~~~~~

We can also configure the security for individual regions by writing to
``SMPU_SECURERCTL[n]``. Each register covers one region (selected by ``n``) and
consists of 4 bits: read/write permission crossed with secure/non-secure access.

Read Speculation
-------------------

The SMPU can forward read requests to memory before checking permissions,
saving one clock cycle. However, this may cause side effects for memory-mapped
registers that change state when read (like FIFOs that auto-clear). This is controlled
by ``RSDIS`` bit in ``SMPU_CTL`` register. When protecting memory-mapped FIFOs or other
auto-clearing memory, always disable read speculation to prevent unintended side effects.

Error Handling
-----------------

Interrupts
~~~~~~~~~~~~~~~~~~~

We can configure the SMPU to generate interrupts. This is controlled by the ``PINTEN``
bit in the ``SMPU_CTL`` register. After setting this bit, we can examine the ``SMPU_IADDR``
and ``SMPU_IDTLS`` registers to see the details of the violation. Detailed instructions on
how we can handle interrupts can be examined in the processor's Hardware Reference Manual.

Bus Errors
~~~~~~~~~~

Bus errors are enabled as default. We can disable them by setting the ``PBEDIS`` bit in the
``SMPU_CTL`` register. When a transaction is blocked and bus error generation is enabled, the
SMPU returns an error to the requesting master. The master's bus fault handler will be called.
We can examine the ``SMPU_BADDR`` and ``SMPU_BDTLS`` registers to see the details of the
violation. Detailed instructions on how we can handle bus errors can be examined in the
processor's Hardware Reference Manual.

Locking Configuration
------------------------

SMPU allows us to protect the configurations we created by providing a lock mechanism. These lock
is simply the ``LOCK`` and/or ``RLOCK`` bits under ``SMPU_CTL`` register. If we lock the configs,
they are protected until SPU releases global lock.

Register Summary
-------------------

Key SMPU registers for each region n (0-7):

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Register
     - Purpose
   * - ``SMPU_CTL``
     - Control: Lock, interrupts, bus errors, read speculation
   * - ``SMPU_STAT``
     - Status: Interrupts, errors, overruns
   * - ``SMPU_RADDR[n]``
     - Region base address (bits 31:12)
   * - ``SMPU_RCTL[n]``
     - Region control: Size, enable, read/write protection, ID invert
   * - ``SMPU_RIDA[n]``
     - Region ID A for matching
   * - ``SMPU_RIDB[n]``
     - Region ID B for matching
   * - ``SMPU_RIDMSKA[n]``
     - Mask for ID A matching
   * - ``SMPU_RIDMSKB[n]``
     - Mask for ID B matching
   * - ``SMPU_SECURECTL``
     - Security control: Global secure/non-secure enable
   * - ``SMPU_SECURERCTL[n]``
     - Per-region security configuration
   * - ``SMPU_IADDR``
     - Address that caused last interrupt
   * - ``SMPU_IDTLS``
     - Interrupt details: ID, read/write, secure
   * - ``SMPU_BADDR``
     - Address that caused last bus error
   * - ``SMPU_BDTLS``
     - Bus error details: ID, read/write, secure

Important Notes
------------------

- An overly permissive mask might allow more IDs than intended. Always verify
  your mask matches only the intended IDs.

- After reset, only secure transactions are allowed. If you're running non-secure
  code, you must enable non-secure transactions or you'll be blocked.

- Don't enable protection on memory regions that are actively being used by
  code or data. You'll immediately get violations.

- The SMPU will mask misaligned addresses. Always verify alignment to prevent
  protecting the wrong memory range.

Current Linux Support Status
--------------------------------

SMPU Linux support is currently under development
(`PR #3339 <https://github.com/analogdevicesinc/linux/pull/3339>`_).

The ADI DSP Linux kernel and accompanying examples are designed with the intent
that the ARM core owns and allocates most of the system's peripherals.
The accompanying SHARC examples leverage peripherals minimally to prevent
contention with the ARM for system resources.

Loading a SHARC application before Linux boots on the ARM cores is not
supported, due to contention with Linux for system resources (peripherals,
interrupts, DMA, shared L2 memory, etc.). Linux/ARM owns the SMPU
configuration and all system resources allocated in the devicetree.

See Also
------------

- :doc:`spu` for peripheral protection
- :doc:`system-protection` for overview of protection features
- Hardware Reference Manuals for
  :adi:`SC57x <media/en/dsp-documentation/processor-manuals/adsp-sc57x-2157x_hwr.pdf>`,
  :adi:`SC58x <media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf>`,
  :adi:`SC592/SC594 <media/en/dsp-documentation/processor-manuals/adsp-2159x-sc591-592-594-hrm.pdf>`,
  and :adi:`SC595/SC596/SC598 <media/en/dsp-documentation/processor-manuals/adsp-sc595-sc596-sc598-hrm.pdf>`
- Silicon Anomaly 20000003 in the applicable anomaly list for
  :adi:`SC57x <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-sc570_571_572_573_adsp-21571_573-silicon-anomaly-list.pdf>`,
  :adi:`SC58x <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-2158x_adsp-sc58x-sharc-anomaly.pdf>`,
  :adi:`SC591/SC592/SC594 <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-21591_21593_21594_adsp-sc591_sc592_sc594-anomaly.pdf>`,
  and :adi:`SC595/SC596/SC598 <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-sc595-sc596-sc598-anomaly.pdf>`

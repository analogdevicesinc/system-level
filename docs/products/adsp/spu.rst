.. _adsp-spu:

System Protection Unit (SPU)
============================

The System Protection Unit (SPU) protects peripheral configuration registers from
unintended writes. In systems with multiple processors and DMA controllers, the SPU
acts like a security guard, controlling who can modify critical peripheral settings.

.. note::
   This guide applies to all ADSP-SC5xx processors. While the SPU
   functionality is consistent across processor families, the specific details vary:

   - Number of protected peripherals
   - Specific register mappings

What Does the SPU Do?
------------------------

Think of the SPU as a gatekeeper for peripheral registers. It sits between the
system bus and peripheral configuration registers, checking every write request.
If a write comes from an unauthorized source, the SPU blocks it.

Key Features
---------------

Write Protection per Peripheral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each peripheral has a dedicated protection register ``SPU_WP[n]`` that controls
which bus requesters can write to its registers. We can:

- Allow or block specific processor cores
- Allow or block DMA controllers
- Configure different permissions for each peripheral

Global Locking
~~~~~~~~~~~~~~

The SPU can issue a system-wide lock signal that all peripherals recognize. When
enabled, any peripheral with its lock bit set will reject all write attempts to
its control register.

Security Integration
~~~~~~~~~~~~~~~~~~~~

The SPU integrates with ARM TrustZone to enforce security boundaries:

- Secure peripherals only accept secure transactions
- Non-secure masters cannot access secure peripherals
- Each peripheral's security level is configurable

Self-Protection
~~~~~~~~~~~~~~~

The SPU can protect its own configuration registers, preventing unauthorized changes
to the protection settings. Once locked, only a system reset can restore access.

How It Works
---------------

The SPU examines every write transaction in this order:

1. Destination Check - Which peripheral is being accessed?
2. Source Check - Which bus requester is requesting the write?
3. Permission Check - Is this master allowed to write to this peripheral?
4. Decide - Pass the write through, or return a bus error

Basically, SPU sits between the system crossbar and peripheral registers.

Basic Configuration
----------------------

Protecting a Peripheral
~~~~~~~~~~~~~~~~~~~~~~~~~

To protect a peripheral from writes by specific bus requesters, we need to configure several registers.

First, we should find the peripheral's write-protect register number in the Hardware Reference Manual.

Second, we can set the corresponding bits in ``SPU_WP[n]`` for bus requesters we want to block. It consists of
two types of bits, named ``CM[n]`` and ``SM[n]`` for Core Requesters and System Requesters. They keep the
information of who is going to be blocked.

- Bits [2:0] = ``CM[n]`` - Block writes from processor cores
- Bits [18:16] = ``SM[n]`` - Block writes from system requesters (DMA, etc.)

The bit positions (CM, SM) are similar across all families, but the peripheral-to-WP register
mappings differ more.

Using Global Lock
~~~~~~~~~~~~~~~~~~~

Global lock provides a quick way to simultaneously protect control registers
across multiple peripherals. This mechanism is controlled by registers both in SPU and others.
For example CDU_CTL register has LOCK bit to enable it. When we activate the global lock over
SPU_CTL by setting GLCK bit, the registers with lock bit enabled are going to be blocked from write access.

Configuring Security
~~~~~~~~~~~~~~~~~~~~~

TrustZone security features apply to all SC5xx processors with ARM Cortex cores.
The SPU security register numbers match the WP numbers. This is controlled over
SSEC and MSEC bits under ``SPU_SECUREP[n]`` registers for peripherals. For cores, there is
``SPU_SECUREC[n]`` register with ``CSEC[n]`` bits. For peripherals, each ``SPU_SECUREP``
register is assigned to a specific MMR address range associated with one peripheral. Each has
a Slave Secure (SSEC) bit and a Master Secure (MSEC) bit. When the Slave Secure (SSEC) bit is
set, the SPU will only allow Secure Masters generating secure transactions to access the
peripheral's MMR address space. When the Master Secure (MSEC) bit is set, the associated
peripheral will be secure and will generate secure transactions.

Checking Security Status
~~~~~~~~~~~~~~~~~~~~~~~~~

Software can check if it's running in secure or non-secure mode by examining the value of
``SPU_SECURECHK`` register. The ``SPU_SECURECHK`` register reads by secure requesters return
``0xFFFFFFFF``. Reads by non-secure requesters return ``0x00000000``.

Locking the SPU
~~~~~~~~~~~~~~~~

To prevent any changes to SPU configuration until the next reset, we can even lock the SPU itself.
For this, we can set WPLCK and GLCK and also block all masters to SPUs own write-protect registers.
We need to be careful since this lock can only be unlocked with a reset.

Error Handling
-----------------

Interrupts
~~~~~~~~~~~~~~~~~~~

The SPU can generate interrupts when a write is blocked.

We can configure the SPU to generate interrupts. This is controlled by the ``PINTEN``
bit in the ``SPU_CTL`` register. After setting this bit, we can examine the ``SPU_STAT``
register to see the details of the violation. Detailed instructions on how we can handle
interrupts can be examined in the processor's Hardware Reference Manual.

Bus Errors
~~~~~~~~~~~
When a transaction is blocked, the SPU returns a bus error to the requesting master.
The master's bus fault handler will be called. We can examine the ``SPU_STAT`` register to see the
details of the violation. Specifically, the LWERR, ADDRERR or VIRQ bits can be used to see
the details of the error. Detailed instructions on how we can handle bus errors can be examined
in the processor's Hardware Reference Manual.

Peripherals with Global Lock Support
---------------------------------------

The following peripherals support the global lock feature (they have a lock
enable bit in their control register) for SC59x.

- General-Purpose IO
- System Event Controller
- Trigger Routing Unit
- Clock Generation Unit
- Clock Distribution Unit
- Dynamic Power Management
- Reset Control Unit
- System Protection Unit
- L2 Memory Controller

For SC57x and SC58x, see the list of peripherals that support global lock in the
respective :adi:`SC57x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/adsp-sc57x-2157x_hwr.pdf>` and
:adi:`SC58x Hardware Reference Manual
<media/en/dsp-documentation/processor-manuals/sc58x-2158x-hrm.pdf>`.

Register Summary
-------------------

Key SPU registers:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Register
     - Purpose
   * - ``SPU_CTL``
     - Control: Global lock, write-protect lock, interrupt enable
   * - ``SPU_STAT``
     - Status: Lock write errors, interrupts
   * - ``SPU_WP[n]``
     - Write-protect register for each peripheral (n = 0-202)
   * - ``SPU_SECURECTL``
     - Security control: Lock secure config, interrupt enable
   * - ``SPU_SECUREC[n]``
     - Core security configuration
   * - ``SPU_SECUREP[n]``
     - Peripheral security configuration (n = 0-213)
   * - ``SPU_SECURECHK``
     - Check if running in secure or non-secure mode

Important Notes
-----------------

- Don't lock peripherals before completing all initialization. You might lock
  yourself out and need a hard reset.

- If you lock the SPU's control register but forget to protect the SPU's own
  WP register (WP121), someone can still modify the protection settings.

- Global lock only works if the peripheral has its lock enable bit set in its
  control register. Don't forget that step.

- After system initialization, lock down clock, power, and boot configuration
  to prevent accidental changes.

Current Linux Support Status
------------------------------

SPU driver support is currently being tracked in the ADI Linux kernel repository
(:git-linux:`Implement system partitioning in ADSP SoCs <issues/3133+>`).

The ADI DSP Linux kernel and accompanying examples are designed with the intent
that the ARM core owns and allocates most of the system's peripherals.
The accompanying SHARC examples leverage peripherals minimally to prevent
contention with the ARM for system resources.

Loading a SHARC application before Linux boots on the ARM cores is not
supported, due to contention with Linux for system resources (peripherals,
interrupts, DMA, shared L2 memory, etc.). Linux/ARM owns the SPU
configuration and all system resources allocated in the devicetree.

See Also
----------

- :doc:`smpu` for memory protection
- :doc:`system-protection` for overview of protection features
- Hardware Reference Manuals for
  :adi:`SC57x <media/en/dsp-documentation/processor-manuals/adsp-sc57x-2157x_hwr.pdf>`,
  :adi:`SC58x <media/en/dsp-documentation/processor-manuals/sc58x-2158x-hrm.pdf>`,
  :adi:`SC592/SC594 <media/en/dsp-documentation/processor-manuals/adsp-2159x-sc591-592-594-hrm.pdf>`,
  and :adi:`SC595/SC596/SC598 <media/en/dsp-documentation/processor-manuals/adsp-sc595-sc596-sc598-hrm.pdf>`
- Silicon Anomaly 20000003 in the applicable anomaly list for
  :adi:`SC57x <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-sc570_571_572_573_adsp-21571_573-silicon-anomaly-list.pdf>`,
  :adi:`SC58x <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-2158x_adsp-sc58x-sharc-anomaly.pdf>`,
  :adi:`SC591/SC592/SC594 <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-21591_21593_21594_adsp-sc591_sc592_sc594-anomaly.pdf>`,
  and :adi:`SC595/SC596/SC598 <media/en/dsp-documentation/integrated-circuit-anomalies/adsp-sc595-sc596-sc598-anomaly.pdf>`

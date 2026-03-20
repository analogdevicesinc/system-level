AD-FMCMOTCON2-EBZ Signal Measurement Chain
==========================================

The motor control system allows the measurement of the Ia(phase A current),
Ib(phase B current) and Vbus using signal chains which involve components from
both the controller and low voltage driver boards. The entire analog frontend is
placed on the drive board and only digital signals are exchanged between the
controller and drive boards.

Ia, Ib Measurement Signal Chain
-------------------------------

The Ia and Ib currents are sensed using 10mΩ shunt resistors. The ADC is placed in the proximity of the shunt resistor to reduce noise coupling. The small differential voltage on the shunt resistor is measured directly with the :adi:`AD7403` isolated ΣΔ modulator without the need of extra interfacing and signal conditioning circuitry. The digital data and clock signals of the ADC travel the entire length of the drive and controller boards all the way to the FPGA. Since the analog signals were digitized close to the source and sent in a digital format to the FPGA there are no concerns related to the quality of the measurements. The Ia and Ib XADC measurement chain utilizes the entire path of the regular measurement chain and adds on the controller board after the :adi:`AD7403` isolated ΣΔ modulator a Sallen Key analog reconstruction filter implemented using :adi:`AD8646` operational amplifiers. The combination between the isolated ΣΔ modulator and the analog reconstruction filter provides a convenient and cheap way to achieve analog isolation of the XADC input signals. This analog isolation technique is described in this `paper <http://www.analog.com/media/en/reference-design-documentation/reference-designs/CN0185.pdf>`_.

The equation for calculating Ia or Ib is: :math:`I = (ADCvalue - 2^{ADCbits-1}) \times ADCrange / 2^{ADCbits-1} \times R_{shunt}` where :math:`R_{shunt} = 10e{-3}\,\Omega,\; ADCrange = 320e{-3}\,V,\; ADCbits = 16`

.. image:: ../images/current_chain.png
   :width: 800

Vbus Measurement Signal Chain
-----------------------------

Vbus sensing is done on the drive board using a resistive divider and the :adi:`AD7403` ΣΔ modulator. The Vbus XADC measurement chain utilizes the entire path of the regular measurement chain and adds on the controller board after the :adi:`AD7403` isolated ΣΔ modulator a Sallen Key analog reconstruction filter implemented using :adi:`AD8646` operational amplifiers. The combination between the isolated ΣΔ modulator and the analog reconstruction filter provides a convenient and cheap way to achieve analog isolation of the XADC input signals. This analog isolation technique is described in this `paper <http://www.analog.com/media/en/reference-design-documentation/reference-designs/CN0185.pdf>`_.

The equation for calculating Vbus is: :math:`V = (ADCvalue-2^{ADCbits-1}) \times ADCrange / 2^{ADCbits-1} \times gain` where :math:`ADCrange = 320e{-3}\,V,\; ADCbits = 16,\; gain = \frac{1}{220.1}`

.. image:: ../images/vbus_chain.png
   :width: 800

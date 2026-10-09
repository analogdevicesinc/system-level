.. _matlab bsp-extend:

Extending Device Interfaces
===========================

By default, only a small number of settings are available as direct attributes
for many of the devices like the transceiver. This is primarily done to not
burden the user with too many knobs which they do not care about since a device
the transceiver can have over 100 addressable attributes. However, sometimes you
want to get access to more IIO attributes available in the driver.

The MATLAB and Simulink interfaces can be extended in two ways.

Directly Addressing Attributes
------------------------------

Directly address properties through the underlying libIIO API calls. By
default the AD9361 receiver interfaces only provide or control the following
properties:

::

   rx =

     adi.AD9361.Rx with properties:

                CenterFrequency: 2.4000e+09
                   SamplingRate: 3000000
                    RFBandwidth: 3000000
        GainControlModeChannel0: 'slow_attack'
       EnableQuadratureTracking: true
             EnableRFDCTracking: true
       EnableBasebandDCTracking: true
                SamplesPerFrame: 32768
                   channelCount: 2
             EnableCustomFilter: false
                            uri: 'ip:192.168.2.1'

This does not provide status attributes or other more obscure control
attributes. For example, the RSSI measurement is not provided as part of the
AD9361 transceiver interfaces. To read this attribute directly we could do the
following with the
:git-MathWorks_tools:`common abstractions from here <%2Badi/%2Bcommon/Attribute.m#L25>`__:

::

   rx = adi.AD9361.Rx('uri','ip:192.168.2.1');
   rssiValue = rx.getAttributeLongLong('voltage0','rssi',false);

Adding MATLAB Properties For Attributes
---------------------------------------

If additional APIs are needed for a device, and that code will be used by
others, then it is recommended to add an actual property to the class. This can
provide additional documentation as well as range checking. Below the
:git-MathWorks_tools:`Rx <%2Badi/%2BAD9361/Rx.m>`__
class is modified to allow to selection of the RF port attribute of the
transceiver. This is done by inserting the following:

::

       properties
           %RFPort RF Port
           %   specified as one of the following:
           %   'A_BALANCED' - Select A Balanced RF input
           %   'B_BALANCED' - Select B Balanced RF input
           %   'TX_MONITOR1' - Select TX Monitor 1 RF input
           %   'TX_MONITOR2' - Select TX Monitor 2 RF input
           RFPort = 'A_BALANCED';
       end

Now under the standard methods scope the following set method is added

::

           % Check RFPort
           function set.RFPort (obj, value)
               obj.RFPort = value;
               if obj.ConnectedToDevice
                   id = 'voltage1';
                   obj.setAttributeRAW(id,'rf_port_select',value,false);
               end
           end

Now when the class is expanded the new property is populated:

::

   rx =

     adi.AD9361.Rx with properties:

                CenterFrequency: 2.4000e+09
                   SamplingRate: 3000000
                    RFBandwidth: 3000000
                         RFPort: 'A_BALANCED'
        GainControlModeChannel0: 'slow_attack'
       EnableQuadratureTracking: true
             EnableRFDCTracking: true
       EnableBasebandDCTracking: true
                SamplesPerFrame: 32768
                   channelCount: 2
             EnableCustomFilter: false
                            uri: 'ip:192.168.2.1'

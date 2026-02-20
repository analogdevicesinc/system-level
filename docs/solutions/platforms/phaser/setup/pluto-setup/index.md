# Updating Pluto for Phaser

The Pluto that ships with the Phaser kit has been pre-configured and should not need to be modified.  However, in case something goes wrong or the firmware needs to be updated, this page details the Pluto setup procedures. 

## Updating Pluto Firmware
The latest Pluto firmware is found here:

[https://github.com/analogdevicesinc/plutosdr-fw/releases](https://github.com/analogdevicesinc/plutosdr-fw/releases)

It is recommended that all Phaser's operate with version 0.39, or later.  Details on how to perform the firmware update are found here:

{ref}`pluto-m2k firmware`


## Pluto Configuration

The next step is to update the Pluto configuration to enable the AD9361's second channel. Follow the directions at: [Updating to the AD9364](https://wiki.analog.com/university/tools/pluto/users/customizing#updating_to_the_ad9364)

For setting the mode of a Rev. C PlutoSDR to 2r2t, login to Pluto (via PuTTY) and enter the following sequence of commands:

```{code-block} bash
fw_setenv attr_name compatible
fw_setenv attr_val ad9361
fw_setenv compatible ad9361
fw_setenv mode 2r2t
reboot
```


Next, verify that the configuration was programmed properly by entering the following commands:
```{code-block} bash
fw_printenv attr_name
fw_printenv attr_val
fw_printenv compatible
fw_printenv mode
```

Which should return:
```{code-block} bash
# fw_printenv attr_name
attr_name=compatible
# fw_printenv attr_val
attr_val=ad9361
# fw_printenv compatible
compatible=ad9361
# fw_printenv mode
mode=2r2t
#
```


```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```


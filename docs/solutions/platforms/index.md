(adc-platforms)=

# Aerospace, Defense and Communication Platforms

## Complete Evaluation & Demonstration Systems for ADI Data Converters

The **ADC System Platforms** team develops and supports fully integrated
evaluation and demonstration systems built around ADI data-converter
technologies.

Each platform delivers a validated system stack --- from RF hardware to
application software --- enabling rapid performance evaluation and
real-world system development.


## What Makes a Platform?

`````{grid}
:columns: 4

````{card} Signal-Chain Hardware

ADI MxFE, SDR, MEMS and power solutions integrated into validated system architectures.

```{image} resources/signal-chain-hardware.png
```
````

````{card} FPGA + Reference HDL

COTS FPGA platforms with production-grade HDL reference designs.

```{image} resources/fpga-reference-hdl.png
```
````

````{card} Linux + IIO

Embedded Linux builds with native [IIO](https://www.kernel.org/doc/html/latest/driver-api/iio/index.html) support.

```{image} resources/linux-iio.png
```
````

````{card} Application Software

System-level control via Python, MATLAB, or QIQ using libIIO APIs.

```{image} resources/application-software.png
```
````
`````

## Platforms

For more information on each of ADC Platforms, please click on the links below:


`````{grid}
:columns: 2

````{card} Phaser (CN0566)
:ref: adc adalm-phaser

X-Band Beamforming and Radar Learning Platform

```{image} resources/phaser_pict.svg
```
````

````{card} Pluto SDR
:ref: adc pluto

Low-cost SDR system based on the AD9361

```{image} resources/pluto.png
```
````

````{card} Triton
:ref: adc triton

16T/16R X-Band System Platform

```{image} triton/images/adxband16ebz-top-angle-evaluation-board.png
```
````

````{card} Jupiter SDR
:ref: adc jupiter

Ruggedized, high-performance SDR platform

```{image} jupiter/ad-jupiter-ebz-angle-web.jpg
```
````

`````  

## Platform Pilots

```{image} resources/pilot_ships.svg
:width: 400px
:align: right
```

Each platform includes at least one **Pilot** --- a fully documented system-level example of a representative use case--complete with all the key elements to implement that use case.   

**Pilots are more than just a demo!**  A Pilot provides:

-   Hardware + software setup
-   Stable drivers, APIs, and plug-ins
-   Example scripts in Python, MATLAB, or QIQ Systems
-   Documented workflows (setup → configure → run → analyze → modify)
-   A foundation for customer algorithm development

Pilots range from basic *"boot and capture"* examples to advanced
demonstrations including:

-   RF beamforming
-   FMCW radar operation
-   Wideband streaming
-   JESD bring-up validation 


## ADC Catalyst

ADI operates dedicated **ADC Catalyst Centers** where customers can
experience platforms and pilots live, receive training, and collaborate
directly with ADI engineers.

```{image} resources/rtp_nc_adaptive.jpeg
:width: 400px
:align: right
```

We have a Catalyst centres in:  
- North Carolina (USA): Contact [Ian Beavers](mailto:Ian.Beavers@analog.com)
- Limerick (Ireland): Contact [Simon Walkin](mailto:Simon.Walkin@analog.com)

### Catalyst Mission​


1.  **Elevate System-Level Expertise**\
    Enable customers to solve real-world system integration challenges.

2.  **Empower Customer Learning**\
    Provide hands-on access to ADI hardware, tools, and training.

3.  **Drive Collaborative Innovation**\
    Co-develop system-level solutions with customers and ADI design
    teams.

```{toctree}
:maxdepth: 1
:hidden:

Phaser (CN0566)<phaser/index>
Triton <triton/index>
Jupiter SDR <jupiter/index>
Pluto SDR<pluto/index>
```



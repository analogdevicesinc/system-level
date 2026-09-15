.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters

.. _ad-fmcomms2-ebz software filters:

MATLAB Filter Design Wizard for AD9361
======================================

The AD9361 Filter Design Wizard is a small :mw:`MATLAB <products/matlab/>` App,
which can be used to design transmitter and receiver FIR filters, which take
into account the magnitude and phase response from other analog and digital
stages in the filter chain. This tool provides not only a general purpose low
pass filter designer, but also magnitude and phase equalization for other stages
in the signal path.

With this wizard, users can perform the following tasks:

- Choose correct digital filters to use for receive and transmit.
- Design the programmable FIR filters, get the filter coefficients and save them
  in a .ftr file, which can be directly loaded into the hardware.
- Examine the independent response of each filter, and the composite response of
  all the filters, including both digital and analog filters.

For information about the transmit and receive paths consult
:dokuwiki:`AD9361, AD9363, AD9364 transceiver outline </resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`.
This also includes information on alternative solutions for programming the
transceiver"s filters.

Videos
------

Here is a brief introduction on why everyone needs to, and how to use this tool.

.. todo:: .. figure: ahttps://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/nalogTV>3845680080001

.. todo:: .. include: /resources/eval/user-guides/ad-fmcomms2-ebz/downloads.rst

   :start-after: .. start-download-filters
   :end-before: .. end-download-filters

Use MATLAB App
--------------

Generally speaking, there are two ways you can use the design wizard:

#. MATLAB App: A graphical user interface is created to facilitate the process
   of filter design. Users can easily define the input, observe the design
   performance, and specify the way they want to save the results. This is a
   more straightforward method to use the wizard.
#. MATLAB function: The link to design functions can be found in the Download
   section. They are MATLAB functions, which users can launch from the MATLAB
   command window by properly defining the input parameters. Using this way,
   users have more control of the internal design process.

In this section, we are going to elaborate on the first option - MATLAB App.

Basic Functions
~~~~~~~~~~~~~~~

After you launch the MATLAB App, there shows a drop-down list in ``Device
Settings``, which includes the default parameter profiles for several widely
used LTE applications. You can move the highlight bar to the one you would like
to start with.

This table is stored in
:git-ad936x-filter-wizard:`github <ad9361_settings.mat+>`.

.. note::

   .. list-table::
      :header-rows: 1

      * - LTE Specification
        -
        -
      * - LTE Bandwidth Set  [1]_
        - Occupied RF Bandwidth
        - Sample Rate
      * - MHz
        - MHz
        - MSPS
      * - 1.4
        - 1.08
        - 1.92
      * - 3
        - 2.7
        - 3.84
      * - 5
        - 4.5
        - 7.68
      * - 10
        - 9
        - 15.36
      * - 15
        - 13.5
        - 23.04
      * - 20
        - 18
        - 30.72

.. note::

   .. list-table::
      :header-rows: 1

      * - AD9361 settings
        -
        -
        -
        -
        -
        -
      * - Sample Rate
        - F\ :sub:`PASS`
        - F\ :sub:`STOP`
        - A\ :sub:`PASS`
        - A\ :sub:`STOP`
        - max Tx input
        - Tx input backoff
      * - MSPS
        - MHz
        - MHz
        - dB
        - dB
        - dB
        - dB
      * - 1.92
        - 0.54
        - 0.66
        - 0.1
        - 80
        -
        -
      * - 3.84
        - 1.35
        - 1.65
        - 0.1
        - 80
        -
        -
      * - 7.68
        - 2.25
        - 2.75
        - 0.1
        - 80
        - 0.93667
        - -0.56830
      * - 15.36
        - 4.5
        - 5.5
        - 0.1
        - 80
        - 0.93665
        - -0.56850
      * - 23.04
        - 6.75
        - 8.25
        - 0.1
        - 80
        - 0.93813
        - -0.55478
      * - 30.72
        - 9
        - 11
        - 0.1
        - 80
        - 0.93813
        - -0.55478

The LTE Release-8 physical layer specification actually supports 105 different
bandwidth options (not just the 6 shown above). Occupied RF Bandwidth from
between 1.08MHz to 19.8MHz with 180kHz steps complies with the spec, and while
these filters can be designed (manually) they are not included as defaults.

In addition, you can also save your favorite parameter settings in this list,
such as ``foobar (Rx & Tx)`` shown in the figure.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/1start.png
   :width: 600px

Assume that you choose the ``LTE10 (Rx & Tx)`` profile, after you click it, all
the parameters are filled in automatically for you, as shown in the figure
below. There are three categories of input parameters: magnitude specifications,
frequency specifications, and AD936x clock settings. If you are satisfied with
all the parameters, you can go ahead and click ``Design Filter`` to start the
design.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/2basic.png
   :width: 600px

As soon as the design process completes, you will see a magnitude plot displayed
on the top half of the GUI, where the specified Fpass, Fstop, Apass and Astop
are highlighted in the plot. The x-axis is from 0 to half of the data rate.
Below it, on the right, you will see a ``Filter Results`` portion, where the
actual Apass, Astop, the number of FIR taps and the pass band group delay
variance are shown. From these numbers, you will get an idea whether the design
meets the requirements quantitatively.

If you are interested in more details of the design performance, you can click
the :mw:``FVTool`` buttons left to ``Filter Results`` to launch the
`Filter Visualization Tool (fvtool) </help/signal/ref/fvtool.html>` provided by
The MathWorks. For your convenience, we provide this tool on two different
frequency scales. One is from 0 Hz to half of the data rate, the other is from 0
Hz up to half of the converter rate.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/3basicdesign.png
   :width: 600px

If you are mainly interested in pass band, click the top button, it will open
the following three figures:

- Magnitude response of half band filters and HB + designed FIR filter.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/fvtooldatarate.png
   :width: 600px

- Magnitude Response of the designed FIR only. Besides the magnitude response,
  you can use the toolbar on the upper left corner (as highlighted in square) to
  navigate to the other responses, including phase response, group delay
  response, impulse response, poles/zeros and etc. It will enable you to have a
  better understanding of the designed FIR.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/6fironly.png
   :width: 600px

- Overall group delay on pass band. For your convenience, the group delay
  variance has been calculated and indicated on the figure.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/5fvt2.png
   :width: 600px

If you are interested in the whole frequency band, click the bottom button, it
will open the following figure:

- Magnitude response of half band filters and HB + designed FIR filter. You can
  easily have a closer observation on certain portion of the magnitude response
  by using the ``Zoom In/Out`` functions on the toolbar (as highlighted in
  square).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/4fvt1.png
   :width: 600px

.. note::

   For more information about the FVTool, please refer to:
   http://www.mathworks.com/help/signal/ref/fvtool.html

After the deeper analysis, if you are satisfied with the results and would like
to save the designed FIR filter, there are several options you can choose from.
These options are in the ``Controls`` portion on the upper left corner of the
GUI.

- Save object and data to workspace: If you will use the designed filter chain
  with some other MATLAB functions or Simulink models, you can simply leave it
  in the workspace by clicking ``Save to Workspace`` button, as shown in the
  figure below. After click this button and exit the App, you will find a
  mfilt.cascade object named ``AD9361_Tx_Filter_object`` or
  ``AD9361_Rx_Filter_object`` depending on whether it is on Tx or Rx.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/7save2ws.png
   :width: 600px

.. note::

   When you click ``Save to Workspace``, besides the filter object, there is
   also a data structure saved to workspace, which will initialize the SimRF
   model of FMCOMMS2. The data structure is named ``FMCOMMS2_TX_Model_init`` or
   ``FMCOMMS2_RX_Model_init``.

   For more information about the SimRF model of FMCOMMS2, please refer to:
   http://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html

- Save coefficients to a ftr file: If you will use the designed FIR filter with
  the IIO Oscilloscope application  [2]_, you can save the FIR coefficients by
  clicking ``Coefficients to ftr File`` button, as shown in the figure below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/fig7.png
   :width: 600px

.. note::

   You need to have designed both the Transmit and Receive filters before you
   can use the ``Coefficients to ftr File`` button. Otherwise, this button is
   grayed out.

After that, a window will pop up, asking you to specify the name and the
location of the ftr file, as shown in the figure below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/8savecoeff.png
   :width: 600px

If you plan to use the Filter Design Wizard with a zyqn-based platform, there
are several options available that will facilitate this process. These options
are in the ``Target (Zynq Board)`` portion of the GUI.

- Connect to the target: In the IP box, you should input the IP address of the
  target. In Linux system, it can be easily found by the ``ifconfig`` command.
  Then, click the ``Connect to Target`` button.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/13connecttozynq.png
   :width: 600px

- Read clock settings: If a target is detected at the specified IP address, the
  ``Read Clock Settings`` button will show up, as shown in the picture below. If
  you want to overwrite the current clock settings with the ones belong to the
  target, you can click this button.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/14readclock.png
   :width: 600px

- Save FIR coefficients to the target: If an FIR filter is designed for the
  target, the FIR coefficients can be saved directly to the target by clicking
  the ``Coefficients to Target`` button, as shown in the picture below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/15tozynq.png
   :width: 600px

Advanced Functions
~~~~~~~~~~~~~~~~~~

The functions introduced so far provide a basic infrastructure to design and
observe the FIR filter. If you would like to have more control and
functionality, you can turn on the ``Advanced`` option, as shown in the figure
below, which provides you with several more advanced options.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/9advanced.png
   :width: 600px

*Phase Equalization: If you would like to have the FIR filter do phase
equalization, you can turn on the "Phase Equalization" option, as shown in the
figure below. The main purpose of the phase equalization is to reduce the pass
band group delay*variance* brought by analog filters, digital filters and FIR
filter, so that for signals at different frequencies, they will be delayed by
an almost identical amount when going through the filter chain.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/10targetdelay.png
   :width: 600px

After you click ``Design Filter``, the phase equalization part of the FIR design
file is executed, and you will get an updated FIR filter design. Comparing the
group delay variance in the Results portion, it is decreased from 16.6 ns to
1.52 ns with phase equalization. Also note that when the design process
completes, there is an updated target delay number (this number is 0 before
phase equalization) shown in the ``Filter Options`` portion.

Please note the phase equalization process may take a few minutes, depending on
the performance of your PC, since it tries to find a best target delay which
yields the minimum group delay variance.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/10pheq.png
   :width: 600px

- Astop (FIR): This is a new parameter in magnitude specifications. It specifies
  the attenuation of FIR (not the composite response), which corresponds to the
  ``dBstop_FIR`` input in the design file. This parameter is not needed most of
  the time, so you can leave it as 0. However, if you do want to play around
  with it, you can enter a number there. For more information about
  ``dBstop_FIR``, please refer to ``Some Notes About dBstop_FIR`` at the end of
  this page.

- Fcutoff (Analog): This is a new parameter in frequency specifications. It
  specifies the cutoff frequency of the analog Butterworth filters. By default,
  this parameter is calculated for you by the App according to the Fpass and
  Fstop you entered, so you can leave it as it is. However, if you do want to
  play around with it, you can enter a number there.

- Use Internal FIR: Due to the constraint on power consumption, some users may
  not want to use the FIR filter on AD936x. Instead, they want to move the FIR
  filter implementation on FPGA or some other processors. The Filter Design
  Wizard can also accommodate this requirement. If you decide not to use the
  AD936x FIR, you can turn off the ``Use Internal FIR`` option, as shown in the
  figure below, and click ``Design Filter``. In this case, there is no longer
  any constraint on the number of the FIR taps, so the design file conducts a
  minimum order design. Comparing the FIR Taps in the Results portion, it is
  decreased from 128 to 105 if the AD936x FIR is not used.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/11usefir.png
   :width: 600px

- Generate HDL: Following the previous step, if you decide to have the FIR
  filter implemented on FPGA, the design wizard can help you generate the HDL
  code. By clicking ``Generate HDL``, the "fdhdltool" function
  (http://www.mathworks.com/help/hdlfilter/fdhdltool.html) is called and the
  Generate HDL dialog box will pop up, as shown in the figure below. There are
  quite a few options you can choose concerning how you would like the HDL to be
  generated. In the end, by clicking ``Generate``, the HDL will be generated for
  you.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/12createhdl.png
   :width: 600px

Toolbar
~~~~~~~

The icons shown on the toolbar below provide a shortcut to some frequently used
functions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/13toolbar.png
   :width: 600px

From left to right, the first four icons are related to filter parameter
settings:

- New Filter: It will open the drop-down list for you.
- Open Filter Design Parameters: It will open a saved parameter setting and load
  it for you.
- Save Parameters to File: It has the similar function as ``Coefficients to ftr
  File`` button.
- Save Parameters to Workspace: It has the similar function as ``Object to
  Workspace`` button.

The next four icons work on the magnitude response plot shown in the GUI:

- Zoom In: Click the area of the axes where you want to zoom in, or drag the
  cursor to draw a box around the area you want to zoom in on.
- Zoom Out: Click the area of the axes where you want to zoom out, or drag the
  cursor to draw a box around the area you want to zoom out on.
- Pan: Interactively pan the view of a plot.
- Data Cursor: Enable the interactive data cursor mode.

Use MATLAB Functions
--------------------

In addition to MATLAB App, users can also employ the MATLAB functions to
complete the filter design. What they need to do is to launch the MATLAB
functions from the MATLAB command window by properly defining the input
parameters in a MATLAB structure.

In MATLAB command window, the command is:

.. code:: matlab

   output = design_filter(input)

.. admonition:: Download

   In order to use this method, you need to download the whole
   ad936x-filter-wizard repository from GitHub. The following are the two most
   important functions for this method:

   - Main function: :git-ad936x-filter-wizard:`design_filter.m`
   - Design file: :git-ad936x-filter-wizard:`internal_design_filter.m`

Please note this method is suitable for those users who have a clear idea about
the parameter settings. For those who are not sure about the parameters, the
MATLAB App is a better way to start with.

Inputs and Outputs
~~~~~~~~~~~~~~~~~~

According to the design requirements, the inputs and outputs of the MATLAB
function are as following:

Inputs
^^^^^^

Input structure containing the following fields:

#. Rdata = input/output sample data rate (in Hz)
#. FIR = FIR interpolation/decimation factor
#. PLL_mult = PLL multiplication
#. Fpass = passband frequency (in Hz)
#. Fstop = stopband frequency (in Hz)
#. Apass = max ripple allowed in passband (in dB)
#. Astop = min attenuation in stopband (in dB)
#. FIRdBmin = min rejection that FIR is required to have (in dB)
#. phEQ = Phase Equalization on (not -1)/off (-1)
#. int_FIR = Use AD9361 FIR on (1)/off (0)
#. wnom = analog cutoff frequency (in Hz)

Outputs
^^^^^^^

Output structure containing the following fields:

#. firtaps = fixed point FIR coefficients
#. filter = system object for visualization (does not include analog filters)
#. delay = actual delay used in phase equalization

Transmit
~~~~~~~~

According to AD9361 Filter Guide, the TX signal path is as following:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/txfilter.png

The digital and analog paths are separated by DAC. Before DAC, there are four
digital filters. The first one (PROG TX FIR) is a programmable poly-phase FIR
filter, which can interpolate by a factor of 1, 2, or 4, or it can be bypassed
if not needed. The others (HB1, HB2, HB3 and INT3) are all digital filters with
fixed coefficients, and they can be turned on or turned off. After DAC, there
are two low-pass analog filters.

Receive
~~~~~~~

According to AD9361 Filter Guide, the RX signal path is as following:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/rxfilter.png

The analog and digital paths are separated by ADC. Before ADC, there are two
low-pass analog filters. After ADC, there are three digital filters with fixed
coefficients (HB3/DEC3, HB2, HB1) followed by a programmable poly-phase FIR
filter (PROG RX FIR). The FIR filter can be decimated by a factor of 1, 2, or 4,
or it can be bypassed if not needed.

Example: Tx LTE-5
~~~~~~~~~~~~~~~~~

In this section, we present the results for LTE-5 transmit signal path by using
the MATLAB function. The input parameters are defined in ad9361_settings.mat
included in the repository.

Therefore, in MATLAB command window, the command is:

.. code:: matlab

   >> input = ad9361_settings.tx.LTE5;
   >> output = design_filter(input);

After this command is executed, in MATLAB, you will see the output structure
saved in workspace. We can now observe the independent filter, as well as the
composite response by specifying the stage of the object. For example,

.. code:: matlab

   TFIR = output.Hmd;
   Hm1 = output.Hm1;

If you are interested in the filter response of HB1, you can proceed to apply
the fvtool on HB1,

.. code:: matlab

   hfvt1 = fvtool(Hm1,...
       'FrequencyRange','Specify freq. vector', ...
       'FrequencyVector',linspace(0,122.88e6/2,2048),'Fs',122.88e6,...
       'ShowReference','off','Color','White');
   set(hfvt1, 'Color', [1 1 1]);
   set(hfvt1.CurrentAxes, 'YLim', [-100 1]);
   legend('HB1');

and you will get:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/HB1.png
   :width: 600px

Key Steps in Design
-------------------

In this section, we will talk about the key steps in AD9361 filter design.
Referring to this section, you will have a better understanding of the MATLAB
design files. Later on, if you would like to implement your own design
algorithm, you can edit the design files to incorporate your changes.

The AD9361 filter design file can be found here:

.. admonition:: Download

   - :git-ad936x-filter-wizard:`internal_design_filter.m`

Based on the structure of Tx and Rx filters, in the design process, we first
need to determine which half band digital filters should be included. We then
design the programmable FIR filter and get its coefficients. In the end, we
complete the design and return the whole filter chain in an object. Since both
Tx and Rx designs follow a similar workflow, the following steps take the Tx
side for example.

Define Filters
~~~~~~~~~~~~~~

Define Analog Filters
^^^^^^^^^^^^^^^^^^^^^

For the analog part, there is a third-order Butterworth low-pass filter and a
single-pole low-pass filter on the Tx side. Both of them can be easily defined
by the MATLAB function *butter*  [3]_ .

.. code:: matlab

   [b1,a1] = butter(3,2*pi*wc,'s');     % 3rd order
   [b2,a2] = butter(1,2*pi*wreal,'s');  % 1st order

Define Half Band Filters
''''''''''''''''''''''''

The digital filters with fixed coefficients can be easily defined by referring
to the AD9361 filter guide. Since they are interpolation filters on transmit
path, the coefficients declaration is followed by the mfilt.firinterp  [4]_
function.

Take HB1 for example, the full-scale range for this filter is 2^13, and it has
an interpolation factor of 2, so its coefficients are scaled by 2^(-14).

.. code:: matlab

   % Define the filters with fixed coefficients
   hb1 = 2^(-14)*[-53 0 313 0 -1155 0 4989 8192 4989 0 -1155 0 313 0 -53];
   Hm1 = mfilt.firinterp(2,hb1);

If your MATLAB license includes Fixed-Point Designer, the Hm1 object can be
further defined in a fixed point format, which is a better representation of the
real hardware:

.. code:: matlab

   set(Hm1,'arithmetic','fixed');
   Hm1.InputWordLength = 16;
   Hm1.InputFracLength = 14;
   Hm1.FilterInternals = 'SpecifyPrecision';
   Hm1.OutputWordLength = 16;
   Hm1.OutputFracLength = 14;
   Hm1.CoeffWordLength = 16;

Determine Half-band Filters
'''''''''''''''''''''''''''

Since there are 4 digital half-band filters on the TX signal path, there are a
finite number of interpolations they can provide. Therefore, the digital
half-band filters are picked up according to the overall interpolation factor
required by the user.

Design TFIR
'''''''''''

Ideally, when the whole filter chain is completed, it will have flat response of
magnitude 1 on passband, and magnitude 0 on stopband, call it
<m>Filter(\\omega)</m>. Since in the previous step, we have already picked up
the digital filters, we can get the filter response without TFIR, call it
<m>Filter1(\\omega)</m>. Therefore, the required response of TFIR is:

<m>TFIR(\\omega)={Filter(\\omega)}/{Filter1(\\omega)}</m>.

On passband, the required response *rg* and the weight *w* is:

.. code:: matlab

   rg1 = freqz(Filter1,omega,Fdac).*analogresp('Tx',omega,Fdac,b1,a1,b2,a2);
   rg2 = exp(-1i*2*pi*omega*delay);
   rg = rg2./rg1;
   w = abs(rg1)/(dBinv(dBripple/2)-1);

.. note::

   For the analog filters, unlike digital filter, there is no ``cascade``
   function to combine them and quickly calculate the composite response, so we
   made a helper function *analogresp* to calculate the overall response of the
   two analog filters and the converter. On the Tx side, the DAC is represented
   by a *sinc* function. While on the Rx side, the ADC is represented by a
   *sinc*\ ^3 function.

   :git-ad936x-filter-wizard:`analogresp.m`

On stopband, the required response *rg* = 0 and the weight *w* is:

.. code:: matlab

   wg1 = abs(freqz(Filter1,omega(Gpass+2:end),Fdac).*analogresp('Tx',omega(Gpass+2:end),Fdac,b1,a1,b2,a2));
   wg2 = (sqrt(FIR_interp)*wg1)/(dBinv(-dBstop));
   wg3 = dBinv(dBstop_FIR);
   wg = max(wg2,wg3);

One other constraint about TFIR is the number of filter taps. In the AD9361
Filter Guide, it says ``the number of taps is configurable between a minimum of
16 taps and a maximum of 128 taps in groups of 16``. Therefore, the following
piece of code calculates the tap number *N*:

.. code:: matlab

   % Determine the number of taps for TFIR
   switch tfirint
       case 1
           Nmax = 64;
       case 2
           Nmax = 128;
       case 4
           Nmax = 128;
   end

   N = min(16*floor((Fdac*DAC_mult)/(2*Fin)),Nmax);

Given the tap number *N*, the required response on passband and stopband (*A1*
and *A2*), as well as the corresponding weights (*W1* and *W2*), we can now use
fdesign.arbmag  [5]_ function to design the TFIR filter. In the following piece,
*B*\ =2, which means there are two bands in the design.

.. code:: matlab

   d = fdesign.arbmag('N,B,F,A',N-1,B,F1,A1,F2,A2);
   Hd = design(d,'equiripple','B1Weights',W1,'B2Weights',W2,'SystemObject',true);

The design of the TFIR is saved in the system object *Hmd*. In order to get the
16-bit filter coefficients, the following line is used:

.. code:: matlab

   tfirtaps = Hmd.Numerator.*(2^16);

Visualization
'''''''''''''

fvtool opens FVTool and displays the magnitude response of the digital filter
defined with the system object. Using FVTool you can display the phase response,
group delay, impulse response, step response, pole-zero plot, and coefficients
of the filter.

For example, the following piece of code use fvtool to display the TFIR filter
we just designed in the previous step. *Hmd* is the corresponding system object:

.. code:: matlab

   fvtool(...
       Hmd,...
       'FrequencyRange','Specify freq. vector', ...
       'FrequencyVector',linspace(0,clkTFIR/2,2048),'Fs',...
       clkTFIR, ...
       'ShowReference','off','Color','White','Legend','off');

Some Notes About dBstop_FIR
'''''''''''''''''''''''''''

The ``dBstop_FIR`` variable insures a ceiling where no matter how much rejection
comes from external filters, the FIR filter is required to have a minimum
rejection. To understand the reason for this, imagine that at some frequency we
need 60dB of rejection and we have an external filter that gives us 75dB of
rejection. If the FIR filter gave us 15dB of gain at that frequency, we would be
meet the frequency response. However having gain in a stop band would cause the
filter to resonate strongly at that frequency which would result in time domain
problems such as very large coefficients and over-ranging of signals at that
frequency. ``dBstop_FIR`` limits this concern.

Picking up a proper dBstop_FIR value is a very important step in designing the
filter. Since it determines the weight values on stopband, different dBstop_FIR
will result in very different filter responses. It is suggested to try different
dBstop_FIR values and observe the time-domain coefficients (it is desired to
have smooth coefficients) and frequency-domain responses (passband ripple &
stopband attenuation) until you pick up a the one which shows the best
combination of everything.

Generally speaking, dBstop_FIR plays a more important role in narrow bandwidth
filter design than in wide bandwidth filter design. It can even be omitted when
designing a filter with wide bandwidth.

C/C++ Source For Internal Designer
----------------------------------

For users wishing to deploy or embed this filter designer into their own C/C++
source two options are available. First a GPL licensed C version of the
``internal_filter_designer`` function is provided as part of the
`lib9361-iio <https://github.com/analogdevicesinc/libad9361-iio>`__ library.
This includes all the necessary source to generate filter coefficients.
Alternatively, if you do not want to utilize a GPL license with your eventual
code or product the MATLAB source, which has been enhanced for code generation,
can be found in the codegen-support branch of
`ad936x-filter-wizard <https://github.com/analogdevicesinc/ad936x-filter-wizard>`__.
A secondary designer function called ``internal_filter_designer_cg`` which
supports code generation is provided in this branch. This function will only
provide filter coefficients and will numerically match outputs of the
non-codegen designer except when the AD9361 FIR is turned off. However, this
mode is still supported and will generate filters with flat magnitude responses.

Getting MATLAB Source and Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Required MathWorks Toolboxes and Products:

- :mw:`MATLAB <products/matlab/>`
- :mw:`Signal Processing Toolbox <products/signal/>`
- :mw:`Fixed-Point Designer <products/fixed-point-designer/>`
- :mw:`MATLAB Coder <products/matlab-coder/>`

The MATLAB source with code generation support is provided in the
codegen-support branch of
`ad936x-filter-wizard <https://github.com/analogdevicesinc/ad936x-filter-wizard>`__,
which can be found here:

.. admonition:: Download

   :git-ad936x-filter-wizard:`archive/codegen-support.zip\+`

To make sure the code is functional and your local compilers are set up
correctly, automated testing has been added to this repository. To run these
tests first make sure you are in the root of the downloaded codegen-support
branch and run:

.. code:: matlab

   addpath(genpath('test'));
   runTests

If you have MATLAB configured correctly you should observe the following output
after the tests complete:

::

                       Name                          Passed    Failed    Incomplete    Duration    Details
    _____________________________________________    ______    ______    __________    ________    ____________

    'FilterDesignerTests/testRXMEX'                  true      false     false         160.63      [1x1 struct]
    'FilterDesignerTests/testRXEQMEX'                true      false     false         14.787      [1x1 struct]
    'FilterDesignerTests/testRXNonStandardFIRMEX'    true      false     false          18.38      [1x1 struct]
    'FilterDesignerTests/testRXDLL'                  true      false     false         15.854      [1x1 struct]
    'FilterDesignerTests/testRXNonStandardFIRDLL'    true      false     false         33.401      [1x1 struct]
    'FilterDesignerTests/testTXMEX'                  true      false     false         7.6336      [1x1 struct]
    'FilterDesignerTests/testTXEQMEX'                true      false     false         8.5157      [1x1 struct]
    'FilterDesignerTests/testTXNonStandardFIRMEX'    true      false     false          16.03      [1x1 struct]
    'FilterDesignerTests/testTXDLL'                  true      false     false         8.2624      [1x1 struct]
    'FilterDesignerTests/testTXNonStandardFIRDLL'    true      false     false         26.961      [1x1 struct]


These tests evaluate the numerical output of the generated designer with respect
to the original designer. Usage of these tests can be helpful if modification of
the MATLAB source is required. Note that it is possible to generate C/C++ source
without the necessary compilers, but the generate code cannot be tested with the
provided infrastructure.

Generating C/C++ Source Code From MATLAB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For convenience, an example script called :mw:``generate_internal_designer.m``
is provided in the repository to generate C/C++ source and optionally compile a
DLL. This script utilizes the ``coder.Config`` class to configure MATLAB Coder.
For additional configuration options not used in the script consult
`coder.CodeConfig <help/coder/ref/coder.codeconfig.html?searchHighlight=coder.codeconfig-class&s_tid=srchtitle>`.
MATLAB Coder can be used to generate source code only, compile the generate code
into a library, or compile external code with the newly generated code.

In the provided script, which we show a portion of here, a ``coder.config``
object is created and configured to generate C code with the majority of the
code output to a single file. We disable binary compilation and turn off OpenMP
calls which are enabled by default. Since MATLAB Coder requires knowledge of
input types they are provided as the ``args`` input to the codegen call.

.. code:: matlab

   cfg = coder.config('dll');
   cfg.TargetLang = 'C';
   cfg.FilePartitionMethod = 'SingleFile';
   cfg.GenCodeOnly = true;
   outputLIBName = 'libinternal_filter_designer';
   result = codegen('-config','cfg',functionName,'-O ','disable:openmp','-args', args,'-o',outputLIBName);

Once this script completes the generated code will be available in the directory
``codegen\dll\internal_filter_designer``. Example code is provided in the
``cpp`` folder of the root directory to demonstrate calls to the generated code.
Due to MATLAB Coder styling before directly using the desired function a call to
the initializer and terminator functions may be required as:

::

   // Initialize the application.
   internal_design_filter_cg_initialize();

   // Invoke the entry-point functions.
   main_internal_design_filter_cg();

   // Terminate the application.
   internal_design_filter_cg_terminate();

Support
-------

If you have any questions about these scripts/tools, please ask on the
EngineerZone.\
:ez:`Help & Support <community/linux-device-drivers/microcontroller-no-os-drivers>`.

.. [1]
   Release-8

.. [2]
   :dokuwiki:`IIO_Oscilloscope </resources/tools-software/linux-software/iio_oscilloscope>`

.. [3]
   :mw:`Butterworth filter design <help/signal/ref/butter.html>`

.. [4]
   :mw:`FIR filter-based interpolator <help/dsp/ref/mfilt.firinterp.html>`

.. [5]
   :mw:`Arbitrary response magnitude filter specification object <help/dsp/ref/fdesign.arbmag.html?searchHighlight=fdesign.arbmag&s_tid=srchtitle>`

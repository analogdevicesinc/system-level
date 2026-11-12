.. _m2k matlab:

Using with MATLAB
=================

The :adi:`ADALM2000` (M2K) can be controlled programmatically in a number of
languages, including MATLAB. Controlling M2K and access the data streams is
provided through a set of bindings for libm2k. If you are already familiar with
libm2k, moving into MATLAB is minimal work. If you are unfamiliar, there is
extensive `libm2k API documentation available <https://analogdevicesinc.github.io/libm2k/index.html>`__.

Quick Start
-----------

To get started with libm2k+MATLAB there are integrated installers available for
:mw:`Windows and Linux <matlabcentral/fileexchange/74385-libm2k-matlab>`.
Simply download the MLTBX file and open it within MATLAB. This will install the
necessary libraries and classes to interface with M2K. The installer packages
the dependent libraries libiio, libm2k, and the MATLAB bindings so they do not
need to be installed externally.
The only requirement is the
:ref:`M2K driver <pluto-m2k drivers windows>`.
For manual build see :ref:`m2k matlab build`.

After installation of the driver and the MLTBX file, you will have access to the
bindings through
:mw:`MATLAB's clib interface for C++ libraries <help/matlab/call-cpp-library-functions.html>`.
For libm2k this
will be in the form:

::

   clib.libm2k.libm2k.<M2K classes> 

.. important::

   Note that not every libm2k method is supported due to MATLAB
   limitations but these methods are usually uncommon.

This is a common API styling MATLAB uses for external languages or even internal
components that are Java-like or class-like. Below is a simple example of how to
call into the library and construct an M2K object, then call into the API from
that object.

.. code:: matlab

   %{
   This example reads the analog voltage from channel 0 of the analog input
   %}
   %% Setup
   m2k = clib.libm2k.libm2k.context.m2kOpen();

   %% Setup analog in
   ain = m2k.getAnalogIn();
   ain.enableChannel(0,true);
   voltage = ain.getVoltage(0);
   disp(voltage);

   %% Get more data
   d3 = ain.getSamplesInterleaved(1024);
   plot(d3)

   %% Cleanup
   clib.libm2k.libm2k.context.contextCloseAll();
   clear m2k

More examples are :git-libm2k-matlab:`available on GitHub <master:examples>`.

Inspecting the API
------------------

The MATLAB bindings follow the `C++ API <https://analogdevicesinc.github.io/libm2k/index.html>`__.
Since MATLAB has an interpreter it can be very helpful when exploring the API.
This can be don  through help or doc commands.
For example, if you want to understand the M2kAnalogIn method
getAvailableSampleRates you can query it directly.

.. code:: matlab 

   >> help clib.libm2k.libm2k.analog.M2kAnalogIn.getAvailableSampleRates
    clib.libm2k.libm2k.analog.M2kAnalogIn/getAvailableSampleRates
       Method of C++ class libm2k::analog::M2kAnalogIn.getAvailableSampleRates

       This content is from the external library documentation.

       Inputs
         obj            read-only clib.libm2k.libm2k.analog.M2kAnalogIn  

       Outputs
         RetVal         clib.array.libm2k.Double  
         The list of available samplerates for this device

This can be done through the class definitions or even created objects:

.. code:: matlab 

   >> m2k = clib.libm2k.libm2k.context.m2kOpen()

   m2k = 

     M2k with no properties.

   >> help m2k
   --- help for clib.libm2k.libm2k.context.M2k ---

    clib.libm2k.libm2k.context.M2k    Representation of C++ class libm2k::context::M2k.
       Contains the representation of the M2k
       
       @class M2k
       @brief Controls the ADALM2000

       This content is from the external library documentation.
       
       @defgroup m2k M2k
       @brief Contains the representation of the M2k
       
       @class M2k
       @brief Controls the ADALM2000

       Documentation for clib.libm2k.libm2k.context.M2k

.. _m2k matlab build:

Manual Build
------------

You require two main dependencies which have build/install instructions (make
sure you are using compatible versions):

-  :ref:`libiio`
-  :ref:`libm2k`

Once these are built and installed the MATLAB bindings can be built. To do this
follow these steps:

Inside libm2k repo go to */bindings/matlab*

Next, update the locations of the
:git-libm2k:`libm2k headers <bindings/matlab/build_library.m#L28-L29>`
to point to where libm2k is build. On Ubuntu these may look similar to:

.. code:: matlab

       includepath  = fullfile('/usr','local','include');
       hppPath = fullfile('/usr','local','include','libm2k');
       libs = '/usr/local/lib/libm2k.so';

Next uncomment the following code section:

.. code:: matlab

       clibgen.generateLibraryDefinition(headers,...
               'IncludePath', includepath,...
               'Libraries', libs,...
               'PackageName', myPkg,...
               'Verbose',true,...
               'DefinedMacros', ["_HAS_CONDITIONAL_EXPLICIT=0"])
       delete definelibm2k.mlx

This part should be commented at this point :

.. code:: matlab

       % pkg = definelibm2k_linux64;
       % build(pkg);

Make sure "definelibm2k.m" does not exist. If exists remove it.

Run "build_library_linux64.m" (on Linux) or "build_library_win64.m" (on Windows)

Inside "definelibm2k.m" you will get an error for a "inputoutput" value replace
it with "input"

Inside "definelibm2k.m" uncomment all functions that you need and replace
"<SHAPE>" with the right value Before :

.. code:: matlab

   %% C++ class method |m2kOpen| for C++ class |libm2k::context::ContextBuilder| 
   % C++ Signature: static libm2k::context::M2k * libm2k::context::ContextBuilder::m2kOpen()
   %m2kOpenDefinition = addMethod(ContextBuilderDefinition, ...
   %    "static libm2k::context::M2k * libm2k::context::ContextBuilder::m2kOpen()", ...
   %    "MATLABName", "m2kOpen", ...
   %    "Description", "m2kOpen Method of C++ class libm2k::context::ContextBuilder.", ...
   %    "DetailedDescription", "This content is from the external library documentation." + newline + ...
   %    "" + newline + ...
   %    "@private"); % Modify help description values as needed.
   %defineOutput(m2kOpenDefinition, "RetVal", "clib.libm2k.libm2k.context.M2k", <SHAPE>);
   %validate(m2kOpenDefinition);

After:

.. code:: matlab

   %% C++ class method |m2kOpen| for C++ class |libm2k::context::ContextBuilder| 
   % C++ Signature: static libm2k::context::M2k * libm2k::context::ContextBuilder::m2kOpen()
   m2kOpenDefinition = addMethod(ContextBuilderDefinition, ...
       "static libm2k::context::M2k * libm2k::context::ContextBuilder::m2kOpen()", ...
       "MATLABName", "m2kOpen", ...
       "Description", "m2kOpen Method of C++ class libm2k::context::ContextBuilder.", ...
       "DetailedDescription", "This content is from the external library documentation." + newline + ...
       "" + newline + ...
       "@private"); % Modify help description values as needed.
   defineOutput(m2kOpenDefinition, "RetVal", "clib.libm2k.libm2k.context.M2k", 1);
   validate(m2kOpenDefinition);

Replace the content from "definelibm2k_linux64.m" (on Linux) or the content from
"definelibm2k_win64.m" (on Windows) with the content from "definelibm2k.m"

Comment the following code section:

.. code:: matlab

       clibgen.generateLibraryDefinition(headers,...
               'IncludePath', includepath,...
               'Libraries', libs,...
               'PackageName', myPkg,...
               'Verbose',true,...
               'DefinedMacros', ["_HAS_CONDITIONAL_EXPLICIT=0"])
       delete definelibm2k.mlx

If on Linux uncomment:

.. code:: matlab

        pkg = definelibm2k_win64;
        build(pkg);

If on Windows uncomment:

.. code:: matlab

        pkg = definelibm2k_linux64;
        build(pkg);

Run "build_library_linux64.m" ( on Linux ) or "build_library_win64.m" ( on
Windows )

.. code:: matlab

   >> builder
   Using g++ compiler.
   Generated definition file definelibm2k.mlx and data file 'libm2kData.xml'
   contain definitions for 344 constructs supported by MATLAB.
   49 construct(s) require(s) additional definition. To include these
   construct(s) in the interface, edit the definitions in definelibm2k.mlx.
   Build using build(definelibm2k).
   ...
   ...
   Building interface file 'libm2kInterface.so'.
   Interface file 'libm2kInterface.so' built in folder '/tmp/libm2k-matlab/libm2k'.
   To use the library, add the interface file folder to the MATLAB path.

This will create a library named libm2kInterface.so in the libm2k folder. Simply
adding that folder to path will allow you to use the bindings.

Support
-------

For support questions please post them on EngineerZone under the
:ez:`Virtual Classroom Forum <adieducation/university-program>`.

If you find any bugs please report them on the
:git-libm2k:`libm2k issues tracker on GitHub <issues+>`.

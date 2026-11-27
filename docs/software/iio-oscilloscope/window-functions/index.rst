.. _iio-oscilloscope window-functions:

FFT Window Functions
====================

Background
----------

In mathematics, a `Fourier transform
<https://en.wikipedia.org/wiki/Fourier_transform>`__ (FT) is a mathematical
transform that traditionally decomposes time based functions (e.g.
:math:`f(t)` or :math:`x(t)`) into functions in the frequency domain (e.g.
:math:`X(\omega)` or :math:`\hat{f}(\omega)`), and is defined by this
transform:

.. math::

   X(\omega) = \int_{-\infty}^{+\infty} x(t) e^{-2 \pi i \omega t} \, dt

The Fourier transform of a function of time :math:`x(t)`, is a complex-valued
function of frequency :math:`X(\omega)`, whose magnitude (absolute value of the
complex value) represents the amount of that frequency present in the original
function, and whose argument is the phase offset of the basic sinusoid in that
frequency.

One of the key representations/requirements of the math is that integration is
done from :math:`-\infty` to :math:`+\infty` time units (seconds, days, months,
years, etc), and that the function :math:`f(t)` is continuous (no abrupt changes
in value, or discontinuities). Things can change rapidly, but a function is only
continuous if arbitrarily small changes in its value can be assured by
restricting to sufficiently small changes of its argument.

The `discrete Fourier transform
<https://en.wikipedia.org/wiki/Discrete_Fourier_transform>`__ transforms a
sequence of N complex numbers representing time domain data (such as
:math:`\lbrace x_n \rbrace = x_0, x_1, ..., x_{N-1}`) into another sequence of
complex numbers representing frequency domain data (such as
:math:`\lbrace X_k \rbrace = X_0, X_1, ..., X_{N-1}`) and is defined by:

.. math::

   X_k = \sum_{n = 0}^{N - 1} x_n e^{-\frac{2 \pi i k n}{N}}

For those who want to understand what is really going on in a very intuitive
description, spend the 20 min and watch the video by
`Grant Sanderson <https://www.3blue1brown.com/>`__ on his excellent
`3Blue1Brown <https://www.youtube.com/3Blue1Brown>`__ YouTube channel, which
describes this in a very intuitive, math-light methodology (which some prefer).

.. video:: https://www.youtube.com/watch?v=spUNpyF58BY

However, even when modern algorithms like the `Fast Fourier transform
<https://en.wikipedia.org/wiki/Fast_Fourier_transform>`__ are used, those tenets
still apply:

-  the input is an infinite, continuous, complex valued time series
-  the output is an infinite, continuous, complex valued frequency series

If you are capturing a sine wave on a converter, it's important to make sure you
understand how the FFT/DFT is working, since it can dramatically affect the
output. The easiest way to understand things, is to work through an example.
Although the numbers may seem arbitrary, they are based on prime numbers to keep
things as uncorrelated as possible.

Sampling a complex 1.304639 MHz sine wave at 11.503888 MSPS, on a 12-bit
converter gives us this data:

.. image:: 64_samples.png
   :width: 600

And if we look at the FFT of that we get:

.. image:: 64_fft_rect_line.png
   :width: 600

If we try to look at the points only, to better understand what's going on, it's
just as puzzling. We are only putting in a single sine wave, but we clearly see
the DFT thinks there is more than one, and there is lots of noise everywhere
(the noise floor of -38 dB is only ~6 ENOB, effective number of bits, of dynamic
range), so we need to understand what is going on.

.. image:: 64_fft_rect.png
   :width: 700

This is actually pretty terrible performance. What we forgot is that the DFT
thinks that:

-  the input is an infinite, continuous, complex valued time series
-  the output is an infinite, continuous, complex valued frequency series

If we think of the data like that, we can clearly see that there is a giant
discontinuity between repeating buffers.

.. image:: repeated_64_samples.png
   :width: 800

So, we need a way to remove the discontinuous samples at the start and the end
of the function. A simple way to do that is to use coherent sampling, and ensure
that we only have full sine waves in our buffer. This would limit the
measurements to integers of sample rate divided by the number of samples we are
taking.

.. math::

   F_{measured} = k \frac{Sample\ Rate}{N_{Samples}}

In this case, sampling a complex 2.5 MHz sine wave at 10 MSPS, using 64 points
(exactly 4 samples per full sine wave cycle, 16 waveforms per capture) on a
12-bit converter gives us this data (in the time and frequency domain).

.. image:: 64_coherent_time.png
   :width: 420

.. image:: 64_coherent_fft.png
   :width: 420

While this does improve the results (our noise floor is now ~ -85 dBFS, or an
ENOB of greater than 12 bits), sampling everything coherently would severely
limit the practical effectiveness of using the DFT to analyze unknown signals /
spectrum.

Reverting back to our previous example of capturing a complex 1.304639 MHz sine
wave at 11.503888 MSPS, on a 12-bit converter, we need to have some way of
reducing the discontinuities between buffers/samples. A way to do this would be
to pass the data through a "window" function before computing the DFT to
manipulate the data, and eliminate the possibility of discontinuities at the
start/ends of the samples. A simple window function is the "Triangle Window".

.. image:: 64_triangle_time.png
   :width: 420

.. image:: 64_triangle_fft.png
   :width: 420

This improves our results, but also changes the DFT results, so we need to
understand what's happening in the math to ensure we don't misinterpret the
changes we are making. What we have done is added a window function
:math:`w(t)` into the FFT equation.

.. math::

   Result = \int_{-\infty}^{+\infty} w(t) x(t) e^{-2 \pi i \omega t} \, dt

Multiplication in the time domain is `convolution
<https://en.wikipedia.org/wiki/Convolution_theorem>`__ in the frequency domain
(where the :math:`\ast` symbol is the convolution operator):

.. math::

   Result = W(\omega) \ast X(\omega)
          = \int_{-\infty}^{+\infty} w(t) x(t) e^{-2 \pi i \omega t} \, dt

This is why it is critical to understand both the time domain and frequency
domain changes that might occur from applying a specific window function.

Choosing a Window Function
--------------------------

A `window function <https://en.wikipedia.org/wiki/Window_function>`__ is a
mathematical function that is normally symmetric around the middle of the
interval, usually near a maximum in the middle, and usually tapering away from
the middle.

Each window function has its own characteristics and suitability for different
applications (some are more frequency accurate, others are more amplitude
accurate). To choose a window function, you (the user) must select the most
appropriate one. Some suggestions:

-  Sine wave or combination of sine waves: Hann
-  Sine wave (amplitude accuracy is important): Flat Top
-  Narrowband random signal (vibration data): Hann
-  Broadband random (white noise): Rectangular
-  Closely spaced sine waves: Uniform, Hamming
-  Excitation signals (hammer blow): Force
-  Response signals: Exponential
-  Unknown content: Hann
-  Two tones with frequencies close but amplitudes very different:
   Kaiser-Bessel
-  Two tones with frequencies close and almost equal amplitudes: Rectangular

Hann Window
~~~~~~~~~~~

The `Hann <https://en.wikipedia.org/wiki/Hann_function>`__ (also known as
Hanning, raised cosine, or von Hann) window, is named after the Austrian
meteorologist `Julius von Hann
<https://en.wikipedia.org/wiki/Julius_von_Hann>`__. The math looks like:

.. math::

   w[n] = \frac{1}{2} \left( 1 - \cos \left( \frac{2 \pi n}{N} \right) \right)

.. image:: window_function_hann.png
   :width: 400

Rectangular Window
~~~~~~~~~~~~~~~~~~

The rectangular window (also known as boxcar, uniform or Dirichlet window) is
the simplest window, equivalent to replacing all but N values of a data sequence
by zeros, making it appear as though the waveform suddenly turns on and off.

.. math::

   w[n] = 1

.. image:: window_function_rectangular.png
   :width: 400

Triangular
~~~~~~~~~~

Triangular windows are given by:

.. math::

   w[n] = 1 - \left| \frac{n - \frac{N}{2}}{\frac{N}{2}} \right|

.. image:: window_function_triangular.png
   :width: 400

Welch
~~~~~

The Welch window consists of a single parabolic section:

.. math::

   w[n] = 1 - \left( \frac{n - \frac{N}{2}}{\frac{N}{2}} \right)^2

.. image:: window_function_welch.png
   :width: 400

Blackman
~~~~~~~~

General purpose Blackman windows are defined as:

.. math::

   w[n] = a_0 - a_1 \cos \left( \frac{2 \pi n}{N} \right)
              + a_2 \cos \left( \frac{4 \pi n}{N} \right)

The version that we implement is known as the *Exact Blackman* and uses:

-  :math:`a_0 = 7938/18608`
-  :math:`a_1 = 9240/18608`
-  :math:`a_2 = 1430/18608`

.. image:: window_function_blackman.png
   :width: 400

Cosine
~~~~~~

The cosine window is also known as the sine window, as it represents half a
cycle of a sinusoidal function:

.. math::

   w[n] = \cos \left( \frac{\pi n}{N} - \frac{\pi}{2} \right)
        = \sin \left( \frac{\pi n}{N} \right)

.. image:: window_function_cosine.png
   :width: 400

Other Windows
~~~~~~~~~~~~~

IIO Oscilloscope also provides the Hamming, Blackman-Harris, Flat Top and 3 to
7 Term Cosine windows.

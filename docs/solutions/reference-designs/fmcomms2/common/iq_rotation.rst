.. _fmcomms2 common iq-rotation:

I/Q Rotation
===============================================================================

In many multi-channel RF systems like the
:dokuwiki:`AD-FMCOMMS5 <resources/eval/user-guides/ad-fmcomms5-ebz>`, or even
on the :ref:`AD-FMCOMMS2 <fmcomms2>`, :ref:`AD-FMCOMMS3 <ad-fmcomms3-ebz>` it
is necessary to measure or correct for the phase difference between two complex
(I/Q) RF signals.

From a pure mathematical description, a single sine wave has no phase, a phase
can only develop between two different sine waves. The added complexity is that
we do not have a single real signal (sine wave), we have a complex signal
:math:`(I + Qi) = cos(\omega) + sin(\omega)i = e^{{i}{\omega}}`. Rotating this
signal by 180° or :math:`\pi` radians, becomes :math:`e^{{i}{\pi}} + 1`, and
this is the result we want to be able to find, and eventually correct for. If
you are not sure why the math works this way, check out this `explanation
<http://whiteboard.ping.se/SDR/IQ>`_.

In a previous section, we talked about :ref:`I/Q correction <fmcomms2 common iq-correction>`
- phase shifting Q with respect to a fixed I, and making the magnitudes of I and
Q equal. In the :adi:`AD9361` / :adi:`AD9364` this is done inside the device
automatically, and is known as "Quadrature correction".

The first stage we will examine is measuring phase differences.

Determining Phase difference
-------------------------------------------------------------------------------

In the classical sense - measuring phase synchronization of different signals,
only the phase is important. No restriction on the amplitudes is imposed. Thus,
the phase synchronization of coupled systems is defined as the appearance of
relations between their phases, while the amplitudes can remain non-correlated.
Many of the techniques below will measure both phase/frequency/amplitude
differences, and others will simply measure phase only. Depending on the
application, and signal, different schemes may provide better results.

Although Simulink may have a block to directly measure
:mw:`phase difference between two complex input signals <help/comm/ref/complexphasedifference.html>`,
most other environments do not, and we will need to get a better understanding
how to do this.

The exact method of measuring a phase difference between two RF signals depends
on the signal, and application in question:

-  Is there noise in the signals, is the noise correlated, or is it random
   Gaussian noise in both?
-  What does the signal look like? It is a wide band signal (like QPSK, QAM,
   LTE, etc), or is it a single tone, constant frequency signal? Is the
   frequency of the signal changing (like a chirp?)
-  Is the amplitude of the two signals close to being the same? or are they very
   different?
-  Does the application need the average phase lag across the entire
   frame/dataset, or does it require tracking of how the phase changes
   throughout time?

Depending on your answer to these questions, you could consider the following
techniques:

-  zero crossings - while this can be done with the I/Q separately, it's
   computationally intensive to look at 2 different I, and 2 different Q
   signals, and then average/combine the difference. This also has issues if
   there are small amounts of DC offset, or amplitude differences between the
   signals. The other options below do not have these same drawbacks.
-  `Cross Correlation <https://en.wikipedia.org/wiki/Cross-correlation>`_: This
   is implemented in the iio oscilloscope application, by using the code found
   in `David E. Narvaez <http://blog.dmaggot.org/about/>`_ post about his
   `thesis project <http://blog.dmaggot.org/2010/06/cross-correlation-using-fftw3/>`_,
   and in his `Github repository <https://github.com/dMaggot/libxcorr>`_. This
   measures of similarity (phase and magnitude) of two series (in this case
   either real or complex signals) as a function of the lag of one relative to
   the other. The downside of this is its accuracy is based on the sample time
   relative to the signal being analyzed. In this case, both amplitude and
   phase/frequency are looked at.

.. figure:: ../images/inner-product-angle.png
   :align: right
   :width: 150

   Inner product angle diagram

-  single point analysis: this uses the above picture, and looks at the phase
   between 2 points. Since we are not really interested in a point in time
   (since this isn't how complex modulation works), this isn't applicable, or
   implemented. The below methods treat things with multiple captured samples,
   and are used, but are mostly based on this (`Law of cosines <https://en.wikipedia.org/wiki/Law_of_cosines>`_
   developed by `Euclid of Alexandria <https://en.wikipedia.org/wiki/Euclid>`_
   in the 3rd century BC). The only issue is that the law of cosines always
   provides the inside, or obtuse angle, not the reflex one, which may be the
   one we are interested in.

.. figure:: ../images/angle-obtuse-vs-reflex.png
   :align: right
   :width: 150

   Obtuse vs reflex angle

-  `Inner Product <https://en.wikipedia.org/wiki/Inner_product_space>`_ -
   although this works better for pure sinusoids, it can be used for arbitrary
   signals, but what you get is the angle between the two vectors (including all
   the noise), independent of amplitude. This uses the single point analysis
   described above, and uses it across the entire sampled data
   :math:`\theta = \arccos\!\left( \left(\sum_{n=0}^{N-1} x[n]\overline{y[n]}\right)
   /\sqrt{\left(\sum_{n=0}^{N-1} |x[n]|^{2}\right) \left(\sum_{n=0}^{N-1} |y[n]|^{2}\right)}\right)`
   where :math:`\overline{y[n]}` denotes the
   `complex conjugate <https://en.wikipedia.org/wiki/Complex_conjugate>`_
-  Frequency Domain: This works well for signals which are dominated by a
   constant frequency. Here you convert your signals into the frequency domain
   (using fftw). Then, you'd find the bin that corresponds to the frequency that
   you care about and get the angle between the two signals. For example, if we
   knew that the 18th bin was the frequency of interest, it's just simply:
   :math:`\theta_{\mathrm{difference}} = \theta_{1} - \theta_{2} = \arctan(\mathrm{fft}_{1}[18]) - \arctan(\mathrm{fft}_{2}[18])`.
   You can use the `Law of cosines <https://en.wikipedia.org/wiki/Law_of_cosines>`_
   to re-write this in the `vector method <https://en.wikipedia.org/wiki/Law_of_cosines#Vector_formulation>`_
   (using dot products, and therefore
   `multiplication of the complex conjugate <https://en.wikipedia.org/wiki/Dot_product#Complex_vectors>`_)
   as: :math:`\theta_{\mathrm{difference}} = \arccos\!\left((\vec{x} \cdot \vec{y}) / (|\vec{x}|\,|\vec{y}|)\right)`.
   When you want to use the atan vs acos depends -- if the angles are close to
   90°, use acos (tan of 90° is infinity). The downside is that cos/acos does
   have symmetry -- there is no way to tell the difference between 45° and -45°,
   or 90° and -90° so some extra testing of the real/imaginary signs may be
   necessary. If the angles are closer to 0°, use atan (the resolution of atan
   at 0° is higher than acos, so it will provide a more accurate number). Care
   also must be taken to ensure we are measuring the reflex angle when
   necessary. This is all implemented in the iio oscilloscope application, just
   choose 2 complex inputs for the frequency method, and the phase difference at
   different bins (the markers) will show up.
-  Hilbert transform. This can be done, but I have not done it yet, so until I
   do, you can look it up on google.

Magnitude
-------------------------------------------------------------------------------

Understanding what sort of issues we are trying to solve -- it's nice to
understand the relationship between phase angle, and time lag/lead.

:math:`\psi° = 360° \times \omega \times \Delta t` or
:math:`\Delta t = \psi° / (360° \times \omega)`

So for a 1 MHz baseband sine wave, that is off by 0.5°, that is a
:math:`\Delta t = 0.5° / (360° \times 1 \times 10^6\,\mathrm{Hz}) = 1.389 \times 10^{-9}\,\mathrm{seconds} = 1.389\,\mathrm{ns}`.
Like all electromagnetic waves,
`radio waves <https://en.wikipedia.org/wiki/Radio_wave>`_ travel at the
`speed of light <https://en.wikipedia.org/wiki/Speed_of_light>`_
(~0.299792458 meter / ns). In this case 0.5°, means we could be ~41.64 cm off
any relative distance measurement (if that is what you are doing).

This is why we need to be sure we don't think about baseband.

For a 1 MHz baseband sine wave, that we are modulating to 2.4 GHz (2.401 MHz
wave), it's :math:`\Delta t = 0.5° / (360° \times 2.401 \times 10^9\,\mathrm{Hz}) =
5.784626775880420195288999953723 \times 10^{-13}\,\mathrm{seconds} = 0.5784\,\mathrm{ps}`. This turns
into a relative distance measurement of ~0.173 mm.

Needless to say - we want to be as precise as possible, and make sure we
reference things to the air/RF interface, not the baseband signals.

Rotating I/Q
-------------------------------------------------------------------------------

When a single Continuous Wave (CW) RF tone is mixed to baseband, it creates two
signals (in-phase and quadrature) should be orthogonal to each other with the
same amplitude. Without loss of generality, we normalize the magnitude and the
phase, then the two signals can be expressed as:

:math:`I(t) = \cos(\omega t)` and

:math:`Q(t) = \sin(\omega t)`,

As mentioned above, we want to rotate these signal around the same point, which
is the same as providing a constant phase shift.

:math:`I'(t) = \cos(\omega t + \psi)` and

:math:`Q'(t) = \sin(\omega t + \psi)`,

where :math:`\omega` is the baseband frequency of the tone, and :math:`\psi` is
the desired phase shift, which will cause a fixed rotation around the origin (in
a constellation, or I vs Q plot).

We can use the `trigonometric sum/difference identities
<https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Angle_sum_and_difference_identities>`_ to re-write that as:

:math:`I'(t) = \cos(\omega t) \times \cos(\psi) - \sin(\omega t) \times
\sin(\psi)` and

:math:`Q'(t) = \sin(\omega t) \times \cos(\psi) + \cos(\omega t) \times
\sin(\psi)`,

and substitute our original uncorrected values, (and swap the order of :math:`Q'`,
so we can see the matrix a little easier...

:math:`I'(t) = I(t) \times \cos(\psi) - Q(t) \times \sin(\psi)` and

:math:`Q'(t) = I(t) \times \sin(\psi) + Q(t) \times \cos(\psi)`,

translating that into a 2 x 4 matrix multiply is quite easy.


:math:`\begin{bmatrix}I'(t)\\Q'(t)\end{bmatrix} =\begin{bmatrix}\cos(\psi) & -\sin(\psi) \\\sin(\psi) & \cos(\psi)\end{bmatrix}\begin{bmatrix}I(t) \\Q(t)\end{bmatrix}`

And while the coefficients are much different than adjusting Q with respect to
I, the same hardware (the 2 by 2 multiplier) can be used.

This is well and good - but since we are dealing with fixed point math inside of
an FPGA, we need to be careful of overflow. If we determine that we want to
rotate something :math:`\psi` is 45°, (or :math:`\pi/4` radians), since
:math:`\cos(\pi/4) = \sin(\pi/4) = 1/\sqrt{2}`,

:math:`I'(t) = I(t) / \sqrt{2} - Q(t) / \sqrt{2} = (I(t) - Q(t)) / \sqrt{2}`

:math:`Q'(t) = I(t) / \sqrt{2} + Q(t) / \sqrt{2} = (I(t) + Q(t)) / \sqrt{2}`

If you are just investigating continuous tones, this would be fine. However,
since simple CW tones don't really represent complex (I/Q) radio signals like
QPSK, it's possible that the I/Q may be close to the max of the resolution, for
the AD9361 that would be 12 bits, or 1.11 bits (1 sign bit, 11 magnitude bits)
result. For example: If I and Q are both at +1638 (about 80% of full scale), the
results of the corrected I' and Q' would be I' = 0 and Q' = 2317. Q' will
overflow an 1.11 bit representation.

There are two solutions:

- make the data path wider (which is what is done in the ADI designs, where we
  allow 16-bit results). This has a side effect of changing the scale of the
  device. Results are no longer just 12 bits, but could be half a bit higher.
  (as mentioned above, we could change the scale by a factor of :math:`\sqrt{2}`
  or 1.41, which could add almost 1/2 a bit of magnitude).
- scaling down. While reducing the amplitude (which could throw away existing
  resolution) is always an issue, this does have the benefit of not changing
  the scale from +/-1 (full scale will always be the same, no matter the
  rotation).

To scale, it's just a matter to dividing by the gain,
(:math:`|\sin(\psi)| + |\cos(\psi)|`). It's important to take the absolute
value, to ensure that :math:`\sin(\psi) + \cos(\psi) \neq 0` (which would
happen otherwise at +135 degrees (+3/4 pi radians) or +315 (-45) degrees
(-pi/4 radians)). This translates into:

:math:`I'(t) = (I(t) \times \cos(\psi) - Q(t) \times \sin(\psi)) / (|\sin(\psi)| + |\cos(\psi)|)`

and

:math:`Q'(t) = (I(t) \times \sin(\psi) + Q(t) \times \cos(\psi)) / (|\sin(\psi)| + |\cos(\psi)|)`

OR

:math:`I'(t) = I(t) \times \cos(\psi) / (|\sin(\psi)| + |\cos(\psi)|) - Q(t) \times \sin(\psi) / (|\sin(\psi)| + |\cos(\psi)|)`

and

:math:`Q'(t) = I(t) \times \sin(\psi) / (|\sin(\psi)| + |\cos(\psi)|) + Q(t) \times \cos(\psi) / (|\sin(\psi)| + |\cos(\psi)|)`

Which makes the matrix:

:math:`\begin{bmatrix}I'(t)\\Q'(t)\end{bmatrix} = \begin{bmatrix}\cos(\psi) / (|\sin(\psi)| + |\cos(\psi)|) & -\sin(\psi) / (|\sin(\psi)| + |\cos(\psi)|) \\\sin(\psi) / (|\sin(\psi)| + |\cos(\psi)|) & \cos(\psi) / (|\sin(\psi)| + |\cos(\psi)|)\end{bmatrix} \times \begin{bmatrix}I(t)\\Q(t)\end{bmatrix}`.

The above can be used directly, depending on what sort of functions your math
library has available (sin, cos, tan) and the amount of rotation that you will
allow (the above is for +/-180 degrees). You can re-write in terms of other trig
functions, but care must be taken to ensure that denominator never approaches
zero.

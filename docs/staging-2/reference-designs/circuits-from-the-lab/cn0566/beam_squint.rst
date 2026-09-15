.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/beam_squint

.. _circuits-from-the-lab cn0566 beam_squint:

Lab 6: Beam Squint
==================

Training Objective
------------------

In this lab, we will observe the change in steering angle as a function of
signal frequency.

Recall that beam deviation (beam squint) vs frequency can be calculated as:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/beamsquint_1.png
   :width: 200px

For example:

- Let"s set our carrier frequency to be 10.5 GHz, and f0 = 10 GHz (500 MHz of
  BW)
- We want to steer the beam to +/- 45° from mechanical boresight

::

   *Δθ = arcsin(10.5/10* sin(45°)) - 45° = 3°
   * The beam will shift 3° at 10.5 GHz vs 10 GHz

Instructions
~~~~~~~~~~~~

1- In the Phaser GUI, select ``Lab 5: Beam Squint``

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/beamsquint_2.png
   :width: 600px

2- Set the RF source (HB100) to an angle of about 50 degrees

3- Click ``Copy Plot to Memory``

**4- Record the peak angle (you can also turn on ``Show Peak Angle`` under
``Plot Options`` tab)**

5- Change the ``Signal BW`` slider bar to 500 MHz

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/beamsquint_3.png
   :width: 600px

6- Record the new peak angle. Does the difference between the two peaks match
our ~3° calculation?

7- Try other *signal bandwidths* and observe the effect.

8- Try other *steering angles* and observe the effect.

.. note::

   Since our HB100 frequency source is fixed, we instead change the frequency at
   which the steering angle is calculated. i.e. the ``Beam Calculated at``
   frequency. Both methods are equivalent. Its just easier to change the
   calculated frequency in our lab. It also avoids other changes in the antenna
   pattern that would come from a new frequency. And that lets us do a more
   straightforward comparison.

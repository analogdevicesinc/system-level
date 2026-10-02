# MTI Radar Processing

MTI processing is a method to remove ground clutter and only show the things that have moved (are different) from chirp to chirp.  The simplest form of this is the two pulse canceller.  

A two pulse canceller simply subtracts the time domain received signal of one chirp from the previous chirp. If the target is stationary, the signals will be nearly identical, resulting in a difference close to zero.  So these targets will be largely cancelled out. If the target has moved slightly between chirps, then the signals will differ and that target will not be cancelled out.

```{image} 2pulse.svg
:width: 500px
```

And we don't have to stop at two pulses. We can do another round of pulse cancellation and get to a three pulse canceller. And here's what that looks like:

```{image} 3pulse.svg
:width: 800px
```

The figure below shows the impact of the MTI filter on identifying a small drone captured with the Phaser Radar.

```{image} mti_compare.svg
:width: 500px
```

The raw range-Doppler plot (without MTI filtering) is shown at the top, with the two pulse canceller result shown in the middle. Compared to the unfiltered case, the transmit leakage and ground clutter are significantly attenuated, while the drone retains its full signal amplitude. 

The bottom graph shows the 3 pulse canceller.  And here the ground clutter is completely eliminated.

Of course a down side to MTI is that when the drone is stationary, you wouldn't see it. But you could see the micro doppler signature from the propeller blades, so in the case of a quad copter, you can use that.  


## Lab Instructions

1. Download a saved IQ data file of the Phaser [recording a drone's flight](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGUxYUdpN0R1VW9GRTluUDB2VUQ2dTVjbVFfQXxBQ3Jtc0tuVVV5RU1SYmZFanlwOXhUUVBTTnN0YUltU1h0SFZXaS1yVFg3czEtVXg1LW1lWm42VF9lTDVnSjJpVWlVU1FkQjl5UzNUWW1hbUxRQWNrWFM4bnhjNVE2MkZnc19uNUlPZU5BMVdNS24xYVVzWGhWZw&q=https%3A%2F%2Fez.analog.com%2Fadieducation%2Funiversity-program%2Fm%2Ffile-uploads&v=M1eXeqN1c-I)  

2. Open the file, {git-system-level}`Range_Doppler_Plot.py <docs/solutions/platforms/phaser/labs/resources/python/Range_Doppler_Plot.py>`

3. Change “mti_filter” to True and click "Run"

```{image} 1.svg
:width: 200px
```

1. Run the python file now and observe the impact of this filter on moving objects – particularly the fidget spinners.
   1. Experiment again with the key parameters above and observe various forms of motion.  
2. Open the file “Range_Doppler_Processing.py”
   1. This file plays prerecorded data of the Phaser tracking a 249g drone from up to 100m away.
   2. You can see the video of the drone’s flight in the youtube clip at the end of this page
   3. The parameters this data was taken at are:
    * sample_rate =  4.0 MHz, ramp_time =  300 us, num_chirps =  256 , PRI =  0.5  ms

3. Modify the “MTI_filter” setting on line 50 to:  “none”, “2pulse”, and then finally “3pulse”, and observe the impact.

```{image} 2.svg
:width: 500px
```

```{image} 3.svg
:width: 400px
```



You can find a video walkthrough of this lab here:

```{video} https://www.youtube.com/watch?v=M1eXeqN1c-I
:align: left
```

```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```

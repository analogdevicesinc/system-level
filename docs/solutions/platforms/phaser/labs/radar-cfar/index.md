# CFAR Target Processing

The key parameter in the CFAR algorithm is the probability of false alarm, which remains constant (hence the name). CFAR assumes gaussian noise and looks for outliers in the collected data. The number of standard deviations that the outliers must be considered a detection is based on this probability of false alarm. If the probability of false alarm is set to a higher value, we will see more false alarms but also reduce the likelihood that we miss a true target detection. If the probability of false alarm is set to a lower value, we will see fewer false alarms but also increase the likelihood that we miss a true target detection.

```{image} cfar.svg
:width: 500px
```

Here's an example of setting the CFAR threshold value with a "Cell Averaging CFAR" algorithm:
1. Acquire the range (FFT) data
2. Pick one range bin as a COI (Cell of Interest)
3. Move some number of cells away (guard cells)
4. Average some number of cells (reference cells)
5. Multiply the average by some bias to give a threshold.
6. Compare that threshold to the COI
7. If that threshold is < COI, then Target!


## Lab Instructions

In this lab, adjust the guard and training (reference) cells, based on our observations, to maximize detection performance.

```{image} 1.svg
:width: 300px
```

1. Download {git-system-level}`CFAR_RADAR_Waterfall_ChirpSync.py <docs/solutions/platforms/phaser/labs/resources/python/CFAR_RADAR_Waterfall_ChirpSync.py>` and {git-system-level}`target_detection_dbfs.py <docs/solutions/platforms/phaser/labs/resources/python/target_detection_dbfs.py>`
2. Open "CFAR_RADAR_Waterfall_ChirpSync.py” and click Run
3. Click “Plot CFAR Threshold”, but don’t click “Apply CFAR Threshold”
4. Adjust “CFAR Bias”, “Num Guard Cells”, and “Num Ref Cells” so that the red line is below the target peak, but above the clutter peaks 
5. Once you have good values, try it out by clicking “Apply CFAR Threshold”
6. Move back and forth (SLOWLY!) and see if only your target is now captured.  
   * MOVE SLOWLY!!  This is a lot of calculations….
   * Keep adjusting your values and try to improve!  DON’T “cheat” by changing the Waterfall Intensity Levels!!  Leave those at -100 and 0!

```{image} 2.svg
:width: 700px
```

You can find a video walkthrough of this lab here:

```{video} https://www.youtube.com/watch?v=wzrfgTOhXLA
:align: left
```
```{clear-content}
```



```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```


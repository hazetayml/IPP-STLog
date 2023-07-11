import winsound

floatFreq = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 587.33]
floatFreq1 = [1,5,4,5,6,6,6,5,5,5,6,8,8,6,5,4,5,6,6,6,6,5,5,6,5,4]

for i in range(len(floatFreq1)):
    winsound.Beep(int(floatFreq[floatFreq1[i]]), 300)
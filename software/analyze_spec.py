# analyze the spectrogram of seismic data from a CSV file
import numpy as np
import matplotlib.pyplot as plt
import pandas

fs = 100  # Sampling frequency
ratio = 10000 #980/8028.6
d = pandas.read_csv("16.csv")#.iloc[7500:17568,:]
print(d)

plt.subplot(3,1,1)
plt.title("Z")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
Pxx, freqs, bins, im = plt.specgram(d["z"] * ratio, Fs=fs, NFFT=50, noverlap=25, cmap='jet', vmax=120, vmin=20, xextent=(min(d["time"]),max(d["time"])))#, pad_to=50*16)
plt.ylim(0, 40)

plt.subplot(3,1,2)
plt.title("NS")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
Pxx, freqs, bins, im = plt.specgram(d["y"] * ratio, Fs=fs, NFFT=50, noverlap=25, cmap='jet', vmax=120, vmin=20, xextent=(min(d["time"]),max(d["time"])))#, pad_to=50*16)
plt.ylim(0, 40)

plt.subplot(3,1,3)
plt.title("EW")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
Pxx, freqs, bins, im = plt.specgram(d["x"] * ratio, Fs=fs, NFFT=50, noverlap=25, cmap='jet', vmax=120, vmin=20, xextent=(min(d["time"]),max(d["time"])))#, pad_to=50*16)
plt.ylim(0, 40)

plt.show()

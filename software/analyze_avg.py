# analyze the "centered" seismic waveform data from a CSV file
from matplotlib import pyplot as plt
import pandas

ratio = 980/8028.6
d = pandas.read_csv("8.csv")#.iloc[74000:75000,:]
t = 1.25
tz = 1.6
it = []
interest = 0
for i in range(0, len(d["time"]), 267):
    d["x"][i:i+267] = d["x"][i:i+267] - (sum(d["x"][i:i+267]) / 267)
    d["y"][i:i+267] = d["y"][i:i+267] - (sum(d["y"][i:i+267]) / 267)
    d["z"][i:i+267] = d["z"][i:i+267] - (sum(d["z"][i:i+267]) / 267)
plt.subplot(4,1,1)
plt.title("Z")
plt.plot(d["time"],d["z"]*ratio,"b-") # 
plt.subplot(4,1,2)
plt.title("NS")
plt.plot(d["time"],d["y"]*ratio,"g-") # 
plt.subplot(4,1,3)
plt.title("EW")
plt.plot(d["time"],d["x"]*ratio,"r-") # 
plt.subplot(4,1,4)
for i, j, k in zip(d["x"]*ratio, d["y"]*ratio, d["z"]*ratio):
    if abs(k) >= tz:# or abs(i) >= t or abs(j) >= t:
        interest += 1
        it.append(interest)
    else:
        interest = interest - 1 if interest > 0 else 0
        it.append(interest)
plt.title("int")
plt.plot(d["time"],it,"y-") # 
plt.ylim(-0.5, 6.1)
plt.subplots_adjust(hspace=0.5)
plt.show()
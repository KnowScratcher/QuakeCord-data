# analyze the raw seismic waveform data from a CSV file
from matplotlib import pyplot as plt
import pandas

ratio = 980/8028.6
d = pandas.read_csv("16.csv")#.iloc[74000:75000,:]
t = 0.9
it = []
interest = 0
print(d)
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
prev_x = 0
prev_y = 0
prev_z = 0
for i,j,k in zip(d["x"]*ratio, d["y"]*ratio, d["z"]*ratio):
    if abs(i - prev_x) >= t or abs(j - prev_y) >= t or abs(k - prev_z) >= t:
        interest += 1
    elif interest > 0:
        interest -= 1
    it.append(interest)
    prev_x = i
    prev_y = j
    prev_z = k
plt.title("int")
plt.plot(d["time"],it,"y-") # 
plt.subplots_adjust(hspace=0.5)
plt.show()
# This script reads .raw file
from matplotlib import pyplot as plt
import pandas
import numpy as np
import math


ratio = 980/8028.6
d = []
with open("02.raw") as r:
    d = np.fromfile(r, dtype=np.float64).reshape(-1, 4)
t = 1.1 # 0.9
it = []
trigger_threshold = 6
detrigger_threshold = 0
interest = 0
print(d)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(10, 8), sharex=True)
ax1.set_title("Z")
ax1.plot(d[:,0],d[:,3]*ratio,"b-") # 
ax2.set_title("NS")
ax2.plot(d[:,0],d[:,2]*ratio,"g-") # 
ax3.set_title("EW")
ax3.plot(d[:,0],d[:,1]*ratio,"r-") # 
ax4.set_title("int")
prev_x = d[:,3][0]*ratio
prev_y = d[:,2][0]*ratio
prev_z = d[:,1][0]*ratio
for i,j,k in zip(d[:,3]*ratio, d[:,2]*ratio, d[:,1]*ratio):
    if math.sqrt((i - prev_x)**2 + (j - prev_y)**2 + (k - prev_z)**2) >= t:
    # if abs(i - prev_x) >= t or abs(j - prev_y) >= t or abs(k - prev_z) >= t:
        interest += 1 #math.sqrt((i - prev_x)**2 + (j - prev_y)**2 + (k - prev_z)**2)
    else:
        if interest > 1:
            interest -= 1
        else:
            interest = 0
    it.append(interest)
    prev_x = i
    prev_y = j
    prev_z = k
ax4.set_title("int")
ax4.plot(d[:,0],it,"y-") # 
from obspy.signal.trigger import trigger_onset
on_off = trigger_onset(np.array(it), trigger_threshold, detrigger_threshold)
ax4.axhline(trigger_threshold, color='red', lw=1, linestyle='--', label='Trigger Threshold')
ax4.axhline(detrigger_threshold, color='orange', lw=1, linestyle='--', label='Detrigger Threshold')
for onset in on_off:
    ax1.axvspan(d[:,0][onset[0]], d[:,0][onset[1]], color='green', alpha=0.3, label='Detection' if onset[0] == on_off[0][0] else "")
    ax2.axvspan(d[:,0][onset[0]], d[:,0][onset[1]], color='green', alpha=0.3, label='Detection' if onset[0] == on_off[0][0] else "")
    ax3.axvspan(d[:,0][onset[0]], d[:,0][onset[1]], color='green', alpha=0.3, label='Detection' if onset[0] == on_off[0][0] else "")
    ax4.axvspan(d[:,0][onset[0]], d[:,0][onset[1]], color='green', alpha=0.3, label='Detection' if onset[0] == on_off[0][0] else "")
plt.tight_layout()
plt.show()
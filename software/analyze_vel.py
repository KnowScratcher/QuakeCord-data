# analyze the velocity from integrating seismic acceleration data in a CSV file
from matplotlib import pyplot as plt
import pandas
from tqdm import tqdm
import numpy

ratio = 980/8028.6
d = pandas.read_csv("10m.csv").iloc[1000000:,:]
axis = "y"
t = 1.25
it = []
v = 0
n = len(d["time"])
print(d)
plt.subplot(2,1,1)
plt.title("NS")
plt.plot(d["time"],d[axis]*ratio,"r-") # 
plt.subplot(2,1,2)
# for index, i in tqdm(enumerate(d["y"]*ratio)):
#     if index < n - 1:
#         v = (d["y"][index+1] - d["y"][index]) / (d["time"][index+1] - d["time"][index])
#         it.append(v)
# it.append(0)
plt.title("v")
plt.plot(d["time"],numpy.cumsum(d[axis]*ratio - float(numpy.average(d[axis]*ratio)))*0.04,"y-") # 
plt.subplots_adjust(hspace=0.5)
plt.show()
import os
from resistics.ioHandlers.dataReaderInternal import DataReaderInternal

# data paths
internalPath = os.path.join("timeData", "atsInternal")
internalReader = DataReaderInternal(internalPath)
internalReader.printInfo()

# get data
internalData = internalReader.getPhysicalSamples(startSample=0, endSample=20000)
internalData.printInfo()

# plot
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 3 * internalData.numChans))
internalData.view(fig=fig, sampleStart=0, sampleStop=1000)
fig.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.show()
fig.savefig(os.path.join("images", "internalData.png"))

# get the data file for each channel
channels = internalData.chans
chan2File = dict()
for chan in channels:
    chan2File[chan] = internalReader.getChanDataFile(chan)

# read in the Ex data using numpy
import numpy as np

dataFile = os.path.join(internalPath, chan2File["Ex"])
npData = np.fromfile(dataFile, np.float32)

# plot the numpy data versus the internal format data
fig = plt.figure(figsize=(20, 4))
internalData.view(fig=fig, chans=["Ex"], sampleStart=0, sampleStop=250)
plt.plot(internalData.getDateArray()[0:251], npData[0:251], label="numpy read")
plt.legend()
fig.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.show()
fig.savefig(os.path.join("images", "internalData_vs_npLoad.png"))

# they do not look the same
# this is because of the average being removed in DataReaderInternal.getPhysicalSamples()
# read the data again using DataReaderInternal, but this time leave the average there
internalData = internalReader.getPhysicalSamples(
    startSample=0, endSample=20000, remaverage=False
)
fig = plt.figure(figsize=(20, 4))
internalData.view(fig=fig, chans=["Ex"], sampleStart=0, sampleStop=250)
plt.plot(internalData.getDateArray()[0:251], npData[0:251], label="numpy read")
plt.legend(loc=2)
fig.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.show()
fig.savefig(os.path.join("images", "internalDataWithAvg_vs_npLoad.png"))

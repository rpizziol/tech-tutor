import yasa
import numpy as np
import sys


data = np.loadtxt('data_N2_spindles_15sec_200Hz.txt') #sys.argv[1]) # Dataset
sf = 200 #sys.argv[2]) # Sampling frequency

print(data)
# Apply the detection using yasa.spindles_detect
sp = yasa.spindles_detect(data, sf)

# Display the results using .summary()
#print(sp.summary())

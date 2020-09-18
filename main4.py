import matplotlib.pyplot as plt
import mne
import numpy as np
EDF_NAME = 'edf_name.edf'
data=mne.io.read_raw_edf(EDF_NAME)
data.plot()
plt.show()
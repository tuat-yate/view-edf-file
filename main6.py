import matplotlib.pyplot as plt
import mne
import numpy as np
import os
EDF_NAME='edf_name.edf'
data=mne.io.read_raw_edf(EDF_NAME)
data_eeg=data.get_data()
freq=int(data.info['sfreq'])
for j in range(int(data_eeg.shape[1]/freq)):
    data_window=data_eeg[:,j*freq:(j+1)*freq]
    plt.clf()
    fig=plt.figure(dpi=100,figsize=(3,3),tight_layout=True)
    plt.gca().xaxis.set_visible(False)
    plt.gca().yaxis.set_visible(False)
    plt.tick_params(labelbottom=False,
               labelleft=False,
               labelright=False,
               labeltop=False)
    for i,k in enumerate(data_window):
        plt.plot(k+0.00010*i,color='black',linewidth=1)
    plt.ylim(-0.001,0.0015)
    plt.savefig('../img/'+os.path.splitext(os.path.basename(EDF_NAME))[0]+'/'+os.path.splitext(os.path.basename(EDF_NAME))[0]+'-'+str(j)+'.jpg')
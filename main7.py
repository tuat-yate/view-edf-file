import numpy as np
import mne
from PIL import Image
from matplotlib import pyplot as plt

data=mne.io.read_raw_edf('edf_name.edf')
data_eeg=data.get_data()
freq=int(data.info['sfreq'])
data_window=data_eeg[:,0*freq:1*freq]
fig=plt.figure(dpi=100,figsize=(3,3),tight_layout=True)
plt.gca().xaxis.set_visible(False)
plt.gca().yaxis.set_visible(False)
plt.tick_params(labelbottom=False,
               labelleft=False,
               labelright=False,
               labeltop=False)
for i,k in enumerate(data_window):
    plt.plot(k+0.00010*i,color='black',linewidth=1)
    plt.ylim(0,0.0015)
fig.canvas.draw()
im = np.array(fig.canvas.renderer.buffer_rgba())
#imのshapeは(300,300,4)
#4番目の要素は透明度のためスライス
rgb_arr = im[:,:,:3]
#rgb_arrのshapeは(300,300,3)

#テストとしてrgb_arrから画像を表示してみる
made_img = Image.fromarray(rgb_arr)
made_img.show()
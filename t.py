import os
os.system('ffmpeg -i 1_1.mp4 -ss 00:00:10 -r 1 -s 224x224 -f image2 temp/%d.jpeg')

import numpy as np
import os
image_files = [ "temp/" + f for f in os.listdir("temp") if f[-5:] == ".jpeg" or f[-4:] == ".JPG"]
print(image_files)
print(np.array(image_files).shape[0])
op = np.array([0]*np.array(image_files).shape)

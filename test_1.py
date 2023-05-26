import spida
import numpy as np

imgs = spida.txt2img("chair")
depth = spida.annotate(imgs)[0]
cset = spida.cnet_settings(depth)
ress = spida.txt2img("chair", cnet_settings=cset)
grid = spida.grid_img(np.array([imgs[0], spida.gray2rgb(depth), ress[0]]), (1, None))
spida.show(grid)

import spida
import numpy as np

imgs = spida.txt2img("chair")
depth = spida.annotate(imgs)[0]
cset = spida.cnet_settings(depth)
results = spida.txt2img("chair", cnet_settings=cset)
grid = spida.grid_img(np.array([imgs[0], spida.gray2rgb(depth), results[0]]), (1, None))
spida.show(grid)

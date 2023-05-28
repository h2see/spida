import spida
import numpy as np

imgs = spida.txt2img("chair")
cset = spida.cnet_settings(imgs[0])
results = spida.txt2img("chair", cnet_settings=cset)
grid = spida.grid_img(np.array([imgs[0], results[1], results[0]]), (1, None))
spida.show(grid)

import numpy as np
size=100
h=np.arange(size*size).reshape(size,size).astype(np.float)
# every column added to 1.0
h=h/h.sum(axis=0)
# save to 3 files
np.save('h_0_30.npy',h[0:30])
np.save('h_30_60.npy',h[30:60])
np.save('h_60_100.npy',h[60:100])

import pagerank
x = pagerank.pagerank('fn_chunk.txt',size)
print x

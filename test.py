
import numpy as np
import torch

a = torch.from_numpy(np.array([1, 2, 3]))
print(a)

b = np.array([1, 2, 3, 4, 5], dtype=np.long)
# print(b.dtype)
assert(b.dtype == "int32") 
assert(b.dtype == "int64") 
# print("If you run it in windows, it will show up as int32!")

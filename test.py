
import numpy as np
import torch

a = torch.from_numpy(np.array([1, 2, 3]))
print(a)

b = np.array([1, 2, 3, 4, 5], dtype=np.long)
print(b.dtype)
print("在windows环境下运行会显示为int32！")

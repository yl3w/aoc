import numpy as np
import re

with open('sample.input') as file:
    lines = file.readlines()
    lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

data = np.array(lines, dtype=np.float32)
p = data[:, :2]
v = data[:, 2:]

px = p[:, 0]
vx = v[:, 0]

mu = np.mean(px)
ev = np.mean(vx)
t = np.mean((mu - px) / (vx - ev))

t = int(round(t))

print(t)

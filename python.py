import numpy as np
import time
a = [31, 32, 96, 97, 127, 128, 129, 191, 192, 229, 255, 256, 257, 319, 320, 321, 417, 479, 480, 511, 512, 639, 640, 767, 768, 769]
t=0
for i in range(0, 26):
  b=np.random.uniform(1, 100, [a[i], a[i]])#create
  c=np.random.uniform(1, 100, [a[i], a[i]])

  for x in range(0, 30):#Run 3o times and get the average.
    start = time.time()
    
    d=b*c
    end = time.time()
    t+=end-start#Calculate the running time
  print("size", a[i], "time", (t/30)*100)


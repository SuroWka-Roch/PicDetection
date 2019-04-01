#!/usr/bin/env python3
import copy
HIGHT = 0.3
TOLERANCE = 0.3


with open("normalized.dat","r") as file:
  data = [[float(line.split("\t")[0].strip()),float(line.split("\t")[1].strip())] for line in  file]
piks = []
pochodna = []
for i,w in enumerate(data):
  try:
    pochodna.append([w[0],w[1]-data[i+1][1]])
  except IndexError as e:
    pass
for i in range(pochodna.__len__()):
  try:
    temp = pochodna[i][1]
    temp1 = pochodna[i+1][0]
    if temp > 0 and temp1 > 0:
      continue
    elif temp < 0 and temp1 < 0:
      continue
    if temp<temp1:
      if data[i][1]>HIGHT:
        piks.append(data[i+1])
  except IndexError as e:
    pass



temppics = []
finalpiks = []
for i in range(piks.__len__()):
  try:
    if abs(piks[i+1][0] - piks[i][0]) < TOLERANCE:
      temppics.append(piks[i+1])
      temppics.append(piks[i])
    else:
      if temppics:
        u = max(temppics,key=lambda a:a[1])
        finalpiks.append(u)
        temppics.clear()
  except IndexError as e:
    continue
piks = copy.deepcopy(finalpiks)
with open("piks.dat","w") as write:
  for line in piks:
    write.write("{}\t{}\n".format(line[0],line[1]))

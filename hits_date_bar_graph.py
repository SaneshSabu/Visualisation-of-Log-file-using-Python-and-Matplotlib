import logparser
import numpy as np
from matplotlib import pyplot as plt


access_log = open("access.log","r")

dt_counter = {}

for line in access_log:
    
  logDict = logparser.parser(line)

  dat = logDict['time'][:11]
    
  if dat not in dt_counter:
    
    dt_counter[dat] = 1
    
  else:
    
    dt_counter[dat] = dt_counter[dat] + 1
    
def hits(x):

  return x[-1]
    
sort = sorted(dt_counter.items(),key=hits,reverse=True)[:15]

date = []

hits = []

for item in sort:
    
  date.append(item[0])
  hits.append(item[1])
    
access_log.close()

plt.figure(figsize=(12, 7))
plt.xlabel("IP -->")
plt.ylabel("Number of Hits -->")
plt.title("Hits per IP")

plt.xticks(rotation=90)

x = date
y = hits


plt.bar(x, y, width = 0.3, color = ['red','green'])

plt.yticks(np.arange(0, 8000+250, 500))
 

plt.show()

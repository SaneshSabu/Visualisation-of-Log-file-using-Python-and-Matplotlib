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

plt.figure(figsize=(12,7))
plt.xlabel("Date -->")
plt.ylabel("Hits -->")
plt.title("Hits per Date")

plt.xticks(rotation=90)
x = date
y = hits


plt.plot(x, y, color = 'red')
plt.yticks(np.arange(min(y)+12, 8000+250, 250))
plt.show()


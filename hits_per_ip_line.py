import logparser
import numpy as np
from matplotlib import pyplot as plt

access_log = open("access.log","r")

counter = {}

for line in access_log:
    
  parsed = logparser.parser(line)

  if parsed['host'] not in counter:
        
    counter[parsed['host']] = 1
    
  else:
    
    counter[parsed['host']] = counter[parsed['host']] + 1
    
def hits(x):
    
  return x[-1]

sort = sorted(counter.items(),key=hits,reverse=True)[:15]


IPs = []
Hits = []

for item in sort:
    
  IPs.append(item[0])
  Hits.append(item[1])
    

plt.figure(figsize=(14,15))
plt.xlabel("IP -->")
plt.ylabel("Number of Hits -->")
plt.title("Hits per IP")

plt.xticks(rotation=90)
x = IPs
y = Hits


plt.plot(x, y, color = 'red')
plt.yticks(np.arange(0, 60000+2000, 2000))
plt.show()

  
access_log.close()

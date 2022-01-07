# FACILITIES AT CHC

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\chcf\TN_fchc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')			
pos = list(range(len(data['With functioning Stabilization Units for New Born']))) # setting position of the graphs
width = 0.2
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data['With functioning Stabilization Units for New Born'],width , alpha=0.5 , color='#ff99cc',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['With New Born Care Corner'],width,alpha = 0.5,color='#d5beff',label=data['year'][1])
autolabel(rect2)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('CHC facilities in Tamil Nadu across years')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, 100] )
plt.legend(['With functioning Stabilization Units for New Born', 'With New Born Care Corner'], loc='upper left')
plt.grid()
plt.show()
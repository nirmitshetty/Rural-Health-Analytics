# FACILITIES AT SUB CENTRES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\sc_facilities_statewise\HP_fsc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')			
pos = list(range(len(data['Without Regular Water Supply']))) # setting position of the graphs
width = 0.2
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data['Without Regular Water Supply'],width , alpha=0.5 , color='#ff99cc',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['Without Electric Supply'],width,alpha = 0.5,color='#d5beff',label=data['year'][1])
autolabel(rect2)
rect3 = plt.bar([p+width*2 for p in pos],data['Without All-Weather Motorable  Approach Road'],width,alpha=0.5,color='#9988cc',label=data['year'][2])
autolabel(rect3)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Sub Centre facilities in HP across years')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, 100] )
plt.legend(['Without Regular Water Supply', 'Without Electric Supply', 'Without All-Weather Motorable Approach Road'], loc='upper left')
plt.grid()
plt.show()
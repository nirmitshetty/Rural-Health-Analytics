# FACILITIES AT PHC

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\phcf\TRI_fphc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')			
pos = list(range(len(data['With Labour Room']))) # setting position of the graphs
width = 0.2
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data['With Labour Room'],width , alpha=0.5 , color='#ff99cc',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['With Operation Theatre'],width,alpha = 0.5,color='#d5beff',label=data['year'][1])
autolabel(rect2)
rect3 = plt.bar([p+width*2 for p in pos],data['With 4-6 Beds'],width,alpha=0.5,color='#9988cc',label=data['year'][2])
autolabel(rect3)
rect4 = plt.bar([p+width*3 for p in pos],data['With 24 Hrs. Delivery Facility'],width,alpha=0.5,color='#00aadd',label=data['year'][3])
autolabel(rect4)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('PHC facilities in Tripura across years')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, 100] )
plt.legend(['With Labour Room', 'With Operation Theatre', 'With 4-6 Beds','With 24 Hrs. Delivery Facility'], loc='best')
plt.grid()
plt.show()
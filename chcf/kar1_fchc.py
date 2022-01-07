# OTHER FACILITIES AT CHC

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\chcf\KAR_fchc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 0.95*height, '%d'%int(height),
                ha='center', va='bottom')			
pos = list(range(len(data['With all four specialists']))) # setting position of the graphs
width = 0.2
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data['With all four specialists'],width , alpha=0.5 , color='#ffd700',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['With functional O.T.'],width,alpha = 0.5,color='#469649',label=data['year'][1])
autolabel(rect2)
rect3 = plt.bar([p+width*2 for p in pos],data['With functional Labor Room'],width,alpha = 0.5,color='#b4eeb4',label=data['year'][2])
autolabel(rect3)
rect4 = plt.bar([p+width*3 for p in pos],data['With at least 30 beds'],width,alpha = 0.5,color='#bf1616',label=data['year'][3])
autolabel(rect4)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Other CHC facilities in Karnataka across years')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*6)
plt.ylim([0, 100] )
plt.legend(['With all four specialists', 'With functional O.T.','With functional Labor Room','With at least 30 beds'], loc='center')
plt.grid()
plt.show()
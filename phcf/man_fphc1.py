# OTHER FACILITIES AT PHC

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\phcf\MAN_fphc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')			
pos = list(range(len(data[' Without Electric Supply']))) # setting position of the graphs
width = 0.15
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data[' Without Electric Supply'],width , alpha=0.7 , color='#0e2f44',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['Without Regular Water Supply'],width,alpha = 0.5,color='#ff7f50',label=data['year'][1])
autolabel(rect2)
rect3 = plt.bar([p+width*2 for p in pos],data['Without AllWeather Motorable Approach Road'],width,alpha=0.5,color='#6897bb',label=data['year'][2])
autolabel(rect3)
rect4 = plt.bar([p+width*3 for p in pos],data['With Telephone'],width,alpha=0.5,color='#66cdaa',label=data['year'][3])
autolabel(rect4)
rect5 = plt.bar([p+width*4 for p in pos],data['With Computer'],width,alpha=0.5,color='#8b0000',label=data['year'][4])
autolabel(rect5)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('PHC facilities in Manipur across years')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*6)
plt.ylim([0, 100] )
plt.legend([' Without Electric Supply', 'Without Regular Water Supply', 'Without AllWeather Motorable Approach Road','With Telephone','With Computer'], loc='upper left')
plt.grid()
plt.show()
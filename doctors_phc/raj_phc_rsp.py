import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\doctors_phc\RAJ_rsp_phc.csv")#enter path here
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')		
pos = list(range(len(data['R']))) # setting position of the graphs
width = 0.25
fig, ax = plt.subplots(figsize=(10,5)) # plotting the graphs
rect1=plt.bar(pos,data['R'],width , alpha=0.5 , color='#EE3224',label=data['year'][0])
autolabel(rect1)
rect2 = plt.bar([p+width for p in pos],data['S'],width,alpha = 0.5,color='#FFC222',label=data['year'][1])
autolabel(rect2)
rect3 = plt.bar([p+width*2 for p in pos],data['P'],width,alpha=0.5,color='#F78F1E',label=data['year'][2])
autolabel(rect3)
ax.set_xlabel('Year')
ax.set_ylabel('No of doctors')
ax.set_title('Number of doctors in PHC in Rajasthan across years 2005-14')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(data['year'])
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(data['R'] + data['S'] + data['P'])] )
plt.legend(['Required', 'Sanctioned', 'InPosition'], loc='upper left')
plt.grid()
plt.show()
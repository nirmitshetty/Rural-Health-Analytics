import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("kanoe_project\death_statewise\INDIA_death.csv")#enter path here
year=data['Year']
death = data['death_rate']
rect = plt.bar(year,death,align='center')
plt.xlabel('Year')
plt.ylabel('DeathRate')
plt.title('DeathRate in India across years(2005-13)')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(float(rect.get_x())+float(rect.get_width()/2.), 1.05*float(height), '%d'%float(height),
                ha='center', va='bottom')
bar_width=0.35
plt.xticks(np.arange(min(year), max(year)+1, 1.0),('2005','2006','2007','2008','2009','2010','2011','2012','2013'),rotation='vertical')
autolabel(rect)
plt.grid(True)
plt.show()

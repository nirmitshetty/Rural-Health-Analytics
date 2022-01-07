import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\death_statewise\JHA_death.csv")#enter path here
death_rate = data['death_rate']
Shortfall = data['Shortfall']
plt.scatter(death_rate,Shortfall)
plt.xlabel('DeathRate')
plt.ylabel('Shortfall(R-P)')
plt.title('DeathRate VS Shortfall(2006-13)')
plt.grid(True)
plt.show()
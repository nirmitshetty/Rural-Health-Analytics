# MATERNAL MORTALITY RATIO VS YEAR

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:\Users\Nirmit\kanoe_project\mmr_statewise\WB_mmr.csv")#enter path here
df=pd.DataFrame({'Year': data['year'],
                 'MMR': data['mmr']})
df = df.set_index('Year')
ax = df.plot(kind='bar',  title='MMR in West Bengal across years')
ax.set_ylim(0, 400)
for i, label in enumerate(list(df.index)):
    score = df.ix[label]['MMR']
    ax.annotate(str(score), (i, score + 0.2))
plt.xlabel('Year')
plt.ylabel('MMR')
plt.grid()
plt.show()
import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('branch_data.xlsx')

#plt.style.use("ggplot")

fig, axes = plt.subplots(2, 2, figsize=(5, 5))


axes[0][0].scatter(df['BRANCH_ID'], df['TOT_CD_AC_MAY'])
axes[0][1].scatter(df['BRANCH_ID'], df['TOT_SB_AC_MAY'])
axes[1][0].scatter(df['BRANCH_ID'], df['TOT_CD_AMT_MAY'])
axes[1][1].scatter(df['BRANCH_ID'], df['TOT_SB_AMT_MAY'])

plt.tight_layout()

plt.show()

plt.close()

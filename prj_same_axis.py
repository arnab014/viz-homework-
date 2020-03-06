import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('branch_data.xlsx')

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# axes.scatter(df['alcohol'], df['total_phenols'], alpha=0.7, label='Total Phenols')


# axes.plot(df['BRANCH_ID'], df['TOT_CD_AC_MAY'],label='No Cost Deposit')
# axes.plot(df['BRANCH_ID'], df['TOT_SB_AC_MAY'],label='Low Cost Deposit')
# axes.plot(df['BRANCH_ID'], df['TOT_SND_AC_MAY'],label='High Cost Deposit')

axes.scatter(df['BRANCH_ID'], df['TOT_CD_AC_MAY'],alpha=0.9,marker='x',label='No Cost Deposit')
axes.scatter(df['BRANCH_ID'], df['TOT_SB_AC_MAY'],alpha=0.9,marker='x',label='Low Cost Deposit')
axes.scatter(df['BRANCH_ID'], df['TOT_SND_AC_MAY'],alpha=0.9,marker='x',label='High Cost Deposit')

axes.set_xlabel('Branch ID')
axes.set_ylabel('Total Number of Accounts')
axes.set_title(f'Branch wise Account Info')
axes.legend()

plt.tight_layout()

plt.show()

plt.close()

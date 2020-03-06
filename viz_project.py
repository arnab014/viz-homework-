import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('branch_data.xlsx')

#print(df)

os.makedirs('plots/br_data', exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            print(f'Generating {column1} to {column2} plot')
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/br_data/br_data_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()

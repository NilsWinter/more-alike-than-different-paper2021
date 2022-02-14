import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('../results/protect_ad/Contrast 0002/all/residuals.csv')

sns.histplot(data=df, hue='Group', x='residuals')

plt.show()

sns.boxplot(data=df, y='residuals', x='Group', orient='v')
plt.show()

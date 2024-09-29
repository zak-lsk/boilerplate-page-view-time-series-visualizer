import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

df = pd.read_csv("fcc-forum-pageviews.csv")

df.index = df['date']

lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)

df['date'] = pd.to_datetime(df['date'])
df = df[(df['value'] >= lower) & (df['value'] <= upper)]

plt.figure(figsize=(18, 6))
plt.plot(df['date'], df['value'], color='red')

# Etiquetas y título
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
plt.ylabel('Page Views')



plt.savefig('prueba.png')
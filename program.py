import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

df_pop = pd.read_csv('befolkning_stockholm.csv', sep=';')

# graf för folkmängd per ålder för 2000-2019
df_pop.plot(kind='line')
plt.ylabel('Folkmängd')
plt.xlabel('Ålder')
plt.show()

# scatter
fig, scat = plt.subplots(figsize=(8, 6))
scat.scatter(df_pop['år'], df_pop['2000'], df_pop['2010'], df_pop['2019'])
scat.set_xlabel('Ålder')
scat.set_ylabel('Folkmängd')
plt.show()

# heatmap
correlation_matrix = df_pop.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()

# förändringsmultipeln för de olika åldrarna från 2000-2019
data_div = df_pop['2019']/df_pop['2000']
data_div.plot(title='Förändringsmultipeln från 2000-2019', kind='bar')
plt.ylabel('Förändringsmultipel')
plt.xlabel('Ålder')
plt.show()

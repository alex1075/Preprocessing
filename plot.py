import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV = 'cell_locations.csv'

# Load the data
df = pd.read_csv(CSV)

# filter data and remove outliers
df = df[df['x'] > 0]
df = df[df['y'] > 0]
df = df[df['x'] < 3140]
df = df[df['y'] < 2100]


# set the size of the plot
fig, ax = plt.subplots()
fig.set_size_inches(16, 10)
# set boundaries of the plot
plt.xlim(0, 3140)
plt.ylim(0, 2100)

# set orgin of the plot to top left
ax.invert_yaxis()

# set x axis to the top
ax.xaxis.set_label_position('top')

# Plot the data
sns.scatterplot(x='x', y='y', data=df, s=0.5, ax=ax)



plt.savefig('cell_locations.png', bbox_inches='tight')
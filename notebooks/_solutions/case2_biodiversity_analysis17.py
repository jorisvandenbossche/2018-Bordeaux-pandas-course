heatmap_prep.index.name = 'year'
heatmap_prep.columns.name = 'month'

fig, ax = plt.subplots()
ax = sns.heatmap(heatmap_prep, cmap='Reds')
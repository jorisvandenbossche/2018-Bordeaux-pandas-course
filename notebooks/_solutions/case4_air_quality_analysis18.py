# with tidy long table
fig, ax = plt.subplots()
sns.violinplot(x='station', y='no2', data=data_tidy[data_tidy['datetime'].dt.year == 2011], palette="GnBu_d", ax=ax)
ax.set_ylabel("NO$_2$ concentration (µg/m³)")
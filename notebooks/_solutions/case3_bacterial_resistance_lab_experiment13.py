sns.barplot(x='Bacterial_genotype', y='optical_density', hue='Phage_t',
            data=density_mean[density_mean['experiment_time_h'] == 'OD_0h'])
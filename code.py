import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Chargement des données
df = pd.read_excel('/Users/paulsocheleau/Documents/stage/Stage_Paul/ANALYSE/06:08:2024/Plot_CT/Valeurs_microgliamorphologie.xlsx')

# Calcul des moyennes par condition et réplicat
df_means = df.groupby(['Conditions', 'Replica'])['Roundness'].mean().reset_index()

# Définition de l'ordre des catégories
order = ['mgl_dapi_iba1', 'mgl_ATP_dapi_iba1', 'AAV2 10^4', 'AAV2 10^5', 'AAV6 10^4', 'AAV6 10^5', 'AAV8 10^4', 'AAV8 10^5']
df_means['Conditions'] = pd.Categorical(df_means['Conditions'], categories=order, ordered=True)

# Graphique
plt.figure(figsize=(15,6))
ymin_val = (df['Roundness'].min(), df['Roundness'].max())
plt.ylim(ymin_val[0] - 1, ymin_val[1] + 1)

violinplot = sns.violinplot(x='Conditions', y='Roundness', data=df, inner="box", palette=None, scale='width')

# Ajouter les bordures noires aux violons
for violin in violinplot.collections:
    violin.set_edgecolor('black')
    violin.set_linewidth(3)

# Ajouter les points de moyenne des réplicats
sns.stripplot(
    x='Conditions',
    y='Roundness',
    hue='Replica',
    data=df_means,
    dodge=True,
    palette='pastel',
    size=10,
    marker='o',
    edgecolor='black',
    linewidth=1,
    alpha=0.8
)

# Afficher la légende
plt.legend(title='Réplicat', bbox_to_anchor=(1.05, 1), loc='upper left')

# Titre et étiquettes
plt.title('Violin Plot de la circularité des microglies en fonction des différents sérotypes de AAV à différentes concentrations', fontsize=1, fontweight='bold', color='black')
plt.xlabel('Microglia_phagocytosis')
plt.ylabel('Roundness')

plt.show()

# Courbe de densité
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Roundness', hue='Conditions', fill=True, alpha=0.3, bw_adjust=0.5)
plt.title('Courbe de Densité')
plt.xlabel('Roundness1')
plt.ylabel('Densité')

plt.show()






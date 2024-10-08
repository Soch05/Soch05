import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Chargement des données
df = pd.read_excel('/Users/paulsocheleau/Documents/stage/Stage_Paul/ANALYSE/mgl_06:08:2024/Plot_CT/Microglia_morphométrie.xlsx')

# Renommer les conditions
df['Conditions'] = df['Conditions'].replace({'mgl_dapi_iba1': 'CT', 'mgl_ATP_dapi_iba1': 'ATP'})

# Calcul des moyennes par condition et réplicat
df_means = df.groupby(['Conditions', 'Replica'])['Roundness'].mean().reset_index()

# Définition de l'ordre des catégories
order = ['CT', 'ATP']
df['Conditions'] = pd.Categorical(df['Conditions'], categories=order, ordered=True)
df_means['Conditions'] = pd.Categorical(df_means['Conditions'], categories=order, ordered=True)

# Graphique
plt.figure(figsize=(10,7))
ymin_val = (df['Roundness'].min(), df['Roundness'].max())
plt.ylim(ymin_val[0] - 1, ymin_val[1] + 1)

# Création du violon plot
violinplot = sns.violinplot(x='Conditions', y='Roundness', data=df, inner="box", palette=None, scale='width')

# Supprimer les bordures noires du cadre
sns.despine(left=False, bottom=False)

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

# Ajuster la légende pour qu'elle soit plus proche
plt.legend(title='Réplicat', bbox_to_anchor=(0.9, 0.9), loc='upper left')

# Titre et étiquettes
plt.title('Violin Plot de la circularité des microglies en fonction des différents sérotypes de AAV à différentes concentrations', fontsize=12, fontweight='bold', color='black')
plt.xlabel('CONDITIONS')
plt.ylabel('CIRCULARITÉ')

# Afficher le graphique
plt.show()



# Courbe de densité
plt.figure(figsize=(10, 6))

# Création du plot
sns.kdeplot(data=df, x='Roundness', hue='Conditions', fill=True, alpha=0.3, bw_adjust=0.5)

# Supprimer les bordures mais garder les axes (ticks)
sns.despine(left=False, bottom=False)

# Titre et étiquettes
plt.title('Courbe de Densité')
plt.xlabel('CIRCULARITÉ')
plt.ylabel('DENSITÉ')

# Afficher le graphique
plt.show()


import pandas as pd
import numpy as np
from scipy import stats



df = pd.read_excel('/Users/paulsocheleau/Documents/stage/Stage_Paul/ANALYSE/06:08:2024/Plot_CT/Valeurs_microgliamorphologie.xlsx')



# Séparer les données par groupe
condition_sans_atp = df[df['condition']=='sans_atp']['moyenne']
condition_avec_atp = df[df['condition']=='avec_atp']['moyenne']

# Appliquer la transformation logarithmique
condition_sans_atp_log = np.log(condition_sans_atp)
condition_avec_atp_log = np.log(condition_avec_atp)

# Effectuer le test t de Student sur les données transformées
t_stat, p_value = stats.ttest_ind(condition_sans_atp_log, condition_avec_atp_log)

# Afficher les résultats
print("\nRésultats du test t:")
print(f"T-statistique : {t_stat}")
print(f"Valeur p : {p_value}")

# Interprétation
alpha = 0.05
if p_value < alpha:
    print("\nConclusion: Les moyennes log-transformées des deux groupes sont significativement différentes.")
else:
    print("\nConclusion: Il n'y a pas de différence significative entre les moyennes log-transformées des deux groupes.")

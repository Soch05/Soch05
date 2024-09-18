import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Charger le fichier Excel
df = pd.read_excel('/Users/paulsocheleau/Documents/stage/Stage_Paul/ANALYSE/mgl_06:08:2024/Plot_CT/Microglia_morphométrie.xlsx')

# Séparer les données par groupe 'sans_atp' et 'avec_atp'
condition_sans_atp = df[df['condition'] == 'sans_atp']['moyenne']
condition_avec_atp = df[df['condition'] == 'avec_atp']['moyenne']

# Vérifier les valeurs minimales pour voir si la transformation logarithmique est possible
min_sans_atp = condition_sans_atp.min()
min_avec_atp = condition_avec_atp.min()

# Si les valeurs minimales sont positives, on applique la transformation logarithmique
if min_sans_atp > 0 and min_avec_atp > 0:
    # Appliquer la transformation logarithmique
    condition_sans_atp_log = np.log(condition_sans_atp)
    condition_avec_atp_log = np.log(condition_avec_atp)
    
    # Effectuer le test t de Student avec assumption d'inégalité des variances (Welch's t-test)
    t_stat, p_value = stats.ttest_ind(condition_sans_atp_log, condition_avec_atp_log, equal_var=False)
    
    # Afficher les résultats
    print("\nRésultats du test t avec transformation logarithmique :")
    print(f"T-statistique : {t_stat}")
    print(f"Valeur p : {p_value}")
    
    # Interprétation du résultat
    alpha = 0.05
    if p_value < alpha:
        print("\nConclusion: Les moyennes log-transformées des deux groupes sont significativement différentes.")
    else:
        print("\nConclusion: Il n'y a pas de différence significative entre les moyennes log-transformées des deux groupes.")
else:
    print("\nErreur : Les valeurs minimales ne permettent pas d'appliquer une transformation logarithmique. Vérifiez les données.")
    
# Visualisation des distributions des moyennes log-transformées (si applicable)
if min_sans_atp > 0 and min_avec_atp > 0:
    plt.hist(condition_sans_atp_log, alpha=0.5, label='Sans ATP (log)')
    plt.hist(condition_avec_atp_log, alpha=0.5, label='Avec ATP (log)')
    plt.legend(loc='upper right')
    plt.title('Distribution des moyennes log-transformées')
    plt.show()

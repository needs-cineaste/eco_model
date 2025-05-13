# ######################################################
Problématique
# ######################################################

    - Quel est l'évolution optimale du nucléaire historique ?
    - Quel est la sensibilité de l'évolution du parc historique en fonction du cout de grand carénage ? 

# ######################################################
TO DO 
# ######################################################

# Nucléaire historique

    - Chiffrer Grand carénage en fonction de hypothèse Nuke (=> Voir Annexe RTE)
    - Meilleure gestion Facteur de dispo
    - Rajouter PMin

# Nouveau nucléaire

    - Meilleure gestion Facteur de dispo 
    - P ne peut prendre que des valeurs type n * P_EPR ?
    - Créer deux nuke new. Un manoeuvrnant un autre quesi fixe
        => Faire une fonction dump ? 
    - Rajouter Pmin

# Interconnexion

    - Interconnexions (P exogène + E annuelle exogène = comme le ROR)
    - Warning -> Respecter les semaines types avec le profil interco associé

# Ecretement

    - Actuellement stocké dans var_EC
    - Quel prix doit-on implémenter pour var_EC ? 
    - Comment dispatcher l'écretement entre PV / WOF / WON

# Demande

    - Quel évolution de la demande ? 

    - Dans un second temps 
        - Prise en compte d'une certaine flexibilité de la demande
        - Par exemple, sensibilité du calcul de référence par rapport à un "applatissement" de la demande

# ENR

    - Synchroniser le WOF et le WON

# Cout de système

    - Cout de raccordement (ex : 1Md€/GW WOF - cf PNC conférence André Merlin)
    - Ajouter un cout réseau au ENR => Fonction de la Capa installée genre ccout de profil?

# Reserve de Capacité 

    - Intégrer les équations 

# Fonction objectif 

    - Prise en compte de la valeur résiduelle à la fin du scénario
    - Check prise en compte du facteur d'actualisation
        - Check s'il est correctement implémenté => doublon avec l'annualisation du capital ?
        - Possible de mettre un r variable en fonction de y ?

# STEP

    - Check cost Charge/Discharge (cf RTE)

# Output

    - Ajouter le prix de l'élec via cout marginal de la techno marginal
    - Ajouter le calcul du Levelized Cost of Mix Elec (€/MWh)
    - Ajouter le Lost Of Load (LOL)

# Technologies 

    - Biogaz => OK via prix gaz exogène
    - Hydrogène

# Calcul Monte Carlo ? 

# Electrolyseur ?     

    - Endogène en P + courbe d'apprentissage et voir type de technologie
    - Limité par la Capacité de production
    - Pas de limite en stock => output = masse d'H2


    

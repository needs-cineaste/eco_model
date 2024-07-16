TO DO 

- Ajouter Technos : 
    - Biogaz => OK via prix gaz exogène
    - Hydrogène
    - Interconnexions (P exogène + E annuelle exogène)

- Curtailment

- Data eco
    - Chiffrer Grand carénage en fonction de hypothèse Nuke (=> Voir Annexe RTE)
    - Ajouter le LCOE dans output
    - Ajouter LOL
    - Facteur d'actualisation 
        - Check s'il est correctement implémenté => doublon avec l'annualisation du capital ?
        - Possible de mettre un r variable en fonction de y ?
    - Check la valeur résiduelle
    - Check cost Charge/Discharge STEP

- Electrolyseur
    - Endogène en P + courbe d'apprentissage et voir type de technologie
    - Limité par la Capacité de production
    - Pas de limite en stock => output = masse d'H2

- Technique 
    - Nuke historique
        - Meilleure gestion Facteur de dispo
        - Rajouter PMin
    - Nuke New
        - Meilleure gestion Facteur de dispo 
        - P ne peut prendre que des valeurs type n * P_EPR
        - Créer deux nuke new. Un manoeuvrnant un autre quesi fixe => Faire une fonction dump ? 
        - Rajouter Pmin
    - Quel est le coût du compress pour le storage ??
    - Verifier l'algo reconstitution cout fix capex via le nucléaire historique

- Non chiffré dans les couts 
    - Raccordement ENR 
    
- Monte Carlo
    - Semaine type en fonction des années
    
    
    => Demande 10% de la demande journaliere
    => Nombre d'heure ou on peut moduler
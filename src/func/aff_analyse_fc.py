def aff_analyse_fc(dict_lf,weight_week_dict,type_energy) :
    dict1 = copy.deepcopy(dict_lf)

    year_number = random.randint(2020, 2050)
    average_week_values=[]
 
    for w in weeks :
        average_week_values+=[np.sum([dict1[(year_number,w,h)] for h in hours])/(168)]
 
 
    fig = go.Figure()
 
    # Ajouter le diagramme en barres
    fig.add_trace(go.Scatter(x=[i for i in weeks],y=average_week_values ,mode='lines',name="Moyenne hebdomadères"))
 
    fig.update_layout(
        title='Moyenne hebdomadaire du facteur de charge de ' + type_energy + ' pour l\'année '  + str(year_number),
        xaxis_title='Semaine de l\'année représentative',
        yaxis_title='Moyenne du facteur de charge'
    )
    fig.show()
    
     # 1. Extraire les données pour chaque année et calculer la consommation annuelle moyenne
    average_years_values=[]

    for y in years :
        average_years_values+=[np.sum([dict1[(y,w,h)]*weight_week_dict[w] for w in weeks for h in hours])/(52*168)]

 
    # 2. Calculer la moyenne totale de la consommation de 2020 à 2050
    total_average = np.mean(average_years_values) # 3. Calculer la moyenne totale de la consommation de 2020 à 2050
 
    # 3. Affichage
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in years],y=average_years_values ,mode='lines',name="Moyenne annuelle"))
 
    fig.add_trace(go.Scatter(x=[2020,2050] ,y=[total_average,total_average] , name="Moyenne totale", line=dict(color="Red", width=2, dash="dot")) )
 
    fig.update_layout(title="Facteurs de charge de " + str(type_energy) ,yaxis_title='Facteur de charge',xaxis_title="Années",
                      width=1000,height=500,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18), showlegend=True)
 
    fig.add_annotation(
    x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
    y=total_average*1.05,  # Position y de l'annotation
    xref="paper",  # Utilisation de l'échelle de l'axe x
    yref="y",  # Utilisation de l'échelle de l'axe y
    text="Moyenne totale " + str(round(total_average,3)),
    showarrow=False,
    font=dict(color="Red", size=12)
 )
 
    fig.show()
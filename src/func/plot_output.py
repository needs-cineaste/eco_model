fig_output = {}

################################################
# Plotting Production
################################################
key = 'production'
if Display_output[key] :

    fig_output[key] = go.Figure()
    
    for i,t in techno.items():
        if t.get_title()=='charge' :
            name = t.get_name() + ' ' + t.get_title()
            week = week_start
            year = year_start
            vals =[]
            x =[]
            for i in range(nombre_week_affichage):
                # Vérification et mise à jour de l'année si nécessaire
                if week > number_of_mean_weeks:
                    week = 1
                    year += 1
                # Ajout des valeurs et des axes x pour chaque semaine
                vals += [t.get_tech().get_E()[(year,week,h)] for h in hours]
                x += [h + i * 168 for h in hours]
                week += 1
            fig_output[key].add_trace(go.Scatter(x=x,y=vals,stackgroup='one',line=dict(width=0.2),name=name))
        
    for i,t in techno.items():
        if not t.get_title() == 'charge' :
            week = week_start
            year = year_start
            name = t.get_name() + ' ' + t.get_title()
            vals =[]
            x =[]
            for i in range(nombre_week_affichage) :
                # Vérification et mise à jour de l'année si nécessaire
                if week > number_of_mean_weeks:
                    week = 1
                    year += 1
                # Ajout des valeurs et des axes x pour chaque semaine
                vals += [t.get_tech().get_E()[(year,week,h)] for h in hours]
                x += [h + i * 168 for h in hours]
                week+=1
            fig_output[key].add_trace(go.Scatter(x=x,y=vals,stackgroup='one',line=dict(width=0.2),name=name))

    annotations_text=[]
    week = week_start
    year = year_start
    vals =[]
    x =[]
    ligneH=[]
    for i in range(nombre_week_affichage) :
        # Vérification et mise à jour de l'année si nécessaire
        if week > number_of_mean_weeks:
            week = 1
            year += 1
        vals += [demand_dict [(year,week,h)]for h in hours]
        x += [h + i * 168 for h in hours]
        # Ajout du texte de l'annotation pour l'axe x
        annotations_text.append(f"Y : {year}, W : {week}<br> Poids :198 {weight_week_dict[week]}")
        # Ajout de lignes horizontales en pointillé pour chaque semaine
        ligneH.append(dict(
            type="line",
            x0=i * 168,
            y0=100000 ,
            x1=i * 168,
            y1=0,
            xref='x',
            yref='y',
            line=dict(
                color="red",
                width=2,
                dash="dot",
            )))
        week+=1
    # Création des annotations pour l'axe x
    annotations = []
    for i, text in enumerate(annotations_text):
        annotations.append(
            dict(
                x=i * 168 + 84,
                y=-0.1,
                xref="x",
                yref="paper",
                text=text,
                showarrow=False,
                xanchor='center',
                font=dict(size=15)
            )
        )

    fig_output[key].add_trace(go.Scatter(x=x,y=vals,mode='lines',line=dict(width=2.0),opacity=0.50,name='Demand'))
    fig_output[key].update_layout(title=f"Optimal Mix - PRODUCTION",
                     yaxis_title='Production (MWh [1h step])',
                     xaxis_title=None,
                     #barmode='stack',
                     width=800,height=500,margin=dict(l=50,r=150,b=50,t=50),font=dict(size=18),annotations=annotations,
                    xaxis = dict(tickvals=[],ticktext=[],showticklabels=False),
                    shapes=ligneH)
    fig_output[key].show()
    fig_output[key].write_html(current_path + '/out/' + name_simulation + '/output' + '/' + key + '.html')

################################################
# Plotting Stock
################################################
key = 'stock'
if Display_output[key] :
    
    for i,t in techno.items() :
        is_storage = (t.get_type() == 'storage')
        titre = t.get_title()
        if is_storage and titre=='charge' :
            fig_output[key] = go.Figure()
            ligneH=[]
            week = week_start
            year = year_start
            vals = []
            x = []
            Stockage = t.get_spec().get_level()
            annotations_text= []
            # Boucle à travers chaque semaine restante
            for i in range(0, nombre_week_affichage):
                # Vérification et mise à jour de l'année si nécessaire
                if week > number_of_mean_weeks:
                    week = 1
                    year += 1
                # Ajout des valeurs et des axes x pour chaque semaine
                vals += [Stockage[year, week, h] for h in hours]
                x += [h + i * 168 for h in hours]
                # Ajout du texte de l'annotation pour l'axe x
                annotations_text.append(f" Y : {year}, W : {week}<br> Poids : {weight_week_dict[week]}")
                # Ajout de lignes horizontales en pointillé pour chaque semaine
                ligneH.append(dict(type="line",x0=i * 168,y0=500000 ,x1=i * 168,y1=0,xref='x',yref='y',line=dict(color="red",width=2,dash="dot")))
                week += 1
            # Ajout de la trace
            fig_output[key].add_trace(go.Scatter(x=x, y=vals, mode='lines', line=dict(width=2.0), opacity=0.50, name='Stockage'))
            # Création des annotations pour l'axe x
            annotations = []
            for i, text in enumerate(annotations_text):
                annotations.append(dict(x=i * 168 + 84,y=-0.1,xref="x",yref="paper",text=text,showarrow=False,xanchor='center',font=dict(size=15)))
            # Mise à jour du layout de la fig_output[key]ure
            fig_output[key].update_layout(
                title="Parc Optimal - STORAGE STEP",
                yaxis_title='Stock (MWh [1h step])',
                xaxis_title=None,
                xaxis = dict(tickvals=[],ticktext=[],showticklabels=False),
                #dict(
                 #   tickvals=[i * 168 + 84 for i in range(nombre_week_affichage)],
                  #  ticktext=annotations_text,tickangle=-90
                #),
                width=800,height=500,margin=dict(l=50, r=150, b=50, t=50),font=dict(size=18),
                annotations=annotations,shapes=ligneH
            )
            # Affichage de la fig_output[key]ure
            fig_output[key].show()
            fig_output[key].write_html(current_path + '/out/' + name_simulation + '/output' + '/' + key + '.html')

################################################
# Capacity evolution
################################################
key = 'capacity'
if Display_output[key] :

    fig_output[key] = go.Figure()
    for i,t in techno.items():
        name = t.get_name() + ' ' + t.get_title()
        x    = list(t.get_tech().get_P().keys())
        vals = list(t.get_tech().get_P().values())
        fig_output[key].add_trace(go.Scatter(x=x,y=vals,mode='lines',line=dict(width=2.0),name=name))
    fig_output[key].update_layout(title="Capacity",yaxis_title='MW',xaxis_title="",width=800,height=500,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
    # Add vertical line
    fig_output[key].add_shape(type='line',x0=start_of_scenario-1,y0=0,x1=start_of_scenario-1,y1=60e3,line=dict(color='Red', width=1.0, dash='dot'))

    
    fig_output[key].show()
    fig_output[key].write_html(current_path + '/out/' + name_simulation + '/output' + '/' + key + '.html')

############################################
# Mix electrique en Energie
###########################################
key = 'mix'
if Display_output[key] :

    # Initialiser la fig_output[key]ure
    fig_output[key] = go.Figure()
    # Calculer les valeurs totales pour chaque année
    total_per_year = {year: 0 for year in years}
    for year in years:
        for t in techno.values():
            vals_list = [t.get_tech().get_E()[(year, week, h)] for week in weeks for h in hours]
            total_per_year[year] += sum(vals_list)
    # Boucle sur les éléments du dictionnaire 'techno'
    for i, t in techno.items():
        if not t.get_type()=='storage' :
            name = t.get_name() + ' ' + t.get_title()
            x = [year for year in years]
            vals = []  # Initialiser 'vals' pour chaque 'name'
            for year in years:
                vals_list = [t.get_tech().get_E()[(year, week, h)] for week in weeks for h in hours]
                total_val = sum(vals_list)
                percentage_val = (total_val / total_per_year[year]) * 100  # Calculer le pourcentage
                vals.append(percentage_val)
            fig_output[key].add_trace(go.Bar(x=x, y=vals, name=name))
    # Mettre à jour le layout du diagramme
    fig_output[key].update_layout(
        title="Optimal Mix (%)",
        yaxis_title='Production (%)',
        xaxis_title='',
        barmode='stack',  # Empiler les barres
        width=800,height=500,
        margin=dict(l=50, r=150, b=50, t=50),
        font=dict(size=18),
        xaxis=dict(tickvals=list(years), ticktext=[str(year) for year in years], showticklabels=True)
    )
    # Afficher le diagramme
    fig_output[key].show()
    fig_output[key].write_html(current_path + '/out/' + name_simulation + '/output' + '/' + key + '.html')

############################################
# Mix electrique en Energie
###########################################
key = 'inv_dec_capa'
if Display_output[key] :
    n_of_hist_data_to_plot = 0
    for i,t in techno.items():
        if t.get_eco().is_cap() :
            n_of_hist_data_to_plot += 1
    fig_output[key] = make_subplots(cols=2,rows=n_of_hist_data_to_plot)
    n = 1
    fig_output[key] = make_subplots(cols=2,rows=n_of_hist_data_to_plot)
    for i,t in techno.items():
        if t.get_eco().is_cap() :
            historic_data_inv  = t.get_tech().get_Inv()
            historic_data_capa = t.get_tech().get_P()
            historic_data_dec = t.get_tech().get_Dec()
            name=t.get_name() + ' ' + t.get_title()
            x,y = list(historic_data_inv.keys()),list(historic_data_inv.values())
            fig_output[key].add_trace(go.Bar(name=name + " INV", x=x, y=y), col=1, row=n)
            x,y = list(historic_data_dec.keys()),[-historic_data_dec[y-1] for y in years]
            fig_output[key].add_trace(go.Bar(name=name + " DEC", x=x, y=y), col=1, row=n)
            x,y = list(historic_data_capa.keys()),list(historic_data_capa.values())
            fig_output[key].add_trace(go.Scatter(name=name + " CAPA", x=x, y=y), col=2, row=n)
            n += 1
    fig_output[key].update_layout(title_text="Investissement, Dec, Capa",
                          height=n_of_hist_data_to_plot*200, width=800,
                          margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
    fig_output[key].show()
    fig_output[key].write_html(current_path + '/out/' + name_simulation + '/output' + '/' + key + '.html')

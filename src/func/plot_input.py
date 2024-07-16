if plot_input:

    fig_input = {}
    
    ############# Demand #############
    # key = 'demand'
    # if Display_input['demand']:
    #
    #    demand_year = {}
    #    
    #    PRENDRE EN COPPTE LES SEMAINES REPRESENTATIVES
    #    for (y, w, h), value in demand_dict.items():
    #        if y in demand_year:
    #            demand_year[y] += value
    #        else:
    #            demand_year[y] = value
    #
    #    fig_input[key] = go.Figure()
    #    fig_input[key].add_trace(go.Scatter(x = list(demand_year.keys()) , y = list(demand_year.values()),line=dict(width=2.0),mode='lines',name=n))
    #
    #    fig_input[key].update_layout(title="Demand" ,yaxis_title='MW',
    #                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
    #    fig_input[key].show()
    
    # print()
        
    ############# Cout techno #############
    key = 'fix_costs'
    if Display_input[key] :
        fig_input[key] = go.Figure()
        for t in techno.keys():
            n = techno[t].get_name() + ' ' + techno[t].get_title()
            fig_input[key].add_trace(go.Scatter(x = list(years_world) , y = list(techno[t].get_eco().get_cost_profile_fix().values()),line=dict(width=2.0,shape='hv'),mode='lines',name=n))
        fig_input[key].update_layout(title="Fix Cost Evolution" ,yaxis_title='Total Cost [€/MW/y]',xaxis_title="years",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    key = 'tot_costs'
    if Display_input[key] :
        fig_input[key] = go.Figure()
        for t in techno.keys():
            U = np.arange(1, 8761, 1)
            n = techno[t].get_name() + ' ' + techno[t].get_title()
            # print(techno_d[tec].get_type())
            fig_input[key].add_trace(go.Scatter(x = U, y = techno[t].get_eco().get_cost_profile_tot(year),line=dict(width=2.0,shape='hv'),mode='lines',name=n))
        fig_input[key].update_layout(title="Total cost for the year - " + str(year) ,yaxis_title='Total Cost [€/MW/y]',xaxis_title="Use (h/y)",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ############# Historical Data #############
    
    key = 'hist_data'
    if Display_input[key] :
        n_of_hist_data_to_plot = 0
        for i,t in techno.items():
            historic_data_capa = t.get_tech().get_historic_data("CAPA")
            if not (historic_data_capa is None) and (not all(value == 0 for value in historic_data_capa.values())) :
                n_of_hist_data_to_plot += 1
    
        fig_input[key] = make_subplots(cols=2,rows=n_of_hist_data_to_plot)
        n = 1
        for i,t in techno.items():
            historic_data_inv  = t.get_tech().get_historic_data("INV")
            historic_data_capa = t.get_tech().get_historic_data("CAPA")
            name=t.get_name() + ' ' + t.get_title()
            
            if historic_data_capa is not None and isinstance(historic_data_capa, dict) and any(value != 0 for value in historic_data_capa.values()):
                x,y = list(historic_data_inv.keys()),list(historic_data_inv.values())
                fig_input[key].add_trace(go.Bar(name=name, x=x, y=y), col=1, row=n)
                x,y = list(historic_data_capa.keys()),list(historic_data_capa.values())
                fig_input[key].add_trace(go.Scatter(name=name, x=x, y=y), col=2, row=n)
                n += 1
    
        fig_input[key].update_layout(title_text="Historic data for : Investment | Capacity [MW]",
                          height=n_of_hist_data_to_plot*180, width=750,
                          margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
        fig_input[key].show()   
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ############# Carbon Trajectory #############
    
    key = 'carbon_cost'
    if Display_input[key] :
    
        fig_input[key] = go.Figure()
        for t in techno.keys():
            n = techno[t].get_name() + ' ' + techno[t].get_title()
            if re.match('gas', n):
                fig_input[key].add_trace(go.Scatter(x = list(years_world) , y = list(techno[t].get_eco().get_var_co2().values()),line=dict(width=2.0,shape='linear'),mode='lines',name=n))
        fig_input[key].update_layout(title="CO2",yaxis_title='CO2 Cost [€/MWh]',xaxis_title="year",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ############# Demande représentative #############
    
    key = 'week_demand'
    if Display_input[key]: 
        fig_input[key] = go.Figure()
        for index, row in demand_average.iterrows():
            fig_input[key].add_trace(go.Scatter(x=demand_average.columns,y=row,mode='lines',name=f'week {index}'))
     
        fig_input[key].update_layout(title="year - " + str(year),yaxis_title='Demand (MW)',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
     
        fig_input[key].show()   
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ############# PV #############
    
    key = 'week_pv'
    if Display_input[key] :
        fig_input[key] = go.Figure()
        for index, row in pv_lf_new.iterrows():
            fig_input[key].add_trace(go.Scatter(x=pv_lf_new.columns,y=row,mode='lines',name=f'week {index}'))
     
        fig_input[key].update_layout(title="year - " + str(year),yaxis_title='Load Factor PV',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
     
        fig_input[key].show()   
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ################# Eolien Offshore ################
    
    key = 'week_wof'
    if Display_input[key] :
    
        fig_input[key] = go.Figure()
        for index, row in wof_lf_new.iterrows():
            fig_input[key].add_trace(go.Scatter(x=wof_lf_new.columns,y=row,mode='lines',name=f'week {index}'))
     
        fig_input[key].update_layout(title="year - " + str(year),yaxis_title='Load Factor WOFF',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
     
        fig_input[key].show()   
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ############## Eolien On shore #############
    
    key = 'week_won'
    if Display_input[key] :
        fig_input[key] = go.Figure()
        for index, row in won_lf_new.iterrows():
            fig_input[key].add_trace(go.Scatter(x=won_lf_new.columns,y=row,mode='lines',name=f'week {index}'))
     
        fig_input[key].update_layout(title="year - " + str(year),yaxis_title='Load Factor WON',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15))
     
        fig_input[key].show()   
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ################# Analyse de la moyenne du FC de éolien off shore et onshore sur l'ensemble de la modélisation ###########
    
    key = 'load_factor_total'
    if Display_input[key] :
     
        aff_analyse_fc(dict_won_lf,weight_week_dict,'EOLIEN ONSHORE')
        aff_analyse_fc(dict_wof_lf,weight_week_dict,'EOLIEN OFFSHORE')
        aff_analyse_fc(dict_pv_lf,weight_week_dict,'PV')
        aff_analyse_fc(dict_lake_lf,weight_week_dict,'LAKE')
        aff_analyse_fc(dict_ror_lf,weight_week_dict,'ROR')
        
    key = 'load_factor_data'
    if Display_input[key] :
        won_lf_weekmean=won_lf_reshape.mean(axis=1)
        won_lf_yearmean=won_lf_weekmean.mean()
     
        wof_lf_weekmean=wof_lf_reshape.mean(axis=1)
        wof_lf_yearmean=wof_lf_weekmean.mean()
     
        pv_lf_weekmean=pv_lf_reshape.mean(axis=1)
        pv_lf_yearmean=pv_lf_weekmean.mean()
     
    
        ##"##### Eolien Onshore ### 
     
        fig_input[key] = go.Figure()
        fig_input[key].add_trace(go.Scatter(x=[i for i in range(1,52)],y=np.array(won_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
     
        fig_input[key].add_trace(go.Scatter(x=[0,52] ,y=[won_lf_yearmean,won_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
     
        fig_input[key].update_layout(title="Données d'entrée : des facteurs de charge de l'éolien onshore" ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15), showlegend=True)
        fig_input[key].add_annotation(
        x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
        y=won_lf_yearmean*1.05,  # Position y de l'annotation
        xref="paper",  # Utilisation de l'échelle de l'axe x
        yref="y",  # Utilisation de l'échelle de l'axe y
        text="Moyenne annuelle " + str(round(won_lf_yearmean,4)),
        showarrow=False,
        font=dict(color="Red", size=12))
    
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
        ##### Eolien Offshore ## 
     
        fig_input[key] = go.Figure()
        fig_input[key].add_trace(go.Scatter(x=[i for i in range(1,52)],y=np.array(wof_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
     
        fig_input[key].add_trace(go.Scatter(x=[0,52] ,y=[wof_lf_yearmean,wof_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
     
        fig_input[key].update_layout(title="Données d'entrée : des facteurs de charge de l'EOLIEN OFFSHORE " ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15), showlegend=True)
        fig_input[key].add_annotation(
        x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
        y=wof_lf_yearmean*1.05,  # Position y de l'annotation
        xref="paper",  # Utilisation de l'échelle de l'axe x
        yref="y",  # Utilisation de l'échelle de l'axe y
        text="Moyenne annuelle " + str(round(wof_lf_yearmean,4)),
        showarrow=False,
        font=dict(color="Red", size=12))
    
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
    
    ##### Eolien Onshore ## 
    
        fig_input[key] = go.Figure()
        fig_input[key].add_trace(go.Scatter(x=[i for i in range(1,len(pv_lf_weekmean))],y=np.array(pv_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
     
        fig_input[key].add_trace(go.Scatter(x=[0,len(pv_lf_weekmean)] ,y=[pv_lf_yearmean,pv_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
     
        fig_input[key].update_layout(title="Données d'entrée : des facteurs de charge du PV " ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15), showlegend=True)
        fig_input[key].add_annotation(
        x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
        y=pv_lf_yearmean*1.05,  # Position y de l'annotation
        xref="paper",  # Utilisation de l'échelle de l'axe x
        yref="y",  # Utilisation de l'échelle de l'axe y
        text="Moyenne annuelle " + str(round(pv_lf_yearmean,4)),
        showarrow=False,
        font=dict(color="Red", size=12))
     
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
        
    ################# Nuclear Historic ###########
    
    key = 'nuclear_hist'
    if Display_input[key] :
    
        fig_input[key] = go.Figure()
    
        for col in filtered_df.columns[1:]:
            fig_input[key].add_trace(go.Scatter(x=filtered_df['Year'],y=filtered_df[col],mode='lines',name='nuclear ' + col))
    
        fig_input[key].update_layout(title='Capacity of nuclear historic', yaxis_title='MW',xaxis_title='',
                          width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=15), showlegend=True)
        fig_input[key].show()
        fig_input[key].write_html(current_path + '/out/' + name_simulation + '/input' + '/' + key + '.html')
        
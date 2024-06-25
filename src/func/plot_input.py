############# Cout techno #############
if Display_input['cout_techno_fix'] :
    fig = go.Figure()
    for t in techno.keys():
        n = techno[t].get_name() + ' ' + techno[t].get_title()
        fig.add_trace(go.Scatter(x = list(years_world) , y = list(techno[t].get_eco().get_cost_profile_fix().values()),line=dict(width=2.0,shape='hv'),mode='lines',name=n))
    fig.update_layout(title="Evolution des coûts fixes par techno" ,yaxis_title='Total Cost [€/MW/y]',xaxis_title="years",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
    fig.show()

print()

if Display_input['cout_techno_tot'] :
    fig = go.Figure()
    for t in techno.keys():
        U = np.arange(1, 8761, 1)
        n = techno[t].get_name() + ' ' + techno[t].get_title()
        # print(techno_d[tec].get_type())
        fig.add_trace(go.Scatter(x = U, y = techno[t].get_eco().get_cost_profile_tot(year),line=dict(width=2.0,shape='hv'),mode='lines',name=n))
    fig.update_layout(title="Cout total par techno pour l'année - " + str(year) ,yaxis_title='Total Cost [€/MW/y]',xaxis_title="Use (h/y)",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
    fig.show()

print()

############# Carbon Trajectory #############

if Display_input['carbon cost'] :

    fig = go.Figure()
    for t in techno.keys():
        n = techno[t].get_name() + ' ' + techno[t].get_title()
        if re.match('gas', n):
            fig.add_trace(go.Scatter(x = list(years_world) , y = list(techno[t].get_eco().get_var_co2().values()),line=dict(width=2.0,shape='linear'),mode='lines',name=n))
    fig.update_layout(title="CO2",yaxis_title='CO2 Cost [€/MWh]',xaxis_title="year",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
    fig.show()

print()


############# Demande représentative #############

if Display_input['week_repr_demand']: 
    fig = go.Figure()
    for index, row in demand_average.iterrows():
        fig.add_trace(go.Scatter(x=demand_average.columns,y=row,mode='lines',name=f'week {index}'))
 
    fig.update_layout(title="année : " + str(year),yaxis_title='Demand (MW)',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
 
    fig.show()   

############# PV #############

if Display_input['week_repr_pv'] : 
    fig = go.Figure()
    for index, row in pv_lf_random.iterrows():
        fig.add_trace(go.Scatter(x=pv_lf_random.columns,y=row,mode='lines',name=f'week {index}'))
 
    fig.update_layout(title="année : " + str(year),yaxis_title='Facteur de charge PV',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                      width=1000,height= 500,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
 
    fig.show()   

################# Eolien Offshore ################

if Display_input['week_repr_wof'] :

    fig = go.Figure()
    for index, row in wof_lf_random.iterrows():
        fig.add_trace(go.Scatter(x=wof_lf_random.columns,y=row,mode='lines',name=f'week {index}'))
 
    fig.update_layout(title="année : " + str(year),yaxis_title='Facteur de charge eolien offshore',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
 
    fig.show()   


############## Eolien On shore #############

if Display_input['week_repr_won'] :
    fig = go.Figure()
    for index, row in won_lf_random.iterrows():
        fig.add_trace(go.Scatter(x=won_lf_random.columns,y=row,mode='lines',name=f'week {index}'))
 
    fig.update_layout(title="année : " + str(year),yaxis_title='Facteur de charge eolien onshore',xaxis_title=f"hour for {number_of_mean_weeks} weeks",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
 
    fig.show()   



################# Analyse de la moyenne du FC de éolien off shore et onshore sur l'ensemble de la modélisation ###########

if Display_input['analyse_FC_total'] : 
 
    aff_analyse_fc(dict_won_lf,weight_week_dict,'EOLIEN ONSHORE')
    aff_analyse_fc(dict_wof_lf,weight_week_dict,'EOLIEN OFFSHORE')
    aff_analyse_fc(dict_pv_lf,weight_week_dict,'PV')
    aff_analyse_fc(dict_lake_lf,weight_week_dict,'LAKE')
    aff_analyse_fc(dict_ror_lf,weight_week_dict,'ROR')
    
if Display_input['analyse_fc_data'] : 
    won_lf_weekmean=won_lf_reshape.mean(axis=1)
    won_lf_yearmean=won_lf_weekmean.mean()
 
    wof_lf_weekmean=wof_lf_reshape.mean(axis=1)
    wof_lf_yearmean=wof_lf_weekmean.mean()
 
    pv_lf_weekmean=pv_lf_reshape.mean(axis=1)
    pv_lf_yearmean=pv_lf_weekmean.mean()
 

    ##"##### Eolien Onshore ### 
 
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(1,52)],y=np.array(won_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
 
    fig.add_trace(go.Scatter(x=[0,52] ,y=[won_lf_yearmean,won_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
 
    fig.update_layout(title="Données d'entrée : des facteurs de charge de l'éolien onshore" ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18), showlegend=True)
    fig.add_annotation(
    x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
    y=won_lf_yearmean*1.05,  # Position y de l'annotation
    xref="paper",  # Utilisation de l'échelle de l'axe x
    yref="y",  # Utilisation de l'échelle de l'axe y
    text="Moyenne annuelle " + str(round(won_lf_yearmean,4)),
    showarrow=False,
    font=dict(color="Red", size=12))

    fig.show()
 
    ##### Eolien Onshore ## 
 
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(1,52)],y=np.array(wof_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
 
    fig.add_trace(go.Scatter(x=[0,52] ,y=[wof_lf_yearmean,wof_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
 
    fig.update_layout(title="Données d'entrée : des facteurs de charge de l'EOLIEN OFFSHORE " ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18), showlegend=True)
    fig.add_annotation(
    x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
    y=wof_lf_yearmean*1.05,  # Position y de l'annotation
    xref="paper",  # Utilisation de l'échelle de l'axe x
    yref="y",  # Utilisation de l'échelle de l'axe y
    text="Moyenne annuelle " + str(round(wof_lf_yearmean,4)),
    showarrow=False,
    font=dict(color="Red", size=12))

    fig.show()

##### Eolien Onshore ## 

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(1,len(pv_lf_weekmean))],y=np.array(pv_lf_weekmean),mode='lines',name="Moyenne hebdomadaire"))
 
    fig.add_trace(go.Scatter(x=[0,len(pv_lf_weekmean)] ,y=[pv_lf_yearmean,pv_lf_yearmean] , name="moyenne annuelle", line=dict(color="Red", width=2, dash="dot")) ) 
 
    fig.update_layout(title="Données d'entrée : des facteurs de charge du PV " ,yaxis_title='Facteur de charge',xaxis_title="Semaine",
                      width=750,height=350,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18), showlegend=True)
    fig.add_annotation(
    x=0.5,  # Position x de l'annotation (en coordonnées relatives, 0.5 est au milieu de l'axe x)
    y=pv_lf_yearmean*1.05,  # Position y de l'annotation
    xref="paper",  # Utilisation de l'échelle de l'axe x
    yref="y",  # Utilisation de l'échelle de l'axe y
    text="Moyenne annuelle " + str(round(pv_lf_yearmean,4)),
    showarrow=False,
    font=dict(color="Red", size=12))
 
    fig.show()
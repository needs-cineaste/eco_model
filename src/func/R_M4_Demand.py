# Oopen class room clustering
# voir https://openclassrooms.com/fr/courses/4379436-explorez-vos-donnees-avec-des-algorithme[…]z-vos-donnees-avec-un-algorithme-de-clustering-hierarchique

def clustering_upgma(dem):
    dem=dem.to_numpy()
    nb_dem, nb_heures = dem.shape
    index_cluster=np.arange(52)
    index=51
    Z=[] 
    L=[]
    for i in range(52) :
        L+=[[i]]
 
    for i in range(51) : 
        similarite = []
        nb_dem, nb_heures = dem.shape
        for j in range(len(L)-1):
 
            index_cluster_theorique=L[j]+ L[j+1]
            moy_cluster=np.array([])
 
            Matrice_cluster_therorique=[]
            for i in index_cluster_theorique :
                Matrice_cluster_therorique=Matrice_cluster_therorique + [dem[i]]
 
            moy_cluster=np.mean(Matrice_cluster_therorique, axis=0)
 
            moy_distance=0
            for i in index_cluster_theorique : 
                moy_distance += np.linalg.norm(dem[i] - moy_cluster)
 
            moy_distance=moy_distance/len(index_cluster_theorique)
 
            similarite.append(moy_distance)
 
        index_min=np.argmin(similarite)
 
 
        index+=1
 
        index_a=index_cluster[index_min]
        index_b=index_cluster[index_min+1]
 
        index_cluster=np.delete(index_cluster,index_min,axis=0)
        index_cluster=np.delete(index_cluster,index_min,axis=0)
 
        index_cluster=np.insert(index_cluster,index_min,index)
 
        La=L.pop(index_min)
        Lb=L.pop(index_min)
 
        Lfusion=La+Lb
 
        L_before = L[:index_min]
        L_after = L[index_min:]
 
        L.insert(index_min,Lfusion)
 
        Z.append([index_a,index_b,similarite[index_min],len(Lfusion)])
    return(Z)

def R_M4_Demand(number_of_mean_weeks, dem,print_info=True):

    Z=clustering_upgma(dem)
 
    t= 52 - number_of_mean_weeks
 
    groups=fcluster(Z, number_of_mean_weeks, criterion='maxclust')
 
    distance=np.array(Z)[:,2]
 
    element=groups[0]
    group_reindexed=[0]
 
    for i in range(1,len(groups)) :
        if element==groups[i] : 
            group_reindexed+=[group_reindexed[i-1]]
        else : 
            element=groups[i]
            group_reindexed+=[group_reindexed[i-1]+1]
 
    if print_info : 
 
        #Affichage du dendrogramme
        plt.figure(figsize=(10, 5))
        plt.title('Dendrogramme CAH')
        dendrogram(np.array(Z))
        plt.xlabel('dem')
        plt.ylabel('Distance')
 
        plt.axhline(y=Z[52-1-number_of_mean_weeks][2], color='r', linestyle='--',
                    label=f"seuil pour {number_of_mean_weeks} dem réprésentatives")
        plt.legend()
        plt.show()
 
 
        #Figure distance - nombre de semaine représentative
        fig = go.Figure()
        fig.add_trace(go.Scatter(x= np.arange(51,0,-1), y=distance,mode='lines'))
        fig.add_vline(x=number_of_mean_weeks, line_dash='dash', line_color='red',
                      annotation_text=f"{number_of_mean_weeks} dem réprésentatives", annotation_position='top')
 
        fig.update_layout(title="Analyse distance/nombre de dem représentatifs", yaxis_title='Distance de la dernière fusion',
                          xaxis_title="Nombre de dem représentatifs",
                    width=1000,height=500,margin=dict(l=50,r=150,b=30,t=50),font=dict(size=18))
 
        fig.show()   
 
 
        print("Les regroupements de dem avec " + str(number_of_mean_weeks) + " dem représentatives se font suivant : " + str(group_reindexed))
 
 
 
    return np.array(group_reindexed)



removal_rates1=sorted(list([1/j for j in range(1,11)]),reverse=False) # [:-1]

### one plot for hubs first protocol (for initial graph)

# для исходного графа


### art pts

list_of_art_perc_and_rem_fr_for_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=gg28917_cp,
                           removal_rates=removal_rates1)


art_pts_df_for_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



# for legend
#plt.title('''Сhange the ratio of articulation points as the vertices are removed for initial graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''')


### mcc

perc_mcc_list_for_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=gg28917_cp, \
                          removal_rates=removal_rates1)


mcc_df_for_init_g=pd.DataFrame(perc_mcc_list_for_init_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])


# for legend
# plt.title('''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (hubs first protocol)''')


## после удаления вершин степени 1


gg28917_cp2=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in dict(gg28917_cp2.degree()).items() if degree ==1]
gg28917_cp2.remove_nodes_from(vert_with_deg1)



### art pts

list_of_art_perc_and_rem_fr_for_filt_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=gg28917_cp2,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])

# plt.title('Percolation transition for random internet g bef rem vertices with deg 1 (with % of art pts by vertical axis)')
# plt.ylabel('num of art pts')

# for legend

# plt.title('''Сhange the ratio of articulation points as the vertices are removed for initial 
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''')



### mcc

perc_mcc_list_for_filt_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=gg28917_cp2, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_init_g=pd.DataFrame(perc_mcc_list_for_filt_init_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])





import seaborn as sns
fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('MCC and articulation points curves for initial graph (hubs first protocol)', fontsize=19, fontweight='bold')


dfs_to_plot=[art_pts_df_for_init_g, art_pts_df_for_filt_init_g, mcc_df_for_init_g, mcc_df_for_filt_init_g]

colors=['olive', 'green','red', 'darkred']
styles = ['-', '--', '-', '--']

legends=['''Сhange the ratio of articulation points as the vertices are removed for initial graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis)''', 
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial 
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis)''',
        '''Сhange the ratio of nodes in MCC as the vertices are removed for 
# initial graph after remove vertices with degree 1 (with % of nodes in MCC by vertical axis)'''
        ]

iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)
#for i in range(4):
    
#    dfs_to_plot[i].plot(color=next(iterable_color), legend=legends[i])
    #ax.plot(*(x, y) = (data_to_plot[i]),
    #                 styles[i], color='black')
#ax.axis('equal')

# ax.
import seaborn as sns

# 
sns.lineplot(data=dfs_to_plot[0], x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for initial graph (hubs first protocol)')
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for initial graph after remove vertices with degree 1 (hubs first protocol)')
#plt.plot(x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color))

#plt.legend([next(iterable_legends), next(iterable_legends), 
#            next(iterable_legends), next(iterable_legends)], bbox_to_anchor=(1, 1), loc='upper left')
plt.legend()


### для графа ER (hubs first )

n = 81145 # 10 nodes
m = 123822  # 20 edges
seed = 20160  # seed random number generators for reproducibility
# Use seed for reproducibility
erdos_renyi_g = nx.gnm_random_graph(n, m, seed=seed)


erdos_renyi_g_cp=erdos_renyi_g.copy()

### art pts



list_of_art_perc_and_rem_fr_for_er_g=\
hubs_first_with_perc_of_art_pts_0411(network=erdos_renyi_g_cp,
                           removal_rates=removal_rates1)


art_pts_df_for_er_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_er_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



# for legend
#plt.title('''Сhange the ratio of articulation points as the vertices are removed for ER graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis)''')


### mcc

perc_mcc_list_for_er_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=erdos_renyi_g_cp, \
                          removal_rates=removal_rates1)


mcc_df_for_er_g=pd.DataFrame(perc_mcc_list_for_er_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])


# for legend
# plt.title('''Сhange the ratio of nodes in mcc as the vertices are removed for ER graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis)''')


## после удаления вершин степени 1


er_g_to_filt=erdos_renyi_g_cp.copy()
nodes_with_deg1=[node for node, degree in dict(er_g_to_filt.degree()).items() if degree==1]

er_g_to_filt.remove_nodes_from(nodes_with_deg1)

filt_er_g=er_g_to_filt.copy()


### art pts

list_of_art_perc_and_rem_fr_for_filt_er_g=\
hubs_first_with_perc_of_art_pts_0411(network=filt_er_g,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_er_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_er_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])

# plt.title('Percolation transition for random internet g bef rem vertices with deg 1 (with % of art pts by vertical axis)')
# plt.ylabel('num of art pts')

# for legend

# plt.title('''Сhange the ratio of articulation points as the vertices are removed for initial 
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''')



### mcc

perc_mcc_list_for_filt_er_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=filt_er_g, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_er_g=pd.DataFrame(perc_mcc_list_for_filt_er_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])





import seaborn as sns
fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('MCC and articulation points curves for ER graph (hubs first protocol)', fontsize=19, fontweight='bold')


dfs_to_plot=[art_pts_df_for_er_g, art_pts_df_for_filt_er_g, mcc_df_for_er_g, mcc_df_for_filt_er_g]

colors=['olive', 'green','red', 'darkred']
styles = ['-', '--', '-', '--']

legends=['''Сhange the ratio of articulation points as the vertices are removed for ER graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis)''', 
        '''Сhange the ratio of nodes in mcc as the vertices are removed for ER graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis)''',
            '''Сhange the ratio of articulation points as the vertices are removed for ER 
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis)''',
        '''Сhange the ratio of nodes in MCC as the vertices are removed for 
# ER graph after remove vertices with degree 1 (with % of nodes in MCC by vertical axis)'''
        ]

iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)
#for i in range(4):
    
#    dfs_to_plot[i].plot(color=next(iterable_color), legend=legends[i])
    #ax.plot(*(x, y) = (data_to_plot[i]),
    #                 styles[i], color='black')
#ax.axis('equal')

# ax.
import seaborn as sns

# 
sns.lineplot(data=dfs_to_plot[0], x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for ER graph')
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for ER graph after remove vertices with degree 1')
#plt.plot(x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color))

#plt.legend([next(iterable_legends), next(iterable_legends), 
#            next(iterable_legends), next(iterable_legends)], bbox_to_anchor=(1, 1), loc='upper left')
plt.legend()



### для графа power law (hubs first)




exp_ks = [2.6]

power_law_net=get_power_law_net(n_nodes=81145, k=2.5, verbose=False)


power_law_net_cp=power_law_net.copy()

### art pts



list_of_art_perc_and_rem_fr_for_pl_g=\
hubs_first_with_perc_of_art_pts_0411(network=power_law_net_cp,
                           removal_rates=removal_rates1)


art_pts_df_for_pl_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_pl_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



# for legend
#plt.title('''Сhange the ratio of articulation points as the vertices are removed for power law graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis)''')


### mcc

perc_mcc_list_for_pl_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=power_law_net_cp, \
                          removal_rates=removal_rates1)


mcc_df_for_pl_g=pd.DataFrame(perc_mcc_list_for_pl_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])


# for legend
# plt.title('''Сhange the ratio of nodes in mcc as the vertices are removed for power law graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis)''')


## после удаления вершин степени 1


## после удаления вершин степени 1

pl_g_to_filt=power_law_net_cp.copy()
nodes_with_deg1=[node for node,degree in dict(pl_g_to_filt.degree()).items() if degree==1]

pl_g_to_filt.remove_nodes_from(nodes_with_deg1)

filt_pl_g=pl_g_to_filt.copy()


### art pts

list_of_art_perc_and_rem_fr_for_filt_er_g=\
hubs_first_with_perc_of_art_pts_0411(network=filt_pl_g,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_pl_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_pl_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



# for legend

# plt.title('''Сhange the ratio of articulation points as the vertices are removed for power law
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis)''')



### mcc

perc_mcc_list_for_filt_pl_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=filt_pl_g, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_pl_g=pd.DataFrame(perc_mcc_list_for_filt_pl_g, columns=['p (fraction of removed nodes)', 'fraction of nodes in MCC'])





import seaborn as sns
fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('MCC and articulation points curves for power law graph (hubs first protocol)', fontsize=19, fontweight='bold')


dfs_to_plot=[art_pts_df_for_pl_g, art_pts_df_for_filt_pl_g, mcc_df_for_pl_g, mcc_df_for_filt_pl_g]

colors=['olive', 'green','red', 'darkred']
styles = ['-', '--', '-', '--']

legends=['''Сhange the ratio of articulation points as the vertices are removed for power law graph before
#remove vertices with degree 1 (with % of articulation points by vertical axis)''', 
        '''Сhange the ratio of nodes in mcc as the vertices are removed for power law graph before
# remove vertices with degree 1 (with % of nodes in MCC by vertical axis)''',
            '''Сhange the ratio of articulation points as the vertices are removed for power law 
# graph after remove vertices with degree 1 (with % of articulation points by vertical axis)''',
        '''Сhange the ratio of nodes in MCC as the vertices are removed for 
# power law graph after remove vertices with degree 1 (with % of nodes in MCC by vertical axis)'''
        ]

iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)
#for i in range(4):
    
#    dfs_to_plot[i].plot(color=next(iterable_color), legend=legends[i])
    #ax.plot(*(x, y) = (data_to_plot[i]),
    #                 styles[i], color='black')
#ax.axis('equal')

# ax.
import seaborn as sns

# 
sns.lineplot(data=dfs_to_plot[0], x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for power law graph')
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('Nodes in MCC and articulation points percentage curves for power law graph after remove vertices with degree 1')
#plt.plot(x=dfs_to_plot[0].iloc[:,0], y=dfs_to_plot[0].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[1].iloc[:,0], y=dfs_to_plot[1].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[2].iloc[:,0], y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color))
#plt.plot(x=dfs_to_plot[3].iloc[:,0], y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color))

#plt.legend([next(iterable_legends), next(iterable_legends), 
#            next(iterable_legends), next(iterable_legends)], bbox_to_anchor=(1, 1), loc='upper left')
plt.legend()
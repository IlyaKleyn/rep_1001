


# # Initial graph, hubs first protocol, art pts


removal_rates1=sorted(list([1/j for j in range(1,11)]),reverse=False) # [:-1]


# до удаления вершин степени 1

list_of_art_perc_and_rem_fr_for_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=gg28917_cp,
                           removal_rates=removal_rates1)


art_pts_df_for_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])


## после удаления вершин степени 1


gg28917_cp2=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in dict(gg28917_cp2.degree()).items() if degree ==1]
gg28917_cp2.remove_nodes_from(vert_with_deg1)




list_of_art_perc_and_rem_fr_for_filt_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=gg28917_cp2,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])

## init gr, small degree, art pts


## до фильтрации

list_of_art_perc_and_rem_fr_for_init_g_small_dp=\
small_deg_first_with_perc_of_art_pts_0411(network=gg28917_cp,
                           removal_rates=removal_rates1)


art_pts_df_for_init_g_small_dp=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_init_g_small_dp, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



## после удаления вершин степени 1


gg28917_cp_small_dp=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in
                  dict(gg28917_cp_small_dp.degree()).items()
                  if degree ==1]
gg28917_cp_small_dp.remove_nodes_from(vert_with_deg1)





list_of_art_perc_and_rem_fr_for_filt_init_g_small_dp=\
small_deg_first_with_perc_of_art_pts_0411(network=
                           gg28917_cp_small_dp,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_init_g_small_dp=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_init_g_small_dp, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])


## init gr,  random protocol, art pts


import random as rn


list_of_art_perc_and_rem_fr_for_init_g_rnd_p=\
random_art_pts_perc_change_0411(network=gg28917_cp,
                           removal_rates=removal_rates1)


art_pts_df_f_init_g_rnd_p=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_init_g_rnd_p, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



### после удаления из исх -го графа вершин со степ - ю 1

gg28917_cp_rnd_p=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in
                  dict(gg28917_cp_rnd_p.degree()).items()
                  if degree ==1]
gg28917_cp_rnd_p.remove_nodes_from(vert_with_deg1)





list_of_art_perc_and_rem_fr_for_filt_init_g_rnd_p=\
random_art_pts_perc_change_0411(network=gg28917_cp_rnd_p,
                           removal_rates=removal_rates1)


art_pts_df_f_filt_init_g_rnd_p=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_init_g_rnd_p, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])


### часть с рандомизированным графом




! pip install tqdm


from tqdm import *
import random


def degree_preserving_randomization(G, epsilon=10.0):
    G1=G.copy()
    L1=list(G1.edges())
    e_max=len(L1)-1
    st=0
    steps=int(epsilon*len(L1))
    for st in tqdm(range(steps)):
        e1=random.randint(0, e_max)   
        e2=random.randint(0, e_max)
        (P,Q)=L1[e1]
        (S,R)=L1[e2]
        if ((P!=R) and (Q!=S) and(not G1.has_edge(P,R)) and(not G1.has_edge(S,Q))):
            try:
                G1.remove_edge(S,R)
                G1.remove_edge(P,Q)
                G1.add_edge(P,R)
                G1.add_edge(S,Q)
                L1[e1]=(P,R)
                L1[e2]=(S,Q)
            except:
                continue
    return(G1)


randomized_initial_gr=degree_preserving_randomization(G=gg28917_cp, 
                                                      epsilon=10.0)

### randomized initial graph, hubs first

# removal_rates1=sorted(list([1/j for j in range(1,11)]),
#                      reverse=False) # [:-1]


# # rand init gr,  random protocol, art pts
# до удаления вершин степени 1

list_of_art_perc_and_rem_fr_for_randomized_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=randomized_initial_gr,
                           removal_rates=removal_rates1)


art_pts_df_for_randomized_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_randomized_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])




## после удаления вершин степени 1


randomized_initial_gr_to_filt=randomized_initial_gr.copy()
vert_with_deg1 = [node for node,degree in 
                  dict(randomized_initial_gr.degree()).items() 
                  if degree ==1]
randomized_initial_gr_to_filt.remove_nodes_from(vert_with_deg1)







list_of_art_perc_and_rem_fr_for_filt_randomized_init_g=\
hubs_first_with_perc_of_art_pts_0411(network=randomized_initial_gr_to_filt,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_randomized_init_g=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_randomized_init_g, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])



### randomized initial graph, small degree first, art pts


list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_small_dp=\
small_deg_first_with_perc_of_art_pts_0411(network=randomized_initial_gr,
                           removal_rates=removal_rates1)


art_pts_df_for_randomized_init_g_small_dp=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_small_dp, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])




## после удаления вершин степени 1




list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_small_dp=\
small_deg_first_with_perc_of_art_pts_0411(network=
                           randomized_initial_gr_to_filt,
                           removal_rates=removal_rates1)


art_pts_df_for_filt_randomized_init_g_small_dp=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_small_dp, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])




### randomized init gr, random protocol, art pts


import random as rn


list_of_art_perc_and_rem_fr_for_randomized_init_g_rnd_p=\
random_art_pts_perc_change_0411(network=randomized_initial_gr,
                           removal_rates=removal_rates1)


art_pts_df_f_randomized_init_g_rnd_p=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_randomized_init_g_rnd_p, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])


### после удаления вершин степени 1

list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_rnd_p=\
random_art_pts_perc_change_0411(network=randomized_initial_gr_to_filt,
                           removal_rates=removal_rates1)


art_pts_df_f_filt_randomized_init_g_rnd_p=\
pd.DataFrame(list_of_art_perc_and_rem_fr_for_filt_randomized_init_g_rnd_p, \
             columns=['p (fraction of removed nodes)', \
                      'fraction of articulation points'])

### plotting art pts curves for randomized init gr


"""


fig, ax = plt.subplots(figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('Articulation points curves for randomized initial graph', fontsize=15, fontweight='bold')


common_df_list_for_init_and_rnd_init_gr=[art_pts_df_for_randomized_init_g,
            art_pts_df_for_filt_randomized_init_g,
            art_pts_df_for_randomized_init_g_small_dp,
            art_pts_df_for_filt_randomized_init_g_small_dp,
            art_pts_df_f_randomized_init_g_rnd_p,
            art_pts_df_f_filt_randomized_init_g_rnd_p
            ]

colors=['lightcoral', 'coral', 'orange', 'darkorange', 'pink', 'hotpink']
styles = ['-', '--', '-', '--', '-', '--']

legends=['''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (hubs first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (small degree first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (small degree first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (random protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (random protocol)'''
]

iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)

sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[0], x=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[1],  x=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends))
ax.set_title('Articulation points percentage curves for randomized initial graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[2], x=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[3],  x=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends))
# ax.set_title('Articulation points percentage curves for power law graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[4], x=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[5],  x=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[5].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends))


### изображаем кривые для исходного графа до и после фильтрации



fig, ax = plt.subplots(figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('Articulation points curves for initial graph', fontsize=15, fontweight='bold')


common_df_list_for_init_and_rnd_init_gr=[art_pts_df_for_init_g,
            art_pts_df_for_filt_init_g,
            art_pts_df_for_init_g_small_dp,
            art_pts_df_for_filt_init_g_small_dp,
            art_pts_df_f_init_g_rnd_p,
            art_pts_df_f_filt_init_g_rnd_p
            ]

colors=['blue', 'darkblue', 'orange', 'darkorange', 'pink', 'hotpink']
styles = ['-', '--', '-', '--', '-', '--']

legends=['''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (hubs first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (small degree first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (small degree first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (random protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (random protocol)'''
]

iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)

sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[0], x=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[1],  x=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends))
ax.set_title('Articulation points percentage curves for initial graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[2], x=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[3],  x=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends))
# ax.set_title('Articulation points percentage curves for power law graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[4], x=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,1], color=next(iterable_color), ax=ax,
             label=next(iterable_legends))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[5],  x=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[5].iloc[:,1], color=next(iterable_color), ax=ax,
             linestyle='dashed', label=next(iterable_legends)) 
"""


fig, ax = plt.subplots(figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('Articulation points curves for initial and randomized initial graph', fontsize=15, fontweight='bold')


## готовим легенды и прочее для рандомизированного графа

common_df_list_for_init_and_rnd_init_gr_for_rnd_init_gr=[art_pts_df_for_randomized_init_g,
            art_pts_df_for_filt_randomized_init_g,
            art_pts_df_for_randomized_init_g_small_dp,
            art_pts_df_for_filt_randomized_init_g_small_dp,
            art_pts_df_f_randomized_init_g_rnd_p,
            art_pts_df_f_filt_randomized_init_g_rnd_p
            ]

colors_for_rnd_init_gr=['lightcoral', 'coral', 'orange', 'darkorange', 'pink', 'hotpink']
styles_for_rnd_init_gr = ['-', '--', '-', '--', '-', '--']

legends_for_rnd_init_gr=['''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (hubs first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (small degree first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (small degree first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for randomized initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (random protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for randomized initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (random protocol)'''
]

color_iter_for_rnd_init_gr=iter(colors_for_rnd_init_gr)

legends_iter_for_rnd_init_gr=iter(legends_for_rnd_init_gr)

styles_iter_for_rnd_init_gr=iter(styles_for_rnd_init_gr)



common_df_list_for_init_and_rnd_init_gr_for_init_gr=[art_pts_df_for_init_g,
            art_pts_df_for_filt_init_g,
            art_pts_df_for_init_g_small_dp,
            art_pts_df_for_filt_init_g_small_dp,
            art_pts_df_f_init_g_rnd_p,
            art_pts_df_f_filt_init_g_rnd_p
            ]

colors_for_init_gr=['blue', 'darkblue', 'orange', 'darkorange', 'pink', 'hotpink']
styles_for_init_gr = ['-', '--', '-', '--', '-', '--']

legends_for_init_gr=['''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (hubs first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (hubs first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (small degree first protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (small degree first protocol)''',
'''Сhange the ratio of articulation points as the vertices are removed for initial graph before
remove vertices with degree 1 (with % of articulation points by vertical axis) (random protocol)''',
            '''Сhange the ratio of articulation points as the vertices are removed for initial
graph after remove vertices with degree 1
(with % of articulation points by vertical axis) (random protocol)'''
]

color_iter_for_init_gr=iter(colors_for_init_gr)

legends_iter_for_init_gr=iter(legends_for_init_gr)

styles_iter_for_init_gr=iter(styles_for_init_gr)


## объединяем списки легенд, датафреймов для исходного и рандомизированного исходного графа

common_df_list_for_init_and_rnd_init_gr=common_df_list_for_init_and_rnd_init_gr_for_rnd_init_gr+common_df_list_for_init_and_rnd_init_gr_for_init_gr








sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[0], 
             x=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[0].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_rnd_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[1],  
             x=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[1].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', label=next(legends_iter_for_rnd_init_gr))
ax.set_title('Articulation points percentage curves for initial graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[2], 
             x=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[2].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_rnd_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[3],  
             x=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[3].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', label=next(legends_iter_for_rnd_init_gr))
# ax.set_title('Articulation points percentage curves for power law graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[4], 
             x=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[4].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_rnd_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[5],  
             x=common_df_list_for_init_and_rnd_init_gr[5].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[5].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', label=next(legends_iter_for_rnd_init_gr)) 


### кривые для исходного графа

sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[6], 
             x=common_df_list_for_init_and_rnd_init_gr[6].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[6].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[7],  
             x=common_df_list_for_init_and_rnd_init_gr[7].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[7].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', 
             label=next(legends_iter_for_init_gr))
ax.set_title('Articulation points percentage curves for initial graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[8], 
             x=common_df_list_for_init_and_rnd_init_gr[8].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[8].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[9],  
             x=common_df_list_for_init_and_rnd_init_gr[9].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[9].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', 
             label=next(legends_iter_for_init_gr))
# ax.set_title('Articulation points percentage curves for power law graph')
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[10], 
             x=common_df_list_for_init_and_rnd_init_gr[10].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[10].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             label=next(legends_iter_for_init_gr))
sns.lineplot(data=common_df_list_for_init_and_rnd_init_gr[11],  
             x=common_df_list_for_init_and_rnd_init_gr[11].iloc[:,0], y=common_df_list_for_init_and_rnd_init_gr[11].iloc[:,1], 
             color=next(color_iter_for_init_gr), ax=ax,
             linestyle='dashed', 
             label=next(legends_iter_for_init_gr)) 




### part for mcc ### 





### randomized initial graph, hubs first, mcc

## до фильтрации

perc_mcc_list_for_randomized_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=randomized_initial_gr, \
                          removal_rates=removal_rates1)


mcc_df_for_randomized_init_g=pd.DataFrame(perc_mcc_list_for_randomized_init_g, 
                               columns=['p (fraction of removed nodes)', 
                                        'fraction of nodes in MCC'])



## после фильтрации

perc_mcc_list_for_filt_randomized_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=randomized_initial_gr_to_filt, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_randomized_init_g=pd.DataFrame(perc_mcc_list_for_filt_randomized_init_g, 
                            columns=['p (fraction of removed nodes)', 
                                     'fraction of nodes in MCC'])




### randomized initial graph, small degree protocol , mcc 

## до фильтрации 


perc_mcc_list_for_randomized_initial_gr_small_dp=\
small_deg_first_with_perc_of_nodes_in_mcc_0411(
    network=randomized_initial_gr, \
        removal_rates=removal_rates1)


mcc_df_for_randomized_initial_gr_small_dp=pd.DataFrame(
    perc_mcc_list_for_randomized_initial_gr_small_dp,
        columns=['p (fraction of removed nodes)',
        'fraction of nodes in MCC'])



## после удаления вершин степени 1

perc_mcc_list_for_filt_randomized_initial_gr_small_dp=\
small_deg_first_with_perc_of_nodes_in_mcc_0411(
    network=randomized_initial_gr_to_filt, \
        removal_rates=removal_rates1)




mcc_df_for_filt_randomized_initial_gr_small_dp=pd.DataFrame(
    perc_mcc_list_for_filt_randomized_initial_gr_small_dp,
    columns=['p (fraction of removed nodes)',
             'fraction of nodes in MCC'])



### randomized initial graph, random protocol , mcc 

## до фильтрации 

perc_mcc_list_for_randomized_initial_gr_rnd_p=\
random_MCC_perc_change_0411(network=randomized_initial_gr, \
                          removal_rates=removal_rates1)



mcc_df_for_randomized_initial_gr_rnd_p=pd.DataFrame(
    perc_mcc_list_for_randomized_initial_gr_rnd_p,
                               columns=['p (fraction of removed nodes)',
                                        'fraction of nodes in MCC'])


## после фильтрации

perc_mcc_list_for_filt_randomized_initial_gr_rnd_p=\
random_MCC_perc_change_0411(network=randomized_initial_gr_to_filt, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_randomized_initial_gr_rnd_p=\
pd.DataFrame(perc_mcc_list_for_filt_randomized_initial_gr_rnd_p,
             columns=['p (fraction of removed nodes)',
                      'fraction of nodes in MCC'])








### initial graph, hubs first, MCC




## до фильтрации 

perc_mcc_list_for_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=gg28917_cp, \
                          removal_rates=removal_rates1)


mcc_df_for_init_g=pd.DataFrame(perc_mcc_list_for_init_g, 
                               columns=['p (fraction of removed nodes)', 
                                        'fraction of nodes in MCC'])



## после удаления вершин степени 1


gg28917_cp2=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in dict(gg28917_cp2.degree()).items() if degree ==1]
gg28917_cp2.remove_nodes_from(vert_with_deg1)




perc_mcc_list_for_filt_init_g=\
hubs_first_with_perc_of_nodes_in_mcc_0411(network=gg28917_cp2, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_init_g=pd.DataFrame(perc_mcc_list_for_filt_init_g, 
                            columns=['p (fraction of removed nodes)', 
                                     'fraction of nodes in MCC'])



### initial graph, small degree protocol , MCC


perc_mcc_list_for_init_g_small_dp=\
small_deg_first_with_perc_of_nodes_in_mcc_0411(
    network=gg28917_cp, \
        removal_rates=removal_rates1)


mcc_df_for_init_g_small_dp=pd.DataFrame(
    perc_mcc_list_for_init_g_small_dp,
        columns=['p (fraction of removed nodes)',
        'fraction of nodes in MCC'])




## после удаления вершин степени 1


gg28917_cp2_small_dp=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in
                  dict(gg28917_cp2_small_dp.degree()).items()
                  if degree ==1]
gg28917_cp2_small_dp.remove_nodes_from(vert_with_deg1)





perc_mcc_list_for_filt_init_g_small_dp=\
small_deg_first_with_perc_of_nodes_in_mcc_0411(
    network=gg28917_cp2_small_dp, \
        removal_rates=removal_rates1)




mcc_df_for_filt_init_g_small_dp=pd.DataFrame(
    perc_mcc_list_for_filt_init_g_small_dp,
    columns=['p (fraction of removed nodes)',
             'fraction of nodes in MCC'])


### initial graph, random protocol , MCC 


perc_mcc_list_for_init_g_rnd_p=\
random_MCC_perc_change_0411(network=gg28917_cp, \
                          removal_rates=removal_rates1)



mcc_df_for_init_g_rnd_p=pd.DataFrame(perc_mcc_list_for_init_g_rnd_p,
                               columns=['p (fraction of removed nodes)',
                                        'fraction of nodes in MCC'])




### после удаления из исх -го графа вершин со степ - ю 1

gg28917_cp_rnd_p=gg28917_cp.copy()
vert_with_deg1 = [node for node,degree in
                  dict(gg28917_cp_rnd_p.degree()).items()
                  if degree ==1]
gg28917_cp_rnd_p.remove_nodes_from(vert_with_deg1)



perc_mcc_list_for_filt_init_g_rnd_p=\
random_MCC_perc_change_0411(network=gg28917_cp_rnd_p, \
                          removal_rates=removal_rates1)




mcc_df_for_filt_init_g_rnd_p=\
pd.DataFrame(perc_mcc_list_for_filt_init_g_rnd_p,
             columns=['p (fraction of removed nodes)',
                      'fraction of nodes in MCC'])






fig, ax = plt.subplots(figsize=[12, 12])




common_dfs_list_to_plot_mcc_for_init_gr=\
                    [mcc_df_for_init_g,
                        mcc_df_for_filt_init_g,
                        mcc_df_for_init_g_small_dp,
                        mcc_df_for_filt_init_g_small_dp,
                        mcc_df_for_init_g_rnd_p,
                        mcc_df_for_filt_init_g_rnd_p
                    ]

colors_for_init_gr=['red','darkred', 'pink','deeppink', 'magenta', 'darkmagenta']
styles_for_init_gr = ['-', '--', '-', '--', '-', '--']

legends_for_init_gr=[
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (hubs first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (hubs first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (small degree first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (small degree first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (random protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (random protocol)'''
        ]

color_iterator_for_init_gr=iter(colors_for_init_gr)

legends_iterator_for_init_gr=iter(legends_for_init_gr)

styles_iterator_for_init_gr=iter(styles_for_init_gr)



# ax[1].legend(loc='lower left')




### plotting mcc for rnd initial graph



fig, ax = plt.subplots(figsize=[12, 12])

fig.suptitle('''MCC curves for initial and randomized initial graph''',
             fontsize=15, fontweight='bold')


common_dfs_list_to_plot_mcc_for_randomized_init_gr=\
                    [mcc_df_for_randomized_init_g,
                    mcc_df_for_filt_randomized_init_g,
                    mcc_df_for_randomized_initial_gr_small_dp,
                    mcc_df_for_filt_randomized_initial_gr_small_dp,
                    mcc_df_for_randomized_initial_gr_rnd_p,
                    mcc_df_for_filt_randomized_initial_gr_rnd_p
                    ]

colors_for_randomized_init_gr=['red','darkred', 'pink','deeppink', 'gray', 'dimgray']
styles_for_randomized_init_gr = ['-', '--', '-', '--', '-', '--']

legends_for_randomized_init_gr=[
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (hubs first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (hubs first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (small degree first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (small degree first protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph before remove vertices with degree 1 (with % of nodes in MCC by vertical axis) (random protocol)''',
        '''Сhange the ratio of nodes in mcc as the vertices are removed for randomized initial graph after remove vertices with degree 1
        (with % of nodes in MCC by vertical axis) (random protocol)'''
        ]

color_iter_for_randomized_init_gr=iter(colors_for_randomized_init_gr)

legends_iter_for_randomized_init_gr=iter(legends_for_randomized_init_gr)

styles_iter_for_randomized_init_gr=iter(styles_for_randomized_init_gr)


common_dfs_list_to_plot_mcc=common_dfs_list_to_plot_mcc_for_randomized_init_gr+common_dfs_list_to_plot_mcc_for_init_gr



ax.legend(loc='lower left')
sns.lineplot(data=common_dfs_list_to_plot_mcc[0],
             x=common_dfs_list_to_plot_mcc[0].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[0].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             label=next(legends_iterator_for_init_gr))

sns.lineplot(data=common_dfs_list_to_plot_mcc[1],
             x=common_dfs_list_to_plot_mcc[1].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[1].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iterator_for_init_gr))
#ax[0].set_title('''Articulation points percentage curves for initial graph''')

sns.lineplot(data=common_dfs_list_to_plot_mcc[2],
             x=common_dfs_list_to_plot_mcc[2].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[2].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             label=next(legends_iterator_for_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[3],
             x=common_dfs_list_to_plot_mcc[3].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[3].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iterator_for_init_gr))

sns.lineplot(data=common_dfs_list_to_plot_mcc[4],
             x=common_dfs_list_to_plot_mcc[4].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[4].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             label=next(legends_iterator_for_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[5],
             x=common_dfs_list_to_plot_mcc[5].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[5].iloc[:,1],
             color=next(color_iterator_for_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iterator_for_init_gr))
ax.set_title('''Nodes in MCC percentage curves for randomized initial graph''')




# plotting for randomized init graph

ax.legend(loc='lower left')
sns.lineplot(data=common_dfs_list_to_plot_mcc[6],
             x=common_dfs_list_to_plot_mcc[6].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[6].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             label=next(legends_iter_for_randomized_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[7],
             x=common_dfs_list_to_plot_mcc[7].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[7].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iter_for_randomized_init_gr))
#ax[0].set_title('''Articulation points percentage curves for initial graph''')

sns.lineplot(data=common_dfs_list_to_plot_mcc[8],
             x=common_dfs_list_to_plot_mcc[8].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[8].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             label=next(legends_iter_for_randomized_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[9],
             x=common_dfs_list_to_plot_mcc[9].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[9].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iter_for_randomized_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[10],
             x=common_dfs_list_to_plot_mcc[10].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[10].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             label=next(legends_iter_for_randomized_init_gr))
sns.lineplot(data=common_dfs_list_to_plot_mcc[11],
             x=common_dfs_list_to_plot_mcc[11].iloc[:,0],
             y=common_dfs_list_to_plot_mcc[11].iloc[:,1],
             color=next(color_iter_for_randomized_init_gr),
             ax=ax,
             linestyle='dashed',
             label=next(legends_iter_for_randomized_init_gr))
ax.set_title('''Nodes in MCC percentage curves for initial graph''')









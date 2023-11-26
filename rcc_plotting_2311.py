import pandas as pd
import numpy as np
import seaborn as sns




def degree_rich_club_coefficient(G):
    deg = G.degree()
    rich_club = []
    rich_club_coefficient = 0.0
    for x in range(1,200):
        a  = dict((k, v) for k, v in deg.items() if v > x)
        N = len(a)
        if N == 1:
            break
        nodes = set(a)
        edges = 0
        for start_id, end_id in G.edges(nodes):
            if start_id in nodes:
                if end_id in nodes:
                    edges = edges + 1
        if rich_club_coefficient != edges/((N*(N-1))/2):
            rich_club_coefficient = edges/((N*(N-1))/2) 
            if rich_club_coefficient != 0:
                rich_club.append((x,rich_club_coefficient))
    return rich_club


rich_club_coefficient= nx.rich_club_coefficient(gg, normalized=False, seed=42)
rich_club_coefficient_li=[(k, v) for k, v in rich_club_coefficient.items()]
df_for_rc_distrib=pd.DataFrame(rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])
# df_for_rc_distrib.head(10)

norm_rich_club_coefficient= nx.rich_club_coefficient(gg, normalized=True, seed=42)
norm_rich_club_coefficient_li=[(k, v) for k, v in norm_rich_club_coefficient.items()]
df_for_norm_rc_distrib=pd.DataFrame(norm_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])



### with rcc udf

rich_club_coefficient2= nx.rich_club_coefficient(gg, normalized=False, seed=42)
rich_club_coefficient_li=[(k, v) for k, v in rich_club_coefficient.items()]
df_for_rc_distrib2=pd.DataFrame(rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])








### для графа power law

power_law_net=get_power_law_net(n_nodes=81145, k=2.5, verbose=False)


power_law_net_cp=power_law_net.copy()


pl_rich_club_coefficient= nx.rich_club_coefficient(power_law_net_cp, normalized=False, seed=42)
pl_rich_club_coefficient_li=[(k, v) for k, v in pl_rich_club_coefficient.items()]
df_for_pl_rc_distrib=pd.DataFrame(pl_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])
# df_for_rc_distrib.head(10)

pl_norm_rich_club_coefficient= nx.rich_club_coefficient(power_law_net_cp, normalized=True, seed=42)
pl_norm_rich_club_coefficient_li=[(k, v) for k, v in pl_norm_rich_club_coefficient.items()]
df_for_pl_norm_rc_distrib=pd.DataFrame(pl_norm_rich_club_coefficient_li,
                               columns=['degree', 'norm rich-club coefficient'])



### with rcc udf

pl_udf_rich_club_coefficient= nx.rich_club_coefficient(power_law_net_cp, normalized=False, seed=42)
pl_udf_rich_club_coefficient_li=[(k, v) for k, v in pl_udf_rich_club_coefficient.items()]
df_for_pl_udf_rc_distrib=pd.DataFrame(pl_udf_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])








### после удаления вершин степени 1

pl_g_to_filt_small_dp=power_law_net_cp.copy()
nodes_with_deg1=[node for node,degree in 
                 dict(pl_g_to_filt_small_dp.degree()).items() 
                 if degree==1]

pl_g_to_filt_small_dp.remove_nodes_from(nodes_with_deg1)

filt_pl_g_small_dp=pl_g_to_filt_small_dp.copy()


rich_club_coefficient_for_filt_pl_g= nx.rich_club_coefficient(filt_pl_g_small_dp, normalized=False, seed=42)
rich_club_coefficient_li_for_filt_pl_g=[(k, v) for k, v in rich_club_coefficient_for_filt_pl_g.items()]
df_for_pl_rc_distrib=pd.DataFrame(rich_club_coefficient_li_for_filt_pl_g,
                               columns=['degree', 'rich-club coefficient'])


### нормализованный
norm_rich_club_coefficient= nx.rich_club_coefficient(power_law_net_cp, normalized=True, seed=42)
norm_rich_club_coefficient_li=[(k, v) for k, v in pl_norm_rich_club_coefficient.items()]
df_for_filt_pl_norm_rc_distrib=pd.DataFrame(norm_rich_club_coefficient_li,
                               columns=['degree', 'norm rich-club coefficient'])



### with rcc udf

rich_club_coefficient_for_filt_pl_g_using_udf= nx.rich_club_coefficient(power_law_net_cp, normalized=False, seed=42)
rich_club_coefficient_for_filt_pl_g_using_udf=[(k, v) for k, v in rich_club_coefficient_for_filt_pl_g_using_udf.items()]
for_filt_pl_g_rc_distrib_using_udf=pd.DataFrame(rich_club_coefficient_for_filt_pl_g_using_udf,
                               columns=['degree', 'rich-club coefficient'])




'''import seaborn as sns
fig, ax = plt.subplots(3,1, figsize=(18, 18))



ax[0] = sns.barplot(data=df_for_pl_rc_distrib, x='degree', y='rich-club coefficient', color='orange')
ax[0].bar_label(ax[0].containers[0], fontsize=10)
ax[0].set_title('Rich-club coefficient as a function of k')


ax[1] = sns.barplot(data=df_for_pl_norm_rc_distrib, x='degree', y='norm rich-club coefficient', color='yellow')
ax[1].bar_label(ax[1].containers[1], fontsize=10)
ax[1].set_title('Normalized rich-club coefficient as a function of k')


ax[2] = sns.barplot(data=df_for_pl_udf_rc_distrib, x='degree', y='rich-club coefficient', color='pink')
ax[2].bar_label(ax[2].containers[2], fontsize=10)
ax[2].set_title('Normalized rich-club coefficient as a function of k')'''









fig, ax = plt.subplots(3, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('''RCC curves for power law graph''', fontsize=15, fontweight='bold')


dfs_to_plot=[df_for_pl_rc_distrib,
df_for_pl_norm_rc_distrib,
df_for_pl_udf_rc_distrib,
df_for_pl_rc_distrib,
df_for_filt_pl_norm_rc_distrib,
for_filt_pl_g_rc_distrib_using_udf]

colors=['violet', 'magenta', 'goldenrod', 'darkgoldenrod', 'orange', 'darkorange']
styles = ['-', '--', '-', '--']

legends=['''RCC curve for power law graph before remove vertices with degree 1''', 
         '''RCC curve for power law graph after remove vertices with degree 1''',

         '''Normalized RCC curve for power law graph before remove vertices with degree 1''', 
         '''Normalized RCC curve for power law graph after remove vertices with degree 1''',

         '''RCC curve for power law graph before remove vertices with degree 1 (using udf function)''', 
         '''RCC curve for power law graph after remove vertices with degree 1  (using udf function)''']


iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)


# simple rcc
sns.lineplot(data=dfs_to_plot[0], 
             x=dfs_to_plot[0].iloc[:,0], 
             y=dfs_to_plot[0].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  
             x=dfs_to_plot[1].iloc[:,0], 
             y=dfs_to_plot[1].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('''RCC curve for power law graph before and after remove vertices with degree 1''')
ax[0].legend(loc='lower left')

### normalized rcc
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], 
             y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], 
             y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[1].set_title('''Normalized RCC curve for power law graph before and after remove vertices with degree 1''')
ax[1].legend(loc='lower left')

### udf rcc


sns.lineplot(data=dfs_to_plot[4],  x=dfs_to_plot[4].iloc[:,0], 
             y=dfs_to_plot[4].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[5],  x=dfs_to_plot[5].iloc[:,0], 
             y=dfs_to_plot[5].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[2].set_title('''RCC curve for power law graph before and after remove vertices with degree 1 (using udf)''')
ax[2].legend(loc='lower left')





### для графа ER


n = 81145 
m = 123822  
seed = 20160  # seed random number generators for reproducibility
# Use seed for reproducibility
erdos_renyi_g = nx.gnm_random_graph(n, m, seed=seed)


erdos_renyi_g_cp=erdos_renyi_g.copy()








## simple rich club

er_g_rich_club_coefficient= nx.rich_club_coefficient(erdos_renyi_g_cp, normalized=False, seed=42)
er_g_rich_club_coefficient_li=[(k, v) for k, v in er_g_rich_club_coefficient.items()]
df_for_er_g_rc_distrib=pd.DataFrame(er_g_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])

## normalized rich club

er_g_norm_rich_club_coefficient= nx.rich_club_coefficient(erdos_renyi_g_cp, normalized=True, seed=42)
er_g_norm_rich_club_coefficient_li=[(k, v) for k, v in er_g_norm_rich_club_coefficient.items()]
df_for_er_g_norm_rc_distrib=pd.DataFrame(er_g_norm_rich_club_coefficient_li,
                               columns=['degree', 'norm rich-club coefficient'])



### with udf rcc 

er_g_udf_rich_club_coefficient= nx.rich_club_coefficient(power_law_net_cp, normalized=False, seed=42)
er_g_udf_rich_club_coefficient_li=[(k, v) for k, v in er_g_udf_rich_club_coefficient.items()]
df_for_er_g_udf_rc_distrib=pd.DataFrame(er_g_udf_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])








### после удаления вершин степени 1

er_g_to_filt=erdos_renyi_g_cp.copy()
nodes_with_deg1=[node for node, degree in 
                 dict(erdos_renyi_g_cp.degree()).items() 
                 if degree==1]

er_g_to_filt.remove_nodes_from(nodes_with_deg1)

filt_er_g=er_g_to_filt.copy()


# simple rcc after filt 

rich_club_coefficient_for_filt_er_g= nx.rich_club_coefficient(filt_er_g, normalized=False, seed=42)
rich_club_coefficient_li_for_filt_er_g=[(k, v) for k, v in rich_club_coefficient_for_filt_er_g.items()]
df_for_filt_er_g_rc_distrib=pd.DataFrame(rich_club_coefficient_li_for_filt_er_g,
                               columns=['degree', 'rich-club coefficient'])


### нормализованный
norm_rich_club_coefficient_for_filt_er_g= nx.rich_club_coefficient(filt_er_g, normalized=True, seed=42)
norm_rich_club_coefficient_li_for_filt_er_g=[(k, v) for k, v in norm_rich_club_coefficient_for_filt_er_g.items()]
df_for_filt_er_g_norm_rc_distrib=pd.DataFrame(norm_rich_club_coefficient_li_for_filt_er_g,
                               columns=['degree', 'norm rich-club coefficient'])



### with rcc udf

rich_club_coefficient_for_filt_er_g_using_udf= nx.rich_club_coefficient(filt_er_g, normalized=False, seed=42)
rich_club_coefficient_li_for_filt_er_g_using_udf=[(k, v) for k, v in rich_club_coefficient_for_filt_er_g_using_udf.items()]
for_filt_er_g_rc_distrib_using_udf=pd.DataFrame(rich_club_coefficient_li_for_filt_er_g_using_udf,
                               columns=['degree', 'rich-club coefficient'])



fig, ax = plt.subplots(3, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('''RCC curves for ER graph''', fontsize=15, fontweight='bold')


dfs_to_plot=[
df_for_er_g_rc_distrib,
df_for_er_g_norm_rc_distrib,
df_for_er_g_udf_rc_distrib,
df_for_filt_er_g_rc_distrib,
df_for_filt_er_g_norm_rc_distrib,
for_filt_er_g_rc_distrib_using_udf]

colors=['fuchsia', 'mediumorchid', 'pink', 'hotpink', 'lime', 'seagreen']
styles = ['-', '--', '-', '--']

legends=['''RCC curve for ER graph before remove vertices with degree 1''', 
         '''RCC curve for ER graph after remove vertices with degree 1''',

         '''Normalized RCC curve for ER graph before remove vertices with degree 1''', 
         '''Normalized RCC curve for ER graph after remove vertices with degree 1''',

         '''RCC curve for ER graph before remove vertices with degree 1 (using udf function)''', 
         '''RCC curve for ER graph after remove vertices with degree 1  (using udf function)''']


iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)


# simple rcc
sns.lineplot(data=dfs_to_plot[0], 
             x=dfs_to_plot[0].iloc[:,0], 
             y=dfs_to_plot[0].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  
             x=dfs_to_plot[1].iloc[:,0], 
             y=dfs_to_plot[1].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('''RCC curve for ER graph before and after remove vertices with degree 1''')
ax[0].legend(loc='lower left')

### normalized rcc
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], 
             y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], 
             y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[1].set_title('''Normalized RCC curve for ER graph before and after remove vertices with degree 1''')
ax[1].legend(loc='lower left')

### udf rcc


sns.lineplot(data=dfs_to_plot[4],  x=dfs_to_plot[4].iloc[:,0], 
             y=dfs_to_plot[4].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[5],  x=dfs_to_plot[5].iloc[:,0], 
             y=dfs_to_plot[5].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[2].set_title('''RCC curve for ER graph before and after remove vertices with degree 1 (using udf)''')
ax[2].legend(loc='lower left')






### для исходного графа



initial_gr=gg28917_cp.copy()


## simple rich club

init_g_rich_club_coefficient= nx.rich_club_coefficient(initial_gr, normalized=False, seed=42)
init_g_rich_club_coefficient_li=[(k, v) for k, v in init_g_rich_club_coefficient.items()]
df_for_init_g_rc_distrib=pd.DataFrame(init_g_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])

## normalized rich club

init_g_norm_rich_club_coefficient= nx.rich_club_coefficient(initial_gr, normalized=True, seed=42)
init_g_norm_rich_club_coefficient_li=[(k, v) for k, v in init_g_norm_rich_club_coefficient.items()]
df_for_init_g_norm_rc_distrib=pd.DataFrame(init_g_norm_rich_club_coefficient_li,
                               columns=['degree', 'norm rich-club coefficient'])


### with udf rcc 

init_g_udf_rich_club_coefficient= nx.rich_club_coefficient(initial_gr, normalized=False, seed=42)
init_g_udf_rich_club_coefficient_li=[(k, v) for k, v in init_g_udf_rich_club_coefficient.items()]
df_for_init_g_udf_rc_distrib=pd.DataFrame(init_g_udf_rich_club_coefficient_li,
                               columns=['degree', 'rich-club coefficient'])



### после удаления вершин степени 1


initial_gr_to_filt=gg28917_cp.copy()

vert_with_deg1 = [node for node,degree in 
                  dict(initial_gr_to_filt.degree()).items() 
                  if degree ==1]
initial_gr_to_filt.remove_nodes_from(vert_with_deg1)

filt_init_gr=initial_gr_to_filt.copy()


# simple rcc after filt 

rich_club_coefficient_for_filt_init_g= nx.rich_club_coefficient(filt_init_gr, normalized=False, seed=42)
rich_club_coefficient_li_for_filt_init_g=[(k, v) for k, v in rich_club_coefficient_for_filt_init_g.items()]
df_for_filt_init_g_rc_distrib=pd.DataFrame(rich_club_coefficient_li_for_filt_init_g,
                               columns=['degree', 'rich-club coefficient'])


### нормализованный
norm_rich_club_coefficient_for_filt_init_g= nx.rich_club_coefficient(filt_init_gr, normalized=True, seed=42)
norm_rich_club_coefficient_li_for_filt_init_g=[(k, v) for k, v in norm_rich_club_coefficient_for_filt_init_g.items()]
df_for_filt_init_g_norm_rc_distrib=pd.DataFrame(norm_rich_club_coefficient_li_for_filt_init_g,
                               columns=['degree', 'norm rich-club coefficient'])



### with rcc udf

rich_club_coefficient_for_filt_init_g_using_udf= nx.rich_club_coefficient(filt_init_gr, normalized=False, seed=42)
rich_club_coefficient_li_for_filt_init_g_using_udf=[(k, v) for k, v in rich_club_coefficient_for_filt_init_g_using_udf.items()]
for_filt_init_g_rc_distrib_using_udf=pd.DataFrame(rich_club_coefficient_li_for_filt_init_g_using_udf,
                               columns=['degree', 'rich-club coefficient'])



fig, ax = plt.subplots(3, 1, figsize=[12, 12])
# fig ax= plt.figure(figsize=(16, 8))                          #задаем фигуру
fig.suptitle('''RCC curves for origin graph''', fontsize=15, fontweight='bold')


dfs_to_plot=[df_for_init_g_rc_distrib,
df_for_init_g_norm_rc_distrib,
df_for_init_g_udf_rc_distrib,
df_for_filt_init_g_rc_distrib,
df_for_filt_init_g_norm_rc_distrib,
for_filt_init_g_rc_distrib_using_udf]

colors=['cornflowerblue', 'royalblue', 'lightcoral', 'firebrick', 'orange', 'darkorange']
styles = ['-', '--', '-', '--']

legends=['''RCC curve for origin graph before remove vertices with degree 1''', 
         '''RCC curve for origin graph after remove vertices with degree 1''',

         '''Normalized RCC curve for origin graph before remove vertices with degree 1''', 
         '''Normalized RCC curve for origin graph after remove vertices with degree 1''',

         '''RCC curve for origin graph before remove vertices with degree 1 (using udf function)''', 
         '''RCC curve for origin graph after remove vertices with degree 1  (using udf function)''']


iterable_color=iter(colors)

iterable_legends=iter(legends)

iterable_styles=iter(styles)


# simple rcc
sns.lineplot(data=dfs_to_plot[0], 
             x=dfs_to_plot[0].iloc[:,0], 
             y=dfs_to_plot[0].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[1],  
             x=dfs_to_plot[1].iloc[:,0], 
             y=dfs_to_plot[1].iloc[:,1], 
             color=next(iterable_color), ax=ax[0], 
             linestyle='dashed', label=next(iterable_legends))
ax[0].set_title('''RCC curve for origin graph before and after remove vertices with degree 1''')
ax[0].legend(loc='lower left')

### normalized rcc
sns.lineplot(data=dfs_to_plot[2],  x=dfs_to_plot[2].iloc[:,0], 
             y=dfs_to_plot[2].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[3],  x=dfs_to_plot[3].iloc[:,0], 
             y=dfs_to_plot[3].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[1].set_title('''Normalized RCC curve for origin graph before and after remove vertices with degree 1''')
ax[1].legend(loc='lower left')

### udf rcc


sns.lineplot(data=dfs_to_plot[4],  x=dfs_to_plot[4].iloc[:,0], 
             y=dfs_to_plot[4].iloc[:,1], color=next(iterable_color), ax=ax[1],
             label=next(iterable_legends))
sns.lineplot(data=dfs_to_plot[5],  x=dfs_to_plot[5].iloc[:,0], 
             y=dfs_to_plot[5].iloc[:,1], color=next(iterable_color), ax=ax[1], 
             linestyle='dashed', label=next(iterable_legends))
ax[2].set_title('''RCC curve for origin graph before and after remove vertices with degree 1 (using udf)''')
ax[2].legend(loc='lower left')







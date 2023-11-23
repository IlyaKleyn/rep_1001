




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


import seaborn as sns
fig, ax = plt.subplots(3,1, figsize=(18, 18))
# ax = sns.barplot(flights, x="year", y="passengers", estimator="sum", errorbar=None)
# ax.bar_label(ax.containers[0], fontsize=10);
ax[0] = sns.barplot(data=df_for_rc_distrib, x='degree', y='rich-club coefficient', color='orange')
ax[0].bar_label(ax[0].containers[0], fontsize=10)
ax[0].set_title('Rich-club coefficient as a function of k')


ax[1] = sns.barplot(data=df_for_norm_rc_distrib, x='degree', y='rich-club coefficient', color='yellow')
ax[1].bar_label(ax[1].containers[1], fontsize=10)
ax[1].set_title('Normalized rich-club coefficient as a function of k')


ax[2] = sns.barplot(data=df_for_rc_distrib2, x='degree', y='rich-club coefficient', color='pink')
ax[2].bar_label(ax[2].containers[2], fontsize=10)
ax[2].set_title('Normalized rich-club coefficient as a function of k')






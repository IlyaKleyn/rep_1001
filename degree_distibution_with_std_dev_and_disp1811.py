
import numpy as np

removal_rates1=sorted(list([1/j for j in range(1,11)]),reverse=False) # [:-1]

### распределение для исходного графа 
fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# Create a gridspec for adding subplots of different sizes

degree_sequence_for_init_g=sorted((d for n, d in gg28917_cp.degree()), reverse=True)

degree_sequence_for_init_g_cutted=sorted((d for n, d in gg28917_cp.degree() if d <=60), reverse=True)

# после удаления вершин степени 1
degree_sequence_for_filt_init_g=sorted((d for n, d in gg28917_cp2.degree()), reverse=True)
degree_sequence_for_filt_init_g_cutted=sorted((d for n, d in gg28917_cp2.degree() if d<=80), reverse=True)

# ax[0].bar(*np.unique(degree_sequence_for_init_g, return_counts=True))
# cut version

'''for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center'''

values, counts = np.unique(degree_sequence_for_init_g_cutted, return_counts=True)
#x_labels = counts
df1=pd.DataFrame(list(zip(values, counts)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df1, ax=ax[0])
ax[0].set_title("Degree distribution for initial graph")
ax[0].set_xlabel("Degree")
ax[0].set_ylabel("# of Nodes")
for x,y in zip(values, counts):

    label1 = "{:.0f}".format(y)

    ax[0].annotate(label1, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# ax[0].set_xticklabels(x_labels)

# ax[1].bar(*np.unique(degree_sequence_for_filt_init_g, return_counts=True))
# cut version
values2, counts2 = np.unique(degree_sequence_for_filt_init_g_cutted, return_counts=True)
# x_labels2 = counts2
df2=pd.DataFrame(list(zip(values2, counts2)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df2, ax=ax[1])
ax[1].set_title("Degree distribution for initial graph after remove vertices with degree 1")
ax[1].set_xlabel("Degree")
ax[1].set_ylabel("# of Nodes")

for x,y in zip(values2, counts2):

    label = "{:.0f}".format(y)

    ax[1].annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# ax[1].set_xticklabels(x_labels2)

fig.tight_layout()
plt.show()


variance=np.round(np.var(degree_sequence_for_init_g),3)
std=np.round(np.std(degree_sequence_for_init_g),3)

variance2=np.round(np.var(degree_sequence_for_filt_init_g),3)
std2=np.round(np.std(degree_sequence_for_filt_init_g),3)

print('degree variance for initial graph:', variance)
print('degree std for  initial graph:', std)


print('degree variance for initial graph after remove vertices with degree 1:', variance2)
print('degree std for  initial graph after remove vertices with degree 1:', std2)



# zip joins x and y coordinates in pairs
'''for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center'''



### распределение для power law



def get_power_law_net(n_nodes, k, verbose=False):
    '''
    powerlaw.Power_Law-A power-function continuous random variable-
    generate_random(n=1, estimate_discrete=None)
    Generates random numbers from the theoretical probability distribution. If xmax is present, it is currently ignored.

    '''
    distribution = powerlaw.Power_Law(xmin=1, parameters=[k])
    degrees = distribution.generate_random(n_nodes).astype(np.int32)

    start_time = time.time()
    generator = ConfigurationGenerator(degrees)
    net = generator.get_network()

    if verbose:
        print("** Gen PowerLaw k=%.2f took %.3fs" % (k, time.time() - start_time))

    return net


## до удаления вершин степени 1



exp_ks = [2.6]

power_law_net=get_power_law_net(n_nodes=81145, k=2.5, verbose=False)


power_law_net_cp=power_law_net.copy()

fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# Create a gridspec for adding subplots of different sizes

degree_sequence_for_pl_g=sorted((d for n, d in \
                                   power_law_net_cp.degree()), reverse=True)

degree_sequence_for_pl_g_cutted=sorted((d for n, d in \
                                    power_law_net_cp.degree() if d <=60), reverse=True)






values3, counts3 = np.unique(degree_sequence_for_pl_g_cutted, return_counts=True)
#x_labels = counts
df3=pd.DataFrame(list(zip(values3, counts3)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df3, ax=ax[0])
ax[0].set_title("Degree distribution for power law graph")
ax[0].set_xlabel("Degree")
ax[0].set_ylabel("# of Nodes")
for x,y in zip(values3, counts3):

    label1 = "{:.0f}".format(y)

    ax[0].annotate(label1, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

## после удаления вершин степени 1

pl_g_to_filt=power_law_net_cp.copy()
nodes_with_deg1=[node for node,degree in dict(pl_g_to_filt.degree()).items() if degree==1]

pl_g_to_filt.remove_nodes_from(nodes_with_deg1)

filt_pl_g=pl_g_to_filt.copy()

# после удаления вершин степени 1
degree_sequence_for_filt_pl_g=sorted((d for n, d in \
                                    filt_pl_g.degree()), reverse=True)
degree_sequence_for_filt_pl_g_cutted=sorted((d for n, d in \
                                    filt_pl_g.degree() if d<=80), reverse=True)


values4, counts4 = np.unique(degree_sequence_for_filt_pl_g_cutted, return_counts=True)
# x_labels2 = counts2
df4=pd.DataFrame(list(zip(values4, counts4)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df4, ax=ax[1])
ax[1].set_title("Degree distribution for power law graph after remove vertices with degree 1")
ax[1].set_xlabel("Degree")
ax[1].set_ylabel("# of Nodes")

for x,y in zip(values4, counts4):

    label = "{:.0f}".format(y)

    ax[1].annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# ax[1].set_xticklabels(x_labels2)

fig.tight_layout()
plt.show()


variance_pl_g=np.round(np.var(degree_sequence_for_pl_g),3)
std_pl_g=np.round(np.std(degree_sequence_for_pl_g),3)

variance_filt_pl_g=np.round(np.var(degree_sequence_for_filt_pl_g),3)
std_filt_pl_g=np.round(np.std(degree_sequence_for_filt_pl_g),3)

print('degree variance for power law graph:', variance_pl_g)
print('degree std for power law graph:', std_pl_g)


print('degree variance for power law graph after remove vertices with degree 1:', variance_filt_pl_g)
print('degree std for power law graph after remove vertices with degree 1:', std_filt_pl_g)







### для графа ER

n = 81145 # 10 nodes
m = 123822  # 20 edges
seed = 20160  # seed random number generators for reproducibility
# Use seed for reproducibility
erdos_renyi_g = nx.gnm_random_graph(n, m, seed=seed)


erdos_renyi_g_cp=erdos_renyi_g.copy()



fig, ax = plt.subplots(2, 1, figsize=[12, 12])
# Create a gridspec for adding subplots of different sizes

degree_sequence_for_erl_g=sorted((d for n, d in \
                                   erdos_renyi_g_cp.degree()), reverse=True)

degree_sequence_for_er_g_cutted=sorted((d for n, d in \
                                    erdos_renyi_g_cp.degree() if d <=60), reverse=True)






values5, counts5 = np.unique(degree_sequence_for_er_g_cutted, return_counts=True)
#x_labels = counts
df5=pd.DataFrame(list(zip(values5, counts5)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df5, ax=ax[0])
ax[0].set_title("Degree distribution for ER graph")
ax[0].set_xlabel("Degree")
ax[0].set_ylabel("# of Nodes")
for x,y in zip(values5, counts5):

    label1 = "{:.0f}".format(y)

    ax[0].annotate(label1, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

## после удаления вершин степени 1

er_g_to_filt=erdos_renyi_g_cp.copy()
nodes_with_deg1=[node for node, degree in dict(er_g_to_filt.degree()).items() if degree==1]

er_g_to_filt.remove_nodes_from(nodes_with_deg1)

filt_er_g=er_g_to_filt.copy()

# после удаления вершин степени 1
degree_sequence_for_filt_er_g=sorted((d for n, d in \
                                    filt_er_g.degree()), reverse=True)
degree_sequence_for_filt_er_g_cutted=sorted((d for n, d in \
                                    filt_er_g.degree() if d<=80), reverse=True)


values6, counts6 = np.unique(degree_sequence_for_filt_er_g_cutted, return_counts=True)
# x_labels2 = counts2
df6=pd.DataFrame(list(zip(values6, counts6)), columns=['degree', 'frequency'])
sns.barplot(x='degree',y='frequency', data=df6, ax=ax[1])
ax[1].set_title("Degree distribution for ER graph after remove vertices with degree 1")
ax[1].set_xlabel("Degree")
ax[1].set_ylabel("# of Nodes")


for x,y in zip(values6, counts6):

    label = "{:.0f}".format(y)

    ax[1].annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# ax[1].set_xticklabels(x_labels2)

fig.tight_layout()
plt.show()


variance_er_g=np.round(np.var(degree_sequence_for_er_g),3)
std_er_g=np.round(np.std(degree_sequence_for_er_g),3)

variance_filt_er_g=np.round(np.var(degree_sequence_for_filt_er_g),3)
std_filt_er_g=np.round(np.std(degree_sequence_for_filt_er_g),3)

print('degree variance for ER graph:', variance_er_g)
print('degree std for ER graph:', std_er_g)


print('degree variance for ER graph after remove vertices with degree 1:', variance_filt_er_g)
print('degree std for ER graph after remove vertices with degree 1:', std_filt_er_g)

### hubs first (без random)


def hubs_first_with_perc_of_nodes_in_mcc_0411(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=sorted(list(dict(net.nodes())), reverse=True)
      num_of_nodes=len(nodes)
      print('total nodes:', num_of_nodes)

      num_of_nodes_to_rem=int(len(nodes)*float(rate))

      print('total nodes to rem: ', num_of_nodes_to_rem)
      print('num_of_nodes_to_rem', num_of_nodes_to_rem)

      nodes_to_rem=[nodes[i] for i in range(num_of_nodes_to_rem)]
      # rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(nodes_to_rem)
      try:
        largest_cc = max(nx.connected_components(net), key=len)

        print('largest_cc', largest_cc)
        size_of_lrg_cc=len(largest_cc)

      #nodes=list(dict(net.nodes()))
      #num_of_nodes=len(nodes)

        frac_of_mcc_nodes=size_of_lrg_cc/num_of_nodes
        # art_pts_num=len(list(nx.articulation_points(net)))
        # art_pts_perc=art_pts_num/len(nodes)
        print('pair i', tuple([rate, frac_of_mcc_nodes]))
        res_list.append(tuple([rate, frac_of_mcc_nodes]))
        net=network.copy()
      except:
        break
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list



def hubs_first_with_perc_of_art_pts_0411(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=sorted(list(dict(net.nodes())), reverse=True)
      num_of_nodes=len(nodes)
      print('total nodes:', num_of_nodes)

      num_of_nodes_to_rem=int(len(nodes)*float(rate))

      print('total nodes to rem: ', num_of_nodes_to_rem)
      print('num_of_nodes_to_rem', num_of_nodes_to_rem)

      nodes_to_rem=[nodes[i] for i in range(num_of_nodes_to_rem)]
      # rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(nodes_to_rem)
      art_pts_num=len(list(nx.articulation_points(net)))
      art_pts_perc=art_pts_num/len(nodes)
      res_list.append(tuple([rate, art_pts_perc]))
      net=network.copy()
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list


### теперь создаем функции для сценария not hubs first

def small_deg_first_with_perc_of_art_pts_0411(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=sorted(list(dict(net.nodes())), reverse=False)
      num_of_nodes=len(nodes)
      print('total nodes:', num_of_nodes)

      num_of_nodes_to_rem=int(len(nodes)*float(rate))

      print('total nodes to rem: ', num_of_nodes_to_rem)
      print('num_of_nodes_to_rem', num_of_nodes_to_rem)

      nodes_to_rem=[nodes[i] for i in range(num_of_nodes_to_rem)]
      # rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(nodes_to_rem)
      art_pts_num=len(list(nx.articulation_points(net)))
      art_pts_perc=art_pts_num/len(nodes)
      res_list.append(tuple([rate, art_pts_perc]))
      net=network.copy()
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list


### not hubs first (без random)


def small_deg_first_with_perc_of_nodes_in_mcc_1111(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=sorted(list(dict(net.nodes())), reverse=False)
      num_of_nodes=len(nodes)
      print('total nodes:', num_of_nodes)

      num_of_nodes_to_rem=int(len(nodes)*float(rate))

      print('total nodes to rem: ', num_of_nodes_to_rem)
      print('num_of_nodes_to_rem', num_of_nodes_to_rem)

      nodes_to_rem=[nodes[i] for i in range(num_of_nodes_to_rem)]
      # rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(nodes_to_rem)
      try:
        largest_cc = max(nx.connected_components(net), key=len)

        print('largest_cc', largest_cc)
        size_of_lrg_cc=len(largest_cc)

      #nodes=list(dict(net.nodes()))
      #num_of_nodes=len(nodes)
        nodes=sorted(list(dict(net.nodes())), reverse=False)
        num_of_nodes=len(nodes)

        frac_of_mcc_nodes=size_of_lrg_cc/num_of_nodes
        # art_pts_num=len(list(nx.articulation_points(net)))
        # art_pts_perc=art_pts_num/len(nodes)
        print('pair i', tuple([rate, frac_of_mcc_nodes]))
        res_list.append(tuple([rate, frac_of_mcc_nodes]))
        net=network.copy()
      except:
        break
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list



### для сценария random

def random_art_pts_perc_change_0411(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=list(dict(net.nodes()))
      num_of_nodes_to_rem=int(len(nodes)*float(rate))
      rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(rnd_nodes_to_rem)
      # mod from 1111
      # nodes=list(dict(net.nodes()))
      # art_pts_num=len(list(nx.articulation_points(net)))
      try:
        art_pts_perc=art_pts_num/len(nodes)
        res_list.append(tuple([rate, art_pts_perc]))
      except:
        break
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list


def random_MCC_perc_change_0411(network, removal_rates):
    res_list=[]
    for rate in removal_rates:

      net=network.copy()
      nodes=list(dict(net.nodes()))
      num_of_nodes=len(nodes)
      # print('total nodes:', num_of_nodes)

      num_of_nodes_to_rem=int(len(nodes)*float(rate))

      # print('total nodes to rem: ', num_of_nodes_to_rem)
      # print('num_of_nodes_to_rem', num_of_nodes_to_rem)

      # nodes_to_rem=[nodes[i] for i in range(num_of_nodes_to_rem)]
      rnd_nodes_to_rem=rn.sample(population=nodes, k=num_of_nodes_to_rem)
      net.remove_nodes_from(rnd_nodes_to_rem)
      try:
        largest_cc = max(nx.connected_components(net), key=len)

        print('largest_cc', largest_cc)
        size_of_lrg_cc=len(largest_cc)

      #nodes=list(dict(net.nodes()))
      #num_of_nodes=len(nodes)

        ## mod from 1111
        # nodes=list(dict(net.nodes()))
        # num_of_nodes=len(nodes)
        frac_of_mcc_nodes=size_of_lrg_cc/num_of_nodes
        # art_pts_num=len(list(nx.articulation_points(net)))
        # art_pts_perc=art_pts_num/len(nodes)
        print('pair i', tuple([rate, frac_of_mcc_nodes]))
        res_list.append(tuple([rate, frac_of_mcc_nodes]))
        net=network.copy()
      except:
        break
      #res_dict.setdefault(rate, art_pts_num)
      #res_df_to_plot=pd.DataFrame.from_dict(res_dict, orient='index').reset_index()
      # res_df_to_plot.columns=['perc_of_rem_nodes','perc_of_art_pts']
    return res_list
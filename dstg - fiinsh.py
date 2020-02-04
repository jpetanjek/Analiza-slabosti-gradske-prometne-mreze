import networkx as nx
import matplotlib.pyplot as plt

#Funkcija  defineNodesAndEdges_Problem1()   sadrži   predefinirane   unose  vrhova  i  bridova  za  graf  iz  zadatka 1.
#Pokretanjem funkcije "gradi" se graf iz navedenog zadatka. Svrha funkcije je olakšan unos grafa pri pokretanju programa.
def defineNodesAndEdges_Problem1():
    G.add_node(1, name='v1')
    G.add_node(2, name='v2')
    G.add_node(3, name='v3')
    G.add_node(4, name='v4')
    G.add_node(5, name='v5')
    G.add_node(6, name='v6')

    G.add_edges_from([(1,2,{'weight':2}), (1,3,{'weight':3}), (2,1,{'weight':2}), (2,6,{'weight':5}), (3,1,{'weight':3}), (3,4,{'weight':3}),(3,5,{'weight':1}),(3,6,{'weight':3}),(4,3,{'weight':3}),(4,5,{'weight':1}),(5,3,{'weight':1}),(5,4,{'weight':1}),(5,6,{'weight':4}),(6,2,{'weight':5}),(6,3,{'weight':3}),(6,5,{'weight':4})])

#Funkcija  defineNodesAndEdges_Problem2()   sadrži   predefinirane   unose  vrhova  i  bridova  za  graf  iz  zadatka 2.
#Pokretanjem funkcije "gradi" se graf iz navedenog zadatka. Svrha funkcije je olakšan unos grafa pri pokretanju programa.
def defineNodesAndEdges_Problem2():
    G.add_node(1, name='v1')
    G.add_node(2, name='v2')
    G.add_node(3, name='v3')
    G.add_node(4, name='v4')
    G.add_node(5, name='v5')

    G.add_edges_from([(1,2,{'weight':3}),(1,3,{'weight':1}),(2,1,{'weight':1}),(2,4,{'weight':3}),(2,5,{'weight':7}),(3,1,{'weight':2}),(3,5,{'weight':3}),(4,2,{'weight':4}),(4,5,{'weight':2}),(5,4,{'weight':2})])

#Funkcija  defineNodesAndEdges_Problem3()   sadrži   predefinirane   unose  vrhova  i  bridova  za  graf  iz  zadatka 3.
#Pokretanjem funkcije "gradi" se graf iz navedenog zadatka. Svrha funkcije je olakšan unos grafa pri pokretanju programa.
def defineNodesAndEdges_Problem3():
    G.add_node(1, name='v1')
    G.add_node(2, name='v2')
    G.add_node(3, name='v3')
    G.add_node(4, name='v4')
    G.add_node(5, name='v5')
    G.add_node(6, name='v6')
    G.add_node(7, name='v7')
    G.add_node(8, name='v8')
    G.add_node(9, name='v9')
    G.add_node(10, name='v10')
    G.add_node(11, name='v11')
    G.add_node(12, name='v12')
    G.add_node(13, name='v13')
    G.add_node(14, name='v14')
    G.add_node(15, name='v15')
    G.add_node(16, name='v16')

    G.add_edges_from([(1,2,{'weight':1}), (1,4,{'weight':2}), (1,7,{'weight':9}), (2,1,{'weight':1}), (2,3,{'weight':2}), (2,4,{'weight':1}), (3,2,{'weight':2}), (3,6,{'weight':2}), (3,9,{'weight':5}), (4,1,{'weight':2}),(4,5,{'weight':1}),(5,4,{'weight':1}),(5,6,{'weight':1}),(5,7,{'weight':8}),(6,3,{'weight':2}),(6,5,{'weight':1}),(6,8,{'weight':1}), (7,1,{'weight':9}), (7,5,{'weight':8}),(7,11,{'weight':4}),(8,6,{'weight':1}),(8,9,{'weight':3}), (9,3,{'weight':5}),(9,8,{'weight':3}),(9,14,{'weight':5}),(10,8,{'weight':1}),(10,11,{'weight':4}),(10,12,{'weight':1}),(11,7,{'weight':4}),(11,10,{'weight':4}),(11,16,{'weight':5}),(12,10,{'weight':1}),(12,13,{'weight':2}),(12,16,{'weight':4}), (13,12,{'weight':2}),(13,14,{'weight':2}),(13,15,{'weight':3}),(14,9,{'weight':5}),(14,13,{'weight':2}),(14,15,{'weight':2}),(15,13,{'weight':3}),(15,14,{'weight':2}),(15,16,{'weight':5}),(16,11,{'weight':5}),(16,12,{'weight':4}),(16,15,{'weight':5})])

#Funkcija   plotGraph()  u   novom   prozoru   crta  graf  na  temelju  unesenih  vrhova  i  lukova.
#Parametar  G  - graf  koji  želimo  iscrtati  u  novom  prozoru
def plotGraph(G):
    pos=nx.spring_layout(G)
    labels={}
    for i in range (1,len(G)+1):
        labels[i]=r'$v'+str(i)+'$'

    nx.draw_networkx_nodes(G,pos,node_color='b',node_size=500,alpha=0.75)
    nx.draw_networkx_edges(G,pos,edge_color='gray',width=3,alpha=0.75)
    nx.draw_networkx_labels(G,pos,labels,font_size=13,font_color="white")
    plt.show()

#Funkcija sum_of_shortest_paths() izračunava sumu najkraćih puteva u grafu. U funkciji terativno se izračunava najkraći put između svih parova vrhova grafa G.
#Parametar  G  -  graf/pograf   kojem   želimo   izračunati   sumu   najkraćih   puteva
def sum_of_shortest_paths(G):
    referent_val = 0
    
    for s in G.nodes:
        for t in G.nodes:
                if(nx.has_path(G,s,t)):
                    referent_val = referent_val + nx.shortest_path_length(G, source=s, target=t, weight='weight')

    return referent_val

#Funkcija calculate_criticallity_for_given_edge() izračunava kritičnost danog brida ee u grafu G. U funkciji se izračunava suma najkraćih puteva u podgrafu H koji ne sadrži brid koji je proslijeđen u parametru.
#Parametar G - početni graf u kojem se nalazi određeni brid
#Parametar ee - brid kojemu želimo izračunati kritičnost
#Parametar m - način izvršavanja (0 ili 1). 0 - Grafovi u kojemu su lukovi između para vrhova v1 i v2 jednakih težina. 1 - Grafovi u kojemu lukovi između para vrhova v1 i v2 različitih težina.
def calculate_criticallity_for_given_edge(G, ee, m):
    try:
        H = G.copy()

        if m==0:
            H.remove_edge(ee[0],ee[1])
            if(H.has_edge(ee[1],ee[0])):
                H.remove_edge(ee[1],ee[0])
        elif m==1:
            H.remove_edge(ee[0],ee[1])    

        edge_val = sum_of_shortest_paths(H)
          
        H.clear()

        return edge_val
    except Exception as e:
        print('', end = '')

#Funkcija calculate_referent_node_value() izračunava referentnu vrijednost za dani vrh tako da stvori podgraf H u kojemu se uklanja vrh ne proslijeđen u parametru i bridovi 
#koji ulaze/izlaze iz njega, zatim se lukovi povezuju s obzirom na susjedne vrhove vrha ne i dodijeljuje im se odgovarajuća težina.
#Parametar G - početni graf u kojem se nalazi određeni brid
#Parametar ne - vrh kojemu želimo izračunati kritičnost
#Parametar m - način izvršavanja (0 ili 1). 0 - Grafovi u kojemu su lukovi između para vrhova v1 i v2 jednakih težina. 1 - Grafovi u kojemu lukovi između para vrhova v1 i v2 različitih težina.
def calculate_referent_node_value(G, ne, m):
    H = G.copy()
    edge_list_for_ne = []

    if m==0:
        for ee in G.edges:
            if ee[1]==ne:
                edge_list_for_ne.append(ee)
    elif m==1:
        for ee in G.edges:
            if ee[1]==ne or ee[0]==ne:
                edge_list_for_ne.append(ee)
        
    for ee in edge_list_for_ne:
        try:
            H.remove_edge(ee[0],ee[1])
        except Exception as e:
            print('', end = '')
        try:
            H.remove_edge(ee[1],ee[0])
        except Exception as e:
            print('', end = '')

    H.remove_node(ne)
    
    if m==0:  
        for sv in edge_list_for_ne:
            for dv in edge_list_for_ne:
                if sv!=dv:
                    s=sv[0]
                    d=dv[0]
                    w = G[sv[0]][sv[1]][0]['weight'] + G[dv[0]][dv[1]][0]['weight']
                    H.add_edge(s, d, weight=w)
        try:
            return sum_of_shortest_paths(H)
        except:
            return 0    
    elif m==1:
        for sv in edge_list_for_ne:
            for dv in edge_list_for_ne:
                if  sv!=dv and sv[1]==dv[0]:
                    s=sv[0]
                    d=dv[1]
                                        
                    w = G[sv[0]][sv[1]][0]['weight'] + G[dv[0]][dv[1]][0]['weight']

                    if s!=ne and d!=ne:
                        H.add_edge(s, d, weight=w)
        
        try:
            return sum_of_shortest_paths(H)
        except:
            return 0

#Funkcija calculate_sum_of_shortest_paths_without_given_node() izračunavu sumu najkraćih puteva između svakog para vrhova bez vrha koji je proslijeđen u parametru i lukova koji ulaze/izlaze iz njega.
#Funkcija stvara podgraf H na kojem se provode promijene te poziva funkciju sum_of_shortest_paths()
#Parametar G - početni graf u kojem se nalazi određeni brid
#Parametar ne - vrh kojemu želimo izračunati kritičnost
def calculate_sum_of_shortest_paths_without_given_node(G, ne):
    H = G.copy()
    edge_list_for_ne = []
    
    for ee in G.edges:
        if ee[1]==ne:
            edge_list_for_ne.append(ee)

    for ee in edge_list_for_ne:
        try:
            H.remove_edge(ee[0],ee[1])
        except Exception as e:
            print('', end = '')
        try:
            H.remove_edge(ee[1],ee[0])
        except Exception as e:
            print('', end = '')

    H.remove_node(ne)

    try:
        return sum_of_shortest_paths(H)
    except:
        return 0

######      MAIN        #######
G = nx.MultiDiGraph()

odabir = 0
mode = 0
odabir = int(input("1 - Preset unos za graf iz prvog zadatka\n2 - Preset unos za graf iz drugog zadatka\n3 - Preset unos za graf iz trećeg zadatka\n4 - Unos (Custom) za graf od strane korisnika\nUnesite odabir: "))

if odabir==1:
    defineNodesAndEdges_Problem1()
    mode=0
elif odabir==2:
    defineNodesAndEdges_Problem2()
    mode=1
elif odabir==3:
    defineNodesAndEdges_Problem3()
    mode=0
elif odabir==4:
    number_of_nodes = int(input('Unesite željeni broj vrhova: '))
    for i in range(1,number_of_nodes+1):
        G.add_node(i, name='v'+str(i))
    print("Kreirani vrhovi: " + str(G.nodes))
    number_of_edges = int(input('Unesite željeni broj lukova: '))
    i = 1
    while True:
        print("Luk " + str(i))
        source_node = int(input('Izvorišni vrh: '))
        target_node = int(input('Odredišni vrh: '))
        weight = int(input('Težina luka: '))
        correct_input_source = 0
        correct_input_target = 0
        correct_input_weight = 0

        for ne in G.nodes:
            if ne==source_node:
                correct_input_source=1
                break
            else:
                correct_input_source=0

        for ne in G.nodes:
            if ne==target_node:
                correct_input_target=1
                break
            else:
                correct_input_target=0

        if weight>0:
            correct_input_weight=1
        else:
            correct_input_weight=0

        if correct_input_source==0 or correct_input_target==0 or correct_input_weight==0:
            print('Pogrešni unosi - ponovite unos luka')
        elif correct_input_source==1 or correct_input_target==1 or correct_input_weight==1:
            G.add_edge(source_node, target_node, weight=weight)
            i=i+1
        
        if i==(number_of_edges+1):
            break
    while True:
        mode = int(input("Unesite parametar m (0 ili 1):"))
        if mode==0 or mode==1:
            break

print('Referentna vrijednost: ' + str(sum_of_shortest_paths(G)))

list_of_edges = G.edges

for ee in list(list_of_edges):
    try:
        print('Kriticnost brida (ulice) ' +str(ee) +'=' + str(calculate_criticallity_for_given_edge(G,ee,mode)-sum_of_shortest_paths(G)))
    except Exception as e:
        print(e)

for ne in range(1, len(G)+1):
    print('Kriticnost vrha (raskršća) '+ str(ne) + ' : ' + str( calculate_sum_of_shortest_paths_without_given_node(G, ne) - calculate_referent_node_value(G,ne,mode)))

plotGraph(G)


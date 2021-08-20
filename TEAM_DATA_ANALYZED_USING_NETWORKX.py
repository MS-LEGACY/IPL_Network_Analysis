import networkx as nx

G = nx.read_graphml("D:\\WINTER_SEMESTER_2020_21\\CSE3021_SOCIAL_AND_INFORMATION_NETWORKS\\ANALYZED_TEAMS_DATA_GEPHI.graphml")
pr = nx.pagerank(G, alpha=0.9)
team_to_node={'0':"Chennai Super Kings",'1':"Deccan Chargers",'2':"Delhi Capitals",'3':"Delhi Daredevils",'4':"Gujarat Lions",'5':"Kings XI Punjab",'6':"Kochi Tuskers Kerala",'7':"Kolkata Knight Riders",'8':"Mumbai Indians",'9':"Pune Warriors",'10':"Rajasthan Royals",'11':"Rising Pune Supergiant",'12':"Royal Challengers Bangalore",'13':"Sunrisers Hyderabad"}
sorted_page = sorted(pr.items(), key=lambda x: x[1],reverse=True)   
for i in sorted_page:
	print(f"{team_to_node[i[0]] : <30}{i[1] : ^20}")
	# print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}")
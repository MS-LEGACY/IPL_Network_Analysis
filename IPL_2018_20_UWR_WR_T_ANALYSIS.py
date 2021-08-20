import pandas as pd 
from openpyxl import load_workbook
import xlsxwriter
import tabulate
import math
xl = pd.ExcelFile("D:\\WINTER_SEMESTER_2020_21\\CSE3021_SOCIAL_AND_INFORMATION_NETWORKS\\New folder\\archive\\IPL_2018_20_UWR_APPROACH.xlsx")
df = xl.parse("IPL_2018_20_UWR_APPROACH")

dict1_wins = {"Chennai Super Kings" :{},"Delhi Capitals":{},"Kings XI Punjab":{},"Kolkata Knight Riders":{},"Mumbai Indians":{},"Rajasthan Royals":{},"Royal Challengers Bangalore":{},"Sunrisers Hyderabad":{}}
dict1_t_val = {"Chennai Super Kings" :{},"Delhi Capitals":{},"Kings XI Punjab":{},"Kolkata Knight Riders":{},"Mumbai Indians":{},"Rajasthan Royals":{},"Royal Challengers Bangalore":{},"Sunrisers Hyderabad":{}}
team_to_node={"Chennai Super Kings" :0,"Delhi Capitals":1,"Kings XI Punjab":2,"Kolkata Knight Riders":3,"Mumbai Indians":4,"Rajasthan Royals":5,"Royal Challengers Bangalore":6,"Sunrisers Hyderabad":7}
set1 = {"Chennai Super Kings"}

dict1_weighted_outlinks = {"Chennai Super Kings" :{},"Delhi Capitals":{},"Kings XI Punjab":{},"Kolkata Knight Riders":{},"Mumbai Indians":{},"Rajasthan Royals":{},"Royal Challengers Bangalore":{},"Sunrisers Hyderabad":{}}

team_names= []
for i in range(0,173):
	set1.add(df['team1'][i])
team_names = sorted(set1)
for i in team_names:
	num_wins=0
	num_wickets=0
	num_runs=0
	sum_wickets=0
	sum_runs=0
	for k in range(0,173):
		if(df['winner'][k]==i):
			num_wins+=1
			if(df['result'][k]=="wickets"):
				num_wickets+=1
				sum_wickets+=df['result_margin'][k]
			elif(df['result'][k]=="runs"):
				num_runs+=1
				sum_runs+=df['result_margin'][k]
	dict1_wins[i]["wins"]=num_wins
	dict1_wins[i]["by_runs"]=num_runs
	dict1_wins[i]["by_wickets"]=num_wickets
	dict1_wins[i]["sum_runs"]=sum_runs
	dict1_wins[i]["sum_wickets"]=sum_wickets
for i in team_names:
	t_wickets = math.sqrt(dict1_wins[i]['sum_wickets'])/2
	t_runs = math.sqrt(dict1_wins[i]['sum_runs'])/2
	t_val = math.sqrt(t_wickets+t_runs)/2
	dict1_t_val[i]['t_wickets'] = t_wickets
	dict1_t_val[i]['t_runs'] = t_runs
	dict1_t_val[i]['t_val'] = t_val
sorted_t_val=(sorted(dict1_t_val, key=lambda x: dict1_t_val[x]['t_val'],reverse=True))
for i in sorted_t_val:
	print(i,"   ",dict1_t_val[i]['t_wickets'],"         ",dict1_t_val[i]['t_runs'],"             ",dict1_t_val[i]['t_val'])
for i in sorted_t_val:
	print(i,"     ",dict1_wins[i]["wins"],"   ",dict1_wins[i]["sum_runs"],"     ",dict1_wins[i]["sum_wickets"])

for i in team_names:
	for j in team_names:
		num_losses=0
		num_losses_runs=0
		num_losses_wickets=0
		for k in range(0,173):
			if((df['team1'][k]==i and df['team2'][k]==j) or (df['team1'][k]==j and df['team2'][k]==i)):
				if(df['winner'][k]==j):
					num_losses+=1
					if(df['result'][k]=="wickets"):
						num_losses_wickets+=df['result_margin'][k]
					elif(df['result'][k]=="runs"):
						num_losses_runs+=df['result_margin'][k]
		list1=[num_losses,num_losses_wickets,num_losses_runs]
		if(num_losses!=0):
			weight_outlink = 60*(num_losses)+20*(num_losses_runs)+20*(num_losses_wickets)/(num_losses+num_losses_runs+num_losses_wickets)
			list1.append(weight_outlink)
			dict1_weighted_outlinks[i][j] = list1
	print(i,"     ",dict1_weighted_outlinks[i])		
	print(" ")

team_uwtr_rank={"Chennai Super Kings" :1/8,"Delhi Capitals":1/8,"Kings XI Punjab":1/8,"Kolkata Knight Riders":1/8,"Mumbai Indians":1/8,"Rajasthan Royals":1/8,"Royal Challengers Bangalore":1/8,"Sunrisers Hyderabad":1/8}
team_uwtr_rank_next={"Chennai Super Kings" :1/8,"Delhi Capitals":1/8,"Kings XI Punjab":1/8,"Kolkata Knight Riders":1/8,"Mumbai Indians":1/8,"Rajasthan Royals":1/8,"Royal Challengers Bangalore":1/8,"Sunrisers Hyderabad":1/8}

for k in range(0,1000):
	for i in team_names:
		damp_factor=0.15
		sum_wtr=0
		sum_t_val=dict1_t_val[i]['t_val']
		for j in team_names:
			if (i!=j):
				sum_wtr=team_uwtr_rank[j]/dict1_weighted_outlinks[j][i][3]
				sum_t_val=dict1_t_val[j]['t_val']
		team_uwtr_rank_next[i] =  (1-damp_factor)*(dict1_t_val[i]['t_val'])/len(team_names)*sum_t_val+damp_factor*sum_wtr
	for val in team_names:
		team_uwtr_rank[val] = team_uwtr_rank_next[val]
print("---------------------------------------------------------------------------------------------")
sorted_team_uwtr = sorted(team_uwtr_rank.items(), key=lambda x: x[1],reverse=True)
for i in sorted_team_uwtr:
	print(i)



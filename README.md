# Social Network Analysis of Indian Premier League (IPL) Cricket Teams and Batsmen.
## Abstract
The aim of the paper is to analyze the team and player data using the matches played in the Indian
Premier League (IPL) which is franchise-based cricket league played in India, involving players
of various cricket playing nations. It is huge franchise and involves millions of rupees. The
revenue generated by the league is quite large and the role of the league is very significant for the
thousands of cricket players whose performance in this game paves the way for a place in Indian
Cricket Team. The paper uses the fundamentals of social network analysis to create a weighted
and directed graph for teams participating in this league. The weights of the graph will be based
on number of wins against other teams. Then using the diffusion page ranking algorithm ranks of
the teams will be based on the “quality” of wins instead of the simple measure of number of wins.
Then the main aim of any team is to increase its batting capabilities that can be done by
improving the partnerships between different batsmen. Using the various centrality measure I
have tried and identified the key batsmen in a team that are effective partnership formers teams
should help honing their performance and retain these players as they are very good.

## Page Rank Algorithm of Team Ranking.
Data was collected from the website of espncricinfo.com for the IPL matches and their results
from the year of 2008-2020. For each match the data consisted of the teams which the match was
played, date of match, venue of match, result of match, runs or wicket by which match was won. I
have analyzed network of teams by taking into the account of head-to-head encounters of
competing teams. A match can be represented by a directed link. If a team i wins against team j, a
directed link is drawn from j to i. A weighted representation of the directed network is obtained
by assigning a weight wji to link, where wji is equal to the fraction of times team i wins against
team j.
The code used to accomplish the task is given in Appendix 1. The number of matches played
between two teams are analyzed over the time period of 2008-2020. The team playing matches
against each other form a link. Where the outgoing link from team i to j represent the fraction of
the matches won by team j against team i. The resulting graph in Fig.1 is constructed using Gephi
software as it gives beautiful graphs that can by analyzed by exporting the data to NetworkX
software. The thickness of the edges is proportional to the weights of edges. While size of nodes
is based on in-degree strength of nodes.
<br>
![image](https://user-images.githubusercontent.com/64634411/130266796-ad195eab-a7fb-4051-a1ae-7be7942b1ba9.png)

The edges are colored with respect to the color of the nodes they are directed towards, hence
nodes with thicker edges and more incoming edges have won a greater number of matches
against the team form which the edges are originating from. The size of the nodes are directly
proportional to the in-degree of that node.
The page ranking algorithm for ranking of the reams is as follows.<br>
![image](https://user-images.githubusercontent.com/64634411/130266692-0489dc01-9dfb-4db7-82ed-04328821f500.png)
Where w ji is the weight of an edge and the variable S jout = ∑i w ji is the out-strength of a link. pi
is the PageRank score assigned to team i, and it represents the fraction of the overall “influence”
when applied to the steady state of the diffusion process on vertex i. The equation is applied to all
the teams in the given graph. q is in range of [0,1], acts as a control parameter that accounts for
the importance of the various terms influencing the score of the rest of nodes, and N is the sum of
wji
the number of teams in the network. The term (1 − q ) ∑ j p j is used for the portion of score
Sout
j
received by the node i in the diffusion process of the hypothesis that nodes redistribute their
q
entire credit to the neighboring nodes. The term stands for a uniform redistribution of credit
n1−q
among all nodes. The term
 ∑j δ(S jout ) serves as a correction in the case of existence of
N
dangling nodes.
As some of the teams were nor present in all the seasons, a fair analysis consisting of seasons of
fixed teams playing matches against each other is done for the years 2018-2020. The teams like
Delhi Capitals, Chennai Super kings, Rajasthan Royals, Kings XI Punjab, Kolkata Knight Riders,
Sunrisers Hyderabad, Royal Challengers Bangalore, Mumbai Indians were the team who
participated in the IPL seasons of 2018-2020. The network analysis diagram constructed with the
help of Gephi is presented in the Figure 2. The outward directed edge with is of the same color as
that of the node from which is originating from.


## Read More
Please read the detailed description in this [PDF]()

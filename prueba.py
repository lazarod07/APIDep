#!/bin/python
# Small python script to prove a TV hosts' statement of like
# 'Why is it, that this year there are loads of goals scored?'
# 
# @date 2018/12/28
# @author daniel (daniel@football-data.org)

import requests
import json

uri = 'https://api.football-data.org/v2/competitions/2001/teams'
headers = { 'X-Auth-Token': '433be9172e014d48a8539a0cf2777fe7' }
response = requests.get(uri, headers=headers)
#print(response.content)
matches = response.json()['teams'] 
#print(response._content)

for m in matches:
  print(m['name'])
    
""" uri = 'http://api.football-data.org/v2/competitions/BL1/matches?season=2019'
headers = { 'X-Auth-Token': '433be9172e014d48a8539a0cf2777fe7' }
response = requests.get(uri, headers=headers)
print(response.content)
matches = response.json()['matches'] 
finishedMatches = filter(lambda match: match['status'] == 'FINISHED', matches)
matchesUntilMatchdayX = filter(lambda match: match['matchday'] < 18, matches)

totalGoals = 0
for match in matchesUntilMatchdayX:
  totalGoals += match['score']['fullTime']['homeTeam'] + match['score']['fullTime']['awayTeam']

print ("   That is an avg of " + str(round((float(totalGoals) / 18.0),2)) + " per matchday.")
#print ("   and an avg of " + str(round((float(totalGoals) / len(matchesUntilMatchdayX)),2)) + " per game.") """
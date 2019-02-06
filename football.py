import json
import urllib
import urllib2
import sys


api_headers = {
            "X-Auth-Token": '2ed6f2e3137c4c5b952f71554c3a236f'
         }

url = 'http://api.football-data.org/v2/'

request = urllib2.Request(url + 'competitions?plan=TIER_ONE', headers=api_headers)
response = urllib2.urlopen(request).read()
values = json.loads(response)

def printResultsAndMatchesForTeam(FavTeam):
	for c in values['competitions']:
		teamsUrl = url + 'competitions/' + str(c['id']) + '/teams'
		teamsRequest = urllib2.Request(teamsUrl, headers=api_headers)
		teamsResponse = urllib2.urlopen(teamsRequest).read()
		teamValues = json.loads(teamsResponse)
		for t in teamValues['teams']:
#			print (c['area']['name'] + " - " + c['name'] + " - " + t['shortName'])
			if (FavTeam.lower() == t['shortName'].lower()):
                                previousResultsUrl = url + 'teams/' + str(t['id']) + '/matches?status=FINISHED&dateFrom=2019-01-10&dateTo=2019-02-10&limit=5'
                                previousResultRequest = urllib2.Request(previousResultsUrl, headers=api_headers)
				previousResultResponse = urllib2.urlopen(previousResultRequest).read()
				previousResultValues = json.loads(previousResultResponse)
				for match in previousResultValues['matches']:
					print match['utcDate'] + " : " + match['homeTeam']['name']  + " vs " + match['awayTeam']['name']
					print "                SCORE: " + str(match['score']['fullTime']['homeTeam']) + " - " + str(match['score']['fullTime']['awayTeam'])
				
				matchUrl = url + 'teams/' + str(t['id']) + '/matches?limit=5&status=SCHEDULED'
				matchRequest = urllib2.Request(matchUrl, headers=api_headers)
				matchResponse = urllib2.urlopen(matchRequest).read()
				matchValues = json.loads(matchResponse)
				for match in matchValues['matches']:
					print match['utcDate'] + " : " + match['homeTeam']['name'] + " vs " + match['awayTeam']['name']
    

printResultsAndMatchesForTeam(sys.argv[1])

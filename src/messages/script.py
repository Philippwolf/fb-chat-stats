#  -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import datetime
import json


def monthToNum(month):
	json_data = json.load(open('months.json'))
	return json_data[monthLang][month]


#theme = input("Theme name: ")
#monthLang = input("Month language: ")
theme = "valentines"
monthLang = "pl"

# open file with messages and read them all
file = open("messages.html", "r", encoding="utf-8")
readlines = file.readlines()
file.close()

# find all messages
soup = BeautifulSoup(str(readlines), 'html.parser')
messages = soup.findAll('div', attrs={'class': 'message'})
# in fb files <p> is acctually message
p = soup.findAll('p')


# count messages
messagesAmount = len(messages)


# create index.html file
index = open("../index.html", "w", encoding="utf-8")
index.write('<!DOCTYPE html><html><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>OUR FACEBOOK CHAT</title><link href=\'css/main.css\' rel=\'stylesheet\' type=\'text/css\'><link href=\'themes/'+ theme +'/'+ theme +'.css\' rel=\'stylesheet\' type=\'text/css\'></head><body id="mainDiv"><div><div id="main" class="container"><h1 style="text-align: center;">OUR FACEBOOK CHAT</h1>')

members = []
dates = {}
startDate = ""
mostActiveDay = ""
mostActiveDayMessagesCount = 0
totalDays = 0
totalMessages = messagesAmount
totalWords = 0
averageMessageLen = 0
messagesPerDay = 0

pAmount = 0

print("Reading messages...    ", end="")
for w in range(0, messagesAmount-1):
	user = messages[w].find('span', attrs={'class': 'user'})
	date = messages[w].find('span', attrs={'class': 'meta'})
	message = p[pAmount]
	x = message.find("p")
	while x != None:
		pAmount += 1
		x = x.find("p")

	user = user.text
	date = date.text[:-14]
	message = message.text

	# https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
	totalWords += len(re.findall(r"[\w']+", message))

	if (user not in members):
		members.append(user)

	if (date not in dates):
		dates[date] = 1
	else:
		dates[date] += 1
	
	if pAmount%10 == 0: 
		for x in range(0, len(str(pAmount))): print('\b', end="")
		print(str(pAmount), end="")

	pAmount += 1



# TOTALS

print("\nFinding users...    ")
index.write('<div class="block">')
index.write('<h3>Members: ' + ', '.join(members) + '</h3>')

print("Finding start date...")
index.write('<h3>Start date: ' + messages[messagesAmount-1].find('span', attrs={'class': 'meta'}).text[:-14] + '</h3>')

print("Finding most active day...")
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
index.write('<h3>Most active day: ' + max(dates, key=dates.get) + '( <b>'+ str(dates[max(dates, key=dates.get)]) +'</b> messages )</h3>')
index.write('</div>')

date1 = messages[messagesAmount-1].find('span', attrs={'class': 'meta'}).text.split()
fDay = date1[0]
fMonth = monthToNum(date1[1])
fYear = date1[2]
firstDate = datetime.date(int(fYear), int(fMonth), int(fDay))

date2 = messages[0].find('span', attrs={'class': 'meta'}).text.split()
sDay = date2[0]
sMonth = monthToNum(date2[1])
sYear = date2[2]
secondDate = datetime.date(int(sYear), int(sMonth), int(sDay))

delta = secondDate - firstDate

index.write('<div class="block"><h1>Totals</h1>')
index.write('<div class="md-3"><h4>'+ str(delta.days) +'</h4><h5>Days</h5></div>')
index.write('<div class="md-3"><h4>'+ str(totalMessages) +'</h4><h5>Messages</h5></div>')
index.write('<div class="md-3"><h4>'+ str(totalWords) +'</h4><h5>Words</h5></div>')
index.write('</div>')



# AVERAGES

index.write('<div class="block"><h1>Averages</h1>')
index.write('<div class="md-2"><h4>'+ str(round(totalWords/totalMessages, 2)) +'</h4><h5>Length of a message</h5></div>')
index.write('<div class="md-2"><h4>'+ str(round(totalMessages/delta.days, 2)) +'</h4><h5>Messages per day</h5></div>')
index.write('</div>')





index.write('<script type="text/javascript" src="themes/'+ theme +'/'+theme+'.js"></script><script type="text/javascript" src="js/main.js"></script><script src="js/plotly-latest.min.js"></script><script type="text/javascript">window.onload = function() {	Plotly.newPlot(\'chart-area\', data, layout);	Plotly.newPlot(\'chart-area2\', data2);	Plotly.newPlot(\'chart-area3\', data3);	Plotly.newPlot(\'chart-area4\', data4);	Plotly.newPlot(\'chart-area5\', data5);	Plotly.newPlot(\'chart-area6\', data6);}</script></body></html>')

index.close()
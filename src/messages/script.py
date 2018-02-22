#  -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import datetime
import json
import random


def monthToNum(month):
	json_data = json.load(open('months.json'))
	return json_data[monthLang][str(month)]

def fbDateToWeekday(date1):
	date1 = date1.split()
	fDay = date1[0]
	fMonth = monthToNum(date1[1])
	fYear = date1[2]
	wholeDate = datetime.date(int(fYear), int(fMonth), int(fDay))

	return wholeDate.strftime("%A")


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

members = {}
dates = {}
hours = {'0': 0, '1': 0, '2': 0,'3': 0, '4': 0, '5': 0,'6': 0, '7': 0, '8': 0,'9': 0, '10': 0, '11': 0,'12': 0, '13': 0, '14': 0,'15': 0, '16': 0, '17': 0,'18': 0, '19': 0, '20': 0,'21': 0, '22': 0, '23': 0}
weekDays = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
allWords = {}
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
for w in range(messagesAmount-1, 0, -1):
	user = messages[w].find('span', attrs={'class': 'user'})
	date = messages[w].find('span', attrs={'class': 'meta'})
	message = p[pAmount]
	x = message.find("p")
	while x != None:
		pAmount += 1
		x = x.find("p")

	user = user.text
	date = date.text
	message = message.text
	hour = date.split()[4]
	hour = hour.split(":")[0]
	'''
	m = BeautifulSoup.unicode(message).encode("utf-8")
	print(m)
	'''
	# https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
	words = re.findall(r"[\w']+", message)
	totalWords += len(words)

	for word in words:
		if word in allWords:
			allWords[word] += 1
		else:
			allWords[word] = 1

	if str(hour) in hours:
		hours[hour] += 1
	else:
		hours[hour] = 1

	weekD = fbDateToWeekday(date)
	if weekD in weekDays:
		weekDays[weekD] += 1
	else:
		weekDays[weekD] = 1

	if (user not in members):
		members[user] = 1
	else:
		members[user] += 1


	date = date[:-14]
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
index.write('<h3>Members: ' + ', '.join(members.keys()) + '</h3>')

print("Finding start date...")
index.write('<h3>Start date: ' + messages[messagesAmount-1].find('span', attrs={'class': 'meta'}).text[:-14] + '</h3>')

print("Finding most active day...")
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
index.write('<h3>Most active day: ' + max(dates, key=dates.get) + '( <b>'+ str(dates[max(dates, key=dates.get)]) +'</b> messages )</h3>')
index.write('</div>')


print("Counting days...")
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


print("Counting averages...")
index.write('<div class="block"><h1>Averages</h1>')
index.write('<div class="md-2"><h4>'+ str(round(totalWords/totalMessages, 2)) +'</h4><h5>Length of a message</h5></div>')
index.write('<div class="md-2"><h4>'+ str(round(totalMessages/delta.days, 2)) +'</h4><h5>Messages per day</h5></div>')
index.write('</div>')


# CHARTS
print("Drawing charts...")
index.write('<div class="block"><h4>Who texts the most?</h4><div class="charts"><div id="chart-area"></div></div><h4>Activity by Day</h4><div class="charts"><div id="chart-area2"></div></div><h4>Timeline</h4><div class="charts"><div id="chart-area3"></div></div><h4>Activity by Week</h4><div class="charts"><div id="chart-area4"></div></div><h4>Top emoji*</h4><div class="charts"><div id="chart-area5"></div></div><h4>Top words</h4><div class="charts"><div id="chart-area6"></div></div><h6>* Counts how many times found in chat, not in message ( if in one message there were 3 &#x1F618, it counts it as 1)</h6></div>')


index.write('<script type="text/javascript" src="themes/'+ theme +'/'+theme+'.js"></script><script type="text/javascript" src="js/main.js"></script><script src="js/plotly-latest.min.js"></script><script type="text/javascript">window.onload = function() {	Plotly.newPlot(\'chart-area\', data, layout);	Plotly.newPlot(\'chart-area2\', data2);	Plotly.newPlot(\'chart-area3\', data3);	Plotly.newPlot(\'chart-area4\', data4);	/*Plotly.newPlot(\'chart-area5\', data5);*/	Plotly.newPlot(\'chart-area6\', data6);}</script></body></html>')

index.close()
print()
mainjs = open("../js/main.js", "w", encoding="utf-8")


# layout
mainjs.write('var layout = {  height: 400,  width: 500,  showlegend: {"orientation": "h"} };')


# who texts the most
mainjs.write('var data = [{  values: [')

for x in members:
	mainjs.write("\"" + str(members[x]) + "\",")

mainjs.write('],  labels: [')

for x in members:
	mainjs.write("\"" + str(x) + "\",")

mainjs.write('],  type: \'pie\',  marker: {\n\ncolors: [    ')

for x in members:
	mainjs.write("\"" + "#%06x" % random.randint(0, 0xFFFFFF) + "\",")

mainjs.write('\n\n]},  name: "Who texts the most",  textinfo:\'none\',  hole: .6,}];')



# daily activity
mainjs.write('var data2 = [  {    x: [\'00:00\', \'01:00\', \'02:00\',\'03:00\', \'04:00\', \'05:00\',\'06:00\', \'07:00\', \'08:00\',\'09:00\', \'10:00\', \'11:00\',\'12:00\', \'13:00\', \'14:00\',\'15:00\', \'16:00\', \'17:00\',\'18:00\', \'19:00\', \'20:00\',\'21:00\', \'22:00\', \'23:00\'],    y: [')

for x in hours:
	mainjs.write(str(hours[x]) + ",")

mainjs.write('],    type: \'bar\',    marker: {     \n\n color: "#d83434", \n\n },  }];')



# timeline
mainjs.write('var data3 = [  {    x: [')

for x in dates:
	mainjs.write("\"" + str(x) + "\",")

mainjs.write('],y: [')

for x in dates:
	mainjs.write(str(dates[x]) + ",")

mainjs.write('],    type: \'bar\',    marker: {      \n\n color: "#d83434", \n\n  },  }];')




# Week days
mainjs.write('var data4 = [  {    x: [')

for x in weekDays:
	mainjs.write("\"" + str(x) + "\",")

mainjs.write('],    y: [')

for x in weekDays:
	mainjs.write(str(weekDays[x]) + ",")

mainjs.write('],    type: \'bar\',    marker: {    \n\n  color: "#d83434", \n\n },  }];')	


# Top emoji

'''

var data5 = [
  {
    x: [String.fromCodePoint(0x1F612), String.fromCodePoint(0x1F60F), String.fromCodePoint(0x1F618), String.fromCodePoint(0x1F60A), String.fromCodePoint(0x1F602), String.fromCodePoint(0x1F620), String.fromCodePoint(0x1F61A)],
    y: [584,388,274,235,183,182,162],
    type: 'bar',
    marker: {
      color: "#d83434",
  },
  }
];

'''



# Top words

mainjs.write('var data6 = [  {    x: [')

i = 0
for key in sorted(allWords, key=allWords.__getitem__, reverse=True):
	mainjs.write("\"" + str(key) + "\",")
	i += 1
	if (i == 10): break

mainjs.write('],    y: [')

i = 0
for key in sorted(allWords, key=allWords.__getitem__, reverse=True):
	mainjs.write(str(allWords[key]) + ",")
	i += 1
	if (i == 10): break

mainjs.write('],    type: \'bar\',    marker: {    \n\n  color: "#d83434", \n\n },  }];')

mainjs.close()

print("Done! Unfortunately if you don't want random colors you have to edit /js/main.js file on your own")
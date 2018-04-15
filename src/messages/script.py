#  -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import datetime
import json
import random


def monthToNum(month):
	json_data = json.load(open('months.json', encoding='utf8'))
	for x in json_data[monthLang]:
		if str(x) == str(month).lower():
			return json_data[monthLang][x]

def fbDateToWeekday(date1, monthLang):
	date1 = date1.replace(",", "")
	date1 = date1.split()
	if (monthLang.lower() == "pl"):
		fDay = date1[0]
		fMonth = monthToNum(date1[1])
		fYear = date1[2]
	elif (monthLang.lower() == "en"):
		fDay = date1[2]
		fMonth = monthToNum(date1[1])
		fYear = date1[3]
	wholeDate = datetime.date(int(fYear), int(fMonth), int(fDay))
	return wholeDate.strftime("%A")

fileName = input("Fb messages file: ") + ".html"
theme = input("Theme name: ")
monthLang = input("Month language: ")
'''
fileName = "messages.html"
theme = "valentines"
monthLang = "pl"
'''
# open file with messages and read them all
file = open(fileName, "r", encoding="utf-8")
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
index.write('<!DOCTYPE html><html><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>OUR FACEBOOK CHAT</title><link href=\'css/main.css\' rel=\'stylesheet\' type=\'text/css\'><link href=\'themes/'+ theme +'/'+ theme +'.css\' rel=\'stylesheet\' type=\'text/css\'></head><body id="mainDiv"><span id="version">Version 1.0<br /><a href="https://github.com/Smirnoffq/" target="_blank">My Github</a></span><div><div id="main" class="container"><h1 style="text-align: center;">OUR FACEBOOK CHAT</h1>')

members = {}
dates = {}
hours = {'0': 0, '1': 0, '2': 0,'3': 0, '4': 0, '5': 0,'6': 0, '7': 0, '8': 0,'9': 0, '10': 0, '11': 0,'12': 0, '13': 0, '14': 0,'15': 0, '16': 0, '17': 0,'18': 0, '19': 0, '20': 0,'21': 0, '22': 0, '23': 0}
weekDays = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
allWords = {}
emojis = {'&#128054': 0, '&#128049': 0, '&#128045': 0, '&#128057': 0, '&#128048': 0, '&#129418': 0, '&#128059': 0, '&#128060': 0, '&#128040': 0, '&#128047': 0, '&#129409': 0, '&#128046': 0, '&#128055': 0, '&#128061': 0, '&#128056': 0, '&#128053': 0, '&#128586': 0, '&#128585': 0, '&#128586': 0, '&#128018': 0, '&#128020': 0, '&#128039': 0, '&#128038': 0, '&#128036': 0, '&#128035': 0, '&#128037': 0, '&#129414': 0, '&#129413': 0, '&#129417': 0, '&#129415': 0, '&#128058': 0, '&#128023': 0, '&#128052': 0, '&#129412': 0, '&#128029': 0, '&#128027': 0, '&#129419': 0, '&#128012': 0, '&#128026': 0, '&#128030': 0, '&#128028': 0, '&#128375': 0, '&#128376': 0, '&#128034': 0, '&#128013': 0, '&#129422': 0, '&#129410': 0, '&#129408': 0, '&#129425': 0, '&#128025': 0, '&#129424': 0, '&#128032': 0, '&#128031': 0, '&#128033': 0, '&#128044': 0, '&#129416': 0, '&#128051': 0, '&#128011': 0, '&#128010': 0, '&#128006': 0, '&#128005': 0, '&#128003': 0, '&#128002': 0, '&#128004': 0, '&#129420': 0, '&#128042': 0, '&#128043': 0, '&#128024': 0, '&#129423': 0, '&#129421': 0, '&#128014': 0, '&#128022': 0, '&#128016': 0, '&#128015': 0, '&#128017': 0, '&#128021': 0, '&#128041': 0, '&#128008': 0, '&#128019': 0, '&#129411': 0, '&#128330': 0, '&#128007': 0, '&#128001': 0, '&#128000': 0, '&#128063': 0, '&#128062': 0, '&#128009': 0, '&#128050': 0, '&#127797': 0, '&#127876': 0, '&#127794': 0, '&#127795': 0, '&#127796': 0, '&#127793': 0, '&#127807': 0, '&#9752': 0, '&#127808': 0, '&#127885': 0, '&#127883': 0, '&#127811': 0, '&#127810': 0, '&#127809': 0, '&#127812': 0, '&#127806': 0, '&#128144': 0, '&#127799': 0, '&#127801': 0, '&#129344': 0, '&#127803': 0, '&#127804': 0, '&#127800': 0, '&#127802': 0, '&#127758': 0, '&#127757': 0, '&#127759': 0, '&#127765': 0, '&#127766': 0, '&#127767': 0, '&#127768': 0, '&#127761': 0, '&#127762': 0, '&#127763': 0, '&#127764': 0, '&#127770': 0, '&#127773': 0, '&#127774': 0, '&#127771': 0, '&#127772': 0, '&#127769': 0, '&#128171': 0, '&#11088': 0, '&#127775': 0, '&#10024': 0, '&#9889': 0, '&#128293': 0, '&#128165': 0, '&#9732': 0, '&#9728': 0, '&#127780': 0, '&#9925': 0, '&#127781': 0, '&#127782': 0, '&#127752': 0, '&#9729': 0, '&#127783': 0, '&#9928': 0, '&#127785': 0, '&#127784': 0, '&#9731': 0, '&#9924': 0, '&#10052': 0, '&#127788': 0, '&#128168': 0, '&#127786': 0, '&#127787': 0, '&#127754': 0, '&#128167': 0, '&#128166': 0, '&#9748': 0, '&#128512': 0, '&#128513': 0, '&#128514': 0, '&#129315': 0, '&#128515': 0, '&#128516': 0, '&#128517': 0, '&#128518': 0, '&#128521': 0, '&#128522': 0, '&#128523': 0, '&#128526': 0, '&#128525': 0, '&#128536': 0, '&#128535': 0, '&#128537': 0, '&#128538': 0, '&#128578': 0, '&#129303': 0, '&#129321': 0, '&#129300': 0, '&#129320': 0, '&#128528': 0, '&#128529': 0, '&#128566': 0, '&#128580': 0, '&#128527': 0, '&#128547': 0, '&#128549': 0, '&#128558': 0, '&#129296': 0, '&#128559': 0, '&#128554': 0, '&#128555': 0, '&#128564': 0, '&#128524': 0, '&#128539': 0, '&#128540': 0, '&#128541': 0, '&#129316': 0, '&#128530': 0, '&#128531': 0, '&#128532': 0, '&#128533': 0, '&#128579': 0, '&#129297': 0, '&#128562': 0, '&#128577': 0, '&#128534': 0, '&#128542': 0, '&#128543': 0, '&#128548': 0, '&#128546': 0, '&#128557': 0, '&#128550': 0, '&#128551': 0, '&#128552': 0, '&#128553': 0, '&#129327': 0, '&#128556': 0, '&#128560': 0, '&#128561': 0, '&#128563': 0, '&#129322': 0, '&#128565': 0, '&#128545': 0, '&#128544': 0, '&#129324': 0, '&#128567': 0, '&#129298': 0, '&#129301': 0, '&#129314': 0, '&#129326': 0, '&#129319': 0, '&#128519': 0, '&#129312': 0, '&#129313': 0, '&#129317': 0, '&#129323': 0, '&#129325': 0, '&#129488': 0, '&#129299': 0, '&#128520': 0, '&#128127': 0, '&#128121': 0, '&#128122': 0, '&#128128': 0, '&#128123': 0, '&#128125': 0, '&#129302': 0, '&#128169': 0, '&#128570': 0, '&#128568': 0, '&#128569': 0, '&#128571': 0, '&#128572': 0, '&#128573': 0, '&#128576': 0, '&#128575': 0, '&#128574': 0, '&#128584': 0}
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
for w in range(messagesAmount-1, -1, -1):
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
	if(monthLang == "pl"):
		hour = date.split()[4]
		hour = hour.split(":")[0]
	elif(monthLang == "en"):
		hour = date.split()[5]
		identifier = hour[-2:]
		print(hour + " >>> " + identifier)
		hour = hour.split(":")[0]
		if(identifier == "pm"):
			hour = str(int(hour) + 12)

	m = message.encode("ascii", 'xmlcharrefreplace')
	for x in emojis:
		if str(x) in str(m):
			emojis[x] += 1
	
	# https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
	words = re.findall(r"[\w']+", message)
	totalWords += len(words)

	for word in words:
		word = word.lower()
		if word in allWords:
			allWords[word] += 1
		else:
			allWords[word] = 1

	if hour in hours.keys():
		hours[hour] += 1
	else:
		hours[hour] = 1

	weekD = fbDateToWeekday(date, monthLang)
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
date1 = messages[messagesAmount-1].find('span', attrs={'class': 'meta'}).text.replace(",", "").split()
if(monthLang.lower() == "pl"):
	fDay = date1[0]
	fMonth = monthToNum(date1[1])
	fYear = date1[2]
elif(monthLang.lower() == "en"):
	fDay = date1[2]
	fMonth = monthToNum(date1[1])
	fYear = date1[3]
firstDate = datetime.date(int(fYear), int(fMonth), int(fDay))

date2 = messages[0].find('span', attrs={'class': 'meta'}).text.replace(",", "").split()
if(monthLang.lower() == "pl"):
	sDay = date2[0]
	sMonth = monthToNum(date2[1])
	sYear = date2[2]
elif(monthLang.lower() == "en"):
	sDay = date2[2]
	sMonth = monthToNum(date2[1])
	sYear = date2[3]
secondDate = datetime.date(int(sYear), int(sMonth), int(sDay))

delta = secondDate - firstDate


index.write('<div class="block"><h1>Totals</h1>')
index.write('<div class="md-3"><h4>'+ str(delta.days + 1) +'</h4><h5>Days</h5></div>')
index.write('<div class="md-3"><h4>'+ str(totalMessages) +'</h4><h5>Messages</h5></div>')
index.write('<div class="md-3"><h4>'+ str(totalWords) +'</h4><h5>Words</h5></div>')
index.write('</div>')



# AVERAGES


print("Counting averages...")
index.write('<div class="block"><h1>Averages</h1>')
index.write('<div class="md-2"><h4>'+ str(round(totalWords/totalMessages, 2)) +'</h4><h5>Length of a message</h5></div>')
index.write('<div class="md-2"><h4>'+ str(round(totalMessages/(delta.days + 1), 2)) +'</h4><h5>Messages per day</h5></div>')
index.write('</div>')


# CHARTS
print("Drawing charts...")
index.write('<div class="block"><h4>Who texts the most?</h4><div class="charts"><div id="chart-area"></div></div><h4>Activity by Day</h4><div class="charts"><div id="chart-area2"></div></div><h4>Timeline</h4><div class="charts"><div id="chart-area3"></div></div><h4>Activity by Week</h4><div class="charts"><div id="chart-area4"></div></div><h4>Top emoji*</h4><div class="charts"><div id="chart-area5"></div></div><h4>Top words</h4><div class="charts"><div id="chart-area6"></div></div><h6>* Counts how many times found in chat, not in message ( if in one message there were 3 &#x1F618, it counts it as 1)</h6></div>')




index.write('<script type="text/javascript" src="themes/'+ theme +'/'+theme+'.js"></script>')
index.write('<script type="text/javascript" src="js/main.js"></script><script src="js/plotly-latest.min.js"></script><script type="text/javascript">window.onload = function() {	Plotly.newPlot(\'chart-area\', data, layout);	Plotly.newPlot(\'chart-area2\', data2);	Plotly.newPlot(\'chart-area3\', data3);	Plotly.newPlot(\'chart-area4\', data4);	Plotly.newPlot(\'chart-area5\', data5);	Plotly.newPlot(\'chart-area6\', data6);}</script></body></html>')

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

mainjs.write('var data5 = [  {    x: [')

i = 0
for key in sorted(emojis, key=emojis.__getitem__, reverse=True):
	mainjs.write("String.fromCodePoint(" + hex(int(key[2:])) + "),")
	i += 1
	if (i == 10): break

mainjs.write('],    y: [')

i = 0
for key in sorted(emojis, key=emojis.__getitem__, reverse=True):
	mainjs.write(str(emojis[key]) + ",")
	i += 1
	if (i == 10): break


mainjs.write('],    type: \'bar\',    marker: {   \n\n   color: "#d83434", \n\n },  }];')


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
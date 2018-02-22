#  -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


#theme = input("Theme name: ")
theme = "valentines"

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
pAmount = len(p)

# create index.html file
index = open("../index.html", "w", encoding="utf-8")
index.write('<!DOCTYPE html><html><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>OUR FACEBOOK CHAT</title><link href=\'css/main.css\' rel=\'stylesheet\' type=\'text/css\'><link href=\'themes/'+ theme +'.css\' rel=\'stylesheet\' type=\'text/css\'></head><body id="mainDiv"><div><div id="main" class="container"><h1 style="text-align: center;">OUR FACEBOOK CHAT</h1><div class="block">')

members = []
startDate = ""
mostActiveDay = ""
mostActiveDayMessagesCount = 0
totalDays = 0
totalMessages = messagesAmount
totalWords = 0
averageMessageLen = 0
messagesPerDay = 0


print("Finding users: 0  ", end="")
for w in range(0, messagesAmount):
	user = messages[w].find('span', attrs={'class': 'user'})
	user = user.text

	if (user not in members):
		members.append(user)
	
	if pAmount%10 == 0: 
		for x in range(0, len(str(pAmount))): print('\b', end="")
		print(str(pAmount), end="")

	pAmount += 1

index.write('<h3>Members: ' + ', '.join(members) + '</h3>')

index.close()
import praw
from random import randint

user_agent = ("ratBat 0.12")
r = praw.Reddit(user_agent = user_agent)

sublist = ["india", "bakchodi", "indianews", "atheismindia", "tilinindia", "desicringe", "IndianPeopleFacebook", "BrownBubbas", "hindi", "indianfood"]

subTitle = []
subText = []
subLink = []

def getdata(subreddit):
	sub = r.get_subreddit(subreddit)
	for subm in sub.get_new(limit = 200):
		subTitle.append("{[ " + subm.title +" ]}")
		if (subm.selftext != ""): 
			subText.append("{[ " + subm.selftext + " ]}")
		else:
			subLink.append(subm.url)

for i in range(len(sublist)):
        getdata(sublist[i])

def markovmod(myList, ):
	newword = "{["
	mysent = ""
	while (newword.strip() != "]}"):	
		match = [s for s in myList if newword in s]
		newword = newword.strip()
		posword = []
		for i in range(len(match)):
			wordlist = match[i].split()		
			posword.append(wordlist[wordlist.index(newword) + 1])		
		
		sel = randint(0, max(len(posword) - 1, 0))
		try:
			newword = posword[sel]
			pt = ['"', "(", "[", "'"]
			if (newword[0] in pt):
				selp = pt[pt.index(newword[0])]
				wordlist = match[sel].split()
				for i in range(wordlist.index(newword) + 1, len(wordlist)):			
					newword = newword + wordlist[i]
					if (newword[len(newword) - 1] == selp): break
					if (newword.count(" ") > 5): 
						newword = newword + selp
						break
		except:
			break
		mysent = mysent + " " + newword
		if (" " in newword):
			newword = newword.split()
			newword = newword[len(newword) -1]
		newword  = " " + newword + " "
		
	mysent = mysent.replace("]}", "")
	print(mysent)
	return mysent;

myTitle = ""
while (myTitle.count("") < 5):
	myTitle = markovmod(subTitle)
	
myselftext = markovmod(subText)


lno = randint(0, len(subLink) - 1)
mylink = subLink[lno]

REDDIT_USERNAME = 'kulchabot'
REDDIT_PASS = 'xchange'

r.login(REDDIT_USERNAME, REDDIT_PASS)
toru = randint(0,1)
print(toru)
raw_input()

	


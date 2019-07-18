'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)

# print(type(tweetData))
# print(type(tweetData[1]))
# We can close the file now that we have locally stored the data.

# print(tweetData[1]["favorite_count"])
tweetFile.close()



# sum = 0
# for i in range(0,len(tweetData)):
# 	if "favorite_count" in tweetData[i]:
# 		sum += tweetData[i]["favorite_count"]
# 	else:
# 		sum += 0
# 	t = sum/len(tweetData)
# print(t)


# sum = 0
# num = 0
# for tweet in tweetData:
# 	# tweet = tweetData[i]
# 	if "favorite_count" not in tweet:
# 		sum += 0
# 	else:
# 		# print(tweet['favorite_count'])
# 		num += 1
# 		sum += tweet["favorite_count"]
# avg = sum/num
# print(avg)


tweetlist = []
for i in range(len(tweetData)):
	tweetlist.append(tweetData[i]["text"])
# print(tweetlist)

polarityList = []
for i in tweetlist:
	blob1 = TextBlob(i)
	polar1 = blob1.polarity
	polarityList.append(polar1)
print(polarityList)

list1 = []
for i in range(len(tweetData)):
	dictionaree = {}
	dictionaree["t_id"] = tweetData[i]["id"]
	dictionaree["polarity"] = polarityList[i]
	dictionaree["tweet"] = tweetData[i]
	list1.append(dictionaree)
# print(tweetData)

tweetstring = " "
for tweet in tweetlist:
	tweet = tweet + " "
	tweetstring += tweet
# print(tweetstring)

'''
# Word Cloud
text = "hello hello there its me fion fion"
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
plt.figure(figsize = (10, 10), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('fionschart.png')
'''

n, bins, patches = plt.hist(polarityList)
print(min(polarityList), max(polarityList))
plt.axis([-0.55, 1.05, 0.0, 50])


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.grid()
plt.show()
plt.savefig('fionschart.png')
# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.

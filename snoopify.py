# by ME
# snoopify.py
# changes comments into snoop dog/lions language

import praw 
import re 
import pprint
import os

#gets password
with open('passwords.txt', 'r') as passFile:
	password = passFile.read()

with open('user.txt', 'r') as uFile:
	userName = uFile.read()


r = praw.Reddit('Snoop Translator by u/kmurph45 v0.1.')
r.login(str(userName)[:-1], str(password)[:-1])

#main loop - look at posts from /r/all - switch to /r/test for debugging
if not os.path.isfile("replies.txt"):
    beenDone = []
else:
    print "Loading previous reply ids"
    with open("beendDone.txt", "r") as f:
        replies = f.read()
        replies = replies.split("\n")
        replies = filter(None, replies)


all_comments = r.get_comments('tessst')


#Maintain a list of comments that have been translated so we don't spam

snoopComment = ''
punct = ''
signature = 'Snoop Dog be like \n\n'
PUNCTUATION = (".", ",", ":", "?", "!", ";")

#while True:
	


#evaluate comments without worrying about their rank
for comment in all_comments:
	if comment.id not in beenDone:
	
	#Find comments containing "Pig Latin"
		if "snoopIt" in comment.body and comment.id not in beenDone.read():
			words = re.split(' ', comment.body)
		#words is a list of the words in the comment
		
			for entry in words:
				
				last = len(entry) 
				last2 = last - 1 
						#if it starts with a vowel, just add -ay
				snoopComment += entry[0:last2] + "izzle" + " "
			
			#clear punctuation for next word
				punct = ''

		#comment result
			comment.reply(signature + snoopComment)
			snoopComment = ''
		#clear for next comment
			our_comment = ''

			beenDone.write(comment.id)
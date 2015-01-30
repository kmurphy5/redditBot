# by ME
# snoopify.py
# changes comments into snoop dog/lions language

import praw, re

#gets password
with open('passwords.txt', 'r') as passFile:
	password = passFile.read()
	
	with open('user.txt', 'r') as uFile:
		userName = uFile.read()


r = praw.Reddit('Snoop Translator by u/kmurph45 v0.1.')
r.login(str(userName)[:-1], str(password)[:-1])

#main loop - look at posts from /r/all - switch to /r/test for debugging

all_comments = r.get_comments('tessst')


#Maintain a list of comments that have been translated so we don't spam
beenDone = set()
snoopComment = ''
punct = ''
signature = 'Snoop Dog be like \n\n'
PUNCTUATION = (".", ",", ":", "?", "!", ";")


#evaluate comments without worrying about their rank
for comment in all_comments:

	#Find comments containing "Pig Latin"
	if "snoopIt" in comment.body and comment.id not in beenDone:
		words = re.split(' ', comment.body)
		#words is a list of the words in the comment
		
		for entry in words:
			last = len(entry) -1 
						#if it starts with a vowel, just add -ay
		our_comment += entry[0:last] + "izzle" + punct + " "
			
			#clear punctuation for next word
		punct = ''

		#comment result
		comment.reply(signature + snoopComment)

		#clear for next comment
		our_comment = ''

		beenDone.add(comment.id)
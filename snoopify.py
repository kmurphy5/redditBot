# by ME
# snoopify.py
# changes comments into snoop dog/lions language

import praw 
import re 
import pprint
import os
import time
import sys

#gets password
with open('passwords.txt', 'r') as passFile:
	password = passFile.read()

with open('user.txt', 'r') as uFile:
	userName = uFile.read()


r = praw.Reddit('Snoop Translator by u/kmurph45 v0.1.')
r.login(str(userName)[:-1], str(password)[:-1])


if not os.path.isfile("beenDone.txt"):
    beenDone = []
else:
    print "Loading previous reply ids"
    with open("beenDone.txt", "r") as s:
        beenDone = s.read()
        beenDone = beenDone.split("\n")
        beenDone = filter(None, beenDone)


#used for testing
#all_comments = r.get_subreddit('tessst')
all_comments = r.get_subreddit('umw_cpsc470Z')


#Maintain a list of comments that have been translated so we don't spam

snoopComment = ''
punct = ''
signature = 'Snoop Dog would say \n\n'
punctuation = (".", ",", ":", "?", "!", ";")
vow = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')




while True:
	if not os.path.isfile("beenDone.txt"):
	    beenDone = []
	else:
	    print "Loading previous reply ids"
	    with open("beenDone.txt", "r") as f:
	        beenDone = f.read()
	        beenDone = beenDone.split("\n")
	        beenDone = filter(None, beenDone)
	


#evaluate comments for reply
	for submission in all_comments.get_hot(limit=10):
		flat_comments = praw.helpers.flatten_tree(submission.comments)
		for comment in flat_comments:
			
			if "snoopIt" in comment.body and comment.id not in beenDone:
				words = re.split(' ', comment.body)
				removeCall = words.index('snoopIt')
		#remove snoopIt from comment 
				words.pop(removeCall)
		#words is a list of the words in the comment
		
				for entry in words:
					
					last = len(entry)
					
					if last < 3:
						#no two letters words are changed
						snoopComment += entry[0:last] + " "
					elif last < 5 and last > 2:
						snoopComment += entry[0:last] + "izle" + " "
					else:
						#shortened longer words
						last = last -1
						print "in greator than 4 loop"
						if entry[last] in vow:
							print "in vow if"
							last = last -1 
							snoopComment += entry[0:last] + "izle" + " "
					
						else:
							snoopComment += entry[0:last] + "izle" + " "
							print " in last else"
							
					
					
						
				
			
			#clear punctuation for next word
					punct = ''

		#comment result
				print "reply to comment ", comment.id
				#check what camment replied to 
				try:
					
					comment.reply(signature + snoopComment)
					beenDone.append(comment.id)
					break
				except Exception:
					print "over rate limit"
				#add comment id to array
			
				
			snoopComment = ''
		#clear for next comment
		

	print "Saving ids to file"
	with open("beenDone.txt", "w") as f:
		for i in beenDone:
			f.write(i + "\n")
		
						
	#controls how often the program runs in seconds	
	time.sleep(600)
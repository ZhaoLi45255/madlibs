
## Mad Libs generator

import time
import string
import nltk

## All strings beginning with "__" are input signs.
## __PROPN = proper noun
## __VRB = verb

lineList = [] ## List that will contain all the lines in the text.
finalStory = "" ## The string that will contain the final version of the mad lib.
punctExceptions = [string.punctuation, ".", "'s", \
				   "'t", "'m", "'ve"] ## All the punctuation and contractions to skip over.

with open("easy/testfile1.txt") as file:
	for line in file:
		lineList.append(line)
"""
for i in lineList:
	print(i, end="")
	time.sleep(1)
print()
"""

for line in lineList:
	count = 0
	for word in line.split():
		question = "" ## Always reset the question
		wordToAdd = word 
		if word in punctExceptions: ## If the word is a punctuation or a contraction, do not add a space.
			finalStory += wordToAdd
			continue
		else:
			if count != 0: ## Make sure that no space is added before the first word.
				finalStory += " "
		if word == "__PROPN":
			question = "Name a proper noun: "
		elif word == "__VRB":
			question = "Name a verb: "
		if question != "": ## Question should be blank if it hasn't detected an input sign
			wordToAdd = input(question)
		finalStory += wordToAdd ## Add the word to the final version of the story.
		count += 1
		time.sleep(1)
	finalStory += "\n"
print(finalStory)
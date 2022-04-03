# Mad Libs generator

import time
import string
import nltk
import os
import random

def main():
	finalStory = "" # The string that will contain the final version of the mad lib.
	lineList = [] # List that will contain all the lines in the text.
	randomizer = False
	print("Welcome to Mad Libs Generator.\n"\
		"There are two modes: Easy Mode and Random Mode.\n"\
		"In Easy Mode, you fill in spots already decided for you.\n"\
		"In Random Mode, you fill in spots that will be randomly chosen."\
	   )
	while True:
		answer = input("Would you like to play Easy Mode? Say Yes or No.\n")
		if answer.lower() == "yes":
			randomizer = False
			with open("easy/testfile1.txt") as file:
				for line in file:
					lineList.append(line)
			break
		elif answer.lower() == "no":
			randomizer = True
			with open("random/testfile1.txt") as file:
				for line in file:
					lineList.append(line)
			break
		else:
			print("Please try again.")
	finalStory = fillStory(lineList, randomizer)
	print(finalStory)

def fillStory(lineList, randomizer):
	result = ""
	count = 0 # Keep track of how many lines have been gone through.
	for i in lineList:
		tokens = nltk.word_tokenize(i)
		tagged = nltk.pos_tag(tokens)
		count += 1
		firstWord = True;
		for j in tagged:
			wordToAdd = j[0]
			if isPunc(j) == False and firstWord == False: ## Add a space if the word is not punctuation, and it is not the first word.
				result += " "
			if randomizer == True and j[1] in replaceTags: # Only randomize the word half the time.
				randNum = random.randint(1, 10)
				if randNum <= 5:
					wordToAdd = j[1] # Set the word to a tag to be replaced afterwards.
			question = whichQuestion(wordToAdd) # Ask for the user's input to replace the tag with.
			if question != "": # If there is no question, just add the word to the result.
				wordToAdd = input(question)
			if firstWord == True:
				wordToAdd = wordToAdd.capitalize()
			result += wordToAdd
			firstWord = False
		if count != len(lineList): # Do not add a new line after we are done with all the lines.
			result += "\n" # Start a new line after the current line is done
		firstWord = True
	return result

replaceTags = ["JJ", "JJR", "JJS", "NN", "NNP", "NNS", "RB", "RBR", "RBS", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
noReplaceTags = ["CC", "CD", "DT", "EX", "IN", "LS", "MD", "PDT", "POS", "PRP", "PRP$", "RP", "TO", "WDT", "WP", "WRB"]
"""
def randStory(lineList):
	try:
		os.remove("testcase.txt")
	except OSError:
		pass
"""

# Check whether the word has any punctuation in it.
def isPunc(word):
	if "'" in word[0] or (word[1] not in replaceTags and word[1] not in noReplaceTags):
		return True
	return False

# Return a question response if the word is to be replaced.
def whichQuestion(word):
	question = ""
	if "NN" == word:
		question = "Name a singular noun: "
	elif "NNP" == word:
		question = "Name a proper noun: "
	elif "NNS" == word:
		question = "Name a plural noun: "
	elif "VB" == word:
		question = "Name a verb: "
	elif ""
	elif "VBG" == word:
		question = "Name an -ing word: "
	elif "JJ" == word:
		question = "Name an adjective: "
	return question

if __name__ == "__main__":
    main()
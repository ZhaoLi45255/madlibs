# Mad Libs generator

import time
import string
import nltk
import os

def main():
	finalStory = "" # The string that will contain the final version of the mad lib.
	lineList = [] # List that will contain all the lines in the text.
	with open("easy/testfile1.txt") as file:
		for line in file:
			lineList.append(line)
	#randStory(lineList)
	finalStory = fillStory(lineList)
	print(finalStory)

def fillStory(lineList):
	result = ""
	count = 0 # Keep track of how many lines have been gone through.
	for i in lineList:
		tokens = nltk.word_tokenize(i)
		tagged = nltk.pos_tag(tokens)
		count += 1
		firstWord = True;
		print(tagged)
		for j in tagged:
			question = whichQuestion(j[0])
			wordToAdd = j[0]
			if isPunc(j) == False and firstWord == False: ## Add a space if the word is not punctuation, and it is not the first word.
				result += " "
			if question != "": # If there is no question, just add the word to the result.
				wordToAdd = input(question)
			result += wordToAdd
			firstWord = False
		if count != len(lineList): # Do not add a new line after we are done with all the lines.
			result += "\n" # Start a new line after the current line is done
		firstWord = True
	return result

replaceTags = ["JJ", "JJR", "JJS", "NN", "NNP", "NNS", "RB", "RBR", "RBS", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
noReplaceTags = ["CC", "CD", "DT", "EX", "IN", "LS", "MD", "PDT", "POS", "PRP", "PRP$", "RP", "TO", "WDT", "WP", "WRB"]

def randStory(lineList):
	try:
		os.remove("testcase.txt")
	except OSError:
		pass
	with open("testcase.txt", "x") as f:
		for i in lineList:
			tokens = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(tokens)
			for j in tagged:
				if isPunc(j) == True:
					print(j[0])
				if j[1] not in replaceTags:
					f.write(j[0] + " ")
			f.write("\n")

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
	elif "VBG" == word:
		question = "Name an -ing word: "
	elif "JJ" == word:
		question = "Name an adjective: "
	return question

if __name__ == "__main__":
    main()
# Mad Libs generator

import time
import string
import nltk
import os

# All strings beginning with "_" are input signs.
# @PROPN = proper noun
# _VRB = verb 
# _ADJ = adjective
# _N = singular noun
# _PLN = plural noun
# _ING = verb ending in "-ing"
# _NUM = number
# _POSSN = possessive noun

def main():
	finalStory = "" # The string that will contain the final version of the mad lib.
	lineList = [] # List that will contain all the lines in the text.
	with open("easy/testfile1.txt") as file:
		for line in file:
			lineList.append(line)
	#randStory(lineList)
	fillStory(finalStory, lineList)

def fillStory(result, lineList):
	lastPunc = " "
	count = 0 # Keep track of how many lines have been gone through.
	for line in lineList:
		for word in line.split():
			question = "" # Always reset the question
			wordToAdd = word
			if lastPunc != " ":
				result += " "
			lastPunc = " " # Reset the last punctuation mark
			if word[0] == "_":
				check = word[len(word) - 1]
				if check == "." or check == "?" or check == "!" or check == ",":
					lastPunc = check
			question = whichQuestion(word)
			if question != "": # No input is asked for if the question is blank
				wordToAdd = input(question)
			result += wordToAdd + lastPunc # Add the word and either a space or a punctuation mark to the final story.
		count += 1
		if count != len(lineList): # Do not add a new line after we are done with all the lines.
			result += "\n" # Start a new line after the current line is done
		lastPunc = " "
	print(result)

replaceTags = ["JJ", "JJR", "JJS", "NN", "NNP", "NNS", "RB", "RBR", "RBS", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
noReplaceTags = ["CC", "CD", "DT", "EX", "IN", "LS", "MD", "PDT", "POS", "PRP", "RP", "TO", "WDT", "WP", "WRB"]

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
				if j[1] not in replaceTags:
					f.write(j[0] + " ")
				else:
					print(j)
					print("Hello, world!")
			f.write("\n")

def whichQuestion(word):
	question = ""
	if "_PROPN" in word:
		question = "Name a proper noun: "
	elif "_VRB" in word:
		question = "Name a verb: "
	elif "_ADJ" in word:
		question = "Name an adjective: "
	elif "_NOUN" in word:
		question = "Name a noun: "
	elif "_PLN" in word:
		question = "Name a plural noun: "
	elif "_ING" in word:
		question = "Name an -ing word: "
	elif "_POSSN" in word:
		question = "Name a possessive noun: "
	return question

if __name__ == "__main__":
    main()
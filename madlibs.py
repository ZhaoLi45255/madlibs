# Mad Libs generator

import time
import string

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
	with open("easy/testfile2.txt") as file:
		for line in file:
			lineList.append(line)
	fillStory(finalStory, lineList)

def fillStory(result, lineList):
	lastPunc = " "
	for line in lineList:
		count = 0
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
			elif "_NUM" in word:
				question = "Name a number: "
			elif "_POSSN" in word:
				question = "Name a possessive noun: "

			if question != "": # No input is asked for if the question is blank
				wordToAdd = input(question)
			result += wordToAdd + lastPunc # Add the word and either a space or a punctuation mark to the final story.
			count += 1
			time.sleep(1)
		result += "\n" # Start a new line after the current line is done
	print(result)

if __name__ == "__main__":
    main()
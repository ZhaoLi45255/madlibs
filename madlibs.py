# Mad Libs generator

import time
import string

# All strings beginning with "__" are input signs.
# __PROPN = proper noun
# __VRB = verb 
# __ADJ = adjective
# __N = singular noun
# __PLN = plural noun
# __ING = verb ending in "-ing"
# __NUM = number

punctExceptions = ["'s", "'t", "'m", "'ve", "'d", "'ll", "'re"] # All the punctuation and contractions to skip over.
for char in string.punctuation: # Add the punctuation marks
		punctExceptions.append(char)

def main():
	finalStory = "" # The string that will contain the final version of the mad lib.
	lineList = [] # List that will contain all the lines in the text.
	with open("easy/testfile2.txt") as file:
		for line in file:
			lineList.append(line)
	fillStory(finalStory, lineList)

def fillStory(result, lineList):
	for line in lineList:
		count = 0
		for word in line.split():
			question = "" # Always reset the question
			wordToAdd = word 
			if word in punctExceptions: # If the word is a punctuation mark or a contraction, do not add a space.
				result += wordToAdd
				continue
			else:
				if count != 0: # Make sure that no space is added before the first word.
					result += " "

			if word == "__PROPN":
				question = "Name a proper noun: "
			elif word == "__VRB":
				question = "Name a verb: "
			elif word == "__ADJ":
				question = "Name an adjective: "
			elif word == "__N":
				question = "Name a noun: "
			elif word == "__PLN":
				question = "Name a plural noun: "
			elif word == "__ING":
				question = "Name an -ing word: "
			elif word == "__NUM":
				question = "Name a number: "

			if question != "": # No input is asked for if the question is blank
				wordToAdd = input(question)
			result += wordToAdd # Add the word to the final version of the story.
			count += 1
			time.sleep(1)
		result += "\n" # Start a new line after the current line is done
	print(result)

if __name__ == "__main__":
    main()
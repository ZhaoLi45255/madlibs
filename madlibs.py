
## Mad Libs generator

import time
## import nltk

story = ["There was a boy named ", "__PROPN__", ".\n", "He liked to ", "__VRB__"]
finalStory = ""

for i in range(0, len(story)):
	question = ""
	if story[i] == "__PROPN__":
		print("Hello, world!")
		question = "Name a proper noun: "
	elif story[i] == "__VRB__":
		print("This is a verb!")
		question = "Name a verb: "
	if question != "":
		myInput = input(question)
		story[i] = myInput
	question = ""
	finalStory += story[i]
	time.sleep(1)
print(finalStory)

"""
with open("testfile.txt") as file:
	for line in file:
		tokens = nltk.word_tokenize(line)
		tagged = nltk.pos_tag(tokens)
		print(tokens)
		print(tagged)
"""

## Mad Libs generator

import time

words = [
	"Name a noun: ",
	"Name an adjective: ",
	"Name a proper noun: ",
	"Name a verb: ",
	"Name an adverb: "
]

answers = []
for i in range(0, len(words)):
	myInput = input(words[i])
	answers.append(myInput)
	time.sleep(1)
#coding: utf-8
import random

print "Please input sentence"
sentence = raw_input()
sentence = sentence.replace(".","") #.の除去
sentence = sentence.replace(",","") #,の除去
sentence_list = sentence.split(" ")

k = len(sentence_list)
word_list = []
for i in xrange(k):
	word_list = list(sentence_list[i])
	if len(word_list) > 4:
		head = word_list[0]
		tail = word_list[len(word_list)-1]

		del word_list[0]
		del word_list[len(word_list)-1]

		random.shuffle(word_list)

		word_list.insert(0,head)
		word_list.insert(len(word_list),tail)

	sentence_list[i] = "".join(word_list)

print " ".join(sentence_list)+"."
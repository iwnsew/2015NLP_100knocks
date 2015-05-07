#coding: utf-8
import random

def Typoglycemia(text):
	text = text.replace(".","") #.の除去
	text = text.replace(",","") #,の除去
	text = text.replace(":","") #:の除去
	text = text.replace(";","") #;の除去
	text_list = text.split(" ")

	return text_list

print "Please input sentence"
sentence = raw_input()
sentence_list = Typoglycemia(sentence)

if len(sentence_list) <= 4:
	print ' '.join(sentence_list)
else:
	head = sentence_list[0]
	tail = sentence_list[len(sentence_list)-1]

	del sentence_list[0]
	del sentence_list[len(sentence_list)-1]

	random.shuffle(sentence_list)

	sentence_list.insert(0,head)
	sentence_list.insert(len(sentence_list),tail)

	print ' '.join(sentence_list)
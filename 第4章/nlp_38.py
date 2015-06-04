#coding:utf-8
import nlp_30
from collections import Counter
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	pos_list = []
	pos_list_word = []
	pos_list_cnt = []
	for morpheme in morpheme_list:
		pos_list.append(morpheme["pos"])
	counter = Counter(pos_list)
	for word, cnt in counter.most_common():
 		# print word, cnt
 		word = unicode(word,encoding='utf-8')
 		pos_list_word.append(word)
 		pos_list_cnt.append(cnt)

 	X =[]
	for x in xrange(len(pos_list_word)):
		X.append(x)
	Y = pos_list_cnt

	plt.barh(X,Y, align="center")  # 中央寄せ
	plt.yticks(X, pos_list_word)
	plt.show()

if __name__ == '__main__':
	main()
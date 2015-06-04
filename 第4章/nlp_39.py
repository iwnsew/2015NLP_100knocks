#coding:utf-8
import nlp_30
from collections import Counter
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	pos_list = []
	pos_frequency_list = []
	for morpheme in morpheme_list:
		pos_list.append(morpheme["surface"])
	counter = Counter(pos_list)
	rank = 1
	cnt_compare = 0
	ranking = []
	for word, cnt in counter.most_common():
		if cnt < cnt_compare:
			rank = rank + 1
		cnt_compare = cnt
 		# print rank,":",word, cnt
 		ranking.append(cnt)
 		# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ←R
 	# print sorted(set(ranking))
 	# print len(set(ranking))
 	pos_frequency_list = sorted(set(ranking), reverse=True)
 	X = []
	for x in xrange(len(set(ranking))):
		# print x
		num = x + 1
		# print num
		X.append(num)
	Y = pos_frequency_list
	# print X
	# print Y

	plt.plot(X, Y)
	plt.xscale("log")
	plt.yscale("log")
	plt.show()
if __name__ == '__main__':
	main()
# ジフの法則とは、出現頻度がk番目に大きい要素が全体に占める割合が1/kに比例するという経験則
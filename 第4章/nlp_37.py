#coding:utf-8
import nlp_30
from collections import Counter

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	word_list = []
	for morpheme in morpheme_list:
		word_list.append(morpheme["surface"])
	counter = Counter(word_list)
	for word, cnt in counter.most_common(10):
 	   print word, cnt
				
if __name__ == '__main__':
	main()
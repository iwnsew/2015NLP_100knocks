#coding:utf-8
import re
import collections

def mecab_morpheme():
	readfile = open("neko.txt.mecab", "r")
	txt = readfile.readlines()

	others_list = []
	morpheme_list = []

	for line in txt:
		pattern = re.compile("")
		pattern = re.compile("(?P<surface>.+?)(\s)(?P<others>.+)")
		format = re.finditer(pattern, line)
		for match in format:
			surface = match.group("surface")
			others_list = match.group("others").split(",")
			base = others_list[6] #基本形
			pos = others_list[0] #品詞
			pos1 = others_list[1] #品詞細分類1

			morpheme_list.append({"surface": surface, "base": base, "pos": pos, "pos1": pos1})

	readfile.close()
	return morpheme_list

def main():
	morpheme_list = mecab_morpheme()
	for morpheme in morpheme_list:
		print "表層系:", morpheme["surface"]
		print "基本形:", morpheme["base"]
		print "品詞:", morpheme["pos"]
		print "品詞細分類:", morpheme["pos1"]
		print "------------"

if __name__ == '__main__':
	main()
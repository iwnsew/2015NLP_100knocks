#coding:utf-8
import nlp_30

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	noun_sahen = set([])
	for morpheme in morpheme_list:
		if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続":
			noun_sahen.add(morpheme["surface"])
	for noun in noun_sahen:
		print noun


if __name__ == '__main__':
	main()

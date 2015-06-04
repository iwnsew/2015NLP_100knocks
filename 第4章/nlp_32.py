#coding:utf-8
import nlp_30

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	verb_surface = set([])
	for morpheme in morpheme_list:
		if morpheme["pos"] == "動詞":
			verb_surface.add(morpheme["base"])
	for verb in verb_surface:
		print verb

if __name__ == '__main__':
	main()
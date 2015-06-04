#coding:utf-8
import nlp_30

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	noun_list = []
	output_noun_list = []
	for i in range(len(morpheme_list)-1):
		if morpheme_list[i]["pos"] == "名詞":
			noun_list.append(morpheme_list[i]["surface"])
		else:
			noun_list = []

		if len(noun_list) > 1:
			if morpheme_list[i+1]["pos"] == "名詞":
				pass
			else:
				for word in noun_list:
					output_noun_list.append(word)
				output_noun_list.append("\n")
	for j in output_noun_list:
		print j,
if __name__ == '__main__':
	main()
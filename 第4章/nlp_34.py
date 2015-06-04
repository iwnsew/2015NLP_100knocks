#coding:utf-8
import nlp_30

def main():
	morpheme_list = nlp_30.mecab_morpheme()
	noun_sahen = set([])
	for i in range(1, len(morpheme_list)-1):
		if morpheme_list[i]["surface"] == "の":
			if morpheme_list[i-1]["pos"] == "名詞" and morpheme_list[i+1]["pos"] == "名詞":
				print "------"
				print morpheme_list[i-1]["surface"] + morpheme_list[i]["surface"] + morpheme_list[i+1]["surface"]
				
if __name__ == '__main__':
	main()
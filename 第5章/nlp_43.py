# coding:utf-8
import nlp_41
def main():
	all_chunk_list = nlp_41.make_chunk()
	for line in all_chunk_list:
		for chunk_element in line:
			sentence = "";dst_sentence = ""
			pos_list = [];dst_pos_list = []
			for mor in chunk_element.morphs:
				pos_list.append(mor.pos)
				if mor.surface == "。" or mor.surface == "、":
					pass
				else:
					sentence += mor.surface
			if chunk_element.dst != -1:
				for dst_mor in line[chunk_element.dst].morphs:
					dst_pos_list.append(dst_mor.pos)
					if dst_mor.surface == "。" or dst_mor.surface == "、":
						pass
					else:
						dst_sentence += dst_mor.surface
			if "名詞" in pos_list and "動詞" in dst_pos_list:
				print sentence,"\t",dst_sentence

if __name__ == "__main__":
	main()
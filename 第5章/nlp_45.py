# coding:utf-8
import nlp_41

#############		UNIXを使った出力ができていない		###################
def main():
	all_chunk_list = nlp_41.make_chunk()
	for chunk_list in all_chunk_list:
		for chunk_element in chunk_list:
			verb = "";particle = ""
			for mor in chunk_element.morphs:
				if mor.pos == "動詞":
					verb += mor.base
					break # 最左の動詞の基本形を述語とするため
			# 動詞にかかる文節の助詞(格)の出力
			for num in chunk_element.srcs:
				for mor in chunk_list[num].morphs:
					if mor.pos == "助詞":
						particle += mor.surface
						particle += " "
			if verb != "" and particle != "":
				print verb,"\t",particle

if __name__ == "__main__":
	main()
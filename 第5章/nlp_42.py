# coding:utf-8
import nlp_41
def main():
	all_chunk_list = nlp_41.make_chunk()
	for line in all_chunk_list:
		for chunk_element in line:
			sentence = ""
			for morph in chunk_element.morphs:
				sentence += morph.surface
			sentence += ":"
			# 係り受け先の出力:chunk_element.dst
			if chunk_element.dst == -1:
				sentence += "<NONE>"
			else:
				for mor in line[chunk_element.dst].morphs:
					if mor.surface == "。" or mor.surface == "、":
						pass
					else:
						sentence += mor.surface

			sentence += "\t"
			# 係り受け元の出力:chuk_element.srcs
			if len(chunk_element.srcs) == 0:
				sentence += "<NONE>"
			else:
				for num in chunk_element.srcs:
					for mor in line[num].morphs:
						if mor.surface == "。" or mor.surface == "、":
							pass
						else:
							sentence += mor.surface
					sentence += " "
			print sentence
if __name__ == "__main__":
	main()
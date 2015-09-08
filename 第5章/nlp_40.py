# coding:utf-8
class Morph:
	def __init__(self, surface, base, pos, pos1):
		# メンバ変数
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

def readfile_morph():
	all_list = []#文書全体の構文解析結果を格納
	one_list = []#1文の構文解析結果を格納

	for line in open("neko.txt.cabocha"):
		if line.startswith("*"):
			continue
		elif "\t" in line:
			surf, other = line.strip().split("\t") # \t の前後で区切り:前=surf,後=item
			others = other.split(",") # itemを,で区切って配列に格納
			morph = Morph(surf,others[6],others[0],others[1]) # morph作成
			one_list.append(morph) # 1形態素のmorphをone_txtに格納
		elif "EOS" in line: # EOS←分の区切り
			if len(one_list) != 0:
				all_list.append(one_list) # one_txt をつなげて all_txtに
				one_list = []
	return all_list

def main():
	all_list = readfile_morph()
	morphs_list = all_list[29]

	for item in morphs_list:
		print "表層形:surface->",item.surface,"\t基本形:base->",item.base,"\t品詞:pos->",item.pos,"\t品詞細分類1:pos1->",item.pos1

if __name__ == "__main__":
	main()
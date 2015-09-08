# coding:utf-8
from collections import defaultdict
class Morph:
	def __init__(self, surface, base, pos, pos1):
		# メンバ変数
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1
class Chunk:
	def __init__(self, morphs, dst, srcs):
		# メンバ変数
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs
		
def make_chunk():
	all_chunk_list = []#全ての文節の構文解析結果と係り受け関係を格納する配列

	chunk_list = []#各文章に対する複数のchunkを記憶しておく配列
	relate_dict = defaultdict(list)#係り受け元がどこなのかを記憶しておく配列

	for line in open("neko.txt.cabocha"):
		if line.startswith("*"): #*で始まる文章が係り受け情報を表す
			morphs = [] #←各形態素の解析結果を格納する配列の初期化
			chunk_replesent_list = line.strip().split(" ")
			dst = int(chunk_replesent_list[2][:-1]) #係り受け先 [:-1]でDの削除
			srcs = relate_dict[int(chunk_replesent_list[1])] #係り受け元 relate_dictで記憶している

			chunk = Chunk(morphs,dst,srcs)
			chunk_list.append(chunk)

			relate_dict[dst].append(int(chunk_replesent_list[1]))

		elif "\t" in line: #Morphの処理
			surf, other = line.strip().split("\t")
			others = other.split(",")
			morph = Morph(surf,others[6],others[0],others[1])
			morphs.append(morph)

		elif "EOS" in line:
			all_chunk_list.append(chunk_list)
			chunk_list = [] # chunk_list の初期化
			relate_dict = defaultdict(list) # relate_dictの初期化

	return all_chunk_list

def main():
	all_chunk_list = make_chunk()
	# for i in xrange(0,len(all_chunk_list)):
	# 	j=0
	# 	print i
	# 	for item in all_chunk_list[i]:
	# 		print j,
	# 		for  morph in item.morphs:
	# 			print morph.surface,
	# 		# print "\t係り受け先->",item.dst,"\t係り受け元->",item.srcs,
	# 		print ""
	# 		j += 1
	# 	j = 0
	for item in all_chunk_list[33]:
			for morph in item.morphs:
				print morph.surface,
			print "\t係り受け先->",item.dst,"\t係り受け元->",item.srcs,
			print ""
 

if __name__ == "__main__":
	main()
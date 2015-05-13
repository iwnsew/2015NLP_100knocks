#coding: utf-8

read_file = open("hightemp.txt", "r")

lines = read_file.readlines()
lines_list = []
k = sum(1 for line in open("hightemp.txt"))

num = 0 # Nの値が不適切な時のループ用変数
while num <=0 :
	print "最初から何行目までを出力させますか？:N(自然数) =",
	N = input()
	if N <= 0:
		print "値は自然数を入力してください"
	elif N > k:
		print "値が大きすぎます",
		print "(N =",k,"まで)"
	else:
		for line in lines:
			lines_list.append(line) #行ごとにリストに格納
		else:
			lines_list = lines_list[:N]
			print "".join(lines_list).strip() #strip()により最後の行の余計な改行を回避
			read_file.close()
			num = num + 1

# UNIX
# >head -n 6 hightemp.txt
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
# 山形県	山形	40.8	1933-07-25
# 山梨県	甲府	40.7	2013-08-10
# 和歌山県	かつらぎ	40.6	1994-08-08
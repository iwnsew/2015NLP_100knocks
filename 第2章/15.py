#coding: utf-8

read_file = open("hightemp.txt", "r")

lines = read_file.readlines()
lines_list = []
k = sum(1 for line in open("hightemp.txt"))

num = 0 # Nの値が不適切な時のループ用変数
while num <=0 :
	print "最後から何行目までを出力させますか？:N(自然数) =",
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
			lines_list = lines_list[-N:]
			print "".join(lines_list).strip() #strip()により最後の行の余計な改行を回避
			read_file.close()
			num = num + 1

# UNIX
# >tail -n 6 hightemp.txt
# 千葉県	茂原	39.9	2013-08-11
# 埼玉県	鳩山	39.9	1997-07-05
# 大阪府	豊中	39.9	1994-08-08
# 山梨県	大月	39.9	1990-07-19
# 山形県	鶴岡	39.9	1978-08-03
# 愛知県	名古屋	39.9	1942-08-02
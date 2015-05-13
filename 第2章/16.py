#coding: utf-8
import itertools

read_file = open("hightemp.txt", "r")

lines = read_file.readlines()
lines_list = [] #入力ファイルの取り出してきた１行毎を格納するリスト
split_list = [] #その１行に対し,タブで分割し単語毎を格納するリスト

num = 0 # Nの値が不適切な時のループ用変数
while num <=0 :
	print "何分割しますか？:N(自然数) =",
	N = int(input())
	print N,"分割します"

	k = sum(1 for line in open("hightemp.txt")) #k=入力txtの行数
	n = k // N #N分割して,何行毎で区切るか=>n行毎で区切る
	surplus = k % N #txtの行数kをn行毎で区切った時のあまりの行数
	file_num = 1 #分割後のファイル番号(インクリメント用)

	if N <= 0:
		print "値は自然数を入力してください"
	elif N > k:
		print "値が大きすぎます",
		print "(N =",k,"まで)"
	else:
		for line in lines:
			lines_list.append(line) #行ごとにリストに格納
		else:
			if surplus > 0: #txtをN分割したときに余りが出る(割り切れない)時
				z = (n+1) * surplus #余りの数の行数分だけnの値(区切る行数)を１増やす

				#z行目までの処理
				for i in itertools.izip_longest(*[iter(lines_list[:z])]*(n+1)): #n+1行毎に区切る
					split_list = list(i)
					#リストsplit_listに含まれる値がNoneの時(区切った時に行数が足りないとNoneが格納されている),""に置換
					for l in xrange(len(split_list)):
						if split_list[l] == None:
							split_list[l] = ""

					print "".join(split_list)
					write_file = open(str(file_num)+".txt", "w") #出力ファイルの決定
					write_file.write(''.join(split_list))
					file_num = file_num + 1

				#z行目以降の処理
				for j in itertools.izip_longest(*[iter(lines_list[z:])]*n): #残りの行はもとのnの値そのまま
					split_list = list(j)
					#リストsplit_listに含まれる値がNoneの時(区切った時に行数が足りないとNoneが格納されている),""に置換
					for l in xrange(len(split_list)):
						if split_list[l] == None:
							split_list[l] = ""

					print "".join(split_list)
					write_file = open(str(file_num)+".txt", "w") #出力ファイルの決定
					write_file.write(''.join(split_list))
					file_num = file_num + 1

				read_file.close()
				write_file.close()
				num = num + 1

			else: ##txtをN分割したときに余りが出ない(割り切れる)時
				for i in itertools.izip_longest(*[iter(lines_list)]*n):
					split_list = list(i)
					#リストsplit_listに含まれる値がNoneの時(区切った時に行数が足りないとNoneが格納されている),""に置換
					for l in xrange(len(split_list)):
						if split_list[l] == None:
							split_list[l] = ""

					print "".join(split_list)
					write_file = open(str(file_num)+".txt", "w") # 出力ファイルの決定
					write_file.write(''.join(split_list))
					file_num = file_num + 1

				read_file.close()
				write_file.close()
				num = num + 1



# UNIX
# UNIXコマンドの方で"N分割"する方法がわからなかった.
# (N行毎の分割でのみ実行)
# >split -8 hightemp.txt
# ファイル名:xaa↓
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
# 山形県	山形	40.8	1933-07-25
# 山梨県	甲府	40.7	2013-08-10
# 和歌山県	かつらぎ	40.6	1994-08-08
# 静岡県	天竜	40.6	1994-08-04
# 山梨県	勝沼	40.5	2013-08-10

# ファイル名:xab↓
# 埼玉県	越谷	40.4	2007-08-16
# 群馬県	館林	40.3	2007-08-16
# 群馬県	上里見	40.3	1998-07-04
# 愛知県	愛西	40.3	1994-08-05
# 千葉県	牛久	40.2	2004-07-20
# 静岡県	佐久間	40.2	2001-07-24
# 愛媛県	宇和島	40.2	1927-07-22
# 山形県	酒田	40.1	1978-08-03

# ファイル名:xac↓
# 岐阜県	美濃	40	2007-08-16
# 群馬県	前橋	40	2001-07-24
# 千葉県	茂原	39.9	2013-08-11
# 埼玉県	鳩山	39.9	1997-07-05
# 大阪府	豊中	39.9	1994-08-08
# 山梨県	大月	39.9	1990-07-19
# 山形県	鶴岡	39.9	1978-08-03
# 愛知県	名古屋	39.9	1942-08-02
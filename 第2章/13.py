#coding: utf-8
read_file1 = open("col1.txt", "r")
read_file2 = open("col2.txt", "r")
write_file = open("merge.txt", "w")

col1_list = [] #col1の中身保管用リスト
col2_list = [] #col2の中身保管用リスト
merge_list = [] #col1とcol2の各行をタブで結合させたもののリスト

lines1 = read_file1.readlines()
lines2 = read_file2.readlines()

for line1 in lines1:
	col1_list.append(line1.strip()) #col1の中身をリストcol1_listに格納
for line2 in lines2:
	col2_list.append(line2) #col2の中身をリストcol2_listに格納

for i in xrange( min(len(col1_list),len(col2_list)) ):
	merge = col1_list[i]+"	"+col2_list[i] #タブで結合(タブ区切り)
	merge_list.append(merge) #col1とcol2の各行をタブで結合したものをリストmerge_listに格納
else:
	write_file.write(''.join(merge_list)) #merge.txtにmerge_listの中身を書き込む
	read_file1.close()
	read_file2.close()
	write_file.close()

for line in open("merge.txt", "r"):
    print line,

# UNIX
# >paste col1.txt col2.txt
# 高知県	江川崎
# 埼玉県	熊谷
# 岐阜県	多治見
# 山形県	山形
# 山梨県	甲府
# 和歌山県	かつらぎ
# 静岡県	天竜
# 山梨県	勝沼
# 埼玉県	越谷
# 群馬県	館林
# 群馬県	上里見
# 愛知県	愛西
# 千葉県	牛久
# 静岡県	佐久間
# 愛媛県	宇和島
# 山形県	酒田
# 岐阜県	美濃
# 群馬県	前橋
# 千葉県	茂原
# 埼玉県	鳩山
# 大阪府	豊中
# 山梨県	大月
# 山形県	鶴岡
# 愛知県	名古屋
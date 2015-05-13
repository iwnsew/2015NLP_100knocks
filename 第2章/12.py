#coding: utf-8

new_read_file = open("hightemp.txt", "r")
write_file1 = open("col1.txt", "w")
write_file2 = open("col2.txt", "w")

new_lines = new_read_file.readlines()

col1_list = [] #col1の中身保管用リスト
col2_list = [] #col2の中身保管用リスト
line_split = []

for line in new_lines:
	line_split = line.split("	") #タブで分割した要素をリストline_splitに格納
	col1_list.append(line_split[0]) #line_split[0]=１列目
	col2_list.append(line_split[1]) #line_split[1]=２列目
else:
	write_file1.write('\n'.join(col1_list)) #１列目の内容をcol1.txtに書き込み
	write_file2.write('\n'.join(col2_list)) #２列目の内容をcol1.txtに書き込み
	new_read_file.close()
	write_file1.close()
	write_file2.close()

# ↓確認用出力
# for line in open("col1.txt", "r"):
#     print line,

# print "\n--------------------------"

# for line in open("col2.txt", "r"):
#     print line,

# UNIX
# >cut -f1 hightemp.txt
# 高知県
# 埼玉県
# 岐阜県
# 山形県
# 山梨県
# 和歌山県
# 静岡県
# 山梨県
# 埼玉県
# 群馬県
# 群馬県
# 愛知県
# 千葉県
# 静岡県
# 愛媛県
# 山形県
# 岐阜県
# 群馬県
# 千葉県
# 埼玉県
# 大阪府
# 山梨県
# 山形県
# 愛知県

# >cut -f2 hightemp.txt
# 江川崎
# 熊谷
# 多治見
# 山形
# 甲府
# かつらぎ
# 天竜
# 勝沼
# 越谷
# 館林
# 上里見
# 愛西
# 牛久
# 佐久間
# 宇和島
# 酒田
# 美濃
# 前橋
# 茂原
# 鳩山
# 豊中
# 大月
# 鶴岡
# 名古屋
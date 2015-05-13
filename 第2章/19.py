#coding: utf-8

read_file = open("hightemp.txt", "r")

lines = read_file.readlines()

col1_list = [] #1列目の中身保管用リスト
line_split = []

for line in lines:
	line_split = line.split("	") #タブで分割した要素をリストline_splitに格納
	col1_list.append(line_split[0]) #line_split[0]=１列目
else:
	read_file.close()

# 数え上げ
pre_dict = {}
for word in col1_list:
    pre_dict[word] = pre_dict.get(word, 0) + 1
# ソート
for k, v in sorted(pre_dict.items(), reverse=True, key=lambda x:x[1]):
    print v, k

# >cut -f1 hightemp.txt | sort -k1,1 | uniq -c | sort -r
#    3 群馬県
#    3 山梨県
#    3 山形県
#    3 埼玉県
#    2 静岡県
#    2 愛知県
#    2 岐阜県
#    2 千葉県
#    1 和歌山県
#    1 高知県
#    1 愛媛県
#    1 大阪府
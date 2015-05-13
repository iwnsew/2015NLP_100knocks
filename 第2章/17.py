#coding: utf-8
read_file = open("hightemp.txt", "r")

lines = read_file.readlines()

line_split = []
lines_set = set([])

for line in lines:
	line_split = line.split("	") #タブで分割した要素をリストline_splitに格納
	lines_set.add(line_split[0]) #line_split[0]=１列目
else:
	read_file.close()

print "\n".join(sorted(lines_set)).strip()

# >cut -f1 hightemp.txt | sort -k1,1 | uniq
# 千葉県
# 埼玉県
# 大阪府
# 山形県
# 山梨県
# 岐阜県
# 愛媛県
# 愛知県
# 群馬県
# 静岡県
# 高知県
# 和歌山県
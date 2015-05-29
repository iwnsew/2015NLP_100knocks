# coding:utf-8
import json
import re

read_file = open("jawiki-country.json", "r")
lines = read_file.readlines()

# "title"キー:記事名,"text"キーの辞書オブジェクト:記事本文　の辞書
country_dict = {}

# 1行に1記事が格納->行ごと(記事ごと)に分割, counyry_dictに格納
for line in lines:
	# "title":記事のタイトル, "text":記事の本文
	country_dict[json.loads(line)["title"]] = json.loads(line)["text"]

england = country_dict[u"イギリス"]
#----------------------------------------#
# セクション部分の抽出(pattern)
pattern = re.compile("=(=+)(.+)(=+)=")
iterator = re.finditer(pattern, england)

for section in iterator:
	# セクション名とレベルの抽出
	pattern_section = re.compile("(?P<sectionname>=+)\s*(?P<level>[^=]+)")
	section_name_level = re.search(pattern_section, section.group())
	
	print section.group()
	print "セクション名:"+str(section_name_level.group("sectionname").encode("utf-8"))
	print "レベル:"+str(len(section_name_level.group("level"))-1)

read_file.close()
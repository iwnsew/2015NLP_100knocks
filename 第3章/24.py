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
# ファイル参照部分の抽出
pattern = re.compile(u"(ファイル|File):(.+)")
iterator = re.finditer(pattern, england)

for media_file in iterator:
	# # ---確認用出力---
	# print "---------"
	# print media_file.group()
	# # ------------ #

	pattern_media = re.compile(":(?P<filename>.+?)\|")
	match_media = re.search(pattern_media, media_file.group())
	print match_media.group("filename")

read_file.close()
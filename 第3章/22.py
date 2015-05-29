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
# カテゴリ行の抽出
pattern = re.compile("\[\[Category:.+")
iterator = re.finditer(pattern, england)

for colum_include_category in iterator:
		# カテゴリ名の抽出
		# []の入れ子構造には対応できてないが...
		pattern_category = re.compile(":(?P<categoryname>.+?)(\]\])")
		category_name = re.search(pattern_category, colum_include_category.group())

		print colum_include_category.group()
		print "->",category_name.group("categoryname")

read_file.close()
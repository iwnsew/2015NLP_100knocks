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
# テンプレートの抽出
pattern = re.compile(u"(\{\{基礎情報 国\n)(.+|\n)+?\}\}")

dictionary = {}
template_colums = re.finditer(pattern, england)

for template in template_colums:
	# format(template_colums())は{{基礎情報 国〜}}の複数行
	format = template.group()
	# print format

	# *{{ もしくは **{{ 以降の部分除去
	format = re.sub("\*\*?\{\{.+\n", "", format)
	# <references 以外の <以降の部分削除
	format = re.sub("\<(?!references)(.+)", "", format)
	# print format

	# =の前後で分割(=の直前,直後に空白スペースがあるので\sで除去)
	devide_equal = re.compile("(?P<fieldname>.+[^=])\s(=)\s(?P<value>.+)")
	format = re.finditer(devide_equal, format)

	for format_pair in format:
		# フィールドの名前から先頭にある|の除去
		fieldname = re.sub("^\|", "", format_pair.group("fieldname"))
		# フィールド名と値を対応付け,辞書に格納
		dictionary[fieldname] = format_pair.group("value")

for k,v in dictionary.iteritems():
	print k, ":", v
read_file.close()
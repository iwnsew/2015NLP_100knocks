# coding:utf-8
import json
import re
import requests

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

	#問26:強調マークアップの除去
	format = re.sub("'{1,5}", "", format)
	# 問27:内部リンクの除去
	format = re.sub("(\[{1,2})|(\]{1,2})", "", format)
	# 問28:Mediawikiマークアップの可能な限りの除去
	format = re.sub("(\{{1,2})|(\}{1,2})", "", format) #{},{{}}テンプレートの除去
	format = re.sub("(\({1,2})|(\){1,2})", "", format) #(),(())の除去
	format = re.sub("(\*{1,2})|(\#{1,2})", "", format) #箇条書き,番号付き箇条書きの除去
	format = re.sub(":|;", "", format) #定義の箇条書きの除去
	format = re.sub("\<(.+?)\>", "", format) #コメントアウトの除去
	format = re.sub(u"ファイル:", "", format) # ファイル:の除去
	# print format

	# =の前後で分割
	devide_equal = re.compile("(?P<fieldname>.+[^=])\s(=)\s(?P<value>.+)")
	format = re.finditer(devide_equal, format)

	for format_pair in format:
		# フィールドの名前から先頭にある|の除去
		fieldname = re.sub("^\|", "", format_pair.group("fieldname"))
		# フィールド名と値を対応付け,辞書に格納
		dictionary[fieldname] = format_pair.group("value")

# for k,v in dictionary.iteritems():
# 	print k+":"+v

#----------------------------------------#

url = "http://ja.wikipedia.org/w/api.php?action=query&format=json&titles=Image:%s&prop=imageinfo&iiprop=url"
r = requests.get(url % dictionary[u"国旗画像"])
print r.json()["query"]["pages"]["-1"]["imageinfo"][0]["url"]

read_file.close()




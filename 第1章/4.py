#coding: utf-8

Genso = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

Genso = Genso.replace(".","") #,の除去
Genso_list = Genso.split(" ")

One_list = {}#１文字の元素の辞書型リスト
Two_list = {}#２文字の元素の辞書型リスト
#辞書型リストへの挿入
for n in xrange(0,len(Genso_list)):
	if n == 0:
		One_list[Genso_list[n][0:1]] = n
	elif n == 4:
		One_list[Genso_list[n][0:1]] = n
	elif n == 5:
		One_list[Genso_list[n][0:1]] = n
	elif n == 6:
		One_list[Genso_list[n][0:1]] = n
	elif n == 7:
		One_list[Genso_list[n][0:1]] = n
	elif n == 8:
		One_list[Genso_list[n][0:1]] = n
	elif n == 14:
		One_list[Genso_list[n][0:1]] = n
	elif n == 15:
		One_list[Genso_list[n][0:1]] = n
	elif n == 18:
		One_list[Genso_list[n][0:1]] = n
	elif n == 19:
		One_list[Genso_list[n][0:1]] = n
	else:
		Two_list[Genso_list[n][0:2]] = n
		pass

# #１文字のリストソート
print "1文字の辞書"
print One_list

# #１文字のリストソート
print "2文字の辞書"
print Two_list
ted(Two_list.items(), key=lambda x:x[1]):
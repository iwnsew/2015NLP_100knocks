#coding: utf-8

ensyu = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

ensyu = ensyu.replace(",","")#,の除去
ensyu = ensyu.replace(".","")#.の除去

print ensyu
ensyu_list = ensyu.split(" ")
print ensyu_list

i = len(ensyu_list)

num_list = []

for x in xrange(0,i):
	num_list += [len(ensyu_list[x])]

print num_list
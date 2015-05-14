#coding: utf-8

#文字(Character)単位
def ch_ngram(text, n):
    text = text.replace(" ","")#,の除去
    text = text.replace(",","")#.の除去
    text = text.replace(".","")#.の除去

    results = []
    if len(text) >= n:
        for i in xrange(len(text)-n+1):
            results.append(text[i:i+n])
    return results

X = set([])
Y = set([])

text1 = "paraparaparadise"
for i in ch_ngram(text1, 2):
	X.add(i)
print "X=",X
text2 = "paragraph"
for j in ch_ngram(text2, 2):
	Y.add(j)
print "Y=",Y

print "-------------------------------------------------------"
#setを用いて集合を実現
#和集合
wa = X.union(Y)
print "和集合=",wa
#積集合
seki = X.intersection(Y)
print "積集合=",seki
#差集合
sa_xy = X.difference(Y)
sa_yx = Y.difference(X)
print "差集合(X-Y)=",sa_xy
print "差集合(Y-X)=",sa_yx

print "-------------------------------------------------------"

if "se" in X:
    print "Xにseが含まれる"

if "se" in Y:
    print "Yにseが含まれる"
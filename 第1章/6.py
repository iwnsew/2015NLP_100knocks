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

X = []
Y = []

text1 = "paraparaparadise"
for i in ch_ngram(text1, 2):
	X += [i]
print "X=",X
text2 = "paragraph"
for j in ch_ngram(text2, 2):
	Y += [j]
print "Y=",Y


print "-------------------------------------------------------"
newX = []
for k in X:
    if not k in newX:
        newX.append(k)
newY = []
for l in Y:
    if not l in newY:
        newY.append(l)
SUM = newX + newY
#和集合
wa = []
for m in SUM:
    if not m in wa:
        wa.append(m)
print "和集合=",wa
#積集合
seki = []
for n in newX:
    if n in newY:
        seki.append(n)
print "積集合=",seki
#差集合
sa = wa
for z in seki:
    if z in sa:
        sa.remove(z)
print "差集合=",sa

print "-------------------------------------------------------"

if "se" in X:
    print "Xにseが含まれる"

if "se" in Y:
    print "Yにseが含まれる"
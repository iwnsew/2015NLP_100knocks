#coding: utf-8

#N-gramの実装
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
#単語(word)単位
def wo_ngram(text, n):
    text = text.replace(".","")#,の除去
    text = text.replace(",","")#.の除去
    text_list = text.split(" ")#分割

    results = []
    if len(text_list) >= n:
        for i in xrange(len(text_list)-n+1):
            results.append(text_list[i:i+n])
    return results



print "テキストを入力してください."
text = raw_input() #May the Force be with you.
print "N = ???"
n = input()
for i in ch_ngram(text, n):
    print i
for j in wo_ngram(text, n):
    print j

print "-------------------"

text1 = "I am an NLPer."
for i in ch_ngram(text1, 2):
    print i
for j in wo_ngram(text1, 2):
    print j
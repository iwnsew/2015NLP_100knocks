#coding: utf-8
def cipher(sentence):
	if sentence.islower() == True:
		#(219 - 文字コード)の文字に置換
		sentence_list = list(sentence)
		for i in xrange(len(sentence_list)):
			code = 219 - ord(sentence_list[i])
			sentence_list[i] = chr(code)
		sentence = "".join(sentence_list)
		return sentence
	else:
		return sentence


print "please enter message"
message = raw_input()
print ">>>"+str(cipher(message))
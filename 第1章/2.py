# coding: utf-8

msg_p = u"パトカー"
msg_t = u"タクシー"

msg_new = ""

for x in range(0,len(msg_p)):
	msg_new += msg_p[x] + msg_t[x]
print msg_new
#coding: utf-8

print sum(1 for line in open("hightemp.txt"))

# UNIX
#１コラム目が行数(２コラム目が単語数,３コラム目がバイト数)
# >wc hightemp.txt
#       24      98     813 hightemp.txt

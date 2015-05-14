#coding: utf-8

def template(x,y,z):
	print str(x)+"の時の"+str(y)+"は"+str(z)

print "x時のyはz"
print "xは？:",
_x = raw_input()
if _x.isdigit() == True:
 	_x = int(_x)
print "yは？:",
_y = raw_input()
if _y.isdigit() == True:
 	_y = int(_y)
print "zは？:",
_z = raw_input()
if _z.isdigit() == True:
 	_z = int(_z)

template(_x,_y,_z)
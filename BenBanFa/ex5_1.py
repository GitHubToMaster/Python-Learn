
#-*-coding:utf-8-*-

# 我的姓名
name = 'Zed A.Shaw'

# 我的年龄
age = 35 # not a lie

height = 74 # inches

weight = 74 # lbs

eyes = 'Blue' 

teeth = 'White'

hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky. try to get it exactly right
print "If i add %d , %d and %d i get %d" % ( age, height, weight, age + height + weight)


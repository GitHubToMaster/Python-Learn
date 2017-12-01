#-*-coding:utf-8-*-
# 用来测试 %r的用例

# 下面3个print语句将不会产生差异
print "I am %d years old." % 22  
print "I am %s years old." % 22  
print "I am %r years old." % 22  

# 下面两个print语句将会产生差异
text = "I am %d years old." % 22  
print "I said: %s." % text  
print "I said: %r." % text  

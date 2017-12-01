#-*-coding:utf-8-*-
# 用来测试 %r的用例

#	%r用rper()方法处理对象
#	%s用str()方法处理对象

# 下面3个print语句将不会产生差异
print "I am %d years old." % 22  
print "I am %s years old." % 22  
print "I am %r years old." % 22  

# 下面两个print语句将会产生差异
text = "I am %d years old." % 22  
print "I said: %s." % text  
print "I said: %r." % text  

#	 可见，%r打印时能够重现它所代表的对象(rper() unambiguously recreate the object it represents) 

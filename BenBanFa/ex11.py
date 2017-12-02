
#-*-coding:utf-8-*-
print "How old are you?",
age = raw_input();

print "How tall are you?",

height = raw_input();

print "How much do you weight?",

weight = raw_input();

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

## 注意:每一行print后面都加了一个逗号(comma),这样之后print就不会输出新行符而结束一行符跑到下一行去了

## 注意:这里最后一行 '6\'2"' 里边有一个\'序列,单引号需要被转义,从而防止它被识别为字符串的结尾.

#-*-coding:utf-8-*-

# 用来
x = "There are %d types of people." % 10;

# 定义binary为binary
binary = "binary"

# 定义do_not为don't
do_not = "don't"

# 定义
y = "Those who know %s and those who %s." % (binary, do_not)

print(x);
print y;


print "I said:%r." % x;
print "I also said:%s." % y

hilarious = False;
joke_evaluation = "Isn't that joke so funny?!%r"

print joke_evaluation % hilarious;

w = "This is the left side of.."
e = "a string with a right side."

print joke_evaluation % w;

print w + e;

# 16.35
# 2578. 最小和分割
# 主要是策略。就两个数，肯定是平衡。
# 好吧 道理我也算懂 实现不了。抄抄。。胶水语言封装太好了自己写不出来。。
#17.00 AC
num = 4325
s = "".join(sorted(str(num)))
n1 = int(s[::2])
n2 = int(s[1::2])
print(n1+n2)
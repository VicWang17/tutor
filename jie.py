import jieba
str="我等下去图书馆"
re = jieba.cut(str)
ls =list(re)
print(ls)

#Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
str1='this is a string example'
print(str1.find('string',0,len(str1)))


str2='this is a string example, this is also a testing' #查出该字符串中所有‘is’的索引
a=0
for i in range(1,len(str2)) :
    if a!= i :
        a = str2.find('is', i, len(str2))
        continue
        print(a)
    else:
        print(i)
        continue


str3='abcdsdfdsfgrtdf'
print(str3.find('is',0,len(str3)))
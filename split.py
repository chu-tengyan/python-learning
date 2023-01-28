str1='CTY  \nis \nlearning python'
print(str1.split())  #以空格为分隔符，包含\n
print(str1.split(' ',1)) #以空格为分隔符，分割1次;输出得到一个列表
name=str1.split()[0]
print('name:'+name)
str2='cty#hgh#hcx'
print(str2.split('#',1)) #以#为分隔符，分割2次
print(str2.split('#',2))
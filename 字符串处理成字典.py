# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}

str1= "k:1 |k1:2|k2:3|k3:4"
def str_to_dict(str):
    list_key_value=str.split('|')     #把键值对格式的字符串用|分阁成list
    #print(type(list_key_value))
    dict01={}                         #初始化空的字典作为返回值变量
    for temp in list_key_value:
        str_1=temp.strip()            #去除字符串结尾的空格
        #print('{}-'.format(str_1))
        #list_1=str_1.split(':')
        #key=list_1[0]
        #value=int(list_1[1])
        [key,value]=str_1.split(':')
        #print(key,value)
        dict01[key]=int(value)           #给字典赋值
    return dict01

a=str_to_dict(str1)
print(a)
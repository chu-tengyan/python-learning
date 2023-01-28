'''定义一个函数，要求接受一个字符串参数，判断这个输入的字符串是否是合法的参数，
最大允许长度为20个字符，如果小于等于20个字符，返回true， 否则返回false'''
def function(str1):
    if len(str1)<=20:
        return True
    else:
        return False

result=function("112344")
print(result)


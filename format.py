str1='hello'
str2='world'
s1='{} {}'
s2=s1.format(str1,str2)
print(s2)

print('{0} {1}'.format('hello','world'))
print('{0} {0} {1}'.format('hello','world'))
print('{1} {1} {0}'.format('hello','world'))
print('{wo} {he} {wo}'.format(he='hello',wo='world'))
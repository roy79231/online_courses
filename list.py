#list跟for迴圈的學習
a = ['roy','chris','jason']
print(a[2])
a.append('justin')
print('justin' in a)
print(a)
print(len(a)) 
for guy in a:
    print(guy)
    if guy == 'chris':
    	break 
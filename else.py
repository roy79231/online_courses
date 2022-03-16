#else and elif practice
age = int(input('請輸入您的年齡:'))
if age < 13 :
	print('國小生')
elif age>=13 and age <=18:
	print('國高中生')
elif age>18 and age<22:
    print('大學生')
else :
	print('出社會的人')
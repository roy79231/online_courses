#練習雙層IF和LOOP迴圈
while True:
	driving = input('你有開過車嗎?')
	if driving == '有' or driving == '沒有':
		break
	print('請輸入有or沒有')
age = int(input('請問你現在幾歲?'))
if driving == '有':
	if age >= 18 :
		print('很棒!你通過測驗了')
	elif age < 18 :
		print('你這樣母湯喔')
if driving == '沒有' :
	if age >= 18 :
		print('你可以考慮去考駕照喔!')
	elif age <18 :
		print('等到成年時，記得去考駕照喔')

#製作及理解二維清單 #藉由填入的數據直接做出一個表單
import os 
product = []
#檢查檔案是否存在
if os.path.isfile('products.csv') :
	with open('products.csv','r',encoding='utf-8') as k:
		for line in k :
			if '商品,價格' in line :
				continue
			t = line.strip().split(',')
			name = t[0]
			price = t[1]
			product.append([t[0],t[1]])
else :
	print('找不到檔案qq')

print(product)
#讓使用者輸入
while True :
	name = input('請輸入商品名稱:')
	if name == 'q' :
		break
	price = input('請輸入商品價格:')
	p=[]
	p.append(name)
	p.append(price)
	product.append(p)      #8~11行=products.append([name],[price])
print(product)
#印出所有商品價格
for f in product :
	print(f[0],'的價格為',f[1])
#寫入檔案
with open('products.csv','w',encoding='utf-8') as s :
	s.write('商品,價格\n')
	for g in product :
		s.write(g[0]+','+g[1]+'\n')
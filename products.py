#製作及理解二維清單
product = []
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
print(product[0][1])

for f in product :
	print(f[0],'的價格為',f[1])
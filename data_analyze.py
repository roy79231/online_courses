#數據分析--學會如何分析數據和從中篩出自己想要的
#因為數據檔案過大，因此改用文字檔(txt)傳

data=[]
count = 0
with open('reviews.txt','r' ) as f :
	for line in f:
		data.append(line)
		count += 1 #count = count +1
		if count % 1000 == 0: # %為餘數
			print(len(data))
print('檔案讀取完畢，共有',len(data),'筆資料')

sum_len = 0
for d in data :
	sum_len += len(d)
	
average = sum_len/len(data)
print('平均留言長度為',average,'個字')

new = []
for d in data:
	if len(d)<100 :
		new.append(d)
print('一共有',len(new),'筆留言小於100字')
print(new[0])

good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有',len(good),'筆留言裡有good')
print(good[0])

bad = [b for b in data if 'bad' in b] #嘗試速寫法
print('一共有',len(bad),'筆留言裡有bad')
print(bad[0])
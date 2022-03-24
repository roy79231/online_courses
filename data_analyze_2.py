#數據分析--學會如何分析數據和從中篩出自己想要的
import time
import progressbar
data=[]
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt','r' ) as f :
	for line in f:
		data.append(line)
		count += 1 #count = count +1
		bar.update(count)		
print('檔案讀取完畢，共有',len(data),'筆資料')

start = time.time()
wc = {}             #word_count
for line in data : 
	words = line.split(' ')
	for word in words :
		if word in wc :
			wc[word] += 1
		else :
			wc[word] = 1
end = time.time()
print('花費',end-start,'秒')

while True :
	x = input('請輸入你想找出現幾次的單字:')
	if x == 'q':
		break
	if x in wc :
		print('你查找到的單字',x,'出現次數為',wc[x])
	else :
		print('你輸入的字',x,'沒出現過喔')

print('感謝您的使用')
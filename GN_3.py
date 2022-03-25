import random
#先載入模組
r = random.randint (1, 100)
count = 0 #count=計數
while True:
	count += 1 #count = count +1
	num = input ('猜一個數字:')
	num = int(num)
	if num == r:
		print ('你猜對了!')
		break
	elif num > r: 
		print('不對~再小一點')
	elif num < r:
		print ('不對~再大一點')
	print ('這是你猜的第', count, '次')
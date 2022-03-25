import random
#先載入模組
r = random.randint (1, 100)
while True:
	num = input ('猜一個數字:')
	num = int(num)
	if num == r:
		print ('你猜對了!')
		break
	elif num > r: 
		print('不對~再小一點')
	elif num < r:
		print ('不對~再大一點')
	else:
		print ('不對~繼續猜!')
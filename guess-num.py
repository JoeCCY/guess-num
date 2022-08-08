import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	n = input('請輸入數字: ')
	n = int(n)
	if n == r:
		print('恭喜答對!')
		print('這是你猜的第', count, '次')
		break
	elif n < r:
		print('比答案小')
	else:
		print('比答案大')
	print('這是你猜的第', count, '次')

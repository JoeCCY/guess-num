import random
while True:
	start = int(input('請輸入隨機數字範圍開始值: '))
	end = int(input('請輸入隨機數字範圍結束值: '))
	if start < end:
		r = random.randint(start, end)
		break
	else:
		print('開始值必須小於結束值!')

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
import random
start = input('請輸入隨機數字開始範圍值: ')
end = input('請輸入隨機數字結束範圍值: ')
start = int(start)
end = int(end)
r = random.randint(start , end)
x = 0
while True:
	x += 1
	guess = input('請猜一個數字: ')
	guess = int(guess)
	if guess == r:
		print('恭喜猜對了！')
		print('你已經猜了', x , '次')
		break
	elif guess < r:
		print('比答案小')
	else:
		print('比答案大')
	print('你已經猜了', x , '次')
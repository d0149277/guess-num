import random
r = random.randint(1 , 100)
x = 0
while True:
	guess = input('請猜一個數字: ')
	guess = int(guess)
	if guess == r:
		print('恭喜猜對了！')
		break
	elif guess < r:
		print('比答案小')
	else:
		print('比答案大')
	x = x + 1
	print('你已經猜了',x,'次')
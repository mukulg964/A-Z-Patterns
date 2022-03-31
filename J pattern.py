for row in range(5):
	for col in range(6):
		if row==0 or col==3 or row==4 and col>1 and col<4 or row==3 and col==1:
			print("*",end='')
		else:
			print(end=' ')
	print()
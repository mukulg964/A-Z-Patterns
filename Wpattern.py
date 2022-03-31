for row in range(5):
	for col in range(5):
		if col==0 or col==4 or row==3 and col!=2 or col==2 and row==2:
			print("*",end='')
		else:
			print(end=' ')
	print()
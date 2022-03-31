for row in range(5):
	for col in range(9):
		if  col==row or row+col== 8:
			print("*",end='')
		else:
			print(end=' ')
	print()
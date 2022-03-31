for row in range(7):
   for col in range(7):
	   if col == 0 or col == 6 or (row== col and row<4) or (col+row==6 and row<3 and row>0):
		    print('*',end ='')
	   else:
		    print(end =' ')
   print(' ')
		   
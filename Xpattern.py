for row in range (7):
   for col in range(6):
	   if   row +col == 5 or col == row:
		    print("*",end ='')
	   else:
		    print(end =' ')
   print(' ')
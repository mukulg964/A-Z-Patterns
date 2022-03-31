for row in range (7):
   for col in range(7):
	   if   row +col == 4 or row-col == 2 or col ==0:
		    print("*",end ='')
	   else:
		    print(end =' ')
   print(' ')
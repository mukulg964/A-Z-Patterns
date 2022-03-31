for row in range(6):
   for col in range(5):
	   if (row==5 and (col>0 and col<4)) or (col==0  and (row<5 )) or (col==4  and (row<5 )) :
		    print("*",end = '')
	   else:
		    print(end = ' ')
   print('')    
   

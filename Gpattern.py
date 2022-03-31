for row in range(6):
   for col in range(6):
        if col==0  and (row!=0 and row!=5) or (row==0 and col>0 and col<5) or (row==5 and col>0 and col<5) or (row==3 and col>2 and col<5) or (col==4 and row==4)  :
          print("*",end = '')
        else:
           print(end = ' ')
   print()
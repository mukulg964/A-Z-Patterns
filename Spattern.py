for row in range(7):
   for col in range(6):
        if  (row== 3 or row==0 or row==6) and (col>0 and col<5) or ((row==1 or row==2) and col==0) or (col==5 and (row==4 or row==5)):
            print("*",end = '')
        else:
            print(end = ' ')
   print('')
   
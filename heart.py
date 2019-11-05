for i in range(5):
  for j in range(7):
   if((i==0 and j%3!=0) or (i==1  and j%3==0) or (i>1and (j==i-1 or    j==7-i))):
    print("*", end=" ")
   else:
    print(" ",  end=" ")
  print()

def multiply(m,n):  
  for i in range(1,m+1):
   print("\n")
   for j in range(1,n+1):
    print(f'{i*j:2}',end=' ')

print("enter 2 numbers for table of multiply:")
m=int(input())
n=int(input())    
multiply(m,n)   





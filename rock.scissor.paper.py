import random
while True:
  print("rock","scissor","paper")
  list=["rock","scissor","paper"]
  user_gamer=str(input())
  com_gamer=random.choice(list)
  
  if user_gamer=="exit":
   break
 
  else:
   print("computer:",com_gamer)
  if user_gamer==com_gamer:
    print("both of them are equall")
   
  elif user_gamer==list[0] and com_gamer==list[2]:
     print("com_gamer is won")
  elif user_gamer==list[0] and com_gamer==list[1]:
     print("user_gamer is won") 

  elif user_gamer==list[2] and com_gamer==list[0]:
     print("user_gamer is won")
  elif user_gamer==list[2] and com_gamer==list[1]:
     print("com_gamer is won")    
 
  elif user_gamer==list[1] and com_gamer==list[0]:
     print("com_gamer is won")
  elif user_gamer==list[1] and com_gamer==list[2]:
     print("user_gamer is won")  

 
  
  
  
  
  
 



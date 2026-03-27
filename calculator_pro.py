#---CALCULATOR---
res=0
#infinate loop to keep calculator running until user take exit.
while True:
  # showing calculation menu.
  print("---CALCULATOR----")
  print("1-->addition(+)\n2-->substraction(-)\n3-->division(/)")
  print("4-->multiplication(x)\n5-->all clear(AC)\n6-->exit")
  # taking user choice.
  try:
    choice=int(input("enter the choice:"))
  except (TypeError,ValueError):
    print("enter choice in numbers only, try again")
    
  if choice==6:
    print("exiting..,")
    break
  elif choice==5:
    res=0
    print("all clear(AC)")
    continue
  #taking user inputs for operations.
  try:
    num1,num2=map(float,input("enter num1 & num2 :").split())
  except ValueError:
    print("enter two num only,separated with space")
    continue
  match choice:
    case 1:
      res = num1 + num2
      print("addition of two numbers=",res)
    case 2:
      res = num1 - num2
      print("substraction of two numbers=",res)
    case 3:
      if num2!=0:
        res = num1 / num2
        print("division of two numbers:",res)
        
      else:
        print("division not possible with these numbers,try again")
        continue
    case 4:
      res = num1 * num2
      print("multiplication of two numbers=",res)
      
      
    
    
  
  
  
    
    
    
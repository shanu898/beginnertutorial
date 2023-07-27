while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(choice == '#'):
    #program ends here
    print("Done. Terminating")
    break
    
  elif (choice in ['+','-','*','/','^','%']):
      if choice=='+':
          sum=self.add()
      if choice=='-':
          subtraction()
          
  num1=input('Enter first number:')  
  num2=input('Enter second number:')    


  
def add(self,num1,num2):
    sum=num1+num2
    return sum    
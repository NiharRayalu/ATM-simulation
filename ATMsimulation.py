# ATM code
chance=3
balence=10000
k=0
print("Welcome to SBI ATM\n")
print("Please insert your card")  
while chance>0 and k<1:
  print("Enter the correct pin")
  pin=int(input())
  if pin==6969:
      while chance>=0 and k<1:
            print("Press 1 to check your balence")
            print("Press 2 to withdraw money")
            print("press 3 to transfer money")
            print("Press 4 to add cash to your account")
            print("Press 5 to return the card")
            a=int(input())
            if a==1:
              print(balence)
              k=k+1
              break
            elif a==2:
              print("How much u wanna withdraw ??")
              w=int(input())
              if w<balence:
                print("Take your cash\n")
                print("Your balence amount is =")
                print(balence-w)
                k=k+1
              else:
                print('You dont have enough balence !!')
                k=k+1
                break
            elif a==3:
              print('To whome u wanna transfer\n')
              print("Enter the account no")
              g=input()
              print("How much you wanna transfer?\n")
              j=int(input())
              print('Money succesfully transferd')
              print("Your remaining balence")
              print(balence-j)
              k=k+1
              break
            elif a==4:
              print("Ok how much u wanna add to your account ??")
              k=int(input())
              print("Drop the cash in the drawer\n")
              print("Your money has been added this is your new balence =")
              print(balence+k)
              k=k+1
              break
            elif a==5:
              print("Thank you have a great time\n")
              print("Take your card")
              k=k+1
              break 
            else:
              print("Press the correct button")
  elif pin!=1166 and chance<0:
    print("Sorry You dont have any more chance")
  elif pin!=1166:
    print("Please enter the correct pin\nYou have still",chance-1,"Chance left")    
    chance=chance-1

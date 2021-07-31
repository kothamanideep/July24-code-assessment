import re
import smtplib
try:
    
   
    while(True):
      print("Select an option from menu ")
      print("\n")
      print("1. Tea (Rs.7)")
      print("2. Coffee (Rs.10)")
      print("3. Masala Dosa (Rs.50)")
      print("4. for exit ")
      choice=int(input("Enter your Order choice:"))
      if choice==1:
        print("\nTea selected")
        
      if choice==2:
        print("\nCoffee selected")
      if choice==3:
        print("\nMasala Dosa Selected")
      if choice==4:
        print("Your Bill ")
        print("RS ",)
        break
        
    num1 = int(input("Enter the number of cup of TEA:"))
    num2 = int(input("Enter the number of cup of COFFEE: "))
    num3 = int(input("Enter the number of MASALA DOSA: "))
    num4= int(input("you have completed the order now press 4 to get your bill"))
    email = input("Enter your email id:")
    emailid=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email)
    if emailid:
        Email=email
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
    if(num4==4):
        message =num1*7+num2*10+num3*50
    message=str(message)
    connection.sendmail("barfikhan78621@gmail.com",Email, message)
    connection.quit()
except Exception:
    print("You enter wrong input")
else:
    print("Successfuly sent")
finally:
    print("Thank you !")
import re
import smtplib
while(True):
    name=input("Please Enter your Name :")
    email=input("Please Enter the Email Id :")
    regex = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    value=re.match(regex,email)
    if value:
        class Tea:
            def priceoftea(self):
                self.teaprice=7
                return self.teaprice

        class Coffee:
            def priceofcoffee(self):
                self.coffeeprice=10 
                return self.coffeeprice
        
        class MasalaDosa:
            def priceofdosa(self):
                self.dosaprice=50
                return self.dosaprice




        class Order(Coffee,Tea,MasalaDosa):
            pass


        totalbill=Order()
        cost=0

        while(True):

            print("\nSelect an option from menu ")
            print("\n")
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("Enter your Order choice:"))
            


            if choice==1:
                print("\nTea selected")
                teacost=totalbill.priceoftea()
                cost+=teacost
                    

            if choice==2:
                print("\nCoffee selected")
                coffeecost=totalbill.priceofcoffee()
                cost+=coffeecost
            

            if choice==3:
                print("\nMasala Dosa Selected")
                dosacost=totalbill.priceofdosa()
                cost+=dosacost
                
            if choice==4:
                print("Your Bill ")
                print(cost)
                message=str(cost)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("chavala.sridhar476@gmail.com","Sridhar123@")
                connection.sendmail("chavala.renuka476@gmail.com",email,message)

                print("bill send to your email")
                connection.quit()
                break
        break          
    else:
        print("Enter valid emailid")
        


        
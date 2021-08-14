
import pymongo
import re,logging
import smtplib

try:

    client=pymongo.MongoClient("mongodb://localhost:27017/") 
    mydatabase=client['BMSDb']     
    collection_name=mydatabase['Donars']

    blist=[]
    bview=[]


    class BMS:

        def bdata(self,name,address,bloodgroup,pincode,mobileno,last_donate,place,email):
            dic={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobileno":mobileno,"lastdonated date":last_donate,"place":place,"email":email}
            blist.append(dic)

    def val(name,address,pincode,mobileno,bloodgroup,place,email):
        valname=re.search("[A-Za-z]{0,25}$",name)
        valpin=re.search("^[1-9]{1}[0-9]{5}$",pincode)
        valmobile=re.search("[6-9]\d{9}$",mobileno)
        valadd=re.search("[A-Za-z]{0,25}$",address)
        valplace=re.search("[A-Za-z]{0,25}$",place)
        valbg=re.search("^(A|B|AB|O)[+-]$",bloodgroup)
        valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",email)
        if valname and valpin and valmobile and valadd and valplace and valbg and valemail:
            return True
        else:
            return False

    obj1=BMS()

    while(True):
        print("1. Add Donors: ")
        print("2. Search Donors based on blood group: ")
        print("3. Search Donors based on blood group AND place: ")
        print("4. Update all the donor details with their mobile number: ")
        print("5. Delete the donor using mobile number: ")
        print("6. Display the total number of donors on each blood group: ")
        print("7. Immediate notification to all via email: ")
        print("8. view all the details")
        print("9. EXIT")

        choice=int(input("\nEnter the number of your choice:"))

        if (choice==1):
            name=input("\nEnter the name:")
            address=input("\nEnter your address:")
            bloodgroup=input("\nEnter your blood group:")
            mobileno=input("\nenter your mobile no: ")
            pincode=input("\nEnter your pincode:")
            last_donate=input("\nEnter your last date of donate:")
            place=input("\nEnter the place:")
            email=input("enter the email:")

        
        
            if val(name,address,pincode,mobileno,bloodgroup,place,email)==True:
              v=obj1.bdata(name,address,bloodgroup,mobileno,pincode,last_donate,place,email) 
              blist.append(v)
              result=collection_name.insert_many(blist)
              print(result.inserted_ids)
            else:
                logging.error("VALIDATION ERROR!!!")
                break
        

        if(choice==2):
            n=input("enter the blood group to be searched: ")
            result2=collection_name.find({"bloodgroup":n})
            for i in result2:
                print(i)

        if(choice==3):
            n=input("enter the blood group to be searched: ")
            m=input("enter the place to searched : ")
            result3=collection_name.find({"$and":[{"bloodgroup":n},{"place":m}]})
            for i in result3:
                print(i)



        if(choice==4):
            mno=input("enter the mobile no: ")
            na=input("enter the c name to be update: ")
            result3=collection_name.update_many({"mobileno":mno}, {"$set": {"name":na}})
            print(result3)

        if(choice==5):
            mb=input("enter the mobile no to delete: ")
            d=collection_name.delete_one({"mobileno":mb})
            print(d)


        if(choice==6):
            result=collection_name.aggregate([{"$group":{"_id":"$bloodgroup","count":{"$sum":1}}}]) 
            for i in result:        
                print(i) 
    
        if (choice==7):
                name=input("Enter name : ")
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("manideepkotha324@gmail.com","mani@9324")
                message="immediately want A+ blood group in XYz Hospital"
                connection.sendmail("manideepkotha324@gmail.com",email,message)
                print("Mail sent sucessfully")
                connection.quit()

        if (choice==8):
            result1=collection_name.find()
            for i in result1:
                bview.append(i)
            print(bview)
            bview.clear()
                    
        if (choice==9):
            break    
except:

     logging.error("OPPS! Something is wrong !") 

finally:

   print("THANK YOU")

  

import json
import random
import string
from pathlib import Path





class Bank:
    database = 'data.json'

    ## Dummy data to be stored in a file
    data = []

    try:
        # Check whether the file exists or not
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists! Please enter valid path.")
    except Exception as err:
        print(f"An exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    ## generating Account Number
    @classmethod
    def __accountgenerate(cls):
        aplpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchr = random.choices("!@#$%^&*()_+",k=1)
        id = aplpha + num + spchr
        random.shuffle(id)
        return "".join(id) 



    def create_account(self):
        info = {
            "name": input("Enter name: "),
            "age": int(input("Enter age: ")),
            "email": input("Enter email address: "),
            "pin": int(input("Enter 4 number pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        ## Updating the data in the json file
        if info ['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you are not able to create your account")
        else:
            print("Your account has been created successfully!")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please remember your account no and pin.")


            Bank.data.append(info)

            ## updating the data into json using update function
            Bank.__update()

    def withdraw_money(self):
        accnumber = input("Enter your account Number ") 
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:  
            print("Invalid credentials, No data found!")
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Insufficient funds!")    
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"You have withdrew {amount}. Your current balance is {userdata[0]['balance']}")

    def deposit_money(self):
        accnumber = input("Enter your account Number ") 
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:  
            print("Invalid credentials, No data found!")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000:
                print("You can't deposit more than Rs. 10,000 at once!")
            elif amount <= 0:
                print("Amount must be greater than zero!")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"You have deposited {amount}. Your current balance is {userdata[0]['balance']}")
            
    def show_details(self):
        accnumber = input("Enter your account Number ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Invalid credentials, No data found!")
        else:
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")

    def update_details(self):
        accnumber = input("Enter your account Number ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Invalid credentials, No data found!")
        else:
           print("You can't change the age, account number and balance")
           print("What do you want to update?")
        newdata = {
            "name": input("Enter updated name: "),
            "email": input("Enter updated email address: "),
            "pin": input("Enter updated 4 digit pin: ")
        }

        if newdata["name"] == "":
            newdata["name"] = userdata[0]["name"]
        elif newdata["email"] == "":
            newdata["email"] = userdata[0]["email"]
        elif newdata["pin"] == "":
            newdata["pin"] = str(userdata[0]["pin"])
        
        newdata["age"] = userdata[0]["age"]
        newdata["accountNo."] = userdata[0]["accountNo."]
        newdata["balance"] = userdata[0]["balance"]

        if newdata["pin"].isdigit() == True and len(newdata["pin"])   == 4:
            userdata[0].update(newdata)
            Bank.__update()
            print("Details Updated Successfully!")
        else:
            print("Pin should contain only numbers and length should be equal to four digits!")

    def delete_account(self):
        accnumber = input("Enter your account Number ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]       

        if userdata == False:
            print("Invalid credentials, No data found!")
        else:
            check = input("Are you sure you want to delete this account?(y/n): ").lower()
            if check == "y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index) 
                Bank.__update() 
                print("Account deleted successfully!")
            elif check == "n":
                pass
            else:
                print("Invalid Input!")

## Object of the Bank class
user = Bank()






print("Press 1 for creating an account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for details of your account")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")

check = int(input("Enter your choice: "))


if check == 1:
    user.create_account()
 
if check == 2:
    user.deposit_money()

if check == 3:
    user.withdraw_money()

if check == 4:
    user.show_details()

if check == 5:
    user.update_details()
if check == 6:
    user.delete_account()
else:
    print("Wrong Choice")
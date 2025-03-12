def menu(name, age):
    if age >= 18:
        selection = input(f"Hello {name}!\nPlease Enter Your Selection:\n1. Debit Menu\n2. Credit Menu\n3. Exit\n")
        if (selection == "1"):
            debitMenu(name, age)
        elif (selection == "2"):
            creditMenu(name, age)
        elif (selection == "3"):
            print("Goodbye!")
        else:
            print("Please Enter a Valid Input.")
    else:
        print("Sorry, You're Not Old Enough.")

def createDebitAccount(name, age, start):
    return {"Name" : name, "Age" : age, "Balance" : start}

def addToDebitAccount(account, amount):
    return {"Name" : account["Name"], "Age" : account["Age"], "Balance" : account["Balance"] + amount}

def debitMenu(name, age):
    count = 0
    while True:
        selection = input("Please Enter What You'd Like To Do:\n1: Create Account\n2: Add Money to Existing Account\n3: Exit\n")
        if (selection == "1"):
            if count <= 0:
                startingAmount = int(input("Please Enter Your Starting amount (digits): $"))
                account = createDebitAccount(name, age, startingAmount)
                print(f"Debit Account Successfully Created! Name: {account["Name"]}, Age: {account["Age"]}, and you have ${account["Balance"]}\n")
                count += 1
            else:
                print("Sorry, You Already Have an Account.\n")
        elif (selection == "2"):
            amount = int(input("Please Enter How much You'd Like to Add to Your Account (digits): $"))
            account = addToDebitAccount(account, amount)
            print(f"${amount} Successfully Added! Current Account Details: Name: {account["Name"]}, Age: {account["Age"]}, and you have ${account["Balance"]}\n")
        elif (selection == "3"):
            print("Goodbye!")
            break
        else:
            print("Please Enter a Valid Input.\n")

def createCreditAccount(name, age):
    return {"Name" : name, "Age" : age, "Debt" : 0}

def payOffDebt(account, amount):
    return {"Name" : account["Name"], "Age" : account["Age"], "Debt" : account["Debt"] + amount}

def creditMenu(name, age):
    count = 0
    while True:
        selection = input("Please Enter What You'd Like To Do:\n1: Create Account\n2: Pay Debt\n3: Exit\n")
        if (selection == "1"):
            if count <= 0:
                account = createCreditAccount(name, age)
                print(f"Debit Account Successfully Created! Name: {account["Name"]}, Age: {account["Age"]}, and you have ${account["Debt"]} debt.\n")
                count += 1
            else:
                print("Sorry, You Already Have an Account.\n")
        elif (selection == "2"):
            amount = int(input("Please Enter the Amount You'd Like to Pay Off (digits): $"))
            account = payOffDebt(account, amount)
            print(f"${amount} Successfully Paid Off! Current Account Details: Name: {account["Name"]}, Age: {account["Age"]}, and you have ${account["Debt"]} debt.\n")
        elif (selection == "3"):
            print("Goodbye!")
            break
        else:
            print("Please Enter a Valid Input.\n")

if __name__ == "__main__":
    name = input("Please Enter Your Name: ")
    age = int(input("Please Enter Your Age (digits): "))
    menu(name, age)
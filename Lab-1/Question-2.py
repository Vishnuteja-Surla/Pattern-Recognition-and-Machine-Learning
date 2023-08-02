# To create tables and do some basic operations on it using Pandas library.
# Create a csv file using python script with the following content
# Write a Menu Driven program to support the following functionalities
# 1. Append Record (row) of account holder
# 2. Delete Record, given the account number
# 3. Credit : Ask the user to enter the amount to be credited, and then add it to the balance.
# 4. Debit : Ask the user to enter the amount to be debited, say x, and then subtract it from the balance.
# In case of SB account type, debit operation should report an error if (balance-x) < 0 .
# 5. Print Account details given the account number.

# Importing Modules
import pandas as pd


def create_csv():

    name = ["Ram", "Sam", "Prabhu"]
    acno = [9893893891, 9893893898, 9893893871]
    actype = ["SB", "CA", "SB"]
    adhaar_no = [959389389173, 959389389179, 959389389159]
    balance = [8989839, 7690990, 989330]
    dict = {
        "Name": name,
        "Account Number": acno,
        "Account Type": actype,
        "Aadhar Number": adhaar_no,
        "Balance": balance
    }

    dataframe = pd.DataFrame(dict)
    dataframe.to_csv('SBIAccountHolder.csv')

    return dataframe


if __name__ == "__main__":
    df = create_csv()
    print(df)

    while 1:
        print('''
    Enter the operation you want to perform:-
    1. Append a new record  2. Delete record using Account Number  3. Credit
    4. Debit  5. Print  6. End
        ''')

        ch = int(input("Your Choice : "))

        if ch == 1:
            name = input("Enter name of new customer : ")
            acno = int(input("Enter account number : "))
            actype = input("Enter Account Type(SB or CA) : ").upper()
            adhar_no = int(input("Enter Aadhar Number : "))
            balance = int(input("Enter initial balance : "))
            new_record = [name, acno, actype, adhar_no, balance]
            df.loc[len(df.index)] = new_record
            df.to_csv("SBIAccountHolder.csv", index=False)

        elif ch == 2:
            acno = int(input("Enter their account number : "))
            user_index = df[df["Account Number"] == acno].index
            if len(user_index) > 0:
                df.drop(user_index, inplace=True)
                df.to_csv("SBIAccountHolder.csv", index=False)
            else:
                print("User not found")

        elif ch == 3:
            acno = int(input("Enter their account number : "))
            user_index = df[df["Account Number"] == acno].index
            if len(user_index) > 0:
                amount = int(input("Enter the money to be credited : "))
                df.loc[df['Account Number'] == acno, ['Balance']] += amount
                df.to_csv("SBIAccountHolder.csv", index=False)
            else:
                print("User not found")

        elif ch == 4:
            acno = int(input("Enter their account number : "))
            user_index = df[df["Account Number"] == acno].index.tolist()
            if len(user_index) > 0:
                amount = int(input("Enter the money to be debited : "))
                user_index = user_index[0]

                if df.loc[user_index, "Account Type"] == "SB":
                    if df.loc[user_index, 'Balance'] >= amount:
                        df.loc[user_index, 'Balance'] -= amount
                    else:
                        print("Insufficient Balance")
                else:
                    df.loc[user_index, ['Balance']] -= amount
                df.to_csv("SBIAccountHolder.csv", index=False)
            else:
                print("User not found")

        elif ch == 5:
            print(df)

        elif ch == 6:
            break

        else:
            print("INVALID COMMAND")


        print("**************************************************************************************************")

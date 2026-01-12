USer_information = {"Name":"Bhanu Teja", "Mobile Number": "", "ATM PIN": "6600", "Balance" : 5000, "Transaction History" : []}  # User data
print("Please insert your ATM card")
remaining_attempts = 3
while remaining_attempts > 0 :
    User_pin = input("Enter 4 digits pin: ")   # Input Personal Identification Number
    if len(User_pin) == 4:
        if User_pin in USer_information['ATM PIN'] :   # Checking the User_pin present in the USer_information
            print("Welcome to the Bakara ATM")
            User_input = int(input("Enter \n1.Deposit Money \n2.Withdraw Money \n3.Check Balance \n4.Change Pin \n5.Transaction History : "))
            if User_input == 1 :        # Statement to Deposit Money
                Deposit_M = int(input("Please enter amount to deposit: "))
                if Deposit_M >= 1000 and Deposit_M % 100 == 0 :
                    USer_information['Balance']+= Deposit_M
                    USer_information ['Transaction History'].append(f"Deposited: {Deposit_M}")
                    print("Amount is deposited and total amount is ", USer_information['Balance'])
                    user_chioce = int(input("Enter \n1.Home Page \n2. Exit: "))
                    if user_chioce == 1:
                        print("Taking you to Home page")
                    if user_chioce == 2:
                        print("Thank you for using our ATM")
                        break
                else:
                    print("Please deposit more than 1000 or Don't deposit change in this ATM")
                    break
            elif User_input == 2 :      # Statement to  Withdraw Money
                Withdraw_M = int(input("Enter amount to withdraw: "))
                if Withdraw_M <= USer_information ['Balance'] and Withdraw_M % 100 == 0 :
                        USer_information['Balance'] -= Withdraw_M
                        USer_information['Transaction History'].append(f'Withdraw: {Withdraw_M}')
                        print("Your have withdraw ", Withdraw_M, "and total amount in your bank is ", USer_information['Balance'])
                        exit_chioce = int(input("Enter \n1.HOme Page \n2.Exit: "))
                        if exit_chioce == 1:
                            print("Taking you to home page")
                        if exit_chioce == 2:
                            print("Thank you for using our ATM")
                            break
                else:
                    print(f"Total amount is {USer_information["Balance"]} and your are trying to withdraw {Withdraw_M} or This ATM can't provide change")
                    break
            elif User_input == 3 :      # Statement to Check Balance
                print("Your total balance is ", USer_information['Balance'])
                USER_Exit = int(input("Enter \n1.Home Page \n2.Exit: "))
                if USER_Exit == 1:
                    print("Taking you to home page")
                if USER_Exit == 2:
                    print("Thank you for using our ATM")
                    break
            elif User_input == 4:       # Statement to Changing pin
                Attempts_remaining = 3
                while Attempts_remaining > 0 :
                    Old_pin = input("Enter your old ATM PIN: ")
                    if len(Old_pin) == 4:
                        if Old_pin in USer_information ['ATM PIN']:
                            Pin_change = input("Enter a new 4 digits ATM PIN: ")
                            USer_information['ATM PIN'] = Pin_change
                            print("New pin is updated")
                            break
                        else:
                            remaining_attempts -= 1   # substrating wrong pin entered
                            if remaining_attempts > 0 :
                                print(f"Invalied pin entered and  You have {remaining_attempts} attempts left")
                            else:
                                print("You've run out of attempts, Your card has been temporarily blocked and Please contact customer service.")
                                break
                    else:
                        print("Please enter 4 digit password")
            elif User_input == 5 :
                for Transaction in USer_information ['Transaction History'] :
                    print(USer_information ['Transaction History'])
                    EXIT_input = int(input("Enter \n1.Home Page \n2.Exit: "))
                    if EXIT_input == 1:
                        print("Taking you to home page")
                    if EXIT_input == 2:
                        print("Thank you for using our ATM")
                        break
                else:
                    print("No transaction history")
                    break
            else:
                print("Invalied input")
                break

        print("Please enter 4 digit password")




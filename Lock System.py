User_password = {"Name" : "Teja Garikapati", "Password" : '6600'}
Remaining_attempts = 3
while Remaining_attempts > 0:
    Home_password = input('Enter password to open your home: ')
    if Home_password in User_password['Password'] :
        print("Welcome to Home")
        break
    else:
        Remaining_attempts -= 1
        if Remaining_attempts > 0 :
            print(f"Invalied Password You have {Remaining_attempts} attemps left")
        else:
            print("Someone is trying to open the door, Is it you")
            Wrong_password = int(input("Enter \n1.YES \n2.NO: "))
            if Wrong_password == 1:
                Own_name = input("Enter your name: ")
                if Own_name in User_password['Name']:
                    print("You've run out of attempts, Please 5 minutes or contact customer service")
                    break
                else:
                    print("Your not own of this house, an alarm will be ring in 5 seconds")
                    break
            else:
                print("Your not own of this house, an alarm will be ring in 5 seconds")
                break

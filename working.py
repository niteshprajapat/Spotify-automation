import bot
import password
import pyfiglet

developer = "Nitesh Prajapat"

print("\n\t\tDeveloper by :-\n")
name = pyfiglet.figlet_format(developer)
print(name)

print("Features :-")
print("1. Sign Up")
print("2. Login")

x = int(input("Enter your Choice :: "))

if __name__ == "__main__":
    if x == 1:
        bot.Sign_UP()

    elif x == 2:
        bot.Login(password.main_acc_email, password.main_acc_pwd)

    else:
        pass
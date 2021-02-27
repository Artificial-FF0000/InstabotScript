import socket, qrcode, wifi_qrcode
from instabot import Bot

#Dope banner because LMAO why not?
def Banner():
        print("                 A script written by Jonny")
print("'####:'##::: ##::'######::'########::::'###::::'########:::'#######::'########:")
print(". ##:: ###:: ##:'##... ##:... ##..::::'## ##::: ##.... ##:'##.... ##:... ##..::")
print(": ##:: ####: ##: ##:::..::::: ##:::::'##:. ##:: ##:::: ##: ##:::: ##:::: ##::::")
print(": ##:: ## ## ##:. ######::::: ##::::'##:::. ##: ########:: ##:::: ##:::: ##::::")
print(": ##:: ##. ####::..... ##:::: ##:::: #########: ##.... ##: ##:::: ##:::: ##::::")
print(": ##:: ##:. ###:'##::: ##:::: ##:::: ##.... ##: ##:::: ##: ##:::: ##:::: ##::::")
print("'####: ##::. ##:. ######::::: ##:::: ##:::: ##: ########::. #######::::: ##::::")
print("....::..::::..:::......::::::..:::::..:::::..::........::::.......::::::..:::::")
Banner()

#Main Menu Options.
MMenu = ["1. Generate a QR Code URL.", "2. Generate a Wifi QR_Code.", "3. Tell me my IPv4 Address."]
for x in MMenu:
        print(x)

#Records User Input for the Main Menu.

MMenuInput = int(input('What would you like to do? (Choose a number and hit Enter: )'))

if MMenuInput == 1:
    QRurl = input("What is the URL? ")
    URL = qrcode.make(QRurl)
    URL.save(QRurl + ".png")

    Caption = (str(input("What would you like th caption to say?")))
    print("The caption says " + Caption)

    Username = (str(input("What is your Instagram username? ")))
    #Find out how to hide the password as it's typed.
    Password = (str(input("What is your Instagram password? ")))

    bot = Bot()
    bot.login(username = Username,
              password = Password)
    bot.upload_photo(QRurl + ".png",
                     caption = Caption)

elif MMenuInput == 2:
    print("This generates a wifi qr code")
elif MMenuInput == 3:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("This is your Hostname")
    print(f"Hostname: {hostname}")

    print("This is your IPv4 Address")
    print(f"IP Address: {ip_address}")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import pickle, sys, os, time, shutil, re, webbrowser, random

class OxinyONE:
    def __init__(self):
        self.count = 0
        self.count += 1
        if self.count == 1:
            self.money = 150
            self.bag = []

    def start(self):
        def is_empty(file_path):
            return os.path.isfile(file_path) and os.path.getsize(file_path) > 0
        if is_empty("C:/StopIT/Log.dat"):
            self.login()
        else:
            self.register()

    def register(self):
        self.clean()
        os.system("color B")
        self.stop_it()
        self.name = input("\nHi, What is your name? ")
        self.lener2 = len(self.name)
        self.add = re.findall("[a-zA-Z0-9_]", self.name)
        if len(self.name) == len(self.add):
            print("Good, " + self.name + "!")
        else:
            print("uncorrect characters!")
            self.sleep()
            self.start()
        if self.lener2 <= 3:
            print("Your name must be at least 3 letters")
            self.sleep()
            self.start()
        else:
            self.path = "C:\\"
            self.NewFolder = "StopIT"
            os.chdir(self.path)
            os.makedirs(self.NewFolder)
            pickle.dump(self.money, open("C:/StopIT/Money.dat", "wb"))
            pickle.dump(self.name, open("C:/StopIT/Log.dat", "wb"))
            pickle.dump(self.bag, open("C:/StopIT/Bag.dat", "wb"))
            pickle.dump(self.achievements, open("C:/StopIT/Achievements.dat", "wb"))
            self.requests()

    def login(self):
        self.load_all()
        os.system("color B")
        self.requests()

    def menu(self):
        self.stop_it()
        print("\n          HI,", self.name + "!",  "          Money -", self.money, "$",
              "\n"
              "\nMAIN COMMANDS:"
              "\n"
              "\nCommand: update"
              "\nCommand: color"
              "\nCommand: leave"
              "\nCommand: shop"
              "\nCommand: trade"
              "\nCommand: bag"
              "\nCommand: logout"
              "\nCommand: about - very secret command!"
              "\nCommand: help <Command name> Example <help leave>"
              "\n")

        self.achievements()

    def requests(self):
        try:
            self.stop_it()
            self.menu()
            self.request = input(">>> ")

            if self.request == "leave":
                self.leave()

            elif self.request == "achievements":
                self.achievements()

            elif self.request == "color":
                self.color()

            elif self.request == "about":
                self.about()

            elif self.request == "shop":
                self.shop()

            elif self.request == "update":
                self.load_all()
                self.requests()

            elif self.request == "logout":
                self.logout()

            elif self.request == "bag":
                print(self.bag)
                input("Are you done? ")
                self.requests()

            elif self.request == "trade":
                self.buyers()

            else:
                print("Unknown command, " + self.request + "!")
                self.sleep()
                self.clean()
                self.requests()
                self.save_all()

        except:
            self.clean()
            os.system("color 7")
            print("[Error] - program exit!")
            self.sleep()
            print("Saving...")
            self.sleep()
            self.save_all()

    def shop(self):
        self.clean()
        self.stop_it()
        print("\n                              SHOP"
              "\n"
              "\n                Vegetables & Fruits"
              "\n        1: Apple 25 $         7: Banana 100 $"
              "\n        2: Orange 55 $        8: Onion 35 $"
              "\n        3: Pineapple 75 $     9: Carrot 80 $"
              "\n        4: WaterMelon 125 $   10: Pumpkin 170 $"
              "\n        5: Cherry 45 $        11: potato 95 $"
              "\n                  6: Tomat 90 $"
              "\n"
              "\nTo buy one item, type the product number"
              "\n")
        self.sell()

    def achievements(self):
        self.information = 0
        self.a1 = 0
        if self.a1 == 0:
            if self.money == 150:
                self.a1 += 1
                self.money += 100
                print("Get 150$ dollars")
                self.information += 1
                time.sleep(3)
                if self.information == 1:
                    print("YOU MADE AN ADVANCEMENT!")
                else:
                    print("You didnt any advancement!")
        if self.a1 == 1:
            print("REACHED GOT 150$")

    def buyers(self):
        self.random_buyer = random.randint(1, 11)
        if self.random_buyer == 1:
            try:
                self.buy_or = input("I want to buy Apple 45 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Apple")
                    self.money += 45
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 2:
            try:
                self.buy_or = input("I want to buy Orange 65 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Orange")
                    self.money += 65
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 3:
            try:
                self.buy_or = input("I want to buy Pineapple 90 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Pineapple")
                    self.money += 90
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 4:
            try:
                self.buy_or = input("I want to buy Watermelon 165 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Watermelon")
                    self.money += 165
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 5:
            try:
                self.buy_or = input("I want to buy Cherry 55 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Cherry")
                    self.money += 55
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 6:
            try:
                self.buy_or = input("I want to buy Tomat 125 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Tomat")
                    self.money += 125
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 7:
            try:
                self.buy_or = input("I want to buy Banana 120 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Banana")
                    self.money += 120
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 8:
            try:
                self.buy_or = input("I want to buy Onion 65 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Onion")
                    self.money += 65
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 9:
            try:
                self.buy_or = input("I want to buy Carrot 95 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Carrot")
                    self.money += 95
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()
        elif self.random_buyer == 10:
            try:
                self.buy_or = input("I want to buy Pumpkin 195 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Pumpkin")
                    self.money += 195
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

        elif self.random_buyer == 11:
            try:
                self.buy_or = input("I want to buy Potato 125 $, you have? y/n ")
                if self.buy_or == "y":
                    self.bag.remove("Potato")
                    self.money += 125
                else:
                    print("Okay bro i will come soon!")
                    self.sleep()
                    self.requests()
            except:
                print("Do not LIE!")
                if self.money >= 100:
                    self.money -= 100
                    self.sleep()
                    self.requests()
                else:
                    self.sleep()
                    self.requests()

    def sell(self):
        self.buy = input("What are you want? ")
        if self.buy == "1":
            if self.money >= 25:
                self.money -= 25
                print("you are buyed one item - Apple, Your money -", self.money)
                self.bag.append("Apple")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "2":
            if self.money >= 55:
                self.money -= 55
                print("you are buyed one item - Orange, Your money -", self.money)
                self.bag.append("Orange")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "3":
            if self.money >= 75:
                self.money -= 75
                print("you are buyed one item - Pineapple, Your money -", self.money)
                self.bag.append("Pineapple")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "4":
            if self.money >= 125:
                self.money -= 125
                print("you are buyed one item - Watermelon, Your money -", self.money)
                self.bag.append("Watermelon")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "5":
            if self.money >= 45:
                self.money -= 45
                print("you are buyed one item - Cherry, Your money -", self.money)
                self.bag.append("Cherry")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "6":
            if self.money >= 90:
                self.money -= 90
                print("you are buyed one item - Tomat, Your money -", self.money)
                self.bag.append("Tomat")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "7":
            if self.money >= 100:
                self.money -= 100
                print("you are buyed one item - Banana, Your money -", self.money)
                self.bag.append("Banana")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "8":
            if self.money >= 35:
                self.money -= 35
                print("you are buyed one item - Onion, Your money -", self.money)
                self.bag.append("Onion")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "9":
            if self.money >= 80:
                self.money -= 80
                print("you are buyed one item - Carrot, Your money -", self.money)
                self.bag.append("Carrot")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "10":
            if self.money >= 170:
                self.money -= 170
                print("you are buyed one item - Pumpkin, Your money -", self.money)
                self.bag.append("Pumpkin")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        elif self.buy == "11":
            if self.money >= 95:
                self.money -= 95
                print("you are buyed one item - Potato, Your money -", self.money)
                self.bag.append("Potato")
                self.sleep()
                self.requests()
            else:
                print("Bruh...")
                self.sleep()
                self.requests()
        else:
            print("Hmm...")
            self.sleep()
            self.requests()

    def color(self):
        print("\n0 = Black       8 = Gray        "
              "\n1 = Blue        9 = Light Blue  "
              "\n2 = Green       A = Light Green "
              "\n3 = Aqua        B = Light Aqua  "
              "\n4 = Red         C = Light Red   "
              "\n5 = Purple      D = Light Purple"
              "\n6 = Yellow      E = Light Yellow"
              "\n7 = White       F = Bright White")
        self.change_color = input("\n>>> ")
        if self.change_color == "0":
            os.system("color 0")
        elif self.change_color == "1":
            os.system("color 1")
        elif self.change_color == "2":
            os.system("color 2")
        elif self.change_color == "3":
            os.system("color 3")
        elif self.change_color == "4":
            os.system("color 4")
        elif self.change_color == "5":
            os.system("color 5")
        elif self.change_color == "6":
            os.system("color 6")
        elif self.change_color == "7":
            os.system("color 7")
        elif self.change_color == "8":
            os.system("color 8")
        elif self.change_color == "9":
            os.system("color 9")
        elif self.change_color == "A":
            os.system("color A")
        elif self.change_color == "B":
            os.system("color B")
        elif self.change_color == "C":
            os.system("color C")
        elif self.change_color == "D":
            os.system("color D")
        elif self.change_color == "E":
            os.system("color E")
        elif self.change_color == "F":
            os.system("color F")
        else:
            print("Unknown color!")
        self.requests()

    def save_all(self):
        os.remove("C:/StopIT/Money.dat")
        pickle.dump(self.money, open("C:/StopIT/Money.dat", "wb"))
        os.remove("C:/StopIT/Bag.dat")
        pickle.dump(self.bag, open("C:/StopIT/Bag.dat", "wb"))
        os.remove("C:/StopIT/Achievements.dat")
        pickle.dump(self.achievements, open("C:/StopIT/Achievements.dat", "wb"))

    def load_all(self):
        self.money = pickle.load(open("C:/StopIT/Money.dat", "rb"))
        self.name = pickle.load(open("C:/StopIT/Log.dat", "rb"))
        self.bag = pickle.load(open("C:/StopIT/Bag.dat", "rb"))
        self.achievements = pickle.load(open("C:/StopIT/Achievements.dat", "rb"))

    def leave(self):
        print("\nSaving please wait...")
        self.sleep()
        self.clean()
        os.system("color 7")
        self.save_all()

    def logout(self):
        self.sure = input("Are you sure? Remove all your data? y/n ")
        if self.sure == "y":
            shutil.rmtree("C:/StopIT")
            print("\nData removing...")
            self.sleep()
            self.clean()
            os.system("color 7")
        else:
            self.requests()

    def about(self):
        webbrowser.open_new("https://www.youtube.com/channel/UC_9rp90Pr0lYl93bLCGcnGA")
        self.requests()

    def clean(self):
        self.stuff()
        os.system("cls")

    def sleep(self):
        time.sleep(1)

    def stuff(self):
        pass

    def stop_it(self):
        self.clean()
        print("\n   /$$$$$$   /$$                            / $$   /$$      "
              "\n  /$$__  $$  | $$                           | $$   | $$     "
              "\n | $$  \__/ /$$$$$$     /$$$$$$    /$$$$$$  | $$  /$$$$$$   "
              "\n |  $$$$$$ |_  $$_/    /$$__  $$  /$$__  $$ | $$ |_  $$_/   "
              "\n  \____  $$  | $$     | $$  | $$ | $$  | $$ | $$   | $$     "
              "\n  /$$  \ $$  | $$ /$$ | $$  | $$ | $$  | $$ | $$   | $$ /$$ "
              "\n |  $$$$$$/  |  $$$$/ |  $$$$$$/ | $$$$$$$/ | $$   |  $$$$/ "
              "\n  \______/    \____/   \______/  | $$____/  |__/    \____/  "
              "\n                                 | $$                       "
              "\n                                 | $$                       "
              "\n                                 |__/                       "
              "\n                                                            "
              "\n     BETA | CODER : OxinyONE | YouTube OxinyONE | MORE?     ")
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def main():
    oxinyone = OxinyONE()
    oxinyone.start()

if __name__ == '__main__':
    main()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import pickle, sys, os, time, shutil, re, webbrowser, random

class OxinyONE:
    def __init__(self):
        pass

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
            pickle.dump(self.name, open("C:/StopIT/Log.dat", "wb"))
            pickle.dump(self.color, open("C:/StopIT/color.dat", "wb"))
            self.requests()

    def login(self):
        self.load_all()
        os.system("color B")
        self.requests()

    def menu(self):
        self.stop_it()
        print("\n          HI,", self.name + "!",
              "\n"
              "\nMAIN COMMANDS:"
              "\n"
              "\nCommand: update"
              "\nCommand: color"
              "\nCommand: leave"
              "\nCommand: "
              "\nCommand: "
              "\nCommand: "
              "\nCommand: logout"
              "\nCommand: about - very secret command!"
              "\n")

    def requests(self):
        try:
            self.stop_it()
            self.menu()
            self.request = input(">>> ")

            if self.request == "leave":
                self.leave()

            elif self.request == "color":
                self.color()

            elif self.request == "":
                pass

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

    def color(self):
        print("\n0 = Black       8 = Gray        "
              "\n1 = Blue        9 = Light Blue  "
              "\n2 = Green       A = Light Green "
              "\n3 = Aqua        B = Light Aqua  "
              "\n4 = Red         C = Light Red   "
              "\n5 = Purple      D = Light Purple"
              "\n6 = Yellow      E = Light Yellow"
              "\n7 = White       F = Bright White")

        self.change_color = input("\nC010R >>>")
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
        os.remove("C:/StopIT/color.dat")
        pickle.dump(self.color, open("C:/StopIT/color.dat", "wb"))

    def load_all(self):
        self.name = pickle.load(open("C:/StopIT/Log.dat", "rb"))
        self.color = pickle.load(open("C:/StopIT/color.dat", "rb"))

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
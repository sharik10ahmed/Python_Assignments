RED = '\033[91m'
RESET = '\033[0m'
WHITE = '\033[97m'
reset = '\033[0m'
l = int(input("Enter Length-> "))
b = int(input("Enter Breath-> "))
if l>b:
    rec = 2*(l+b)
    def fparameter(rec):
        print(f"Parameter of rectangle-> {rec} Centimeters\nArea of rectangle-> {l*b} Square Units")
    fparameter(rec)
else:
    print(f"{RED}WARNING !!!{RESET}".center(160))
    print(f"{WHITE}Invaild Response !{reset}".center(161))
    print("\n")
    print(f"{RED}BEWARE{RESET}".center(157))
    print(f"{WHITE}NOTE -> \"Length should be less than Breath\"{reset}".center(154))
    exit()
import locale as lc

def object_weightNEWTONS(massKg):
    weightNewtons = 0.0
    weightNewtons = massKg*9.8
    if weightNewtons < 100:
        print("Object is too light.")
    elif weightNewtons > 500:
        print("Object is too heavy.")
    else:
        print("Object weighs: " + str(round(weightNewtons, 2)) + " newtons")
    

def main():
    choice = "y"
    while choice == "y":
        massKg = float(input("Enter mass in Kilograms: "))
        
        weightNewtons = object_weightNEWTONS(massKg)

        print()
        choice = str(input("Would you like to compare again?: (y/n)  "))
        print()
    
if __name__ == "__main__":
    main()

		

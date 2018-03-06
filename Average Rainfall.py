def calculate_RainFall(years):
    for i in range(0, years):
        for n in range(0,12):
            inches = int(input("Enter amount of inches:"))
            s = i/12
    print("average number of rain fall: " + str(s))
    print()
def main():
    choice = "y"
    while choice == "y":
        
        years = int(input("Enter number of years: "))
        print()
        functionCallVAR = calculate_RainFall(years) #Variables can be passed into the function

        print()
        choice = str(input("Would you like to compare again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()
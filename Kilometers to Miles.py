def KM2Miles(kiloDist):
    milesDist = kiloDist*0.6214
    return(round(milesDist,2))

def main():
    choice = "y"
    while choice == "y":
        
        kiloDist = float(input("Enter distance in kilometers: "))
        
        distMI = KM2Miles(kiloDist) #Variables can be passed into the function
        print(distMI)

        print()
        choice = str(input("Would you like to run it again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()
def KM2Miles(kiloDist):
    #Converts kilometers to miles
    milesDist = kiloDist*0.6214
    #Returns the distance in miles, rounded to the 2nd decimal point
    return(round(milesDist,2))

def main():
    choice = "y"
    while choice == "y":
        
        #Prompts the user to input a distance in kilometers and stores it in variable kiloDist
        kiloDist = float(input("Enter distance in kilometers: "))
        
        #Passes value to function KM2Miles
        distMI = KM2Miles(kiloDist) #Variables can be passed into the function
        print(distMI)

        print()
        choice = str(input("Would you like to run it again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()

def calculate_MPH(uMPH, uHTRVLD):
    distance = 0
    hours = uHTRVLD
    speed = uMPH
    
    n=1
    iDist = float(1.0)
    
    print("Hours                Distance Traveled")
    for iDist in range(1, hours+1):
        print(str(n) + '\t\t\t\t'+str(speed))
        n += 1
        speed += uMPH

    print()
def main():
    choice = "y"
    while choice == "y":
        
        userMPH = int(input("Enter speed of vehicle: "))
        userHoursTRVLD = int(input("Enter hours traveled: "))
        print()
        functionCallVAR = calculate_MPH(userMPH, userHoursTRVLD) #Variables can be passed into the function

        print()
        choice = str(input("Would you like to compare again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()
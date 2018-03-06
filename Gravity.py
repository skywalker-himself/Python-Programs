def falling_distance(fallSEC):
    for i in range(0,10):
        distance = (1/2)*((fallSEC**2)*9.8)
        fallSEC -= 1
        print(round(distance, 2), str("meters"))

def main():
    choice = "y"
    while choice == "y":
        
        fallSEC = 10
        
        distM = falling_distance(fallSEC) #Variables can be passed into the function
        print(distM)

        print()
        choice = str(input("Would you like to run it again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()
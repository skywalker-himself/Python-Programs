def calculate_Factorial(posINT):
    #Sets initial condition
    if posINT == 1:
       print(posINT)
       return posINT
    #Sets recursive condition by calling function calculate_Factorial
    else:
        x = posINT * calculate_Factorial(posINT - 1)
        print(x)
        return x
    
def main():
    choice = "y"
    while choice == "y":
        
        #Prompts the user to enter a positive integer, and stores it in variable posINT
        posINT = int(input("Enter a positive integer: "))
        
        #Passes the value to function calculate_Factorial
        functionCallVAR = calculate_Factorial(posINT) #Variables can be passed into the function

        print()
        choice = str(input("Would you like to run it again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()

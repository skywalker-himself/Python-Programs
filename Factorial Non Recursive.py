def calculate_factorial(posINT):
    #Factorials start with 1
    x = 1
    
    #A for loop is used to get the products of the range from 1 to the integer the user entered.
    for i in range(1, posINT + 1):
        #Value of 'x' is updated after the products each iteration 
        x = i * x
        print(x)
    
def main():
    choice = "y"
    while choice == "y":
        #Prompts the user to input a positive integer
        posINT = int(input("Enter a positive integer: ")) 

        #Variables are passed to function calculate_factorial
        functionCallVAR = calculate_factorial(posINT) 

        print()
        
        choice = str(input("Would you like to run it again?: (y/n)  "))
        
        print()
        
if __name__ == "__main__":
    main()

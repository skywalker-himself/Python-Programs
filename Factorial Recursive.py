def calculate_factorial(posINT):
    x = 0
    if posINT == 1:
       print(posINT)
       return posINT
    else:
        x = posINT * calculate_factorial(posINT - 1)
        print(x)
        return x
def main():
    choice = "y"
    while choice == "y":
        
        posINT = int(input("Enter a positive integer: "))
        functionCallVAR = calculate_factorial(posINT) #Variables can be passed into the function

        print()
        choice = str(input("Would you like to run it again?: (y/n)  "))
        print()
if __name__ == "__main__":
    main()
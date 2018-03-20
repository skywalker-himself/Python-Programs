def main():
    #This for loop sets up how many rows of *'s there will be
    for n in range(0,7):
        #This for loop displays the number of *'s that should be displayed per row
        for i in range(7, n, -1):
            print("* ", end="")
        print()
if __name__ == "__main__":
    main()

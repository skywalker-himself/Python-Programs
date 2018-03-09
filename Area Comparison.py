def compareAreas(rect_firstLength, rect_firstWidth,rect_secondLength, rect_secondtWidth):
	
    #Receives the dimensions from both rectangles, and calculates their areas. 
    areaRecA = rect_firstLength * rect_firstWidth
    areaRecB = rect_secondLength * rect_secondtWidth

    #Compares the areas of the rectangles, and determines if one has a bigger area than the other, or if they have equal areas.
    #The results are printed.
    if areaRecA == areaRecB:
        print("The areas of the rectangles are the same.")
    elif areaRecA > areaRecB:
        print("Rectangle 'A' has more area than Rectangle 'B'.")
    else:
        print("Rectangle 'B' has more area than Rectangle 'A'.")

    

def main():
    choice = "y"

    while choice == "y":
		
        rectLA = float(input("Enter the length of rectangle 'A': ")) #Gets the length of rectangle 'A' from the user
        rectWA= float(input("Enter the width of rectangle 'A': ")) #Gets the width of rectangle 'A' from the user
        rectLB = float(input("Enter the length of rectangle 'B': ")) #Gets the length of rectangle 'B' from the user
        rectWB = float(input("Enter the width of rectangle 'B': ")) #Gets the width of rectangle 'B' from the user
	
        areaDifference = compareAreas(rectLA, rectWA, rectLB, rectWB) #passes the dimensions of the rectangles to the function compareAreas
	
        print()
	
        choice = str(input("Would you like to compare again?: (y/n)  "))

    
if __name__ == "__main__":
    main()

		

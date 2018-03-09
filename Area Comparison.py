import locale as lc

def compareAreas(rect_firstLength, rect_firstWidth,rect_secondLength, rect_secondtWidth):
    areaDifference = 0.0
    areaRecA = rect_firstLength * rect_firstWidth
    areaRecB = rect_secondLength * rect_secondtWidth

    if areaRecA == areaRecB:
        print("The areas of the rectangles are the same.")
    elif areaRecA > areaRecB:
        print("Rectangle 'A' has more area than Rectangle 'B'.")
    else:
        print("Rectangle 'B' has more area than Rectangle 'A'.")

    

def main():
    choice = "y"
    while choice == "y":
        rectLA = float(input("Enter the length of rectangle 'A': "))
        rectWA= float(input("Enter the width of rectangle 'A': "))
        rectLB = float(input("Enter the length of rectangle 'B': "))
        rectWB = float(input("Enter the width of rectangle 'B': "))
        areaDifference = compareAreas(rectLA, rectWA, rectLB, rectWB)
        print()
        choice = str(input("Would you like to compare again?: (y/n)  "))

    
if __name__ == "__main__":
    main()

		

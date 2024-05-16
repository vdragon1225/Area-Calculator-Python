import math # for pi

# function to calculate area of rectangle
def areaRectangle(length, width):
    return length * width

# function to calculate area of square
def areaSquare(side):
    return side * side

# function to calculate area of triangle
def areaTriangle(base, height):
    return 1/2 * (base * height)

# function to calculate area of circle
def areaCircle(radius):
    pi_value = math.pi
    return pi_value * (radius ** 2)

def main():
    # print welcome message
    print("Welcome to the Area Calculator!")

    # while loop to continue to play till user wants to stop
    while True:
        # ask user what shape they want to calculate area for
        shape = input("What shape do you want to calculate the area for? (rectangle/square/triangle/circle) ").lower()

        if shape == "rectangle": # calculate area of rectangle
            length = float(input("What is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            calculatedArea = round(areaRectangle(length, width), 1) # round area to one decimal place
            print("The area of the rectangle is", calculatedArea)
        elif shape == "square": #calculate area of square
            side = float(input("What is the length of the side? "))
            calculatedArea = round(areaSquare(side), 1) # round area to one decimal place
            print("The area of the square is", calculatedArea)
        elif shape == "triangle": # calculate area of triangle
            base = float(input("What is the base of the triangle? "))
            height = float(input("What is the height of the triangle? "))
            calculatedArea = round(areaTriangle(base, height), 1) # round area to one decimal place
            print("The area of the triangle is", calculatedArea)
        elif shape == "circle": # calculate area of circle
            radius = float(input("What is the radius of the circle? "))
            calculatedArea = round(areaCircle(radius), 1) # round area to one decimal place
            print("The area of the circle is", calculatedArea)
        else: # prompt user to enter a valid shape
            print("Please enter a valid shape ('rectangle', 'square', 'triangle', 'circle')")
            continue # make user enter another shape

        # ask user if they want to play again
        userChoice = input("Do you want to play again? (y/n) ").lower()
        
        # if statement to stop while loop
        if userChoice != 'y':
            print("Thank you for playing the Area Calculator!")
            break # stop while loop

if __name__ == "__main__":
    main()
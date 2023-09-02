def area(side_length):
    #Calculate the area of the square
    square_area = side_length ** 2
    return square_area
    
#Input the side length of the square from the user
side_length = float(input("Enter the side length of the square:"))

#Call the area() function to calculate the area
result = area(side_length)

#Display the calculated area
print(f"The area of the square with side length {side_length} is {result}")

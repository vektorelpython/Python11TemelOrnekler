"""
Write a program which accepts a one-digit integer from the user. 
The program should calculate the square of the given number. If the calculated square’s last digit is equal to the given input, the program should stop and print out the square. If not, program should continue by calculating the square of the square and so on if necessary. If no such square is found in 5 iterations, program should also stop and inform the user. 
"""

# sayi = int(input("Enter number:"))
# squareOf = sayi
# iteraNum = 0
# while iteraNum < 5:
#     squareOf = squareOf ** 2
#     if squareOf != str(squareOf)[::-1][0]:
#         print(squareOf)
#         break
#     iteraNum += 1
# else:
#     print(squareOf,sayi)


"""
Write a program that prompts the user to enter the height and radius of a cone. Use the
given values to calculate and show the volume of the cone. (Use pi as 3.14.)
"""
# import math

# height = float(input("Write Height"))
# radius = float(input("Write Radius"))
# print((1/3)*math.pi*(radius**2)*height)

"""
Write a program that accepts three inputs (two integers and one character as a string)
from the user and uses them to draw a rectangle of the desired string. The inner side 
of the rectangle should be empty. For example, if the user enters 4,10 and “&” as inputs,
the resulting rectangle should look like one of the below ones.
"""

num1 = int(input("Give Number1 "))
num2 = int(input("Give Number2 "))
char = input("Give Char ")

for i in range(0,num1):
    if not (i == 0  or i == num1-1):
        var1 = char + " "*(num2-2) + char 
    else:
        var1 = char*num2
    print(var1)


"""
Write a program that accepts two integers from the user which will be used as two angles
 from a triangle. After confirming that the numbers can be used as triangle angles 
 (i.e. their sum is smaller than 180, etc.), calculate the third angle and inform 
 the user whether the triangle is an isosceles triangle, equilateral triangle or a right 
 triangle when applicable. 
"""

























"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(numbers):
    length = len(numbers)
    index = (length-1) // 2

    if (length % 2):
        return numbers[index]
    else:
        return (numbers[index] + numbers[index + 1])/2.0

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print("The median is " + str(findMedian(numbers)))

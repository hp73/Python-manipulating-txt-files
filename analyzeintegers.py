"""
Author: Harry Pinkerton
Project 4
File name: analyzeintegers.py

This program reads a file of integers and displays the number of integers,
their average,their maximum value, and their minimum value.
"""

def main():
    """The starting point of the application."""
    print("Running the progam template.")

    filename = input("What is the File name?: ")
    f = open(filename, 'r')
    theSum = 0
    count = 0
    maximum = 0
    minimum = 9999999999999999999
    for line in f:
        count += 1
        lines = line.strip()
        number = int(line)
        theSum += number
        average = theSum / count
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    print("The Number of Integers is:",count)    
    print("The Average is:",average)
    print ("The Maximum is:",maximum)
    print("The Minimum is:",minimum)
    f.close()
    print("Have a nice day!")
if __name__ == "__main__":
    main()

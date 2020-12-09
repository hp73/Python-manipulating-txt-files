"""
Author: Harry Pinkerton
Project 4
File name: randomintegers.py

This program randomly generates integers to a text file. 
"""

def main():
    """The starting point of the application."""
    print("Running the progam template.")

    import random

    integers = int(input("How many integers are being generated: "))
    filename = input("What is the File name?: ")
    f = open(filename, 'w')

    for count in range (integers):
        numbers = random.randint(1, integers)
        f.write(str(numbers) + '\n')
    f.close()
    print("Have a nice day!")

if __name__ == "__main__":
    main()

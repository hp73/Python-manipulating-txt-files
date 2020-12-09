"""
Author: Harry Pinkerton
Project 4
File name: numberlines.py

This program takes a pre-existing file and numbers each line of text. After
numbering each line of text, the program creates a new file.
"""

def main():
    """The starting point of the application."""
    print("Running the progam template.")

    filename = input("Enter the File Name: ")

    inputFile = open(filename, "r")
    linenumber = 0
    newFile = open("numberedtestfile.txt", "w")

    for line in (inputFile):
        linenumber += 1
        string = ("%4s   %s" % (str(linenumber), line))
        newFile.write(string)
    
    print("Have a nice day!")
    
if __name__ == "__main__":
    main()

"""
Author: Harry Pinkerton
Project 4
File name: filestats.py

This program asks the user for a file name and states the number of characters,
number of words, and number of lines in the file. 
"""



def main():
    """The starting point of the application."""
    print("Running the progam template.")    
    
    filename = input("Enter the File Name: ")

    import os.path
    if not os.path.exists(filename):
        print('Error: the file not not exist!')

    else:
        inputFile = open(filename, "r")
        wordcount = 0
        characters = 0
        linenumber = 0
    
        for line in inputFile:
            linenumber += 1
            characters += len(line.split())
            wordcount += len(line)

        print("This File contains",linenumber, "lines,", wordcount, "words, and" ,characters, "characters") 
        
        print("Have a nice day!")

if __name__ == "__main__":
    main()

    


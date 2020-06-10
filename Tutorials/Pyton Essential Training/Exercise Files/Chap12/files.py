

def main():
    f = open('lines.txt') #this by default is read only mode 
    f = open('lines.txt', 'r') # read mode.
    f = open('lines.txt', 'w') # write mode. it empties the file even if the file is not empty and writes over the file
    f = open('lines.txt','a') #append mode. Starts at end of the file if the file is not empty
    f = open('lines.txt', 'r+') #read or write
    f = open('lines.txt', 'r+t') #text mode
    f = open('lines.txt', 'r+b') #binary mode
    for line in f:
        print(line.rstrip()) #rstrip strips any white spaces including new lines at the end of the line

if __name__ == '__main__': main()




x = 'string\n'

"""
by english word, that has 6 letters. This is followed by a metacharacter that indicates the end of the line.  New line character

In many systems, it is represented by a single line feed character, ASCII 10 Decimal , or zero A hex. Modern MACs and Unix Based Systems.
String has 7 bytes including line feed. 

In other systems, a new line is represented by a carriage return and the line feed. Because of the need to properly recognise any combination
of these line endings , most systems have separate modes for opening text files and non-text, or binary files. 

"""


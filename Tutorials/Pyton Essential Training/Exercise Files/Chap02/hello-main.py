

import platform

def main(): #this has a block of code
    message() #indentation & part of the main function
    #if there is a code here message() and this line of code are within the same block 

def message():
    print('This is python version {}'.format(platform.python_version())) #part of message function
    print('line 2')
    if False:
        print('Line 3') 
    else:
        print('not true') # under different block compared to else and if, since different indentation

if __name__ == '__main__': main()

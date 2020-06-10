

def main():
    infile = open('lines.txt', 'rt') #read and text mode .. read anf text mode is default so not necessary to specify, but being explicit is always better
    outfile = open('lines-copy.txt', 'wt') #this file will be created since it is write and text mode.. But take note it is not needed as by default it is text mode
    for line in infile:
        print(line.rstrip(), file=outfile) 
        #same as
        #outfile.writelines(line)
        print('.', end='', flush=True) #we are printing dots for every line that is written into the output file. Hence there are 10 lines and 10 dots. 
    outfile.close() #close file 
    infile.close() #less important as we won't lose any data but fine to specify
    print('\ndone.')

if __name__ == '__main__': main()


"""

 print(line.rstrip(), file=outfile) 
        #same as
outfile.writelines(line)

With print function I'm able to strip these line endings, and rewrite the line endings with the default line endings for this operating system, 
which print does by default, and that way, if my input file is from another operating system with different line endings, 
I'm actually serving to translate those line endings into the correct one for this operating system, so it's important to know that distinction.

You may or may not want that, in which case you may choose to use the writelines method instead.

"""
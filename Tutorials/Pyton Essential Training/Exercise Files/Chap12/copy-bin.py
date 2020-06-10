

def main(): 
    infile = open('berlin.jpg', 'rb') #binary mode NOT text mode as text mode will give error as the very first byte of the file is not a valid unicode character
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) #using 10 kb as the size of the buffer.  
        if buf:
            outfile.write(buf) 
            print('.', end='', flush=True)  
        else: break #empty buffer thus break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

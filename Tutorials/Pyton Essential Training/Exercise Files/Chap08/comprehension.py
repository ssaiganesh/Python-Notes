#list comprehension is a list created based on another list
# or iterator. 
def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    print_list(seq)
    print_list(seq2) #first sequence multiplied by 2
    seq3 = [x for x in seq if x % 3 != 0] #will get elements not divisible by 3
    print_list(seq3)
    seq4 = [(x, x**2) for x in seq] #tuples with original element and squared of the element
    print_list(seq4)
    from math import pi
    seq5 = [round(pi,i) for i in seq] #pi rounded to different dp (+1)
    print_list(seq5)
    seq6 = {x : x**2 for x in seq} #dictionary for key-value pairs
    print(seq6) # since dictionary cannot use the function of print_list below
    seq7 = {x for x in 'superduper' if x not in 'pd'} #only alphabets that are not pd but in superduper
    print_list(seq7)
    
def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

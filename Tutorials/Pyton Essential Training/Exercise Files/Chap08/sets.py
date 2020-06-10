#set is like a list that does not allow duplicate elements


def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    print_set(sorted(a)) #sorted order
    print_set(sorted(b))
    print_set(a - b) #members in set a but not in set b 
    print_set(a | b) #members in set a or set b or both
    print_set(a ^ b) # a or b but not both
    print_set(a & b) #only both 

    #but mostly won't use sorted for sets as if you want a ordered list,
    # you will use a list or a string

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

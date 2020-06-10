N = int(input("value: "))
i = 21
string = [i]
n = 1
while True:
    if(i<N):
        i += 11 * n
        n += 1
        string.append(i)
    elif(i==N):
        print(string)
        break
    
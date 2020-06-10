#str class is built in class .. standard strubg ckass
#inherting that and overwriting the string representation method
#to instead of returning the string itself, to returen a slice of the string where the
#step goes backwards. This will reverse the string in this case


class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()


#you can inherit and extend , and even as in this case, change built-in classes
#or classes that define yourself. Class inhertance is vital part of object-oritented programming
#and in Python, you can see it's relatively easy and intuitive
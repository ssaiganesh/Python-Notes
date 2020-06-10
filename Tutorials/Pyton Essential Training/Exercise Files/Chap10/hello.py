
import sys

def main():
    try:
        x = 5/0
    except ValueError:  ## x = int('foo')
        print('I caught a ValueError')
    #except ZeroDivisionError: ## x = 5/0
    #   print('don\'t divide by zero')
    except:
        print(f'unknown error: {sys.exc_info()}') #this explains the type of error
    else:
        print('Good Job!')
        print(x)
 
if __name__ == '__main__': main()


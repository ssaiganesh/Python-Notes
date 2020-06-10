hours= int(input("enter hours: ")) 
rate= int(input("enter rate: ")) 
def computepay(hours, rate): 
    wages= hours * rate  
    return wages

def computepay (overhours, rate):
    wages=int((overhours) *int(rate) *1.5)+(30*int(rate)) 
    return wages
 
if hours <=30:
    x=computepay(hours, rate) 
    print("pay: " +str(x)) 

else:
    overhours= hours -30
    x=computepay(overhours, rate) 
    print("pay: " +str(x))
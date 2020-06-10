

'While Loop'
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt  = 5


while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue #it skips 3
    pw = input(f"{count}: What's the secret word? ") #repeats this until swordfish is entered
else: #else statement here after breaking loop
    auth = True

print("Authorized" if auth else "Calling the FBI....")

"""
While Loop Controls

break

continue

else 

"""



    

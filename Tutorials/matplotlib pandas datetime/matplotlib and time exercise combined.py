
"""
Prorgam that helps the user to type faster
Input 5 times a word
Check how many seconds it took him to type each round. 
magnificient

mistakes were made how many
chart with typing speed evolution during the five rounds'


import time as t
import matplotlib as mpl
time_first = t.localtime()
first_try = input("Type the word magnificient: ")
time_afterinput = t.localtime()
time_difference = time_afterinput -time_first
j = 0
For i in range(0,5)
    another_try = input ("Type magnificient again: ")
    if(another_try != "magnificient"):
        j += 1
    time_anothertry = t.localtime()
    time_differences = time_anothertry - time_difference
    print(time_differences)
print("the number of mistakes are", j)
"""


import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

input("Press enter to continue.")
while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if(word.lower() != "magnificient"):
        mistakes += 1

print("You made "+ str(mistakes) + "mistakes")
print("Now let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()




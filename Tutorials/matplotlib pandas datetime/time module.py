import time as t
t.localtime()
time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")
t.time()
t.time()
time_now = t.time()
deliver_time = time_now + (86400 * 7 )
t.localtime(deliver_time)
t.sleep(5) #takes time 5 seconds for next line to appear

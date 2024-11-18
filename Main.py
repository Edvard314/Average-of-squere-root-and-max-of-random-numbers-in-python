import random
import math

progress = 100000 #set to 0 if you dont want updates, otherwise set it to how often you want updates (larger number = fewer iterations)

while True:
    try:
        noi = int(input("number of iterations:"))
        break
    
    except:
        print("please try again")

s1 = 0
s2 = 0

for i in range(1,noi):


    s1 += max(random.uniform(0,1),random.uniform(0,1))
    s2 += math.sqrt(random.uniform(0,1))
    
    
    if progress != 0:
        if i % progress == 0:
            print(i , "/" , noi , i/noi*100)


print((s1/noi,s2/noi))


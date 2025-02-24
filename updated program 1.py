#Ben Krehbiel
#2/24/2025
#gamba


import random as rn
def randdice():
    return rn.randint(1, 6) + rn.randint(1, 6)


#mainline
total = 0
for x in range(100):
    total += randdice()
else:
    print(round(total / 100 , 2))

import numpy as np #to generate random array

a=np.array([[1,2,3],[2,3,4],[1,2,3]])#nb
np.random.shuffle(a)
print(a)

'''import secrets true random be used for passorward
a=secrets.randbits(32)
secrets.randbelow()
secrets.randchoice()

print(a)
'''


'''  import random all these random is pseudo random 
#mylist=list('abcdefgh')
#random.shuffle(mylist)
#random.choices(mylist,k=3)
#random.uniform(1,4)
#random.randint(1,10) the scale without upper bonder
#random.random() whithout argument
print(mylist)
'''
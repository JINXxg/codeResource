#Collections: this is a modle in python 1:Counter 2:namedtuple(a lightweight way to create class only with two position) 


'''namedtuple need to know what time to use it 
from collections import namedtuple
Graph=namedtuple('Graph','collor') only two position
graph=Graph('pink')
print(graph)
'''
'''Counter
from collections import Counter
s="aaaabbbccc"
my_counter=Counter(s)
use my_counter.items() to check key&value pair tuple
my_counter.kers() check keys
my_counter.values() check values
my_counter.most_common() the most common element
my_counter.elements() add other data type coulde exchange

'''
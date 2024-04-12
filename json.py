import json

'''way to convert object to json
    class Users():
    def __init__(self,name,age):
        self.name=name
        self.age=age

users=Users('Mark',34)

def user_encode(o):#if use return with def just like java object with each onwn instance
    if isinstance(o,Users):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}#the __class__.__name__ python will automaticly output the class name
    else: 
        raise TypeError('wron type')


userJSON=json.dumps(users,default=user_encode)
print(userJSON)
'''

'''the way to converto json file to python 
    with open('person.json','r') as file:
    person=json.load(file)
    print(person)
'''


'''convert to jsonfile it's mean I could use python to write json file instead of write json directely
    with open('person.json','w') as file:
    json.dump(person,file,indent=4)
'''    
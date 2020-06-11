class person:
    def __init__(self,age=18,weight = 60):
        self.age = age
        self.__weight = weight

    def birthday(self):
        self.age+=1

    @staticmethod
    def nextage(age):
        return age + 1

    @property
    def weight(self):
        return self.__weight

    @classmethod
    def getchild(cls):
        return cls(age=0,weight=0.05)

    def anotherchild(self):
        cls = type(self)
        return cls(age=1,weight=3)

jack = person()
print(jack.age)
# print(jack.__weight)
# print(jack._person__weight)

child = jack.getchild()
child2 = jack.anotherchild()
print(child.age)
print(child.weight)
print(child2.age)
print(child2.weight)
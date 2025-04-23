from random import randint

class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if not self.__conjunto: return None
        return sum(self.__conjunto)/len(self.__conjunto)

num_elements = randint(1,50)
elements= [randint(1,1000)for i in range(num_elements)]

print(elements)
print(Conjunto(elements).promedio())
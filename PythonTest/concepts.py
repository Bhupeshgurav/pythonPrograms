# lambda
def add(a, b):
    return a+b


sol = add(10, 15)
print(type(sol))

#


def result(num1, num2): return num1*num2


print(type(result))


def result(a, b): return a+b


print(type(result))

set1 = ("val")
print(type(set1))

# inside the tuple we are having one limitation
ls = [1, 2, 3, 4, 5, 67]

(i > 3 for i in lst)

#(exp for i in var)


class IceCream:
    def __init(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)


def sweetest_icecreamlst(lst):
    flavor_val = {
        "Plain": 0,
        "Vanila": 5,
        "ChocolateChip": 5,
        "Strawberry": 10,
        "Chocolate": 10
    }
    return (i.num_sprinkles + flavor_val[i.flavor] for i in lst)

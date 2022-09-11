
# Functional Prompt

# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
# Remember, when writing in a functional style:

#   - Keep variables immutable
#   - Write only pure functions
#   - Remember, functions may be higher order

from enum import Enum


def flatten_and_sort(int_list):
    new_list = []

    def flatten(l):
        for item in l:
            if type(item) == list:
                flatten(item)
            else:
                new_list.append(item)

    flatten(int_list)

    return sorted(new_list)


print(flatten_and_sort([17, 4, 55, 12, 33, 8]))  #  [4, 8, 12, 17, 33, 55]
print(flatten_and_sort([2, 22, 0, 80, [47, 19]]))  #  [0, 2, 19, 22, 47, 80]
print(flatten_and_sort([11, 2, [23, 14, [5]], [109, 47, [91, 16, [25]]]]))  #  [2, 5, 11, 14, 16, 23, 25, 47, 91, 109]


# Once a functional solution to this problem has been implemented, answer the following questions.

#   - How does this solution ensure data immutability? - The input list is NOT changed. The function returns a new

#   - Is this solution a pure function? Why or why not? - Yes! Does not produce or rely on side effects and it's
#                                                         list output purely depends on its input

#   - Is this solution a higher order function? Why or why not? - It is not a higher order function because it does
#                                                                 not take a function as input nor does return a
#                                                                 function

#   - Would it have been easier to solve this problem using a different programming style? - No

#   - Why in particular is functional programming
#     a helpful paradigm when solving this problem? - It is easier to decompose this problem into a set of functions


#


#


#  Object Oriented Prompt


#  Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing
#  an Object Oriented solution according to the following criteria.

#   - First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired)
#     and price attributes.
#   - Define a repair() method that will update the condition of the podracer to "repaired".
#   - Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called
#     boost that will multiply max_speed by 2.
#   - Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special
#     method called flame_jet that will update the condition of another podracer to "trashed".


class CONDITION(Enum):
    PERFECT = 1
    TRASHED = 2
    REPAIRED = 3


class Podracer():
    def __init__(self, max_speed, condition, price) -> None:
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = CONDITION.REPAIRED


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed += 2


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)

    def flame_jet(self, podracer):
        if isinstance(podracer, Podracer):
            podracer.condition = CONDITION.TRASHED
        else:
            print("this method can only be used on Podracer derived types")


#

sp = SebulbasPod(9, CONDITION.PERFECT, 10000000)
ap = AnakinsPod(10, CONDITION.PERFECT, 20000000)

# Once an Object Oriented solution has been implemented, answer the following questions:

#   - How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

#       - Encapsulation - attributes and functions are bundled together

#       - Abstraction - For example, when we call the function repair, we don't care about how repair is implemented

#       - Inheritance - AnakinsPod and SebulbasPod inherits name, max_speed, and condition from parent class Podracer


print(f"sp is SebulbasPod -> {isinstance(sp , SebulbasPod)}")  #  sp is SebulbasPod -> True
print(f"sp is Podracer -> {isinstance(sp , Podracer)}")  #  sp is Podracer -> True
print(f"ap is AnakinsPod -> {isinstance(ap , AnakinsPod)}")  #  ap is AnakinsPod -> True
print(f"ap is Podracer -> {isinstance(ap , Podracer)}")  #  ap is Podracer -> True

#       - Polymorphism - The function 'flame_jet' expects type Podracer. When calling this function we can pass in an object of type Podracer, AnakinsPod, or SebulbasPod

sp.flame_jet(ap)
print(f"ap condition -> {ap.condition}")  # ap condition -> CONDITION.TRASHED

x = 10
sp.flame_jet(x)  # this method can only be used on Podracer derived types

#     Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? - Not really, the solution would be much more complex

#     How in particular did Object Oriented Programming assist in the solving of this problem? - Inheritance, Polymorphism

ap.repair()
print(f"ap condition -> {ap.condition}")  # ap condition -> CONDITION.REPAIRED

print(f"ap -> max_speed: {ap.max_speed}, condition: {ap.condition}, price: {ap.price}")  #  ap -> max_speed: 10, condition: CONDITION.REPAIRED, price: 20000000
ap.boost()
print(f"ap -> max_speed: {ap.max_speed}")  #  ap -> max_speed: 12
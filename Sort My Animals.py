"""
LINK:https://www.codewars.com/kata/58ff1c8b13b001a5a50005b4/train/python

Consider the following class:

class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs
Write a method that accepts a list of objects of type Animal, and returns a new list. The new list should be a copy of the original list, sorted first by the animal's number of legs, and then by its name.

If null or None is passed in, the method should return the same. If an empty list is passed in, it should return an empty list back.

LISTS SORTING FUNDAMENTALS
"""
def sort_key(animal):
    return animal.number_of_legs,animal.name

def sort_animals(input):
    return sorted(input, key=sort_key)
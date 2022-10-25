from add import add_fruit
from multiply import multiply_fruit
from divide import divide_fruit


apples = int(input("How many apples?"))
oranges = int(input("How many oranges?"))

#function called for adding apples and orages
fruit = add_fruit(apples, oranges)
print(fruit)

#function for dividing apples and oranges
divide = divide_fruit(apples, oranges)
print(divide)
#function for multiplying apples and oranges
multiply = multiply_fruit(apples, oranges)
print(multiply)
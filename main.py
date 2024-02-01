from main_decorator import logger
import os

path = 'log_1.log'

if os.path.exists(path):
    os.remove(path)

@logger(path)
def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        dishes = {} # Блюда
        for line in file.read().split('\n\n'):
            ingredients_quantity = [] # ингридиенты количество
            name, *ingredients = line.split('\n')
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split('|')
                ingredients_quantity.append(
                          {
                              'ingredient_name': ingredient_name,
                              'quantity': int(quantity),
                              'measure': measure
                          }
                      )
                dishes[name] = ingredients_quantity
        return dishes

my_cook_book() # Вызов функции

"""
Peace of cake.
By: Eliad Karni.

The feature receives a dict of ingredients as keys and its prices as value,
a list of unconsderable in calculatinon ingredients, and dict of 
as keys, ingredients and its amounts needed.
The code calculate and returns the final recepie price.
"""

def get_recipe_price(prices: dict, optionals: list = None, **ingredients):
    '''
    The code receives a dict of ingredients as keys and its prices as value,
    a list of unconsderable in calculatinon ingredients, and dict of 
    as keys, ingredients and its amounts needed.
    The code calculate and returns the final recepie price.
    '''
    final_price = 0
    for ingredient, amount in ingredients.items():
        if not optionals or ingredient not in optionals:
            final_price += prices.get(ingredient) * (amount / 100)
    return int(final_price)

if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

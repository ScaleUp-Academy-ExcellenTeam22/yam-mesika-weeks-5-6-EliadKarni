"""
Peace of cake.
By: Eliad Karni.

The code receives a dict of ingredients as keys and its prices as value,
    a list of optional ingredients which needed to be reduced in the calculation, and dict of
    the recipe's ingredients as keys, and the needed amount of each as value.
"""


def get_recipe_price(prices: dict, optionals: list = None, **ingredients) -> int:
    """
    The function receives a dict of ingredients as keys and its prices as value,
    a list of optional ingredients which needed to be reduced in the calculation, and dict of
    the recipe's ingredients as keys, and the needed amount of each as value.
    :param prices: Ingredients as keys and its prices as value.
    :param optionals: List of reduced ingredients which needed to be ignored in the calculation.
    :param ingredients: The recipe's ingredients as keys, and the needed amount of each as value.
    :return The code calculate and returns the final recipe price.
    """
    final_price = 0
    for ingredient, amount in ingredients.items():
        if not optionals or ingredient not in optionals:
            final_price += prices.get(ingredient) * (amount / 100)
    return int(final_price)


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))



class Allergies(object):

    ALLERGENS = (
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats'
    )

    def __init__(self, score):
        self._allergens = set(
            a for i, a in enumerate(self.ALLERGENS)
            if 1 << i & score > 0
        )

    def is_allergic_to(self, allergen):
        return allergen in self._allergens

    @property
    def lst(self):
        return list(self._allergens)

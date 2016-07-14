from itertools import permutations


def right(x, y):
    return x - y == 1


def next_to(x, y):
    return right(x, y) or right(y, x)


def solution():
    # 1. There are five houses.
    # (identify by nationality)
    englishman, spaniard, ukrainian, norwegian, japanese = range(5)
    perms = list(permutations(range(5)))
    answers = next(
        (zebra, water)
        for (first, second, middle, fourth, last) in perms
        # 10. The Norwegian lives in the first house.
        if norwegian is first
        for (red, green, yellow, blue, ivory) in perms
        # 15. The Norwegian lives next to the blue house.
        if next_to(norwegian, blue)
        # 6. The green house is immediately to the right of the ivory house.
        if right(ivory, green)
        # 2. The Englishman lives in the red house.
        if red is englishman
        for (dog, fox, horse, snails, zebra) in perms
        # 3. The Spaniard owns the dog.
        if dog is spaniard
        for (coffee, tea, orange_juice, milk, water) in perms
        # 9. Milk is drunk in the middle house.
        if milk is middle
        # 4. Coffee is drunk in the green house.
        if green is coffee
        # 5. The Ukrainian drinks tea.
        if ukrainian is tea
        for (old_gold, chesterfields, lucky_strike, parliaments, kools) in perms
        # 7. The Old Gold smoker owns snails.
        if old_gold is snails
        # 8. Kools are smoked in the yellow house.
        if kools is yellow
        # 11. The man who smokes Chesterfields lives in the house next to the
        # man with the fox.
        if next_to(chesterfields, fox)
        # 12. Kools are smoked in the house next to the house where the horse
        # is kept.
        if next_to(kools, horse)
        # 13. The Lucky Strike smoker drinks orange juice.
        if lucky_strike is orange_juice
        # 14. The Japanese smokes Parliaments.
        if japanese is parliaments
    )

    names = ('Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese')
    return ('It is the {} who drinks the water.\n'
            'The {} keeps the zebra.'.format(*(names[i] for i in answers)))

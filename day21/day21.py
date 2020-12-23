from utils import file_utils


def solution(file_name):
    all_ingredients, ingredients_by_allergen = prepare_data(file_name)
    associated_ingredients, real_allergens = find_hypoallergenics(ingredients_by_allergen)
    return len([ingredient for ingredient in all_ingredients if ingredient not in real_allergens])


def solution2(file_name):
    all_ingredients, ingredients_by_allergen = prepare_data(file_name)
    associated_ingredients, real_allergens = find_hypoallergenics(ingredients_by_allergen)
    print('trop la flemme, fini à la main...')


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    ingredients_by_allergen = dict()
    all_ingredients = list()
    for line in lines:
        ingredients_allergens = line.split(' (')
        ingredients = set(ingredients_allergens[0].split(' '))
        all_ingredients.extend(ingredients)
        allergens = ingredients_allergens[1].replace(')', '').removeprefix('contains ').split(', ')
        for allergen in allergens:
            if allergen in ingredients_by_allergen:
                ingredients_list = ingredients_by_allergen[allergen]
            else:
                ingredients_list = list()
                ingredients_by_allergen[allergen] = ingredients_list
            ingredients_list.append(ingredients)

    return all_ingredients, ingredients_by_allergen


def find_hypoallergenics(ingredients_by_allergen):
    real_allergens = set()
    associated_ingredients = dict()
    for allergen in ingredients_by_allergen:
        ingredients_list = ingredients_by_allergen[allergen]
        intersect = ingredients_list[0].intersection(*ingredients_list)
        real_allergens.update(intersect)
        associated_ingredients[allergen] = intersect
    return associated_ingredients, real_allergens


def test_solution():
    count_hypoallergenic_occurences = solution('input')
    print(count_hypoallergenic_occurences)
    assert 2614 == count_hypoallergenic_occurences


def test_solution2():
    solution2('input')

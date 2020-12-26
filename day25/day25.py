def transform_number(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value = loop_round(subject_number, value)
    return value


def loop_round(subject_number, value):
    value = value * subject_number
    value = value % 20201227
    return value


def card_transform(card_loop_size):
    transform_number(7, card_loop_size)


def door_transform(door_loop_size):
    transform_number(7, door_loop_size)


def test_sample():
    assert transform_number(7, 8) == 5764801
    assert transform_number(7, 11) == 17807724
    assert transform_number(17807724, 8) == 14897079
    assert transform_number(5764801, 11) == 14897079


def find_loop(searched_number):
    result = 1
    not_found = True
    card_loop = 1
    while not_found:
        result = loop_round(7, result)
        if result == searched_number:
            return card_loop
        card_loop += 1


def test_find_card():
    card_loop = find_loop(15335876)
    assert 250288 == card_loop


def test_find_door():
    door_loop = find_loop(15086442)
    assert 14519824 == door_loop


def test_find_key():
    card_key = transform_number(15086442, 250288)
    door_key = transform_number(15335876, 14519824)
    print(card_key)
    assert card_key == door_key

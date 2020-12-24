def prepare_data(cups):
    return [int(cup) for cup in cups]

def turns(cups):
    return one_turn(cups, 0)


def one_turn(cups, current_cup_index):
    all_cups = cups.copy()
    current_index_value = cups[current_cup_index]
    length = len(cups)
    next_start = (current_cup_index + 1) % length
    next_end = (next_start + 3) % length
    if next_start>next_end:
        pickedup_cups = cups[next_start:]+cups[:next_end]
        del cups[next_start:]
        del cups[:next_end]
    else:
        pickedup_cups = cups[next_start:next_end]
        del cups[next_start:next_end]
    destination_cup = current_index_value-1
    if destination_cup < min(all_cups):
        destination_cup = max(all_cups)
    while destination_cup in pickedup_cups:
        destination_cup -= 1
        if destination_cup < min(all_cups):
            destination_cup = max(all_cups)
    index = cups.index(destination_cup)
    cups = insert_position(index + 1, cups, pickedup_cups)
    current_cup_index = (cups.index(current_index_value)+1)%length
    return current_cup_index, cups


def insert_position(position, list1, list2):
    return list1[:position] + list2 + list1[position:]


def test_prepare_data():
    cups = '523764819'
    cups = prepare_data(cups)
    print(cups)
    current_index = 0
    for i in range(100):
        current_index, cups = one_turn(cups, current_index)
    print(cups)
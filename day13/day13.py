from utils import file_utils, math_utils


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    earliest = int(lines[0])
    bus_ids = lines[1].split(',')
    bus_ids = list(filter(lambda x: x != 'x', bus_ids))
    return earliest, [int(id) for id in bus_ids]


def solution(file_name):
    earliest, bus_ids = prepare_data(file_name)
    gap = [id - (earliest % id) for id in bus_ids]
    minutes = min(gap)
    index = gap.index(minutes)
    return minutes * bus_ids[index]


def solution2(file_name):
    ids_with_gaps = prepare_data2(file_name)
    return calculate_with_chinese_remainder(ids_with_gaps)


def calculate_with_chinese_remainder(ids_with_gaps):
    bus_ids = ids_with_gaps.keys()
    produit_total = math_utils.prod(bus_ids)
    e_a_s = [calculate_prod_e_a(calculate_e(bus_id, produit_total), ids_with_gaps, bus_id) for
             bus_id in bus_ids]
    return sum(e_a_s) % produit_total


def calculate_prod_e_a(ei, ids_with_gaps, bus_line):
    return ids_with_gaps[bus_line] % bus_line * ei


def calculate_e(ni, produit_total):
    nic = produit_total // ni
    vi = math_utils.euclid_extended_calc(ni, nic)[1]
    ei = vi * nic
    return ei


def prepare_data2(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    bus_ids = lines[1]
    return build_gaps_by_bus_id(bus_ids)


def build_gaps_by_bus_id(bus_ids):
    gap = 0
    ids_with_gaps = dict()
    for id in bus_ids.split(','):
        if id != 'x':
            ids_with_gaps[int(id)] = int(id) - gap
        gap += 1
    return ids_with_gaps

from utils import file_utils
import re

PASSPORTS_SEPARATOR = '*'
PASSPORTS_INFO_SEPARATOR = ' '
JOINED_PASSPORTS_SEPARATOR = " %s " % PASSPORTS_SEPARATOR


def solution(file_name):
    passports = prepare_data(file_name)
    return len([line for line in passports if line.is_valid()])


def solution2(file_name):
    passports = prepare_data(file_name)
    return len([line for line in passports if line.is_full_valid()])


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    lines = [line if line else PASSPORTS_SEPARATOR for line in lines]
    joined_lines = PASSPORTS_INFO_SEPARATOR.join(lines)
    prepared_lines = joined_lines.split(JOINED_PASSPORTS_SEPARATOR)
    return [Passport(line) for line in prepared_lines]


def validate_birthyear(byr):
    return validate_number(byr, 1920, 2002)


def validate_issueyear(iyr):
    return validate_number(iyr, 2010, 2020)


def validate_expirationyear(eyr):
    return validate_number(eyr, 2020, 2030)


def validate_number(number_string, min, max):
    try:
        return min <= int(number_string) <= max
    except ValueError:
        return False


def validate_height(hgt):
    unit = hgt[- 2:]
    hgt_num = hgt[: - 2]
    if unit == "cm":
        return validate_number(hgt_num, 150, 193)
    elif unit == "in":
        return validate_number(hgt_num, 59, 76)
    else:
        return False


HAIR_COLOR_REGEX = re.compile('^\#([0-9]|[a-f]){6}$')


def validate_haircolor(hcr):
    return HAIR_COLOR_REGEX.search(hcr) != None


VALID_EYES_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_eyecolor(ecr):
    return ecr in VALID_EYES_COLORS


VALID_PASSWORD_REGEX = re.compile('^([0-9]){9}$')


def validate_passwordid(pid):
    return VALID_PASSWORD_REGEX.search(pid) != None


PASSPORT_VALIDATORS = dict()
PASSPORT_VALIDATORS["byr"] = validate_birthyear
PASSPORT_VALIDATORS["iyr"] = validate_issueyear
PASSPORT_VALIDATORS["eyr"] = validate_expirationyear
PASSPORT_VALIDATORS["hgt"] = validate_height
PASSPORT_VALIDATORS["hcl"] = validate_haircolor
PASSPORT_VALIDATORS["ecl"] = validate_eyecolor
PASSPORT_VALIDATORS["pid"] = validate_passwordid


class Passport:
    def __init__(self, line):
        self.passport_info = dict()
        parts = line.split()
        for part in parts:
            split = part.split(":")
            self.passport_info[split[0]] = split[1]

    def is_valid(self):
        return (len(self.passport_info) == 7 and "cid" not in self.passport_info) or len(
            self.passport_info) == 8

    def is_full_valid(self):
        return self.is_valid() and self.validate_data()

    def validate_data(self):
        for key in PASSPORT_VALIDATORS:
            if not PASSPORT_VALIDATORS[key](self.passport_info[key]):
                return False
        return True


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))

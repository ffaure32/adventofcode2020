from utils import file_utils
import re


def solution(file_name):
    passports = prepare_data(file_name)
    return len([line for line in passports if line.is_valid()])


def solution2(file_name):
    passports = prepare_data(file_name)
    return len([line for line in passports if line.is_full_valid()])


def prepare_data(file_name):
    lines = file_utils.get_lines("inputs", file_name)
    prepared_lines = list()
    actual_string = ""
    for line in lines:
        if not line:
            prepared_lines.append(actual_string)
            actual_string = ""
        else:
            actual_string += " " + line
    prepared_lines.append(actual_string)
    return [Passport(line) for line in prepared_lines]


def validate_birthyear(byr):
    return validate_number(byr, 1920, 2002)


def validate_issueyear(byr):
    return validate_number(byr, 2010, 2020)


def validate_expirationyear(byr):
    return validate_number(byr, 2020, 2030)


def validate_number(year, min, max):
    try:
        year = int(year)
        return min <= year <= max
    except ValueError:
        return False


def validate_height(hgt):
    hgt_cut = len(hgt) - 2
    if hgt_cut <= 0:
        return False
    unit = hgt[hgt_cut:]
    hgt_num = hgt[: hgt_cut]
    if unit == "cm":
        return validate_number(hgt_num, 150, 193)
    elif unit == "in":
        return validate_number(hgt_num, 59, 76)
    else:
        return False


hcr_regex = re.compile('^\#([0-9]|[a-f]){6}$')


def validate_haircolor(hcr):
    return hcr_regex.search(hcr) != None


valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_eyecolor(ecr):
    return ecr in valid_colors


pid_regex = re.compile('^([0-9]){9}$')


def validate_passwordid(pid):
    return pid_regex.search(pid) != None


validators = dict()
validators["byr"] = validate_birthyear
validators["iyr"] = validate_issueyear
validators["eyr"] = validate_expirationyear
validators["hgt"] = validate_height
validators["hcl"] = validate_haircolor
validators["ecl"] = validate_eyecolor
validators["pid"] = validate_passwordid


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
        for key in validators:
            if not validators[key](self.passport_info[key]):
                return False
        return True


if __name__ == "__main__":
    print(solution("input"))
    print(solution2("input"))

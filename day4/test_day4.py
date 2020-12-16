import day4


def test_prepare_data():
    result = day4.prepare_data("test_1")
    assert len(result) == 4


def test_parse_passport():
    input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    passport = day4.Passport(input)
    assert passport.is_valid()

def test_parse_valid_passport():
    input = "byr:2010 pid:#1bb4d8 eyr:2021 hgt:186cm iyr:2020 ecl:grt"
    passport = day4.Passport(input)
    assert not passport.is_valid()


def test_day4():
    result = day4.solution("test_1")
    assert result == 2


def test_day4_real():
    result = day4.solution("inputs")
    assert result == 213


def test_validate_byr():
    assert day4.validate_birthyear("1920")
    assert day4.validate_birthyear("2002")
    assert not day4.validate_birthyear("2003")
    assert not day4.validate_birthyear("1919")
    assert not day4.validate_birthyear("sdfsdf")


def test_validate_iyr():
    assert day4.validate_issueyear("2010")
    assert day4.validate_issueyear("2020")
    assert not day4.validate_issueyear("2021")
    assert not day4.validate_issueyear("2009")
    assert not day4.validate_issueyear("sdfsdf")


def test_validate_eyr():
    assert day4.validate_expirationyear("2020")
    assert day4.validate_expirationyear("2030")
    assert not day4.validate_expirationyear("2019")
    assert not day4.validate_expirationyear("2031")
    assert not day4.validate_expirationyear("sdfsdf")


def test_validate_hgt():
    assert day4.validate_height("150cm")
    assert day4.validate_height("193cm")
    assert not day4.validate_height("149cm")
    assert not day4.validate_height("194cm")
    assert day4.validate_height("59in")
    assert day4.validate_height("76in")
    assert not day4.validate_height("58in")
    assert not day4.validate_height("77in")
    assert not day4.validate_height("123fr")
    assert not day4.validate_height("r")
    assert not day4.validate_height("dsfsdfdsr")


def test_validate_ecl():
    assert day4.validate_eyecolor("amb")
    assert day4.validate_eyecolor("blu")
    assert day4.validate_eyecolor("brn")
    assert day4.validate_eyecolor("gry")
    assert day4.validate_eyecolor("grn")
    assert day4.validate_eyecolor("hzl")
    assert day4.validate_eyecolor("oth")
    assert not day4.validate_eyecolor("dsfsdfdsr")


def test_validate_hcl():
    assert day4.validate_haircolor("#123abc")
    assert not day4.validate_haircolor("#123abz")
    assert not day4.validate_haircolor("123abc")


def test_validate_pid():
    assert day4.validate_passwordid("123456789")
    assert day4.validate_passwordid("000000123")
    assert not day4.validate_passwordid("1234567891")


def test_full_valid_password():
    is_full_valid("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f")
    is_full_valid("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
    is_full_valid("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")
    is_full_valid("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022")


def test_full_invalid_password():
    is_not_full_valid("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
    is_not_full_valid("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946")
    is_not_full_valid("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
    is_not_full_valid("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007")

def is_full_valid(input):
    passport = day4.Passport(input)
    assert passport.is_full_valid()

def is_not_full_valid(input):
    passport = day4.Passport(input)
    assert not passport.is_full_valid()


def test_day4_part2():
    result = day4.solution2("test_1")
    assert result == 2


def test_day4_real_part2():
    result = day4.solution2("inputs")
    assert result == 147


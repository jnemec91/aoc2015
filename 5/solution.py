import re

def is_vowel(s:str) -> bool:
    """check if letter is a vowel"""
    vowels = ['a','e','i','o','u']
    if s in vowels:
        return True
    return False

def does_not_contain_these(s:str) -> bool:
    """check if string contains forbidden substrings"""
    forbidden = ["ab", "cd", "pq", "xy"]
    for i in forbidden:
        if i in s:
            return False
    return True

def get_number_of_nice_strings(inp):
    """check the input for count of 'nice' strings"""
    counter = 0

    for s in inp:
        if does_not_contain_these(s):
            last_letter = ''
            has_double_letter = False
            vowel_counter = 0
            for i in s:
                if is_vowel(i):
                    vowel_counter += 1

                if last_letter == i:
                    has_double_letter = True

                last_letter = i

            if vowel_counter >= 3 and has_double_letter:
                counter += 1

    return counter


def contains_two_pairs_of_same_letter(s):
    """
    checks if string contains two pairs of same letters that not overlap with regex
    (e.g.: abab, xxyxx, bcafhgjejkbc)
    """
    if re.search(r'(\w)(\w).*(\1)(\2)', s):
        # print(re.search(r'(\w)(\w).*(\1)(\2)', s))
        return True
    return False

def contains_same_letter_spaced_by_one(s):
    """checks if string contains same letter spaced by any letter with regex (e.g.: yxy, aba)"""
    if re.search(r'(\w)\w(\1)', s):
        # print(re.search(r'(\w)\w(\1)', s))
        return True
    return False

def get_number_of_nice_strings_2(inp):
    """checks the input for number of the 'nice' strings"""
    counter = 0
    for s in inp:
        if contains_same_letter_spaced_by_one(s) and contains_two_pairs_of_same_letter(s):
            counter += 1
    return counter

if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as f:
        inp = f.read().split()

        print(f'Part one: {get_number_of_nice_strings(inp)}')
        print(f'Part two: {get_number_of_nice_strings_2(inp)}')
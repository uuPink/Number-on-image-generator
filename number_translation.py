"""Translates integers to strings. Works within the number range 0:1000 (meaning 1000 isn't included)"""

translation_small = {
    "0": "noll",
    "1": "ett",
    "2": "två",
    "3": "tre",
    "4": "fyra",
    "5": "fem",
    "6": "sex",
    "7": "sju",
    "8": "åtta",
    "9": "nio"}

translation_big = {
    10: "tio", 
    '10': "tio",
    "11": "elva",
    "12": "tolv",
    "13": "tretton",
    "14": "fjorton",
    "15": "femton",
    "16": "sexton",
    "17": "sjutton",
    "18": "arton",
    "19": "nitton",
    20: "tjugo",
    30: "trettio",
    40: "fyrtio",
    50: "femtio",
    60: "sextio",
    70: "sjuttio",
    80: "åttio",
    90: "nittio",
    100: "hundra",
}

translation_small_string_to_big = {
    "1": 10,
    "2": 20,
    "3": 30,
    "4": 40,
    "5": 50,
    "6": 60,
    "7": 70,
    "8": 80,
    "9": 90
}

def get_tenth(small_number_string: str):
    return translation_big[translation_small_string_to_big[small_number_string]]

def get_ton(big_number_string: str):
    return translation_big[big_number_string]


def translate_number(number: int):
    number_string = str(number)
    length = len(number_string)

    if length == 1:
        return translation_small[number_string]
    
    elif length == 2:
        new_string = ""
        if number_string[0] != "1" and number_string != "10":
            new_string = get_tenth(number_string[0])
        else:
            return new_string + get_ton(number_string)

        if number_string[1] != "0":
            new_string = new_string + translation_small[number_string[1]]

        return new_string
    elif length == 3:
        new_string = translation_small[number_string[0]] + "hundra"
        if number_string[1] != "0" and number_string[1] != "1":
            new_string = new_string + get_tenth(number_string[1])
        elif number_string[1] == "1":
            new_string = new_string + get_ton(number_string[-2:])
            return new_string

        if number_string[2] != "0":
            new_string = new_string + translation_small[number_string[2]]
        return new_string
    else:
        print("Length out of range")
        print("Number string:", str(number))
        print("Length:", length)
        return

if __name__ == "__main__":
    print(translate_number(114))
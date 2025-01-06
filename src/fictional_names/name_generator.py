from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname,
    generate_surname_less,
    styles
)
from . import arab, aztec, chinese, dragonborn, drow, dwarven, elven, english, giant, gnomish, halfling, japanese, mongolian, norsemen, orc, slavic, greek, steampunk, tolkien, viking, germanic, turkish, human, martin, jordan, erikson, roman, rowling, sapkowski


def generate_name(gender=choice(["female", "male"]), style=choice(styles), library=choice([True, False])):
    if type(gender) != str:
        raise TypeError("Invalid gender type.")
    if type(style) != str:
        raise TypeError("Invalid style type.")
    if type(library) != bool:
        raise TypeError("Invalid library type.")
    
    # Female names section
    if gender.lower() == "female":
        if style.lower() == "elven":
            name = choice(elven.female_names) if library else generate_female_name(elven.female_prefix, elven.female_suffix)
        elif style.lower() == "dragonborn":
            name = choice(dragonborn.female_names) if library else generate_female_name(dragonborn.female_prefix, dragonborn.female_suffix)
        elif style.lower() == "drow":
            name = choice(drow.female_names) if library else generate_female_name(drow.female_prefix, drow.female_suffix)
        elif style.lower() == "dwarven":
            name = choice(dwarven.female_names) if library else generate_female_name(dwarven.female_prefix, dwarven.female_suffix, min=1, max=2)
        elif style.lower() == "giant":
            name = choice(giant.female_names) if library else generate_female_name(giant.female_prefix, giant.female_suffix, min=0, max=1)
        elif style.lower() == "gnomish":
            name = choice(gnomish.female_names) if library else generate_female_name(gnomish.female_prefix, gnomish.female_suffix)
        elif style.lower() == "halfling":
            name = choice(halfling.female_names) if library else generate_female_name(halfling.female_prefix, halfling.female_suffix)
        elif style.lower() == "orc":
            name = choice(orc.female_names) if library else generate_female_name(orc.female_prefix, orc.female_suffix, min=0, max=1)
        elif style.lower() == "steampunk":
            name = choice(steampunk.female_names_lbr) if library else choice(steampunk.female_names)
        elif style.lower() == "human":
            name = choice(human.female_names)
        elif style.lower() == "english":
            name = choice(english.female_names_lbr) if library else choice(english.female_names)
        elif style.lower() == "greek":
            name = choice(greek.female_names) if library else generate_female_name(greek.female_prefix, greek.female_suffix)
        elif style.lower() == "norsemen":
            name = choice(norsemen.female_names) if library else generate_female_name(norsemen.female_prefix, norsemen.female_suffix, min=0, max=1)
        elif style.lower() == "arab":
            name = choice(arab.female_names) if library else generate_female_name(arab.female_prefix, arab.female_suffix, min=1, max=2)
        elif style.lower() == "japanese":
            name = choice(japanese.female_names) if library else generate_female_name(japanese.female_prefix, japanese.female_suffix)
        elif style.lower() == "viking":
            name = choice(viking.female_names) if library else generate_female_name(viking.female_prefix, viking.female_suffix)
        elif style.lower() == "germanic":
            name = choice(germanic.female_names) if library else generate_female_name(germanic.female_prefix, germanic.female_suffix)
        elif style.lower() == "turkish":
            name = choice(turkish.female_names) if library else generate_female_name(turkish.female_prefix, turkish.female_suffix)
        elif style.lower() == "chinese":
            name = choice(chinese.female_names) if library else generate_female_name(chinese.female_prefix, chinese.female_suffix)
        elif style.lower() == "mongolian":
            name = choice(mongolian.female_names) if library else generate_female_name(mongolian.female_prefix, mongolian.female_suffix)
        elif style.lower() == "slavic":
            name = choice(slavic.female_names) if library else generate_female_name(slavic.female_prefix, slavic.female_suffix)
        elif style.lower() == "aztec":
            name = choice(aztec.female_names) if library else generate_female_name(aztec.female_prefix, aztec.female_suffix)
        elif style.lower() == "roman":
            name = choice(roman.female_names) if library else generate_female_name(roman.female_prefix, roman.female_suffix)
        elif style.lower() == "tolkien":
            name = choice(tolkien.female_names) if library else generate_female_name(tolkien.female_prefix, tolkien.female_suffix, min=1, max=2)
        elif style.lower() == "martin":
            name = choice(martin.female_names) if library else generate_female_name(martin.female_prefix, martin.female_suffix, min=0, max=1)
        elif style.lower() == "jordan":
            name = choice(jordan.female_names) if library else generate_female_name(jordan.female_prefix, jordan.female_suffix, min=0, max=2)
        elif style.lower() == "erikson":
            name = choice(erikson.female_names) if library else generate_female_name(erikson.female_prefix, jordan.female_suffix, min=0, max=2)
        elif style.lower() == "rowling":
            name = choice(rowling.female_names) if library else generate_female_name(rowling.female_prefix, rowling.female_suffix)
        elif style.lower() == "sapkowski":
            name = choice(sapkowski.female_names) if library else generate_female_name(sapkowski.female_prefix, sapkowski.female_suffix)

    # Male names section
    elif gender.lower() == "male":
        if style.lower() == "elven":
            name = choice(elven.male_names) if library else generate_male_name(elven.male_prefix, elven.male_suffix)
        elif style.lower() == "dragonborn":
            name = choice(dragonborn.male_names) if library else generate_male_name(dragonborn.male_prefix, dragonborn.male_suffix)
        elif style.lower() == "drow":
            name = choice(drow.male_names) if library else generate_male_name(drow.male_prefix, drow.male_suffix)
        elif style.lower() == "dwarven":
            name = choice(dwarven.male_names) if library else generate_male_name(dwarven.male_prefix, dwarven.male_suffix)
        elif style.lower() == "gnomish":
            name = choice(gnomish.male_names) if library else generate_male_name(gnomish.male_prefix, gnomish.male_suffix)
        elif style.lower() == "giant":
            name = choice(giant.male_names) if library else generate_male_name(giant.male_prefix, giant.male_suffix, min=0, max=1)
        elif style.lower() == "halfling":
            name = choice(halfling.male_names) if library else generate_male_name(halfling.male_prefix, halfling.male_suffix)
        elif style.lower() == "orc":
            name = choice(orc.male_names) if library else generate_male_name(orc.male_prefix, orc.male_suffix, min=0, max=1)
        elif style.lower() == "steampunk":
            name = choice(steampunk.male_names_lbr) if library else choice(steampunk.male_names)
        elif style.lower() == "human":
            name = choice(human.male_names)
        elif style.lower() == "english":
            name = choice(english.male_names_lbr) if library else choice(english.male_names)
        elif style.lower() == "greek":
            name = choice(greek.male_names) if library else generate_male_name(greek.male_prefix, greek.male_suffix)
        elif style.lower() == "norsemen":
            name = choice(norsemen.male_names) if library else generate_male_name(norsemen.male_prefix, norsemen.male_suffix, min=0, max=1)
        elif style.lower() == "arab":
            name = choice(arab.male_names) if library else generate_male_name(arab.male_prefix, arab.male_suffix, min=1, max=2)
        elif style.lower() == "japanese":
            name = choice(japanese.male_names) if library else generate_male_name(japanese.male_prefix, japanese.male_suffix)
        elif style.lower() == "viking":
            name = choice(viking.male_names) if library else generate_male_name(viking.male_prefix, viking.male_suffix)
        elif style.lower() == "germanic":
            name = choice(germanic.male_names) if library else generate_male_name(germanic.male_prefix, germanic.male_suffix)
        elif style.lower() == "turkish":
            name = choice(turkish.male_names) if library else generate_male_name(turkish.male_prefix, turkish.male_suffix)
        elif style.lower() == "chinese":
            name = choice(chinese.male_names) if library else generate_male_name(chinese.male_prefix, chinese.male_suffix)
        elif style.lower() == "mongolian":
            name = choice(mongolian.male_names) if library else generate_male_name(mongolian.male_prefix, mongolian.male_suffix)
        elif style.lower() == "slavic":
            name = choice(slavic.male_names) if library else generate_male_name(slavic.male_prefix, slavic.male_suffix)
        elif style.lower() == "aztec":
            name = choice(aztec.male_names) if library else generate_male_name(aztec.male_prefix, aztec.male_suffix)
        elif style.lower() == "roman":
            name = choice(roman.male_names) if library else generate_male_name(roman.male_prefix, roman.male_suffix)
        elif style.lower() == "tolkien":
            name = choice(tolkien.male_names) if library else generate_male_name(tolkien.male_prefix, tolkien.male_suffix, min=1, max=2)
        elif style.lower() == "martin":
            name = choice(martin.male_names) if library else generate_male_name(martin.male_prefix, martin.male_suffix, min=0, max=1)
        elif style.lower() == "jordan":
            name = choice(jordan.male_names) if library else generate_male_name(jordan.male_prefix, jordan.male_suffix, min=0, max=2)
        elif style.lower() == "erikson":
            name = choice(erikson.male_names) if library else generate_male_name(erikson.male_prefix, erikson.male_suffix, min=0, max=2)
        elif style.lower() == "rowling":
            name = choice(rowling.male_names) if library else generate_male_name(rowling.male_prefix, rowling.male_suffix)
        elif style.lower() == "sapkowski":
            name = choice(sapkowski.male_names) if library else generate_male_name(sapkowski.male_prefix, sapkowski.male_suffix)
    else:
        raise ValueError("Invalid gender specified. Please choose 'male' or 'female'.")

    # Surnames section
    if style.lower() == "elven":
        surname = choice(elven.surnames) if library else generate_surname(elven.surname_syllables)
    elif style.lower() == "dragonborn":
        surname = choice(dragonborn.surnames) if library else generate_surname_less(dragonborn.surname_prefix, dragonborn.surname_suffix)
    elif style.lower() == "drow":
        surname = choice(drow.surnames) if library else generate_surname(drow.surname_syllables)
    elif style.lower() == "dwarven":
        surname = choice(dwarven.surnames) if library else generate_surname(dwarven.surname_syllables, min=1, max=3)
    elif style.lower() == "giant":
        surname = choice(giant.surnames) if library else generate_surname_less(giant.surname_prefix, giant.surname_suffix)
    elif style.lower() == "gnomish":
        surname = choice(gnomish.surnames) if library else generate_surname_less(gnomish.surname_prefix, gnomish.surname_suffix)
    elif style.lower() == "halfling":
        surname = choice(halfling.surnames) if library else generate_surname_less(halfling.surname_prefix, halfling.surname_suffix)
    elif style.lower() == "orc":
        surname = choice(orc.surnames) if library else choice(orc.titles)
    elif style.lower() == "steampunk":
        surname = choice(steampunk.surnames_lbr) if library else choice(steampunk.surnames)
    elif style.lower() == "human":
        surname = choice(human.surnames) if library else generate_surname_less(human.surname_prefix, human.surname_suffix)
    elif style.lower() == "english":
        surname = choice(english.surnames_lbr) if library else choice(english.surnames)
    elif style.lower() == "greek":
        surname = choice(greek.surnames) if library else generate_surname_less(greek.surname_prefix, greek.surname_suffix)
    elif style.lower() == "norsemen":
        surname = choice(norsemen.surnames) if library else generate_surname_less(norsemen.surname_prefix, norsemen.surname_suffix)
    elif style.lower() == "arab":
        surname = choice(arab.surnames) if library else generate_surname_less(arab.surname_prefix, arab.surname_suffix)
    elif style.lower() == "japanese":
        surname = choice(japanese.surnames) if library else generate_surname_less(japanese.surname_prefix, japanese.surname_suffix)
    elif style.lower() == "viking":
        surname = (choice(viking.female_surnames) if gender == "female" else choice(viking.male_surnames)) if library else generate_surname_less(viking.surname_prefix, viking.surname_suffix)
    elif style.lower() == "germanic":
        surname = choice(germanic.surnames) if library else generate_surname_less(germanic.surname_prefix, germanic.surname_suffix)
    elif style.lower() == "turkish":
        surname = choice(turkish.surnames) if library else generate_surname_less(turkish.surname_prefix, turkish.surname_suffix)
    elif style.lower() == "chinese":
        surname = choice(chinese.surnames) if library else generate_surname_less(chinese.surname_prefix, chinese.surname_suffix)
    elif style.lower() == "mongolian":
        surname = choice(mongolian.surnames) if library else generate_surname_less(mongolian.surname_prefix, mongolian.surname_suffix)
    elif style.lower() == "slavic":
        surname = choice(slavic.surnames) if library else generate_surname_less(slavic.surname_prefix, slavic.surname_suffix)
    elif style.lower() == "aztec":
        surname = choice(aztec.surnames) if library else generate_surname_less(aztec.surname_prefix, aztec.surname_suffix)
    elif style.lower() == "roman":
        surname = choice(roman.surnames) if library else generate_surname_less(roman.surname_prefix, roman.surname_suffix)
    elif style.lower() == "tolkien":
        surname = choice(tolkien.surnames) if library else generate_surname_less(tolkien.surname_prefix, tolkien.surname_suffix)
    elif style.lower() == "martin":
        surname = choice(martin.surnames) if library else generate_surname_less(martin.surname_prefix, martin.surname_suffix)
    elif style.lower() == "jordan":
        surname = choice(jordan.surnames) if library else generate_surname_less(jordan.surname_prefix, jordan.surname_suffix)
    elif style.lower() == "erikson":
        surname = choice(erikson.surnames) if library else generate_surname(erikson.surname_syllables)
    elif style.lower() == "rowling":
        surname = choice(rowling.surnames)
    elif style.lower() == "sapkowski":
        surname = choice(sapkowski.surnames) if library else generate_surname_less(sapkowski.surname_prefix, sapkowski.surname_suffix)
    else:
        raise ValueError(
            "Invalid style specified. Please choose a valid style between 'elven', 'dwarven', 'giant', 'halfling', 'orc', 'steampunk', 'human', 'english', 'greek', 'norsemen', 'arab', 'japanese', 'viking', 'germanic', 'turkish', 'chinese', 'mongolian', 'slavic', 'aztec', 'roman', 'tolkien', 'martin', 'jordan', 'erikson', 'rowling', or 'sapkowski'."
        )

    return f"{name} {surname}"

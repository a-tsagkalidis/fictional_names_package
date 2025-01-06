from random import choice, randint


def generate_female_name(female_prefix, female_suffix, min=1, max=1):
    while True:
        try:
            num_prefix_syllables = randint(min, max)
            num_suffix_syllables = randint(min, max)
            if num_prefix_syllables == 0 and num_suffix_syllables == 0:
                raise ValueError

            if num_prefix_syllables == 1 and num_suffix_syllables == 0:
                name = choice(female_prefix)
                return name.capitalize()

            name = ""
            for _ in range(num_prefix_syllables):
                syllable = choice(female_prefix)
                name += syllable

            for _ in range(num_suffix_syllables):
                syllable = choice(female_suffix)
                name += syllable

            return name.capitalize()
        except ValueError:
            continue


def generate_male_name(male_prefix, male_suffix, min=1, max=1):
    while True:
        try:
            num_prefix_syllables = randint(min, max)
            num_suffix_syllables = randint(min, max)
            if num_prefix_syllables == 0 and num_suffix_syllables == 0:
                raise ValueError

            if num_prefix_syllables == 1 and num_suffix_syllables == 0:
                name = choice(male_prefix)
                return name.capitalize()

            name = ""
            for _ in range(num_prefix_syllables):
                syllable = choice(male_prefix)
                name += syllable

            for _ in range(num_suffix_syllables):
                syllable = choice(male_suffix)
                name += syllable

            return name.capitalize()
        except ValueError:
            continue


def generate_surname(surname_syllables, min=2, max=3):
    num_syllables = randint(min, max)
    synth_surname = ""
    for _ in range(num_syllables):
        syllable = choice(surname_syllables)
        synth_surname += syllable

    return synth_surname.capitalize()


def generate_surname_less(surname_prefix, surname_suffix):
    synth_surname = ""
    syllable_prefix = choice(surname_prefix)
    syllable_suffix = choice(surname_suffix)
    synth_surname += syllable_prefix + syllable_suffix

    return synth_surname.capitalize()


def remove_duplicates(namelist):
    # Remove duplicates
    namelist_ordered = list(set(namelist))

    # Sort alphabetically
    namelist_ordered.sort()

    return namelist_ordered


styles = [
    'arab',
    'aztec',
    'chinese',
    'dragonborn',
    'drow',
    'dwarven',
    'elven',
    'english',
    'giant',
    'gnomish',
    'halfling',
    'japanese',
    'mongolian',
    'norsemen',
    'orc',
    'slavic',
    'greek',
    'steampunk',
    'tolkien',
    'viking',
    'germanic',
    'turkish',
    'human',
    'martin',
    'jordan',
    'erikson',
    'roman',
    'rowling',
    'sapkowski'
    ]

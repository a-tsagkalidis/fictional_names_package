from . import arab, aztec, chinese, dwarven, elven, english, giant, halfling, japanese, mongolian, norsemen, orc, slavic, greek, steampunk, tolkien, viking, germanic, turkish, human, martin, jordan, erikson, roman, rowling, sapkowski
from random import choice

def generate_name(gender=choice(["female", "male"]), style="human", library=True):
    if type(gender) != str:
        raise TypeError("Invalid gender type.")
    if type(style) != str:
        raise TypeError("Invalid style type.")
    if type(library) != bool:
        raise TypeError("Invalid library type.")
    if gender.lower() == "female":
        match style:
            case "elven":
                name = elven.female if library is False else elven.female_lbr
            case "dwarven":
                name = dwarven.female if library is False else dwarven.female_lbr
            case "giant":
                name = giant.female if library is True else giant.female_lbr
            case "halfling":
                name = halfling.female if library is False else halfling.female_lbr
            case "orc":
                name = orc.female if library is False else orc.female_lbr
            case "steampunk":
                name = steampunk.female if library is False else steampunk.female_lbr
            case "human":
                name = human.female
            case "english":
                name = english.female if library is False else english.female_lbr
            case "greek":
                name = greek.female if library is False else greek.female_lbr
            case "norsemen":
                name = norsemen.female if library is False else norsemen.female_lbr
            case "arab":
                name = arab.female if library is False else arab.female_lbr
            case "japanese":
                name = japanese.female if library is False else japanese.female_lbr
            case "viking":
                name = viking.female if library is False else viking.female_lbr
            case "germanic":
                name = germanic.female if library is False else germanic.female_lbr
            case "turkish":
                name = turkish.female if library is False else turkish.female_lbr
            case "chinese":
                name = chinese.female if library is False else chinese.female_lbr
            case "mongolian":
                name = mongolian.female if library is False else mongolian.female_lbr
            case "slavic":
                name = slavic.female if library is False else slavic.female_lbr
            case "aztec":
                name = aztec.female if library is False else aztec.female_lbr
            case "roman":
                name = roman.female if library is False else roman.female_lbr
            case "tolkien":
                name = tolkien.female if library is False else tolkien.female_lbr
            case "martin":
                name = martin.female if library is False else martin.female_lbr
            case "jordan":
                name = jordan.female if library is False else jordan.female_lbr
            case "erikson":
                name = erikson.female if library is False else erikson.female_lbr
            case "rowling":
                name = rowling.female if library is False else rowling.female_lbr
            case "sapkowski":
                name = sapkowski.female if library is False else sapkowski.female_lbr
    elif gender.lower() == "male":
        match style:
            case "elven":
                name = elven.male if library is False else elven.male_lbr
            case "dwarven":
                name = dwarven.male if library is False else dwarven.male_lbr
            case "giant":
                name = giant.male if library is True else giant.male_lbr
            case "halfling":
                name = halfling.male if library is False else halfling.male_lbr
            case "orc":
                name = orc.male if library is False else orc.male_lbr
            case "steampunk":
                name = steampunk.male if library is False else steampunk.male_lbr
            case "human":
                name = human.male
            case "english":
                name = english.male if library is False else english.male_lbr
            case "greek":
                name = greek.male if library is False else greek.male_lbr
            case "norsemen":
                name = norsemen.male if library is False else norsemen.male_lbr
            case "arab":
                name = arab.male if library is False else arab.male_lbr
            case "japanese":
                name = japanese.male if library is False else japanese.male_lbr
            case "viking":
                name = viking.male if library is False else viking.male_lbr
            case "germanic":
                name = germanic.male if library is False else germanic.male_lbr
            case "turkish":
                name = turkish.male if library is False else turkish.male_lbr
            case "chinese":
                name = chinese.male if library is False else chinese.male_lbr
            case "mongolian":
                name = mongolian.male if library is False else mongolian.male_lbr
            case "slavic":
                name = slavic.male if library is False else slavic.male_lbr
            case "aztec":
                name = aztec.male if library is False else aztec.male_lbr
            case "roman":
                name = roman.male if library is False else roman.male_lbr
            case "tolkien":
                name = tolkien.male if library is False else tolkien.male_lbr
            case "martin":
                name = martin.male if library is False else martin.male_lbr
            case "jordan":
                name = jordan.male if library is False else jordan.male_lbr
            case "erikson":
                name = erikson.male if library is False else erikson.male_lbr
            case "rowling":
                name = rowling.male if library is False else rowling.male_lbr
            case "sapkowski":
                name = sapkowski.male if library is False else sapkowski.male_lbr
    else:
        raise ValueError("Invalid gender specified. Please choose 'male' or 'female'.")

    if style.lower() == "elven":
        surname = elven.surname if library is False else elven.surname_lbr
    elif style.lower() == "dwarven":
        surname = dwarven.surname if library is False else dwarven.surname_lbr
    elif style.lower() == "giant":
        surname = giant.surname if library is True else giant.surname_lbr
    elif style.lower() == "halfling":
        surname = halfling.surname if library is False else halfling.surname_lbr
    elif style.lower() == "orc":
        surname = orc.surname if library is False else orc.surname_lbr
    elif style.lower() == "steampunk":
        surname = steampunk.surname if library is False else steampunk.surname_lbr
    elif style.lower() == "human":
        surname = human.surname if library is False else human.surname_lbr
    elif style.lower() == "english":
        surname = english.surname if library is False else english.surname_lbr
    elif style.lower() == "greek":
        surname = greek.surname if library is False else greek.surname_lbr
    elif style.lower() == "norsemen":
        surname = norsemen.surname if library is False else norsemen.surname_lbr
    elif style.lower() == "arab":
        surname = arab.surname if library is False else arab.surname_lbr
    elif style.lower() == "japanese":
        surname = japanese.surname if library is False else japanese.surname_lbr
    elif style.lower() == "viking":
        surname = (
            viking.surname
            if library is False
            else (
                viking.female_surname_lbr
                if gender == "female"
                else viking.male_surname_lbr
            )
        )
    elif style.lower() == "germanic":
        surname = germanic.surname if library is False else germanic.surname_lbr
    elif style.lower() == "turkish":
        surname = turkish.surname if library is False else turkish.surname_lbr
    elif style.lower() == "chinese":
        surname = chinese.surname if library is False else chinese.surname_lbr
    elif style.lower() == "mongolian":
        surname = mongolian.surname if library is False else mongolian.surname_lbr
    elif style.lower() == "slavic":
        surname = slavic.surname if library is False else slavic.surname_lbr
    elif style.lower() == "aztec":
        surname = aztec.surname if library is False else aztec.surname_lbr
    elif style.lower() == "roman":
        surname = roman.surname if library is False else roman.surname_lbr
    elif style.lower() == "tolkien":
        surname = tolkien.surname if library is False else tolkien.surname_lbr
    elif style.lower() == "martin":
        surname = martin.surname if library is False else martin.surname_lbr
    elif style.lower() == "jordan":
        surname = jordan.surname if library is False else jordan.surname_lbr
    elif style.lower() == "erikson":
        surname = erikson.surname if library is False else erikson.surname_lbr
    elif style.lower() == "rowling":
        surname = rowling.surname
    elif style.lower() == "sapkowski":
        surname = sapkowski.surname if library is False else sapkowski.surname_lbr
    else:
        raise ValueError(
            "Invalid style specified. Please choose a valid style between 'elven', 'dwarven', 'giant', 'halfling', 'orc', 'steampunk', 'human', 'english', 'greek', 'norsemen', 'arab', 'japanese', 'viking', 'germanic', 'turkish', 'chinese', 'mongolian', 'slavic', 'aztec', 'roman', 'tolkien', 'martin', 'jordan', 'erikson', 'rowling', or 'sapkowski'."
        )

    return f"{name} {surname}"


if __name__ == "__main__":
    name = generate_name()
    print(name)

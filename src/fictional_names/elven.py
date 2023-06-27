from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname,
    remove_duplicates,
)


female_prefix = [
    "ael",
    "al",
    "an",
    "ar",
    "cal",
    "dael",
    "el",
    "er",
    "fae",
    "fal",
    "fi",
    "gal",
    "gil",
    "glor",
    "hal",
    "ia",
    "id",
    "il",
    "im",
    "in",
    "laer",
    "lan",
    "leg",
    "li",
    "lind",
    "lith",
    "lor",
    "mae",
    "mel",
    "na",
    "nar",
    "nen",
    "ner",
    "or",
    "pe",
    "ran",
    "rhov",
    "sae",
    "saer",
    "se",
    "sil",
    "ta",
    "thal",
    "thar",
    "thing",
    "ti",
    "tir",
    "val",
    "ví",
    "yar",
    "zeph",
    "zim",
]

female_suffix = [
    "á",
    "ë",
    "í",
    "ír",
    "ís",
    "ith",
    "lá",
    "lé",
    "liël",
    "lís",
    "lith",
    "lyn",
    "má",
    "më",
    "mí",
    "ná",
    "në",
    "niël",
    "nis",
    "nith",
    "nyá",
    "rá",
    "ré",
    "riël",
    "ris",
    "rith",
    "ryá",
    "sä",
    "së",
    "siél",
    "sis",
    "sith",
    "stá",
    "thél",
    "theá",
    "thée",
    "thiël",
    "this",
    "thith",
    "vyl",
    "wén",
    "wiel",
    "wis",
    "withë",
    "yá",
    "yë",
    "yra",
    "ysë",
]

male_prefix = [
    "aeg",
    "aer",
    "am",
    "an",
    "ar",
    "bar",
    "ber",
    "cal",
    "cel",
    "cor",
    "dan",
    "dar",
    "den",
    "dor",
    "el",
    "em",
    "en",
    "er",
    "fal",
    "fer",
    "gal",
    "gar",
    "gil",
    "glor",
    "hal",
    "har",
    "hel",
    "her",
    "iath",
    "im",
    "in",
    "ir",
    "lam",
    "lar",
    "len",
    "lin",
    "lor",
    "mel",
    "men",
    "mir",
    "nem",
    "ner",
    "nim",
    "nor",
    "ol",
    "or",
    "rad",
    "ral",
    "ran",
    "rel",
    "rim",
    "ron",
    "sam",
    "san",
    "ser",
    "sil",
    "sin",
    "sor",
    "tan",
    "tar",
    "tel",
    "thor",
    "tom",
    "tor",
    "ul",
    "ur",
    "val",
    "var",
    "vén",
    "ver",
    "wil",
    "win",
    "wis",
    "yam",
    "yar",
    "ÿer",
    "yin",
    "yol",
]

male_suffix = [
    "ad",
    "aél",
    "an",
    "and",
    "ar",
    "ard",
    "as",
    "ath",
    "énd",
    "ër",
    "ern",
    "eth",
    "il",
    "in",
    "ind",
    "ion",
    "ir",
    "is",
    "ith",
    "lad",
    "läs",
    "lin",
    "lo",
    "lon",
    "or",
    "orn",
    "os",
    "rad",
    "rän",
    "ras",
    "rath",
    "rin",
    "ron",
    "ros",
    "rth",
    "th",
    "thir",
    "thor",
    "únd",
    "úr",
    "us",
    "win",
    "ynd",
    "yon",
    "ÿth",
]

surname_syllables = [
    "ael",
    "al",
    "an",
    "ar",
    "cal",
    "dael",
    "ël",
    "er",
    "fae",
    "fal",
    "fi",
    "gal",
    "gil",
    "glor",
    "hal",
    "ia",
    "id",
    "il",
    "im",
    "in",
    "laér",
    "lan",
    "leg",
    "li",
    "lind",
    "lith",
    "lor",
    "mae",
    "mel",
    "ne",
    "ner",
    "nén",
    "ner",
    "or",
    "pe",
    "ran",
    "rhöv",
    "sae",
    "sae",
    "se",
    "sil",
    "ta",
    "thal",
    "thar",
    "thing",
    "ti",
    "tir",
    "val",
    "vi",
    "yar",
    "zah",
    "zim",
]

female_names = [
    "Aerandir",
    "Aeranduil",
    "Aerandur",
    "Aerandë",
    "Aerendil",
    "Alcanna",
    "Almena",
    "Amarthiel",
    "Anaria",
    "Anorwen",
    "Aranel",
    "Arasinya",
    "Arianeth",
    "Arieneth",
    "Arieth",
    "Arilwen",
    "Arwenia",
    "Avelera",
    "Avendil",
    "Calanthe",
    "Calathiel",
    "Celebeth",
    "Celestria",
    "Cirael",
    "Ciriana",
    "Danathiel",
    "Danoviel",
    "Darien",
    "Dawnstar",
    "Elariel",
    "Elathir",
    "Elenwë",
    "Elindra",
    "Elionor",
    "Elissia",
    "Elora",
    "Elowen",
    "Elthiriel",
    "Elwing",
    "Emerwen",
    "Endellion",
    "Eolande",
    "Erandis",
    "Erendis",
    "Erlindë",
    "Ermalinde",
    "Esteldín",
    "Estrith",
    "Evangeline",
    "Evanya",
    "Faelwen",
    "Faerindel",
    "Fairwen",
    "Firiel",
    "Galadhrim",
    "Galadriel",
    "Galadwen",
    "Galanwë",
    "Galdrielle",
    "Galdwen",
    "Gariel",
    "Gedriel",
    "Gilmith",
    "Glorfindel",
    "Gwindor",
    "Halethriel",
    "Helengil",
    "Hithlindë",
    "Hithrael",
    "Idril",
    "Idrilas",
    "Ithildin",
    "Ithilwen",
    "Ivriniel",
    "Lalwendë",
    "Lhûthien",
    "Liriel",
    "Lómelindi",
    "Maeglin",
    "Maelwë",
    "Maiarwen",
    "Maiel",
    "Melian",
    "Meril",
    "Merilwen",
    "Morwen",
    "Máeldir",
    "Mírwen",
    "Narwindë",
    "Nellas",
    "Nenloth",
    "Nimrodel",
    "Nirneth",
    "Noralindë",
    "Nólemië",
    "Orodreth",
    "Perelin",
    "Píriel",
    "Ravendis",
    "Rhawiel",
    "Rinniell",
    "Roselindë",
    "Ríëndel",
    "Saeldil",
    "Saelindë",
    "Saeros",
    "Salandria",
    "Sarethiel",
    "Sauriel",
    "Selenia",
    "Sereneth",
    "Shalindra",
    "Silmarwen",
    "Sírdathiel",
    "Sírindë",
    "Sírwen",
    "Talindra",
    "Thalion",
    "Tinúviel",
    "Undómë",
    "Valandil",
    "Vanië",
    "Vanwë",
    "Vanyarin",
    "Yavanna",
    "Yavannamírë",
    "Yavannië",
    "Yúvathië",
    "Zíriath",
]

male_names = [
    "Aegnor",
    "Aeran",
    "Aerandir",
    "Alarion",
    "Aldaron",
    "Almarion",
    "Amalion",
    "Amarael",
    "Amathar",
    "Amlach",
    "Anarion",
    "Anduil",
    "Angrod",
    "Anorion",
    "Aradhel",
    "Arador",
    "Aragorn",
    "Aranarth",
    "Arandur",
    "Aranion",
    "Arathorn",
    "Aravel",
    "Aravir",
    "Aredhel",
    "Argon",
    "Arveleg",
    "Arwen",
    "Asfaloth",
    "Asgaloth",
    "Aulendil",
    "Azaghal",
    "Balion",
    "Baragund",
    "Barahir",
    "Bard",
    "Belegon",
    "Belegorn",
    "Beren",
    "Boromir",
    "Bregolas",
    "Caladon",
    "Calenon",
    "Calion",
    "Celebrimbor",
    "Celedorn",
    "Cirdan",
    "Cirelind",
    "Curufin",
    "Daelion",
    "Daeron",
    "Darian",
    "Dior",
    "Dorion",
    "Duilin",
    "Earendur",
    "Ecthelion",
    "Egalmoth",
    "Eladion",
    "Eldacar",
    "Eldamir",
    "Eldaron",
    "Eledhel",
    "Elendil",
    "Elendor",
    "Elendur",
    "Elenion",
    "Elgalad",
    "Elithil",
    "Elladan",
    "Elorand",
    "Elorian",
    "Elrindel",
    "Elrion",
    "Elrond",
    "Elros",
    "Eol",
    "Eonwe",
    "Eorl",
    "Erestel",
    "Erestor",
    "Erkenbrand",
    "Eruhantalë",
    "Eärendil",
    "Faelindir",
    "Faelion",
    "Faladon",
    "Falmir",
    "Faramir",
    "Felagund",
    "Finarfin",
    "Finarion",
    "Findegil",
    "Finduilas",
    "Fingolfin",
    "Fingon",
    "Finrod",
    "Galadhel",
    "Galadriel",
    "Galandir",
    "Galdor",
    "Galion",
    "Gil-galad",
    "Gildor",
    "Gilion",
    "Gimli",
    "Glorandir",
    "Glorfindel",
    "Gwindor",
    "Haldir",
    "Haldirion",
    "Haldon",
    "Halfling",
    "Hallas",
    "Halmir",
    "Hathaldir",
    "Helm",
    "Huan",
    "Húrin",
    "Idril",
    "Imrahil",
    "Indor",
    "Ingwë",
    "Irime",
    "Isildur",
    "Ithilion",
    "Laerion",
    "Landion",
    "Legolas",
    "Lendor",
    "Lirandil",
    "Mablung",
    "Maedhros",
    "Maeglin",
    "Maegon",
    "Maelon",
    "Maendir",
    "Manwë",
    "Melian",
    "Mithrandir",
    "Mîm",
    "Narion",
    "Neldor",
    "Nimloth",
    "Olorin",
    "Olwë",
    "Orandil",
    "Orc",
    "Oromë",
    "Pippin",
    "Radagast",
    "Ralion",
    "Rindon",
    "Saelion",
    "Saeros",
    "Samwise",
    "Saruman",
    "Seldor",
    "Shadowfax",
    "Silindor",
    "Smaug",
    "Taeros",
    "Talandor",
    "Taurion",
    "Thalion",
    "Thalos",
    "Thandir",
    "Thingol",
    "Thorin",
    "Thranduil",
    "Théoden",
    "Tinor",
    "Tinúviel",
    "Tirion",
    "Tuor",
    "Turgon",
    "Ungoliant",
    "Valandil",
    "Valandur",
    "Valarion",
    "Vanyar",
    "Varandil",
    "Varda",
    "Varion",
    "Varyon",
    "Vingil",
    "Voronwe",
    "Voronwë",
    "Yavanna",
]

surnames = [
    "Acalor",
    "Acarnor",
    "Aelindë",
    "Aerendil",
    "Alaraith",
    "Aldorin",
    "Amastë",
    "Anarion",
    "Angolë",
    "Aralion",
    "Arandor",
    "Arathir",
    "Ardalas",
    "Ardilas",
    "Ariandel",
    "Arnoron",
    "Ascarion",
    "Astaldor",
    "Astoron",
    "Belarion",
    "Belarond",
    "Boromir",
    "Borondir",
    "Brenornë",
    "Caerin",
    "Caerion",
    "Caladrel",
    "Calandil",
    "Calithil",
    "Carnadon",
    "Carnador",
    "Celador",
    "Celeborn",
    "Cirdanion",
    "Cirdanor",
    "Cirya",
    "Cúaladir",
    "Cúaldor",
    "Cúrion",
    "Dírhael",
    "Dúrinnë",
    "Eldaron",
    "Elendor",
    "Elessindë",
    "Elgalad",
    "Elgarion",
    "Elnaril",
    "Elnarion",
    "Elorwen",
    "Enethril",
    "Enthil",
    "Enyandil",
    "Faelith",
    "Faenor",
    "Falathan",
    "Faldorin",
    "Falrindil",
    "Finraen",
    "Finroth",
    "Galathil",
    "Galathor",
    "Galdorin",
    "Galdorion",
    "Galithor",
    "Glarion",
    "Glorinor",
    "Haladan",
    "Haladir",
    "Halindir",
    "Hanarë",
    "Hathalon",
    "Hatharion",
    "Hilindë",
    "Idhrendil",
    "Idhrendor",
    "Idhrinor",
    "Ildirion",
    "Ildorion",
    "Ilendil",
    "Imrahil",
    "Imrathor",
    "Inglorion",
    "Innarë",
    "Lindalas",
    "Lindor",
    "Lindorin",
    "Lithariel",
    "Lithilas",
    "Lithilorn",
    "Lorfindel",
    "Lorien",
    "Lorindil",
    "Maegdor",
    "Maegdorin",
    "Maeglin",
    "Melorian",
    "Melorion",
    "Melrondë",
    "Narothir",
    "Narothor",
    "Narwindë",
    "Nimloth",
    "Nimrion",
    "Nimrith",
    "Noraelin",
    "Nórin",
    "Nórion",
    "Orandil",
    "Orandor",
    "Orinor",
    "Peralin",
    "Peregrin",
    "Ranthalas",
    "Rhovandir",
    "Rhovendor",
    "Rhovendur",
    "Rivendal",
    "Saerindë",
    "Saeros",
    "Saldaron",
    "Saldorion",
    "Silgadil",
    "Silgarion",
    "Silrion",
    "Talathor",
    "Talathorin",
    "Talindra",
    "Thalassë",
    "Thandor",
    "Thandorin",
    "Tharrë",
    "Thingolion",
    "Thorondil",
    "Tirithorn",
    "Valandor",
    "Valandorin",
    "Valendil",
    "Virendor",
    "Virendorin",
    "Vírelindë",
    "Yaralan",
    "Yaralon",
    "Yarenthir",
    "Zephiron",
    "Zephiroth",
    "Zephyrnir",
    "Zimranor",
    "Zimrathil",
    "Zimrathor",
]

female = generate_female_name(female_prefix, female_suffix, min=1, max=1)
male = generate_male_name(male_prefix, male_suffix, min=1, max=1)
surname = generate_surname(surname_syllables, min=2, max=3)

female_lbr = choice(female_names)
male_lbr = choice(male_names)
surname_lbr = choice(surnames)

# print(remove_duplicates(female_names, male_names, surnames))

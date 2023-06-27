from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname_less,
    remove_duplicates,
)


female_prefix = [
    "cer",
    "cy",
    "dan",
    "el",
    "es",
    "fi",
    "gwen",
    "is",
    "jil",
    "ka",
    "la",
    "me",
    "nes",
    "phi",
    "que",
    "ri",
    "sha",
    "tri",
    "va",
    "wen",
    "xi",
    "ya",
    "zel",
]


female_suffix = [
    "a",
    "anna",
    "ara",
    "delle",
    "ena",
    "eth",
    "felle",
    "ia",
    "in",
    "is",
    "la",
    "mina",
    "na",
    "nara",
    "ne",
    "neth",
    "ra",
    "re",
    "ri",
    "selle",
    "sha",
    "thel",
    "tri",
    "va",
    "vera",
    "wyn",
    "ya",
    "zara",
]

male_prefix = [
    "al",
    "ar",
    "ber",
    "cor",
    "dan",
    "ed",
    "fer",
    "gar",
    "hal",
    "ian",
    "jar",
    "kar",
    "luc",
    "mar",
    "nor",
    "or",
    "per",
    "quil",
    "rad",
    "ser",
    "ter",
    "ul",
    "val",
    "wal",
    "xan",
    "yar",
    "zan",
]

male_suffix = [
    "an",
    "ard",
    "en",
    "er",
    "ian",
    "ion",
    "is",
    "ix",
    "le",
    "lin",
    "mir",
    "on",
    "or",
    "rick",
    "ton",
    "us",
    "ven",
    "ver",
    "wick",
    "win",
    "xander",
    "yen",
    "yson",
    "zeb",
    "zen",
]


surname_prefix = [
    "ber",
    "car",
    "dor",
    "ev",
    "fal",
    "ger",
    "han",
    "iar",
    "jor",
    "kal",
    "lin",
    "mor",
    "nar",
    "oer",
    "per",
    "qar",
    "ran",
    "sar",
    "tor",
    "ud",
    "var",
    "wer",
    "xan",
    "yor",
    "zar",
]

surname_suffix = [
    "dith",
    "elle",
    "fain",
    "gwen",
    "hild",
    "is",
    "jenn",
    "kath",
    "lith",
    "min",
    "na",
    "orin",
    "phine",
    "quil",
    "rin",
    "sael",
    "thel",
    "uin",
    "veth",
    "wyn",
    "xel",
    "yra",
    "zire",
]

female_names = [
    "Aelirenn",
    "Aguara",
    "Anezka",
    "Anna Henrietta",
    "Anselma",
    "Ariadna",
    "Bianka",
    "Bryonia",
    "Calyce",
    "Cedilla",
    "Cerys",
    "Cirilla",
    "Coral",
    "Dana",
    "Danica",
    "Delanira",
    "Dorregaray",
    "Draug",
    "Duny",
    "Eist",
    "Eleanora",
    "Eleonore",
    "Emhyr",
    "Essi",
    "Falwick",
    "Fiona",
    "Francesca",
    "Freya",
    "Gaga",
    "Geralt",
    "Giselher",
    "Gretka",
    "Guarma",
    "Gyldayn",
    "Hedvig",
    "Helma",
    "Ildiko",
    "Ines",
    "Iola",
    "Iorveth",
    "Isabetta",
    "Ismene",
    "Itlina",
    "Jacques",
    "Jana",
    "Johanna",
    "Jutta",
    "Kalina",
    "Keira",
    "Kenna",
    "Kikimore",
    "Kira",
    "Koshchey",
    "Kovir",
    "Leticia",
    "Lilith",
    "Linda",
    "Lola",
    "Lydia",
    "Magda",
    "Margot",
    "Martyna",
    "Meve",
    "Milva",
    "Molly",
    "Moril",
    "Mousesack",
    "Myrtle",
    "Nenneke",
    "Nivellen",
    "Oxenfurt",
    "Pavetta",
    "Philippa",
    "Polly",
    "Priscilla",
    "Ragnhild",
    "Renfri",
    "Rhiannon",
    "Rita",
    "Roach",
    "Saskia",
    "Shani",
    "Sheala",
    "Syanna",
    "Tissaia",
    "Toruviel",
    "Triss",
    "Uma",
    "Ursine",
    "Valdo",
    "Ves",
    "Vesemir",
    "Vilgefortz",
    "Visenna",
    "Vivienne",
    "Vizima",
    "Vlodimir",
    "Voymir",
    "Waldemar",
    "Werewolf",
    "Witcher",
    "Xenia",
    "Yennefer",
    "Zireael",
    "Zoltan",
    "Zoria",
    "Zuleyka",
]

male_names = [
    "Alar",
    "Alden",
    "Aldert",
    "Aldric",
    "Alf",
    "Aubry",
    "Baldo",
    "Barnabas",
    "Beldar",
    "Berthold",
    "Borkh",
    "Bran",
    "Cahir",
    "Calanthe",
    "Coram",
    "Cyprian",
    "Cyran",
    "Dagon",
    "Dal",
    "Damen",
    "Dandelion",
    "Deidre",
    "Draig",
    "Eamon",
    "Egan",
    "Einar",
    "Emhyr",
    "Emiel",
    "Erdin",
    "Ferrant",
    "Fioravanti",
    "Folan",
    "Folke",
    "Folko",
    "Foltest",
    "Gaetan",
    "Gaston",
    "Gawen",
    "Geoffrey",
    "Gerd",
    "Hawkesburn",
    "Helti",
    "Hemdall",
    "Hjalmar",
    "Hjort",
    "Ida",
    "Igor",
    "Iorveth",
    "Isengrim",
    "Iskra",
    "Istredd",
    "Jarop",
    "Jaskier",
    "Javed",
    "Jehan",
    "Jolan",
    "Jorgen",
    "Kalkstein",
    "Kerack",
    "Kingslayer",
    "Kolgrim",
    "Koshchey",
    "Lauden",
    "Lavellan",
    "Lerant",
    "Letho",
    "Lugos",
    "Madoc",
    "Majordomo",
    "Marder",
    "Milo",
    "Milt",
    "Mousesack",
    "Nagel",
    "Narwal",
    "Nechtan",
    "Nekker",
    "Nivellen",
    "Nordling",
    "Odrin",
    "Olgierd",
    "Olgrym",
    "Ortolan",
    "Ostrit",
    "Peleg",
    "Percival",
    "Peregrine",
    "Petrus",
    "Pimpernel",
    "Quentin",
    "Quirin",
    "Radovid",
    "Radowid",
    "Raffard",
    "Ravix",
    "Redanian",
    "Savolla",
    "Siegfried",
    "Sigismund",
    "Sorel",
    "Talar",
    "Tallim",
    "Tobias",
    "Triss",
    "Tybalt",
    "Ulfric",
    "Ulfried",
    "Ulrich",
    "Urian",
    "Urtica",
    "Vaedermakar",
    "Valdo",
    "Valerian",
    "Vesemir",
    "Vimme",
    "Vladimir",
    "Weasel",
    "Weavess",
    "Werdern",
    "Wilhelm",
    "Witchman",
    "Xander",
    "Xerxes",
    "Xymon",
    "Yanne",
    "Yanniss",
    "Yaren",
    "Yargos",
    "Yarpen",
    "Yngvar",
    "Zdenek",
    "Zoltan",
    "Zyvik",
]

surnames = [
    "of Aedirn",
    "of Anglia",
    "of Angren",
    "of Ban Ard",
    "of Brokilon",
    "of Brugge",
    "of Caelf",
    "of Cidaris",
    "of Cintra",
    "of Claremont",
    "of Creyden",
    "of Darn Rowan",
    "of Dol Blathanna",
    "of Doria",
    "of Ebbing",
    "of Erlenwald",
    "of Geso",
    "of Gors Velen",
    "of Hagge",
    "of Hindarsfjall",
    "of Kaer Morhen",
    "of Kovir",
    "of Lan Exeter",
    "of Lower Posada",
    "of Lyria",
    "of Mahakam",
    "of Malleore",
    "of Maribor",
    "of Marvik",
    "of Murivel",
    "of Nazair",
    "of Nilfgaard",
    "of Novigrad",
    "of Oxenfurt",
    "of Poviss",
    "of Redania",
    "of Rinde",
    "of Riverdell",
    "of Rivia",
    "of Skellige",
    "of Sodden",
    "of Temeria",
    "of Tir Tochair",
    "of Toussaint",
    "of Upper Posada",
    "of Verden",
    "of Vicovaro",
    "of Vizima",
    "of Zerrikania",
]


female = generate_female_name(female_prefix, female_suffix, min=1, max=1)
male = generate_male_name(male_prefix, male_suffix, min=1, max=1)
surname = generate_surname_less(surname_prefix, surname_suffix)

female_lbr = choice(female_names)
male_lbr = choice(male_names)
surname_lbr = choice(surnames)

from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname_less,
    remove_duplicates,
)


female_prefix = [
    "aes",
    "al",
    "an",
    "ar",
    "bel",
    "cy",
    "dam",
    "el",
    "fae",
    "gal",
    "gi",
    "grai",
    "hel",
    "ie",
    "is",
    "jhan",
    "kara",
    "lae",
    "lan",
    "le",
    "ly",
    "mae",
    "mer",
    "nae",
    "ni",
    "ny",
    "pae",
    "pe",
    "rae",
    "ri",
    "sai",
    "ser",
    "shi",
    "syl",
    "the",
    "tho",
    "ty",
    "vae",
    "vel",
    "ver",
    "ya",
    "yse",
    "zel",
]

female_suffix = [
    "a",
    "ai",
    "an",
    "ana",
    "ara",
    "ath",
    "da",
    "di",
    "dra",
    "e",
    "ela",
    "ena",
    "era",
    "i",
    "ia",
    "iana",
    "iara",
    "idra",
    "in",
    "ina",
    "ira",
    "is",
    "isa",
    "la",
    "li",
    "lia",
    "lin",
    "lla",
    "n",
    "na",
    "ne",
    "ni",
    "nia",
    "ra",
    "re",
    "ri",
    "ria",
    "rina",
    "ris",
    "sha",
    "si",
    "sia",
    "th",
    "tha",
    "the",
    "ti",
    "tia",
    "tira",
    "ya",
    "yna",
    "yra",
]

male_prefix = [
    "al",
    "an",
    "ar",
    "ben",
    "cal",
    "cor",
    "dar",
    "el",
    "fal",
    "gal",
    "har",
    "in",
    "jar",
    "kan",
    "lan",
    "mar",
    "nor",
    "or",
    "pal",
    "quan",
    "ran",
    "sar",
    "tal",
    "var",
    "wal",
    "xan",
    "yan",
    "zan",
]

male_suffix = [
    "al",
    "an",
    "ar",
    "as",
    "ath",
    "dan",
    "dar",
    "don",
    "el",
    "en",
    "er",
    "eth",
    "ian",
    "ic",
    "ion",
    "ir",
    "is",
    "ith",
    "lan",
    "lar",
    "len",
    "lon",
    "mar",
    "mon",
    "nor",
    "on",
    "or",
    "ran",
    "ric",
    "ron",
    "sar",
    "son",
    "than",
    "thar",
    "ton",
    "var",
    "von",
    "wan",
    "wen",
    "xar",
    "xon",
    "yan",
    "zan",
]

surname_prefix = [
    "al",
    "an",
    "ar",
    "bal",
    "bar",
    "cal",
    "car",
    "dal",
    "dar",
    "el",
    "en",
    "fal",
    "fin",
    "gal",
    "gar",
    "hal",
    "har",
    "in",
    "jar",
    "kal",
    "kar",
    "lan",
    "lar",
    "mal",
    "mar",
    "nal",
    "nar",
    "or",
    "par",
    "per",
    "qual",
    "qur",
    "ral",
    "rar",
    "sal",
    "sar",
    "tal",
    "tar",
    "val",
    "var",
    "wal",
    "war",
    "xal",
    "xar",
    "yal",
    "yar",
    "zal",
    "zar",
]

surname_suffix = [
    "al",
    "am",
    "an",
    "ar",
    "ash",
    "ath",
    "ban",
    "bar",
    "bel",
    "bor",
    "dal",
    "dan",
    "dar",
    "del",
    "den",
    "dir",
    "don",
    "dor",
    "el",
    "em",
    "en",
    "er",
    "eth",
    "fal",
    "fer",
    "gal",
    "gar",
    "gor",
    "hal",
    "har",
    "in",
    "ir",
    "is",
    "kar",
    "ken",
    "kor",
    "lan",
    "lar",
    "len",
    "lor",
    "mal",
    "mar",
    "mel",
    "mor",
    "nal",
    "nel",
    "nor",
    "on",
    "or",
    "oth",
    "par",
    "pel",
    "por",
    "qar",
    "qor",
    "ral",
    "ran",
    "ren",
    "ril",
    "ron",
    "sal",
    "sel",
    "sol",
    "tal",
    "tel",
    "thor",
    "ton",
    "tor",
    "val",
    "vel",
    "vor",
    "wal",
    "wen",
    "wor",
    "xal",
    "xar",
    "xel",
    "xor",
    "yal",
    "yen",
    "yor",
    "zal",
    "zar",
]

female_names = [
    "Acuin",
    "Adina",
    "Adria",
    "Aes",
    "Alain",
    "Alanna",
    "Alind",
    "Alise",
    "Alsbet",
    "Aludra",
    "Amaline",
    "Amathera",
    "Amena",
    "Amerie",
    "Amira",
    "Amys",
    "Anaiya",
    "Ananda",
    "Anarra",
    "Anla",
    "Aradia",
    "Aramina",
    "Arathelle",
    "Ariena",
    "Arymilla",
    "Asne",
    "Astara",
    "Astrid",
    "Athelle",
    "Aviendha",
    "Avila",
    "Avin",
    "Azil",
    "Azira",
    "Bael",
    "Bain",
    "Basel",
    "Bela",
    "Beldeine",
    "Berelain",
    "Beri",
    "Berowin",
    "Berylla",
    "Bethamin",
    "Betsi",
    "Birgitte",
    "Blaes",
    "Boirin",
    "Bolivar",
    "Brendas",
    "Briar",
    "Brigitte",
    "Byar",
    "Cabriana",
    "Cadsuane",
    "Cadwyn",
    "Caemlyn",
    "Caire",
    "Caraighan",
    "Caraline",
    "Careane",
    "Cari",
    "Carlinya",
    "Carlyn",
    "Caryn",
    "Catalyn",
    "Cath",
    "Cerise",
    "Chaelin",
    "Chai",
    "Chana",
    "Chanai",
    "Charris",
    "Chel",
    "Chesa",
    "Chesmal",
    "Chesna",
    "Ciara",
    "Cieryl",
    "Corele",
    "Covril",
    "Daigan",
    "Dalyn",
    "Damer",
    "Danelle",
    "Danette",
    "Daricain",
    "Deain",
    "Deindre",
    "Deira",
    "Delana",
    "Delinda",
    "Delora",
    "Derys",
    "Doraise",
    "Dorindha",
    "Dorine",
    "Duhara",
    "Edarra",
    "Egeanin",
    "Egwene",
    "Elaida",
    "Elayne",
    "Elly",
    "Elmindreda",
    "Elza",
    "Emara",
    "Erian",
    "Escarin",
    "Esne",
    "Faile",
    "Fearnan",
    "Fel",
    "Fela",
    "Felain",
    "Felice",
    "Felinda",
    "Felisa",
    "Ferane",
    "Gaebril",
    "Gaidal",
    "Galadriel",
    "Galina",
    "Ganin",
    "Garenia",
    "Gareth",
    "Garima",
    "Gawyn",
    "Geofram",
    "Gisela",
    "Graendal",
    "Greandil",
    "Gween",
    "Haesel",
    "Hafwen",
    "Hamlin",
    "Hanlon",
    "Haviar",
    "Ileen",
    "Ileis",
    "Ilena",
    "Ilyane",
    "Ilyena",
    "Indirian",
    "Iona",
    "Ionin",
    "Isendre",
    "Ispan",
    "Izar",
    "Jahar",
    "Jaichim",
    "Jaik",
    "Jaisin",
    "Jalan",
    "Jamil",
    "Janwin",
    "Janya",
    "Jeaine",
    "Jennet",
    "Joline",
    "Jorin",
    "Juilaine",
    "Julanya",
    "Juliane",
    "Juline",
    "Juliya",
    "Kadere",
    "Kairen",
    "Karale",
    "Karind",
    "Katerine",
    "Katrine",
    "Kelle",
    "Keraille",
    "Kesra",
    "Kewin",
    "Keylin",
    "Keylyn",
    "Kirstian",
    "Kirstin",
    "Kiruna",
    "Kiva",
    "Korinna",
    "Krinnin",
    "Lacile",
    "Lan",
    "Lanfear",
    "Lanfir",
    "Laras",
    "Larelle",
    "Larine",
    "Larissa",
    "Latelle",
    "Layne",
    "Leah",
    "Leane",
    "Learen",
    "Leira",
    "Lelaine",
    "Lemai",
    "Lesale",
    "Letice",
    "Lian",
    "Liandrin",
    "Lidya",
    "Lilaine",
    "Lini",
    "Linna",
    "Linora",
    "Lirene",
    "Lizl",
    "Lizla",
    "Llyw",
    "Loisane",
    "Loise",
    "Loral",
    "Lorel",
    "Ludice",
    "Lusonia",
    "Lyala",
    "Lyrelle",
    "Maigan",
    "Mair",
    "Maire",
    "Malane",
    "Malia",
    "Mallia",
    "Mandarb",
    "Mandevwin",
    "Mandhol",
    "Marah",
    "Marande",
    "Mardene",
    "Maredo",
    "Marees",
    "Marinda",
    "Marinna",
    "Marly",
    "Martine",
    "Meidani",
    "Melaine",
    "Melavaire",
    "Meli",
    "Melis",
    "Mella",
    "Mellar",
    "Melore",
    "Merana",
    "Merane",
    "Meri",
    "Merice",
    "Merinda",
    "Merith",
    "Merya",
    "Merym",
    "Merza",
    "Mesaana",
    "Midra",
    "Miesh",
    "Milam",
    "Mili",
    "Milis",
    "Min",
    "Miri",
    "Mirise",
    "Mirshalan",
    "Mist",
    "Mistri",
    "Moghedien",
    "Moiraine",
    "Monaelle",
    "Morelin",
    "Morgase",
    "Moridin",
    "Morvanya",
    "Morvrin",
    "Mychelle",
    "Naday",
    "Nadia",
    "Nadore",
    "Naean",
    "Nalin",
    "Nalria",
    "Namina",
    "Nana",
    "Naorise",
    "Narenwin",
    "Nari",
    "Narin",
    "Narisse",
    "Narra",
    "Natal",
    "Nela",
    "Neldis",
    "Nelin",
    "Nerin",
    "Nessa",
    "Nesune",
    "Nien",
    "Nisain",
    "Nisha",
    "Nishan",
    "Nishelle",
    "Nishin",
    "Nissin",
    "Noane",
    "Nuhel",
    "Nymeria",
    "Nyna",
    "Nynaeve",
    "Nyneave",
    "Nyse",
    "Obray",
    "Olver",
    "Oran",
    "Ordi",
    "Osan",
    "Osen",
    "Pura",
    "Quillin",
    "RJ",
    "Raen",
    "Rahari",
    "Rahlin",
    "Rahvin",
    "Rainyn",
    "Rajin",
    "Rajine",
    "Randa",
    "Randalle",
    "Randi",
    "Randina",
    "Reanne",
    "Renaile",
    "Renaj",
    "Renal",
    "Renara",
    "Rendra",
    "Resara",
    "Resh",
    "Reshan",
    "Rhiale",
    "Rhys",
    "Rianna",
    "Rienne",
    "Ries",
    "Rigna",
    "Rilla",
    "Riwal",
    "Rohannon",
    "Rohara",
    "Rohelle",
    "Rohila",
    "Rolan",
    "Rolin",
    "Rolina",
    "Rolum",
    "Romanda",
    "Romany",
    "Roshalle",
    "Roshin",
    "Roshina",
    "Rosil",
    "Rovair",
    "Rubinde",
    "Rushal",
    "Rylen",
    "Saerain",
    "Saerin",
    "Safride",
    "Sailene",
    "Sair",
    "Sairah",
    "Saje",
    "Saldaean",
    "Salian",
    "Salmara",
    "Salome",
    "Salorin",
    "Samitsu",
    "Samma",
    "Samya",
    "Sanche",
    "Sandair",
    "Sare",
    "Sareitha",
    "Sarene",
    "Saria",
    "Sariel",
    "Sarylla",
    "Sasha",
    "Sashalle",
    "Sashan",
    "Sashay",
    "Sashaye",
    "Satina",
    "Seain",
    "Seaine",
    "Seana",
    "Sedore",
    "Selame",
    "Selene",
    "Selinde",
    "Semirhage",
    "Senine",
    "Senit",
    "Seonid",
    "Serafelle",
    "Seraine",
    "Serancha",
    "Seranilla",
    "Seren",
    "Seri",
    "Serile",
    "Serilla",
    "Serin",
    "Seris",
    "Serisha",
    "Serith",
    "Serly",
    "Seryne",
    "Sevanna",
    "Shalin",
    "Shani",
    "Shara",
    "Sharina",
    "Shelonne",
    "Sherain",
    "Sheraine",
    "Sheriam",
    "Sheril",
    "Shiaine",
    "Shiane",
    "Shiara",
    "Shiela",
    "Shielyn",
    "Shin",
    "Shinare",
    "Shiral",
    "Shizar",
    "Shizuk",
    "Shyka",
    "Sidelle",
    "Sidra",
    "Sima",
    "Simara",
    "Siona",
    "Siron",
    "Siuan",
    "Sofela",
    "Soile",
    "Solinda",
    "Sorella",
    "Sorilea",
    "Suana",
    "Suian",
    "Talene",
    "Tamela",
    "Tarna",
    "Tema",
    "Teslyn",
    "Theodrin",
    "Tiana",
    "Toveine",
    "Travera",
    "Turan",
    "Vandene",
    "Varilin",
    "Verin",
    "Yukiri",
    "Zaida",
    "Zarine",
    "Zarya",
    "Zemaille",
    "Zerah",
    "Zeranda",
    "Zhuin",
]

male_names = [
    "Abell",
    "Algar",
    "Aram",
    "Artur",
    "Asmodean",
    "Balwer",
    "Barthanes",
    "Basel",
    "Bayle",
    "Birgitte",
    "Bordin",
    "Bran",
    "Bryne",
    "Cadsuane",
    "Cairhien",
    "Caraline",
    "Carridin",
    "Cauthon",
    "Dain",
    "Damer",
    "Darlin",
    "Daved",
    "Davram",
    "Dobraine",
    "Egwene",
    "Elaida",
    "Elan",
    "Elayne",
    "Fain",
    "Furyk",
    "Gaebril",
    "Galad",
    "Galadedrid",
    "Gareth",
    "Gawyn",
    "Geofram",
    "Gill",
    "Hadnan",
    "Hammar",
    "Haral",
    "Harod",
    "Hurin",
    "Ingtar",
    "Jaem",
    "Jak",
    "Jaret",
    "Jarid",
    "Javindhra",
    "Jeade",
    "Jur",
    "Karldin",
    "Kerene",
    "Lan",
    "Logain",
    "Loial",
    "Lunan",
    "Lyon",
    "Mandevwin",
    "Masema",
    "Mat",
    "Mazrim",
    "Meilan",
    "Meri",
    "Mist",
    "Narishma",
    "Niall",
    "Noal",
    "Nynaeve",
    "Olver",
    "Pedron",
    "Perival",
    "Perrin",
    "Pevin",
    "Rahvin",
    "Rand",
    "Raolin",
    "Rhadam",
    "Rhavin",
    "Rodel",
    "Romain",
    "Samel",
    "Selame",
    "Selvyn",
    "Stepper",
    "Swovan",
    "Taim",
    "Tam",
    "Taringail",
    "Thom",
    "Toram",
    "Tylin",
    "Valan",
    "Verin",
    "Weiramon",
    "Wit",
    "Wyse",
    "Xander",
    "Yarin",
    "Zachere",
    "Zarine",
]

surnames = [
    "Aldiaya",
    "Aldragoran",
    "Ambrey",
    "Arrel",
    "Asha'man",
    "Aybara",
    "Bael",
    "Barashta",
    "Bashere",
    "Bryne",
    "Bukama",
    "Caraighan",
    "Carridin",
    "Cauthon",
    "Charin",
    "Chel Vanin",
    "Congar",
    "Conle",
    "Corly",
    "Dagdara",
    "Dain",
    "Damodred",
    "Danre",
    "Darsson",
    "Davion",
    "Davram",
    "Dearnim",
    "Delein",
    "Elan",
    "Eldre",
    "Eldrene",
    "Eldrith",
    "Farstrider",
    "Gaidin",
    "Ger",
    "Halwin",
    "Hammar",
    "Hark",
    "Hawkwing",
    "Hearn",
    "Hearne",
    "Hearthman",
    "Herand",
    "Hopper",
    "Isidore",
    "Janwin",
    "Jennet",
    "Kandar",
    "Kari",
    "Kiem",
    "Krivin",
    "Lancere",
    "Larsson",
    "Leane",
    "Leanne",
    "Lemore",
    "Luk",
    "Machera",
    "Machin Shin",
    "Mandragoran",
    "Mandros",
    "Matherin",
    "Mathwin",
    "Matuchin",
    "Melan",
    "Menshima",
    "Miliobar",
    "Mishraile",
    "Monaelle",
    "Morad",
    "Narvin",
    "Nimram",
    "Nobuta",
    "Oram",
    "Paeron",
    "Paetram",
    "Palkar",
    "Peverin",
    "Radorn",
    "Raen",
    "Rahvin",
    "Ramshalan",
    "Riatin",
    "Roedran",
    "Romar",
    "Saighan",
    "Sakin",
    "Sashalle",
    "Sedai",
    "Sedore",
    "Selorna",
    "Shi",
    "Shimron",
    "Sisnera",
    "Straif",
    "Taravin",
    "Teir",
    "Thaenic",
    "Thaenis",
    "Thalav",
    "Thane",
    "Tihera",
    "Toma",
    "Tomas",
    "Traemane",
    "Valer",
    "Valon",
    "Vram",
    "Wagstrom",
    "Wilam",
    "Yane",
    "Yanet",
    "Zaeim",
    "Zahn",
    "Zarene",
    "Zea",
    "Zearl",
    "al'Caar",
    "al'Dai",
    "al'Lora",
    "al'Sayar",
    "al'Shieb",
    "al'Tealdar",
    "al'Thor",
    "al'Thorin",
    "al'Vere",
    "an'Boroleos",
]

female = generate_female_name(female_prefix, female_suffix, min=0, max=2)
male = generate_male_name(male_prefix, male_suffix, min=0, max=2)
surname = generate_surname_less(surname_prefix, surname_suffix)

female_lbr = choice(female_names)
male_lbr = choice(male_names)
surname_lbr = choice(surnames)

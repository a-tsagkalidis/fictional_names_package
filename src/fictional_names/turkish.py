from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname_less,
    remove_duplicates,
)

female_prefix = [
    "a",
    "ad",
    "ah",
    "al",
    "ar",
    "as",
    "ay",
    "b",
    "ba",
    "be",
    "ca",
    "ce",
    "ci",
    "da",
    "de",
    "di",
    "e",
    "el",
    "em",
    "en",
    "er",
    "es",
    "ev",
    "f",
    "g",
    "ga",
    "ge",
    "gi",
    "gu",
    "h",
    "ha",
    "i",
    "il",
    "is",
    "k",
    "ka",
    "ke",
    "ki",
    "ko",
    "ku",
    "l",
    "la",
    "le",
    "li",
    "lu",
    "m",
    "ma",
    "me",
    "mi",
    "mu",
    "n",
    "na",
    "ne",
    "ni",
    "o",
    "or",
    "p",
    "r",
    "ra",
    "re",
    "ri",
    "ru",
    "s",
    "sa",
    "se",
    "si",
    "su",
    "t",
    "ta",
    "te",
    "ti",
    "u",
    "un",
    "ur",
    "us",
    "ut",
    "v",
    "ya",
    "ye",
    "yi",
    "yi",
    "yö",
    "yu",
    "z",
]

female_suffix = [
    "a",
    "an",
    "ay",
    "ça",
    "can",
    "ce",
    "çe",
    "dem",
    "den",
    "e",
    "el",
    "em",
    "en",
    "er",
    "es",
    "et",
    "gül",
    "han",
    "i",
    "il",
    "im",
    "in",
    "ir",
    "iş",
    "iz",
    "ka",
    "kan",
    "ke",
    "kiz",
    "la",
    "le",
    "li",
    "lik",
    "miş",
    "nur",
    "o",
    "ol",
    "ön",
    "öz",
    "ra",
    "re",
    "rin",
    "ru",
    "sa",
    "şan",
    "se",
    "si",
    "su",
    "tan",
    "te",
    "ti",
    "tu",
    "tül",
    "u",
    "ur",
    "ü",
    "ya",
    "ye",
    "yi",
    "yi",
    "yor",
    "yu",
    "z",
]

male_prefix = [
    "ah",
    "al",
    "ar",
    "ba",
    "be",
    "ca",
    "ce",
    "da",
    "de",
    "el",
    "em",
    "fa",
    "ga",
    "ge",
    "ha",
    "he",
    "ib",
    "ic",
    "id",
    "id",
    "ja",
    "je",
    "ka",
    "ke",
    "la",
    "le",
    "ma",
    "me",
    "na",
    "ne",
    "oğ",
    "ol",
    "or",
    "pa",
    "pe",
    "ra",
    "re",
    "sa",
    "se",
    "ta",
    "te",
    "uğ",
    "ul",
    "ur",
    "va",
    "ve",
    "ya",
    "ye",
    "za",
    "ze",
]

male_suffix = [
    "an",
    "ar",
    "at",
    "ay",
    "baş",
    "bay",
    "can",
    "dağ",
    "dem",
    "dil",
    "el",
    "er",
    "gün",
    "han",
    "kaç",
    "kan",
    "kara",
    "kar",
    "kurt",
    "köylü",
    "öz",
    "polat",
    "sari",
    "sel",
    "soy",
    "şah",
    "türk",
    "uçar",
    "ul",
    "uzun",
    "yil",
    "yildiz",
    "yüz",
    "zorlu",
]

surname_prefix = [
    "ak",
    "alp",
    "ar",
    "as",
    "ay",
    "bar",
    "bay",
    "boz",
    "can",
    "cev",
    "çak",
    "çel",
    "dağ",
    "dem",
    "dil",
    "doğ",
    "dur",
    "ege",
    "er",
    "ev",
    "gök",
    "güç",
    "han",
    "iş",
    "işik",
    "iz",
    "kaç",
    "kara",
    "kiliç",
    "kurt",
    "küz",
    "men",
    "öz",
    "pinar",
    "sancak",
    "sari",
    "savaş",
    "sevinç",
    "şah",
    "şen",
    "tek",
    "toprak",
    "tunç",
    "ul",
    "üstün",
    "yildiz",
    "yilmaz",
    "yoğun",
    "zor",
]

surname_suffix = [
    "ağa",
    "ak",
    "al",
    "an",
    "baş",
    "bay",
    "bek",
    "boğa",
    "çar",
    "dağ",
    "demir",
    "dil",
    "er",
    "göl",
    "güç",
    "han",
    "kaç",
    "kan",
    "kar",
    "kiliç",
    "köy",
    "kurt",
    "man",
    "oğlu",
    "öz",
    "pinar",
    "san",
    "sar",
    "savaş",
    "şan",
    "şen",
    "taş",
    "tepe",
    "tunç",
    "türk",
    "ul",
    "uş",
    "üz",
    "yalin",
    "yildiz",
    "yilmaz",
    "yoğun",
    "zade",
]

female_names = [
    "Ada",
    "Ahu",
    "Alev",
    "Arzu",
    "Asli",
    "Aydan",
    "Ayfer",
    "Ayla",
    "Aylin",
    "Ayten",
    "Ayça",
    "Ayşe",
    "Bahar",
    "Banu",
    "Belgin",
    "Belkis",
    "Bengü",
    "Berna",
    "Berrin",
    "Betül",
    "Beyza",
    "Bilge",
    "Binnaz",
    "Bircan",
    "Birsen",
    "Burcu",
    "Buse",
    "Candan",
    "Cansu",
    "Cemre",
    "Ceyda",
    "Ceylan",
    "Damla",
    "Defne",
    "Demet",
    "Deniz",
    "Derya",
    "Dilber",
    "Dilek",
    "Dudu",
    "Eda",
    "Ediz",
    "Ekin",
    "Elif",
    "Elmas",
    "Emel",
    "Emine",
    "Esin",
    "Esra",
    "Eylem",
    "Ezgi",
    "Fadime",
    "Fatma",
    "Feride",
    "Feyza",
    "Figen",
    "Filiz",
    "Gaye",
    "Gizem",
    "Gül",
    "Gülay",
    "Gülcan",
    "Gülden",
    "Gülen",
    "Güler",
    "Gülizar",
    "Gülperi",
    "Gülçin",
    "Gülşen",
    "Güneş",
    "Güzin",
    "Hale",
    "Handan",
    "Hazan",
    "Hülya",
    "Kader",
    "Kamile",
    "Kevser",
    "Lale",
    "Leyla",
    "Merve",
    "Meryem",
    "Müge",
    "Nalan",
    "Nergis",
    "Nermin",
    "Nil",
    "Nur",
    "Nuray",
    "Nurdan",
    "Nurten",
    "Oya",
    "Pakize",
    "Pelin",
    "Pinar",
    "Rabia",
    "Reyhan",
    "Seda",
    "Seher",
    "Selma",
    "Sevim",
    "Sevinç",
    "Simge",
    "Songül",
    "Su",
    "Sude",
    "Sultan",
    "Tülay",
    "Türkan",
    "Umay",
    "Yasemin",
    "Yeliz",
    "Yeşim",
    "Yildiz",
    "Yonca",
    "Yurdagül",
    "Zehra",
    "Zeliha",
    "Zerrin",
    "Zeynep",
    "Zübeyde",
    "Çiçek",
    "Çiğdem",
    "Özge",
    "Ümmü",
    "İclal",
    "İlknur",
    "İrem",
    "Şebnem",
    "Şenay",
    "Şermin",
    "Şule",
    "Şükran",
]

male_names = [
    "Abdullah",
    "Acun",
    "Adem",
    "Adnan",
    "Ahmed",
    "Ahmet",
    "Akin",
    "Ali",
    "Alp",
    "Alparslan",
    "Amin",
    "Amir",
    "Asaf",
    "Aslan",
    "Atilla",
    "Aydin",
    "Ayhan",
    "Aytaç",
    "Azat",
    "Aziz",
    "Aşina",
    "Bahadir",
    "Bariş",
    "Batu",
    "Bekir",
    "Berat",
    "Berkant",
    "Bilal",
    "Bozkurt",
    "Bumin",
    "Burhan",
    "Bülent",
    "Can",
    "Cengiz",
    "Cenk",
    "Cevher",
    "Cihan",
    "Cihat",
    "Cüneyt",
    "Davut",
    "Deniz",
    "Dinçer",
    "Doğan",
    "Dursun",
    "Dündar",
    "Emin",
    "Emir",
    "Emre",
    "Ender",
    "Ercüment",
    "Erol",
    "Ertuğrul",
    "Evren",
    "Eymen",
    "Fahri",
    "Faruk",
    "Fatih",
    "Feridun",
    "Gazi",
    "Gencay",
    "Gökhan",
    "Gökmen",
    "Göktürk",
    "Güven",
    "Hakan",
    "Hakki",
    "Halil",
    "Halis",
    "Hamdi",
    "Harun",
    "Hasan",
    "Hulusi",
    "Hüseyin",
    "Ibrahim",
    "Ismail",
    "Kaan",
    "Kadir",
    "Kamuran",
    "Kasim",
    "Kaya",
    "Kemal",
    "Kiliç",
    "Levent",
    "Lütfi",
    "Mahir",
    "Mazlum",
    "Mehmet",
    "Mert",
    "Muhammed",
    "Muhammet",
    "Murat",
    "Mustafa",
    "Necati",
    "Nevzat",
    "Nihat",
    "Orhan",
    "Orkun",
    "Osman",
    "Ozan",
    "Oğuz",
    "Poyraz",
    "Rahmi",
    "Ramazan",
    "Recep",
    "Riza",
    "Sadik",
    "Selahattin",
    "Selim",
    "Serdar",
    "Sultan",
    "Süleyman",
    "Talha",
    "Tarik",
    "Tarkan",
    "Tayfun",
    "Tayyar",
    "Timur",
    "Turgay",
    "Ufuk",
    "Umut",
    "Uğur",
    "Yasin",
    "Yavuz",
    "Yildirim",
    "Yildiz",
    "Yilmaz",
    "Zafer",
    "Zeki",
    "Ziya",
    "Ömer",
    "Önder",
    "Özcan",
    "İbrahim",
    "İlhan",
    "İlyas",
    "İrfan",
    "İskender",
    "İsmet",
    "Şahin",
    "Şevket",
]

surnames = [
    "Abacioğlu",
    "Akinci",
    "Aksoy",
    "Alparslan",
    "Arslan",
    "Ateş",
    "Atçeken",
    "Avci",
    "Aybar",
    "Aydin",
    "Ayhan",
    "Ağaoğlu",
    "Baltaci",
    "Bardakoğlu",
    "Bayik",
    "Bayraktar",
    "Bağriyanik",
    "Bekiroğlu",
    "Beyazit",
    "Beşikçi",
    "Bozkurt",
    "Boğa",
    "Büyükberber",
    "Dağdeviren",
    "Demir",
    "Demirci",
    "Derebey",
    "Dilaver",
    "Doğan",
    "Durmaz",
    "Ekinci",
    "Erdoğan",
    "Eren",
    "Ergin",
    "Eroğlu",
    "Erçetin",
    "Gedikoğlu",
    "Göktürk",
    "Gültekin",
    "Güney",
    "Gürsoy",
    "Haktanir",
    "Kaplan",
    "Karabulut",
    "Karadağ",
    "Karahan",
    "Kartal",
    "Kaya",
    "Keskin",
    "Kiliç",
    "Korkmaz",
    "Koç",
    "Kurt",
    "Kutlu",
    "Kutluay",
    "Kutluhan",
    "Köksal",
    "Mert",
    "Mirza",
    "Mutlu",
    "Noyan",
    "Okçu",
    "Pehlivan",
    "Sari",
    "Savaş",
    "Sağlam",
    "Seçkin",
    "Tayyar",
    "Taşci",
    "Taşkin",
    "Tekin",
    "Topal",
    "Topçu",
    "Tosun",
    "Tuğrul",
    "Türk",
    "Uludağ",
    "Uluçay",
    "Uysal",
    "Yalçin",
    "Yaman",
    "Yildirim",
    "Yildiz",
    "Yilmaz",
    "Yücel",
    "Zeybek",
    "Zorlu",
    "Zülfikar",
    "Zümrüt",
    "Çakir",
    "Çatalkaya",
    "Çelik",
    "Özdemir",
    "Özen",
    "Özkaya",
    "Özkök",
    "Öztürk",
    "Özyürek",
    "Ünal",
    "Üngör",
    "Üstün",
    "İlhan",
    "İnanç",
    "Şahin",
    "Şahsuvar",
    "Şeker",
    "Şen",
    "Şimşek",
]

female = generate_female_name(female_prefix, female_suffix, min=1, max=1)
male = generate_male_name(male_prefix, male_suffix, min=1, max=1)
surname = generate_surname_less(surname_prefix, surname_suffix)

female = generate_female_name(female_prefix, female_suffix, min=1, max=1)
male = generate_male_name(male_prefix, male_suffix, min=1, max=1)
surname = generate_surname_less(surname_prefix, surname_suffix)

female_lbr = choice(female_names)
male_lbr = choice(male_names)
surname_lbr = choice(surnames)

# print(remove_duplicates(surnames))

# for name in female_names:
#     print("'", name.capitalize(), "'", sep='', end=', ')

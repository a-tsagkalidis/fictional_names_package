from random import choice
from .supportive_functions import (
    generate_female_name,
    generate_male_name,
    generate_surname_less,
    remove_duplicates,
)

female_prefix = [
    "að",
    "alfr",
    "arn",
    "asa",
    "astr",
    "aud",
    "berg",
    "bor",
    "brun",
    "dagn",
    "eir",
    "ek",
    "fre",
    "frid",
    "geir",
    "gjo",
    "gud",
    "gyð",
    "haf",
    "halla",
    "hel",
    "her",
    "hild",
    "ing",
    "kat",
    "kel",
    "liv",
    "magn",
    "ny",
    "od",
    "rau",
    "sig",
    "siv",
    "skul",
    "svanh",
    "thor",
    "tor",
    "ulv",
    "val",
    "yngv",
]

female_suffix = [
    "a",
    "dis",
    "dís",
    "frid",
    "fríð",
    "gerðr",
    "gjerd",
    "gunn",
    "gyða",
    "hildr",
    "lif",
    "líf",
    "run",
    "rún",
    "sol",
    "sól",
    "tora",
    "þora",
    "vor",
    "vör",
]

male_prefix = [
    "arn",
    "bal",
    "bjorn",
    "dar",
    "ein",
    "erik",
    "fre",
    "grim",
    "gunn",
    "hakon",
    "har",
    "ing",
    "ivar",
    "leif",
    "magnus",
    "odin",
    "olaf",
    "rag",
    "sig",
    "sven",
    "thor",
    "ulf",
    "vald",
    "vik",
    "wul",
]

male_suffix = [
    "ald",
    "ar",
    "bard",
    "bjorn",
    "brand",
    "dor",
    "end",
    "fred",
    "gard",
    "grim",
    "hak",
    "hart",
    "kel",
    "laf",
    "mar",
    "olf",
    "rak",
    "rik",
    "run",
    "stein",
    "thor",
    "ulf",
    "vald",
    "var",
    "vik",
    "yng",
]

surname_prefix = [
    "arn",
    "as",
    "bal",
    "ber",
    "dag",
    "ein",
    "erl",
    "fro",
    "gar",
    "hak",
    "ing",
    "jar",
    "kar",
    "lif",
    "magn",
    "nor",
    "od",
    "ragn",
    "sig",
    "thor",
    "ulf",
    "val",
    "yng",
]

surname_suffix = [
    "brand",
    "dottir",
    "fjord",
    "grim",
    "hald",
    "ing",
    "jord",
    "karl",
    "lief",
    "mann",
    "nor",
    "olfr",
    "rav",
    "sif",
    "skar",
    "son",
    "ulf",
    "vald",
    "wulf",
    "yr",
]

female_names = [
    "Aesa",
    "Agatha",
    "Ailith",
    "Aldis",
    "Alfhild",
    "Alfhildr",
    "Alva",
    "Arnbjorg",
    "Asa",
    "Asgunna",
    "Aslog",
    "Astrid",
    "Astrida",
    "Auda",
    "Audhildr",
    "Birgit",
    "Birna",
    "Bjorg",
    "Bodil",
    "Boedicia",
    "Borg",
    "Borghild",
    "Borghildr",
    "Borgrun",
    "Botulfr",
    "Brenn",
    "Brenna",
    "Brura",
    "Brynhildr",
    "Brynju",
    "Dagmar",
    "Dagn",
    "Dagney",
    "Dagni",
    "Dagny",
    "Dagný",
    "Dagr",
    "Dagrun",
    "Dagrún",
    "Dofa",
    "Dor",
    "Dárgud",
    "Edda",
    "Edith",
    "Eilif",
    "Eimyrja",
    "Eira",
    "Eirik",
    "Eirika",
    "Eiriksdóttir",
    "Eirny",
    "Eirífa",
    "Eivor",
    "Eldhildr",
    "Eldin",
    "Eldrid",
    "Eldrida",
    "Elin",
    "Estrid",
    "Freya",
    "Freybjorg",
    "Freyda",
    "Freydis",
    "Freylaug",
    "Frida",
    "Fridleif",
    "Fridleva",
    "Fridri",
    "Fridrika",
    "Fridu",
    "Friduna",
    "Frigg",
    "Friggja",
    "Frostina",
    "Fríða",
    "Gerd",
    "Gerda",
    "Gertrúd",
    "Gillaug",
    "Gim",
    "Gin",
    "Gingn",
    "Gio",
    "Gisela",
    "Gisla",
    "Gisli",
    "Gislin",
    "Gizzur",
    "Gladis",
    "Gunnhild",
    "Gyda",
    "Hedvig",
    "Helena",
    "Helga",
    "Hild",
    "Hilda",
    "Hildegard",
    "Hildegunn",
    "Hilding",
    "Hildrid",
    "Hildrun",
    "Hildulv",
    "Hildur",
    "Hildvaldr",
    "Hildvöl",
    "Hildvölur",
    "Hillevi",
    "Ida",
    "Idun",
    "Idunn",
    "Indrid",
    "Inga",
    "Ingeborg",
    "Ingela",
    "Ingiridh",
    "Ingrid",
    "Ingridh",
    "Ingridr",
    "Ingunn",
    "Iolster",
    "Irén",
    "Iréne",
    "Isolde",
    "Jenna",
    "Jofrid",
    "Jofrida",
    "Jona",
    "Jora",
    "Jorid",
    "Jorund",
    "Jorunn",
    "Josefina",
    "Jovilda",
    "Judith",
    "Julfina",
    "Jurdís",
    "Jurðis",
    "Kara",
    "Kari",
    "Karolina",
    "Katrin",
    "Katriona",
    "Katrín",
    "Kelda",
    "Ketra",
    "Kirsten",
    "Kirsti",
    "Kirstin",
    "Kjara",
    "Klara",
    "Kol",
    "Kolbrun",
    "Kolhilda",
    "Lagertha",
    "Lilja",
    "Linda",
    "Lisbeth",
    "Lise",
    "Lisebet",
    "Lisken",
    "Liva",
    "Livia",
    "Lova",
    "Lovis",
    "Lovisa",
    "Ludvika",
    "Lund",
    "Luthviga",
    "Lína",
    "Líne",
    "Magdalena",
    "Magna",
    "Magnhild",
    "Maren",
    "Margareta",
    "Mathilda",
    "Matilda",
    "Mette",
    "Mildred",
    "Mir",
    "Mist",
    "Mjoll",
    "Mojeda",
    "Morrí",
    "Märta",
    "Míldi",
    "Móri",
    "Nanna",
    "Natt",
    "Ninna",
    "Njord",
    "Nora",
    "Norse",
    "Norsea",
    "Nott",
    "Nyda",
    "Nypa",
    "Nyre",
    "Närve",
    "Nína",
    "Nönn",
    "Olga",
    "Ragna",
    "Ragnhild",
    "Ragnhildr",
    "Ragnild",
    "Ranna",
    "Rannvei",
    "Ranveig",
    "Rauth",
    "Rikissa",
    "Rána",
    "Ráðúlfr",
    "Rú",
    "Rúnfrid",
    "Rúnfrí",
    "Rúnh",
    "Rúnhi",
    "Sighild",
    "Sigmund",
    "Signe",
    "Signy",
    "Signý",
    "Sigr",
    "Sigrhildr",
    "Sigrid",
    "Sigridr",
    "Sigrun",
    "Sigryn",
    "Sigrö",
    "Sigrún",
    "Thora",
    "Thordis",
    "Thorfinna",
    "Thorgunna",
    "Thorgunnr",
    "Thornunna",
    "Thurid",
    "Thy",
    "Thyra",
    "Thyri",
    "Thyrs",
    "Tora",
    "Torborg",
    "Tove",
    "Tyra",
    "Ulfhild",
    "Una",
    "Unn",
    "Unnr",
    "Urania",
    "Urd",
    "Urdis",
    "Urdul",
    "Ursula",
    "Urta",
    "Urtla",
    "Urðr",
    "Valdis",
    "Valkyrie",
    "Vigdis",
    "Vigrid",
    "Vigunn",
    "Vilda",
    "Vilde",
    "Vilja",
    "Villgjerd",
    "Vilvei",
    "Vilveig",
    "Vindura",
    "Vinga",
    "Vivianne",
    "Völvina",
    "Ylfa",
    "Ylva",
    "Yngvild",
    "Yngvilda",
    "Yngvildr",
    "Yrsa",
    "Yrse",
    "Yrsel",
    "Yrtt",
    "Yrttt",
    "Yrtu",
    "Yrug",
    "Yvette",
    "Ása",
    "Åsa",
]

male_names = [
    "Agnar",
    "Agni",
    "Aki",
    "Alaric",
    "Alf",
    "Alfgeir",
    "Alrik",
    "Alvar",
    "Amund",
    "Ansgar",
    "Anund",
    "Arne",
    "Arngrim",
    "Arnulf",
    "Arvid",
    "Asbjorn",
    "Asbjørn",
    "Asgeir",
    "Asger",
    "Askold",
    "Aslak",
    "Astrid",
    "Balder",
    "Bengt",
    "Bernt",
    "Bertram",
    "Birger",
    "Birk",
    "Bjarte",
    "Bjorn",
    "Bo",
    "Bragi",
    "Brand",
    "Brandr",
    "Dag",
    "Dagfinn",
    "Dagur",
    "Dan",
    "Egil",
    "Eilif",
    "Einar",
    "Eindride",
    "Eirik",
    "Erik",
    "Erikur",
    "Erlend",
    "Erling",
    "Eyvind",
    "Finn",
    "Folke",
    "Frej",
    "Freybjorn",
    "Freyr",
    "Fridolf",
    "Frode",
    "Gardar",
    "Gisli",
    "Gizur",
    "Gorm",
    "Gudmund",
    "Gunder",
    "Gunnar",
    "Gustav",
    "Hakon",
    "Halfdan",
    "Halfred",
    "Halldor",
    "Hallvard",
    "Halvar",
    "Halvdan",
    "Harald",
    "Havard",
    "Helgi",
    "Hemming",
    "Henrik",
    "Hjalmar",
    "Holger",
    "Hrolf",
    "Inge",
    "Ingimund",
    "Ingvar",
    "Isak",
    "Ivar",
    "Ivarr",
    "Jari",
    "Jarl",
    "Jofrid",
    "Johan",
    "Karl",
    "Ketil",
    "Ketill",
    "Kjartan",
    "Kjell",
    "Knut",
    "Kolbein",
    "Kolli",
    "Lars",
    "Lasse",
    "Leif",
    "Ljot",
    "Loki",
    "Magnar",
    "Magne",
    "Magnus",
    "Malmfrid",
    "Mikkel",
    "Njal",
    "Njord",
    "Njål",
    "Nordal",
    "Odd",
    "Oddbjorn",
    "Oddgeir",
    "Odin",
    "Olaf",
    "Ormr",
    "Orvar",
    "Orvarr",
    "Osvald",
    "Ragnar",
    "Ragnarr",
    "Ragnvald",
    "Rane",
    "Ravn",
    "Reidar",
    "Roald",
    "Rolf",
    "Runar",
    "Sigbjorn",
    "Sigfast",
    "Sigfred",
    "Sigurd",
    "Sigvald",
    "Sigvard",
    "Sigvid",
    "Sivert",
    "Stefan",
    "Stein",
    "Steinar",
    "Sten",
    "Stig",
    "Styr",
    "Styrbiorn",
    "Svein",
    "Sveinn",
    "Sven",
    "Svend",
    "Sverre",
    "Thor",
    "Thorbjorn",
    "Thorbjornr",
    "Thorbjørn",
    "Thorey",
    "Thorleif",
    "Thorvald",
    "Tobias",
    "Torbjorn",
    "Tore",
    "Torfinn",
    "Torger",
    "Torgny",
    "Torkel",
    "Torsten",
    "Trygve",
    "Ulf",
    "Ulfar",
    "Ulfhedin",
    "Ulrik",
    "Ulv",
    "Valdemar",
    "Vidar",
    "Viggo",
    "Viking",
    "Vilhelm",
    "Wilhelm",
    "Yngvar",
    "Yngvarr",
    "Yngve",
    "Åke",
    "Åsgeir",
    "Åsgeirr",
    "Åsmund",
    "Åsmundr",
    "Åsmundur",
    "Åvald",
    "Örjan",
    "Örn",
    "Örnolf",
    "Ørjan",
    "Ørn",
    "Ørnulf",
    "Ørvar",
    "Øystein",
    "Øyvind",
]

female_surnames = [
    "Aesirsdottir",
    "Alvisdottir",
    "Arngrimmsdottir",
    "Asvaldsdottir",
    "Audunsdottir",
    "Bjarnardottir",
    "Bragisdottir",
    "Egilssdottir",
    "Eiriksdottir",
    "Eyvindsdottir",
    "Finnbjarnardottir",
    "Flosadottir",
    "Freysteinsdottir",
    "Geirsdottir",
    "Gisladottir",
    "Grimhildrsdottir",
    "Gudmundsdottir",
    "Gunnarsdottir",
    "Hakonardottir",
    "Halfdanardottir",
    "Hallbergsdottir",
    "Halldorsdottir",
    "Halvdansdottir",
    "Havardsdottir",
    "Helgadottir",
    "Herjolfsdottir",
    "Hognisdottir",
    "Hrolfsdottir",
    "Hunbogadottir",
    "Ingibjorgsdottir",
    "Ingolfsdottir",
    "Jokulsdottir",
    "Ketilsdottir",
    "Kolbeinsdottir",
    "Kormakrsdottir",
    "Leifsdottir",
    "Magnusdottir",
    "Njalsdottir",
    "Oddsdottir",
    "Olafsdottir",
    "Ottarsdottir",
    "Ragnarsdottir",
    "Reynisdottir",
    "Rolfssdottir",
    "Sigmundsdottir",
    "Sigurdsdottir",
    "Skardisdottir",
    "Skarphedinsdottir",
    "Snaedisdottir",
    "Sokkvisdottir",
    "Steinsdottir",
    "Sturlungsdottir",
    "Svavasdottir",
    "Thorbjorgsdottir",
    "Thordissdottir",
    "Thorkelsdottir",
    "Thorleifsdottir",
    "Thormodrsdottir",
    "Thornsdottir",
    "Thorsdottir",
    "Thorvaldsdottir",
    "Torfelsdottir",
    "Torvaldsdottir",
    "Valgardrsdottir",
    "Valgeirsdottir",
    "Vigdisdottir",
    "Vigfusdottir",
    "Viggeirsdottir",
    "Vigiliasdottir",
    "Vigmundsdottir",
    "Vikarsdottir",
    "Vikingrsdottir",
    "Viktoriasdottir",
    "Viktorrsdottir",
    "Vilhjalmrsdottir",
    "Vioarrsdottir",
    "Vordrsdottir",
    "Yngvadottir",
    "Yngvildrsdottir",
    "Yngvisdottir",
    "Yrsadottir",
    "Yrsaelsdottir",
    "Yrungsdottir",
    "Yvaedsdottir",
    "Yvaegisdottir",
    "Yvaegsdottir",
    "Yvaelisdottir",
    "Yvaesnddottir",
    "Yvaesndldottir",
    "Yvaesndnndottir",
    "Yvaesndnrdottir",
    "Yvaesndrdottir",
    "Yvaesndstdottir",
    "Yvaesnndottir",
    "Yvaesnrdottir",
    "Yvaesstdottir",
    "Yvaestdottir",
    "Yvaestldottir",
    "Yvaestndottir",
    "Yvaestrdottir",
    "Yvaetdottir",
    "Yvaethrdottir",
    "Yvaggisdottir",
    "Yvaggisrdottir",
    "Yvagndottir",
    "Yvaiwddottir",
    "Yvaletdottir",
    "Yvalsdottir",
    "Yvawddottir",
    "Yveasandottir",
    "Yveasndottir",
    "Yvedsdottir",
    "Yvessdottir",
    "Yvethsdottir",
    "Yvettesdottir",
    "Yvonnisdottir",
    "Yvorisdottir",
    "Yvundisdottir",
    "Ywainadottir",
    "Ywettesdottir",
    "Ywisdsdottir",
    "Ywishdottir",
]

male_surnames = [
    "Aesirsson",
    "Alfsson",
    "Arnbjornsson",
    "Asgeirsson",
    "Asgotsson",
    "Askellsson",
    "Astridsson",
    "Baldursson",
    "Bjornsson",
    "Dagsson",
    "Egilsson",
    "Einarsson",
    "Eiriksson",
    "Erlendsson",
    "Eyvindsson",
    "Finnsson",
    "Freysson",
    "Gunnarsson",
    "Gunnlaugsson",
    "Guthormsson",
    "Halfdanarson",
    "Halfdansson",
    "Halfreksson",
    "Halvardsson",
    "Haraldsson",
    "Hasteinsson",
    "Hauksson",
    "Helgeirsson",
    "Helgisson",
    "Hemmingsson",
    "Hjalmarsson",
    "Hjortsson",
    "Holmgeirsson",
    "Ingesson",
    "Ivarsson",
    "Jarlsson",
    "Ketilsson",
    "Kolbeinsson",
    "Leifrsson",
    "Magnusson",
    "Njallsson",
    "Odinsson",
    "Olafsson",
    "Ottarsson",
    "Ragnarisson",
    "Ragnarsson",
    "Rolfsson",
    "Siegfriedsson",
    "Sigurdsson",
    "Snorresson",
    "Stefansson",
    "Steinsson",
    "Svennson",
    "Thorbjornsson",
    "Thorfinnsson",
    "Thorgestsson",
    "Thorgilsson",
    "Thorisson",
    "Thorkellsson",
    "Torolfsson",
    "Tryggvason",
    "Ulfarsson",
    "Ulriksson",
    "Valgardsson",
    "Vigfusson",
    "Viggothsson",
    "Vikingsson",
    "Vilhjalmsson",
    "Yngvarsson",
    "Yngvason",
    "Yngvesson",
    "Yrsaardsson",
    "Yrthardsson",
    "Yrvingsson",
    "Ysbrandsson",
    "Ysgrimsson",
    "Ysmundsson",
    "Ysriksson",
    "Ysulfsson",
    "Yvarsson",
    "Yvarthsson",
    "Yvborgsson",
    "Yvdorsson",
    "Yveriksson",
    "Yvfinnsson",
    "Yvfinsson",
    "Yvfrostsson",
    "Yvgardsson",
    "Yvgarthsson",
    "Yvgeirsson",
    "Yvggvinsson",
    "Yvgiannsson",
    "Yvgilmundsson",
    "Yvgjaldsson",
    "Yvgmundsson",
    "Yvgormsson",
    "Yvgrimmsson",
    "Yvgrimsson",
    "Yvhallsson",
    "Yvhildsson",
    "Yvindsson",
    "Yviriksson",
    "Yvjarthsson",
    "Yvkarsson",
    "Yvkeirsson",
    "Yvkelsson",
    "Yvlafsson",
    "Yvmarsson",
    "Yvmirsson",
    "Yvmundsson",
    "Yvnarsson",
    "Yvneriksson",
    "Yvngirsson",
    "Yvnilsson",
    "Yvningsson",
    "Yvnoriksson",
    "Yvnyrdsson",
    "Yvolgsson",
    "Yvonarsson",
    "Yvoresson",
    "Yvoriksson",
    "Yvormundsson",
    "Yvrageirsson",
    "Yvraldsson",
    "Yvreksson",
    "Yvrikksson",
    "Yvriksson",
    "Yvrimsson",
    "Yvroddsson",
    "Yvroldsson",
    "Yvsarsson",
    "Yvsbornsson",
    "Yvsdottir",
    "Yvseliasson",
    "Yvseriksson",
    "Yvsfredsson",
    "Yvsgeirsson",
    "Yvsgerdsson",
    "Yvsgrimsson",
    "Yvssifsson",
    "Yvsson",
    "Yvstafsson",
    "Yvsteinnsson",
    "Yvsursson",
    "Yvsvaldsson",
    "Yvthorisson",
    "Yvthorsson",
    "Yvtliasson",
    "Yvtrafsson",
    "Yvulfsson",
    "Yvulsson",
    "Yvulviksson",
    "Yvunsson",
    "Yvuriksson",
    "Yvwaldsson",
    "Yvythorsson",
]

female = generate_female_name(female_prefix, female_suffix, min=1, max=1)
male = generate_male_name(male_prefix, male_suffix, min=1, max=1)
surname = generate_surname_less(surname_prefix, surname_suffix)

female_lbr = choice(female_names)
male_lbr = choice(male_names)
female_surname_lbr = choice(female_surnames)
male_surname_lbr = choice(male_surnames)
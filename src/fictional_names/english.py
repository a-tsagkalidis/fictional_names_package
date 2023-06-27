from random import choice


female_names = [
    "Abigail",
    "Addison",
    "Adeline",
    "Alice",
    "Amelia",
    "Anna",
    "Aria",
    "Aubrey",
    "Audrey",
    "Aurora",
    "Autumn",
    "Ava",
    "Avery",
    "Bella",
    "Brooklyn",
    "Camila",
    "Caroline",
    "Charlotte",
    "Chloe",
    "Claire",
    "Clara",
    "Eleanor",
    "Elena",
    "Eliana",
    "Elizabeth",
    "Ella",
    "Ellie",
    "Emilia",
    "Emily",
    "Emma",
    "Eva",
    "Evelyn",
    "Everly",
    "Gabriella",
    "Gianna",
    "Grace",
    "Hadley",
    "Hannah",
    "Harper",
    "Hazel",
    "Isabella",
    "Isla",
    "Ivy",
    "Kinsley",
    "Layla",
    "Leah",
    "Lillian",
    "Lily",
    "Lucy",
    "Luna",
    "Lyla",
    "Madison",
    "Maya",
    "Mia",
    "Mila",
    "Natalie",
    "Nora",
    "Nova",
    "Olivia",
    "Paisley",
    "Penelope",
    "Quinn",
    "Reagan",
    "Riley",
    "Ruby",
    "Samantha",
    "Savannah",
    "Scarlett",
    "Skylar",
    "Sofia",
    "Sophia",
    "Stella",
    "Valentina",
    "Victoria",
    "Violet",
    "Vivian",
    "Zoe",
    "Zoey",
]

male_names = [
    "Aaron",
    "Adam",
    "Adrian",
    "Aiden",
    "Alexander",
    "Andrew",
    "Anthony",
    "Asher",
    "Benjamin",
    "Bryson",
    "Caleb",
    "Carter",
    "Charles",
    "Christopher",
    "Cole",
    "Cooper",
    "Damian",
    "Daniel",
    "David",
    "Dylan",
    "Edward",
    "Eli",
    "Elijah",
    "Ethan",
    "Ezra",
    "Gabriel",
    "Grayson",
    "Henry",
    "Hudson",
    "Hunter",
    "Ian",
    "Isaac",
    "Isaiah",
    "Jack",
    "Jackson",
    "Jacob",
    "James",
    "Jaxon",
    "Jayden",
    "John",
    "Jordan",
    "Joseph",
    "Joshua",
    "Josiah",
    "Julian",
    "Leo",
    "Levi",
    "Liam",
    "Lincoln",
    "Logan",
    "Lucas",
    "Luke",
    "Mason",
    "Mateo",
    "Matthew",
    "Micah",
    "Michael",
    "Miles",
    "Nathan",
    "Noah",
    "Nolan",
    "Oliver",
    "Owen",
    "Ryan",
    "Samuel",
    "Sebastian",
    "Theodore",
    "Thomas",
    "Weston",
    "William",
    "Wyatt",
    "Xavier",
]

surnames = [
    "Abbott",
    "Adams",
    "Adkins",
    "Aguilar",
    "Alexander",
    "Allen",
    "Alvarado",
    "Alvarez",
    "Anderson",
    "Andrews",
    "Armstrong",
    "Arnold",
    "Austin",
    "Avila",
    "Bailey",
    "Baker",
    "Baldwin",
    "Ball",
    "Ballard",
    "Banks",
    "Barber",
    "Barker",
    "Barnes",
    "Barnett",
    "Barrett",
    "Bass",
    "Bates",
    "Beard",
    "Beck",
    "Becker",
    "Bell",
    "Bennett",
    "Benson",
    "Berry",
    "Bishop",
    "Black",
    "Blair",
    "Blake",
    "Bowen",
    "Bowman",
    "Boyd",
    "Bradley",
    "Brady",
    "Brewer",
    "Briggs",
    "Brock",
    "Brooks",
    "Brown",
    "Bryant",
    "Buchanan",
    "Burgess",
    "Burke",
    "Burns",
    "Burton",
    "Bush",
    "Butler",
    "Byrd",
    "Caldwell",
    "Campbell",
    "Cannon",
    "Carlson",
    "Carpenter",
    "Carr",
    "Carroll",
    "Carter",
    "Castillo",
    "Castro",
    "Chambers",
    "Chandler",
    "Chapman",
    "Chavez",
    "Christensen",
    "Clark",
    "Clayton",
    "Cobb",
    "Cohen",
    "Cole",
    "Coleman",
    "Collins",
    "Colon",
    "Conner",
    "Cook",
    "Cooper",
    "Copeland",
    "Cox",
    "Craig",
    "Crawford",
    "Cross",
    "Cummings",
    "Cunningham",
    "Curry",
    "Curtis",
    "Dalton",
    "Daniel",
    "Daniels",
    "Davidson",
    "Davis",
    "Dawson",
    "Day",
    "Dean",
    "Delgado",
    "Dennis",
    "Diaz",
    "Dixon",
    "Douglas",
    "Doyle",
    "Drake",
    "Duncan",
    "Dunn",
    "Edwards",
    "Elliott",
    "Erickson",
    "Estrada",
    "Evans",
    "Farmer",
    "Ferguson",
    "Fernandez",
    "Fields",
    "Figures",
    "Fitzgerald",
    "Fleming",
    "Fletcher",
    "Flores",
    "Flowers",
    "Floyd",
    "Foster",
    "Fowler",
    "Fox",
    "Francis",
    "Frank",
    "Franklin",
    "Frazier",
    "Freeman",
    "French",
    "Fuller",
    "Garcia",
    "Gardner",
    "Garner",
    "Garrett",
    "Garza",
    "George",
    "Gibbs",
    "Gilbert",
    "Gill",
    "Glover",
    "Gonzales",
    "Gonzalez",
    "Goodman",
    "Goodwin",
    "Gordon",
    "Grant",
    "Graves",
    "Gray",
    "Green",
    "Greene",
    "Greer",
    "Gregory",
    "Griffin",
    "Griffith",
    "Gross",
    "Guerrero",
    "Gutierrez",
    "Guzman",
    "Hale",
    "Hall",
    "Hammond",
    "Hampton",
    "Hansen",
    "Hanson",
    "Hardy",
    "Harmon",
    "Harper",
    "Harris",
    "Hart",
    "Harvey",
    "Hawkins",
    "Hayes",
    "Haynes",
    "Henderson",
    "Henry",
    "Hernandez",
    "Herrera",
    "Hicks",
    "Higgins",
    "Hill",
    "Hines",
    "Hodges",
    "Hoffman",
    "Holland",
    "Holloway",
    "Holmes",
    "Holt",
    "Hopkins",
    "Horton",
    "Houston",
    "Howard",
    "Howell",
    "Hubbard",
    "Hudson",
    "Huff",
    "Hughes",
    "Hunt",
    "Hunter",
    "Ingram",
    "Jackson",
    "Jacobs",
    "James",
    "Jefferson",
    "Jenkins",
    "Jennings",
    "Jensen",
    "Jimenez",
    "Johnson",
    "Johnston",
    "Jones",
    "Joseph",
    "Keller",
    "Kelley",
    "Kelly",
    "Kennedy",
    "Kim",
    "King",
    "Klein",
    "Knight",
    "Lambert",
    "Lane",
    "Larson",
    "Lawrence",
    "Lawson",
    "Lee",
    "Leonard",
    "Lewis",
    "Lindsey",
    "Little",
    "Lloyd",
    "Logan",
    "Long",
    "Lopez",
    "Love",
    "Lowe",
    "Lucas",
    "Lynch",
    "Lyons",
    "Mack",
    "Maldonado",
    "Malone",
    "Mann",
    "Manning",
    "Marsh",
    "Martin",
    "Martinez",
    "Mason",
    "Massey",
    "Matthews",
    "Maxwell",
    "May",
    "Mcbride",
    "Mccarthy",
    "Mccormick",
    "Mccoy",
    "Mcdaniel",
    "Mcgee",
    "Mckinney",
    "Mclaughlin",
    "Medina",
    "Mendez",
    "Mendoza",
    "Meyer",
    "Miles",
    "Miller",
    "Mills",
    "Mitchell",
    "Montgomery",
    "Moody",
    "Moore",
    "Morales",
    "Moran",
    "Moreno",
    "Morgan",
    "Morris",
    "Morrison",
    "Morton",
    "Moss",
    "Mullins",
    "Munoz",
    "Murphy",
    "Murray",
    "Neal",
    "Nelson",
    "Newman",
    "Newton",
    "Nguyen",
    "Nichols",
    "Norman",
    "Norris",
    "Norton",
    "Nunez",
    "Obrien",
    "Oliver",
    "Olson",
    "Ortega",
    "Osborne",
    "Owen",
    "Padilla",
    "Page",
    "Palmer",
    "Park",
    "Parker",
    "Parks",
    "Parsons",
    "Patrick",
    "Patterson",
    "Patton",
    "Paul",
    "Payne",
    "Pearson",
    "Pena",
    "Perez",
    "Perkins",
    "Perry",
    "Peters",
    "Peterson",
    "Phillips",
    "Pierce",
    "Pittman",
    "Poole",
    "Pope",
    "Porter",
    "Potter",
    "Powell",
    "Powers",
    "Pratt",
    "Price",
    "Quinn",
    "Ramirez",
    "Ramos",
    "Ramsey",
    "Ray",
    "Reed",
    "Reese",
    "Reeves",
    "Reid",
    "Reyes",
    "Reynolds",
    "Rhodes",
    "Rice",
    "Richards",
    "Richardson",
    "Riley",
    "Rios",
    "Robbins",
    "Roberts",
    "Robertson",
    "Robinson",
    "Robles",
    "Rodgers",
    "Rodriguez",
    "Rodriquez",
    "Rogers",
    "Romero",
    "Rose",
    "Ross",
    "Rowe",
    "Roy",
    "Ruiz",
    "Russell",
    "Ryan",
    "Salazar",
    "Sanchez",
    "Sanders",
    "Sandoval",
    "Santiago",
    "Santos",
    "Saunders",
    "Schmidt",
    "Schneider",
    "Schultz",
    "Schwartz",
    "Scott",
    "Sharp",
    "Shaw",
    "Shelton",
    "Sherman",
    "Silva",
    "Simmons",
    "Simon",
    "Simpson",
    "Sims",
    "Smith",
    "Snyder",
    "Soto",
    "Sparks",
    "Spencer",
    "Stanley",
    "Steele",
    "Stephens",
    "Stevens",
    "Stevenson",
    "Stewart",
    "Stokes",
    "Stone",
    "Strickland",
    "Sutton",
    "Swanson",
    "Tate",
    "Taylor",
    "Terry",
    "Thomas",
    "Thompson",
    "Thornton",
    "Todd",
    "Torres",
    "Townsend",
    "Tucker",
    "Turner",
    "Tyler",
    "Valdez",
    "Vance",
    "Vargas",
    "Vasquez",
    "Vaughn",
    "Vega",
    "Wade",
    "Wagner",
    "Walker",
    "Walsh",
    "Walters",
    "Walton",
    "Ward",
    "Warner",
    "Warren",
    "Washington",
    "Waters",
    "Watkins",
    "Watson",
    "Watts",
    "Weaver",
    "Webb",
    "Weber",
    "Webster",
    "Welch",
    "Wells",
    "Wheeler",
    "White",
    "Williams",
    "Williamson",
    "Willis",
    "Wilson",
    "Wise",
    "Wolfe",
    "Wong",
    "Wood",
    "Wright",
    "Yates",
    "Young",
    "Zimmerman",
]

female_names_lbr = [
    "Ada",
    "Aelfgifu",
    "Aelfwynn",
    "Aethelflaed",
    "Aethelthryth",
    "Ailith",
    "Aislinn",
    "Alfgifu",
    "Althryth",
    "Alys",
    "Amina",
    "Anastasia",
    "Anwen",
    "Astrid",
    "Avelina",
    "Beatrix",
    "Benedicta",
    "Blanchefleur",
    "Bridget",
    "Catherine",
    "Cecily",
    "Clarice",
    "Cynethryth",
    "Diana",
    "Eadgyth",
    "Ealhswith",
    "Eanswith",
    "Edith",
    "Edyth",
    "Eleanor",
    "Elfleda",
    "Elfthryth",
    "Elgifu",
    "Elizabeth",
    "Emma",
    "Emmeline",
    "Enfleda",
    "Estrid",
    "Ethelfleda",
    "Eva",
    "Felicia",
    "Flora",
    "Freya",
    "Gisela",
    "Godiva",
    "Gormlaith",
    "Gundred",
    "Gwenllian",
    "Gwladys",
    "Gytha",
    "Hedwig",
    "Helena",
    "Hephzibah",
    "Herleva",
    "Hilda",
    "Hildegard",
    "Ida",
    "Isolde",
    "Iveta",
    "Joan",
    "Juliana",
    "Katherine",
    "Kensa",
    "Layla",
    "Leofgifu",
    "Leofwynn",
    "Leofytha",
    "Leonora",
    "Lilith",
    "Margaret",
    "Matilda",
    "Maud",
    "Millicent",
    "Morwenna",
    "Nesta",
    "Oda",
    "Odelina",
    "Olwen",
    "Osburga",
    "Osthryth",
    "Parnel",
    "Phyllis",
    "Ragnhild",
    "Rhiannon",
    "Rosamund",
    "Rowena",
    "Sabina",
    "Saffira",
    "Serena",
    "Sigrid",
    "Sybil",
    "Tatiana",
    "Thora",
    "Ursula",
    "Vigdis",
    "Winifred",
    "Wulfhilda",
    "Wulfwynn",
    "Ygraine",
    "Yseult",
    "Zenobia",
    "Zillah",
    "Zoe",
    "Zosia",
    "Zuleika",
    "Zuriel",
    "Zyanya",
    "Zyra",
]

male_names_lbr = [
    "Aethelwulf",
    "Alfred",
    "Aelfric",
    "Aelfstan",
    "Aelfwine",
    "Aethelbald",
    "Aethelbert",
    "Aethelred",
    "Aethelstan",
    "Aethelwold",
    "Aldhelm",
    "Beornheard",
    "Beornwulf",
    "Beowulf",
    "Brihtnoth",
    "Ceolwulf",
    "Cerdic",
    "Cuthbert",
    "Cynewulf",
    "Eadberht",
    "Eadfrith",
    "Eadgar",
    "Eadmund",
    "Eadred",
    "Eadric",
    "Eadweard",
    "Eadwig",
    "Ealdred",
    "Ealdwulf",
    "Eanflaed",
    "Eanred",
    "Ecgberht",
    "Ecgfrith",
    "Ecgwulf",
    "Edgar",
    "Edmund",
    "Edred",
    "Edric",
    "Edward",
    "Edwin",
    "Egbert",
    "Elfhere",
    "Elfric",
    "Ethelbert",
    "Ethelred",
    "Ethelstan",
    "Ethelwald",
    "Godfrey",
    "Godric",
    "Godwin",
    "Harold",
    "Hereward",
    "Hildred",
    "Hrothgar",
    "Leofric",
    "Leofwine",
    "Leofwulf",
    "Offa",
    "Osgood",
    "Oswald",
    "Oswin",
    "Oswulf",
    "Radulf",
    "Ragnald",
    "Siward",
    "Theobald",
    "Thurstan",
    "Wulfhere",
    "Wulfric",
    "Wulfstan",
    "Wulfrun",
    "Wulfweard",
    "Aldred",
    "Aldwin",
    "Aldwyn",
    "Alfgar",
    "Alfric",
    "Algar",
    "Alric",
    "Alwin",
    "Anselm",
    "Ansgar",
    "Anson",
    "Arnulf",
    "Athelstan",
    "Aubrey",
    "Baldric",
    "Baldwin",
    "Benedict",
    "Bernard",
    "Bertram",
    "Bertrand",
    "Bran",
    "Bruno",
    "Clement",
    "Conrad",
    "Cuthred",
    "Cwenbeorht",
    "Dagobert",
    "Dunstan",
    "Eadbald",
    "Eadberht",
    "Eadfrid",
    "Eadgar",
    "Eadmund",
    "Eadric",
    "Eadweard",
    "Eadwulf",
    "Ealdfrith",
    "Ealdhelm",
    "Ealdred",
    "Eanbald",
    "Eanfled",
    "Eardwulf",
    "Earnwulf",
    "Ecgbert",
    "Edgar",
    "Edmund",
    "Edred",
    "Edward",
    "Edwin",
    "Egfrid",
    "Elfric",
    "Elfstan",
    "Elfwine",
    "Ethelbald",
    "Ethelbert",
    "Ethelred",
    "Ethelstan",
    "Ethelwald",
    "Frederick",
    "Geoffrey",
    "Godric",
    "Godwin",
    "Gundulf",
    "Helmstan",
    "Hereward",
    "Herfrid",
    "Higbald",
    "Hildbrand",
    "Hrothbert",
    "Hunberht",
    "Hygbald",
    "Kenelm",
    "Leofgar",
    "Leofric",
    "Leofwine",
    "Leofwulf",
    "Ludwig",
    "Oswald",
    "Oswin",
    "Oswulf",
    "Radulf",
    "Ralph",
    "Randolph",
    "Reynard",
    "Richard",
    "Robert",
    "Rodbert",
    "Sebastian",
    "Sigfrid",
    "Sigurd",
    "Swain",
    "Thurstan",
    "Tobias",
    "Ulric",
    "Waldred",
    "Walfrid",
    "Waldric",
    "Wido",
    "Wigmund",
    "Wigstan",
    "Wilfrid",
    "Wilibald",
    "William",
    "Wilmot",
    "Winfred",
    "Winfrith",
    "Winston",
    "Wulfhere",
]

surnames_lbr = [
    "Abbey",
    "Alden",
    "Ashby",
    "Bancroft",
    "Barlow",
    "Beaumont",
    "Bingham",
    "Birch",
    "Blackwood",
    "Blakely",
    "Bramley",
    "Briarwood",
    "Brockley",
    "Burrows",
    "Chadwick",
    "Chalmers",
    "Clayton",
    "Cromwell",
    "Davenport",
    "Dunstan",
    "Eastwood",
    "Fairchild",
    "Falkner",
    "Farley",
    "Fletcher",
    "Gainsborough",
    "Gardner",
    "Gilbert",
    "Granger",
    "Hadley",
    "Hawthorne",
    "Hayward",
    "Hemsworth",
    "Hensley",
    "Hollis",
    "Huntington",
    "Ingram",
    "Jefferson",
    "Kensington",
    "Kingsley",
    "Langley",
    "Larkspur",
    "Lockwood",
    "Manning",
    "Marlowe",
    "Montgomery",
    "Moss",
    "Norwood",
    "Oswald",
    "Pembroke",
    "Preston",
    "Radcliffe",
    "Rutherford",
    "Salisbury",
    "Sheffield",
    "Sherwood",
    "Stanford",
    "Sutton",
    "Tennyson",
    "Thackeray",
    "Thornton",
    "Tilden",
    "Underwood",
    "Walden",
    "Warren",
    "Wellington",
    "Westbrook",
    "Whitaker",
    "Wickham",
    "Willoughby",
    "Winchester",
    "Woodcroft",
    "Wycliffe",
    "Yardley",
    "Abbott",
    "Ainsworth",
    "Archer",
    "Atwood",
    "Baker",
    "Barton",
    "Bennett",
    "Bolton",
    "Bradford",
    "Brewster",
    "Bridges",
    "Buckley",
    "Burton",
    "Chandler",
    "Clarke",
    "Cooper",
    "Cunningham",
    "Darby",
    "Dawson",
    "Delaney",
    "Dixon",
    "Eaton",
    "Fisher",
    "Foster",
    "Gibson",
    "Graham",
    "Hammond",
    "Harrison",
    "Hawkins",
    "Hilton",
    "Hudson",
    "Jackson",
    "Kendall",
    "Knight",
    "Lawson",
    "Mackenzie",
    "Miller",
    "Nelson",
    "Oliver",
    "Palmer",
    "Parker",
    "Potter",
    "Reynolds",
    "Roberts",
    "Rowland",
    "Scott",
    "Shelley",
    "Sinclair",
    "Spencer",
    "Stone",
    "Sullivan",
    "Taylor",
    "Walker",
    "Webster",
    "Wheeler",
    "Wilson",
    "Wright",
    "Young",
    "Ashton",
    "Banks",
    "Beckett",
    "Bolton",
    "Bowers",
    "Brady",
    "Brock",
    "Butler",
    "Carter",
    "Coleman",
    "Conway",
    "Crawford",
    "Crosby",
    "Dalton",
    "Daniels",
    "Darcy",
    "Davenport",
    "Dawson",
    "Devereux",
    "Drake",
    "Dunn",
    "Edwards",
    "Ellis",
    "Fletcher",
    "Francis",
    "Garner",
    "Griffiths",
    "Hamilton",
    "Harper",
    "Hayes",
    "Holland",
    "Hopkins",
    "Hughes",
    "Hutchinson",
    "Jackson",
    "Jordan",
    "Kingsley",
    "Lawrence",
    "Lloyd",
    "Mason",
    "Maynard",
    "Morrison",
    "Newton",
    "Nicholson",
    "O'Connor",
    "Perry",
    "Porter",
    "Quinn",
    "Reeves",
    "Rice",
    "Robinson",
    "Sawyer",
    "Shaw",
    "Simmons",
    "Stewart",
    "Sullivan",
    "Tate",
    "Thompson",
    "Turner",
    "Wade",
    "Watkins",
]

female = choice(female_names)
male = choice(male_names)
surname = choice(surnames)

female_lbr = choice(female_names_lbr)
male_lbr = choice(male_names_lbr)
surname_lbr = choice(surnames_lbr)
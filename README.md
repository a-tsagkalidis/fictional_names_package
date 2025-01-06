# Fictional Names

[![PyPI version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&r=r&ts=1683906897&type=6e&v=1.0.0&x2=0)](https://pypi.org/project/fictional-names/)

A Python package for generating fictional names for characters in your fantasy stories, Dungeons & Dragons, RPGs, or whatever else you need them for.

## Installation

```bash
python3 -m pip install fictional_names
```
## Usage

The generate_name function is the main function of the package, and it can be used in a variety of ways, by passing different arguments to it. It takes the following arguments: `gender`, `style`, and `library`.

**`gender`** can be either `'male'` or`'female'`. Leave it blank if you want random gender.

**`style`** can be any of the following: `'arab'`, `'aztec'`, `'chinese'`, `'dragonborn'`, `'drow'`, `'dwarven'`, `'elven'`, `'english'`, `'eriskon'`, `'germanic'`, `'giant'`, `'gnomish'`, `'greek'`, `'halfling'`, `'human'`, `'japanese'`, `'jordan'`, `'martin'`, `'mongolian'`, `'norsemen'`, `'orc'`, `'roman'`, `'rowling'`, `'sapkowski'`, `'slavic'`, `'steampunk'`, `'tolkien'`, `'turkish'`, or `'viking'`. Leave it blank if you want a random style.

**Most styles are obvious, but some of them are named after famous authors, and some of them are named after famous fantasy races.*

**`library`** can be either `True` or `False`. Leave it blank and it's randomly picked. 

*`True` *libraries are used to generate solid names that resembling real names, or names that is more likely to have been used in books, movies, or TV shows.* `False` *libraries are used to generate more unique names as they are compounded by random syllables, related to the* `style`.

## Importing the package
```python
from fictional_names import name_generator
names = name_generator.generate_name
```

What it follows is a list of examples of how to use the function, and what you can expect to get from it.

## Completely random names
```python
names()
# Probable generated names: 'Eleanor Neumann', 'Nathaniel Eberhardt', 'Yolotzintli (Ethereal Mist)', 'Isabeau of Rhovanion', 'Barthanes al'Tealdar', 'Arabella Bryce', 'Sicilia Lucretillus', 'Orggol the Ruiner', 'Bolbo Honeydew', 'Gerda Einarsdottir', 'Ganoes Untor'
```

## Human names from different cultures
```python
names(style='english')
# Probable generated names: 'Aaron Mckinney', 'Edmund Sheffield', 'Beatrix Moss'

names(style='arab')
# Probable generated names: 'Youssef Shihab', 'Yasmin Fadel', 'Saeed Nader'

names(style='chinese')
# Probable generated names: 'Xiulan Tang', 'Guo Qing', 'Mei Chi'

names(style='germanic')
# Probable generated names: 'Dankrich Vogelweber', 'Folker Holz', 'Siegfried Wiedemann'

names(style='japanese')
# Probable generated names: 'Yumiko Yoshikawa', 'Naoki Yamamoto', 'Ryozo Nagano'

names(style='slavic')
# Probable generated names: 'Valentin Marinov', 'Pavelv Borenko', 'Zina Kovačević'
```
## Human names from lost civilizations
```python
names(style='aztec')
# Probable generated names: 'Miquiztli (Lorekeeper)', 'Huexotzinco (Silver Mist)', 'Callitli Tlanitl'

names(style='greek', library=True)
# Probable generated names: 'Demosthenes of Kydonia', 'Adrastos of Apollonia', 'Kallisto of Larissa'

names(style='roman')
# Probable generated names: 'Faucia Vitruvius', 'Atia Tiberius', 'Aventinus Calpurnius'

names(style='viking')
# Probable generated names: 'Ørvar Yvngirsson', 'Livþora Jarmann', 'Siggyða Norrav'
```

## Fantasy names based on Dungeons & Dragons and other TTRPGs
```python
names(gender='male', style='dwarven', library=False)
# Probable generated names: 'Kazdin Voldurmir', 'Thunûr Kinmarmak', 'Dorgǎrn Bǎlthrak'

names(gender='female', style='elven', library=True)
# Probable generated names: 'Galadhrim Narothor', 'Narwindë Ardalas', 'Ermalinde Nimrith'

names(style='halfling', library=True)
# Probable generated names: 'Lyric Tricklebrook', 'Nibs Cobblehill', 'Sylvia Wildflower'

names(gender='male', style='human', library=True)
# Probable generated names: 'Leander Hecht', 'Jasper Hahn', 'Galahad Thiele'

names(gender='male', style='orc', library=True)
# Probable generated names: 'Snagrag the Desecrator', 'Bolgrag the Crazed', 'Thak the Deathbringer'

names(gender='female', style='steampunk', library=True)
# Probable generated names: 'Dorothea Finnigan', 'Bernadette Baron', 'Mathilda Tarleton'
```

## Human names based on famous authors works
```python
names(gender='male', style='tolkien', library=True)
# Probable generated names: 'Saradoc of Bree', 'Eldric of Rohan', 'Hilbert of Dol Guldur'

names(style='martin', library=False)
# Probable generated names: 'Bran Conford', 'Toras Belton', 'Sen Berdon'

names(gender='female', style='rowling', library=False)
# Probable generated names: 'Sega Ryddle', 'Alda Glanvill', 'Kiola Graham'
```

## Printing the name
You can print the name directly from the function, or you can store it in a variable and print it later.
```python
print(names())
```
or
```python
name = names()
print(name)
```
<style>
    .reveal section p {
    display: inline-block;
    font-size: 0.8em;
    line-height: 1.2em;
    vertical-align: top;
  }
  .reveal th, .reveal td {
    font-size: 0.5em;
  }
  .reveal li, .reveal ul, .reveal ol {
    font-size: 0.8em
  }
</style> 
---
# pandoc -s --mathjax -t revealjs start.md -o start.html --slide-level=2 --embed-resources --standalone
title: Python
author: Søren Magnusson, TEC
date: Februar 2023
theme: white
slide-level: 2 
...

_-- et valgfag på TEC_

# Python

Med fokus på datastrukturer

. . . 

men hvad mener jeg med datastrukturer?

## Datastrukturer er

- lister `[1,2,'tre', ...]`
- tupler `(1,2,'tre')`
- dictionaries `{key1: value1, 'key2': 'value2'}`
- mængder `set`

## og - i høj grad - kombinationer af disse

- Lister af dicts
- Dicts med lister
- Lister af lister af dicts med lister

# Men Aller-Først, 

__*installering*__

## python.org

Download seneste version

![python.org](assets/2023-02-05-23-26-28.png)

---

Check "`Add python.exe to PATH`"  
Og vælg "`Customize installation`"

![installer 1](assets/2023-04-24-18-04-48.png)

---

Vælg alt  
og tryk "`Next`"

![installer 2](assets/2023-04-24-18-06-14.png)


---

Check "`Install Python 3-11 for all users`"  
og tryk på "`Install`"-

![installer 3](assets/2023-04-24-18-07-27.png)

---

vent...  

![installer 4](assets/2023-04-24-18-08-31.png)


# Editor miljø

Man kan f.eks. vælge et af følgende, men der da også andre:

  1. ![vc logo](assets/2023-04-24-13-44-59-75xauto.png) VisualStudio Code [_Min favorit_]
  1. ![pyChsrm logo](assets/2023-04-24-13-44-28-75xauto.png) PyCharm
  1. ![idle logo](assets/2023-04-24-13-46-05-75xauto.png) Idle ("indbygget")

## VS Code extensions

![vs code with python extensions](assets/2023-04-24-17-53-40.png)

## python miljø

* Alle filer med `.py` er python filer
* Der er syntaks highlight og syntaks check med pylance
* Python scriptet udføres med at trykke på trekanten/pilen øverst til højre
* output fra print kommer i konsol panelet
* Man kan vælge fortolker-opsætning (hvis man har flere), nederst til højre

![](assets/2023-04-24-18-43-44-autox400.png)

# Opgaver

## Kildekode til opgaver, med git

* bliv meldt ind, i lærerens github team
  * Hvad er dit brugernavn på github?
* lav en `fork` af https://github.com/TEC-Prog-Stud/PythonData-1
* lav en klon på din computer
  * `git clone https://github.com/<dit-brugernavn ... nej ikke "dit-brugernavn" ... >/PythonData-1`

# Og så i gang...
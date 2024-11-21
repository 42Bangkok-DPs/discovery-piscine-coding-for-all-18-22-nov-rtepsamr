#!/usr/bin/env python3
def famous_births(scientists_data):
    export_data = [f"{name} is a great scientist born in {date_of_birth}" for name, date_of_birth in women_scientists.item()]
    return print(export_data)
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
DOMAIN = "pollenflug_bayern"
PLATFORMS = ["sensor"]

# Mapping der wissenschaftlichen Namen der API zu den deutschen Namen
POLLEN_MAPPING = {
    "Abies": "Tanne",
    "Acer": "Ahorn",
    "Aesculus": "Rosskastanie",
    "Alnus": "Erle",
    "Ambrosia": "Ambrosia",
    "Artemisia": "Beifuß",
    "Asteraceae": "Korbblütler",
    "Betula": "Birke",
    "Carpinus": "Hainbuche",
    "Castanea": "Kastanie",
    "Chenopodium": "Gänsefuß",
    "Corylus": "Hasel",
    "Cruciferae": "Kreuzblütler",
    "Cyperaceae": "Sauergrasgewächse",
    "Erica": "Heidekraut",
    "Fagus": "Buche",
    "Fraxinus": "Esche",
    "Fungus": "Pilzsporen",
    "Galium": "Labkraut",
    "Humulus": "Hopfen",
    "Impatiens": "Springkraut",
    "Juglans": "Walnuss",
    "Larix": "Lärche",
    "Picea": "Fichte",
    "Pinaceae": "Kieferngewächse",
    "Pinus": "Kiefer",
    "Plantago": "Wegerich",
    "Platanus": "Platane",
    "Poaceae": "Gräser",
    "Populus": "Pappel",
    "Quercus": "Eiche",
    "Quercus ilex": "Steineiche",
    "Rumex": "Ampfer",
    "Salix": "Weide",
    "Sambucus": "Holunder",
    "Secale": "Roggen",
    "Taxus": "Eibe",
    "Tilia": "Linde",
    "Ulmus": "Ulme",
    "Urtica": "Brennnessel",
    "Varia": "Sonstige"
}

# Wir extrahieren die API-Schlüssel für unsere bestehende Logik
SENSOR_TYPES = list(POLLEN_MAPPING.keys())

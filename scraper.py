import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fr.wikipedia.org/wiki/Liste_des_langages_de_programmation"
response = requests.get(url)
if response.status_code != 200:
    print("Erreur lors du chargement de la page")
    exit()

soup = BeautifulSoup(response.text, "lxml")

# Récupération de tous les éléments <li> dans la section du contenu principal
content = soup.find("div", {"id": "mw-content-text"})
items = content.find_all("li")

langages = []
for li in items:
    a_tag = li.find("a")
    if a_tag and "/wiki/" in a_tag.get("href", ""):
        texte = a_tag.text.strip()
        if texte and texte not in langages and not texte.startswith("Liste"):
            langages.append(texte)

# Nettoyage possible : retirer les entrées comme "Langage (informatique)"
langages = [l for l in langages if len(l) > 1 and not l.startswith("Portail")]

# Export
df = pd.DataFrame(langages, columns=["Langage"])
df.to_csv("data.csv", index=False, encoding="utf-8")

print("Fichier 'data.csv' généré avec", len(df), "langages.")


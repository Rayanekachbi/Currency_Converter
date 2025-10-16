"""
Currency Converter Script
-------------------------
Convertit un montant d'une devise à une autre à l'aide de l'API ExchangeRate.
Utilise un cache local pour limiter les appels à l'API (valide 30 min).
"""

import requests
import argparse
import os
import json
from datetime import datetime

API_KEY = 'your api key'

def get_taux_change(source):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source}"
    try:
        g = requests.get(url, timeout=5)
        g.raise_for_status()
        data = g.json()
        return data #on renvoi tout le disctionnaire json
    
    except requests.ConnectionError:
        print("Erreur de réseau : impossible de joindre l'API")
        #par defaut ça return None quand on écrit rien
    except requests.Timeout:
        print("Erreur : délai de connextion dépassé")
    except requests.RequestException as e:
        print("Erreur lors de la rêquete : ", e)


def main():
    #créer le parseur
    parser = argparse.ArgumentParser(description="Convertisseur de devises")
    
    #définir les arguments
    parser.add_argument("--amount", type=float, help="montant à convertir")
    parser.add_argument("--from", dest="source", type = str, help = "devise source, ex: USD")
    parser.add_argument("--to", dest="cible", type = str, help = "devise cible, ex: EUR")

    #lire les arguments
    args = parser.parse_args()
    
    #utiliser les valeurs ou fallback en mode input
    if args.amount and args.source and args.cible:
        montant = args.amount
        source = args.source.upper()
        cible = args.cible.upper()
    else:
        while True:
            try:
                montant = float(input("rentrez le montant :"))
                break
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide,")
        #float("abc") lève une exception ValueError, le code passe directement dans le bloc except
        #et la boucle continue

        while True:
            source = input("devise de départ : ").strip().upper()
            if source and len(source) == 3:
                break
            print("Erreur : vous devez entrer une devise valide")
        #.strip() enlève les espaces au début et à la fin, .upper() met tout en majuscules.

        while True:
            cible = input("devise de conversion : ").strip().upper()
            if cible and len(cible) == 3:
                break
            print("Erruer : vous devez entrer une devise valide")


        
    if source == cible:
        print(f"Vous avez choisis la même devise donc le montant reste le même : {montant}{source}")
    else:
        maintenant = datetime.now()
        #si je met .isoformat() ça donne une chaîne du style "2025-10-07T18:40:23.234Z" 
        #sinon c'est du type datetime et on peut faire des soustractions
        fichier_cache = "cache.json"
        if not os.path.exists(fichier_cache):
            print("pas de cache trouvé, appel à l'API")
            data = get_taux_change(source)
            cache = {
                "temps": maintenant.isoformat(),
                "source": source,
                "conversion_rates": data["conversion_rates"]
            }
            json.dump(cache, open(fichier_cache,"w"))
            if cible in data["conversion_rates"]:
                taux = cache["conversion_rates"][cible]
            else:
                print("devise cible introuvable")

        else:
            cache = json.load(open(fichier_cache,"r"))
            dernier_temps = datetime.fromisoformat(cache["temps"])
            #le fromisoformat sert a prendre le str et le transformer en datetime
            diff = (maintenant - dernier_temps).total_seconds()
            
            if diff < 1800 and source == cache["base"]: #moins de 30min
                print("cache valide")
                if cible in cache["conversion_rates"]:
                    taux = cache["conversion_rates"][cible]
                else:
                    print("devise cible introuvable")
            else:
                print("mise à jour du cache !")
                data = get_taux_change(source)
                cache = {
                    "temps": maintenant.isoformat(),
                    "base": source,
                    "conversion_rates": data["conversion_rates"]
                }
                json.dump(cache, open(fichier_cache,"w"))
                if cible in data["conversion_rates"]:
                    taux = cache["conversion_rates"][cible]
                else:
                    print("devise cible introuvable")

        #if data != None:
        #    print(f"taux de conversion : {data}")
        #    print(f"le montant d'origine : {montant:.2f} {source}")
        #    print(f"après conversion : {montant*data}{cible}")
        print(f"taux de conversion : {taux}")
        print(f"le montant d'origine : {montant:.2f} {source}")
        print(f"après conversion : {montant*taux} {cible}")
        
if __name__ == "__main__":
    main()
    
    
    
# fonction get qui retourne seulement le taux 
# afin de travailler avec un cache pour limiter les requettes vers l'api
#nous avons besoin d'une fonction qui retourne toutes les données json
#afin de pouvoir les inscrire directement dans le cache

#def get_taux_change(source, cible):
#    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source}"
#    try:
#        g = requests.get(url, timeout=5)
#        #g.status_code	Code HTTP de la réponse (200 = succès, 404 = erreur).
#        #g.text	Contenu brut de la réponse (du texte JSON).
#        #g.json()	Contenu converti directement en dictionnaire Python.
#        g.raise_for_status()
#        #lève une exception pour les codes HTTP >= 400, qu'on peux attraper avec RequestException
#        #if g.status_code == 200: la ça veut dire code réussit
#        data = g.json()
#        #Convertir le JSON en dictionnaire Python
#        if cible in data["conversion_rates"]:
#            #Extraire le taux voulu (ici USD -> EUR)
#            taux = data["conversion_rates"][cible]
#            return taux
#        else:
#            print("Erreur : Devise cible invalide")
#            return None
#    except requests.ConnectionError:
#        print("Erreur de réseau : impossible de joindre l'API")
#        #par defaut ça return None quand on écrit rien
#    except requests.Timeout:
#        print("Erreur : délai de connextion dépassé")
#    except requests.RequestException as e:
#        print("Erreur lors de la rêquete : ", e)


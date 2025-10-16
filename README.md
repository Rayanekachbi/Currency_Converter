# 💱 Convertisseur de devises (Currency Converter)

Un script Python qui permet de convertir un montant d'une devise à une autre en utilisant l’API **ExchangeRate-API**.
Le programme met automatiquement en cache les taux de change localement pour éviter de multiples appels à l’API et améliorer les performances.

---

## 🇫🇷 **Version française**

### 📦 Fonctionnalités

* Conversion entre plus de **150 devises**.
* Utilise un **cache local (`cache.json`)** pour limiter les appels à l’API (valide pendant 30 minutes).
* Interface en **ligne de commande** (CLI) avec `argparse`.
* Gestion des erreurs réseau et de saisie utilisateur.

---

### ⚙️ Installation

1. **Cloner le projet :**

   ```bash
   git clone https://github.com/Rayanekachbi/Currency_Converter.git
   cd currency-converter
   ```

2. **Installer la dépendance requise :**

   ```bash
   pip install requests
   ```

3. **Ajouter votre clé API :**

   Le script nécessite une clé API pour fonctionner.
   Vous pouvez obtenir gratuitement une clé sur [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/).

   * Cliquez sur **"Get Free Key"**
   * Créez un compte (gratuit)
   * Copiez votre clé API
   * Ouvrez le fichier `converter.py`
   * Remplacez 'your api key' dans la ligne suivante :

     ```python
     API_KEY = 'your api key'
     ```

---

### 🧠 Principe du cache

Le script stocke les résultats de l’API dans un fichier `cache.json`.
Ce fichier contient :

* la **devise source** (base),
* la **liste complète des taux de conversion**,
* un **horodatage** (`temps`).

Lorsqu’une conversion est demandée :

1. Si un cache existe et qu’il date de **moins de 30 minutes**, le script réutilise les données existantes.
2. Sinon, il interroge à nouveau l’API et met à jour le cache.

Cela permet :

* de réduire le **nombre de requêtes API** (plus rapide et économe),
* d’éviter les **erreurs réseau** en cas de déconnexion.

---

### 🖥️ Utilisation

#### 🔹 Mode interactif

Lancez simplement le programme :

```bash
python converter.py
```

Il vous demandera :

* le montant à convertir,
* la devise source (ex : USD),
* la devise cible (ex : EUR).

#### 🔹 Mode en ligne de commande

Vous pouvez aussi tout passer en arguments :

```bash
python converter.py --amount 100 --from USD --to EUR
```

---

### 🧾 Exemple de sortie

```
pas de cache trouvé, appel à l'API
taux de conversion : 0.921
le montant d'origine : 100.00 USD
après conversion : 92.10 EUR
```

---

### 🧑‍💻 Auteur

Créé par **<Rayane KACHBI>** – Projet personnel d’apprentissage Python.

---

---

## 🇬🇧 **English Version**

# 💱 Currency Converter

A simple Python script to convert an amount from one currency to another using the **ExchangeRate-API**.
It automatically caches exchange rates locally to reduce API calls and improve performance.

---

### 📦 Features

* Supports conversion between **150+ currencies**
* Uses a **local cache (`cache.json`)** valid for 30 minutes
* Command-line interface via `argparse`
* Handles network and input errors gracefully

---

### ⚙️ Installation

1. **Clone the project:**

   ```bash
   git clone https://github.com/Rayanekachbi/Currency_Converter.git
   cd currency-converter
   ```

2. **Install required dependency:**

   ```bash
   pip install requests
   ```

3. **Add your API key:**

   The script needs an API key to work.
   Get your free key from [https://www.exchangerate-api.com/](https://www.exchangerate-api.com/).

   * Click **"Get Free Key"**
   * Sign up for a free account
   * Copy your key 
   * Open `converter.py`

     ```python
     API_KEY = 'your api key'
     ```

---

### 🧠 How the Cache Works

The program stores the last exchange rate data in a file called `cache.json`.
It contains:

* The **base currency**
* A **list of all conversion rates**
* A **timestamp**

When you run the program:

1. If the cache exists and is **less than 30 minutes old**, the data is reused.
2. Otherwise, a fresh request is made to the API and the cache is updated.

This approach:

* Reduces **API calls**
* Makes the converter **faster and more reliable offline**

---

### 🖥️ Usage

#### 🔹 Interactive mode

Run:

```bash
python converter.py
```

The program will ask for:

* amount
* source currency (e.g., USD)
* target currency (e.g., EUR)

#### 🔹 Command-line mode

Provide all arguments directly:

```bash
python converter.py --amount 100 --from USD --to EUR
```

---

### 🧑‍💻 Author

Created by **Rayane KACHBI** — Python learning project.

# **Guide Pratique : Utilisation des APIs Temps Réel CTA (Chicago) et SEPTA (Philadelphie)**

Ce guide décrit comment utiliser les APIs **CTA Bus Tracker** et **SEPTA TransitView** pour récupérer des données en temps réel sur les transports urbains, et comment combiner cela avec les données historiques de ridership.

---

## 1. Sources de données historiques

| Source | Type | Contenu | 
|--------|------|---------|------|
| CTA Ridership (Chicago) | RDF → CSV | Moyennes mensuelles par ligne et type de jour (depuis 2001 jusqu'à 2025) | 
| SEPTA Ridership (Philadelphia) | CSV | Ridership moyen quotidien par arrêt et par mode | 
|CTA Mode of transport | Excel |Ridership moyen quotidien  par mode for chicago city|



----------



----------

## **2. APIs Temps Réel**

### **2.1 CTA Bus Tracker (Chicago)**

-   **Type** : REST API (JSON)
    
-   **Accès** : Clé API gratuite (obtenez-la [ici](https://www.transitchicago.com/developers/bustracker/)     ou [ici](https://www.ctabustracker.com/dev-account))
    
-   **Fonctionnalités** :
    
    -   Liste des routes (`getroutes`)
    -   Liste des arrêts par route (`getstops`)
    -   Positions des véhicules en temps réel (`getvehicles`)
    -   Prédictions d’arrivée (`getpredictions`) – parfois indisponibles
    -   Calcul des fréquences et intervalles entre bus
-   **Limitations** :
    
    -   Certaines données peuvent être manquantes (arrêts, prédictions)
    -   La ponctualité ne peut être calculée que si `getpredictions` est disponible
    - pas de donnée historique

#### **Exemple Python : Récupérer la liste des routes**

```python

import  requests
import  pandas  as  pd 

# ==============================
# CONFIG
# ==============================

CTA_API_KEY  =  "2GnRBdjEdbJnub7QLt8HtLGYL"
CTA_BASE  =  "https://www.ctabustracker.com/bustime/api/v3"

# ==============================
# HELPER
# ==============================
def call_cta(endpoint, params):
    """Call a CTA Bus Tracker endpoint and return JSON dict or None."""
    try:
        r = requests.get(f"{CTA_BASE}/{endpoint}", params=params, timeout=10)
        r.raise_for_status()
        j = r.json().get("bustime-response", {})
        if "error" in j:
            print(f"CTA ERROR {endpoint}: {j['error']}")
            return None
        return j
    except Exception as e:
        print(f"CTA Request fail ({endpoint}): {e}")
        return None
# ==============================
# Exemple 1 : for  CTA Routes retrivial
# ==============================

cta_routes = call_cta("getroutes", {"key": CTA_API_KEY, "format": "json"})
df_cta_routes = pd.DataFrame(cta_routes.get("routes", [])) if cta_routes else pd.DataFrame()
print(df_cta_routes.head())
# ==============================
#  Exemple 2 : for CTA Vehicles retrival
# ==============================
SAMPLE_ROUTE = 20 # example de route numero 20
print(f"\n=== CTA: Vehicles on Route {SAMPLE_ROUTE} ===")
cta_vehicles = call_cta("getvehicles", {
    "key": CTA_API_KEY,
    "rt": SAMPLE_ROUTE,
    "format": "json"
})
df_cta_vehicles = pd.DataFrame(cta_vehicles.get("vehicle", [])) if cta_vehicles else pd.DataFrame()
print(df_cta_vehicles.head())
print("Total vehicles:", len(df_cta_vehicles))

```
# Utilisation
df_routes = get_cta_routes(CTA_API_KEY)
print(df_routes.head())


**Résultat** : Un DataFrame contenant la liste des routes disponibles.

----------

### **2.2 SEPTA TransitView (Philadelphie)**

-   **Type** : REST API (JSON)
    
-   **Accès** : Public, pas de clé API nécessaire
    
-   **Fonctionnalités** :
    
    -   Positions GPS de tous les véhicules (`TransitViewAll`)
    -   Positions GPS par route spécifique (`TransitView`)
    -   Calcul des fréquences et intervalles entre véhicules
-   **Limitations** :
    
    -   Pas de prédictions d’arrivée
    -   Informations sur les arrêts manquantes (à compléter avec les données GTFS statiques)

#### **Exemple Python : Récupérer les positions de tous les véhicules**

```python

import pandas as pd
import requests

SEPTA_BASE_ALL = "https://www3.septa.org/api/TransitViewAll/index.php"

r = requests.get(SEPTA_BASE_ALL, timeout=10)
r.raise_for_status()
j = r.json()

rows = []

# Handle different response shapes and flatten into a list of vehicle dicts
if isinstance(j.get("routes"), dict):
    for route, vehicles in j.get("routes", {}).items():
        if isinstance(vehicles, list):
            for v in vehicles:
                if isinstance(v, dict):
                    rec = v.copy()         
                    rec["route"] = route
                    rows.append(rec)

elif isinstance(j.get("routes"), list):
    for item in j.get("routes", []):
        if isinstance(item, dict):
            for route, vehicles in item.items():
                if isinstance(vehicles, list):
                    for v in vehicles:
                        if isinstance(v, dict):
                            rec = v.copy()  
                            rec["route"] = route
                            rows.append(rec)
                elif isinstance(vehicles, dict):
                    rec = vehicles.copy()   
                    rec["route"] = route
                    rows.append(rec)

elif "VehiclePositions" in j:
    rows = j.get("VehiclePositions", [])

df_septa_all = pd.DataFrame(rows)

print(df_septa_all.head())
print("Total vehicles:", len(df_septa_all))

```
**Résultat** : Un DataFrame avec les positions en temps réel de tous les véhicules SEPTA.

**Colonnes :**  
- `lat` : latitude du véhicule  
- `lng` : longitude du véhicule  
- `label` : étiquette du véhicule  
- `VehicleID` : identifiant du véhicule  
- `route_id` : identifiant de la ligne / route  
- `BlockID` : identifiant du bloc de service  
- `Direction` : direction du véhicule  
- `destination` : destination finale  
- `Offset` : décalage actuel par rapport à l’horaire  
- `heading` : cap du véhicule (en degrés)  
- `late` : retard en minutes  
- `original_late` : retard initial  
- `Offset_sec` : décalage en secondes  
- `trip` : identifiant du voyage / trajet  
- `next_stop_id` : identifiant du prochain arrêt  
- `next_stop_name` : nom du prochain arrêt  
- `next_stop_sequence` : séquence du prochain arrêt  
- `estimated_seat_availability` : estimation des places disponibles  
- `timestamp` : horodatage de la position  
- `route` : nom ou code de la route


----------

## **3. Exemple Complet : Analyse des Données Temps Réel**

Voici un script Python complet pour récupérer et analyser les données des deux APIs :

```python
# ==============================
# Example of Comparison Metrics
# ==============================
# Vehicles per city
vehicles_per_city = df_all.groupby("city")["VehicleID"].count()
print("\n=== Active Vehicles by City ===")
print(vehicles_per_city)

# Average delay per city
avg_delay = df_all.groupby("city")["late"].mean()
print("\n=== Average Delay by City (minutes) ===")
print(avg_delay)

# Vehicles per route (top 5 routes each city)
top_routes = df_all.groupby(["city","route"])["VehicleID"].count().sort_values(ascending=False).groupby(level=0).head(5)
print("\n=== Top 5 Routes by Active Vehicles ===")
print(top_routes)

```
----------

## **4. Conseils pour Aller Plus Loin**

-   **Combiner avec les données historiques** : Utilisez les données de fréquentation pour analyser les tendances et les retards.
-   **Automatiser la collecte** : Planifiez des appels réguliers aux APIs pour suivre l’évolution des données.
-   **Visualiser les résultats** : Utilisez des bibliothèques comme `matplotlib` ou `folium` pour cartographier les positions des véhicules.

----------

## **5. Ressources Utiles**

-   [Documentation officielle CTA](https://www.transitchicago.com/developers/bustracker/)
-   [Documentation SEPTA](https://api.septa.org/)


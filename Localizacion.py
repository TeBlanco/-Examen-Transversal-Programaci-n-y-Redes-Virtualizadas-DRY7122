import requests
from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic

#Función para obtener las coordenadas de una ciudad
def get_coordinates(city, api_key):
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(city)
    if results:
        return (results[0]['geometry']['lat'], results[0]['geometry']['lng'])
    else:
        print(f"No se pudieron obtener las coordenadas de {city}.")
        return None

#Función para calcular la distancia entre dos puntos geográficos
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).km

#Solicitar información del usuario
api_key = '095e11a96a4e4f6b93d0482d71ae25ef'
while True:
    origen = input("Ingrese la Ciudad de Origen: ")
    if origen.lower() == 's':
        break
    destino = input("Ingrese la Ciudad de Destino: ")
    if destino.lower() == 's':
        break

    # Obtener coordenadas de las ciudades
    coord_origen = get_coordinates(origen, api_key)
    coord_destino = get_coordinates(destino, api_key)

    if coord_origen and coord_destino:
        # Calcular la distancia
        distancia = calculate_distance(coord_origen, coord_destino)
        print(f"La distancia entre {origen} y {destino} es de {distancia:.2f} km.")

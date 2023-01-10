import folium
import pandas as pd
import csv


log = []
lat = []
name = []

log_pf = []
lat_pf = []
name_pf = []

# ---> PACHECO <---
try:
    with open("Folium Map/joalheria/hstern.csv", "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")

        for i, linha in enumerate(arquivo_csv):

            if i == 0:
                None
            else:
                name.append(linha[0]+'<br><br>'+linha[1])
                log.append(linha[2])
                lat.append(linha[3])


except:
    print("File not found")

# ---> VENANCIO <---

try:
    with open("Folium Map/joalheria/Pandora.csv", "r") as arquivo2:
        arquivo_csv2 = csv.reader(arquivo2, delimiter=";")

        for i, linha2 in enumerate(arquivo_csv2):

            if i == 0:
                None
            else:
                name.append(linha2[0]+'<br><br>'+linha2[1])
                log.append(linha2[2])
                lat.append(linha2[3])


except:
    print("File not found")

# ---> PROFARMA <---

try:
    with open("Folium Map/joalheria/vivara.csv", "r") as arquivo3:
        arquivo_csv3 = csv.reader(arquivo3, delimiter=";")

        for i, linha3 in enumerate(arquivo_csv3):

            if i == 0:
                None
            else:

                name_pf.append(linha3[0]+'<br><br>'+linha3[1])
                log_pf.append(linha3[2])
                lat_pf.append(linha3[3])


except:
    print("File not found")

# print(len(log))
# print(lat)
# print(log_pf)
# print(lat_pf)

# --- CREATING THE GRAPH

m = folium.Map(location=[-20, -43], zoom_start=5)

# mudar estilo
folium.TileLayer('cartodbpositron').add_to(m)

for i, cord in enumerate(log):
    test_name = name[i].split('<')

    # print(test_name)
    # print(cord)

    if test_name[0] == "Pandora":

       # print(test_name[0], cord, lat[i])

        pach2 = folium.features.CustomIcon(
            'Folium Map/joalheria/Pandora.png', icon_size=(15, 15))
        folium.Marker(location=[lat[i], cord],
                      popup=name[i], icon=pach2).add_to(m)
    else:
        pach = folium.features.CustomIcon(
            'Folium Map/joalheria/hstern.jpg', icon_size=(15, 15))
        folium.Marker(location=[lat[i], cord],
                      popup=name[i], icon=pach).add_to(m)

for j, drog in enumerate(log_pf):
    pach3 = folium.features.CustomIcon(
        'Folium Map/joalheria/viva.webp', icon_size=(15, 15))
    folium.Marker(location=[lat_pf[j], drog],
                  popup=name_pf[j], icon=pach3).add_to(m)

# Display the map
m.save('map_jewels.html')

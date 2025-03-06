import requests
import json
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon

key = '32FB2396-7CFE-3175-9B4D-F41D40368252'
url = f'https://api.vworld.kr/req/wfs?key={key}&service=WFS&srsname=EPSG:4326&request=GetFeature&output=application/json&TYPENAME=lt_c_aisuac,lt_c_aisaltc,lt_c_aisfldc,lt_c_aisctrc,lt_c_aismoac,lt_c_aisprhc,lt_c_aisatzc,lt_c_aisresc,lt_c_aisdngc'

response = requests.get(url)
if response.status_code != 200: exit()

data = json.loads(response.content)

id_to_str = {
    'lt_c_aismoac': '군작전구역',
    'lt_c_aisuac': '초경량비행장치공역',
    'lt_c_aisctrc': '관제권',
    'lt_c_aisdngc': '위험구역',
    'lt_c_aisresc': '비행제한구역',
    'lt_c_aisfldc': '경량항공기이착륙장',
    'lt_c_aisaltc': '경계구역',
    'lt_c_aisatzc': '비행장교통구역',
    'lt_c_aisprhc': '비행금지구역',
}

id_to_int = {
    'lt_c_aismoac': 0,
    'lt_c_aisuac': 1,
    'lt_c_aisctrc': 2,
    'lt_c_aisdngc': 3,
    'lt_c_aisresc': 4,
    'lt_c_aisfldc': 5,
    'lt_c_aisaltc': 6,
    'lt_c_aisatzc': 7,
    'lt_c_aisprhc': 8,
}

ids = set()
areas = []
for i, f in enumerate(data['features']):
    type = f["id"].split('.')[0]
    ids.add(type)
    if f["geometry"] is None: continue
    print(f'{i} {f["type"]} {f["id"]} {f["geometry"]["type"]}')
    for idx, cod in enumerate(f['geometry']['coordinates'][0]):
        # print(cod)
        areas.append({
            'name': f'{f["type"]}_{idx}',
            'type': type,
            'type_str': id_to_str[type],
            'type_int': id_to_int[type],
            'area': Polygon(cod)
        })
gdf = gpd.GeoDataFrame(areas, geometry='area', crs="EPSG:4326")
gdf = gdf.set_geometry('area')
gdf.to_file("./data/areas.shp")
print(gdf)

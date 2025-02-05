import pandas as pd
import openpyxl

#cargar base de datos DB_DOTA
url = "https://github.com/Nelson-Mantilla/PRUEBAS/raw/refs/heads/main/DB%20DOTA_.xlsx"
BD_DOTA_ = pd.read_excel(url, engine='openpyxl')

#cargar base de datos Parametria comercio

url = "https://github.com/Nelson-Mantilla/PRUEBAS/raw/refs/heads/main/Parametria%20Comercio.xlsx"
Parametria_Comercio = pd.read_excel(url, engine='openpyxl')

#cargar base de datos reporte fd

url = "https://github.com/Nelson-Mantilla/PRUEBAS/raw/refs/heads/main/Reporte%20FD_.xlsx"
REPORTE_FD = pd.read_excel(url, engine='openpyxl')

# NORMALIZACIÓN DB DOTA

# CARD_NUMBER = Debes unir la columnas 'CARD_SIX_FIRST_DIGITS', 
# el texto 'XXXXXX' y la columna 'CARD_FOUR_LAST_DIGITS'

BD_DOTA_['CARD_NUMBER'] = BD_DOTA_['CARD_SIX_FIRST_DIGITS'].astype(str) + 'XXXXXX' + BD_DOTA_['CARD_FOUR_LAST_DIGITS'].astype(str).str.zfill(4)


# GTWC_AUTHORIZATION_CODE = Si 'CAPTURE_AUTHORIZATION_CODE' es igual a '000000' 
# y 'CAPTURE_ACQUIRER' = 'Cabal' debes dejar el espacio en
#VACIO, pero si no, debes dejar el dato como viene en la columna 'CAPTURE_AUTHORIZATION_CODE'

BD_DOTA_['GTWC_AUTHORIZATION_CODE'] = BD_DOTA_.apply(lambda row: '' if row['CAPTURE_AUTHORIZATION_CODE'] == '0000' and row['CAPTURE_ACQUIRER'] == 'Cabal' else row['CAPTURE_AUTHORIZATION_CODE'], axis=1)

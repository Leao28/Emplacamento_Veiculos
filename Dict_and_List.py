# Setting the dictionary
Dicionario = {
    'ETIOS HB': 'ETIOS_HB', 'YARIS HB': 'YARIS_HB', 'FOX/CROSS FOX': 'FOX+CROSS_FOX', 'CRUZE HB': 'CRUZE_HB', 'CLASSE A': 'CLASSE_A', 'KA SEDAN': 'KA_SEDAN', 'ETIOS SEDAN':'ETIOS_SEDAN', 'ONIX PLUS': 'ONIX_PLUS', 'YARIS SEDAN': 'YARIS_SEDAN',
    'ARRIZO 5': 'ARRIZO_5', 'ARRIZO 6': 'ARRIZO_6', 'CRUZE SEDAN': 'CRUZE_SEDAN', 'CLASSE A': 'CLASSE_A', 'CLASSE C': 'CLASSE_C', 'CLASSE E': 'CLASSE_E', 'A3 SEDAN': 'A3_SEDAN', 'SPACE FOX': 'SPACE_FOX', 'PALIO WEEKEND': 'PALIO_WEEKEND', 
    'RS6 AVANT': 'RS6_AVANT', 'RS4 AVANT': 'RS4_AVANT', 'T CROSS': 'T-CROSS', 'TIGGO 2': 'TIGGO_2', 'TIGGO 3X': 'TIGGO_3X', 'TIGGO 5X': 'TIGGO_5X', 'TIGGO 7': 'TIGGO_7','TIGGO 8': 'TIGGO_8', 'HILUX SW4': 'HILUX_SW4', 'C4 CACTUS': 'C4_CACTUS', 
    'COROLLA CROSS': 'COROLLA_CROSS', 'ECLIPSE CROSS': 'ECLIPSE_CROSS', 'CLASSE GLB': 'CLASSE_GLB', 'JIMNY SIERRA': 'JIMNY_SIERRA', 'DAILY 35-150': 'DAILY_35-150', 'OUTBACK WAGON': 'OUTBACK_WAGON', 'RANGE ROVER': 'RANGE_ROVER', 
    'GOLF VARIANT': 'GOLF_VARIANT', 'E TRON GT': 'E_TRON_GT', 'E TRON': 'E_TRON', 'VW/MAN': 'VW',
    'CAOA CHERY': 'CAOA_CHERY', 'LAND ROVER': 'LAND_ROVER'
}

Dicionario = {r"\b{}\b".format(k): v for k, v in Dicionario.items()}

# Setting the lists
Lista_Categorias = ['Veículo de Entrada', 'Hatch Pequeno', 'Hatch Médio', 'Sedan Pequeno', 'Sedan Compacto', 
'Sedan Médio', 'Sedan Grande', 'SW Médio', 'SW Grande', 'Monocab', 'Grandcab', 'Sport', 'SUV', 'Pick-up Pequena',
'Pick-up Grande', 'Furgoes']

Lista_Eletricos = ['500E', 'E-JS1', 'ZOE', 'LEAF', 'I3', '330E', '530E', 'MODEL S', 'E TRON GT', 'E TRON', 'BOLT', 'E5', '330E', '530E']

Lista_Hibridos = ['COROLLA', 'COROLLA CROSS', 'XC40', 'XC60', 'XC90', 'PANAMERA', '745LE']

Lista_Meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
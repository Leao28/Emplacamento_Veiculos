# Setting the dictionary
Dicionario = {'CITY HATCH': 'CITY_HATCH', 'CORSA SEDAN': 'CORSA_SEDAN', 'MODEL S': 'MODEL_S', 'AMG GT BS': 'AMG_GT_BS',
    'ETIOS HB': 'ETIOS_HB', 'YARIS HB': 'YARIS_HB', 'FOX/CROSS FOX': 'FOX+CROSS_FOX', 
    'CRUZE HB': 'CRUZE_HB', 'CLASSE A': 'CLASSE_A', 'KA SEDAN': 'KA_SEDAN', 'ETIOS SEDAN':'ETIOS_SEDAN', 
    'ONIX PLUS': 'ONIX_PLUS', 'YARIS SEDAN': 'YARIS_SEDAN', 'JETTA VARIANT': 'JETTA_VARIANT',
    'ARRIZO 5': 'ARRIZO_5', 'ARRIZO 6': 'ARRIZO_6', 'CRUZE SEDAN': 'CRUZE_SEDAN', 
    'CLASSE A': 'CLASSE_A', 'CLASSE C': 'CLASSE_C', 'CLASSE E': 'CLASSE_E',  'A 200': 'A_200',
    'A3 SEDAN': 'A3_SEDAN', 'SPACE FOX': 'SPACE_FOX', 'PALIO WEEKEND': 'PALIO_WEEKEND', 
    'RS6 AVANT': 'RS6_AVANT', 'RS4 AVANT': 'RS4_AVANT', 'T CROSS': 'T-CROSS', 
    'TIGGO 2': 'TIGGO_2', 'TIGGO 3X': 'TIGGO_3X', 'TIGGO 5X': 'TIGGO_5X', 'TIGGO 7': 'TIGGO_7','TIGGO 8': 'TIGGO_8', 
    'HILUX SW4': 'HILUX_SW4', 'C4 CACTUS': 'C4_CACTUS',  'NEW FIESTA': 'NEW_FIESTA',
    'COROLLA CROSS': 'COROLLA_CROSS', 'ECLIPSE CROSS': 'ECLIPSE_CROSS', 'CLASSE GLB': 'CLASSE_GLB', 
    'CLASSE GLA': 'CLASSE_GLA', 'JIMNY SIERRA': 'JIMNY_SIERRA', 'CELER SEDAN': 'CELER_SEDAN', 
    'OUTBACK WAGON': 'OUTBACK_WAGON', 'RANGE ROVER': 'RANGE_ROVER', 'PICK UP': 'PICK-UP',
    'GOLF VARIANT': 'GOLF_VARIANT', 'E TRON GT': 'E_TRON_GT', 'E TRON': 'E_TRON', 
    'VW/MAN': 'VW', 'A4 AVANT': 'A4_AVANT', 'FOCUS SEDAN': 'FOCUS_SEDAN', '488 PISTA': '488_PISTA', 
    'FIESTA SEDAN': 'FIESTA_SEDAN', 'M3 SEDAN': 'M3_SEDAN', 'C4 PICASSO': 'C4_PICASSO', 'AGRALE MARRUA': 'AGRALE_MARRUA', 
    'SPRINTER 313': 'SPRINTER_313', 'DAILY 3514': 'DAILY_3514', 'DAILY 35-150': 'DAILY_35-150',
    'J3 TURIN': 'J3_TURIN', 'CLASSE B': 'CLASSE_B', 'SLC 300': 'SLC_300', 'LF 530': 'LF_530',
    'RELY PICK-UP': 'RELY_PICK-UP', 'SPRINTER 311': 'SPRINTER_311', 'A6 ALLROAD': 'A6_ALLROAD',
    'MAREA WEEKEND': 'MAREA_WEEKEND', 'MEGANE GT': 'MEGANE_GT', 'ASTRA SEDAN': 'ASTRA_SEDAN',
    'C3 PICASSO': 'C3_PICASSO', 'C3 AIRCROSS': 'C3_AIRCROSS', 'POLO SEDAN': 'POLO_SEDAN',
    'TOWN COUNTRY': 'TOWN_COUNTRY', 'C 250': 'C_250', 'START ': 'START_',
    'CAOA CHERY': 'CAOA_CHERY', 'LAND ROVER': 'LAND_ROVER'
}

Dicionario = {r"\b{}\b".format(k): v for k, v in Dicionario.items()}

# Setting the lists
Lista_Categorias = ['Veículo de Entrada', 'Hatch Pequeno', 'Hatch Médio', 'Sedan Pequeno', 'Sedan Compacto', 
'Sedan Médio', 'Sedan Grande', 'SW Médio', 'SW Grande', 'Monocab', 'Grandcab', 'Sport', 'SUV', 'Pick-up Pequena',
'Pick-up Grande', 'Furgoes']

Lista_Eletricos = ['500E', 'E-JS1', 'ZOE', 'LEAF', 'I3', 'I5', 'I8', '330E', '530E', 'MODEL S', 'E TRON GT', 'E TRON', 'BOLT', 'E5', '330E', '530E', 'E6', 'TWIZY', 'MODEL X']

Lista_Hibridos = ['COROLLA', 'COROLLA CROSS', 'XC40', 'XC60', 'XC90', 'PANAMERA', '745LE', 'PRIUS', 'EPACE', 'CT200H']

Lista_Meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

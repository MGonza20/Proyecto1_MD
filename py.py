# 'Agricultores y trabajadores calificados de explotaciones agropecuarias con destino al mercado': 1 - 61
# 'Artesanos y operarios de las artes gráficas': 2 - 73
# 'Ayudantes de preparación de alimentos': 3 - 94
# 'Conductores de vehículos y operadores de equipos pesados móviles': 4 - 83
# 'Directores administradores y comerciales': 5 - 12
# 'Directores ejecutivos, personal directivo de administración pública, miembros del poder ejecutivo y cuerpos legislativos': 6 - 11
# 'Directores y gerentes de producción y operaciones': 7 - 13
# 'Empleados contables y encargados del registro de materiales': 8 - 43
# 'Empleados en trato directo con el público': 9 - 42
# 'Ensambladores': 10 - 82
# 'Especialistas en organización de la administración publica y de empresas': 11 - 24
# 'Gerentes de hoteles, restaurantes, comercios y otros servicios': 12 - 14
# 'Limpiadores y asistentes': 13 - 91
# 'No especificado en otro grupo': 14 - NEOG
# ! 'Oficiales de las fuerzas armadas': 15 - 01
# 'Oficiales y operarios de la construcción excluyendo electricistas': 16 - 71
# 'Oficiales y operarios de la metalurgia, la construcción mecánica y afines': 17 - 72
# 'Oficinistas': 18 - 41
# 'Operadores de instalaciones fijas y máquinas': 19 - 81
# !'Operarios y oficiales de procesamiento de alimentos, de la confección, ebanistas, otros artesanos y afines': 20 - 75
# 'Otro personal de apoyo administrativo': 21 - 44
# 'Otros miembros de las fuerzas armadas': 22 - 03
# 'Peones agropecuarios, pesqueros y forestales':  23 - 92
# 'Peones de la minería, la construcción, la industria manufacturera y el transporte': 24 - 93
# !'Personal de los servicios de protección': 25 - 54
# 'Profesionales de la enseñanza':  26 - 23
# 'Profesionales de la salud': 27 - 22
# 'Profesionales de las ciencias y de la ingeniería': 28 - 21
# 'Profesionales de las ciencias y la ingeniería de nivel medio': 29 - 31
# !'Profesionales de nivel medio de la salud': 30 - 32
# 'Profesionales de nivel medio de servicios jurídicos, sociales, culturales y afines': 31 - 34
# 'Profesionales de nivel medio en operaciones financieras y administrativas': 32 - 33
# 'Profesionales de tecnología de la información y las comunicaciones': 33 - 25
# 'Profesionales en derecho, en ciencias sociales y culturales': 34 - 26
# !'Recolectores de desechos y otras ocupaciones elementales': 35 - 96
# 'Trabajadores de los cuidados personales': 36 - 51
# 'Trabajadores de los servicios personales': 36 - 51
# 'Trabajadores especializados en electricidad y la elecrotecnología': 37 - 74
# 'Técnicos de la tecnología de la información y las comunicaciones': 38 - 35
# 'Vendedores': 39 - 52
# 'Vendedores ambulantes de servicios y afines': 40 - 95
# 'Suboficiales de las fuerzas armadas': 22 - 03
# 'Trabajadores forestales calificados, pescadores y cazadores': 41 - 62


# 'Agricultores y trabajadores calificados de explotaciones agropecuarias con destino al mercado': 1 - 61

def map_code(code):
    content = {
        '61': 1, '73': 2, '94': 3, '83': 4, '12': 5,
        '11': 6, '13': 7, '43': 8, '42': 9, '82': 10,
        '24': 11, '14': 12, '91': 13, 'NEOG': 14, '01': 15,
        '71': 16, '72': 17, '41': 18, '81': 19, '75': 20,
        '44': 21, '03': 22, '92': 23, '93': 24, '54': 25,
        '23': 26, '22': 27, '21': 28, '31': 29, '32': 30,
        '34': 31, '33': 32, '25': 33, '26': 34, '96': 35,
        '51': 36, '74': 37, '35': 38, '52': 39, '95': 40, 
        '03': 22, '62': 41
    }
    return content.get(code, 0)
    
def map_code(code):
    content = {
        '61': 1, '73': 2, '94': 3, '83': 4, '12': 5, '11': 6, '13': 7, '43': 8, '42': 9, '82': 10,
        '24': 11, '14': 12, '91': 13, 'NEOG': 14, '01': 15, '71': 16, '72': 17, '41': 18, '81': 19, '75': 20,
        '44': 21, '03': 22, '92': 23, '93': 24, '54': 25, '23': 26, '22': 27, '21': 28, '31': 29, '32': 30,
        '34': 31, '33': 32, '25': 33, '26': 34, '96': 35, '51': 36, '74': 37, '35': 38, '52': 39, '95': 40, 
        '03': 22, '62': 41
    }
    return content.get(code.startswith, 0)

def map_code(code):
    if code.startswith('61'):
        return 1
    elif code.startswith('73'):
        return 2
    elif code.startswith('94'):
        return 3
    elif code.startswith('83'):
        return 4
    elif code.startswith('12'):
        return 5
    elif code.startswith('11'):
        return 6
    elif code.startswith('13'):
        return 7
    elif code.startswith('43'):
        return 8
    elif code.startswith('42'):
        return 9
    elif code.startswith('82'):
        return 10
    elif code.startswith('24'):
        return 11
    elif code.startswith('14'):
        return 12
    elif code.startswith('91'):
        return 13
    elif code.startswith('NEOG'):
        return 14
    elif code.startswith('01'):
        return 15
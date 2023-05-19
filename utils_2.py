
def get_ocupaciones_info():
    return {'Agricultores y trabajadores calificados de explotaciones agropecuarias con destino al mercado': 1,
            'Artesanos y operarios de las artes gráficas': 2,
            'Ayudantes de preparación de alimentos': 3,
            'Conductores de vehículos y operadores de equipos pesados móviles': 4,
            'Directores administradores y comerciales': 5,
            'Directores ejecutivos, personal directivo de administración pública, miembros del poder ejecutivo y cuerpos legislativos': 5,
            'Directores y gerentes de producción y operaciones': 5,
            'Empleados contables y encargados del registro de materiales': 6,
            'Empleados en trato directo con el público': 7,
            'Ensambladores': 2,
            'Especialistas en organización de la administración publica y de empresas': 5,
            'Gerentes de hoteles, restaurantes, comercios y otros servicios': 3,
            'Limpiadores y asistentes': 8,
            'No especificado en otro grupo': 12,
            'Oficiales de las fuerzas armadas': 9,
            'Oficiales y operarios de la construcción excluyendo electricistas': 2,
            'Oficiales y operarios de la metalurgia, la construcción mecánica y afines': 2,
            'Oficinistas': 6,
            'Operadores de instalaciones fijas y máquinas': 4,
            'Operarios y oficiales de procesamiento de alimentos, de la confección, ebanistas, otros artesanos y afines': 2,
            'Otro personal de apoyo administrativo': 6,
            'Otros miembros de las fuerzas armadas': 9,
            'Peones agropecuarios, pesqueros y forestales':  1,
            'Peones de la minería, la construcción, la industria manufacturera y el transporte': 4,
            'Personal de los servicios de protección': 9,
            'Profesionales de la enseñanza':  10,
            'Profesionales de la salud': 10,
            'Profesionales de las ciencias y de la ingeniería': 11,
            'Profesionales de las ciencias y la ingeniería de nivel medio': 11,
            'Profesionales de nivel medio de la salud': 10,
            'Profesionales de nivel medio de servicios jurídicos, sociales, culturales y afines': 10,
            'Profesionales de nivel medio en operaciones financieras y administrativas': 6,
            'Profesionales de tecnología de la información y las comunicaciones': 11,
            'Profesionales en derecho, en ciencias sociales y culturales': 10,
            'Recolectores de desechos y otras ocupaciones elementales': 8,
            'Trabajadores de los cuidados personales': 10,
            'Trabajadores de los servicios personales': 10,
            'Trabajadores especializados en electricidad y la elecrotecnología': 2,
            'Técnicos de la tecnología de la información y las comunicaciones': 11,
            'Vendedores': 7,
            'Vendedores ambulantes de servicios y afines': 7
            }

def map_code(code):
    content = {
        '61': 1, '73': 2, '94': 3, '83': 4, '12': 5, '11': 5, '13': 5, '43': 6, '42': 7, '82': 2,
        '24': 5, '14': 3, '91': 8, 'NE': 12, '01': 9, '71': 2, '72': 2, '41': 6, '81': 4, '75': 2,
        '44': 6, '03': 9, '92': 1, '93': 4, '54': 9, '23': 10, '22': 10, '21': 11, '31': 11, '32': 10,
        '34': 10, '33': 6, '25': 11, '26': 10, '96': 8, '51': 10, '74': 2, '35': 11, '52': 7, '95': 7, 
        '03': 9, '62': 1
    }
    return content.get(code[:2], 0)

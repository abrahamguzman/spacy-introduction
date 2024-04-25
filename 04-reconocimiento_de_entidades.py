# ejecutar en cmd "spacy download es_core_news_lg"

import spacy

nlp = spacy.load('es_core_news_lg')

texto = "Abraham Guzman fue uno de los cofundadores de la empresa Apple"
documento = nlp(texto)

print(len(documento))

for entidad in documento.ents:
    print(entidad.text, entidad.label_)

print(spacy.explain('PER'))
print(spacy.explain('ORG'))

print(type(documento.ents))
print(type(documento.ents[0]))

texto = "La Cordillera de los Andes es una cadena montañosa"
documento = nlp(texto)
for entidad in documento.ents:
    print(entidad.text, entidad.label_)

print(spacy.explain('LOC'))

texto = "Las cataratas del Iguazú son una maravilla natural"
documento = nlp(texto)
for entidad in documento.ents:
    print(entidad.text, entidad.label_)

texto = """
Marcas individuales
General
Más torneos ganados: Bandera de Brasil Pelé con 3 (1958, 1962 y 1970).
Más torneos jugados: seis jugadores han disputado el torneo en 5 ocasiones.n 1​
Bandera de México Antonio Carbajal (1950, 1954, 1958, 1962, 1966)
Bandera de Alemania Lothar Matthäus (1982, 1986, 1990, 1994, 1998)
Bandera de México Rafael Márquez (2002, 2006, 2010, 2014, 2018)
Bandera de Argentina Lionel Messi (2006, 2010, 2014, 2018, 2022)
Bandera de Portugal Cristiano Ronaldo (2006, 2010, 2014, 2018, 2022)
Bandera de México Andrés Guardado (2006, 2010, 2014, 2018, 2022)
Más partidos jugados: Bandera de Argentina Lionel Messi (entre 2006 y 2022) con 26.
Más minutos jugados: Bandera de Argentina Lionel Messi con 2315 minutos (entre 2006 y 2022).
Más partidos ganados: Bandera de Alemania Miroslav Klose con 17 (entre 2002 y 2014).
Más finales alcanzadas: cinco jugadores han alcanzado la final del torneo en 3 ocasiones.
Bandera de Brasil Pelé (1958, 1962, 1970)
Bandera de Brasil Cafú (1994, 1998, 2002)
Bandera de Brasil Ronaldo (1994, 1998, 2002)
Bandera de Alemania Lothar Matthäus (1982, 1986, 1990)
Bandera de Alemania Pierre Littbarski (1982, 1986, 1990).
Más finales consecutivas alcanzadas: cuatro jugadores han alcanzado la final del torneo en 3 ocasiones consecutivas.
Bandera de Brasil Cafú (1994, 1998, 2002)
Bandera de Brasil Ronaldo (1994, 1998, 2002)
Bandera de Alemania Lothar Matthäus (1982, 1986, 1990)
Bandera de Alemania Pierre Littbarski (1982, 1986, 1990).
Más finales jugadas: Bandera de Brasil Cafú con 3 (1994, 1998, 2002).
Más partidos jugados como capitán:
Bandera de Argentina Lionel Messi con 19 (2010, 2014, 2018 y 2022).
Más partidos como sustituto: Bandera de Brasil Denilson con 11 (1998 y 2002).
Más joven en un partido: Bandera de Irlanda del Norte Norman Whiteside con 17 años y 42 días (contra Yugoslavia en 1982).
Más joven en una final: Bandera de Brasil Pelé con 17 años y 249 días (contra Suecia en 1958).
Más joven en un partido clasificatorio: Bandera de Togo Souleymane Mamam con 13 años y 310 días (contra Zambia en las clasificatorias para 2002, el 6 de mayo de 2001).7​
Más joven en un partido como capitán: Bandera de Estados Unidos Tony Meola con 21 años y 316 días (contra Checoslovaquia en 1990).8​
Más veterano en un partido: Bandera de Egipto Essam El-Hadary con 45 años y 161 días (contra Arabia Saudita en 2018).9​10​
Más veterano en una final: Bandera de Italia Dino Zoff con 40 años y 133 días (contra Alemania Federal en 1982).
Más veterano en un partido clasificatorio: Bandera de Islas Vírgenes de los Estados Unidos MacDonald Taylor con 46 años y 180 días (contra Bandera de San Cristobal y Nieves San Cristóbal y Nieves en clasificatorias para 2006, el 18 de febrero de 2004).11​
Más veterano en un partido como capitán: Bandera de Egipto Essam El-Hadary con 45 años y 161 días (contra Arabia Saudita en 2018).
Mayor diferencia de edad en un equipo: Bandera de Camerún Camerún con 23 años y 358 días, en 1994 (entre Rigobert Song, con 18 años y 10 días, y Roger Milla, con 42 años y 1 día).
Mayor diferencia de edad en un equipo campeón: Bandera de Italia Italia con 21 años y 297 días, en 1982 (entre Giuseppe Bergomi, con 18 años y 201 días, y Dino Zoff, con 40 años y 133 días).
Mayor período entre dos participaciones como jugador: Bandera de Colombia Faryd Mondragón con 15 años y 363 días (1998 y 2014).
Mayor período entre dos participaciones en general: 44 años, Bandera de Brasil Tim (en 1938 como jugador; Perú, en 1982 como entrenador).
Menor periodo entre debut deportivo y debut en mundiales: Bandera de Dinamarca Christian Eriksen con 147 días (2010).[cita requerida]
Goles
Mayor cantidad de goles anotados en el torneo: 172 (2022).
Primer gol: Bandera de Francia Lucien Laurent ante México en 1930.
Primer gol de penal: Bandera de México Manuel Rosas ante Argentina en 1930.
Primer gol de penal en una final: Bandera de los Países Bajos Johan Neeskens ante Alemania Federal en 1974.
Primer jugador en fallar un penal en una final: Bandera de Italia Antonio Cabrini ante Alemania Federal en 1982.
Más goles anotados: Bandera de Alemania Miroslav Klose con 16 (2002, 2006, 2010 y 2014).
Más goles anotados en fase clasificatoria: Bandera de Guatemala Carlos Ruiz con 39 (entre 1998 y 2015).
Más goles anotados en un solo torneo: Bandera de Francia Just Fontaine con 13 en 1958.
Más goles anotados en un solo partido: Bandera de Rusia Oleg Salenko con 5, contra Camerún en 1994.
Más goles anotados en una derrota: Bandera de Polonia Ernest Wilimowski con 4, contra Brasil en 1938.
Más goles anotados en un partido clasificatorio: Bandera de Australia Archie Thompson con 13, contra Samoa Americana en las clasificatorias para 2002.
Más goles anotados en una final: Bandera de Inglaterra Geoff Hurst y Bandera de Francia Kylian Mbappé con 3 cada uno.
Más goles anotados en finales: Bandera de Francia Kylian Mbappé, con 4.
Primer gol olímpico: Bandera de Colombia Marcos Coll ante la Unión Soviética en 1962.
Primer gol de oro: Bandera de Francia Laurent Blanc ante Paraguay en 1998.
Último gol de oro: Bandera de Turquía Ilhan Mansiz ante Senegal en 2002.
Gol más rápido: Bandera de Turquía Hakan Şükür a los 11 segundos ante Corea del Sur en 2002.
Gol más tardío: Bandera de Italia Alessandro Del Piero ante Alemania en 2006, y Bandera de Argelia Abdelmoumene Djabou ante Alemania en 2014, ambos a los 121 minutos.
Gol más rápido en una final: Bandera de los Países Bajos Johan Neeskens ante Alemania Federal en 1974 al minuto 1 y 27 segundos.
Gol más tardío en una final: Bandera de Inglaterra Geoff Hurst ante Alemania Federal en 1966 a los 120 minutos.
Doblete más rápido: Bandera de Alemania Toni Kroos en 69 segundos ante Brasil en 2014.
Primer autogol anotado: Bandera de México Manuel Rosas ante Chile en 1930.
Autogol más rápido: Bandera de Bosnia y Herzegovina Sead Kolašinac a los 2 minutos y 9 segundos, ante Argentina en 2014.
Primer autogol en una final: Bandera de Croacia Mario Mandžukić ante Bandera de Francia Francia en 2018.
Jugador debutante más joven en convertir un gol: Bandera de Brasil Pelé con 17 años y 239 días de edad, contra Gales en 1958.
Jugador debutante más veterano en convertir un gol: Bandera de Panamá Felipe Baloy con 37 años y 120 días de edad, contra Inglaterra en 2018.
Jugador más joven en convertir un gol: Bandera de Brasil Pelé con 17 años y 239 días de edad, ante Gales en 1958.
Jugador más veterano en convertir un gol: Bandera de Camerún Roger Milla con 42 años y 39 días de edad ante Rusia en 1994.
Único jugador en convertir un hat-trick en dos mundiales distintos: Bandera de Argentina Gabriel Batistuta ante Grecia en 1994 y Jamaica en 1998.
Único jugador en convertir gol en cinco mundiales distintos: Bandera de Portugal Cristiano Ronaldo (2006, 2010, 2014, 2018 y 2022).
Único jugador en anotar en todas las fases de un mundial: Bandera de Argentina Lionel Messi en 2022.
Único jugador en anotar en todos los partidos de un mundial: Bandera de Brasil Jairzinho en 1970.
Asistencias
Más asistencias: Bandera de Brasil Pelé con 10 (1958-1970)12​
Más asistencias en un solo torneo: Bandera de Brasil Pelé con 6, en 197013​
Más asistencias en un solo partido: Bandera de Polonia Robert Gadocha con 4, contra Haití en 1974.14​15​
Más asistencias en una final: Bandera de Brasil Pelé con 2, contra Italia en 1970.
Más asistencias en finales: Bandera de Brasil Pelé con 316​
Entrenadores
Más torneos ganados: Bandera de Italia Vittorio Pozzo, 2 (1934 y 1938).
Más torneos dirigidos: Bandera de Brasil Carlos Alberto Parreira, 6 (1982, 1990, 1994, 1998, 2006 y 2010).
Más partidos dirigidos: Bandera de Alemania Helmut Schön, 25 (1966, 1970, 1974 y 1978).
Más partidos ganados: Bandera de Alemania Helmut Schön, 16 (1966, 1970, 1974 y 1978).
"""

documento = nlp(texto)

print(len(documento))
print(len(documento.ents))

for entidad in documento.ents:
    if entidad.label_ == "PER":
        print(entidad)

# Link: https://en.wikipedia.org/wiki/Cloud_computing
text = open("computacion_nube.txt", encoding='utf-8').read()

nlp = spacy.load('es_core_news_lg')
document = nlp(text)

print(len(document))

print(len(document.ents))

for named_entity in document.ents:
    if named_entity.label_ == "ORG":
        print(named_entity)

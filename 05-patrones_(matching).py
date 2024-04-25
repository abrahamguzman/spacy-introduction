import spacy
from spacy.matcher import Matcher

nlp = spacy.load('es_core_news_lg')

texto = """La Copa Mundial de Fútbol es un evento deportivo que se celebra cada 4 años.
           Se celebró por primera vez en Uruguay en el año 1930.
           En la última edición participaron 32 equipos.
        """

documento = nlp(texto)

matcher = Matcher(nlp.vocab)

patron_1 =  [{"LEMMA":'celebrar'}]
patron_2 = [{"LEMMA":'participar'}]

matcher.add('celebrar',[patron_1])
matcher.add('participar',[patron_2])

resultados = matcher(documento)

print(type(resultados))

for resultado in resultados:
    print(resultado)

for codigo_hash, comienzo, fin in resultados:
    print("<<< Nuevo match >>>")
    print("--- Lemma")
    print(nlp.vocab.strings[codigo_hash])
    print("--- Palabra encontrada")
    print(documento[comienzo-1:fin+1])

matcher = Matcher(nlp.vocab)
matcher.add('celebrar',[patron_1])
resultados = matcher(documento, as_spans=True)

for resultado in resultados:
    print(type(resultado))
    print(resultado)

patron_2 =  [{"IS_DIGIT":True}]
matcher.add('num', [patron_2])
resultados = matcher(documento, as_spans=True)
for resultado in resultados:
    print(resultado)

matcher.remove('num')
resultados = matcher(documento, as_spans=True)
for resultado in resultados:
    print(resultado)

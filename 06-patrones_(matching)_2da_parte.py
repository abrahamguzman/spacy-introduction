import spacy
from spacy.matcher import Matcher

nlp = spacy.load('es_core_news_lg')

# link https://es.wikipedia.org/wiki/S%26P_500
texto = """ El índice Standard & Poor's 500 (Standard & Poor's 500 Index), también conocido como S&P 500, es uno de los índices bursátiles más importantes de Estados Unidos. Al S&P 500 se lo considera el índice más representativo de la situación real del mercado. El índice se basa en la capitalización bursátil de 500 grandes empresas que poseen acciones que cotizan en las bolsas NYSE o NASDAQ, y captura aproximadamente el 80% de toda la capitalización de mercado en Estados Unidos. Los componentes del índice S&P 500 y su ponderación son determinados por S&P Dow Jones Indices. Se diferencia de otros índices de mercados financieros de Estados Unidos, tales como el Dow Jones Industrial Average o el índice Nasdaq Composite, en la diversidad de los rubros que lo conforman y en su metodología de ponderación. Es uno de los índices de valores más seguidos, y muchas personas lo consideran el más representativo del mercado de acciones de Estados Unidos, y el marcador de tendencias de la economía norteamericana. El National Bureau of Economic Research ha clasificado a las acciones comunes como un indicador relevante de los ciclos de negocios. """

documento = nlp(texto)

for sent in documento.sents:
    print(sent)

patron_0 =  [{'LEMMA':'índice'}]
matcher_0 = Matcher(nlp.vocab)
matcher_0.add('índice',[patron_0])
resultados = matcher_0(documento, as_spans=True)

for resultado in resultados:
    print(resultado)

# https://spacy.io/api/matcher#patterns
patron_1 =  [{'IS_DIGIT': True},{'LEMMA':'grande'}]

matcher_1 = Matcher(nlp.vocab)
matcher_1.add('índices',[patron_1])
resultados = matcher_1(documento, as_spans=True)

for resultado in resultados:
    print(resultado)

patron_2 =  [{'LEMMA':'índice'},{'LENGTH': {">=": 5}}]

matcher_2 = Matcher(nlp.vocab)
matcher_2.add('índices',[patron_2])
resultados = matcher_2(documento, as_spans=True)

for resultado in resultados:
    print(resultado)

patron_3 =  [{'LEMMA':'índice'},{'POS':'ADJ'}]

matcher_3 = Matcher(nlp.vocab)
matcher_3.add('índices',[patron_3])
resultados = matcher_3(documento, as_spans=True)

for resultado in resultados:
    print(resultado)

patron_4 = [{"TEXT": {"REGEX": "[Nn][Aa][Ss][Dd][Aa][Qq]"}}]

matcher_4 = Matcher(nlp.vocab)
matcher_4.add('índices',[patron_4])
resultados = matcher_4(documento, as_spans=True)

for resultado in resultados:
    print(resultado)

patron_5 = [{'IS_PUNCT': False},
            {'IS_DIGIT': False},
            {'IS_DIGIT': False},
            {'IS_DIGIT': True}
           ]
matcher_5 = Matcher(nlp.vocab)
matcher_5.add('índices',[patron_5])
resultados = matcher_5(documento, as_spans=True)

for resultado in resultados:
    print(resultado)




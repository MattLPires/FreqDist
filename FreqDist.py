# -*- coding: utf-8 -*-
"""

# Programa 1:

### O programa 1 deve ser dividido em 5 células. Na primeira célula efetue a importação de todas as bibliotecas necessárias.
"""

from urllib import request
from nltk import *
import nltk
nltk.download('punkt')

"""### Na segunda célula deverá constar o código necessário para download do arquivo em formato bruto original e a impressão em tela das 1000 primeiras letras do arquivo."""

MHLP_url = "http://www.gutenberg.org/files/5200/5200-0.txt"
MHLP_response = request.urlopen(MHLP_url)
MHLP_raw = MHLP_response.read().decode('utf8')
MHLP_raw[0:1000]

"""### Na  terceira  célula  deverá  constar  o  código  para  tokenização  do  arquivo  bruto  e  armazenamento  em  uma variável do tipo Text do NLTK e a impressão em tela dos 98 primeiros tokens."""

MHLP_tokens = word_tokenize(MHLP_raw)
MHLP_text = nltk.Text(MHLP_tokens)
MHLP_text[:98]

"""### Na  quarta  célula  deverá  ser  realizada  a  normalização  dos  tokens  e  a  construção  do  vocabulário,  conforme pipeline do PLN trabalhado em sala de aula. """

MHLP_words = [w.lower() for w in MHLP_tokens]
MHLP_vocab = sorted(set(MHLP_words))

"""### Na quinta célula inclua ao final do vocabulário as palavras “Die Verwandlung” e na sequência imprima os últimos 10 tokens do vocabulário em que conste as duas novas palavras acrescentadas."""

MHLP_vocab.append("Die Verwandlung")
MHLP_vocab[len(MHLP_vocab)-10:len(MHLP_vocab)]

"""# Programa 2:

### Na primeira célula incluir todas as bibliotecas necessárias
"""

import nltk
from nltk.corpus import mac_morpho
from nltk import FreqDist

"""### Na segunda célula gerar uma lista impressa das etiquetas (tags) mais comuns do corpus mac_morpho"""

MHLP_mac_morpho_news_tagged = mac_morpho.tagged_words()
MHLP_tag = nltk.FreqDist(tag for (word, tag) in MHLP_mac_morpho_news_tagged)
MHLP_tag.most_common()

"""### Na terceira célula deve ser gerado um gráfico não acumulativo das etiquetas mais comuns."""

MHLP_tag.plot(cumulative = False)

"""### Na quarta célula converta o dicionário em uma lista para verificarmos apenas as chaves do dicionário."""

MHLP_dict = dict(MHLP_mac_morpho_news_tagged)
MHLP_dict

list(MHLP_dict)

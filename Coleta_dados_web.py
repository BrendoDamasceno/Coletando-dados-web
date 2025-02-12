import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#exibir o texto
print(extracao.text.strip())

#Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
   titulo = linha_texto.text.strip()
   print('Titulo: ', titulo )

#Contar qtd de titulos e paragrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto  in extracao.find_all(['h2', 'P']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 #contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de tituos', contar_titulos)
print('Total de paragrafos', contar_paragrafos)


#Exibir somente o texto das tag h2 e P
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('Titulo: \n', titulo)
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: \n', paragrafo)


#Exibir tags Aninhada
for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto link: ', a.text.strip(), '| URL:', a["href"])
#importando biblioteca
import requests
#importando a função BeautifulSoup do pacote bs4
from bs4 import BeautifulSoup

#acessando url
url='https://www.puspsc.usp.br/cardapio/'
resposta=requests.get(url) #acessa as informações do url e guarda em resposta

#verificando se deu certo
if(resposta.status_code==200):
    print('Site acessado com sucesso!')
    html=resposta.content #armazena o conteúdo da url contido na resposta no html
    
    #analisando o html, agora todos os dados serão acessados através de soup
    soup=BeautifulSoup(html,'html.parser')

    #buscando todas as colunas de: dia, almoço, jantar
    dias=soup.find_all('td',class_='column-1')
    almoco=soup.find_all('td',class_='column-2')
    jantar=soup.find_all('td',class_='column-3')
    
    #imprimindo
    for i in range(len(dias)):
        dia = dias[i].text.strip()
        if(dia):
            print(f'dia: {dia}')

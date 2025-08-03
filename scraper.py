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
    
    #analisando o conteúdo
    soup=BeautifulSoup(html,'html.parser')


import requests

weburl = 'https://jsonplaceholder.typicode.com/users'

resposta = requests.get(weburl)

conteudoJson = resposta.json()
tamanhoListaJson = len(conteudoJson)
listaWebsitesUsuarios = []

if tamanhoListaJson:
    for y in conteudoJson:
        listaWebsitesUsuarios.append((y['website']))

print('1) Os websites de todos os usuários:')
print(listaWebsitesUsuarios)

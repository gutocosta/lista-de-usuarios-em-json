import requests

weburl = 'https://jsonplaceholder.typicode.com/users'

resposta = requests.get(weburl)

conteudoJson = resposta.json()
tamanhoListaJson = len(conteudoJson)
listaWebsitesUsuarios = []
listaJson = resposta.json()
usuaria_samantha = 'Samantha'

if tamanhoListaJson:
    for y in conteudoJson:
        listaWebsitesUsuarios.append((y['website']))

    for x in listaJson:
        if usuaria_samantha in x['username']:
            email_usuaria_samantha = (x['email'])
            
print('1) Os websites de todos os usuários:')
print(listaWebsitesUsuarios)
print('2) O email da usuária que possui o campo username igual a "Samantha":')
print(email_usuaria_samantha)

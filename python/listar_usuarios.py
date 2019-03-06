import requests

weburl = 'https://jsonplaceholder.typicode.com/users'

resposta = requests.get(weburl)

conteudoJson = resposta.json()
tamanhoListaJson = len(conteudoJson)
listaWebsitesUsuarios = []
listaJson = resposta.json()
usuaria_samantha = 'Samantha'
listaJsonLoc = resposta.json()
total_usuarios_hem_sul = 0

if tamanhoListaJson:
    for y in conteudoJson:
        listaWebsitesUsuarios.append((y['website']))

    for x in listaJson:
        if usuaria_samantha in x['username']:
            email_usuaria_samantha = (x['email'])

    for z in listaJsonLoc:
        if float(z['address']['geo']['lat']) < 0:
            total_usuarios_hem_sul += 1

print('1) Os websites de todos os usuários:')
print(listaWebsitesUsuarios)
print('2) O email da usuária que possui o campo username igual a "Samantha":')
print(email_usuaria_samantha)
print('3) EXTRA: Mostrar o total de usuários do hemisfério sul:')
print(total_usuarios_hem_sul)

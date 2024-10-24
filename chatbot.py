import openai

chave_api = 'sua chave api aqui'

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {'role':'user', 'content':mensagem}
    )
    
    resposta = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = lista_mensagens
    )
    
    return resposta['choices'][0]['message']

lista_mensagens=[]
while True:
    texto=input('\nEscreva aqui sua mensagem: ')
    if texto == 'sair':
        break

    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print('\nCHATBOT: ', resposta['content'])
        lista_mensagens.append(resposta)

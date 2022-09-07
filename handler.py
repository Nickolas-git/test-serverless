import json

def hello(event, context):

    #Extraindo o parâmetro informado pelo cliente
    meuinput = int(event['pathParameters']['meuinput'])

    n = meuinput
    mult=0
    retorno = ''

    #Verificando os múltiplos
    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    #Validação se é primo ou não
    if(mult==0):
        retorno = 'eh primo'
    else:
        retorno = 'nao eh primo'

    #Visualização da resposta
    body = {
            "message": "Seu numero",
            "values": retorno
        }
    #
    response = {
        "statusCode": 200,
            "body": json.dumps(body)
        }

    return response
import re

def validar_email(email):
    # Define a expressão regular para validar o email
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Verifica se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False

# inclua uma função para obter o endereço baseado no CEP
def obter_endereco(cep):
    # Define a expressão regular para validar o CEP
    padrao = r"^[0-9]{5}-?[0-9]{3}$"
    # Verifica se o CEP corresponde ao padrão
    if re.match(padrao, cep):
        # Faz a requisição ao serviço de CEP
        url = "https://viacep.com.br/ws/{}/json/".format(cep)
        # Importa o módulo requests
        import requests
        # Faz a requisição
        r = requests.get(url)
        # Converte o resultado para um dicionário
        endereco = r.json()
        # Verifica se o CEP foi encontrado
        if 'erro' not in endereco:
            # Retorna o endereço
            return endereco
        else:
            # Retorna None
            return None
    else:
        # Retorna None
        return None



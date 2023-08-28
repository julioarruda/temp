import re

def validar_email(email):
    # Define a expressão regular para validar o email
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Verifica se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
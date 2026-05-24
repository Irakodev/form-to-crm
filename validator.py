# Validação dos dados do formulário

CAMPOS = ["nome", "email", "empresa", "mensagem"]

def validar(dados):
    for campo in CAMPOS:
        if campo not in dados:
            print(f"Field '{campo}' is missing.")
            return False
        if not dados[campo].strip():
            print(f"Field '{campo}' is empty.")
            return False

    if "@" not in dados["email"]:
        print("Invalid email.")
        return False

    print("Valid data!")
    return True

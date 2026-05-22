# Validação dos dados do formulário

CAMPOS = ["nome", "email", "empresa", "mensagem"]

def validar(dados):
    for campo in CAMPOS:
        if campo not in dados:
            print(f"❌ Campo '{campo}' está faltando.")
            return False
        if not dados[campo].strip():
            print(f"❌ Campo '{campo}' está vazio.")
            return False

    if "@" not in dados["email"]:
        print("❌ Email inválido.")
        return False

    print("✅ Dados válidos!")
    return True

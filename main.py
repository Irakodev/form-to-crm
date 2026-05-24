from validator import validar
from sheets import salvar

# Dados simulando um formulário preenchido
dados = {
    "nome": "John Smith",
    "email": "john@techcorp.com",
    "empresa": "TechCorp Inc.",
    "mensagem": "I would like to learn more about your services."
}

def processar_formulario(dados):
    print("-" * 40)
    print(" Form-to-CRM")
    print("-" * 40)

    if validar(dados):
        salvar(dados)
    else:
        print("❌ Formulário não enviado. Corrija os erros acima.")

processar_formulario(dados)

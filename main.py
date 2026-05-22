from validator import validar
from sheets import salvar

# Dados simulando um formulário preenchido
dados = {
    "nome": "João Silva",
    "email": "joao@email.com",
    "empresa": "Empresa XYZ",
    "mensagem": "Gostaria de mais informações."
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

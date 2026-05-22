import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import CREDENTIALS_FILE, SPREADSHEET_NAME

# Permissões necessárias para acessar o Google Sheets
ESCOPO = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def conectar():
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ESCOPO)
    cliente = gspread.authorize(credenciais)
    return cliente.open(SPREADSHEET_NAME).sheet1

def salvar(dados):
    try:
        planilha = conectar()
        linha = [dados["nome"], dados["email"], dados["empresa"], dados["mensagem"]]
        planilha.append_row(linha)
        print(f"✅ Dados de '{dados['nome']}' salvos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")
        
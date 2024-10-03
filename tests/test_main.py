import pytest
import pandas as pd

# Função principal do script main.py, encapsulada para teste
from src.main import main_function

def test_password_generation():
    # Executa a função principal para gerar e salvar senhas
    main_function()

    # Carrega o arquivo Excel gerado para validação
    df = pd.read_excel('../src/data/contacts_fictitious_with_passwords.xlsx')

    # Verifica se o número de contatos no arquivo é 20
    assert len(df) == 20, "O número de contatos gerados está incorreto."

    # Verifica se a coluna 'Password' existe no arquivo
    assert 'Password' in df.columns, "A coluna 'Password' não foi encontrada."

    # Verifica se todas as senhas foram geradas corretamente (não estão vazias)
    assert df['Password'].isnull().sum() == 0, "Algumas senhas não foram geradas."

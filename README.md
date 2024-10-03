
# Visuall Aut

Um projeto em Python que utiliza Selenium para gerar senhas e salvá-las em um arquivo Excel. O projeto acessa o site [Visuall](https://www.visuall.store/) para gerar senhas complexas.

## Estrutura do Projeto

```
visuall-aut/
├── src/
│   ├── contacts_fictitious.xlsx                  # Planilha de contatos fictícios
│   └── contacts_fictitious_with_passwords.xlsx   # Planilha de contatos com senhas geradas
├── tests/
│   └── test_main.py                               # Testes automatizados para o script principal
├── main.py                                        # Script principal que gera senhas
├── requirements.txt                               # Lista de dependências do projeto
└── setup.py                                       # Configurações do pacote Python
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/visuall-aut.git
   ```
2. Navegue até o diretório do projeto:

   ```bash
   cd visuall-aut
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para executar o script e gerar as senhas, utilize o seguinte comando:

```bash
python main.py
```

O script irá gerar 20 senhas, copiá-las e salvar na planilha `contacts_fictitious_with_passwords.xlsx`.

## Testes

Para rodar os testes, utilize o `pytest`:

```bash
pytest tests/test_main.py
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/SeuRecurso
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m 'Adiciona um novo recurso'
   ```
4. Envie a branch para o repositório remoto:
   ```bash
   git push origin feature/SeuRecurso
   ```
5. Abra um Pull Request.

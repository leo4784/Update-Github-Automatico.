# GitHub Project Uploader

Uma aplicação simples com interface gráfica para fazer upload de seus projetos para o GitHub.

## Requisitos

- Python 3.6 ou superior
- Git instalado e configurado no seu computador
- Token de acesso do GitHub

## Como usar

1. Primeiro, instale as dependências:
```
pip install -r requirements.txt
```

2. Execute o programa:
```
python github_uploader.py
```

3. Na interface do programa:
   - Cole seu token do GitHub
   - Digite o nome do repositório
   - Adicione uma descrição (opcional)
   - Selecione a pasta do seu projeto
   - Clique em "Upload to GitHub"

## Como obter um token do GitHub

1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Selecione os seguintes escopos:
   - repo
   - workflow
4. Gere o token e copie-o
5. Cole o token no programa

## Observações

- O token será salvo localmente para uso futuro
- Certifique-se de que a pasta do projeto não está vazia
- O repositório será criado como público por padrão

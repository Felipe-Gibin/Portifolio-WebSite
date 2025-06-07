# Portfólio WebSite

Este é um projeto de portfólio pessoal desenvolvido com Django. Ele permite gerenciar projetos, tags, contatos e possui uma área administrativa personalizada.

## Funcionalidades

- Listagem e detalhamento de projetos
- Filtro por tags
- Área administrativa customizada para gerenciamento de projetos, tags e emails recebidos
- Formulário de contato com validação e envio de email
- Upload de imagens para projetos e tags

## Estrutura do Projeto

```
admin_app/         # App administrativo customizado
main_app/          # App principal (home, sobre, contato)
projects_app/      # App de projetos
base_static/       # Arquivos estáticos globais (CSS, JS, imagens)
base_templates/    # Templates base e parciais globais
media/             # Uploads de imagens
utils/             # Scripts utilitários
manage.py          # Script de gerenciamento Django
requirements.txt   # Dependências do projeto
.env-example       # Exemplo de variáveis de ambiente
```

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/Felipe-Gibin/Portifolio-WebSite.git
   cd Portifolio-WebSite
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie `.env-example` para `.env` e preencha os valores necessários.

5. Execute as migrações:
   ```sh
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Scripts Úteis

- Rodar migrações automaticamente:
  ```sh
  sh utils/migrations.sh
  ```

## Licença

Distribuído sob a [GNU GPL v3](LICENSE).

---
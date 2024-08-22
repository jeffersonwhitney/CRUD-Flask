# CRUD-Flask

Visão Geral

Este aplicativo web full-stack permite que os usuários gerenciem sua coleção de livros em formato PDF. Ele oferece uma interface simples para realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em livros.

Pagina do projeto no replit.com
https://replit.com/@jeffersonwhitne/CRUD-Flask?v=1#main.py

Funcionalidades Implementadas

CRUD de Livros:
Upload de livros em PDF: Os usuários podem enviar seus livros em formato PDF para o sistema.
Listagem de livros: Uma lista de todos os livros enviados é exibida, com opções para editar ou excluir cada livro.
Exclusão de livros: Os usuários podem remover livros da sua coleção.
(Em desenvolvimento) Edição de livros: A funcionalidade de edição de livros está em desenvolvimento.

Tecnologias Utilizadas

Frontend: HTML, CSS
Backend: Flask (framework web Python)
Banco de Dados: SQLite
ORM: Flask-SQLAlchemy (para interagir com o banco de dados)
Migrações: Flask-Migrate (para gerenciar o esquema do banco de dados)
Upload de Arquivos: Werkzeug (para lidar com o upload de arquivos)

Funcionalidades Futuras (Ainda não Implementadas)

Q&A com Langchain: A integração com o Langchain para perguntas e respostas sobre o conteúdo dos livros ainda não foi implementada.
Docker: A conteinerização da aplicação com Docker ainda não foi realizada.
Edição de livros: A funcionalidade completa de edição de livros ainda está em desenvolvimento.

Instalação e Execução

Clone o repositório:

Bash
git clone https://github.com/<seu-usuario>/CRUD-Flask.git 

Crie um ambiente virtual:

Bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Instale as dependências:

Bash
pip install -r requirements.txt   


Configure o banco de dados:

Bash
flask db init
flask db migrate
flask db upgrade

Execute a aplicação:

Bash
flask run

A aplicação estará acessível em http://127.0.0.1:5000/ no seu navegador.

Como Usar

Acesse a aplicação: Abra o seu navegador e vá para http://127.0.0.1:5000/.
Adicione um livro: Clique no link "Adicionar livro" e preencha o formulário com o nome do livro e o arquivo PDF.
Liste os livros: Clique no link "Listar livros" para ver a lista de todos os livros cadastrados.
Exclua um livro: Clique no link "Excluir" ao lado do livro que você deseja remover.

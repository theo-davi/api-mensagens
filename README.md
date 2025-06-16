# API de Mensagens com Python Flask
## O que é um módulo?
É um arquivo (.py) contendo definições e instruções Python.
## O que é um pacote?
É uma pasta com uma coleção de módulos.
## O que é uma biblioteca?
É um conjunto de códigos desenvolvidos com um objetivo específico para ser reutilizado. O Bootstrap, por exemplo, é uma biblioteca de HTMl e CSS (continuar)
## O que é um framework?
## O que é uma classe? E um objeto?
## O que é uma função?
## O que é um ORM? O que é SQLAlchemy?
ORM é a sigla para Object-Relational Mapping, que significa Mapeamento Objeto-Relacional. No Flask, é responsável por mapear as classes que são modelos para tabelas do banco de dados, identificadas por herdarem da classe Model do Flask SQLAlchemy, o ORM do Flask.
## O que é uma migração?
## URL e URI
## Decoradores
### @errorhandler
Registra (decora) funções para tratar / manipular erros específicos.
## Método dunder
# Referências
https://www.rocketseat.com.br/blog/artigos/post/como-criar-api-com-flask-em-python
https://balta.io/blog/o-que-e-um-framework#oqueeumframework
# Projeto
## 1ª atividade
### Gerenciar recurso de usuário
(ID, email, nome, senha)
### Criar relação com mensagem
Ao criar:
- API associa um usuário padrão de ID (1).
- Não permite alterações de Usuário de Mensagem.

OBS.:
- ID de Usuário é chave primária.
- email deve ser único.
- nome não deve ser vazio.
- formato de email válido.
- regras para senhas:
  - min. de 8 caracteres.
  - precisa ter:
    - dígito.
    - caractere especial (@, #, !, %, *, ?, &)
    - letra maiúscula.
    - letra minúscula.

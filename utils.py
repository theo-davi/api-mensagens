from flask_sqlalchemy import SQLAlchemy
'''
importa, do pacote flask_sqlalchemy, a classe SQLAlchemy, que é um ORM, sigla para Object-Relational Mapping, que significa Mapeamento
Objeto-Relacional, que, no Flask, é responsável por mapear as classes que são modelos para tabelas do banco de dados, identificadas por herdarem
da classe Model do SQLAlchemy. Assim, mapeia as classes que herdam de Model para se tornarem tabelas do banco de dados. Por
serem classes, a manipulação de dados pode ser feita de forma orientada a objetos (com criação de objetos e uso de métodos - funções), e não há necessidade de
usar SQL diretamente.
'''
db = SQLAlchemy()#cria uma instância da classe SQLAlchemy, usada para gerenciar o banco de dados, ou seja, cria o banco de dados.
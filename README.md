# CRUD SQLite

CRUD desenvolvido em **Python** utilizando **SQLite** para praticar operações de banco de dados e integração com Python.

O projeto implementa as principais operações de manipulação de registros — **Create, Read, Update e Delete (CRUD)** — utilizando uma tabela de clientes.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![python-dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=for-the-badge\&logo=python\&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

## Sobre o projeto

Este projeto foi desenvolvido para praticar a integração entre **Python e bancos de dados relacionais**, utilizando o SQLite através do módulo `sqlite3`.

A aplicação trabalha com uma tabela `clientes`, contendo:

* `id` — identificador único do cliente
* `nome` — nome do cliente
* `email` — e-mail do cliente

A conexão com o banco é criada utilizando o nome definido no arquivo `.env`.

## Funcionalidades

* Criação da tabela `clientes`
* Cadastro de um cliente
* Cadastro de vários clientes utilizando `executemany()`
* Listagem dos clientes
* Busca de cliente por ID
* Atualização de cliente
* Exclusão de cliente
* Ordenação dos clientes por nome
* Utilização de variáveis de ambiente para configuração do banco

## Estrutura do projeto

```text
CRUD_SQLite/
│
├── .gitignore
├── conexao_criar_tabela.py
├── create.py
├── delete.py
├── inserir_varios.py
├── read.py
├── recuperar_id.py
└── update.py
```

### Descrição dos arquivos

| Arquivo                   | Função                                                              |
| ------------------------- | ------------------------------------------------------------------- |
| `conexao_criar_tabela.py` | Carrega as configurações, cria a conexão com SQLite e cria a tabela |
| `create.py`               | Insere um novo cliente                                              |
| `inserir_varios.py`       | Insere vários clientes de uma vez                                   |
| `read.py`                 | Lista todos os clientes ordenados por nome                          |
| `recuperar_id.py`         | Busca um cliente pelo ID                                            |
| `update.py`               | Atualiza nome e e-mail de um cliente                                |
| `delete.py`               | Exclui um cliente pelo ID                                           |

## Banco de dados

A tabela utilizada pelo projeto possui a seguinte estrutura:

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150)
);
```

O banco é criado pelo próprio SQLite a partir do nome definido na variável de ambiente.

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/leonardodiello/CRUD_SQLite.git
```

Entre na pasta:

```bash
cd CRUD_SQLite
```

### 2. Crie um ambiente virtual

No macOS/Linux:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

### 3. Instale a dependência

O projeto utiliza `python-dotenv`:

```bash
pip install python-dotenv
```

O módulo `sqlite3` utilizado pelo projeto faz parte da biblioteca padrão do Python.

### 4. Configure o `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
nome_banco=clientes.db
```

O arquivo `.env` não deve ser versionado no Git.

## Executando o projeto

Primeiro, execute o arquivo responsável pela conexão e criação da tabela:

```bash
python conexao_criar_tabela.py
```

Depois, você pode executar individualmente cada operação.

### Create

Para cadastrar um cliente:

```bash
python create.py
```

O programa solicitará:

```text
Digite o nome do cliente que deseja cadastrar:
Digite o email do cliente:
```

### Inserção de vários registros

Para inserir vários clientes:

```bash
python inserir_varios.py
```

A inserção utiliza `executemany()` para executar o mesmo comando com diferentes conjuntos de dados.

### Read

Para listar os clientes:

```bash
python read.py
```

Os registros são recuperados utilizando:

```sql
SELECT * FROM clientes ORDER BY nome
```

### Recuperar por ID

Para buscar um cliente específico:

```bash
python recuperar_id.py
```

Informe o ID solicitado pelo programa.

A consulta utiliza:

```sql
SELECT * FROM clientes WHERE id = ?
```

### Update

Para atualizar um cliente:

```bash
python update.py
```

O programa solicita:

* Novo nome
* Novo e-mail
* ID do cliente

A atualização utiliza:

```sql
UPDATE clientes
SET nome = ?, email = ?
WHERE id = ?
```

### Delete

Para excluir um cliente:

```bash
python delete.py
```

Informe o ID do cliente que deseja excluir.

A operação utiliza:

```sql
DELETE FROM clientes
WHERE id = ?
```

## Conceitos praticados

Este projeto foi desenvolvido principalmente para praticar:

* Python e funções
* Manipulação de bancos de dados
* SQLite
* SQL
* Conexões com banco de dados
* `cursor`
* `commit()`
* `fetchall()`
* `execute()`
* `executemany()`
* Queries parametrizadas
* Variáveis de ambiente
* Organização de operações CRUD

## Fluxo da aplicação

```text
Python
   │
   ▼
sqlite3
   │
   ▼
SQLite
   │
   ▼
clientes
   │
   ├── CREATE
   ├── READ
   ├── UPDATE
   └── DELETE
```

## Próximas melhorias

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Separar melhor a camada de conexão da camada de operações
* [ ] Utilizar `with` para gerenciamento das conexões
* [ ] Adicionar validação de nome e e-mail
* [ ] Criar tratamento de exceções
* [ ] Criar uma interface de terminal com menu
* [ ] Adicionar testes automatizados
* [ ] Criar uma API REST com FastAPI
* [ ] Implementar uma interface web
* [ ] Adicionar `requirements.txt`
* [ ] Melhorar a documentação das funções

## Objetivo

O objetivo deste projeto é consolidar os conhecimentos de **Python, SQL e bancos de dados**, praticando a implementação das operações fundamentais de um sistema de persistência de dados.

## Autor

**Leonardo Diello Charão**

Estudante de Engenharia de Software — IFAM

[![GitHub](https://img.shields.io/badge/GitHub-leonardodiello-181717?style=for-the-badge\&logo=github)](https://github.com/leonardodiello)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Leonardo%20Diello-0A66C2?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/leonardo-diello/)

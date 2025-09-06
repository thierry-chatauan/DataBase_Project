# Database Project - Sistema de Controle de Trabalhos Industriais

## 📋 Visão Geral

Este é um sistema web desenvolvido em Flask para controle e registro de trabalhos industriais, permitindo o gerenciamento de operações de máquinas, operadores e clientes. O projeto foi desenvolvido como parte de uma atribuição de banco de dados e demonstra a implementação de uma aplicação web completa com interface de usuário e persistência de dados.

## 🚀 Funcionalidades

### Principais Recursos

- **Sistema de Login**: Autenticação simples com credenciais fixas (admin/machinery)
- **Registro de Trabalhos**: Formulário para cadastro de novos trabalhos industriais
- **Visualização de Dados**: Tabela com todos os trabalhos registrados
- **Cálculo Automático**: Cálculo automático do tempo total de trabalho
- **Interface Responsiva**: Design moderno com CSS e Font Awesome

### Dados Gerenciados

- **Operador**: Nome do operador responsável
- **Máquina**: Tipo de máquina utilizada (Doosan 5700, Doosan 6700)
- **Cliente**: Nome do cliente
- **Número do Desenho**: Identificação do desenho/projeto
- **Data e Hora de Início**: Timestamp de início do trabalho
- **Data e Hora de Fim**: Timestamp de conclusão do trabalho
- **Tempo Total**: Cálculo automático da duração do trabalho

## 🛠️ Tecnologias Utilizadas

### Backend

- **Python 3.x**
- **Flask**: Framework web minimalista
- **SQLAlchemy**: ORM para manipulação do banco de dados
- **PostgreSQL**: Banco de dados principal (configurável)

### Frontend

- **HTML5**: Estrutura das páginas
- **CSS3**: Estilização e layout responsivo
- **JavaScript**: Validação de formulários e interatividade
- **Font Awesome**: Ícones para interface
- **Google Fonts**: Tipografia (Open Sans)

### Banco de Dados

- **SQLite**: Banco de dados local para desenvolvimento
- **PostgreSQL**: Banco de dados de produção (configurável)

## 📁 Estrutura do Projeto

```
DataBase_Project/
├── app.py                 # Aplicação principal Flask
├── models.py              # Modelos de dados (SQLAlchemy)
├── config.py              # Configurações da aplicação
├── instance/
│   └── mydb.db           # Banco de dados SQLite local
├── static/
│   ├── css/
│   │   └── styles.css    # Estilos CSS
│   └── js/
│       └── login.js      # Scripts JavaScript
├── templates/
│   ├── base.html         # Template base
│   ├── home.html         # Página principal
│   ├── login.html        # Página de login
│   └── newRegister.html  # Formulário de registro
└── 4_Databases_Assignment.pdf  # Documentação da atribuição
```

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação das Dependências

```bash
pip install flask flask-sqlalchemy psycopg2-binary
```

### Configuração

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd DataBase_Project
```

2. Configure as variáveis de ambiente (opcional):

```bash
# Para PostgreSQL
export DATABASE_URL="postgresql://usuario:senha@localhost:5432/database_project"
export SECRET_KEY="sua-chave-secreta"
```

### Execução

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 🔧 Configuração do Banco de Dados

### SQLite (Desenvolvimento)

Por padrão, a aplicação usa SQLite para desenvolvimento. O banco de dados é criado automaticamente na pasta `instance/`.

### PostgreSQL (Produção)

Para usar PostgreSQL, configure a variável de ambiente `DATABASE_URL`:

```bash
export DATABASE_URL="postgresql://usuario:senha@localhost:5432/database_project"
```

## 📊 Modelo de Dados

### Tabela: jobs

| Campo          | Tipo       | Descrição                        |
| -------------- | ---------- | -------------------------------- |
| id             | Integer    | Chave primária (auto-incremento) |
| name           | String(50) | Nome do operador                 |
| machine        | String(50) | Tipo de máquina                  |
| costumer       | String(50) | Nome do cliente                  |
| drawing_number | String(50) | Número do desenho                |
| start_date     | Date       | Data de início                   |
| start_time     | Time       | Hora de início                   |
| end_date       | Date       | Data de fim                      |
| end_time       | Time       | Hora de fim                      |
| total_time     | Time       | Tempo total calculado            |

## 🎯 Rotas da Aplicação

- **GET /** - Página de login
- **GET /home** - Página principal com lista de trabalhos
- **GET /newRegister** - Formulário de novo registro
- **POST /newRegister** - Processamento do formulário de registro

## 🔐 Autenticação

O sistema utiliza autenticação simples com credenciais fixas:

- **Usuário**: admin
- **Senha**: machinery

## 🎨 Interface do Usuário

### Características do Design

- **Layout Responsivo**: Adaptável a diferentes tamanhos de tela
- **Design Moderno**: Interface limpa e profissional
- **Navegação Intuitiva**: Menu de navegação com ícones
- **Feedback Visual**: Mensagens de sucesso e erro
- **Tabela Organizada**: Visualização clara dos dados

### Páginas

1. **Login**: Formulário de autenticação
2. **Home**: Lista de todos os trabalhos registrados
3. **New Register**: Formulário para cadastro de novos trabalhos

## 🔄 Evolução do Projeto

### Versão Atual (1.0)

- ✅ Sistema de autenticação básico
- ✅ CRUD completo para trabalhos
- ✅ Interface web responsiva
- ✅ Cálculo automático de tempo
- ✅ Integração com banco de dados
- ✅ Validação de formulários

### Melhorias Identificadas para Futuras Versões

- 🔄 Sistema de autenticação mais robusto
- 🔄 Validação de dados no backend
- 🔄 Relatórios e estatísticas
- 🔄 Filtros e busca na listagem
- 🔄 Edição e exclusão de registros
- 🔄 Sistema de usuários com diferentes níveis
- 🔄 API REST para integração
- 🔄 Testes automatizados
- 🔄 Documentação da API

## 🐛 Problemas Conhecidos

1. **Bug no Cálculo de Tempo**: Linha 49-51 em `app.py` contém código não utilizado que pode causar erros
2. **Validação de Dados**: Falta validação no backend para os dados do formulário
3. **Segurança**: Credenciais hardcoded no JavaScript
4. **Tabela Home**: Coluna "End time" mostra "End date" (linha 32 em home.html)

## 📝 Notas de Desenvolvimento

### Decisões Técnicas

- **Flask**: Escolhido por sua simplicidade e flexibilidade
- **SQLAlchemy**: ORM robusto para manipulação de dados
- **Template Engine**: Jinja2 para renderização de templates
- **CSS Puro**: Sem frameworks para manter simplicidade

### Padrões Utilizados

- **MVC**: Separação clara entre modelo, visualização e controle
- **Template Inheritance**: Reutilização de código HTML
- **Configuration Management**: Configurações centralizadas
- **Error Handling**: Tratamento básico de erros

## 👥 Contribuição

Este projeto foi desenvolvido como parte de uma atribuição acadêmica. Para contribuições:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é parte de uma atribuição acadêmica. Consulte o arquivo `4_Databases_Assignment.pdf` para mais detalhes sobre os requisitos e especificações.

## 📞 Contato

Para dúvidas ou sugestões sobre este projeto, entre em contato através dos canais apropriados do repositório.

---

**Desenvolvido como parte de uma atribuição de banco de dados - 2025**

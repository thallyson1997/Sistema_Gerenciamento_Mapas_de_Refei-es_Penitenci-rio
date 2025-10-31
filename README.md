# SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário

## Sobre o Projeto

O SGMRP é um sistema web desenvolvido em Python/Flask para gerenciar e monitorar o fornecimento de refeições em unidades prisionais do Estado. O objetivo é substituir o uso de planilhas Excel fragmentadas por uma solução centralizada, automatizada e segura, facilitando a gestão administrativa e o controle de conformidade dos lotes contratuais.

## Funcionalidades Disponíveis

- Autenticação de usuários (login/logout, aprovação administrativa)
- Cadastro de novos usuários (com aprovação do administrador)
- Dashboard com visão geral dos lotes e unidades
- Listagem de lotes e detalhes individuais de cada lote
- Exportação dinâmica de dados para planilhas Excel (modelo.xlsx)
- APIs RESTful para operações básicas (adicionar/excluir dados, entrada manual, adicionar SIISP, listar lotes/unidades/usuários, validação de campos)
- Sistema de permissões (admin x usuário comum)
- Proteção de dados sensíveis via .gitignore

## Restrições e Observações

- **Os arquivos de dados reais (.json) NÃO estão disponíveis no repositório** por questões de segurança e privacidade. Apenas arquivos de exemplo ou estrutura vazia podem ser fornecidos para desenvolvimento.
- O sistema depende dos arquivos JSON em `dados/` para funcionar plenamente (usuarios.json, lotes.json, unidades.json, mapas.json). Para testes, crie arquivos de exemplo ou solicite ao administrador.
- O arquivo modelo.xlsx deve estar presente em `dados/` para exportação de planilhas.

## Estrutura do Projeto

```
Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/
├── main.py                # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── dados/                 # Base de dados JSON (NÃO disponível no repositório)
│   ├── modelo.xlsx        # Modelo de planilha Excel para exportação
│   ├── usuarios.json      # Controle de usuários
│   ├── lotes.json         # Dados dos lotes
│   ├── unidades.json      # Dados das unidades
│   └── mapas.json         # Dados de refeições
├── templates/             # Templates HTML (Jinja2)
├── static/                # Arquivos estáticos (CSS)
└── README.md              # Documentação do projeto
```

## Instalação e Execução

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes)

### Passos para Instalar

1. Clone o repositório:
	```bash
	git clone https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio.git
	cd Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio
	```
2. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```
3. Certifique-se de que o arquivo `modelo.xlsx` está presente em `dados/`.
4. Crie arquivos JSON de exemplo em `dados/` se necessário para testes locais.
5. Execute a aplicação:
	```bash
	python main.py
	```
6. Acesse o sistema em [http://localhost:5000](http://localhost:5000)

### Credenciais Padrão
- Administrador: `admin@seap.gov.br` / `admin123`
- Usuário alternativo: `admin` / `admin123`
- Novos usuários podem se cadastrar via `/cadastro` (necessita aprovação do admin)

## Principais Rotas e APIs

- `/`                : Página inicial
- `/login`           : Login de usuário
- `/cadastro`        : Cadastro de usuário
- `/dashboard`       : Painel principal
- `/lotes`           : Listagem de lotes
- `/lote/<id>`       : Detalhes de lote
- `/admin/usuarios`  : Gestão de usuários (admin)

#### APIs RESTful
- `POST /api/adicionar-dados`      : Adicionar dados de mapas
- `DELETE /api/excluir-dados`      : Excluir dados
- `POST /api/entrada-manual`       : Entrada manual de dados
- `POST /api/adicionar-siisp`      : Adicionar dados SIISP
- `GET /api/lotes`                 : Listar lotes
- `GET /api/unidades`              : Listar unidades
- `GET /api/usuarios`              : Listar usuários (admin)
- `POST /api/validar-campo`        : Validação de campo único

## Exportação de Dados para Excel

O sistema permite exportar dados filtrados para uma planilha Excel baseada no modelo fornecido (`modelo.xlsx`). O arquivo gerado inclui:
- Resumo do lote, empresa, mês/ano
- Número do contrato
- Unidades selecionadas e somatório de refeições
- Preços contratuais por tipo de refeição
- Cálculo automático de somas e produtos

## Segurança e Privacidade

- Dados reais de produção NÃO são versionados no Git (protegidos por `.gitignore`)
- Recomenda-se usar arquivos de exemplo para desenvolvimento
- Nunca compartilhe dados sensíveis em ambientes públicos

## Licença

Este projeto está licenciado sob a GNU General Public License v3.0. Consulte o arquivo LICENSE para detalhes.

## Contato

Desenvolvedor: Thallyson Gabriel Martins Correia Fontenele  
Email: thallysong10@hotmail.com  
Órgão: SEAP/SFA

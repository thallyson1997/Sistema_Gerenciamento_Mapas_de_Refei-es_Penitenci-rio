# SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário

## 📋 Sobre o Projeto

O **SGMRP** é uma aplicação web completa desenvolvida em **Flask** para gerenciar e monitorar o fornecimento de refeições em unidades prisionais, criado para modernizar e otimizar o processo atualmente realizado através de múltiplas planilhas Excel no âmbito da **SEAP (Secretaria de Estado de Administração Penitenciária)**.

### 🎯 Objetivo Principal
Centralizar o controle de dados de refeições fornecidas aos internos, permitindo comparação automática com dados do SIISP, facilitando a gestão administrativa das unidades prisionais e substituindo o modelo atual baseado em planilhas Excel fragmentadas.

### 👨‍💻 Desenvolvedor
**Thallyson Gabriel Martins Correia Fontenele**  
Matrícula: 2022024639  
Órgão: SEAP - Secretaria de Estado de Administração Penitenciária  
Setor: SFA - Subsecretaria de Administração

## 🚀 Status Atual - Sistema Flask Completo e Funcional (v2.0)

Este repositório contém uma **aplicação Flask totalmente funcional** com backend robusto, frontend responsivo e sistema de dados JSON estruturado. O sistema está em produção ativa com recursos avançados de gestão de dados de refeições penitenciárias.

### ✅ Funcionalidades Implementadas

#### 🖥️ Backend Flask Completo
- **Framework**: Flask 3.1.2 com Jinja2 templating
- **Arquitetura**: MVC Pattern com separação clara de responsabilidades
- **Autenticação**: Sistema completo de login/logout com sessões Flask
- **Base de Dados**: Sistema JSON estruturado (`usuarios.json`, `lotes.json`, `unidades.json`, `mapas.json`)
- **APIs RESTful**: Endpoints completos para todas as operações CRUD
- **Validação**: Validação server-side robusta com feedback em tempo real
- **Gestão de Usuários**: Sistema completo de cadastro, aprovação e controle de acesso

#### 🏠 Páginas e Rotas Implementadas

**Páginas Públicas:**
- **Landing Page (`/`)**: Apresentação completa do sistema com hero section e funcionalidades
- **Login (`/login`)**: Autenticação real com validação contra banco de dados
- **Cadastro (`/cadastro`)**: Registro de usuários com aprovação administrativa

**Páginas Autenticadas:**
- **Dashboard (`/dashboard`)**: Painel principal com visão geral dos 9 lotes contratuais
- **Lista de Lotes (`/lotes`)**: Visualização completa dos lotes com filtros avançados
- **Detalhes do Lote (`/lote/<id>`)**: Páginas dinâmicas individuais para cada lote (1-9)

**Área Administrativa:**
- **Gestão de Usuários (`/admin/usuarios`)**: Interface para aprovação/revogação de usuários (admin apenas)

#### 🍽️ Sistema de Dados de Refeições

**Estrutura de Dados Completa:**
- **9 Lotes Contratuais**: Dados reais com empresas e contratos específicos
- **36 Unidades Prisionais**: Presídios e delegacias organizados por lote
- **8 Tipos de Refeição**: Café, Almoço, Lanche, Jantar (internos e funcionários)
- **Dados SIISP**: Integração para comparação e validação
- **Preços por Refeição**: Valores contratuais detalhados por lote

**Funcionalidades de Dados:**
- **Importação Automática**: Upload e processamento de dados via texto/PDF
- **Entrada Manual**: Interface para registro manual de dados diários
- **Validação Inteligente**: Verificação automática de consistência de dados
- **Comparação SIISP**: Cálculo automático de diferenças e conformidade
- **Filtros Avançados**: Por período, unidade, tipo de refeição
- **Indicadores Visuais**: Código de cores para conformidade/divergências

#### 📊 APIs e Integração

**APIs RESTful Implementadas:**
- `POST /api/adicionar-dados` - Adicionar dados de mapas via texto/PDF
- `DELETE /api/excluir-dados` - Exclusão de dados específicos
- `POST /api/entrada-manual` - Entrada manual de dados diários
- `POST /api/adicionar-siisp` - Adicionar dados SIISP para comparação
- `GET /api/lotes` - Listar todos os lotes
- `GET /api/unidades` - Listar todas as unidades
- `GET /api/usuarios` - Gestão de usuários (admin apenas)
- `POST /api/validar-campo` - Validação em tempo real

#### 🎨 Frontend Responsivo

**Design System Profissional:**
- **CSS3 Avançado**: Grid layout, flexbox, custom properties, animações
- **Responsividade**: Mobile-first com breakpoints otimizados
- **Tema Consistente**: Esquema de cores azul profissional (#2c5282)
- **Componentes**: Sistema de cards, formulários, tabelas e botões padronizados
- **UX/UI**: Interface intuitiva com feedback visual imediato

**JavaScript ES6+:**
- **Filtros Dinâmicos**: Filtragem de dados em tempo real
- **Validação Client-side**: Feedback imediato para formulários
- **Interações**: Tabelas interativas, modais e componentes dinâmicos
- **Progressive Enhancement**: Funciona sem JavaScript habilitado

#### 🔐 Sistema de Autenticação e Segurança

**Controle de Acesso:**
- **Login/Logout**: Sistema completo com sessões Flask
- **Níveis de Usuário**: Admin (ID=1) e usuários regulares
- **Aprovação**: Sistema de aprovação administrativa para novos usuários
- **Proteção de Rotas**: Middleware para páginas autenticadas
- **Validação de Dados**: Sanitização e validação de inputs

**Dados Sensíveis:**
- **Proteção Git**: Arquivo `.gitignore` protegendo dados reais
- **Desenvolvimento Seguro**: Arquivos de exemplo para desenvolvimento
- **Logs Protegidos**: Sistema de logs sem exposição de dados sensíveis

#### 🍽️ Sistema de Refeições com Dados Reais
- **Integração Completa**: Dados reais de 60 registros (30 dias × 2 unidades)
- **8 Tipos de Refeição**: Café da manhã, Almoço, Lanche da tarde, Jantar, Ceia, Lanche noturno, Café especial, Almoço especial
- **Filtros Avançados**: 
  - **Filtro de Período**: Seleção personalizada de datas com conversão automática de formato brasileiro (DD/MM/YYYY)
  - **Filtro de Unidades**: Multi-seleção com interface popup, permitindo filtrar por unidades específicas
- **Dupla Visualização**:
  - **Aba "Dados Refeição"**: Tabela dinâmica com dados reais integrados via Flask
  - **Aba "Comparação SIISP"**: Comparação visual com código de cores
- **Indicadores Visuais**: Código de cores para conformidade/divergências

#### 📊 APIs e Integração

**APIs RESTful Implementadas:**
- `POST /api/adicionar-dados` - Adicionar dados de mapas via texto/PDF
- `DELETE /api/excluir-dados` - Exclusão de dados específicos
- `POST /api/entrada-manual` - Entrada manual de dados diários
- `POST /api/adicionar-siisp` - Adicionar dados SIISP para comparação
- `GET /api/lotes` - Listar todos os lotes
- `GET /api/unidades` - Listar todas as unidades
- `GET /api/usuarios` - Gestão de usuários (admin apenas)
- `POST /api/validar-campo` - Validação em tempo real

#### 📊 Gestão de Lotes com Arquitetura Normalizada
- **9 Lotes Contratuais**: Dados reais com empresas e unidades específicas
- **Informações Dinâmicas**: Nome, empresa, contrato, data de início
- **Unidades por Lote**: Lista específica de presídios/delegacias por lote
- **Status de Conformidade**: Cálculo automático de indicadores
- **Filtros Inteligentes**: Mês anterior como padrão (sincronizado)

#### 🎨 Design System & UX
- **Identidade Visual**: Esquema de cores azul profissional (#2c5282)
- **Responsividade**: Layout adaptativo para desktop, tablet e mobile
- **Acessibilidade**: Contraste adequado e navegação por teclado
- **Componentes**: Sistema de cards, formulários, tabelas e botões padronizados
- **Feedback Visual**: Notificações, alertas e validações em tempo real

#### 🔧 Funcionalidades Técnicas
- **Base de Dados JSON**: 
  - `dados/usuarios.json`: Controle de usuários e permissões
  - `dados/lotes.json`: Informações estruturadas dos 9 lotes
- **Templating Jinja2**: Renderização dinâmica server-side
- **Sessões Flask**: Controle de estado e autenticação
- **Roteamento RESTful**: URLs semânticas e organizadas
- **Validação Completa**: Backend + Frontend com feedback imediato

## 📁 Estrutura do Projeto

```
Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/
├── main.py                    # Aplicação Flask principal (1625+ linhas)
├── requirements.txt           # Dependências Python (Flask 3.1.2)
├── .gitignore                # Proteção de dados sensíveis
├── PRD.txt                   # Documento de Requisitos do Produto
├── LICENSE                   # GNU General Public License v3.0
├── dados/                    # Base de dados JSON estruturada
│   ├── usuarios.json         # Controle de usuários e permissões
│   ├── lotes.json           # Dados dos 9 lotes contratuais
│   ├── unidades.json        # 36 unidades prisionais organizadas
│   ├── mapas.json           # Dados de refeições (protegido)
│   └── mapas_exemplo.json   # Exemplo vazio para desenvolvimento
├── templates/               # Templates Jinja2
│   ├── index.html           # Landing page dinâmica
│   ├── login.html           # Autenticação com validação
│   ├── cadastro.html        # Registro com aprovação admin
│   ├── dashboard.html       # Painel principal com dados reais
│   ├── lotes.html           # Lista de lotes com filtros
│   └── lote-detalhes.html   # Detalhes dinâmicos por lote
├── static/                  # Arquivos estáticos
│   └── css/
│       └── style.css        # Sistema de design completo (500+ linhas)
├── Arquivos de documentação legacy (mantidos para referência):
│   ├── dashboard.html       # Interface principal (anterior)
│   ├── lotes.html          # Lista de lotes (anterior)
│   ├── lote-detalhes.html  # Detalhes por lote (anterior)
│   └── css/style.css       # Estilos (anterior)
└── README.md               # Esta documentação
```

## 🔒 Proteção de Dados Sensíveis

**⚠️ IMPORTANTE**: Este sistema lida com dados sensíveis do sistema penitenciário. A proteção de dados é **CRÍTICA**.

### Arquivos Protegidos pelo `.gitignore`:
- `dados/mapas.json` - Dados reais de produção
- `dados/backup_*.json` - Backups de dados
- `*.log` - Logs do sistema
- `.env*` - Variáveis de ambiente
- Arquivos temporários e do sistema

### Como Usar com Segurança:
- **Desenvolvimento**: Use `dados/mapas_exemplo.json` (vazio, seguro para Git)
- **Produção**: Use `dados/mapas.json` (protegido, não vai para Git)
- **Verificação**: Execute `git status` - arquivos protegidos não devem aparecer

## �🛠️ Tecnologias Utilizadas

### Backend (Implementado)
- **Python 3.11+**: Linguagem principal
- **Flask 3.1.2**: Framework web minimalista e flexível
- **Jinja2**: Template engine para renderização dinâmica
- **JSON**: Base de dados estruturada para persistência
- **Session Management**: Controle de estado e autenticação

### Frontend (Implementado)
- **HTML5**: Estrutura semântica moderna
- **CSS3**: Grid layout, flexbox, custom properties, animations
- **JavaScript ES6+**: Módulos, arrow functions, async/await
- **Responsive Design**: Mobile-first approach com breakpoints
- **Progressive Enhancement**: Funciona sem JavaScript habilitado

### Arquitetura
- **MVC Pattern**: Separação clara de responsabilidades
- **RESTful Routes**: URLs semânticas e organizadas
- **Component-Based CSS**: Sistema de design escalável
- **File-Based Database**: JSON estruturado para prototipagem rápida

## 🎯 Próximas Etapas de Desenvolvimento

### Fase 3 - Funcionalidades de Dados (Em Planejamento)
1. **Tabelas Dinâmicas**: Integração real dos dados de refeições via Flask
2. **Import/Export**: Upload de PDFs e planilhas Excel
3. **Relatórios Avançados**: Geração automática de relatórios consolidados
4. **Integração SIISP**: API para sincronização de dados externos

### Fase 4 - Aprimoramentos (Futuro)
1. **Banco de Dados**: Migração de JSON para PostgreSQL
2. **Notificações**: Sistema de alertas automáticos por e-mail
3. **Auditoria**: Log completo de alterações e acessos
4. **Dashboard Analytics**: Gráficos e métricas avançadas

### Fase 5 - Deploy e Produção
1. **Containerização**: Docker para ambiente de produção
2. **CI/CD**: GitHub Actions para deploy automatizado
3. **Segurança**: HTTPS, CSP headers, rate limiting
4. **Monitoramento**: Logs centralizados e métricas de performance

## 🚀 Instalação e Execução

### Pré-requisitos
- **Python 3.11+** instalado
- **pip** para gestão de pacotes
- Navegador moderno (Chrome, Firefox, Safari, Edge)

### Passos de Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio.git

# 2. Navegue para o diretório
cd Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio

# 3. Instale as dependências
pip install -r requirements.txt
# OU simplesmente:
pip install flask

# 4. Execute a aplicação
python main.py

# 5. Acesse no navegador
# http://localhost:5000
```

### Credenciais de Acesso
- **Administrador**: `admin@seap.gov.br` / `admin123`
- **Usuário Alternativo**: `admin` / `admin123`
- **Novos Usuários**: Podem se cadastrar via `/cadastro` (necessita aprovação admin)

### URLs do Sistema
- **🏠 Página Inicial**: http://localhost:5000/
- **🔐 Login**: http://localhost:5000/login
- **📝 Cadastro**: http://localhost:5000/cadastro
- **📊 Dashboard**: http://localhost:5000/dashboard
- **📋 Lotes**: http://localhost:5000/lotes
- **📄 Lote Específico**: http://localhost:5000/lote/1 (1 a 9)
- **⚙️ Admin Usuários**: http://localhost:5000/admin/usuarios

## 📊 Recursos e Funcionalidades

### 🎯 Gestão de Lotes Contratuais
- **9 Lotes Ativos**: Dados reais com empresas e contratos
- **36 Unidades**: Presídios e delegacias organizados por lote
- **Informações Completas**: Contratos, datas, empresas responsáveis
- **Preços Detalhados**: Valores por tipo de refeição e categoria

### 🍽️ Controle de Refeições
- **8 Tipos de Refeição**: Café, almoço, lanche, jantar (internos/funcionários)
- **Importação Automática**: Processamento de dados via texto/PDF
- **Entrada Manual**: Interface para registro diário manual
- **Validação Inteligente**: Verificação de consistência automática
- **Comparação SIISP**: Cálculo de diferenças e conformidade

### 📈 Indicadores e Relatórios
- **Códigos de Cores**: Verde (OK), amarelo/vermelho (divergências)
- **Filtros Avançados**: Por período, unidade, tipo de refeição
- **Estatísticas**: Cálculo automático de conformidade e desvios
- **Visualização Dupla**: Dados simples vs. comparação SIISP

### 👥 Gestão de Usuários
- **Cadastro Aberto**: Qualquer pessoa pode se registrar
- **Aprovação Admin**: Sistema de aprovação para controle
- **Diferentes Níveis**: Admin vs. usuários regulares
- **Dados Completos**: CPF, telefone, cargo, unidade, matrícula

## 🎯 Próximas Funcionalidades

### Fase 3 - Melhorias de UX/UI
1. **Dashboard Analytics**: Gráficos interativos de consumo
2. **Relatórios PDF**: Geração automática de documentos oficiais
3. **Notificações**: Sistema de alertas por email
4. **Exportação**: Excel, PDF, CSV para relatórios

### Fase 4 - Integração e Escalabilidade
1. **Banco de Dados**: Migração para PostgreSQL
2. **API Externa**: Integração real com SIISP
3. **Backup Automático**: Sistema de backup programado
4. **Auditoria**: Logs completos de alterações

### Fase 5 - Deploy e Produção
1. **Docker**: Containerização para deploy
2. **CI/CD**: GitHub Actions para automação
3. **Segurança**: HTTPS, rate limiting, CSP headers
4. **Monitoramento**: Logs centralizados e métricas

## 🤝 Contribuição e Desenvolvimento

### Como Contribuir
1. **Fork** o repositório
2. **Clone** sua fork localmente
3. **Crie** uma branch para sua feature
4. **Teste** suas mudanças completamente
5. **Commit** com mensagens descritivas
6. **Push** para sua fork
7. **Abra** um Pull Request

### Reportar Bugs
- Use as [**GitHub Issues**](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/issues)
- Inclua **passos para reproduzir**
- **Descreva** o comportamento esperado
- **Anexe** screenshots se necessário

### Sugerir Melhorias
- Abra uma **issue** com rótulo "enhancement"
- **Explique** o problema que a melhoria resolve
- **Detalhe** a solução proposta
- **Justifique** o valor para o usuário

## 📄 Licenciamento

Este projeto está licenciado sob a **GNU General Public License v3.0**. Consulte o arquivo [`LICENSE`](LICENSE) para detalhes completos.

### Resumo da Licença:
- ✅ **Uso Comercial** permitido
- ✅ **Modificação** permitida
- ✅ **Distribuição** permitida
- ✅ **Uso Privado** permitido
- ❗ **Copyleft**: Derivações devem usar a mesma licença
- ❗ **Aviso de Licença**: Deve incluir aviso de licença e copyright

## 📞 Contato e Suporte

### Desenvolvedor
**Thallyson Gabriel Martins Correia Fontenele**  
📧 Email: thallysong10@hotmail.com  
🏢 Matrícula: 2022024639  
🏛️ Órgão: SEAP/SFA  

### Recursos Online
- **📚 Repositório**: [GitHub](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio)
- **🐛 Issues**: [GitHub Issues](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/issues)
- **📋 Documentação**: Este README e arquivo PRD.txt
- **🔄 Releases**: [GitHub Releases](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/releases)

### Suporte Técnico
Para questões técnicas específicas:
1. **Verifique** a documentação primeiro
2. **Busque** issues existentes no GitHub
3. **Abra** nova issue se necessário
4. **Inclua** detalhes completos do problema

---

## 🏆 Sobre o Sistema

O **SGMRP** representa um marco na modernização dos processos administrativos da SEAP, substituindo métodos manuais fragmentados por uma solução tecnológica integrada, eficiente e transparente. 

**Desenvolvido com ❤️ para a SEAP/SFA**  
*Modernizando a gestão penitenciária com tecnologia e eficiência.*

---

**Sistema de Gerenciamento de Mapas de Refeições Penitenciário** © 2025 - Todos os direitos reservados à SEAP.

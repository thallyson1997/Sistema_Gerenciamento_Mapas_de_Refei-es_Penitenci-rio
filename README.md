# SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário

## 📋 Sobre o Projeto

O **SGMRP** é um sistema web desenvolvido para gerenciar e monitorar o fornecimento de refeições em unidades prisionais, criado para modernizar e otimizar o processo atualmente realizado através de múltiplas planilhas Excel no âmbito da **SEAP (Secretaria de Estado de Administração Penitenciária)**.

### 🎯 Objetivo Principal
Centralizar o controle de dados de refeições fornecidas aos internos, permitindo comparação automática com dados do SIISP e facilitando a gestão administrativa das unidades prisionais.

## 🚀 Status Atual - Sistema Flask Funcional com Filtros Avançados (v3.0)

Este repositório contém uma **aplicação Flask completa e funcional** desenvolvida em Python com frontend responsivo em HTML5, CSS3 e JavaScript ES6+. O sistema evoluiu para incluir arquitetura de dados normalizada, sistema de filtros multi-seleção avançados e integração completa de dados reais de refeições.

### ✅ Funcionalidades Implementadas

#### 🖥️ Backend Flask
- **Framework**: Flask 3.1.2 com Jinja2 templating
- **Banco de Dados**: Sistema de arquivos JSON normalizado para máxima eficiência
- **Autenticação**: Sistema de login com sessões Flask
- **Roteamento Dinâmico**: URLs parametrizadas para lotes individuais
- **Gestão de Usuários**: Cadastro, aprovação e controle de acesso
- **Sistema de Dados**: Carregamento e filtragem de mapas de refeições reais

#### 🏠 Páginas Principais
- **Landing Page (`/`)**: Apresentação do sistema com recursos e benefícios
- **Login (`/login`)**: Autenticação real com validação de credenciais
- **Cadastro (`/cadastro`)**: Registro de usuários com aprovação administrativa
- **Dashboard (`/dashboard`)**: Painel dinâmico com dados reais dos lotes
- **Lista de Lotes (`/lotes`)**: Visualização avançada com filtros e busca
- **Detalhes do Lote (`/lote/<id>`)**: Páginas dinâmicas por lote com dados específicos e filtros avançados

#### 🍽️ Sistema de Refeições com Dados Reais
- **Integração Completa**: Dados reais de 60 registros (30 dias × 2 unidades)
- **8 Tipos de Refeição**: Café da manhã, Almoço, Lanche da tarde, Jantar, Ceia, Lanche noturno, Café especial, Almoço especial
- **Filtros Avançados**: 
  - **Filtro de Período**: Seleção personalizada de datas com conversão automática de formato brasileiro (DD/MM/YYYY)
  - **Filtro de Unidades**: Multi-seleção com interface popup, permitindo filtrar por unidades específicas
- **Dupla Visualização**:
  - **Aba "Dados Refeição"**: Tabela dinâmica com dados reais integrados via Flask
  - **Aba "Comparação SIISP"**: Comparação visual com código de cores
- **Indicadores Visuais**: Verde para conformidade, amarelo/vermelho para divergências
- **Importação de Dados**: Interface para upload de PDFs e entrada manual

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

## 📁 Estrutura de Arquivos

```
Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/
├── main.py                 # Aplicação Flask principal
├── requirements.txt        # Dependências Python
├── .env                   # Variáveis de ambiente (não versionado)
├── dados/                 # Base de dados JSON
│   ├── usuarios.json      # Usuários e permissões
│   └── lotes.json        # Dados dos 9 lotes contratuais
├── templates/            # Templates Jinja2
│   ├── index.html        # Landing page
│   ├── login.html        # Autenticação
│   ├── cadastro.html     # Registro de usuários
│   ├── dashboard.html    # Painel principal
│   ├── lotes.html        # Lista de lotes
│   ├── lote-detalhes.html # Detalhes dinâmicos por lote
│   └── admin/            # Área administrativa
│       └── usuarios.html # Gestão de usuários
├── static/              # Arquivos estáticos
│   ├── css/
│   │   └── style.css    # Estilos principais
│   ├── js/              # JavaScript (se necessário)
│   └── assets/          # Imagens e recursos
├── dashboard.html          # Painel principal
├── lotes.html              # Lista de lotes com filtros
├── lote-detalhes.html      # Detalhamento com abas
├── css/
│   └── style.css           # Estilos completos (500+ linhas)
├── LICENSE                 # Licença do projeto
├── PRD.txt                 # Documento de Requisitos
└── README.md              # Documentação (este arquivo)
```

## 🛠️ Tecnologias Utilizadas

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

## 🚀 Como Executar o Sistema

### Pré-requisitos
- **Python 3.11+** instalado
- **pip** para gestão de pacotes
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

### Instalação e Execução
```bash
# Clone o repositório
git clone https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio.git

# Navegue até o diretório
cd Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio

# Instale as dependências
pip install flask

# Execute o servidor Flask
python main.py

# Acesse no navegador:
# http://localhost:5000
```

### Credenciais de Teste
- **Admin**: admin@seap.gov.br / admin123
- **Usuário**: admin / admin123

### URLs Principais
- **Landing Page**: http://localhost:5000/
- **Login**: http://localhost:5000/login  
- **Dashboard**: http://localhost:5000/dashboard
- **Lotes**: http://localhost:5000/lotes
- **Lote Específico**: http://localhost:5000/lote/1 (1-9)
- **Admin**: http://localhost:5000/admin/usuarios

## 📊 Funcionalidades em Destaque

### 🔍 Sistema de Abas Inovador
A página de detalhes do lote possui duas abas que atendem diferentes necessidades:

1. **"Dados de Refeições"**: Visualização simples dos números
2. **"Comparação SIISP"**: Análise visual com cores para identificar divergências

### 📈 Indicadores Visuais Inteligentes
- **Verde**: Número de refeições adequado (≤ população SIISP)
- **Vermelho**: Número de refeições excessivo (> população SIISP)
- **Cinza**: Dados de referência SIISP

### 🔄 Workflow Otimizado
O sistema replica e melhora o fluxo atual de trabalho com planilhas Excel, mantendo a familiaridade dos usuários while adding digital advantages.

## 🤝 Contribuição

Este é um projeto em desenvolvimento para modernização dos processos da SEAP. 

### Feedback e Sugestões
- Abra uma **issue** para reportar bugs
- Envie **pull requests** para melhorias
- Entre em contato para discussões sobre requisitos

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

## 📞 Contato

Para mais informações sobre o projeto ou colaboração:
- **Repositório**: [GitHub](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio)
- **Issues**: [GitHub Issues](https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/issues)

---

**SGMRP** - Modernizando a gestão penitenciária com tecnologia e eficiência. 🏛️✨

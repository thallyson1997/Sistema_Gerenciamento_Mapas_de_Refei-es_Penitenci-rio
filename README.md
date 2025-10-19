# SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário

## 📋 Sobre o Projeto

O **SGMRP** é um sistema web desenvolvido para gerenciar e monitorar o fornecimento de refeições em unidades prisionais, criado para modernizar e otimizar o processo atualmente realizado através de múltiplas planilhas Excel no âmbito da **SEAP (Secretaria de Estado de Administração Penitenciária)**.

### 🎯 Objetivo Principal
Centralizar o controle de dados de refeições fornecidas aos internos, permitindo comparação automática com dados do SIISP e facilitando a gestão administrativa das unidades prisionais.

## 🚀 Status Atual - Protótipo Estático (v1.0)

Este repositório contém o **protótipo estático navegável** desenvolvido em HTML5, CSS3 e JavaScript ES6+, servindo como base visual e funcional para o desenvolvimento da aplicação completa.

### ✅ Funcionalidades Implementadas

#### 🏠 Páginas Principais
- **Landing Page (`index.html`)**: Apresentação do sistema com recursos e benefícios
- **Login (`login.html`)**: Autenticação simulada com validação de formulário
- **Cadastro (`cadastro.html`)**: Registro de usuários com validação de CPF e e-mail
- **Dashboard (`dashboard.html`)**: Painel principal com cards de lotes e estatísticas
- **Lista de Lotes (`lotes.html`)**: Visualização avançada com filtros e busca
- **Detalhes do Lote (`lote-detalhes.html`)**: Visualização detalhada com sistema de abas

#### 🍽️ Sistema de Refeições
- **4 Tipos de Refeição**: Café, Almoço, Lanche e Jantar
- **Dupla Visualização**:
  - **Aba "Dados de Refeições"**: Tabela simples com números de internos por refeição
  - **Aba "Comparação SIISP"**: Comparação visual com código de cores
- **Indicadores Visuais**: Verde para conformidade, vermelho para divergências

#### 🎨 Design System
- **Identidade Visual**: Esquema de cores azul profissional (#2c5282)
- **Responsividade**: Layout adaptativo para desktop, tablet e mobile
- **Acessibilidade**: Contraste adequado e navegação por teclado
- **Componentes**: Sistema de cards, formulários, tabelas e botões padronizados

#### 🔧 Funcionalidades Técnicas
- **Simulação de Dados**: Dataset realístico para demonstração
- **LocalStorage**: Persistência local para simulação de autenticação
- **Validação de Formulários**: CPF, e-mail e senhas com feedback visual
- **Sistema de Abas**: Interface intuitiva inspirada no workflow Excel atual
- **Filtros e Busca**: Funcionalidades de pesquisa em tempo real

## 📁 Estrutura de Arquivos

```
Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio/
├── index.html              # Landing page do sistema
├── login.html               # Página de autenticação
├── cadastro.html           # Formulário de registro
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

### Frontend (Atual)
- **HTML5**: Estrutura semântica moderna
- **CSS3**: Grid layout, flexbox, custom properties
- **JavaScript ES6+**: Módulos, arrow functions, template literals
- **Responsive Design**: Mobile-first approach

### Backend (Planejado)
- **Python Flask**: Framework web principal
- **SQLAlchemy**: ORM para banco de dados
- **PostgreSQL**: Banco de dados relacional
- **JWT**: Autenticação segura

## 🎯 Próximas Etapas de Desenvolvimento

### Fase 2 - Backend e Integração
1. **API REST** com Flask
2. **Banco de dados** PostgreSQL
3. **Autenticação** JWT
4. **Integração SIISP** (API externa)

### Fase 3 - Funcionalidades Avançadas
1. **Import/Export** de planilhas Excel
2. **Relatórios** automáticos
3. **Notificações** de divergências
4. **Auditoria** de alterações

### Fase 4 - Deploy e Produção
1. **Containerização** Docker
2. **CI/CD** GitHub Actions
3. **Monitoramento** e logs
4. **Backup** automatizado

## 🚀 Como Executar o Protótipo

### Pré-requisitos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Servidor web local (opcional, mas recomendado)

### Execução Simples
```bash
# Clone o repositório
git clone https://github.com/thallyson1997/Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio.git

# Navegue até o diretório
cd Sistema_Gerenciamento_Mapas_de_Refei-es_Penitenci-rio

# Abra o index.html no navegador
# Ou use um servidor local:
python -m http.server 8000
# Acesse: http://localhost:8000
```

### Credenciais de Teste
- **Login**: admin@seap.rj.gov.br
- **Senha**: admin123

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

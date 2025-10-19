======================================================================================
README - PROTÓTIPO SGMRP (Sistema de Gerenciamento de Mapas de Refeições Penitenciário)
======================================================================================

DESCRIÇÃO DO PROJETO
--------------------
Este é um protótipo estático navegável do Sistema de Gerenciamento de Mapas de Refeições 
Penitenciário (SGMRP), desenvolvido em HTML e CSS puro. O sistema tem como objetivo 
modernizar o controle de refeições em unidades prisionais, substituindo o modelo atual 
baseado em planilhas Excel fragmentadas por uma solução web integrada.

DESENVOLVEDOR
-------------
Thallyson Gabriel Martins Correia Fontenele
Matrícula: 2022024639
Sistema Penitenciário - SFA (Subsecretaria de Administração)

ESTRUTURA DE ARQUIVOS
--------------------
projeto/
├── index.html                  # Landing page - apresentação do sistema
├── login.html                  # Página de autenticação
├── cadastro.html              # Formulário de registro de usuários
├── dashboard.html             # Dashboard principal após login
├── lotes.html                 # Listagem completa dos lotes contratuais
├── lote-detalhes.html         # Detalhes do lote com tabelas de refeições
├── css/
│   └── style.css              # Estilos principais responsivos
├── images/                    # Pasta para imagens (não utilizada no protótipo)
└── README.txt                 # Este arquivo de documentação

PÁGINAS DESENVOLVIDAS
--------------------

1. INDEX.HTML - Landing Page
   - Apresentação do sistema SGMRP
   - Funcionalidades principais com ícones
   - Benefícios e roadmap do sistema
   - Navegação para login e cadastro
   - Design responsivo com animações

2. LOGIN.HTML - Autenticação
   - Formulário de login com validação
   - Toggle para mostrar/ocultar senha
   - Funcionalidade "lembrar-me"
   - Estados de loading e validação
   - Informações sobre acesso restrito

3. CADASTRO.HTML - Registro
   - Formulário completo de cadastro
   - Validação de campos (CPF, email, etc.)
   - Máscaras para telefone e CPF
   - Validador de força da senha
   - Seções organizadas (dados pessoais, profissionais, acesso)

4. DASHBOARD.HTML - Painel Principal
   - Resumo estatístico com cards
   - Grid de lotes contratuais
   - Filtros globais (mês, ano, busca)
   - Alertas e discrepâncias recentes
   - Ações rápidas (importar, manual, relatórios)

5. LOTES.HTML - Listagem
   - Lista completa dos lotes contratuais
   - Filtros avançados (status, empresa, conformidade)
   - Ordenação por diferentes critérios
   - Busca em tempo real
   - Estatísticas detalhadas por lote

6. LOTE-DETALHES.HTML - Detalhes
   - Informações específicas do lote
   - Tabela com indicadores coloridos
   - Seções de importação de dados
   - Entrada manual de refeições
   - Modal com legenda dos indicadores

FUNCIONALIDADES IMPLEMENTADAS
-----------------------------

NAVEGAÇÃO:
- Links funcionais entre todas as páginas
- Breadcrumbs para orientação
- Navegação responsiva
- Menu de logout simulado

AUTENTICAÇÃO SIMULADA:
- Validação de formulários
- Persistência de dados no localStorage
- Redirecionamento baseado em autenticação
- Estados de loading e feedback visual

INTERFACE RESPONSIVA:
- Design adaptável para desktop, tablet e mobile
- Grid system flexível
- Componentes reutilizáveis
- Tipografia hierárquica

INDICADORES VISUAIS:
- Sistema de cores baseado no PRD:
  * Verde: Diferença ≤ 0 (Conforme)
  * Azul: Diferença 1-5 (Atenção)
  * Vermelho: Diferença > 5 (Crítico)
  * Amarelo: Anotações do usuário

FILTROS E BUSCA:
- Filtros temporais (mês/ano)
- Busca em tempo real
- Filtros por status, empresa e conformidade
- Ordenação dinâmica

FORMULÁRIOS INTERATIVOS:
- Validação client-side
- Máscaras de input
- Estados de erro/sucesso
- Feedback visual imediato

ANIMAÇÕES:
- Fade-in na rolagem da página
- Transições suaves em hover
- Estados visuais interativos
- Loading states

TECNOLOGIAS UTILIZADAS
---------------------
- HTML5 semântico (header, nav, main, section, article, footer)
- CSS3 com variáveis customizadas
- JavaScript vanilla (sem frameworks)
- Design system consistente
- Acessibilidade básica (labels, alt texts, ARIA)

PALETA DE CORES
---------------
Cores Principais:
- Primary: #2c5282 (Azul institucional escuro)
- Secondary: #3182ce (Azul médio)  
- Accent: #1a365d (Azul muito escuro)
- Light Blue: #e6f3ff (Fundos claros)

Indicadores do Sistema:
- Success: #38a169 (Verde - OK)
- Warning: #3182ce (Azul - Diferença pequena)
- Danger: #e53e3e (Vermelho - Diferença grande)
- Annotation: #f6e05e (Amarelo - Anotação)

Cores Neutras:
- Escala de cinzas de #f7fafc a #171923
- Fonte principal: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif

CARACTERÍSTICAS TÉCNICAS
------------------------

ACESSIBILIDADE:
- Uso correto de elementos semânticos
- Labels associados aos inputs
- Atributos ARIA apropriados
- Contraste adequado de cores
- Navegação por teclado funcional

PERFORMANCE:
- CSS otimizado com variáveis
- JavaScript modular e eficiente
- Imagens não utilizadas para manter foco no protótipo
- Código limpo e bem estruturado

RESPONSIVIDADE:
- Mobile-first approach
- Breakpoints em 768px e 480px
- Grid system flexível
- Componentes adaptáveis

COMO UTILIZAR
-------------

1. NAVEGAÇÃO INICIAL:
   - Abra o arquivo index.html em um navegador moderno
   - Navegue pelos links da página inicial
   - Clique em "Acessar Sistema" ou "Login" no header

2. TESTE DE LOGIN:
   - Use qualquer nome de usuário (mín. 3 caracteres)
   - Use qualquer senha (mín. 4 caracteres)
   - O login é simulado e sempre permite acesso

3. EXPLORAÇÃO DO DASHBOARD:
   - Visualize os cards dos lotes contratuais
   - Teste os filtros de período
   - Clique nos lotes para ver detalhes

4. FUNCIONALIDADES PRINCIPAIS:
   - Importação de dados (formulário simulado)
   - Entrada manual (formulário funcional)
   - Visualização de indicadores coloridos
   - Sistema de anotações (clique nas células)

5. TESTES DE RESPONSIVIDADE:
   - Redimensione a janela do navegador
   - Teste em dispositivos móveis
   - Verifique adaptação dos componentes

LIMITAÇÕES DO PROTÓTIPO
-----------------------

Este é um protótipo estático com as seguintes limitações:

BACKEND:
- Não há integração com banco de dados
- Dados são simulados via JavaScript
- Não há autenticação real
- Persistência limitada ao localStorage

FUNCIONALIDADES FUTURAS:
- Geração de PDFs
- Dashboards com gráficos interativos
- Sistema de notificações
- Integração com SIISP
- Backup automático
- API REST

RECURSOS NÃO IMPLEMENTADOS:
- Upload real de arquivos
- Exportação de relatórios
- Sistema de permissões
- Auditoria de ações
- Integração com sistemas externos

NAVEGAÇÃO COMPLETA
------------------

FLUXO PRINCIPAL:
index.html → login.html → dashboard.html → lotes.html → lote-detalhes.html

FLUXO ALTERNATIVO:
index.html → cadastro.html → login.html → dashboard.html

LINKS FUNCIONAIS:
- Todos os botões e links principais funcionam
- Navegação entre páginas é fluida
- Breadcrumbs facilitam orientação
- Menu responsivo em dispositivos móveis

DADOS SIMULADOS
---------------

O protótipo inclui dados fictícios para demonstração:

LOTES:
- Lote 1: ABC Alimentação (5 presídios, 96.8% conformidade)
- Lote 2: XYZ Refeições (4 presídios, 91.5% conformidade)  
- Lote 3: DEF Nutrição (3 presídios, 98.2% conformidade)
- Lote 4: GHI Catering (3 presídios, 89.7% conformidade)

PRESÍDIOS SIMULADOS:
- Penitenciária Central
- Casa de Custódia Norte
- Centro de Detenção Sul
- Presídio Metropolitano
- Unidade Prisional Leste

DADOS DE REFEIÇÕES:
- Tabela com 5 dias de outubro/2025
- Indicadores coloridos funcionais
- Sistema de anotações ativo
- Comparação com dados SIISP simulados

VALIDAÇÕES IMPLEMENTADAS
------------------------

FORMULÁRIO DE LOGIN:
- Usuário: mínimo 3 caracteres
- Senha: mínimo 4 caracteres
- Estados de loading e erro

FORMULÁRIO DE CADASTRO:
- Nome completo: obrigatório
- CPF: validação completa com máscara
- Email: validação de formato
- Senha: medidor de força
- Confirmação de senha
- Termos de uso obrigatórios

FILTROS E BUSCAS:
- Validação de datas
- Filtros combinados
- Busca em tempo real
- Ordenação funcional

NAVEGADORES SUPORTADOS
----------------------
- Chrome 90+ (Recomendado)
- Firefox 88+
- Safari 14+
- Edge 90+

RESOLUÇÃO MÍNIMA:
- Desktop: 1024x768
- Tablet: 768x1024
- Mobile: 320x568

CONSIDERAÇÕES DE DESENVOLVIMENTO
--------------------------------

CÓDIGO LIMPO:
- Comentários explicativos no CSS e JavaScript
- Nomenclatura consistente de classes
- Estrutura HTML semântica
- Separação clara de responsabilidades

MANUTENIBILIDADE:
- Variáveis CSS centralizadas
- Componentes reutilizáveis
- JavaScript modular
- Estrutura escalável

PERFORMANCE:
- CSS otimizado com custom properties
- JavaScript eficiente
- Animações suaves com CSS
- Carregamento rápido

PRÓXIMOS PASSOS
---------------

Para transformar este protótipo em sistema funcional:

1. Implementar backend em Flask (conforme PRD)
2. Integrar banco de dados JSON/SQLite
3. Adicionar autenticação real
4. Implementar upload de arquivos PDF
5. Criar sistema de geração de relatórios
6. Adicionar dashboards com gráficos
7. Integrar com sistema SIISP
8. Implementar sistema de notificações

CONTATO
-------
Para dúvidas sobre este protótipo ou implementação:
- Desenvolvedor: Thallyson Gabriel Martins Correia Fontenele
- Sistema: SGMRP v1.0 - Outubro 2025
- Projeto: Sistema Penitenciário - SFA

======================================================================================
FIM DA DOCUMENTAÇÃO
======================================================================================
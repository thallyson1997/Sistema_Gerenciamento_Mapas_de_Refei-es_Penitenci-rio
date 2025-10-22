#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário
Arquivo principal da aplicação Flask

Autor: SEAP
Data: Outubro 2025
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from datetime import datetime, timedelta
import os
import json

# Configuração da aplicação Flask
app = Flask(__name__)
app.secret_key = 'sgmrp_seap_2025_secret_key_desenvolvimento'  # Em produção, usar variável de ambiente
app.config['DEBUG'] = True

# Configurações de paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS_DIR = os.path.join(BASE_DIR, 'dados')

# Funções auxiliares para manipular dados JSON
def carregar_dados_json(arquivo):
    """Carrega dados de um arquivo JSON"""
    caminho = os.path.join(DADOS_DIR, arquivo)
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def salvar_dados_json(arquivo, dados):
    """Salva dados em um arquivo JSON"""
    # Criar diretório se não existir
    os.makedirs(DADOS_DIR, exist_ok=True)
    
    caminho = os.path.join(DADOS_DIR, arquivo)
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo {arquivo}: {e}")
        return False

def carregar_usuarios():
    """Carrega lista de usuários do arquivo JSON"""
    dados = carregar_dados_json('usuarios.json')
    return dados.get('usuarios', [])

def salvar_usuarios(usuarios):
    """Salva lista de usuários no arquivo JSON"""
    dados = {'usuarios': usuarios}
    return salvar_dados_json('usuarios.json', dados)

def carregar_lotes():
    """Carrega lotes do arquivo JSON"""
    dados = carregar_dados_json('lotes.json')
    return dados.get('lotes', [])

def carregar_unidades():
    """Carrega unidades do arquivo JSON"""
    dados = carregar_dados_json('unidades.json')
    return dados.get('unidades', [])

def calcular_colunas_siisp(mapa):
    """
    Calcula automaticamente as colunas _siisp baseado em n_siisp
    Fórmula CORRIGIDA: campo_siisp = campo_original - n_siisp
    """
    # Verificar se tem dados SIISP para processar
    n_siisp = mapa.get('n_siisp', [])
    
    if not n_siisp:  # Se n_siisp está vazio, manter colunas _siisp vazias
        return mapa
    
    # Campos base para calcular as diferenças
    campos_base = [
        'cafe_interno', 'cafe_funcionario',
        'almoco_interno', 'almoco_funcionario', 
        'lanche_interno', 'lanche_funcionario',
        'jantar_interno', 'jantar_funcionario'
    ]
    
    # Calcular cada coluna _siisp
    for campo in campos_base:
        campo_siisp = f"{campo}_siisp"
        valores_originais = mapa.get(campo, [])
        
        # Calcular diferenças: valores_originais - n_siisp (FÓRMULA CORRIGIDA)
        if valores_originais and len(valores_originais) == len(n_siisp):
            diferencas = []
            for i in range(len(n_siisp)):
                diferenca = valores_originais[i] - n_siisp[i]
                diferencas.append(diferenca)
            
            mapa[campo_siisp] = diferencas
        else:
            # Se não há dados compatíveis, manter vazio
            mapa[campo_siisp] = []
    
    return mapa

def salvar_mapas_atualizados(mapas):
    """Salva os mapas atualizados de volta no arquivo JSON"""
    dados = {'mapas': mapas}
    return salvar_dados_json('mapas.json', dados)

def carregar_mapas():
    """Carrega mapas do arquivo JSON e calcula colunas SIISP automaticamente"""
    dados = carregar_dados_json('mapas.json')
    mapas = dados.get('mapas', [])
    
    # Processar cada mapa para calcular colunas SIISP
    mapas_atualizados = []
    houve_alteracoes = False
    
    for mapa in mapas:
        mapa_original = mapa.copy()
        mapa_calculado = calcular_colunas_siisp(mapa)
        mapas_atualizados.append(mapa_calculado)
        
        # Verificar se houve mudanças nas colunas _siisp
        campos_siisp = [
            'cafe_interno_siisp', 'cafe_funcionario_siisp',
            'almoco_interno_siisp', 'almoco_funcionario_siisp',
            'lanche_interno_siisp', 'lanche_funcionario_siisp', 
            'jantar_interno_siisp', 'jantar_funcionario_siisp'
        ]
        
        for campo in campos_siisp:
            if mapa_original.get(campo, []) != mapa_calculado.get(campo, []):
                houve_alteracoes = True
                break
    
    # Salvar de volta se houve alterações
    if houve_alteracoes:
        if salvar_mapas_atualizados(mapas_atualizados):
            print("✅ Colunas SIISP calculadas e salvas automaticamente!")
        else:
            print("❌ Erro ao salvar colunas SIISP calculadas")
    
    return mapas_atualizados

def obter_unidades_do_lote(lote_id):
    """Obtém as unidades de um lote específico fazendo join dos dados"""
    # Carregar dados dos dois arquivos
    lotes = carregar_lotes()
    unidades = carregar_unidades()
    
    # Encontrar o lote
    lote = next((l for l in lotes if l['id'] == lote_id), None)
    if not lote:
        return []
    
    # Buscar as unidades do lote pelos IDs
    unidades_do_lote = []
    for unidade_id in lote.get('unidades', []):
        unidade = next((u for u in unidades if u['id'] == unidade_id), None)
        if unidade:
            unidades_do_lote.append(unidade['nome'])
    
    return unidades_do_lote

def obter_mapas_do_lote(lote_id, mes=None, ano=None):
    """Obtém os mapas de um lote específico, opcionalmente filtrados por mês/ano"""
    mapas = carregar_mapas()
    
    # Filtrar por lote
    mapas_lote = [m for m in mapas if m['lote_id'] == lote_id]
    
    # Filtrar por mês/ano se fornecidos
    if mes is not None:
        mapas_lote = [m for m in mapas_lote if m['mes'] == mes]
    if ano is not None:
        mapas_lote = [m for m in mapas_lote if m['ano'] == ano]
    
    return mapas_lote

def adicionar_usuario(dados_usuario):
    """Adiciona um novo usuário ao arquivo JSON"""
    usuarios = carregar_usuarios()
    
    # Gerar novo ID (pega o maior ID atual + 1)
    proximo_id = max([u.get('id', 0) for u in usuarios], default=0) + 1
    
    # Preparar dados do novo usuário com TODOS os campos
    novo_usuario = {
        'id': proximo_id,
        'nome': dados_usuario.get('nome', '').strip(),
        'email': dados_usuario.get('email', '').strip().lower(),
        'cpf': dados_usuario.get('cpf', '').strip(),
        'telefone': dados_usuario.get('telefone', '').strip(),
        'cargo': dados_usuario.get('cargo', '').strip(),
        'unidade': dados_usuario.get('unidade', '').strip(),
        'matricula': dados_usuario.get('matricula', '').strip(),
        'usuario': dados_usuario.get('usuario', '').strip().lower(),  # Nome de usuário
        'senha': dados_usuario.get('senha', '').strip(),
        'justificativa': dados_usuario.get('justificativa', '').strip(),  # Motivo essencial!
        'aceitar_termos': dados_usuario.get('aceitarTermos') == 'on',  # Checkbox
        'data_cadastro': datetime.now().isoformat() + 'Z',
        'acesso': False  # Campo automático - sempre inicia como False
    }
    
    usuarios.append(novo_usuario)
    
    if salvar_usuarios(usuarios):
        return novo_usuario
    return None

def buscar_usuario_por_email_ou_usuario(identificador):
    """Busca usuário pelo email ou nome de usuário"""
    usuarios = carregar_usuarios()
    identificador = identificador.lower().strip()
    return next((u for u in usuarios if 
                u.get('email', '').lower() == identificador or 
                u.get('usuario', '').lower() == identificador), None)

def validar_dados_unicos(dados_usuario, usuario_id=None):
    """
    Valida se os dados do usuário são únicos no sistema
    Retorna lista de erros encontrados
    """
    usuarios = carregar_usuarios()
    erros = []
    
    # Filtrar o próprio usuário em caso de edição
    if usuario_id:
        usuarios = [u for u in usuarios if u.get('id') != usuario_id]
    
    # Verificar EMAIL único
    email = dados_usuario.get('email', '').strip().lower()
    if email and any(u.get('email', '').lower() == email for u in usuarios):
        erros.append('Este email já está cadastrado no sistema!')
    
    # Verificar CPF único
    cpf = dados_usuario.get('cpf', '').strip()
    if cpf and any(u.get('cpf', '').strip() == cpf for u in usuarios):
        erros.append('Este CPF já está cadastrado no sistema!')
    
    # Verificar USUÁRIO único
    usuario = dados_usuario.get('usuario', '').strip().lower()
    if usuario and any(u.get('usuario', '').lower() == usuario for u in usuarios):
        erros.append('Este nome de usuário já existe! Escolha outro.')
    
    # Verificar MATRÍCULA única (se preenchida)
    matricula = dados_usuario.get('matricula', '').strip()
    if matricula and any(u.get('matricula', '').strip() == matricula for u in usuarios):
        erros.append('Esta matrícula já está cadastrada no sistema!')
    
    # Verificar TELEFONE único (se preenchido)
    telefone = dados_usuario.get('telefone', '').strip()
    if telefone and any(u.get('telefone', '').strip() == telefone for u in usuarios):
        erros.append('Este telefone já está cadastrado no sistema!')
    
    return erros

def atualizar_acesso_usuario(user_id, acesso):
    """Atualiza o status de acesso de um usuário"""
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuario['acesso'] = acesso
            if salvar_usuarios(usuarios):
                return usuario
    return None

# Dados simulados temporários (até criarmos os JSONs)
DADOS_SIMULADOS = {
    'usuarios': [
        {
            'id': 1,
            'email': 'admin@seap.gov.br',
            'senha': 'admin123',
            'nome': 'Administrador Sistema',
            'perfil': 'admin'
        }
    ],
    'unidades': [
        {'id': 1, 'nome': 'Penitenciária Central', 'codigo': 'PC001'},
        {'id': 2, 'nome': 'Penitenciária Industrial', 'codigo': 'PI002'},
        {'id': 3, 'nome': 'Instituto Penal Feminino', 'codigo': 'IPF003'},
    ],
    'lotes': [
        {
            'id': 1,
            'numero': 'LT-2025-001',
            'nome': 'Lote 1',
            'contrato': 'CT-2024-001',
            'data_inicio_contrato': '15/01/2024',
            'empresa': 'Empresa ABC Alimentação',
            'presidios': 5,
            'status': 'em_andamento',
            'data_inicio': '2025-01-01',
            'data_fim': '2025-01-31',
            'refeicoes': 28450,
            'conformidade': 96.8,
            'alertas': 2
        },
        {
            'id': 2,
            'numero': 'LT-2025-002',
            'nome': 'Lote 2',
            'contrato': 'CT-2024-002',
            'data_inicio_contrato': '01/02/2024',
            'empresa': 'Empresa XYZ Refeições',
            'presidios': 4,
            'status': 'em_andamento',
            'data_inicio': '2025-02-01',
            'data_fim': '2025-02-28',
            'refeicoes': 22180,
            'conformidade': 91.5,
            'alertas': 4
        },
        {
            'id': 3,
            'numero': 'LT-2025-003',
            'nome': 'Lote 3',
            'contrato': 'CT-2024-003',
            'data_inicio_contrato': '10/03/2024',
            'empresa': 'Empresa DEF Nutrição',
            'presidios': 3,
            'status': 'em_andamento',
            'data_inicio': '2025-03-01',
            'data_fim': '2025-03-31',
            'refeicoes': 18920,
            'conformidade': 98.2,
            'alertas': 0
        },
        {
            'id': 4,
            'numero': 'LT-2025-004',
            'nome': 'Lote 4',
            'contrato': 'CT-2023-018',
            'data_inicio_contrato': '22/11/2023',
            'empresa': 'Empresa GHI Catering',
            'presidios': 3,
            'status': 'em_andamento',
            'data_inicio': '2025-04-01',
            'data_fim': '2025-04-30',
            'refeicoes': 16800,
            'conformidade': 89.7,
            'alertas': 3
        }
    ]
}

# ===== ROTAS DA APLICAÇÃO =====

@app.route('/')
def index():
    """Página inicial - Landing page"""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        identificador = request.form.get('email', '').strip()  # Pode ser email ou usuário
        senha = request.form.get('senha', '').strip()
        
        # Validação de campos obrigatórios
        if not identificador:
            flash('Por favor, digite seu usuário ou e-mail!', 'error')
            return render_template('login.html')
        
        if not senha:
            flash('Por favor, digite sua senha!', 'error')
            return render_template('login.html')
        
        # Buscar usuário no arquivo JSON (por email ou nome de usuário)
        usuario = buscar_usuario_por_email_ou_usuario(identificador)
        
        if not usuario:
            flash('Usuário não encontrado! Verifique seu e-mail/usuário ou registre-se.', 'error')
            return render_template('login.html')
        
        # Verificar senha
        if usuario['senha'] != senha:
            flash('Senha incorreta! Verifique sua senha e tente novamente.', 'error')
            return render_template('login.html')
        
        # Verificar se usuário tem acesso liberado
        if not usuario.get('acesso', False):
            flash('Sua conta ainda não foi aprovada pelo administrador. Aguarde a liberação ou entre em contato.', 'warning')
            return render_template('login.html')
        
        # Login bem-sucedido
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        session['usuario_email'] = usuario['email']
        session['usuario_cargo'] = usuario.get('cargo', '')
        session['usuario_usuario'] = usuario.get('usuario', '')
        session['login_sucesso'] = True  # Flag para mostrar mensagem no dashboard
        
        print(f"✅ Login realizado: {usuario['nome']} ({usuario.get('usuario', usuario['email'])})")
        
        # Redirecionar para dashboard
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout do sistema"""
    session.clear()
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Página de cadastro de usuários"""
    if request.method == 'POST':
        try:
            # Coletar TODOS os dados do formulário
            dados_usuario = {
                'nome': request.form.get('nome', '').strip(),
                'email': request.form.get('email', '').strip().lower(),
                'cpf': request.form.get('cpf', '').strip(),
                'telefone': request.form.get('telefone', '').strip(),
                'cargo': request.form.get('cargo', '').strip(),
                'unidade': request.form.get('unidade', '').strip(),
                'matricula': request.form.get('matricula', '').strip(),
                'usuario': request.form.get('usuario', '').strip().lower(),
                'senha': request.form.get('senha', '').strip(),
                'justificativa': request.form.get('justificativa', '').strip(),
                'aceitarTermos': request.form.get('aceitarTermos', '')
            }
            
            # Validações básicas obrigatórias
            campos_obrigatorios = ['nome', 'email', 'cpf', 'cargo', 'usuario', 'senha', 'justificativa']
            campos_vazios = [campo for campo in campos_obrigatorios if not dados_usuario[campo]]
            
            if campos_vazios:
                campos_nomes = {
                    'nome': 'Nome completo',
                    'email': 'Email',
                    'cpf': 'CPF',
                    'cargo': 'Cargo/Função',
                    'usuario': 'Nome de usuário',
                    'senha': 'Senha',
                    'justificativa': 'Justificativa de acesso'
                }
                nomes_vazios = [campos_nomes.get(campo, campo) for campo in campos_vazios]
                flash(f'Campos obrigatórios não preenchidos: {", ".join(nomes_vazios)}', 'error')
                return render_template('cadastro.html')
            
            # Validar dados únicos (email, CPF, usuário, matrícula, telefone)
            erros_unicidade = validar_dados_unicos(dados_usuario)
            if erros_unicidade:
                for erro in erros_unicidade:
                    flash(erro, 'error')
                return render_template('cadastro.html')
            
            # Verificar se aceitou os termos
            if dados_usuario['aceitarTermos'] != 'on':
                flash('É necessário aceitar os termos de uso para continuar!', 'error')
                return render_template('cadastro.html')
            
            # Adicionar usuário ao arquivo JSON
            novo_usuario = adicionar_usuario(dados_usuario)
            
            if novo_usuario:
                flash(f'Cadastro realizado com sucesso! Aguarde liberação de acesso.', 'success')
                print(f"✅ Novo usuário cadastrado:")
                print(f"   Nome: {novo_usuario['nome']}")
                print(f"   Email: {novo_usuario['email']}")
                print(f"   Usuário: {novo_usuario['usuario']}")
                print(f"   Cargo: {novo_usuario['cargo']}")
                print(f"   Justificativa: {novo_usuario['justificativa']}")
                return redirect(url_for('login'))
            else:
                flash('Erro interno. Tente novamente mais tarde.', 'error')
                
        except Exception as e:
            print(f"❌ Erro no cadastro: {e}")
            flash('Erro interno no cadastro. Tente novamente.', 'error')
    
    return render_template('cadastro.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard principal - requer login"""
    if 'usuario_id' not in session:
        flash('Acesso negado. Faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Capturar flag de login_sucesso antes de limpar
    mostrar_sucesso = session.pop('login_sucesso', False)
    
    # Carregar lotes e mapas do arquivo JSON
    lotes = carregar_lotes()
    mapas = carregar_mapas()
    
    # Dados para o dashboard
    context = {
        'usuario_nome': session.get('usuario_nome'),
        'mostrar_login_sucesso': mostrar_sucesso,
        'lotes': lotes,
        'total_lotes': len(lotes),
        'lotes_ativos': len([l for l in lotes if l.get('ativo', False)]),
        'total_unidades': sum(len(l.get('unidades', [])) for l in lotes),
        'mapas_dados': mapas  # Passar dados dos mapas para o frontend
    }
    
    return render_template('dashboard.html', **context)

@app.route('/lotes')
def lotes():
    """Página de listagem de lotes"""
    if 'usuario_id' not in session:
        flash('Acesso negado. Faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Carregar lotes do arquivo JSON
    lotes = carregar_lotes()
    
    context = {
        'lotes': lotes,
        'unidades': DADOS_SIMULADOS['unidades']
    }
    
    return render_template('lotes.html', **context)

@app.route('/lote/<int:lote_id>')
def lote_detalhes(lote_id):
    """Página de detalhes de um lote específico"""
    if 'usuario_id' not in session:
        flash('Acesso negado. Faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Carregar lotes e buscar lote específico
    lotes = carregar_lotes()
    lote = next((l for l in lotes if l['id'] == lote_id), None)
    
    if not lote:
        flash('Lote não encontrado!', 'error')
        return redirect(url_for('lotes'))
    
    # Obter unidades do lote com join dos dados
    unidades_lote = obter_unidades_do_lote(lote_id)
    
    # Obter TODOS os mapas do lote (todos os meses disponíveis)
    mapas_lote = obter_mapas_do_lote(lote_id)
    
    context = {
        'lote': lote,
        'unidades_lote': unidades_lote,
        'mapas_lote': mapas_lote
    }
    
    return render_template('lote-detalhes.html', **context)

# ===== ROTAS ADMINISTRATIVAS =====

@app.route('/admin/usuarios')
def admin_usuarios():
    """Página administrativa para gerenciar usuários"""
    if 'usuario_id' not in session:
        flash('Acesso negado. Faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    
    # Verificar se é admin (usuário ID 1)
    if session.get('usuario_id') != 1:
        flash('Acesso negado. Apenas administradores.', 'error')
        return redirect(url_for('dashboard'))
    
    usuarios = carregar_usuarios()
    
    context = {
        'usuarios': usuarios,
        'total_usuarios': len(usuarios),
        'usuarios_pendentes': len([u for u in usuarios if not u.get('acesso', False)]),
        'usuarios_ativos': len([u for u in usuarios if u.get('acesso', False)])
    }
    
    # Por enquanto, retornar dados JSON (depois criaremos template)
    return jsonify(context)

@app.route('/admin/usuarios/<int:user_id>/aprovar', methods=['POST'])
def aprovar_usuario(user_id):
    """Aprovar acesso de um usuário"""
    if 'usuario_id' not in session or session.get('usuario_id') != 1:
        return jsonify({'error': 'Acesso negado'}), 403
    
    usuario = atualizar_acesso_usuario(user_id, True)
    
    if usuario:
        print(f"✅ Acesso aprovado para: {usuario['nome']} ({usuario['email']})")
        return jsonify({
            'success': True, 
            'message': f'Acesso aprovado para {usuario["nome"]}',
            'usuario': usuario
        })
    
    return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/admin/usuarios/<int:user_id>/revogar', methods=['POST'])
def revogar_usuario(user_id):
    """Revogar acesso de um usuário"""
    if 'usuario_id' not in session or session.get('usuario_id') != 1:
        return jsonify({'error': 'Acesso negado'}), 403
    
    usuario = atualizar_acesso_usuario(user_id, False)
    
    if usuario:
        print(f"⚠️ Acesso revogado para: {usuario['nome']} ({usuario['email']})")
        return jsonify({
            'success': True, 
            'message': f'Acesso revogado para {usuario["nome"]}',
            'usuario': usuario
        })
    
    return jsonify({'error': 'Usuário não encontrado'}), 404

# ===== ROTAS DE API (JSON) =====

@app.route('/api/lotes')
def api_lotes():
    """API para listar lotes (JSON)"""
    lotes = carregar_lotes()
    return jsonify(lotes)

@app.route('/api/unidades')
def api_unidades():
    """API para listar unidades (JSON)"""
    return jsonify(DADOS_SIMULADOS['unidades'])

@app.route('/api/usuarios')
def api_usuarios():
    """API para listar usuários (apenas para admins)"""
    if 'usuario_id' not in session or session.get('usuario_id') != 1:
        return jsonify({'error': 'Acesso negado'}), 403
    
    usuarios = carregar_usuarios()
    # Remover senhas da resposta por segurança
    usuarios_safe = []
    for u in usuarios:
        usuario_safe = u.copy()
        usuario_safe.pop('senha', None)
        usuarios_safe.append(usuario_safe)
    
    return jsonify(usuarios_safe)

@app.route('/api/validar-campo', methods=['POST'])
def validar_campo_unico():
    """API para validar se um campo específico já existe (validação em tempo real)"""
    try:
        campo = request.json.get('campo')
        valor = request.json.get('valor', '').strip()
        
        if not campo or not valor:
            return jsonify({'valido': True})
        
        usuarios = carregar_usuarios()
        
        # Validações específicas por campo
        existe = False
        mensagem = ''
        
        if campo == 'email':
            valor = valor.lower()
            existe = any(u.get('email', '').lower() == valor for u in usuarios)
            mensagem = 'Este email já está em uso!'
        elif campo == 'cpf':
            existe = any(u.get('cpf', '') == valor for u in usuarios)
            mensagem = 'Este CPF já está cadastrado!'
        elif campo == 'usuario':
            valor = valor.lower()
            existe = any(u.get('usuario', '').lower() == valor for u in usuarios)
            mensagem = 'Este nome de usuário já existe!'
        elif campo == 'matricula':
            if valor:  # Matrícula é opcional
                existe = any(u.get('matricula', '') == valor for u in usuarios)
                mensagem = 'Esta matrícula já está em uso!'
        elif campo == 'telefone':
            if valor:  # Telefone é opcional
                existe = any(u.get('telefone', '') == valor for u in usuarios)
                mensagem = 'Este telefone já está cadastrado!'
        
        return jsonify({
            'valido': not existe,
            'mensagem': mensagem if existe else 'Disponível!'
        })
        
    except Exception as e:
        print(f"Erro na validação: {e}")
        return jsonify({'valido': True}), 500

# ===== FILTROS PERSONALIZADOS PARA TEMPLATES =====

@app.template_filter('data_br')
def filtro_data_br(data_str):
    """Converte data ISO para formato brasileiro"""
    try:
        data = datetime.strptime(data_str, '%Y-%m-%d')
        return data.strftime('%d/%m/%Y')
    except:
        return data_str

@app.template_filter('status_badge')
def filtro_status_badge(status):
    """Retorna classe CSS para badge de status"""
    badges = {
        'concluido': 'success',
        'em_andamento': 'primary', 
        'planejado': 'warning',
        'cancelado': 'danger'
    }
    return badges.get(status, 'secondary')

# ===== CONTEXTO GLOBAL PARA TEMPLATES =====

@app.context_processor
def contexto_global():
    """Variáveis disponíveis em todos os templates"""
    return {
        'app_nome': 'SGMRP',
        'app_versao': '1.0.0',
        'ano_atual': datetime.now().year,
        'usuario_logado': 'usuario_id' in session,
        'usuario_nome': session.get('usuario_nome', ''),
        'usuario_perfil': session.get('usuario_perfil', '')
    }

# ===== TRATAMENTO DE ERROS =====

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    """Página de erro 404"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def erro_interno(error):
    """Página de erro 500"""
    return render_template('index.html'), 500

# ===== INICIALIZAÇÃO DA APLICAÇÃO =====

if __name__ == '__main__':
    print("🚀 Iniciando SGMRP - Sistema de Gerenciamento de Mapas de Refeições Penitenciário")
    print(f"📁 Diretório base: {BASE_DIR}")
    print(f"📄 Templates: {os.path.join(BASE_DIR, 'templates')}")
    print(f"🎨 Arquivos estáticos: {os.path.join(BASE_DIR, 'static')}")
    print(f"💾 Dados JSON: {DADOS_DIR}")
    print("🔗 Acesse: http://localhost:5000")
    print("👤 Admin: admin@seap.gov.br (ou 'admin') | Senha: admin123")
    print("📋 Usuários: /admin/usuarios (apenas admin)")
    print("📝 Cadastros salvos em: dados/usuarios.json")
    print("-" * 60)
    
    # Executar aplicação
    app.run(
        host='0.0.0.0',      # Aceita conexões de qualquer IP
        port=5000,           # Porta padrão do Flask
        debug=True,          # Modo debug ativo
        use_reloader=True    # Reinicialização automática ao modificar arquivos
    )
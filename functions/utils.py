# Funções auxiliares movidas de main.py
import os
import json
import calendar
from datetime import datetime

def carregar_dados_json(arquivo):
	DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados')
	caminho = os.path.join(DADOS_DIR, arquivo)
	try:
		with open(caminho, 'r', encoding='utf-8') as f:
			return json.load(f)
	except FileNotFoundError:
		return {}
	except json.JSONDecodeError:
		return {}

def salvar_dados_json(arquivo, dados):
	DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados')
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
	dados = carregar_dados_json('usuarios.json')
	return dados.get('usuarios', [])

def salvar_usuarios(usuarios):
	dados = {'usuarios': usuarios}
	return salvar_dados_json('usuarios.json', dados)

def carregar_lotes():
	dados = carregar_dados_json('lotes.json')
	return dados.get('lotes', [])

def carregar_unidades():
	dados = carregar_dados_json('unidades.json')
	return dados.get('unidades', [])

def gerar_datas_do_mes(mes, ano):
	dias_no_mes = calendar.monthrange(ano, mes)[1]
	datas = [f"{dia:02d}/{mes:02d}/{ano}" for dia in range(1, dias_no_mes + 1)]
	return datas

def processar_dados_tabulares(texto, dias_esperados=None):
	if not texto or texto.strip() == "":
		return {
			'cafe_interno': [],
			'cafe_funcionario': [],
			'almoco_interno': [],
			'almoco_funcionario': [],
			'lanche_interno': [],
			'lanche_funcionario': [],
			'jantar_interno': [],
			'jantar_funcionario': [],
			'validacao': {
				'registros_processados': 0,
				'dias_esperados': dias_esperados or 0,
				'valido': True,
				'mensagem': 'Nenhum dado para processar'
			}
		}
	campos = {
		'cafe_interno': [],
		'cafe_funcionario': [],
		'almoco_interno': [],
		'almoco_funcionario': [],
		'lanche_interno': [],
		'lanche_funcionario': [],
		'jantar_interno': [],
		'jantar_funcionario': []
	}
	linhas = texto.strip().split('\n')
	registros_processados = 0
	for linha in linhas:
		if linha.strip():
			if '\t' in linha:
				colunas = linha.split('\t')
			else:
				import re
				colunas = re.split(r'\s+', linha.strip())
			if len(colunas) >= 9:
				try:
					campos['cafe_interno'].append(int(colunas[1]))
					campos['cafe_funcionario'].append(int(colunas[2]))
					campos['almoco_interno'].append(int(colunas[3]))
					campos['almoco_funcionario'].append(int(colunas[4]))
					campos['lanche_interno'].append(int(colunas[5]))
					campos['lanche_funcionario'].append(int(colunas[6]))
					campos['jantar_interno'].append(int(colunas[7]))
					campos['jantar_funcionario'].append(int(colunas[8]))
					registros_processados += 1
				except ValueError:
					continue
	validacao = {
		'registros_processados': registros_processados,
		'dias_esperados': dias_esperados or registros_processados,
		'valido': True,
		'mensagem': 'Dados processados com sucesso'
	}
	if dias_esperados and registros_processados != dias_esperados:
		validacao['valido'] = False
		if registros_processados > dias_esperados:
			validacao['mensagem'] = f'ATENÇÃO: Foram encontrados {registros_processados} registros, mas o mês possui apenas {dias_esperados} dias. Dados excedentes foram incluídos, mas podem estar incorretos.'
		else:
			validacao['mensagem'] = f'ATENÇÃO: Foram encontrados apenas {registros_processados} registros, mas o mês possui {dias_esperados} dias. Alguns dias podem estar faltando.'
	campos['validacao'] = validacao
	return campos

def processar_dados_siisp(texto_siisp, dias_esperados):
	resultado = {
		'n_siisp': [],
		'validacao': {
			'valido': True,
			'mensagem': 'Dados SIISP não fornecidos - campos SIISP ficarão vazios'
		}
	}
	if not texto_siisp or texto_siisp.strip() == "":
		return resultado
	linhas = texto_siisp.strip().split('\n')
	valores_siisp = []
	for linha in linhas:
		linha_limpa = linha.strip()
		if linha_limpa:
			try:
				valor = int(linha_limpa)
				valores_siisp.append(valor)
			except ValueError:
				resultado['validacao'] = {
					'valido': False,
					'mensagem': f'Valor SIISP inválido encontrado: "{linha_limpa}". Todos os valores devem ser números inteiros.'
				}
				return resultado
	if len(valores_siisp) != dias_esperados:
		resultado['validacao'] = {
			'valido': False,
			'mensagem': f'Dados SIISP: encontrados {len(valores_siisp)} valores, mas o mês possui {dias_esperados} dias. Deve ter exatamente {dias_esperados} valores ou estar vazio.'
		}
		return resultado
	resultado['n_siisp'] = valores_siisp
	resultado['validacao'] = {
		'valido': True,
		'mensagem': f'Dados SIISP processados com sucesso - {len(valores_siisp)} valores'
	}
	return resultado

def migrar_dados_existentes():
	try:
		dados_teste = carregar_dados_json('mapas_teste.json')
		if not dados_teste or 'registros' not in dados_teste or not dados_teste['registros']:
			print("ℹ️ Nenhum dado de teste encontrado para migrar")
			return True
		print(f"🔄 Migrando {len(dados_teste['registros'])} registros de mapas_teste.json para mapas.json...")
		dados_mapas = carregar_dados_json('mapas.json')
		if 'mapas' not in dados_mapas:
			dados_mapas['mapas'] = []
		registros_migrados = 0
		for registro in dados_teste['registros']:
			ja_existe = any(
				m.get('id') == registro.get('id') and 
				m.get('nome_unidade') == registro.get('nome_unidade') and
				m.get('mes') == registro.get('mes') and
				m.get('ano') == registro.get('ano') and
				m.get('lote_id') == registro.get('lote_id')
				for m in dados_mapas['mapas']
			)
			if not ja_existe:
				if 'data_criacao' in registro:
					del registro['data_criacao']
				dados_mapas['mapas'].append(registro)
				registros_migrados += 1
				print(f"   ✅ Migrado: {registro.get('nome_unidade')} - {registro.get('mes')}/{registro.get('ano')}")
			else:
				print(f"   ⚠️ Já existe: {registro.get('nome_unidade')} - {registro.get('mes')}/{registro.get('ano')}")
		if registros_migrados > 0:
			if salvar_dados_json('mapas.json', dados_mapas):
				print(f"✅ {registros_migrados} registros migrados com sucesso!")
				import os
				caminho_teste = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dados', 'mapas_teste.json')
				try:
					os.remove(caminho_teste)
					print("🗑️ Arquivo mapas_teste.json removido com sucesso!")
				except OSError:
					print("⚠️ Não foi possível remover mapas_teste.json")
				return True
			else:
				print("❌ Erro ao salvar dados migrados")
				return False
		else:
			print("ℹ️ Nenhum registro novo para migrar")
			return True
	except Exception as e:
		print(f"❌ Erro na migração: {e}")
		return False

def calcular_colunas_siisp(mapa):
	n_siisp = mapa.get('n_siisp', [])
	campos_base = [
		'cafe_interno', 'cafe_funcionario',
		'almoco_interno', 'almoco_funcionario', 
		'lanche_interno', 'lanche_funcionario',
		'jantar_interno', 'jantar_funcionario'
	]
	tamanho_lista = 0
	for campo in campos_base:
		valores = mapa.get(campo, [])
		if valores and len(valores) > tamanho_lista:
			tamanho_lista = len(valores)
	if not n_siisp and tamanho_lista > 0:
		n_siisp = [0] * tamanho_lista
		mapa['n_siisp'] = n_siisp
		print(f"🔢 Criada lista de zeros para n_siisp: {len(n_siisp)} valores")
	if not n_siisp or tamanho_lista == 0:
		return mapa
	for campo in campos_base:
		campo_siisp = f"{campo}_siisp"
		valores_originais = mapa.get(campo, [])
		if valores_originais and len(valores_originais) == len(n_siisp):
			diferencas = [valores_originais[i] - n_siisp[i] for i in range(len(n_siisp))]
			mapa[campo_siisp] = diferencas
		else:
			mapa[campo_siisp] = []
	return mapa

def salvar_mapas_atualizados(mapas):
	dados = {'mapas': mapas}
	return salvar_dados_json('mapas.json', dados)

def carregar_mapas():
	dados = carregar_dados_json('mapas.json')
	mapas = dados.get('mapas', [])
	mapas_atualizados = []
	houve_alteracoes = False
	for mapa in mapas:
		mapa_original = mapa.copy()
		mapa_calculado = calcular_colunas_siisp(mapa)
		mapas_atualizados.append(mapa_calculado)
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
	if houve_alteracoes:
		if salvar_mapas_atualizados(mapas_atualizados):
			print("✅ Colunas SIISP calculadas e salvas automaticamente!")
		else:
			print("❌ Erro ao salvar colunas SIISP calculadas")
	return mapas_atualizados

def obter_unidades_do_lote(lote_id):
	lotes = carregar_lotes()
	unidades = carregar_unidades()
	lote = next((l for l in lotes if l['id'] == lote_id), None)
	if not lote:
		return []
	unidades_do_lote = []
	for unidade_id in lote.get('unidades', []):
		unidade = next((u for u in unidades if u['id'] == unidade_id), None)
		if unidade:
			unidades_do_lote.append(unidade['nome'])
	return unidades_do_lote

def obter_mapas_do_lote(lote_id, mes=None, ano=None):
	mapas = carregar_mapas()
	mapas_lote = [m for m in mapas if m['lote_id'] == lote_id]
	if mes is not None:
		mapas_lote = [m for m in mapas_lote if m['mes'] == mes]
	if ano is not None:
		mapas_lote = [m for m in mapas_lote if m['ano'] == ano]
	return mapas_lote

def adicionar_usuario(dados_usuario):
	usuarios = carregar_usuarios()
	proximo_id = max([u.get('id', 0) for u in usuarios], default=0) + 1
	novo_usuario = {
		'id': proximo_id,
		'nome': dados_usuario.get('nome', '').strip(),
		'email': dados_usuario.get('email', '').strip().lower(),
		'cpf': dados_usuario.get('cpf', '').strip(),
		'telefone': dados_usuario.get('telefone', '').strip(),
		'cargo': dados_usuario.get('cargo', '').strip(),
		'unidade': dados_usuario.get('unidade', '').strip(),
		'matricula': dados_usuario.get('matricula', '').strip(),
		'usuario': dados_usuario.get('usuario', '').strip().lower(),
		'senha': dados_usuario.get('senha', '').strip(),
		'justificativa': dados_usuario.get('justificativa', '').strip(),
		'aceitar_termos': dados_usuario.get('aceitarTermos') == 'on',
		'data_cadastro': datetime.now().isoformat() + 'Z',
		'acesso': False
	}
	usuarios.append(novo_usuario)
	if salvar_usuarios(usuarios):
		return novo_usuario
	return None

def buscar_usuario_por_email_ou_usuario(identificador):
	usuarios = carregar_usuarios()
	identificador = identificador.lower().strip()
	return next((u for u in usuarios if 
				u.get('email', '').lower() == identificador or 
				u.get('usuario', '').lower() == identificador), None)

def validar_dados_unicos(dados_usuario, usuario_id=None):
	usuarios = carregar_usuarios()
	erros = []
	if usuario_id:
		usuarios = [u for u in usuarios if u.get('id') != usuario_id]
	email = dados_usuario.get('email', '').strip().lower()
	if email and any(u.get('email', '').lower() == email for u in usuarios):
		erros.append('Este email já está cadastrado no sistema!')
	cpf = dados_usuario.get('cpf', '').strip()
	if cpf and any(u.get('cpf', '').strip() == cpf for u in usuarios):
		erros.append('Este CPF já está cadastrado no sistema!')
	usuario = dados_usuario.get('usuario', '').strip().lower()
	if usuario and any(u.get('usuario', '').lower() == usuario for u in usuarios):
		erros.append('Este nome de usuário já existe! Escolha outro.')
	matricula = dados_usuario.get('matricula', '').strip()
	if matricula and any(u.get('matricula', '').strip() == matricula for u in usuarios):
		erros.append('Esta matrícula já está cadastrada no sistema!')
	telefone = dados_usuario.get('telefone', '').strip()
	if telefone and any(u.get('telefone', '').strip() == telefone for u in usuarios):
		erros.append('Este telefone já está cadastrado no sistema!')
	return erros

def atualizar_acesso_usuario(user_id, acesso):
	usuarios = carregar_usuarios()
	for usuario in usuarios:
		if usuario['id'] == user_id:
			usuario['acesso'] = acesso
			if salvar_usuarios(usuarios):
				return usuario
	return None

# 🔄 ATUALIZAÇÃO NECESSÁRIA NO BACKEND - Flask/Python

## 📋 **Mudanças na Estrutura de Dados**

Com a normalização dos arquivos JSON (separação de `lotes.json` e `unidades.json`), o backend Flask precisa ser atualizado para fazer o "join" entre os dados.

## 🛠️ **Alterações Necessárias no Flask**

### **1. Carregamento dos Dados**
```python
import json

def carregar_dados():
    # Carregar lotes
    with open('dados/lotes.json', 'r', encoding='utf-8') as f:
        lotes_data = json.load(f)
    
    # Carregar unidades
    with open('dados/unidades.json', 'r', encoding='utf-8') as f:
        unidades_data = json.load(f)
    
    return lotes_data, unidades_data

def get_unidades_por_lote(lote_id, unidades_data):
    """Retorna lista de nomes das unidades para um lote específico"""
    return [u['nome'] for u in unidades_data['unidades'] if u['lote_id'] == lote_id]
```

### **2. Rota do Dashboard**
```python
@app.route('/dashboard')
def dashboard():
    lotes_data, unidades_data = carregar_dados()
    
    # Adicionar contagem de unidades para cada lote
    for lote in lotes_data['lotes']:
        lote['unidades_count'] = len([u for u in unidades_data['unidades'] if u['lote_id'] == lote['id']])
    
    return render_template('dashboard.html', 
                         lotes=lotes_data['lotes'])
```

### **3. Rota dos Detalhes do Lote**
```python
@app.route('/lote/<int:lote_id>')
def lote_detalhes(lote_id):
    lotes_data, unidades_data = carregar_dados()
    
    # Buscar lote específico
    lote = next((l for l in lotes_data['lotes'] if l['id'] == lote_id), None)
    if not lote:
        abort(404)
    
    # Buscar unidades do lote
    unidades_lote = get_unidades_por_lote(lote_id, unidades_data)
    
    return render_template('lote-detalhes.html', 
                         lote=lote, 
                         unidades_lote=unidades_lote)
```

### **4. Rota da Lista de Lotes**
```python
@app.route('/lotes')
def lotes():
    lotes_data, unidades_data = carregar_dados()
    
    # Adicionar contagem de unidades para cada lote
    for lote in lotes_data['lotes']:
        lote['unidades_count'] = len([u for u in unidades_data['unidades'] if u['lote_id'] == lote['id']])
    
    return render_template('lotes.html', 
                         lotes=lotes_data['lotes'])
```

## 📝 **Variáveis dos Templates Atualizadas**

### **Antes (estrutura antiga):**
- `lote.unidades` → Lista de strings com nomes das unidades
- `{{ lote.unidades | length }}` → Contagem de unidades

### **Depois (estrutura nova):**
- `lote.unidades` → Lista de IDs das unidades
- `unidades_lote` → Lista de strings com nomes das unidades (passada pelo Flask)
- `{{ unidades_lote | length }}` → Contagem de unidades
- `{{ lote.unidades | length }}` → Ainda funciona para contagem (IDs)

## ✅ **Templates Atualizados**
- [x] `dashboard.html` → Mantém `{{ lote.unidades | length }}`
- [x] `lote-detalhes.html` → Usa `{{ unidades_lote }}` para nomes e `{{ unidades_lote | length }}` para contagem
- [x] `lotes.html` → Mantém `{{ lote.unidades | length }}`

## 🎯 **Benefícios da Nova Estrutura**
1. **Eliminação de duplicação** de dados
2. **Facilidade de manutenção** (alteração de nome de unidade em um só lugar)
3. **Possibilidade de expansão** (adicionar campos às unidades sem impactar lotes)
4. **Queries otimizadas** para buscar unidades por lote ou vice-versa
5. **Integridade referencial** garantida

## 🚨 **IMPORTANTE**
O sistema funcionará normalmente após essas atualizações no backend Flask. Os templates já estão preparados para a nova estrutura.
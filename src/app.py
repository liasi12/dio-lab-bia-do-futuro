import streamlit as st
import json
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Gestão Financeira - Home", page_icon="💰", layout="wide")

st.title("📊 Painel de Controle Financeiro")

# Mock dos dados caso os arquivos físicos não estejam na pasta exata durante o teste
perfil_mock = {
  "nome": "Joana Maria Da Silva",
  "idade": 45,
  "profissao": "Atendente",
  "renda_mensal": 1880.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 10000.00,
  "reserva_emergencia_atual": 300.00,
  "aceita_risco": False,
  "metas": [
    {"meta": "Completar reserva de emergência", "valor_necessario": 35000.00, "prazo": "2027-06"},
    {"meta": "Entrada do apartamento", "valor_necessario": 5000.00, "prazo": "2028-10"}
  ]
}

# Tenta carregar do arquivo original, se falhar usa o mock acima
try:
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        user_data = json.load(f)
except Exception:
    user_data = perfil_mock

# Layout em colunas para os dados do perfil
st.header(f"Bem-vinda de volta, {user_data['nome']}! 👋")
st.subheader(f"Perfil de Investimento: {user_data['perfil_investidor'].upper()}")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Renda Mensal", value=f"R$ {user_data['renda_mensal']:.2f}")
with col2:
    st.metric(label="Patrimônio Total", value=f"R$ {user_data['patrimonio_total']:.2f}")
with col3:
    st.metric(label="Reserva de Emergência Atual", value=f"R$ {user_data['reserva_emergencia_atual']:.2f}")
with col4:
    st.metric(label="Objetivo Principal", value=user_data['objetivo_principal'])

st.markdown("---")

# Seção de Transações (Baseado no exemplo da base de conhecimento)
st.subheader("📝 Últimas Transações")
transacoes_data = {
    "Data": ["01/10", "02/10", "03/10", "05/10", "07/10", "10/10"],
    "Descrição": ["Salário", "Aluguel", "Supermercado", "Streaming", "Farmácia", "Restaurante"],
    "Valor (R$)": [1800.00, -300.00, -450.00, -55.90, -89.00, -120.00]
}
df_transacoes = pd.DataFrame(transacoes_data)
st.dataframe(df_transacoes, width='stretch')

# Resumo de Gastos
total_gastos = df_transacoes[df_transacoes["Valor (R$)"] < 0]["Valor (R$)"].sum()
st.warning(f"**Total de despesas do período:** R$ {abs(total_gastos):.2f}")

st.markdown("---")

# Seção de Metas
st.subheader("🎯 Suas Metas Financeiras")
for meta in user_data['metas']:
    st.info(f"**Objetivo:** {meta['meta']} | **Valor Necessário:** R$ {meta['valor_necessario']:.2f} | **Prazo:** {meta['prazo']}")


st.markdown("---")
st.subheader("🤖 Precisa de ajuda?")
if st.button("💬 Conversar com a Lua", type="primary", use_container_width=True):
    st.switch_page("pages/Agente.py")
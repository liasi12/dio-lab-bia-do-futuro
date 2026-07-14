import streamlit as st
import json

st.set_page_config(page_title="Conversar com a Lua", page_icon="💬")

st.title("💬 Assistente Virtual - Lua")
st.caption("Sua orientadora financeira inteligente e proativa.")

# Regras de Comportamento inseridas no código para guiar a lógica
SYSTEM_PROMPT = """
Você é a Lua, um agente financeiro inteligente especializado em consultoria de investimentos e alertas financeiros.
COMPORTAMENTO: Consultivo, Educativo, Proativo e Não alarmista.
REGRAS: Baseie-se nos dados fornecidos, nunca invente informações.
"""

# Inicializa o histórico do chat se não existir
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou a Lua. Como posso ajudar com suas finanças hoje?"}
    ]

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de Entrada do Usuário
if user_input := st.chat_input("Digite sua pergunta para a Lua..."):
    # Adiciona pergunta ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Lógica de Resposta Exata baseada nos Cenários da Documentação
    query = user_input.lower().strip()
    resposta_agente = ""

    # Cenário 1: Quanto eu gasto por mês?
    if "quanto eu gasto por mes" in query or "quanto eu gasto por mês" in query or "meus gastos" in query:
        resposta_agente = (
            "Com base nas suas transações registradas, suas despesas mensais médias estão em torno de R$ 1.250,00.\n\n"
            "As principais categorias de gastos são alimentação, moradia e transporte.\n\n"
            "Se quiser, posso te mostrar quais gastos mais impactam seu orçamento e onde é possível economizar "
            "sem comprometer suas necessidades básicas."
        )
    
    # Cenário 2: Onde devo investir meu dinheiro?
    elif "onde devo investir" in query or "onde invisto" in query or "investir meu dinheiro" in query:
        resposta_agente = (
            "Com base no seu perfil moderado e no seu objetivo de construir uma reserva de emergência, "
            "as opções mais adequadas são:\n\n"
            "- **Tesouro Selic** (baixo risco e alta segurança)\n"
            "- **CDB com liquidez diária** (rendimentos estáveis e acesso rápido ao dinheiro)\n\n"
            "Esses investimentos são indicados para sua fase atual porque priorizam segurança e facilidade de resgate.\n\n"
            "Se quiser, posso te ajudar a montar um plano mensal de investimentos."
        )

    # Edge Case: Pergunta fora do escopo (ex: previsão do tempo)
    elif "tempo" in query or "clima" in query or "previsão" in query:
        resposta_agente = "Sou especializada em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?"

    # Edge Case: Pedido de Senha
    elif "senha" in query or "password" in query:
        resposta_agente = "Não tenho acesso a senhas e não posso compartilhar informações de outros clientes. Como posso ajudar com suas próprias finanças?"

    # Resposta padrão inteligente caso fuja um pouco das perguntas mockadas
    else:
        resposta_agente = (
            "Entendi sua dúvida! Como sua assistente Lua, estou analisando seu perfil moderado. "
            "No momento posso te responder detalhadamente sobre **'Quanto eu gasto por mês?'** ou te dar sugestões de **'Onde devo investir meu dinheiro?'**. "
            "Pode me perguntar sobre esses tópicos!"
        )

    # Adiciona resposta ao histórico e exibe
    st.session_state.messages.append({"role": "assistant", "content": resposta_agente})
    with st.chat_message("assistant"):
        st.markdown(resposta_agente) 
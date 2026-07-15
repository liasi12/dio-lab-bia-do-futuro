# 🌙 Projeto Lua: Saúde Financeira Inteligente e Acessível

> **"Transformando organização financeira em inclusão social e dignidade."**

Bem-vindo ao repositório oficial da **Lua**, nossa assistente virtual de finanças pessoais integrada a um painel inteligente de controle de gastos. Este projeto foi desenvolvido para democratizar o planejamento financeiro, focando em quem o mercado tradicional costuma ignorar: trabalhadores de baixa renda, autônomos e iniciantes na jornada de poupar.



## 🎯 O Problema que Resolvemos

No Brasil, milhões de pessoas que ganham até 2 salários mínimos sonham em construir uma reserva de emergência ou adquirir a casa própria, mas enfrentam três grandes barreiras:
1. **Falta de Educação Prática:** Conteúdos de finanças costumam focar em quem já tem muito dinheiro.
2. **Complexidade e Jargões:** O mercado usa termos difíceis ("financês") que geram medo e distanciamento.
3. **Ausência de Suporte:** Planilhas complexas exigem disciplina e tempo que o trabalhador do dia a dia não tem.

### Nosso Estudo de Caso: A Joana Maria da Silva
Para validar o projeto, mapeamos a realidade da Joana:
* **Renda Mensal:** R$ 1.880,00
* **Patrimônio Atual:** R$ 10.000,00
* **Grande Desafio:** Como organizar os gastos de R$ 1.250,00 e poupar com segurança para comprar seu apartamento?

---

## 🚀 A Solução: Painel Financeiro + Assistente Lua

Nesta aplicação desenvolvida em **Python** e **Streamlit**, unimos o melhor de dois mundos: um **dashboard visual direto ao ponto** e uma **IA proativa e ultra-didática**.

### ✨ Principais Funcionalidades:
* **Dashboard Inteligente:** Exibição clara de saldo, gastos recorrentes, patrimônio e o progresso das metas financeiras (como a reserva de emergência).
* **A Lua (Sua Orientadora Financeira):** Uma inteligência artificial integrada que responde dúvidas comuns em linguagem simples e humana.
* **Segurança e Ética:** Recomendações estritamente conservadoras baseadas em produtos reais e seguros (como Tesouro Selic e CDB de liquidez diária).

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando um ecossistema moderno e focado em alta performance e escalabilidade:

* **[Python](https://www.python.org/)** (Linguagem base de backend e dados)
* **[Streamlit](https://streamlit.io/)** (Framework para construção de interfaces web rápidas e interativas)
* **Pandas** (Tratamento estruturado das transações financeiras)

---

## 📂 Estrutura do Repositório (SRC)

O projeto está organizado na seguinte estrutura de arquivos e diretórios dentro do repositório:

```text
SRC/
├── data/
│   ├── historico_atendimento... # Histórico de conversas do usuário
│   ├── perfil_investidor.json   # Dados do perfil financeiro da Joana
│   ├── produtos_financeiros...  # Catálogo de investimentos seguros
│   └── transacoes.csv           # Registro de receitas e despesas
├── docs/
│   ├── 01-documentacao-a...     # Documentação da arquitetura
│   ├── 02-base-conhecimen...    # Informações para a base da IA
│   └── 03-prompts.md            # Engenharia de prompt aplicada à Lua
├── pages/
│   └── Agente.py                # Interface de conversação com a Lua (Chat)
├── app.py                       # Painel Principal do Dashboard (Streamlit)
└── requirements.txt             # Dependências de bibliotecas do projeto

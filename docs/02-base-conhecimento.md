# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Durante o desenvolvimento, os dados foram expandidos e adaptados para permitir maior realismo e funcionalidade do agente.

Principais melhorias:

Inclusão de renda extra além do salário fixo.
Estrutura de gastos por categoria (alimentação, moradia, transporte etc.).
Definição de metas financeiras com prazos.
Criação de faixas financeiras (renda, risco e saúde financeira).
Padronização de valores monetários para facilitar cálculos automáticos.

Essas adaptações permitem que o agente realize análises mais precisas e gere alertas financeiros em tempo real.]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Como os dados são carregados?

Os dados são carregados no início da execução da aplicação através de leitura local dos arquivos:

JSON → carregados via json.load()
CSV → carregados via pandas.read_csv()

Esses dados ficam disponíveis durante toda a sessão do usuário. 
Uma versão resumida dos dados é enviada ao modelo LLM (quando usado), contendo:

perfil do usuário
resumo de gastos
situação financeira atual
metas principais

Isso permite respostas mais naturais e personalizadas.]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
```
Dados do Cliente:
Nome: Joana Maria da Silva
Idade: 45 anos
Perfil: Moderado
Renda mensal: R$ 1.880
Renda extra: R$ 300
Patrimônio total: R$ 10.000
Reserva de emergência: R$ 300

Últimas Transações:
01/10: Salário — R$ 1.800
02/10: Aluguel — R$ 300
03/10: Supermercado — R$ 450
05/10: Streaming — R$ 55,90
07/10: Farmácia — R$ 89
10/10: Restaurante — R$ 120
```

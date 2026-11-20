# 📊 Documentação do Dataset (`tweets.csv`)

> ⚠️ **Aviso de Conteúdo:** Este conjunto de dados contém exemplos reais de discursos racistas e termos ofensivos coletados exclusivamente para fins acadêmicos, de pesquisa em Processamento de Linguagem Natural (NLP) e combate ao discurso de ódio.

## 📋 Dicionário de Colunas

| Coluna | Descrição | Valores |
| :--- | :--- | :--- |
| `text` | Conteúdo textual do tweet em português. | Texto livre |
| `racismo` | Rótulo de classificação manual do conteúdo. | `0` = Não racista \| `1` = Racista |
| `busca` | Origem dos dados coletados. | `1`, `2` ou `3` (ver tabela abaixo) |

---

## 🔍 Origem dos Dados (Coluna `busca`)

* **`1`** — Base acadêmica de **Fortuna et al. (2019)** (*A Hierarchically-Labeled Portuguese Hate Speech Dataset*).
* **`2`** — Base acadêmica de **Leite et al. (2020)** (*Toxic Language Detection in Social Media for Brazilian Portuguese*).
* **`3`** — Coleta direta realizada via **API do Twitter** (utilizando `Tweepy`).

---

## 🔎 Critérios de Busca na API do Twitter (`busca = 3`)

Para ampliar a base com exemplos recentes (racistas e não racistas), foram realizadas três rodadas de coleta combinando termos-alvo (sinônimos) com termos de contexto:

### Termos-alvo (Sinônimos)
* **1ª busca:** `negro`, `neguinho`, `negão`, `preto`, `raça desgraçada`, `escrava`
* **2ª busca:** `nego`, `urubuzinho`, `sub-raça`, `macaca`
* **3ª busca:** `pretinha`, `mulambo`, `macumbeira`

### Termos de Contexto (Acompanhamento)
`bandido`, `coisa de preto`, `cota vantagem`, `meritocracia`, `racismo reverso`, `povo sujo`, `não merece`, `fdp`, `drogado`, `oportunidade`, `vitimiza`, `morte`, `lixo`, `espancado`
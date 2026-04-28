# MGPEB - Simulação de Pouso de Módulos

Este projeto implementa uma simulação de pouso de módulos espaciais para a missão "Aurora Siger". O principal objetivo é demonstrar o uso de estruturas de dados (fila, pilha, listas) e algoritmos de busca e ordenação em Python.

## O que o código faz

O arquivo `mgpeb.py` contém:

- Um conjunto inicial de módulos com atributos como `nome`, `tipo`, `prioridade`, `combustivel`, `massa`, `criticidade` e `horario`.
- Uma fila de pouso (`collections.deque`) que processa cada módulo.
- Regras de autorização de pouso baseadas em:
  - combustivel mínimo
  - massa máxima
  - condições atmosféricas
  - área de pouso disponível
  - sensores operando corretamente
- Tratamento de módulos que não podem pousar:
  - módulos com pouco combustível vão para uma pilha de alertas
  - módulos bloqueados por massa, área, sensores ou clima vão para lista de espera
- Um relatório final que mostra:
  - módulos pousados
  - alertas de combustível (pilha)
  - módulos em espera
- Demonstrações de algoritmos de busca e ordenação:
  - busca linear por tipo
  - busca do módulo com menor combustível
  - busca do módulo com maior prioridade
  - busca binária por horário
  - ordenação por prioridade com Bubble Sort
  - ordenação por combustível com Selection Sort
  - ordenação por horário com Insertion Sort

## Arquivos no repositório

- `mgpeb.py`: código fonte principal da simulação.
- `RELATORIO-FASE2.pdf`: relatório do projeto.
- `README.md`: documentação e instruções de uso.
- `.gitignore`: ignora arquivos de cache do Python e outros arquivos temporários.
- `requirements.txt`: lista de dependências do projeto.

## Pré-requisitos

- Python 3.8 ou superior.

## Como executar

1. Abra um terminal na pasta do projeto.
2. Execute:

```bash
python mgpeb.py
```

3. O programa executa a simulação e exibe o relatório final no terminal.

## Como baixar do GitHub

Você pode obter o projeto de duas formas:

1. Pelo Git:

```bash
git clone <URL-do-repositório>
cd <nome-do-repositório>
python mgpeb.py
```

2. Pelo download direto:

- Acesse a página do repositório no GitHub.
- Clique em "Code" e depois em "Download ZIP".
- Extraia o arquivo ZIP e execute `python mgpeb.py` na pasta extraída.

## Observações

- Não há dependências externas adicionais além da biblioteca padrão do Python.
- Se preferir, use `python3` no lugar de `python`, dependendo da configuração do seu sistema.

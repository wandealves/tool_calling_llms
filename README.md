# Exemplos de Chamadas de LLMs com e sem Ferramentas

Este projeto demonstra diferentes maneiras de interagir com Modelos de Linguagem Grandes (LLMs), incluindo chamadas simples, chamadas com ferramentas e chamadas com execução de funções.

## Descrição

O projeto contém três scripts Python, cada um ilustrando um cenário de interação com um LLM:

- `main_chamada_sem_ferramenta.py`: Demonstra uma chamada básica para um LLM sem o uso de ferramentas.
- `main_chamada_com_ferramenta.py`: Mostra como um LLM pode ser instruído a usar uma ferramenta, mas sem executá-la.
- `main_chamada_execucao_funcao.py`: Ilustra o processo completo de um LLM utilizando uma ferramenta, executando-a e utilizando o resultado para formular a resposta final.

## Pré-requisitos

- Python 3.12 ou superior
- `uv` ou `pip` para gerenciamento de pacotes

## Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/wandealves/tool_calling_llms.git
    cd tool_calling_llms
    ```

2.  Crie um ambiente virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  Instale as dependências com `uv` ou `pip`:
    ```bash
    # Com uv
    uv pip install -e .
    ```

## Configuração

1.  Crie um arquivo `.env` na raiz do projeto. Você pode copiar o exemplo:

    ```bash
    cp .env.example .env
    ```

2.  Adicione sua chave de API da OpenAI ao arquivo `.env`:
    ```
    OPENAI_API_KEY="sua-chave-de-api-aqui"
    ```

## Uso

Para executar os scripts, utilize os seguintes comandos:

### 1. Chamada sem Ferramenta

Este script envia uma mensagem simples para o LLM e imprime a resposta.

```bash
uv run src/main_chamada_sem_ferramenta.py
```

### 2. Chamada com Ferramenta (sem execução)

Este script mostra o LLM identificando que uma ferramenta pode ser usada para responder à pergunta do usuário, mas não a executa.

```bash
uv run src/main_chamada_com_ferramenta.py
```

### 3. Chamada com Execução de Função

Este script demonstra o ciclo completo: o LLM identifica a ferramenta, o script a executa e o resultado é enviado de volta ao LLM para gerar a resposta final.

```bash
uv run src/main_chamada_execucao_funcao.py
```

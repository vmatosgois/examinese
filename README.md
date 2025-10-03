# Examine-SE

**Uma ferramenta de auxílio para formatação e análise de exames médicos.**

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC) em Medicina por Victor Matos Gois, com o objetivo de otimizar a rotina de organização de dados laboratoriais e funcionais de pacientes.

## 📄 Sobre o Projeto

O Examine-SE é uma aplicação desktop com interface gráfica desenvolvida para simplificar a visualização e o registro de exames. A ferramenta converte textos brutos de exames laboratoriais, espirometrias e dados para cálculo de função renal em tabelas organizadas e padronizadas, prontas para serem copiadas e coladas em prontuários eletrônicos ou outros documentos.

### Funcionalidades Principais

  * **Formatação de Exames Laboratoriais**: Copie e cole resultados de exames de diversas fontes. O programa identifica as datas, os nomes dos exames (mesmo com abreviações) e seus respectivos valores, organizando tudo em uma tabela cronológica.
  * **Formatação de Espirometria**: Insira os valores de uma prova de função pulmonar (pré e pós-broncodilatador) para gerar uma tabela-padrão com os principais parâmetros e cálculos de valores relativos.
  * **Cálculo de Função Renal**: Utilize a calculadora integrada para obter a Taxa de Filtração Glomerular (TFG) através da fórmula CKD-EPI 2021 e sua respectiva estratificação de risco segundo o KDIGO.
  * **Interface Intuitiva**: Interface gráfica simples, com temas claro e escuro, construída para ser ágil e de fácil utilização.

## 🛠️ Requisitos

Para executar o projeto, você precisará ter o **Python 3.8 ou superior** instalado. As seguintes bibliotecas são necessárias e podem ser instaladas a partir do arquivo `requirements.txt`.

  * `customtkinter`
  * `Pillow`
  * `pyperclip`
  * `loguru`
  * `table2ascii`
  * `datefinder`
  * `rapidfuzz`
  * `toolboxy`

### Como Instalar as Dependências

Com o Python e o pip instalados, execute o seguinte comando na pasta do projeto:

```bash
pip install -r requirements.txt
```

## 📂 Estrutura de Arquivos

O projeto está organizado nos seguintes arquivos e diretórios principais:

```
examine-se/
│
├── app.py                  # Arquivo principal que executa a interface gráfica (GUI)
├── main.py                 # Módulo com a lógica central para formatação de exames laboratoriais
├── espiro.py               # Módulo para a lógica de formatação de espirometrias
├── kdigo.py                # Módulo para os cálculos de função renal (CKD-EPI e KDIGO)
│
├── requirements.txt        # Lista de todas as dependências do Python
├── LICENSE                 # Arquivo contendo a licença completa do projeto
├── README.md               # Este arquivo de documentação
│
├── images/                 # Diretório com os ícones e imagens utilizados na interface
└── copias/                 # Diretório onde cópias de segurança dos resultados são salvas
```

## 🚀 Como Executar

1.  Clone este repositório para a sua máquina local.
2.  Navegue até o diretório do projeto pelo terminal.
3.  Instale as dependências (conforme a seção **Requisitos**).
4.  Execute o arquivo `app.py`:

<!-- end list -->

```bash
python app.py
```

## ⚖️ Licença

Este projeto está licenciado sob a **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International**.
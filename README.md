# FarmTech-Solutions

Sistema de gerenciamento inteligente para fazendas, integrando análise de dados e previsões meteorológicas para otimizar o plantio e a gestão agrícola.

## 🌱 Sobre o Projeto

O FarmTech-Solutions é uma solução completa para a gestão de fazendas modernas, combinando tecnologias Python e R para fornecer insights valiosos e automatização no processo agrícola.

## 📁 Estrutura do Projeto
FarmTech-Solutions/
 ├── Python/
 ├── main.py # Ponto de entrada da aplicação
 ├── gerenciador_fazenda.py # Gerenciamento geral da fazenda
 ├── gerenciador_plantio.py # Gerenciamento específico de plantio
 └── R/
     ├── CalculoEstatatistica.R # Análises estatísticas
  ├── api_meteorologica.R # Integração com API meteorológica

## 🚀 Funcionalidades

- 🏠 Gerenciamento de fazenda
- 🌱 Sistema de plantio inteligente
- 📊 Análises estatísticas
- ☁️ Previsão meteorológica
- 🔄 Otimização de recursos
- 📈 Monitoramento em tempo real

## 🛠️ Requisitos

### Python
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### R
- R 4.0 ou superior
- RStudio (recomendado)

### Dependências Python
```bash
pip install -r requirements.txt
```

### Dependências R
```r
install.packages(c("tidyverse", "ggplot2", "httr", "jsonlite"))
```

### 📥 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Fiap-RJ/FarmTech-Solutions.git
```

2. Instale as dependências Python:
```bash
cd FarmTech-Solutions
pip install -r requirements.txt
```

3. Instale as dependências R:
```r
# Execute no console R
install.packages(c("tidyverse", "ggplot2", "httr", "jsonlite"))
```

4. Configure as chaves de API:
- Crie um arquivo .env na raiz do projeto
- Adicione suas chaves de API necessárias

## 🚀 Uso

1. Inicie o programa:
```bash
python main.py
```

2. Menu Principal:
```bash
=== Menu Principal ===
1. Cadastrar Fazenda
2. Gerenciar Fazenda
0. Sair
```

3. Cadastrar Fazenda:
```bash
Nome da fazenda: [digite o nome]
Largura do terreno (m): [digite a largura]
Comprimento do terreno (m): [digite o comprimento]
```

4. Gerenciar Fazenda:
```bash
=== Gerenciar fazenda ===
[Lista de fazendas disponíveis]
Informe o identificador da fazenda (ou digite 'voltar' para retornar): [ID da fazenda]
```

5. Opções de Gerenciamento:
```bash
=== Opções de Gerenciamento ===
1. Alterar nome da Fazenda
2. Alterar área da Fazenda
3. Inserir dados de plantio
4. Exibir dados de plantio
5. Alterar dados de plantio
6. Remover dados de plantio
7. Remover Fazenda
0. Voltar
```

6. Exemplos de Uso:
- Cadastrar uma nova fazenda:
```bash
python main.py
1
Nome da fazenda: Fazenda São Francisco
Largura do terreno (m): 1000
Comprimento do terreno (m): 1500
```

- Gerenciar uma fazenda existente:
```bash
python main.py
2
[Lista de fazendas]
Informe o identificador da fazenda: 1
3
[Inserir dados de plantio]
```

7. Alterar dados de uma fazenda:
```bash
CopyInsert
python main.py
2
[Lista de fazendas]
Informe o identificador da fazenda: 1
1
Novo nome da fazenda: Fazenda Nova
```

##⚠️ Importante
Os dados são armazenados apenas em memória
Toda a informação é perdida ao encerrar o programa
Para manter os dados, é necessário salvar manualmente antes de fechar
Recomenda-se salvar periodicamente durante o uso